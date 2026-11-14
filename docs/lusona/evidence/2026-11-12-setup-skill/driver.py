#!/usr/bin/env python3
"""Driver for the setup-skill behavioral trials (spec 20261112-add-setup-skill, T4).

Usage, from the repository root:
    python3 -B docs/lusona/evidence/2026-11-12-setup-skill/driver.py run TRIAL [--revision N]
    python3 -B docs/lusona/evidence/2026-11-12-setup-skill/driver.py grade TRIAL
    python3 -B docs/lusona/evidence/2026-11-12-setup-skill/driver.py ledger

TRIAL is <case>-t<n>, for example C1-t1 or X1-t1. Inputs come from cases.json; the design is
checked against design.lock.json before a trial starts. Host invocation, environment and
stream parsing are imported from evals/loop-conformance/run.py, which is not modified.
"""
import argparse
import datetime
import fcntl
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import time
import uuid

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRATCH = ROOT / "tmp" / "setup-skill-t4"
PLUGIN = SCRATCH / "candidate"
PLUGIN_V1 = PLUGIN
PLUGIN_V2 = SCRATCH / "candidate-v2"  # Amendment 2
PLUGIN_V3 = SCRATCH / "candidate-v3"  # Amendment 3
PLUGIN_V4 = SCRATCH / "candidate-v4"  # Amendment 4
LEDGER = SCRATCH / "ledger.json"
RAW = SCRATCH / "raw"
TRIALS = HERE / "trials"
BUDGET_USD = 25.0
RESERVE_USD = 4.0
# Amendment 4 gate: its own 5.00 USD cap, a 1.00 USD reserve per trial, cost counted from this ledger total.
A4_BASE_USD, A4_CAP_USD, A4_RESERVE_USD = 7.535545, 5.0, 1.0
TIMEOUT = 1200
CLAUDE_MODEL, CLAUDE_EFFORT = "claude-opus-5-5", "high"
CODEX_MODEL, CODEX_EFFORT = "gpt-6.1-sol", "medium"
AUTHOR = ("Trial", "trial@example.invalid")

_spec = importlib.util.spec_from_file_location("loop_run", ROOT / "evals" / "loop-conformance" / "run.py")
run_py = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(run_py)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def amendment_text(n):
    """README text from the line `## Amendment n` up to the line `### Amendment n results`."""
    text = (HERE / "README.md").read_bytes()
    start = text.index(f"\n## Amendment {n}\n".encode()) + 1
    end = text.find(f"\n### Amendment {n} results\n".encode(), start)
    return text[start:] if end < 0 else text[start:end]


def amendment_1_text():
    return amendment_text(1)


def check_lock():
    # Original lock: cases.json as it was before Amendment 1 is kept as cases.v1.json.
    lock = json.loads((HERE / "design.lock.json").read_text())
    for name, expected in lock["files"].items():
        data = (HERE / ("cases.v1.json" if name == "cases.json" else name)).read_bytes()
        if name == "README.md":
            data = data.split(b"\n## Results\n", 1)[0]
            if not data.endswith(b"\n"):
                data += b"\n"
        if sha(data) != expected:
            raise SystemExit(f"{name} differs from design.lock.json; the design is frozen")
    # Amendment 1 lock: cases.json as it was before Amendment 2 is kept as cases.v2.json.
    amended = HERE / "design.lock.amendment-1.json"
    if amended.exists():
        lock = json.loads(amended.read_text())
        current = {"cases.json": (HERE / "cases.v2.json").read_bytes(),
                   "candidate.sha256": (HERE / "candidate.sha256").read_bytes(),
                   "README.md#amendment-1": amendment_text(1)}
        for name, expected in lock["files"].items():
            if sha(current[name]) != expected:
                raise SystemExit(f"{name} differs from design.lock.amendment-1.json")
    # Amendment 2 lock: cases.json as it was before Amendment 3 is kept as cases.v3.json.
    amended = HERE / "design.lock.amendment-2.json"
    if amended.exists():
        lock = json.loads(amended.read_text())
        current = {"cases.json": (HERE / "cases.v3.json").read_bytes(),
                   "candidate.sha256": (HERE / "candidate.sha256").read_bytes(),
                   "candidate.v2.sha256": (HERE / "candidate.v2.sha256").read_bytes(),
                   "README.md#amendment-2": amendment_text(2)}
        for name, expected in lock["files"].items():
            if sha(current[name]) != expected:
                raise SystemExit(f"{name} differs from design.lock.amendment-2.json")
    # Amendment 3 lock: cases.json as it was before Amendment 4 is kept as cases.v4.json.
    amended = HERE / "design.lock.amendment-3.json"
    if amended.exists():
        lock = json.loads(amended.read_text())
        current = {"cases.json": (HERE / "cases.v4.json").read_bytes(),
                   "candidate.v3.sha256": (HERE / "candidate.v3.sha256").read_bytes(),
                   "README.md#amendment-3": amendment_text(3)}
        for name, expected in lock["files"].items():
            if sha(current[name]) != expected:
                raise SystemExit(f"{name} differs from design.lock.amendment-3.json")
    amended = HERE / "design.lock.amendment-4.json"
    if amended.exists():
        lock = json.loads(amended.read_text())
        current = {"cases.json": (HERE / "cases.json").read_bytes(),
                   "candidate.v4.sha256": (HERE / "candidate.v4.sha256").read_bytes(),
                   "README.md#amendment-4": amendment_text(4)}
        for name, expected in lock["files"].items():
            if sha(current[name]) != expected:
                raise SystemExit(f"{name} differs from design.lock.amendment-4.json")
    for hashes, root in (("candidate.sha256", PLUGIN_V1), ("candidate.v2.sha256", PLUGIN_V2),
                         ("candidate.v3.sha256", PLUGIN_V3), ("candidate.v4.sha256", PLUGIN_V4)):
        if not (HERE / hashes).exists():
            continue
        for line in (HERE / hashes).read_text().splitlines():
            digest, name = line.split("  ", 1)
            if sha((root / name).read_bytes()) != digest:
                raise SystemExit(f"frozen plugin file {name} changed ({hashes})")


def cases():
    return json.loads((HERE / "cases.json").read_text())


def resolve_case(case_id, trial_number=None):
    data = cases()
    case = dict(data[case_id])
    override = (case.pop("trial_overrides", None) or {}).get(str(trial_number))
    if override:
        case.update(override)
    host = case.get("host", "claude")
    if "same_as" in case:
        base = dict(data[case["same_as"]])
        base.update({k: v for k, v in case.items() if k != "same_as"})
        base["base_case"] = case["same_as"]
        case = base
    case["host"] = host
    case["id"] = case_id
    return case


# ------------------------------------------------------------------ ledger

def ledger_update(fn):
    SCRATCH.mkdir(parents=True, exist_ok=True)
    with open(SCRATCH / "ledger.lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        data = json.loads(LEDGER.read_text()) if LEDGER.exists() else {"sessions": {}, "in_flight": []}
        result = fn(data)
        LEDGER.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
        return result


def spent(data):
    return sum(v.get("cost_usd") or 0 for v in data["sessions"].values())


def start_gate(trial):
    def fn(data):
        others = [t for t in data["in_flight"] if t != trial]
        remaining = BUDGET_USD - spent(data) - RESERVE_USD * len(others)
        if remaining < RESERVE_USD:
            return False, remaining
        if trial not in data["in_flight"]:
            data["in_flight"].append(trial)
        return True, remaining
    return ledger_update(fn)


def start_gate_a4(trial):
    def fn(data):
        others = [t for t in data["in_flight"] if t != trial]
        total = spent(data)
        remaining = A4_CAP_USD - (total - A4_BASE_USD) - A4_RESERVE_USD * len(others)
        if remaining < A4_RESERVE_USD or total + A4_RESERVE_USD > BUDGET_USD:
            return False, remaining
        if trial not in data["in_flight"]:
            data["in_flight"].append(trial)
        return True, remaining
    return ledger_update(fn)


def record_cost(trial, session, cost, unknown=False):
    def fn(data):
        entry = data["sessions"].setdefault(session or f"{trial}-unknown-{uuid.uuid4().hex[:6]}",
                                            {"trial": trial})
        if cost is not None:
            entry["cost_usd"] = cost  # total_cost_usd is cumulative per session
        if unknown:
            entry["unknown_turns"] = entry.get("unknown_turns", 0) + 1
        return spent(data)
    return ledger_update(fn)


def finish(trial):
    def fn(data):
        data["in_flight"] = [t for t in data["in_flight"] if t != trial]
    ledger_update(fn)


# ------------------------------------------------------------------ workspace

TEXT_KEEP = re.compile(r"^(AGENTS\.md|CLAUDE\.md|docs/.*)$")


def snapshot(workspace):
    workspace = pathlib.Path(workspace)
    entries = {}
    for dirpath, dirnames, filenames in os.walk(workspace):
        rel_dir = pathlib.Path(dirpath).relative_to(workspace)
        dirnames[:] = sorted(d for d in dirnames if not (rel_dir == pathlib.Path(".") and d == ".git")
                             and d not in ("__pycache__",))
        for name in sorted(dirnames + filenames):
            path = pathlib.Path(dirpath) / name
            rel = path.relative_to(workspace).as_posix()
            st = os.lstat(path)
            if os.path.islink(path):
                entries[rel] = {"type": "symlink", "target": os.readlink(path)}
            elif path.is_dir():
                entries[rel] = {"type": "dir"}
            else:
                data = path.read_bytes()
                entry = {"type": "file", "sha256": sha(data), "size": st.st_size}
                if TEXT_KEEP.match(rel):
                    entry["text"] = data.decode("utf-8", errors="replace")
                entries[rel] = entry
    return {"entries": entries, "commits": run_py.commit_count(workspace)}


def git(workspace, *args):
    return subprocess.run(["git", "-C", str(workspace), *args], capture_output=True, text=True, check=True)


def prepare_workspace(case, trial):
    work_root = run_py.check_work_root(run_py.default_work_root())
    work_root.mkdir(parents=True, exist_ok=True)
    workspace = work_root / f"setup-{trial}-{uuid.uuid4().hex[:8]}"
    workspace.mkdir()
    git(workspace, "init", "--quiet")
    for key, value in (("user.name", AUTHOR[0]), ("user.email", AUTHOR[1]), ("commit.gpgsign", "false")):
        git(workspace, "config", key, value)
    files = dict(case["fixture"])
    source = None
    if case.get("fixture_from") or case.get("fixture_from_order"):
        order = case.get("fixture_from_order") or [case["fixture_from"]["trial"]]
        paths = (case.get("fixture_from") or resolve_case("C4")["fixture_from"])["paths"]
        for candidate in order:
            path = TRIALS / candidate / "trial.json"
            if not path.exists():
                continue
            final = json.loads(path.read_text())["snapshots"][-1]["entries"]
            if all(final.get(p, {}).get("type") == "file" for p in paths):
                source = candidate
                for p in paths:
                    files[p] = final[p]["text"]
                break
        if source is None:
            raise RuntimeError(f"no source end state with {paths} among {order}")
        if not re.search(r"^\s*-\s*TDD:", files["AGENTS.md"], re.M):
            raise RuntimeError(f"source end state {source} has no TDD: line in AGENTS.md")
    for name, content in files.items():
        target = workspace / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, dict):
            os.symlink(content["symlink"], target)
        else:
            target.write_bytes(content.encode("utf-8"))
    git(workspace, "add", "-A")
    git(workspace, "commit", "--quiet", "--no-verify", "-m", "Fixture")
    return workspace, source


# ------------------------------------------------------------------ hosts

def condition(host):
    if host == "claude":
        return {"host": "claude", "plugin_path": str(PLUGIN), "model": CLAUDE_MODEL, "effort": CLAUDE_EFFORT,
                "claude_settings": run_py.CLAUDE_SETTINGS, "allowed_tools": run_py.claude_allowed_tools(),
                "timeout_seconds": TIMEOUT}
    return {"host": "codex", "plugin_path": str(PLUGIN), "model": CODEX_MODEL, "effort": CODEX_EFFORT,
            "timeout_seconds": TIMEOUT}


def turn_text(host, skill, index, text):
    if index == 1 and host == "claude":
        return f"/lusona:{skill} {text}\n"
    if index == 1:
        return run_py.codex_prefix(str(PLUGIN), skill) + text + "\n"
    return text + "\n"


def run_turn(cond, workspace, prompt, session, raw_stem):
    host = cond["host"]
    args = run_py.claude_command(cond, session) if host == "claude" else run_py.codex_command(cond, workspace, session)
    env, removed = run_py.actor_env()
    if host == "claude":
        env.update(run_py.CLAUDE_SHELL_ENV)
    record = {"command": args, "resumed_session": session, "removed_env": removed, "status": "setup-blocked",
              "started_at": now()}
    stdout = stderr = ""
    started = time.monotonic()
    try:
        proc = run_py.execute(args, input=prompt, text=True, capture_output=True, cwd=workspace,
                              timeout=TIMEOUT, env=env)
        stdout, stderr = proc.stdout or "", proc.stderr or ""
        record["exit_code"] = proc.returncode
        if host == "claude":
            parsed = run_py.parse_claude(stdout, str(PLUGIN))
            record["session"] = parsed["session"]
            if not parsed["init_seen"]:
                record["error"] = "no init event"
            elif not parsed["plugin_ok"]:
                record["error"] = f"lusona plugin paths {parsed['plugin_paths']} are not exactly the frozen plugin"
            elif parsed["init_model"] != cond["model"]:
                record["error"] = f"init model {parsed['init_model']!r}"
            elif proc.returncode == 0 and parsed["result_ok"] and parsed["reply"] is not None:
                record["status"] = "captured"
            else:
                record["status"] = "inconclusive"
                record["error"] = "no successful result"
            record.update({k: parsed[k] for k in ("reply", "texts", "usage", "cost_usd", "turn_cost_usd",
                                                  "tool_calls", "denied_actions", "workers", "plugin_paths")})
            init = parsed.get("init") or {}
            record["init"] = {k: init.get(k) for k in ("model", "permissionMode", "claude_code_version",
                                                       "memory_paths", "plugins", "cwd")}
        else:
            parsed = run_py.parse_codex(stdout)
            record["session"] = parsed["session"] or session
            if not parsed["session"]:
                record["error"] = "no thread.started event"
            elif proc.returncode == 0 and parsed["completed"] and not parsed["failed"] and parsed["reply"]:
                record["status"] = "captured"
            else:
                record["status"] = "inconclusive"
                record["error"] = f"turn did not complete: {parsed['failed']}"
            record.update({k: parsed[k] for k in ("reply", "texts", "usage", "item_types", "denied_actions")})
    except subprocess.TimeoutExpired as error:
        stdout, stderr = error.stdout or "", error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        record["status"] = "inconclusive"
        record["error"] = f"timeout after {TIMEOUT} s"
    except OSError as error:
        record["error"] = f"launch failed: {error}"
    finally:
        record["elapsed_seconds"] = round(time.monotonic() - started, 1)
        raw_stem.parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path(f"{raw_stem}.stdout.jsonl").write_text(stdout)
        pathlib.Path(f"{raw_stem}.stderr.txt").write_text(stderr)
    return record


# ------------------------------------------------------------------ redaction and saving

def redactor(workspace):
    pairs = []
    for real, label in ((workspace, "<workspace>"), (PLUGIN, "<plugin>"), (ROOT, "<repository>"),
                        (pathlib.Path.home(), "~")):
        for form in {str(real), str(pathlib.Path(real).resolve())}:
            pairs.append((form, label))
    # Claude Code names its per-project directory after the path with "/" replaced by "-".
    pairs.append((str(pathlib.Path.home()).replace("/", "-") + "-", "-<home>-"))
    pairs.sort(key=lambda p: -len(p[0]))

    def redact(value):
        if isinstance(value, str):
            for real, label in pairs:
                value = value.replace(real, label)
            return value
        if isinstance(value, list):
            return [redact(v) for v in value]
        if isinstance(value, dict):
            return {redact(k): redact(v) for k, v in value.items()}
        return value
    return redact


def save_trial(trial_dir, data, workspace):
    redact = redactor(workspace)
    trial_dir.mkdir(parents=True, exist_ok=True)
    (trial_dir / "trial.json").write_text(json.dumps(redact(data), indent=2, sort_keys=True) + "\n")


def save_final(trial_dir, workspace, snap):
    final = trial_dir / "final"
    if final.exists():
        shutil.rmtree(final)
    for rel, entry in snap["entries"].items():
        if rel in ("AGENTS.md", "CLAUDE.md") or rel.startswith("docs/"):
            if entry["type"] == "file":
                target = final / (rel + ".txt")
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((pathlib.Path(workspace) / rel).read_bytes())


# ------------------------------------------------------------------ run

def run_trial(trial, revision=None):
    check_lock()
    case_id, n = trial.rsplit("-t", 1)
    case = resolve_case(case_id, int(n))
    global PLUGIN
    PLUGIN = {"v2": PLUGIN_V2, "v3": PLUGIN_V3, "v4": PLUGIN_V4}.get(case.get("candidate"), PLUGIN_V1)
    if revision:
        revised = json.loads((HERE / "revisions" / f"{trial}.json").read_text())
        case["sessions"] = revised["sessions"]
        case["revision"] = revised
    trial_dir = TRIALS / trial
    if (trial_dir / "trial.json").exists():
        raise SystemExit(f"{trial} already has a record; a rerun takes a new trial number")
    host = case["host"]
    cond = condition(host)
    gate = (True, None)
    if host == "claude":
        gate = start_gate_a4(trial) if case.get("amendment") == 4 else start_gate(trial)
        if not gate[0]:
            raise SystemExit(f"budget gate refused {trial}: remaining {gate[1]:.2f} USD")
    data = {"trial": trial, "case": case_id, "host": host, "started_at": now(), "status": "running",
            "candidate": case.get("candidate", "v1"),
            "condition": {k: v for k, v in cond.items() if k != "claude_settings"},
            "cli_version": run_py.cli_version(host),
            "driver_sha256": sha(pathlib.Path(__file__).read_bytes()),
            "design_lock_sha256": sha((HERE / "design.lock.json").read_bytes()),
            "budget_remaining_at_start_usd": gate[1], "turns": [], "snapshots": []}
    try:
        workspace, source = prepare_workspace(case, trial)
    except Exception as error:  # fixture could not be built
        data.update({"status": "setup-blocked", "error": str(error)})
        save_trial(trial_dir, data, ROOT)
        finish(trial)
        raise SystemExit(f"{trial} setup-blocked: {error}")
    data.update({"workspace": str(workspace), "workspace_name": workspace.name, "fixture_source": source})
    snap = snapshot(workspace)
    data["snapshots"].append({"label": "before turn 1", **snap})
    save_trial(trial_dir, data, workspace)
    turn_no = 0
    try:
        for s_index, sess in enumerate(case["sessions"], 1):
            session = None
            for t_index, text in enumerate(sess["turns"], 1):
                turn_no += 1
                prompt = turn_text(host, sess["skill"], t_index, text)
                record = run_turn(cond, workspace, prompt, session,
                                  RAW / trial / f"s{s_index}-turn-{t_index}")
                record.update({"session_index": s_index, "turn_in_session": t_index, "turn": turn_no,
                               "input": prompt})
                session = record.get("session") or session
                if host == "claude":
                    unknown = record.get("cost_usd") is None
                    record["cumulative_claude_cost_usd"] = record_cost(trial, session, record.get("cost_usd"),
                                                                       unknown)
                data["turns"].append(record)
                snap = snapshot(workspace)
                data["snapshots"].append({"label": f"after session {s_index} turn {t_index}", **snap})
                save_trial(trial_dir, data, workspace)
                print(f"{trial} s{s_index} t{t_index}: {record['status']} cost={record.get('cost_usd')} "
                      f"total={record.get('cumulative_claude_cost_usd')}", flush=True)
                if record["status"] != "captured":
                    raise RuntimeError(record.get("error") or record["status"])
        data["status"] = "complete"
    except RuntimeError as error:
        data["status"] = "stopped"
        data["error"] = str(error)
    finally:
        data["finished_at"] = now()
        data["auto_checks"] = grade_data(case, data)
        save_trial(trial_dir, data, workspace)
        save_final(trial_dir, workspace, snapshot(workspace))
        finish(trial)
    print(json.dumps(data["auto_checks"], indent=1))


# ------------------------------------------------------------------ checks

FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})\s")


def section_bounds(text):
    """Return a list of (start, end) character offsets of `## Lusona skills` sections."""
    lines = text.splitlines(keepends=True)
    offsets, pos = [], 0
    for line in lines:
        offsets.append(pos)
        pos += len(line)
    found, fenced, current = [], False, None
    for i, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if fenced:
            continue
        m = HEADING.match(line)
        if m and current is not None and len(m.group(1)) <= 2:
            found.append((current, offsets[i]))
            current = None
        if line.rstrip("\r\n").rstrip() == "## Lusona skills":
            current = offsets[i]
    if current is not None:
        found.append((current, len(text)))
    return found


def clean_value(value):
    value = value.strip()
    if value.endswith("."):
        value = value[:-1].rstrip()
    return value.strip("\"'`“”‘’ ")


def section_info(text):
    bounds = section_bounds(text)
    info = {"count": len(bounds)}
    if len(bounds) != 1:
        return info
    start, end = bounds[0]
    sec = text[start:end]
    lines = sec.splitlines()
    tdd = [l for l in lines if re.match(r"^\s*-\s*TDD:", l)]
    tiers = [l for l in lines if re.match(r"^\s*-\s*Model tiers:", l)]
    info.update({
        "start": start, "end": end, "text": sec,
        "uses": any("uses Lusona skills" in l for l in lines),
        "invocation": any("`/lusona:<skill>`" in l for l in lines),
        "records": any(re.match(r"^\s*-\s*Project records are under", l) for l in lines),
        "records_full": any("`docs/lusona/`" in l and "`docs/lusona/work.md`" in l for l in lines),
        "tdd_lines": tdd, "tdd_value": clean_value(tdd[0].split("TDD:", 1)[1]) if len(tdd) == 1 else None,
        "tier_lines": tiers,
    })
    return info


def entries(snap):
    return snap["entries"]


def text_of(snap, rel):
    e = entries(snap).get(rel)
    return e.get("text") if e and e["type"] == "file" else None


def outcome(ok, detail):
    return {"outcome": "pass" if ok else "fail", "detail": detail}


def changed_paths(a, b):
    ea, eb = entries(a), entries(b)
    out = []
    for rel in sorted(set(ea) | set(eb)):
        x, y = ea.get(rel), eb.get(rel)
        if (x or {}).get("type") == "dir" and (y or {}).get("type") == "dir":
            continue
        if x != y:
            out.append(rel)
    return out


def allowed(rel, patterns):
    for p in patterns:
        if p.endswith("/**") and (rel == p[:-3] or rel.startswith(p[:-2])):
            return True
        if rel == p:
            return True
        if any(q.startswith(rel + "/") for q in patterns if not q.endswith("/**")) or \
                any(q.endswith("/**") and q[:-3].startswith(rel) for q in patterns):
            return True  # parent directory of an allowed path
    return False


def confirm_split(case, data):
    """Indexes into data['snapshots'] for the pre-confirmation snapshots of each session."""
    groups, snap_index = [], 1  # snapshots[0] is before turn 1
    for s_index, sess in enumerate(case["sessions"]):
        confirm = case.get("confirm_turn", [None] * len(case["sessions"]))[s_index]
        start = snap_index - 1  # snapshot at session start
        n = len(sess["turns"])
        pre = list(range(start, start + (confirm if confirm else n + 1)))
        groups.append({"session_start": start, "pre": pre, "end": start + n})
        snap_index += n
    return groups


def grade_data(case, data):
    snaps = data["snapshots"]
    if not snaps:
        return {}
    first, last = snaps[0], snaps[-1]
    expected_turns = sum(len(s["turns"]) for s in case["sessions"])
    run_ok = data.get("status") == "complete" and len(data["turns"]) == expected_turns
    template = (PLUGIN / "templates" / "work.md.template").read_text()
    checks = {}
    checks["G-run"] = {"outcome": "pass" if run_ok else ("setup-blocked" if not data["turns"] or
                       data["turns"][0]["status"] == "setup-blocked" else "inconclusive"),
                       "detail": [t["status"] for t in data["turns"]]}
    checks["G-commit"] = outcome(first["commits"] == last["commits"] and all(s["commits"] == first["commits"]
                                                                            for s in snaps),
                                 [s["commits"] for s in snaps])
    bad = sorted({rel for s in snaps[1:] for rel in changed_paths(first, s)
                  if not allowed(rel, case["allowed_writes"])})
    # Deviation declared after C1-t1: Claude Code creates the empty directory .claude/.cc-writes
    # in the working directory itself (also present in the 2026-11-09 loop-conformance workspaces;
    # no tool call names it). It is listed separately and does not decide G-scope while it stays
    # an empty directory in every snapshot.
    host = [r for r in bad if r in (".claude", ".claude/.cc-writes")
            and all(entries(s).get(r, {"type": "dir"})["type"] == "dir" for s in snaps)
            and not any(k.startswith(".claude/") and k != ".claude/.cc-writes" for s in snaps for k in entries(s))]
    bad = [r for r in bad if r not in host]
    checks["G-scope"] = outcome(not bad, {"outside_allowed": bad, "host_artifacts": host})
    groups = confirm_split(case, data)
    cid = case.get("base_case", case["id"])
    final_agents = text_of(last, "AGENTS.md")
    final_claude = text_of(last, "CLAUDE.md")

    def ac2():
        problems = []
        for s in snaps[1:]:
            for rel, e in entries(s).items():
                if rel.startswith("docs/lusona/") and rel != "docs/lusona/work.md":
                    problems.append(f"{s['label']}: extra {rel}")
                if rel == "docs/lusona/work.md" and (e["type"] != "file" or e.get("text") != template):
                    problems.append(f"{s['label']}: work.md differs from template")
        if "docs/lusona/work.md" not in entries(last):
            problems.append("work.md missing at end")
        return outcome(not problems, problems)

    def absent_pre(names, grp):
        problems = [f"{snaps[i]['label']}: {n} exists" for i in grp["pre"] if i < len(snaps)
                    for n in names if n in entries(snaps[i])]
        return outcome(not problems, problems)

    def unchanged_pre(names, grp):
        base = snaps[grp["session_start"]]
        problems = [f"{snaps[i]['label']}: {n} changed" for i in grp["pre"] if i < len(snaps)
                    for n in names if entries(snaps[i]).get(n) != entries(base).get(n)]
        return outcome(not problems, problems)

    def shown_aid(grp, rel):
        sect = section_info(text_of(last, rel) or "")
        confirm_turn = grp["pre"][-1]  # index of the snapshot before the confirming turn = reply turn
        turns = data["turns"]
        if confirm_turn - 1 < 0 or confirm_turn - 1 >= len(turns) or sect.get("count") != 1:
            return {"outcome": "aid", "verbatim": None}
        reply = "\n".join(turns[confirm_turn - 1].get("texts") or [turns[confirm_turn - 1].get("reply") or ""])
        body = sect["text"].strip()
        return {"outcome": "aid", "verbatim": body in reply,
                "verbatim_ignoring_blank_lines": re.sub(r"\n\s*\n", "\n", body) in re.sub(r"\n\s*\n", "\n", reply)}

    if cid in ("C1", "C3", "C5", "C6"):
        if cid != "C5":
            checks["AC2"] = ac2()
    if cid in ("C1", "C5"):
        checks["AC4-order"] = absent_pre(["AGENTS.md", "CLAUDE.md"], groups[0])
        checks["AC4-shown-aid"] = shown_aid(groups[0], "AGENTS.md")
        info = section_info(final_agents or "")
        given = case["given"].get("tdd")
        problems = []
        if final_agents is None:
            problems.append("AGENTS.md missing or not a file")
        elif info["count"] != 1:
            problems.append(f"{info['count']} sections")
        else:
            for key in ("uses", "invocation"):
                if not info[key]:
                    problems.append(f"missing {key} statement")
            if cid == "C1" and not info["records_full"]:
                problems.append("missing records statement")
            if given and info["tdd_value"] != given:
                problems.append(f"TDD lines {info['tdd_lines']}")
            if not given and info["tdd_lines"]:
                problems.append(f"unexpected TDD lines {info['tdd_lines']}")
            if info["tier_lines"]:
                problems.append(f"unexpected Model tiers lines {info['tier_lines']}")
        checks["AC5"] = outcome(not problems, problems)
        if cid == "C1":
            checks["AC6-values"] = outcome(info.get("count") == 1 and info.get("tdd_value") == given
                                           and not info.get("tier_lines"),
                                           {"tdd": info.get("tdd_lines"), "tiers": info.get("tier_lines")})
        checks["AC7"] = outcome(final_claude in ("@AGENTS.md", "@AGENTS.md\n"), {"CLAUDE.md": final_claude})
        if cid == "C5":
            dirs = [s["label"] for s in snaps if any(r == "docs/lusona" or r.startswith("docs/lusona/")
                                                     for r in entries(s))]
            checks["AC12-nodir"] = outcome(not dirs, dirs)
            legacy = ["docs/agent/work.md", "docs/agent/specs/0001-example.md"]
            diff = [f"{s['label']}: {r}" for s in snaps for r in legacy if entries(s).get(r) != entries(first).get(r)]
            checks["AC12-legacy"] = outcome(not diff, diff)
            checks["R4"] = outcome(info.get("count") == 1 and not info.get("records"),
                                   {"records_line": info.get("records")})
    if cid == "C3":
        checks["AC4-decline"] = absent_pre(["AGENTS.md", "CLAUDE.md"],
                                           {"pre": list(range(len(snaps)))})
    if cid == "C2":
        fixture = case["fixture"]
        lus = [p for p in fixture if p.startswith("docs/lusona/")]
        problems = []
        for s in snaps:
            for p in lus:
                if text_of(s, p) != fixture[p]:
                    problems.append(f"{s['label']}: {p} differs")
            extra = [r for r, e in entries(s).items() if r.startswith("docs/lusona/") and e["type"] != "dir"
                     and r not in lus]
            problems += [f"{s['label']}: extra {r}" for r in extra]
        checks["AC3-bytes"] = outcome(not problems, problems)
        for label, grp in zip("AB", groups):
            checks[f"AC4-order-{label}"] = unchanged_pre(["AGENTS.md", "CLAUDE.md"], grp)
        if len(groups) >= 1 and groups[0]["end"] < len(snaps):
            end_a = snaps[groups[0]["end"]]
            a_text = text_of(end_a, "AGENTS.md") or ""
            info_a = section_info(a_text)
            problems = []
            if info_a["count"] != 1:
                problems.append(f"{info_a['count']} sections")
            else:
                for key in ("uses", "invocation", "records_full"):
                    if not info_a[key]:
                        problems.append(f"missing {key}")
                if info_a["tdd_value"] != case["given"]["tdd_a"]:
                    problems.append(f"TDD lines {info_a['tdd_lines']}")
                tl = info_a["tier_lines"]
                if len(tl) != 1 or not all(w in tl[0] for w in ("fast", "standard", "deep",
                                                                 *case["given"]["tiers_labels"])):
                    problems.append(f"tier lines {tl}")
                prefix = fixture["AGENTS.md"] + "\n"
                rest = a_text[len(prefix):]
                if not a_text.startswith(prefix):
                    problems.append("text before the section is not the fixture plus one newline")
                elif rest.lstrip("\n") != info_a["text"] or info_a["end"] != len(a_text):
                    problems.append("insertion is not newlines followed by the section to end of file")
            checks["AC5-A"] = outcome(not problems, problems)
            checks["AC6-values-A-aid"] = {"outcome": "aid", "tier_lines": info_a.get("tier_lines")}
            c_text = text_of(end_a, "CLAUDE.md") or ""
            first_line = c_text.split("\n", 1)[0]
            ok = (first_line == "@AGENTS.md" and c_text.endswith(fixture["CLAUDE.md"])
                  and set(c_text[len("@AGENTS.md"):len(c_text) - len(fixture["CLAUDE.md"])]) <= {"\n"}
                  and len(c_text) > len(fixture["CLAUDE.md"]))
            checks["AC7-A"] = outcome(ok, {"CLAUDE.md": c_text})
            if len(groups) >= 2 and groups[1]["end"] < len(snaps):
                end_b = snaps[groups[1]["end"]]
                checks["AC7-B"] = outcome(entries(end_b).get("CLAUDE.md") == entries(end_a).get("CLAUDE.md"),
                                          {"CLAUDE.md": text_of(end_b, "CLAUDE.md")})
                b_text = text_of(end_b, "AGENTS.md") or ""
                info_b = section_info(b_text)
                problems = []
                if info_b["count"] != 1:
                    problems.append(f"{info_b['count']} sections")
                else:
                    if info_b["tdd_value"] != case["given"]["tdd_b"]:
                        problems.append(f"TDD lines {info_b['tdd_lines']}")
                    if info_b["tier_lines"] != info_a.get("tier_lines"):
                        problems.append(f"tier lines {info_b['tier_lines']} vs {info_a.get('tier_lines')}")
                    if info_a.get("count") == 1:
                        out_a = a_text[:info_a["start"]] + a_text[info_a["end"]:]
                        out_b = b_text[:info_b["start"]] + b_text[info_b["end"]:]
                        if out_a != out_b:
                            problems.append("text outside the section changed between A and B")
                if text_of(end_b, "docs/lusona/work.md") != fixture["docs/lusona/work.md"]:
                    problems.append("work.md changed")
                checks["AC8"] = outcome(not problems, problems)
    if cid == "C4":
        diff = [p for p in case["unchanged"] if entries(last).get(p) != entries(first).get(p)]
        checks["C4-unchanged"] = outcome(not diff, diff)
        new = sorted(r for r in entries(last) if r not in entries(first) and entries(last)[r]["type"] == "file")
        checks["C4-created-aid"] = {"outcome": "aid", "created": new}
        mem = [((t.get("init") or {}).get("memory_paths")) for t in data["turns"]]
        checks["C4-memory-paths"] = {"outcome": "recorded", "memory_paths": mem}
    if case.get("amendment") == 3 and cid in ("C3", "C10", "C11", "C9"):
        if cid == "C9":
            checks["AC4-order"] = unchanged_pre(["AGENTS.md", "CLAUDE.md"], groups[0])
        else:
            checks["AC4-order"] = absent_pre(["AGENTS.md", "CLAUDE.md"], groups[0])
    if cid in ("C10", "C11"):
        checks["AC2"] = ac2()
        info = section_info(final_agents or "")
        given = case["given"].get("tdd")
        problems = []
        if final_agents is None:
            problems.append("AGENTS.md missing or not a file")
        elif info["count"] != 1:
            problems.append(f"{info['count']} sections")
        else:
            for key in ("uses", "invocation", "records_full"):
                if not info[key]:
                    problems.append(f"missing {key} statement")
            if given and info["tdd_value"] != given:
                problems.append(f"TDD lines {info['tdd_lines']}")
            if not given and info["tdd_lines"]:
                problems.append(f"unexpected TDD lines {info['tdd_lines']}")
            if info["tier_lines"]:
                problems.append(f"unexpected Model tiers lines {info['tier_lines']}")
        checks["AC5"] = outcome(not problems, problems)
    if cid == "C10":
        info = section_info(final_agents or "")
        checks["AC6-values"] = outcome(info.get("count") == 1 and info.get("tdd_value") == case["given"]["tdd"]
                                       and not info.get("tier_lines"),
                                       {"tdd": info.get("tdd_lines"), "tiers": info.get("tier_lines")})
        checks["AC4-partial-files"] = outcome(final_agents is not None and "CLAUDE.md" not in entries(last),
                                              {"AGENTS.md": final_agents is not None,
                                               "CLAUDE.md": entries(last).get("CLAUDE.md")})
        checks["AC4-shown-aid"] = shown_aid(groups[0], "AGENTS.md")
    if cid == "C11":
        early = [snaps[i]["label"] for i in (0, 1) if i < len(snaps)
                 and any(r == "docs/lusona" or r.startswith("docs/lusona/") for r in entries(snaps[i]))]
        checks["AC12-ask-files"] = outcome(not early, early)
        legacy = ["docs/agent/work.md", "docs/agent/specs/0001-example.md"]
        diff = [f"{s['label']}: {r}" for s in snaps for r in legacy if entries(s).get(r) != entries(first).get(r)]
        checks["AC12-legacy"] = outcome(not diff, diff)
        checks["AC7"] = outcome(final_claude in ("@AGENTS.md", "@AGENTS.md\n"), {"CLAUDE.md": final_claude})
    if cid == "C9":
        fixture = case["fixture"]
        lus = [p for p in fixture if p.startswith("docs/lusona/")]
        problems = []
        for s in snaps:
            problems += [f"{s['label']}: {p} differs" for p in lus if text_of(s, p) != fixture[p]]
            problems += [f"{s['label']}: extra {r}" for r, e in entries(s).items()
                         if r.startswith("docs/lusona/") and e["type"] != "dir" and r not in lus]
        checks["AC3-bytes"] = outcome(not problems, problems)
        diff = [s["label"] for s in snaps
                if entries(s).get("docs/lusona/README.md") != entries(first).get("docs/lusona/README.md")]
        checks["C-readme"] = outcome(not diff, diff)
        info = section_info(final_agents or "")
        checks["C-removed"] = outcome(info["count"] == 1 and not info.get("tdd_lines") and not info.get("tier_lines"),
                                      {"count": info["count"], "tdd": info.get("tdd_lines"),
                                       "tiers": info.get("tier_lines")})
        diff = [s["label"] for s in snaps if entries(s).get("CLAUDE.md") != entries(first).get("CLAUDE.md")]
        checks["AC7"] = outcome(not diff, diff)
        checks["AC8"] = outcome(info["count"] == 1, {"count": info["count"]})
        expected = fixture["AGENTS.md"].replace("- TDD: targeted for validation and persistence boundaries\n", "")
        checks["C-removed-exact-aid"] = {"outcome": "aid", "equals_fixture_without_tdd_line": final_agents == expected}
    if cid in ("C7", "C8"):  # Amendment 1
        fixture = case["fixture"]
        lus = [p for p in fixture if p.startswith("docs/lusona/")]
        problems = []
        for s in snaps:
            problems += [f"{s['label']}: {p} differs" for p in lus if text_of(s, p) != fixture[p]]
            problems += [f"{s['label']}: extra {r}" for r, e in entries(s).items()
                         if r.startswith("docs/lusona/") and e["type"] != "dir" and r not in lus]
        checks["AC3-bytes"] = outcome(not problems, problems)
    if cid == "C7":
        checks["AC4-order"] = absent_pre(["AGENTS.md", "CLAUDE.md"], groups[0])
        info = section_info(final_agents or "")
        checks["R2-noline"] = outcome(info["count"] == 1 and not info.get("tdd_lines") and not info.get("tier_lines"),
                                      {"count": info["count"], "tdd": info.get("tdd_lines"),
                                       "tiers": info.get("tier_lines")})
        diff = [s["label"] for s in snaps
                if entries(s).get("docs/lusona/README.md") != entries(first).get("docs/lusona/README.md")]
        checks["R2-readme"] = outcome(not diff, diff)
        checks["AC7"] = outcome(final_claude in ("@AGENTS.md", "@AGENTS.md\n"), {"CLAUDE.md": final_claude})
    if cid == "C8":
        fixture = case["fixture"]
        checks["AC4-order"] = unchanged_pre(["AGENTS.md", "CLAUDE.md"], groups[0])
        diff = [s["label"] for s in snaps if text_of(s, "CLAUDE.md") != fixture["CLAUDE.md"]]
        checks["R5-noimport-files"] = outcome(not diff, diff)
        info = section_info(final_agents or "")
        checks["R6-one"] = outcome(info["count"] == 1, {"count": info["count"]})
        user_line = case["given"]["user_line"]
        checks["R6-userline"] = outcome(info["count"] == 1 and user_line in info["text"].splitlines(),
                                        {"section": info.get("text")})
        checks["AC8"] = outcome(info["count"] == 1 and info.get("tdd_value") == case["given"]["tdd"],
                                {"tdd": info.get("tdd_lines"), "tiers": info.get("tier_lines")})
        fx = section_info(fixture["AGENTS.md"])
        ok = (info["count"] == 1 and final_agents[:info["start"]] == fixture["AGENTS.md"][:fx["start"]]
              and final_agents[info["end"]:] == fixture["AGENTS.md"][fx["end"]:])
        checks["AC5-outside"] = outcome(ok, {"AGENTS.md": final_agents})
    if cid == "C6":
        checks["AC4-order"] = unchanged_pre(["CLAUDE.md", "AGENTS.md"], groups[0])
        link = entries(last).get("AGENTS.md")
        checks["R1-link"] = outcome(link == {"type": "symlink", "target": "CLAUDE.md"}, link)
        info = section_info(final_claude or "")
        checks["R1-once"] = outcome(info["count"] == 1 and not info.get("tdd_lines") and not info.get("tier_lines"),
                                    {"count": info["count"], "tdd": info.get("tdd_lines"),
                                     "tiers": info.get("tier_lines")})
        lines = (final_claude or "").splitlines()
        checks["R1-noimport"] = outcome(not any(l.strip() in ("@AGENTS.md", "@./AGENTS.md") for l in lines),
                                        [l for l in lines if "@" in l])
        fx = case["fixture"]["CLAUDE.md"]
        ok = (final_claude or "").startswith(fx) and info["count"] == 1 and \
            final_claude[len(fx):].lstrip("\n") == info["text"] and info["end"] == len(final_claude)
        checks["R1-outside"] = outcome(ok, {"CLAUDE.md": final_claude})
    if case.get("amendment") == 4:
        grade_amendment_4(case, data, checks, groups, unchanged_pre, absent_pre)
    if not run_ok:
        for name, check in checks.items():
            if name not in ("G-run",) and check.get("outcome") == "pass":
                check["outcome"] = "inconclusive"
                check["note"] = "trial did not finish; a pass is not counted"
    return checks


def shown_section(reply):
    """Lines of the `## Lusona skills` section shown in a reply (AC4-shown, Amendment 4)."""
    lines = (reply or "").splitlines()
    fenced = False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if line.strip() == "## Lusona skills":
            out = [line]
            for nxt in lines[i + 1:]:
                if fenced and FENCE.match(nxt):
                    break
                m = HEADING.match(nxt)
                if not fenced and m and len(m.group(1)) <= 2:
                    break
                out.append(nxt)
            return out
    return None


def norm_lines(lines):
    lines = [l.rstrip() for l in lines]
    while lines and not lines[-1]:
        lines.pop()
    return lines


def grade_amendment_4(case, data, checks, groups, unchanged_pre, absent_pre):
    snaps = data["snapshots"]
    first, last = snaps[0], snaps[-1]
    cid = case["id"]
    final_agents = text_of(last, "AGENTS.md")
    info = section_info(final_agents or "")
    fixture = case["fixture"]
    if cid in ("C12", "C13"):
        after1 = [n for n in ("AGENTS.md", "CLAUDE.md")
                  if len(snaps) > 1 and entries(snaps[1]).get(n) != entries(first).get(n)]
        checks["C-both-shown-aid"] = {"outcome": "aid", "changed_after_turn_1": after1 if len(snaps) > 1 else None}
        diff = [s["label"] for s in snaps
                if entries(s).get("docs/lusona/README.md") != entries(first).get("docs/lusona/README.md")]
        checks["C-readme"] = outcome(not diff, diff)
        checks["AC8"] = outcome(info["count"] == 1, {"count": info["count"]})
        checks["AC4-order"] = unchanged_pre(["AGENTS.md", "CLAUDE.md"], groups[0])
        detail = {"count": info["count"], "tdd": info.get("tdd_lines"), "tiers": info.get("tier_lines")}
        if cid == "C12":
            checks["C-kept"] = outcome(info["count"] == 1 and len(info.get("tdd_lines") or []) == 1
                                       and info.get("tdd_value") == case["given"]["tdd"]
                                       and not info.get("tier_lines"), detail)
            checks["C-kept-exact-aid"] = {"outcome": "aid", "equals_fixture": final_agents == fixture["AGENTS.md"]}
        else:
            old = case["given"]["old_tdd"]
            checks["C-new"] = outcome(info["count"] == 1 and len(info.get("tdd_lines") or []) == 1
                                      and info.get("tdd_value") == case["given"]["tdd"]
                                      and old not in info.get("text", "") and not info.get("tier_lines"), detail)
            expected = fixture["AGENTS.md"].replace(f"- TDD: {old}\n", f"- TDD: {case['given']['tdd']}\n")
            checks["C-new-exact-aid"] = {"outcome": "aid", "equals_fixture_with_new_value": final_agents == expected}
    if cid in ("C14", "C15"):
        checks["AC4-order"] = absent_pre(["AGENTS.md", "CLAUDE.md"], groups[0])
    if cid == "C14":
        problems = []
        if final_agents is None:
            problems.append("AGENTS.md missing or not a file")
        elif info["count"] != 1:
            problems.append(f"{info['count']} sections")
        else:
            for key in ("uses", "invocation", "records_full"):
                if not info[key]:
                    problems.append(f"missing {key} statement")
            if info["tdd_lines"]:
                problems.append(f"unexpected TDD lines {info['tdd_lines']}")
            if info["tier_lines"]:
                problems.append(f"unexpected Model tiers lines {info['tier_lines']}")
        checks["AC5"] = outcome(not problems, problems)
    if cid == "C15":
        checks["C-notdd"] = outcome(info["count"] == 1 and not info.get("tdd_lines"),
                                    {"count": info["count"], "tdd": info.get("tdd_lines")})
        tl = info.get("tier_lines") or []
        checks["C-tiers-aid"] = {"outcome": "aid", "count": info["count"], "tier_lines": tl,
                                 "one_line_naming_three_tiers": len(tl) == 1
                                 and all(w in tl[0] for w in ("fast", "standard", "deep"))}
    if cid == "C8":
        grp = groups[0]
        idx = grp["pre"][-1] - 1  # turn before the confirming turn
        turns = data["turns"]
        aid = {"outcome": "aid", "reply_turn": idx + 1}
        if 0 <= idx < len(turns) and info["count"] == 1:
            shown = shown_section(turns[idx].get("reply"))
            written = norm_lines(info["text"].splitlines())
            aid.update({"shown_found": shown is not None,
                        "user_line_shown": shown is not None and case["given"]["user_line"] in [l.rstrip() for l in shown],
                        "equal_line_for_line": shown is not None and norm_lines(shown) == written,
                        "shown": shown, "written": written})
        checks["AC4-shown-aid"] = aid


def grade(trial):
    path = TRIALS / trial / "trial.json"
    data = json.loads(path.read_text())
    case = resolve_case(data["case"], int(data["trial"].rsplit("-t", 1)[1]))
    if data["case"] == data["trial"].rsplit("-t", 1)[0] and (HERE / "revisions" / f"{trial}.json").exists():
        case["sessions"] = json.loads((HERE / "revisions" / f"{trial}.json").read_text())["sessions"]
    data["auto_checks"] = grade_data(case, data)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps(data["auto_checks"], indent=1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("run", "grade", "ledger"))
    parser.add_argument("trial", nargs="?")
    parser.add_argument("--revision", action="store_true")
    args = parser.parse_args()
    if args.action == "run":
        run_trial(args.trial, args.revision)
    elif args.action == "grade":
        grade(args.trial)
    else:
        print(LEDGER.read_text() if LEDGER.exists() else "{}")


if __name__ == "__main__":
    main()
