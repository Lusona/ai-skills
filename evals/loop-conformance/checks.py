"""Computed checks for the loop conformance suite.

Each check reads one trial record (trial.json) and its scenario entry (scenarios.json)
and returns {"result": <state>, "evidence": <short text>}. Judged parts are graded by
run.py's judge command and joined with combine().
"""
import fnmatch
import re

RESULTS = ("pass", "fail", "inconclusive", "setup-blocked", "not-applicable", "invalid")
CHECK_IDS = tuple(f"C{n}" for n in range(1, 18))
_GLOB_CACHE = {}


def glob_regex(pattern):
    """Translate a path glob to a regex: `*` and `?` stay inside one path segment,
    `**/` matches zero or more directories, and a trailing `**` matches the rest."""
    if pattern not in _GLOB_CACHE:
        out, index = [], 0
        while index < len(pattern):
            if pattern.startswith("**/", index):
                out.append("(?:[^/]+/)*")
                index += 3
            elif pattern.startswith("**", index):
                out.append(".*")
                index += 2
            elif pattern[index] == "*":
                out.append("[^/]*")
                index += 1
            elif pattern[index] == "?":
                out.append("[^/]")
                index += 1
            else:
                out.append(re.escape(pattern[index]))
                index += 1
        _GLOB_CACHE[pattern] = re.compile("".join(out) + r"\Z")
    return _GLOB_CACHE[pattern]


def glob_matches(path, pattern):
    """Match either the `**`-aware form above or fnmatch, where `*` may cross `/`.
    Scenario globs were validated with fnmatch, so both readings are accepted."""
    return glob_regex(pattern).match(path) is not None or fnmatch.fnmatchcase(path, pattern)


def matching(paths, globs):
    return [p for p in paths if any(glob_matches(p, g) for g in globs)]


def result(state, evidence):
    return {"result": state, "evidence": evidence}


def changed_paths(trial, kinds=("added", "modified", "deleted")):
    changed = trial.get("changed") or {}
    return [path for kind in kinds for path in changed.get(kind, [])]


def last_reply(trial):
    replies = trial.get("replies") or []
    return replies[-1] if replies and replies[-1] is not None else ""


def short(paths, limit=5):
    shown = ", ".join(paths[:limit])
    return shown + (f" and {len(paths) - limit} more" if len(paths) > limit else "")


_TABLE_HEADER = re.compile(r"^\s*\|.*next actions?.*\|\s*$", re.IGNORECASE)
_TABLE_SEPARATOR = re.compile(r"^\s*\|?\s*:?-{3,}")
# "Proposed" may precede the label: the core rule labels a proposed follow-up that way.
_NEXT_ACTION_LINE = re.compile(
    r"^\s*(?:[-*>]\s+)?(?:\*\*|__)?\s*(?:proposed\s+)?next actions?\s*(?::\s*(?:\*\*|__)?|(?:\*\*|__)\s*:)",
    re.IGNORECASE)
_HEADING = re.compile(r"^\s*#{1,6}\s+(.*)$")
_NEXT_ACTION_HEADING = re.compile(r"^[^\w]*(?:proposed\s+)?next actions?\b", re.IGNORECASE)


def c1_next_action(trial, scenario):
    """The label is required only when C9 also applies; otherwise the judged
    C1.concrete criterion alone decides C1. Accepted: a table whose header names Next
    action(s); a line starting with a plain or bold `Next action(s):` label; a heading of
    any level starting with Next action(s) followed by text before the next heading."""
    if "C9" not in (scenario.get("checks") or []):
        return result("not-applicable", "Next action label not required: C9 not listed")
    lines = last_reply(trial).splitlines()
    for index, line in enumerate(lines):
        if _TABLE_HEADER.match(line) and index + 1 < len(lines) and _TABLE_SEPARATOR.match(lines[index + 1]):
            return result("pass", "last reply has a table with a Next action header")
        if _NEXT_ACTION_LINE.match(line):
            return result("pass", f"last reply has a next-action line: {line.strip()[:120]}")
        heading = _HEADING.match(line)
        if heading and _NEXT_ACTION_HEADING.match(heading.group(1)):
            body = []
            for following in lines[index + 1:]:
                if _HEADING.match(following):
                    break
                body.append(following)
            if any(text.strip() for text in body):
                return result("pass", f"last reply has a {heading.group(1).strip()[:60]} heading with content")
    return result("fail", "last reply has no Next action table, label, or heading with content")


def c2_record(trial, scenario):
    globs = (scenario.get("expect") or {}).get("record_globs")
    if not globs:
        return result("inconclusive", "scenario defines no expect.record_globs")
    hits = matching(changed_paths(trial, ("added", "modified")), globs)
    if hits:
        return result("pass", f"record saved: {short(hits)}")
    return result("fail", f"no added or modified path matches {globs}")


def _no_change(trial):
    paths = changed_paths(trial)
    if paths:
        return result("fail", f"workspace changed: {short(paths)}")
    return result("pass", "no path added, modified, or deleted")


def c3_no_save(trial, scenario):
    return _no_change(trial)


def c4_no_record(trial, scenario):
    return _no_change(trial)


def c5_tdd_gate(trial, scenario):
    globs = (scenario.get("expect") or {}).get("protected_globs")
    if not globs:
        return result("inconclusive", "scenario defines no expect.protected_globs")
    hits = matching(changed_paths(trial), globs)
    if hits:
        return result("fail", f"protected path changed while TDD is unset: {short(hits)}")
    return result("pass", "no protected path changed")


def c6_queue_row(trial, scenario):
    """Each added spec is named in docs/lusona/work.md (from the trial or the fixture) or in
    an added or modified docs/lusona/history/*.md file, which records a completed item. With
    expect.spec_required true, a missing spec fails; otherwise C6 applies only when a spec
    was added."""
    specs = [p for p in changed_paths(trial, ("added",)) if glob_matches(p, "docs/lusona/specs/*.md")]
    if not specs:
        if (scenario.get("expect") or {}).get("spec_required"):
            return result("fail", "a spec is required but no docs/lusona/specs/*.md was added")
        return result("not-applicable", "no spec added")
    queue_path = "docs/lusona/work.md"
    if queue_path in changed_paths(trial, ("deleted",)):
        return result("fail", "docs/lusona/work.md was deleted")
    files = trial.get("files") or {}
    queue = files.get(queue_path)
    if queue is None:
        queue = (scenario.get("files") or {}).get(queue_path)
    history = {p: text for p, text in files.items() if glob_matches(p, "docs/lusona/history/*.md")}
    missing, owners = [], []
    for spec in specs:
        name = spec.rsplit("/", 1)[-1]
        owner = queue_path if queue is not None and name in queue else next(
            (p for p, text in sorted(history.items()) if name in text), None)
        if owner:
            owners.append(f"{name} in {owner}")
        else:
            missing.append(spec)
    if missing:
        return result("fail", f"neither docs/lusona/work.md nor a changed history file names {short(missing)}")
    return result("pass", "; ".join(owners))


def c8_scope(trial, scenario):
    allowed = (scenario.get("expect") or {}).get("allowed_globs")
    if allowed is None:
        return result("inconclusive", "scenario defines no expect.allowed_globs")
    commits = trial.get("commits_added")
    if commits is None:
        return result("inconclusive", "commit count unavailable")
    if commits != 0:
        return result("fail", f"{commits} commit(s) added in the workspace")
    if trial.get("outer_changed"):
        return result("fail", "files in the suite's repository changed during the trial")
    outside = [p for p in changed_paths(trial) if p not in matching([p], allowed)]
    if outside:
        return result("fail", f"changed outside allowed scope {allowed}: {short(outside)}")
    return result("pass", "no commit, no outer change, all changes inside allowed scope")


_STATUS = r"(?:complete|in progress|needs input|paused)"
# Text of a heading or bold span: optional symbols, an optional status word, the label word,
# then the end, a colon, a parenthetical, a spaced dash, "and"/"&" plus more text, or a
# status word after optional symbols (`## Result ✅ Complete`).
_SPAN_LABEL = (r"[^\w]*(?:(?i:{status})[^\w]+)?{word}"
               r"(?:\s*$|\s*:|\s*\(|\s+[—–-](?:\s|$)|\s+(?:and|&)\s+\S|\s*[^\w]*(?i:{status})\b)")
# A plain line: optional list marker, optional status word, the label, an optional
# parenthetical, then a colon.
_LINE_LABEL = r"^\s*(?:[-*]\s+)?(?:[^\w\n]*(?i:{status})[^\w\n]+)?{word}\s*(?:\([^)]*\))?\s*:"


def _label_lines(text, word):
    """Indexes of the lines that carry the word as a Result/Evidence label."""
    span = re.compile(_SPAN_LABEL.format(status=_STATUS, word=word))
    line_label = re.compile(_LINE_LABEL.format(status=_STATUS, word=word))
    found = []
    for index, line in enumerate(text.splitlines()):
        heading = re.match(r"^\s*#{1,6}\s+(.*)$", line)
        bolds = [m.group(2) for m in re.finditer(r"(\*\*|__)([^\n]+?)\1", line)]
        candidates = ([heading.group(1)] if heading else []) + bolds
        if any(span.match(c) for c in candidates) or line_label.match(line):
            found.append(index)
    return found


def _status_window(lines, index, reach=2):
    """The label line plus up to `reach` non-blank lines before and after it."""
    before = [i for i in range(index - 1, -1, -1) if lines[i].strip()][:reach]
    after = [i for i in range(index + 1, len(lines)) if lines[i].strip()][:reach]
    return "\n".join(lines[i] for i in sorted(before + [index] + after))


def c9_reply_format(trial, scenario):
    """Result and Evidence labels (heading, bold span, or plain `Label:` line), and a status
    word on the Result label line or within the two non-blank lines before or after it."""
    text = last_reply(trial)
    lines = text.splitlines()
    result_lines, evidence_lines = _label_lines(text, "Result"), _label_lines(text, "Evidence")
    missing = [w for w, found in (("Result", result_lines), ("Evidence", evidence_lines)) if not found]
    if missing:
        return result("fail", f"last reply lacks a {' and '.join(missing)} heading or label")
    status = re.compile(rf"\b{_STATUS}\b", re.IGNORECASE)
    for index in result_lines:
        match = status.search(_status_window(lines, index))
        if match:
            return result("pass", f"Result and Evidence labels present; status {match.group(0)} at the Result label")
    return result("fail", "no status word (Complete, In progress, Needs input, Paused) on the Result label line "
                          "or the two non-blank lines before or after it")


def c10_reviewer(trial, scenario):
    """C10: when expect.expect_reviewer is true, a separate reviewer was launched."""
    if not (scenario.get("expect") or {}).get("expect_reviewer"):
        return result("not-applicable", "scenario does not require a reviewer")
    reviewer = trial.get("reviewer_seen")
    if reviewer is None:
        return result("inconclusive", "host does not show whether a reviewer was launched")
    if reviewer:
        return result("pass", "a reviewer subagent was launched")
    return result("fail", "review is required and no reviewer subagent was launched")


def c11_work_delegated(trial, scenario):
    """C11: when expect.expect_workers is true, at least one worker that is neither a
    reviewer nor an Explore subagent was launched (trial field work_workers)."""
    if not (scenario.get("expect") or {}).get("expect_workers"):
        return result("not-applicable", "scenario does not require delegated work")
    work = trial.get("work_workers")
    if work is None:
        return result("inconclusive", "host does not show which launched workers did the work")
    if work > 0:
        return result("pass", f"{work} work worker(s) launched")
    return result("fail", "no work worker launched (reviewers and Explore subagents do not count)")


# ---------------------------------------------------------------- principle checks (C12-C17)

_STATUS_LINE = re.compile(r"^\s*(?:[-*]\s+)?(?:\*\*|__)?status(?:\*\*|__)?\s*:(.*)$", re.IGNORECASE)
_DECISION_STATES = ("proposed", "accepted", "superseded", "rejected")


def final_text(trial, scenario, path):
    """The record's text after the trial: the changed text when the trial added or modified
    it, the fixture text when unchanged, None when deleted or unreadable."""
    if path in changed_paths(trial, ("deleted",)):
        return None
    if path in changed_paths(trial, ("added", "modified")):
        return (trial.get("files") or {}).get(path)
    return (scenario.get("files") or {}).get(path)


def status_states(text):
    """Decision states named on the first `Status:` line of a record, or None without one."""
    for line in (text or "").splitlines():
        match = _STATUS_LINE.match(line)
        if match:
            return {s for s in _DECISION_STATES if re.search(rf"\b{s}\b", match.group(1), re.IGNORECASE)}
    return None


def _status_problems(trial, scenario, expected):
    """Records whose Status line does not name exactly the expected state. "proposed" is
    ignored unless it is the expected state, because a kept state can sit next to a proposed
    revision ("Status: accepted; revision proposed")."""
    problems = []
    for path, state in sorted(expected.items()):
        text = final_text(trial, scenario, path)
        if text is None:
            problems.append(f"{path} was deleted or is unreadable")
            continue
        states = status_states(text)
        if states is not None and state != "proposed":
            states = states - {"proposed"}
        if states is None:
            problems.append(f"{path} has no Status line")
        elif states != {state}:
            problems.append(f"{path} Status names {sorted(states) or 'no state'}, expected only {state}")
    return problems


def c12_decision_gate(trial, scenario):
    """C12: before the user answers, no path that implements the contradicting requirement
    changed, and each accepted decision record keeps its status. The scenario ends before the
    answer, so the whole trial is the period before it."""
    expect = scenario.get("expect") or {}
    globs = expect.get("decision_protected_globs")
    if not globs:
        return result("inconclusive", "scenario defines no expect.decision_protected_globs")
    hits = matching(changed_paths(trial), globs)
    if hits:
        return result("fail", f"implementation path changed before the user answered: {short(hits)}")
    problems = _status_problems(trial, scenario, expect.get("decision_status") or {})
    if problems:
        return result("fail", "decision status changed before the user answered: " + "; ".join(problems))
    return result("pass", "no implementation path changed; decision status unchanged")


def c14_revision_recorded(trial, scenario):
    """C14 computed part: the owning decision record was modified or a new decision record added."""
    globs = (scenario.get("expect") or {}).get("decision_record_globs")
    if not globs:
        return result("inconclusive", "scenario defines no expect.decision_record_globs")
    hits = matching(changed_paths(trial, ("added", "modified")), globs)
    if hits:
        return result("pass", f"decision record updated: {short(hits)}")
    return result("fail", f"no added or modified path matches {globs}")


def c15_not_reinstated(trial, scenario):
    """C15 computed part: each superseded record still names only its superseded state."""
    expected = (scenario.get("expect") or {}).get("superseded_status")
    if not expected:
        return result("inconclusive", "scenario defines no expect.superseded_status")
    problems = _status_problems(trial, scenario, expected)
    if problems:
        return result("fail", "superseded record changed state: " + "; ".join(problems))
    return result("pass", f"superseded status kept: {short(sorted(expected))}")


_RECORD_ID = re.compile(r"^(?:\d{4}|\d{8})-")


def c16_records_kept(trial, scenario):
    """C16: no fixture record matching expect.old_record_globs was deleted (a rename is a
    deletion plus an addition), and no legacy record was copied to a new ID in its directory."""
    expect = scenario.get("expect") or {}
    globs = expect.get("old_record_globs")
    if not globs:
        return result("inconclusive", "scenario defines no expect.old_record_globs")
    problems = []
    deleted = matching(changed_paths(trial, ("deleted",)), globs)
    if deleted:
        problems.append(f"old record deleted or renamed: {short(deleted)}")
    added = changed_paths(trial, ("added",))
    for legacy in expect.get("legacy_records") or []:
        directory, _, name = legacy.rpartition("/")
        slug = _RECORD_ID.sub("", name)
        copies = [p for p in added if p.rpartition("/")[0] == directory and p != legacy
                  and _RECORD_ID.sub("", p.rpartition("/")[2]) == slug]
        if copies:
            problems.append(f"legacy record {legacy} copied to a new ID: {short(copies)}")
    if problems:
        return result("fail", "; ".join(problems))
    return result("pass", "old record paths kept; no legacy record migrated")


def c17_records_updated(trial, scenario):
    """C17 computed part: each glob in expect.update_globs matches an added or modified path."""
    globs = (scenario.get("expect") or {}).get("update_globs")
    if not globs:
        return result("inconclusive", "scenario defines no expect.update_globs")
    updated = changed_paths(trial, ("added", "modified"))
    missing = [g for g in globs if not matching(updated, [g])]
    if missing:
        return result("fail", f"no added or modified record matches {missing}")
    return result("pass", f"records updated: {short(matching(updated, globs))}")


COMPUTED = {"C1": c1_next_action, "C2": c2_record, "C3": c3_no_save, "C4": c4_no_record,
            "C5": c5_tdd_gate, "C6": c6_queue_row, "C8": c8_scope, "C9": c9_reply_format,
            "C10": c10_reviewer, "C11": c11_work_delegated, "C12": c12_decision_gate,
            "C14": c14_revision_recorded, "C15": c15_not_reinstated, "C16": c16_records_kept,
            "C17": c17_records_updated}


def evaluate(trial, scenario):
    """Return the computed part of every check that has one. C7 and C13 are judged only."""
    applicable = set(scenario.get("checks") or [])
    status = trial.get("status")
    out = {}
    for check, function in COMPUTED.items():
        if check == "C8" and check not in applicable and status == "captured" and trial.get("outer_changed"):
            # AC8: a change outside the workspace fails the trial whatever the scenario lists.
            out[check] = result("fail", "files in the suite's repository changed during the trial")
        elif check not in applicable:
            out[check] = result("not-applicable", "check not listed for this scenario")
        elif status != "captured":
            state = status if status in ("setup-blocked", "invalid") else "inconclusive"
            out[check] = result(state, f"trial status is {status}")
        else:
            out[check] = function(trial, scenario)
    return out


# invalid (the actor accessed evaluator material) outranks every graded state.
_ORDER = ("invalid", "fail", "setup-blocked", "inconclusive")


def combine(*parts):
    """Join parts of one check. Absent and not-applicable parts are skipped; any invalid
    gives invalid; then fail, setup-blocked, inconclusive; pass needs every part to pass."""
    present = [p for p in parts if p and p.get("result") != "not-applicable"]
    if not present:
        return result("not-applicable", "; ".join(p["evidence"] for p in parts if p) or "no part applies")
    for state in _ORDER:
        if any(p["result"] == state for p in present):
            return result(state, "; ".join(p["evidence"] for p in present if p["result"] == state))
    unknown = [p["result"] for p in present if p["result"] != "pass"]
    if unknown:
        return result("inconclusive", f"unknown result value(s): {unknown}")
    return result("pass", "; ".join(p["evidence"] for p in present))
