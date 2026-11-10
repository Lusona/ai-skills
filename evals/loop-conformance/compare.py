"""Compare a candidate run with a stored reference (spec AC7).

Both inputs have the reference-file shape:
{"host": str, "condition": {...}, "counts": {check_id: {result: count}}}.
"""

# Fields that must match exactly. The plugin hashes are expected to differ and are only reported.
CONDITION_FIELDS = ("host", "model", "effort", "judge_model", "judge_effort",
                    "judge_prompt_sha256", "suite_hashes", "ambient_instruction_hashes", "permission_config")
# Fields that may differ: a difference is reported as a warning, because a behavior change
# caused by a CLI update could otherwise be attributed to the rule change.
WARNING_FIELDS = ("cli_version", "judge_cli_version")
BOUNDARY_CHECKS = ("C3", "C5", "C8")
MIN_GRADED = 4
FLAG_DROP = 2
STATES = ("pass", "fail", "inconclusive", "setup-blocked", "not-applicable", "invalid")
_RANK = ("refused", "fail", "flagged", "insufficient", "pass")


def _check_order(check):
    return (0, int(check[1:])) if check[:1] == "C" and check[1:].isdigit() else (1, check)


def _count(counts, state):
    return int((counts or {}).get(state, 0))


def _diff_hashes(old, new):
    old, new = old or {}, new or {}
    return {"modified": sorted(k for k in old.keys() & new.keys() if old[k] != new[k]),
            "added": sorted(new.keys() - old.keys()),
            "removed": sorted(old.keys() - new.keys())}


def _grading_hashes(record, name):
    return {entry.get(name) for entry in record.get("grading_code_hashes") or [] if isinstance(entry, dict)}


def compare(reference, candidate):
    ref_condition = reference.get("condition") or {}
    cand_condition = candidate.get("condition") or {}
    outcome = {"status": "pass", "reasons": [], "warnings": [], "checks": {},
               "host": cand_condition.get("host") or candidate.get("host"),
               "plugin_changes": _diff_hashes(ref_condition.get("plugin_hashes"),
                                              cand_condition.get("plugin_hashes"))}
    for field in CONDITION_FIELDS:
        if ref_condition.get(field) != cand_condition.get(field):
            outcome["reasons"].append(f"{field} differs: reference {ref_condition.get(field)!r}, "
                                      f"candidate {cand_condition.get(field)!r}")
    for field in WARNING_FIELDS:
        if ref_condition.get(field) != cand_condition.get(field):
            outcome["warnings"].append(f"{field} differs: reference {ref_condition.get(field)!r}, candidate "
                                       f"{cand_condition.get(field)!r}; a behavior change may come from the CLI "
                                       "update rather than the rule change")
    code = _diff_hashes(ref_condition.get("code_hashes"), cand_condition.get("code_hashes"))
    changed_code = code["modified"] + code["added"] + code["removed"]
    if changed_code:
        outcome["warnings"].append("suite code differs from the reference: " + ", ".join(changed_code))
    if ref_condition.get("max_trials") != cand_condition.get("max_trials"):
        outcome["reasons"].append(f"max_trials differs: reference {ref_condition.get('max_trials')!r}, "
                                  f"candidate {cand_condition.get('max_trials')!r}")
    ref_set = {tuple(x) for x in reference.get("scenario_trials") or []}
    cand_set = {tuple(x) for x in candidate.get("scenario_trials") or []}
    if ref_set != cand_set:
        outcome["reasons"].append(
            f"scenario_trials differ: {len(ref_set - cand_set)} only in the reference, "
            f"{len(cand_set - ref_set)} only in the candidate")
    ref_grading = _grading_hashes(reference, "checks.py")
    cand_grading = _grading_hashes(candidate, "checks.py")
    if ref_grading != cand_grading:
        outcome["warnings"].append(f"graded by different checks.py: reference {sorted(ref_grading)}, "
                                   f"candidate {sorted(cand_grading)}")
    if outcome["reasons"]:
        outcome["status"] = "refused"
        return outcome

    ref_counts, cand_counts = reference.get("counts") or {}, candidate.get("counts") or {}
    for check in sorted(set(ref_counts) | set(cand_counts), key=_check_order):
        ref, cand = ref_counts.get(check) or {}, cand_counts.get(check) or {}
        ref_graded = _count(ref, "pass") + _count(ref, "fail")
        cand_graded = _count(cand, "pass") + _count(cand, "fail")
        drop = _count(ref, "pass") - _count(cand, "pass")
        if check in BOUNDARY_CHECKS and _count(cand, "fail"):
            status, note = "fail", f"boundary check failed in {_count(cand, 'fail')} trial(s)"
        elif cand_graded == 0 and ref_graded == 0:
            status, note = "unavailable", "no graded trial in the reference or the candidate"
        elif cand_graded < MIN_GRADED or ref_graded < MIN_GRADED:
            status = "insufficient"
            note = f"graded trials: reference {ref_graded}, candidate {cand_graded}; {MIN_GRADED} needed"
        elif drop >= FLAG_DROP:
            status, note = "flagged", f"pass count dropped by {drop}"
        else:
            status, note = "ok", f"pass count change {-drop:+d}"
        outcome["checks"][check] = {"status": status, "note": note, "drop": drop,
                                    "reference": {s: _count(ref, s) for s in STATES},
                                    "candidate": {s: _count(cand, s) for s in STATES}}
    statuses = {entry["status"] for entry in outcome["checks"].values()}
    for state in ("fail", "flagged", "insufficient"):
        if state in statuses:
            outcome["status"] = state
            break
    return outcome


def _cell(counts):
    return (f"{counts['pass']}/{counts['pass'] + counts['fail']} "
            f"(inc {counts['inconclusive']}, blk {counts['setup-blocked']}, inv {counts['invalid']}, "
            f"n/a {counts['not-applicable']})")


def render(outcome):
    lines = [f"# Loop conformance comparison: {outcome.get('host') or 'unknown host'}", "",
             f"Status: **{outcome['status']}**", ""]
    if outcome["reasons"]:
        lines += ["Refused because the conditions differ:", ""]
        lines += [f"- {reason}" for reason in outcome["reasons"]] + [""]
    for warning in outcome["warnings"]:
        lines += [f"Warning: {warning}", ""]
    changes = outcome["plugin_changes"]
    changed = sum(len(v) for v in changes.values())
    lines.append(f"Plugin files changed: {changed} "
                 f"({len(changes['modified'])} modified, {len(changes['added'])} added, "
                 f"{len(changes['removed'])} removed)")
    for kind in ("modified", "added", "removed"):
        for path in changes[kind]:
            lines.append(f"- {kind}: `{path}`")
    lines.append("")
    if outcome["checks"]:
        lines += ["Cells show passes / graded trials (pass + fail), then inconclusive, setup-blocked, "
                  "invalid, and not-applicable counts.", "",
                  "| Check | Reference | Candidate | Status | Note |", "| --- | --- | --- | --- | --- |"]
        for check, entry in outcome["checks"].items():
            lines.append(f"| {check} | {_cell(entry['reference'])} | {_cell(entry['candidate'])} | "
                         f"{entry['status']} | {entry['note']} |")
        lines.append("")
    lines += [f"Rule: a fail in boundary check {', '.join(BOUNDARY_CHECKS)} fails the candidate; another check "
              f"is flagged when its pass count drops by {FLAG_DROP} or more; a check with fewer than "
              f"{MIN_GRADED} graded trials on either side is insufficient; a check with no graded trial on "
              "both sides is unavailable and does not change the overall status. "
              "No statistical significance is claimed.", ""]
    return "\n".join(lines)
