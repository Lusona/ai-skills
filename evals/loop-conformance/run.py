#!/usr/bin/env python3
"""Loop conformance runner: freeze a condition, prepare and run trials on Claude Code or
Codex CLI, grade computed checks, judge semantic criteria, report counts, and compare a
run with a stored reference. Actors never receive rubric.md or other evaluator files."""
import argparse
import glob
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import uuid

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SUITE_FILES = ("scenarios.json", "rubric.md", "suite.lock.json")
CODE_FILES = ("run.py", "checks.py", "compare.py")
HOSTS = ("claude", "codex")
CHECK_IDS = tuple(f"C{n}" for n in range(1, 18))
STATES = ("pass", "fail", "inconclusive", "setup-blocked", "not-applicable", "invalid")
JUDGED_STATES = ("pass", "fail", "inconclusive")
INSTRUCTION_FILES = ("CLAUDE.md", "AGENTS.md")
FIXTURE_AUTHOR = ("Loop Conformance Fixture", "fixture@loop-conformance.invalid")
# Parent-session variables that must not reach an actor or judge process. Names are
# removed; authentication variables in KEEP_ENV stay.
STRIP_ENV = re.compile(r"^(CLAUDECODE|CLAUDE_PID|CLAUDE_EFFORT|CLAUDE_CODE_.*)$")
KEEP_ENV = {"CLAUDE_CODE_OAUTH_TOKEN", "CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX",
            "CLAUDE_CODE_USE_FOUNDRY"}


def _load(name):
    spec = importlib.util.spec_from_file_location(f"loop_conformance_{name}", HERE / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


checks = _load("checks")
comparison = _load("compare")

JUDGE_TEMPLATE = """You are an independent evaluator for a workflow conformance test. You did not \
produce the work below. Grade only the listed criteria, using only the rubric, the scripted user \
turns, the actor's final replies, and the changed files shown here. Do not use tools.

# Rubric

{rubric}

# Criteria to grade

{criteria}

# Scripted user turns and actor replies

{transcript}

# Workspace changes

{changes}

# Output

Reply with one JSON object and nothing else. Use each criterion id above as a key. Each value is \
an object with "result" set to "pass", "fail", or "inconclusive", and "evidence" set to one or two \
sentences that quote or locate the text you used. Example shape:
{{"C1.concrete": {{"result": "pass", "evidence": "..."}}}}
"""
JUDGE_PROMPT_SHA256 = hashlib.sha256(JUDGE_TEMPLATE.encode()).hexdigest()


# ---------------------------------------------------------------- small helpers

def digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache"}


def ignored(relative):
    parts = pathlib.PurePosixPath(relative).parts
    return bool(IGNORED_DIRS.intersection(parts)) or relative.endswith(".pyc")


def hashes(root):
    root = pathlib.Path(root)
    out = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_file() and not path.is_symlink() and not ignored(relative):
            out[relative] = digest(path)
    return out


def save(path, data):
    pathlib.Path(path).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def load_json(path):
    return json.loads(pathlib.Path(path).read_text())


# Environment added for the Claude Code actor. CLAUDE_CODE_SHELL (documented) makes the Bash
# tool use bash instead of the user's zsh, whose aliases (ls -> eza) reached the actor. In
# the 2026-11-09 probes, bash loaded no alias (`compgen -a` empty) and `ls` listed files.
CLAUDE_SHELL_ENV = {"CLAUDE_CODE_SHELL": "/bin/bash"}


def actor_env(environ=None):
    environ = dict(os.environ if environ is None else environ)
    removed = sorted(k for k in environ if STRIP_ENV.match(k) and k not in KEEP_ENV)
    for key in removed:
        del environ[key]
    return environ, removed


def execute(args, *, input, text, capture_output, cwd, timeout, env=None):
    """Run one host process; on timeout stop only its private process group."""
    with subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=text, cwd=cwd, env=env,
                          start_new_session=True) as process:
        try:
            stdout, stderr = process.communicate(input, timeout=timeout)
        except BaseException as error:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            stdout, stderr = process.communicate()
            if isinstance(error, subprocess.TimeoutExpired):
                raise subprocess.TimeoutExpired(args, timeout, output=stdout, stderr=stderr) from error
            raise
        return subprocess.CompletedProcess(args, process.returncode, stdout, stderr)


def git(workspace, *args, check=True):
    return subprocess.run(["git", "-C", str(workspace), *args], text=True, capture_output=True, check=check)


def commit_count(workspace):
    """Number of commits reachable from any ref (all branches, tags, worktrees)."""
    try:
        return int(git(workspace, "rev-list", "--all", "--count").stdout.strip())
    except (subprocess.CalledProcessError, ValueError, OSError):
        return None


def git_state(workspace):
    """HEAD, every ref, the reachable commit count, and the commit set S: hashes from
    `git rev-list --branches --tags HEAD` plus every hash in the HEAD reflog (the reflog
    keeps an amended or reset-away commit). None for a value git cannot give."""
    def value(*args):
        try:
            return git(workspace, *args).stdout.strip()
        except (subprocess.CalledProcessError, OSError):
            return None
    listed = value("rev-list", "--branches", "--tags", "HEAD")
    reflog = value("reflog", "--format=%H", "HEAD")
    hashes_seen = set((listed or "").split()) | set((reflog or "").split())
    # Every linked worktree's HEAD and HEAD reflog, so a commit on a detached worktree counts.
    for line in (value("worktree", "list", "--porcelain") or "").splitlines():
        if line.startswith("HEAD "):
            hashes_seen.add(line.split()[1])
        elif line.startswith("worktree "):
            tree = line[len("worktree "):]
            try:
                hashes_seen.update(git(tree, "reflog", "--format=%H", "HEAD").stdout.split())
            except (subprocess.CalledProcessError, OSError):
                pass
    commits = None if listed is None else sorted(hashes_seen)
    return {"head": value("rev-parse", "HEAD"), "refs": value("for-each-ref", "--format=%(refname) %(objectname)"),
            "all_count": commit_count(workspace), "commits": commits, "reflog_available": reflog is not None}


def outer_repo_state(root=ROOT):
    """sha256 of every tracked and untracked, not ignored, file of the suite's repository.
    A listed file that no longer exists hashes as "absent"."""
    listed = subprocess.run(["git", "-C", str(root), "ls-files", "-co", "--exclude-standard", "-z"],
                            capture_output=True, check=True).stdout.decode(errors="surrogateescape")
    state = {}
    for name in sorted(set(filter(None, listed.split("\0")))):
        path = pathlib.Path(root) / name
        state[name] = digest(path) if path.is_file() else "absent"
    return state


def state_digest(state):
    if isinstance(state, dict):
        return hashlib.sha256(json.dumps(sorted(state.items())).encode()).hexdigest()
    return hashlib.sha256(str(state).encode()).hexdigest()


def check_output_location(path):
    """Refuse an output directory inside the suite's repository unless git ignores it, so
    evidence never appears as a change to the repository (repo-local tmp/ is ignored)."""
    path = pathlib.Path(path).expanduser().resolve()
    if _under(path, ROOT.resolve()):
        ignored_by_git = subprocess.run(["git", "-C", str(ROOT), "check-ignore", "-q", str(path)],
                                        capture_output=True).returncode == 0
        if not ignored_by_git:
            raise ValueError(f"output {path} is inside the repository and not ignored by git; use repo-local tmp/")
    return path


def default_work_root():
    cache = os.environ.get("XDG_CACHE_HOME") or str(pathlib.Path.home() / ".cache")
    return pathlib.Path(cache) / "lusona-evals"


def check_work_root(path):
    """Refuse a work root under the system temporary directory or under any directory
    that holds CLAUDE.md or AGENTS.md, because hosts load those files as instructions."""
    path = pathlib.Path(path).expanduser().resolve()
    for temp in {pathlib.Path("/tmp").resolve(), pathlib.Path(tempfile.gettempdir()).resolve()}:
        if path == temp or path.is_relative_to(temp):
            raise ValueError(f"work root {path} is under the system temporary directory {temp}")
    for directory in (path, *path.parents):
        for name in INSTRUCTION_FILES:
            if (directory / name).exists():
                raise ValueError(f"work root {path} is inside {directory}, which contains {name}")
    return path


# ---------------------------------------------------------------- suite content

def validate_scenarios(scenarios, rubric_text=None):
    """Return a list of problems in scenarios.json (and rubric.md when given)."""
    problems = []
    if not isinstance(scenarios, dict) or not scenarios:
        return ["scenarios.json must be a non-empty object keyed by scenario id"]
    for sid, case in scenarios.items():
        for key, kind in (("skill", str), ("files", dict), ("turns", list), ("checks", list)):
            if not isinstance(case.get(key), kind):
                problems.append(f"{sid}: {key} must be a {kind.__name__}")
        if problems and problems[-1].startswith(f"{sid}:"):
            continue
        if not case["turns"] or not all(isinstance(t, str) and t for t in case["turns"]):
            problems.append(f"{sid}: turns must be non-empty strings")
        unknown = [c for c in case["checks"] if c not in CHECK_IDS]
        if unknown:
            problems.append(f"{sid}: unknown check ids {unknown}")
        expect = case.get("expect") or {}
        for check, key in (("C2", "record_globs"), ("C5", "protected_globs"), ("C8", "allowed_globs")):
            if check in case["checks"] and not isinstance(expect.get(key), list):
                problems.append(f"{sid}: {check} needs expect.{key} as a list")
        for check, key in (("C10", "expect_reviewer"), ("C11", "expect_workers")):
            if check in case["checks"] and key not in expect:
                problems.append(f"{sid}: {check} needs expect.{key}")
        for check, key in (("C12", "decision_protected_globs"), ("C14", "decision_record_globs"),
                           ("C16", "old_record_globs"), ("C17", "update_globs")):
            if check in case["checks"] and not (isinstance(expect.get(key), list) and expect[key]):
                problems.append(f"{sid}: {check} needs expect.{key} as a non-empty list")
        if "C15" in case["checks"] and not expect.get("superseded_status"):
            problems.append(f"{sid}: C15 needs expect.superseded_status as a non-empty object")
        for key in ("decision_status", "superseded_status"):
            value = expect.get(key)
            if value is not None and not (isinstance(value, dict)
                                          and all(isinstance(k, str) and isinstance(v, str) for k, v in value.items())):
                problems.append(f"{sid}: expect.{key} must map record paths to a status word")
        if "legacy_records" in expect and not (isinstance(expect["legacy_records"], list)
                                               and all(isinstance(p, str) for p in expect["legacy_records"])):
            problems.append(f"{sid}: expect.legacy_records must be a list of paths")
        if ("C13" in case["checks"] and rubric_text is not None
                and not any(c.startswith("C13.") for c in rubric_criteria(rubric_section(rubric_text, sid)))):
            problems.append(f"{sid}: C13 needs a judged criterion in rubric.md")
        for key in ("spec_required", "expect_workers", "expect_reviewer"):
            if key in expect and not isinstance(expect[key], bool):
                problems.append(f"{sid}: expect.{key} must be true or false")
        for path in case["files"]:
            pure = pathlib.PurePosixPath(path)
            if pure.is_absolute() or ".." in pure.parts or ignored(path):
                problems.append(f"{sid}: fixture path {path!r} is not a plain workspace path")
        if rubric_text is not None and rubric_section(rubric_text, sid) is None:
            problems.append(f"{sid}: rubric.md has no '## {sid}' section")
    return problems


def validate_pass_marks(data, scenarios):
    """Return a list of problems in pass-marks.json: each mark names a scenario that lists the
    check, a trial count, a minimum pass count per host within it, and a reason."""
    marks = data.get("marks") if isinstance(data, dict) else None
    if not isinstance(marks, list) or not marks:
        return ["pass-marks.json must hold a non-empty marks list"]
    problems, seen = [], set()
    for mark in marks:
        key = f"{mark.get('scenario')} {mark.get('check')}"
        if (mark.get("scenario"), mark.get("check")) in seen:
            problems.append(f"{key}: duplicate mark")
        seen.add((mark.get("scenario"), mark.get("check")))
        case = scenarios.get(mark.get("scenario"))
        if case is None:
            problems.append(f"{key}: unknown scenario")
        elif mark.get("check") not in case.get("checks", []):
            problems.append(f"{key}: check not listed for the scenario")
        trials = mark.get("trials")
        if not isinstance(trials, int) or trials < 1:
            problems.append(f"{key}: trials must be a positive integer")
            trials = None
        minimum = mark.get("min_pass") if isinstance(mark.get("min_pass"), dict) else {}
        for host in HOSTS:
            value = minimum.get(host)
            if not isinstance(value, int) or value < 0 or (trials is not None and value > trials):
                problems.append(f"{key}: min_pass.{host} must be an integer from 0 to trials")
        if not isinstance(mark.get("reason"), str) or not mark["reason"].strip():
            problems.append(f"{key}: reason must be non-empty text")
    return problems


def rubric_preamble(text):
    match = re.search(r"^## ", text, re.MULTILINE)
    return text[:match.start()].strip() if match else text.strip()


def rubric_section(text, scenario):
    lines, start = text.splitlines(), None
    for index, line in enumerate(lines):
        if start is None and re.fullmatch(rf"##\s+{re.escape(scenario)}\s*", line):
            start = index
        elif start is not None and re.match(r"##\s", line):
            return "\n".join(lines[start:index]).strip()
    return "\n".join(lines[start:]).strip() if start is not None else None


def rubric_criteria(section):
    return re.findall(r"^###\s+(C\d+\.[\w-]+)\s*$", section or "", re.MULTILINE)


def criterion_text(section, criterion):
    match = re.search(rf"^###\s+{re.escape(criterion)}\s*$(.*?)(?=^###\s|\Z)", section, re.MULTILINE | re.DOTALL)
    return f"### {criterion}\n{match.group(1).strip()}" if match else f"### {criterion}"


# ---------------------------------------------------------------- hosts

# Claude Code's Bash sandbox (bubblewrap on Linux). Sandboxed Bash commands run without an
# allow rule; they can write only to the working directory and the sandbox's per-user temp
# directory, and reach no network host. dontAsk refuses the unsandboxed retry. The file
# tools are not sandboxed; blockWritesOutsideWorkingDirectories confines Write and Edit.
CLAUDE_SETTINGS = {
    "sandbox": {"enabled": True, "autoAllowBashIfSandboxed": True, "allowUnsandboxedCommands": False,
                "failIfUnavailable": True, "network": {"allowedDomains": []}},
    "permissions": {"blockWritesOutsideWorkingDirectories": True},
}
# Claude Code 2.1.321 lists the subagent tool as "Task" in the init event but emits
# tool_use events named "Agent"; both names are allowed and counted. The bare "Bash" rule
# allows every Bash command: without it, dontAsk refused sandboxed commands whose write target
# Claude Code could not resolve before running (shell variables, command substitution,
# "$TMPDIR", `alias`). The sandbox settings above still confine every Bash command.
CLAUDE_ALLOWED_TOOLS = ["Read", "Edit", "Write", "Skill", "Task", "Agent", "Bash"]


def claude_allowed_tools(plugin=None):
    return list(CLAUDE_ALLOWED_TOOLS)


def cli_version(host, executor=execute):
    proc = executor([host, "--version"], input="", text=True, capture_output=True, cwd=None, timeout=60,
                    env=actor_env()[0])
    return proc.stdout.strip()


def ambient_instruction_hashes(host, home=None, environ=None):
    """sha256 of instruction files the host loads outside the workspace and the plugin."""
    if host != "codex":
        return {}
    environ = os.environ if environ is None else environ
    home = pathlib.Path(home) if home else pathlib.Path.home()
    codex_home = pathlib.Path(environ.get("CODEX_HOME") or home / ".codex")
    out = {}
    for name in ("AGENTS.md", "AGENTS.override.md"):
        candidate = codex_home / name
        if candidate.exists():
            target = candidate.resolve()
            out[str(target)] = digest(target)
    return out


def codex_prefix(plugin, skill):
    return (f"Use the Lusona {skill} skill at {plugin}/skills/{skill}/SKILL.md and applicable linked "
            "instructions. Role: coordinator for this isolated project task. The synthetic workspace is "
            "your consuming project. Own questions, assignments, reconciliation, integration, verification, "
            "and shared project records within user authority; apply the workflow's normal delegation rules "
            "and local fallback when delegation is prohibited or unavailable. Read only this workspace and "
            "the frozen plugin resources.\n\n")


def turn_inputs(host, plugin, case):
    inputs = []
    for index, text in enumerate(case["turns"], 1):
        if index == 1 and host == "claude":
            inputs.append(f"/lusona:{case['skill']} {text}\n")
        elif index == 1:
            inputs.append(codex_prefix(plugin, case["skill"]) + text + "\n")
        else:
            inputs.append(text + "\n")
    return inputs


def claude_command(condition, session):
    args = ["claude", "-p", "--plugin-dir", condition["plugin_path"], "--output-format", "stream-json",
            "--verbose", "--model", condition["model"], "--effort", condition["effort"],
            "--setting-sources", "project", "--strict-mcp-config",
            "--settings", json.dumps(condition["claude_settings"], sort_keys=True),
            "--permission-mode", "dontAsk"]
    if session:
        args += ["--resume", session]
    return args + ["--allowedTools", *condition["allowed_tools"]]


def codex_command(condition, workspace, session):
    args = ["codex", "exec", "--ignore-user-config", "--enable", "multi_agent", "--sandbox", "workspace-write",
            "--json", "--model", condition["model"], "-c",
            "model_reasoning_effort=" + json.dumps(condition["effort"]),
            "-C", str(workspace), "--skip-git-repo-check"]
    return args + (["resume", session, "-"] if session else ["-"])


def _events(stdout):
    for line in (stdout or "").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict):
            yield event


# "review" not preceded by a letter or digit: `\b` would miss "delete_review" (no word
# boundary between "_" and "r").
_REVIEW = re.compile(r"(?<![a-z0-9])review", re.IGNORECASE)


def _mentions_review(value):
    """True for "review", "reviewer", "Code-review", "delete_review"; false for "preview"."""
    return isinstance(value, str) and _REVIEW.search(value) is not None


def parse_claude(stdout, plugin_path):
    """Extract one turn's evidence from Claude Code stream-json output."""
    parsed = {"session": None, "init_seen": False, "plugin_ok": False, "plugin_paths": [], "result_ok": False,
              "reply": None, "usage": None, "cost_usd": None, "turn_cost_usd": None, "workers": 0,
              "reviewer_seen": False,
              "denied_actions": [], "tool_calls": {}, "init": None, "subagents_spawned": None,
              "texts": [], "init_model": None, "work_workers": 0}
    last_text, task_ids = None, set()
    for event in _events(stdout):
        kind = event.get("type")
        if kind == "system" and event.get("subtype") == "init":
            parsed["init_seen"] = True
            parsed["session"] = event.get("session_id") or parsed["session"]
            plugins = [p for p in event.get("plugins") or [] if isinstance(p, dict) and p.get("name") == "lusona"]
            parsed["plugin_paths"] = [p.get("path") for p in plugins]
            parsed["plugin_ok"] = (len(plugins) == 1 and bool(plugins[0].get("path")) and
                                   pathlib.Path(plugins[0]["path"]).resolve() == pathlib.Path(plugin_path).resolve())
            parsed["init_model"] = event.get("model")
            parsed["init"] = {k: event.get(k) for k in ("model", "permissionMode", "mcp_servers", "tools", "cwd",
                                                        "claude_code_version", "plugins", "memory_paths")}
        elif kind == "assistant" and event.get("parent_tool_use_id") is None:
            for block in (event.get("message") or {}).get("content") or []:
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "text" and block.get("text"):
                    last_text = block["text"]
                    parsed["texts"].append(block["text"])
                elif block.get("type") == "tool_use":
                    name = block.get("name") or "unnamed"
                    parsed["tool_calls"][name] = parsed["tool_calls"].get(name, 0) + 1
                    if name in ("Task", "Agent") and block.get("id") not in task_ids:
                        task_ids.add(block.get("id"))
                        data = block.get("input") or {}
                        # The prompt is not read: an implementer's prompt may mention a later review.
                        # An Explore subagent only reads, so it is never a reviewer.
                        explore = str(data.get("subagent_type") or "").lower() == "explore"
                        review = not explore and any(_mentions_review(data.get(k))
                                                     for k in ("description", "subagent_type"))
                        if review:
                            parsed["reviewer_seen"] = True
                        elif not explore:
                            parsed["work_workers"] += 1
        elif kind == "result":
            parsed["session"] = event.get("session_id") or parsed["session"]
            parsed["result_ok"] = event.get("subtype") == "success" and not event.get("is_error")
            if isinstance(event.get("result"), str) and event["result"].strip():
                parsed["reply"] = event["result"]
            parsed["usage"] = event.get("usage")
            # total_cost_usd is cumulative for the session: on a resumed turn it includes earlier
            # turns. model_usage_since_last_result holds this turn's cost per model.
            parsed["cost_usd"] = event.get("total_cost_usd")
            since = event.get("model_usage_since_last_result")
            if isinstance(since, dict):
                parsed["turn_cost_usd"] = sum((v or {}).get("costUSD") or 0 for v in since.values())
            parsed["denied_actions"] = list(event.get("permission_denials") or [])
            stats = event.get("subagent_stats")
            if isinstance(stats, dict):
                parsed["subagents_spawned"] = stats.get("spawned")
    parsed["workers"] = len(task_ids)
    if parsed["reply"] is None:
        parsed["reply"] = last_text
    return parsed


def parse_codex(stdout):
    """Extract one turn's evidence from Codex CLI exec --json output."""
    parsed = {"session": None, "completed": False, "failed": None, "reply": None, "usage": None,
              "workers": None, "reviewer_seen": None, "denied_actions": [], "item_types": {}, "texts": []}
    # workers and reviewer_seen stay None: in codex-cli 0.167.0 the exec JSONL showed a
    # collab "wait" call but omitted the spawn_agent call that the session rollout recorded.
    for event in _events(stdout):
        kind = event.get("type")
        if kind == "thread.started":
            parsed["session"] = event.get("thread_id")
        elif kind == "turn.completed":
            parsed["completed"] = True
            parsed["usage"] = event.get("usage")
        elif kind in ("turn.failed", "error"):
            parsed["failed"] = event.get("error") or event.get("message") or kind
        elif kind == "item.completed" and isinstance(event.get("item"), dict):
            item = event["item"]
            item_type = item.get("type") or "unknown"
            parsed["item_types"][item_type] = parsed["item_types"].get(item_type, 0) + 1
            if item_type == "agent_message" and isinstance(item.get("text"), str):
                parsed["reply"] = item["text"]
                parsed["texts"].append(item["text"])
            if item.get("status") in ("declined", "denied", "rejected"):
                parsed["denied_actions"].append(item)
    return parsed


def default_codex_sessions(environ=None):
    environ = os.environ if environ is None else environ
    return pathlib.Path(environ.get("CODEX_HOME") or pathlib.Path.home() / ".codex") / "sessions"


def codex_rollout_workers(thread, sessions_root):
    """Count spawn_agent calls of the root thread from its session rollout file.

    Returns (workers, reviewer_seen, work_workers, summary). workers is None when the
    rollout cannot be found; work_workers counts spawns whose task name does not mention
    review, and is None when a spawn has no task name. Spawn messages are encrypted in
    storage, so reviewer_seen is True only when a task_name mentions review, False when
    nothing was spawned, and None otherwise."""
    summary = {"thread": thread, "sessions_root": str(sessions_root), "status": "unavailable"}
    matches = sorted(pathlib.Path(sessions_root).rglob(f"rollout-*-{thread}.jsonl")) if thread else []
    if len(matches) != 1:
        summary["error"] = f"expected one rollout for thread {thread}; found {len(matches)}"
        return None, None, None, summary
    calls, spawns, malformed = {}, [], 0
    for line in matches[0].read_text(errors="replace").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            malformed += 1
            continue
        payload = event.get("payload") if isinstance(event, dict) else None
        if not isinstance(payload, dict) or payload.get("type") not in ("function_call", "custom_tool_call"):
            continue
        name = payload.get("name") or "unnamed"
        calls[name] = calls.get(name, 0) + 1
        if name == "spawn_agent":
            try:
                arguments = json.loads(payload.get("arguments") or "{}")
            except (json.JSONDecodeError, TypeError):
                arguments = {}
            spawns.append({k: arguments.get(k) for k in ("task_name", "model", "reasoning_effort")})
    reviewer = True if any(_mentions_review(s.get("task_name")) for s in spawns) else (False if not spawns else None)
    named = all(isinstance(s.get("task_name"), str) and s["task_name"] for s in spawns)
    work = sum(1 for s in spawns if not _mentions_review(s.get("task_name"))) if named else None
    summary.update({"status": "captured", "rollout": str(matches[0]), "rollout_sha256": digest(matches[0]),
                    "function_calls": calls, "spawns": spawns, "malformed_lines": malformed,
                    "basis": "spawn_agent function calls of the root thread; spawn messages are encrypted"})
    summary["work_workers"] = work
    return len(spawns), reviewer, work, summary


# ---------------------------------------------------------------- evaluator-material access

EVALUATOR_NAMES = ("rubric.md", "scenarios.json", "judge-calibration.json", "suite.lock.json", "condition.json",
                   "pass-marks.json")
_TOKEN = re.compile(r"""[^\s'"`;|&<>()=,]+""")
_OUTPUT_KEYS = {"aggregated_output", "output", "stdout", "stderr", "exit_code", "status", "text"}
# Text the actor writes into files, hands to a subagent, or uses as a label is not a read.
_SKIP_KEYS = {"content", "old_string", "new_string", "new_source", "edits", "todos", "prompt", "description"}
_HEREDOC = re.compile(r"<<-?\s*(['\"]?)([A-Za-z_]\w*)\1")
_LINK_TARGET = re.compile(r"\]\([^)\s]*\)")
_SHELL_WRAPPER = re.compile(r"^\s*(?:\S*/)?(?:ba|z)?sh\s+-\w*c\s+(['\"])(.*)\1\s*$", re.DOTALL)
_SEGMENT = re.compile(r"&&|\|\||;|\||\n")
_GLOB_CHARS = re.compile(r"[*?\[]")


def _fields(value, key=None):
    """Yield (key, string) for every string in a tool input, skipping _SKIP_KEYS."""
    if isinstance(value, str):
        yield key, value
    elif isinstance(value, dict):
        for name, item in value.items():
            if name not in _SKIP_KEYS:
                yield from _fields(item, name)
    elif isinstance(value, list):
        for item in value:
            yield from _fields(item, key)


_HERESTRING = re.compile(r"""<<<\s*(?:'[^']*'|"[^"]*"|\S+)""")
_TEXT_WRITERS = {"cat", "tee"}
# Interpreters whose here-document body is program code, not shell: relative strings in it
# (such as '..' or 'from .. import x') are not paths the shell resolves.
_CODE_INTERPRETER = re.compile(r"^(?:python[\d.]*|node|ruby|perl)$")


def _heredoc_receiver(before):
    """The command that receives a here-document: the basename of the first word of the
    segment before `<<`, after NAME=value assignments and the wrappers `env`,
    `timeout <duration>`, `nice [-n <n>]`, `time`, and `uv run`. "" for a redirect-only
    here-document."""
    words = [w.strip("'\"") for w in re.split(r"&&|\|\||;|\|", before)[-1].split()]
    index = 0
    while index < len(words):
        word, name = words[index], os.path.basename(words[index])
        if word.startswith((">", "<")):
            return ""
        if "=" in word or name in ("env", "time"):
            index += 1
        elif name == "timeout":
            index += 2
        elif name == "nice":
            index += 3 if index + 1 < len(words) and words[index + 1] == "-n" else 1
        elif name == "uv" and index + 1 < len(words) and words[index + 1] == "run":
            index += 2
        else:
            return name
    return ""


def strip_shell_text(command):
    """Split a shell command into the text scanned as shell and the code bodies.

    Removed: the word after a here-string (`<<<`), and the body of a here-document whose
    receiver writes text (`cat`, `tee`, or a redirect-only here-document). The body given to
    a code interpreter (`python3 - <<EOF`) is returned separately as code. Any other body,
    such as one given to `sh`, `bash`, or `zsh`, stays in the shell text. Returns
    (shell_text, code_bodies)."""
    lines, out, code, index = command.split("\n"), [], [], 0
    while index < len(lines):
        line = _HERESTRING.sub(" ", lines[index])
        heredocs = [(m.group(2), _heredoc_receiver(line[:m.start()])) for m in _HEREDOC.finditer(line)]
        out.append(_HEREDOC.sub(" ", line))
        index += 1
        for delimiter, receiver in heredocs:
            body = []
            while index < len(lines) and lines[index].strip() != delimiter:
                body.append(lines[index])
                index += 1
            index += 1
            if _CODE_INTERPRETER.match(receiver):
                code.append("\n".join(body))
            elif receiver not in _TEXT_WRITERS and receiver != "":
                out.extend(body)
    return "\n".join(out), code


def tool_calls(host, stdout):
    """Return (tool name, input) for every actor tool call, including subagent calls.
    Tool output is not included: only what the actor asked to read or run."""
    if host == "claude":
        calls = []
        for event in _events(stdout):
            if event.get("type") != "assistant":
                continue
            for block in (event.get("message") or {}).get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    calls.append((block.get("name") or "unnamed", block.get("input")))
        return calls
    items = {}
    for event in _events(stdout):
        item = event.get("item")
        if event.get("type") in ("item.started", "item.completed") and isinstance(item, dict):
            if item.get("type") not in ("agent_message", "reasoning"):
                key = item.get("id") or f"anonymous-{len(items)}"
                items[key] = (item.get("type") or "unknown",
                              {k: v for k, v in item.items() if k not in _OUTPUT_KEYS})
    return list(items.values())


def _under(path, root):
    return path == root or path.is_relative_to(root)


class _Scope:
    def __init__(self, workspace, plugin, condition_dir, trial_dir, work_root, suite_dir, repo_root, fixture_files,
                 home):
        norm = lambda v: pathlib.Path(os.path.normpath(str(v)))
        self.workspace, self.plugin, self.condition_dir = norm(workspace), norm(plugin), norm(condition_dir)
        self.trial_dir, self.work_root, self.suite_dir = norm(trial_dir), norm(work_root), norm(suite_dir)
        self.repo_root, self.home, self.fixture_files = norm(repo_root), str(home), set(fixture_files)

    def resolve(self, token, cwd):
        token = token.rstrip(":,")
        if token.endswith(".") and not token.endswith("..") and token != ".":
            token = token[:-1]
        if not token:
            return None, False
        token = re.sub(r"\$\{?(HOME|PWD)\}?", lambda m: self.home if m.group(1) == "HOME" else str(cwd), token)
        if token == "~" or token.startswith("~/"):
            token = self.home + token[1:]
        relative = not os.path.isabs(token)
        return pathlib.Path(os.path.normpath(os.path.join(cwd, token))), relative

    def concrete(self, path, relative, cwd):
        if _under(path, self.plugin):
            return None
        if _under(path, self.workspace):
            if path.name in EVALUATOR_NAMES and path.relative_to(self.workspace).as_posix() not in self.fixture_files:
                return f"evaluator file name {path.name}"
            return None
        if relative and _under(cwd, self.workspace):
            return "relative path leaves the workspace"
        if _under(path, self.condition_dir):
            return "condition directory outside plugin/"
        if _under(path, self.suite_dir):
            return "suite source directory"
        if _under(path, self.work_root):
            return "another trial's workspace or a judge directory"
        for directory in (path, *path.parents):
            if directory != self.trial_dir and (directory / "run.json").is_file():
                return "another trial's directory"
        if _under(path, self.repo_root):
            return "the suite's repository outside the frozen plugin"
        if path.name in EVALUATOR_NAMES:
            return f"evaluator file name {path.name}"
        return None

    def classify(self, token, cwd, code=False):
        """With code, a relative token (program text, not a shell path) is checked only for
        an evaluator file name; absolute, `~`, and `$HOME` tokens get every rule."""
        path, relative = self.resolve(token, cwd)
        if path is None:
            return None
        if code and relative:
            if path.name in EVALUATOR_NAMES and not (_under(path, self.workspace) and
                                                     path.relative_to(self.workspace).as_posix() in self.fixture_files):
                return f"evaluator file name {path.name}"
            return None
        reason = self.concrete(path, relative, cwd)
        if reason or not _GLOB_CHARS.search(str(path)):
            return reason
        for count, match in enumerate(glob.iglob(str(path))):
            if count >= 200:
                break
            reason = self.concrete(pathlib.Path(match), False, cwd)
            if reason:
                return f"glob reaches {match}: {reason}"
        return None

    def scan_command(self, command):
        wrapped = _SHELL_WRAPPER.match(command)
        if wrapped:
            command = wrapped.group(2)
        command, code_bodies = strip_shell_text(command)
        command = _LINK_TARGET.sub("]", command)
        cwd = self.workspace
        for segment in _SEGMENT.split(command):
            tokens = _TOKEN.findall(segment)
            for token in tokens:
                reason = self.classify(token, cwd)
                if reason:
                    return token, reason
            if tokens and tokens[0] in ("cd", "pushd"):
                target = self.resolve(tokens[1], cwd)[0] if len(tokens) > 1 else pathlib.Path(self.home)
                cwd = target or cwd
        for body in code_bodies:
            for token in _TOKEN.findall(_LINK_TARGET.sub("]", body)):
                reason = self.classify(token, self.workspace, code=True)
                if reason:
                    return token, f"{reason} (in program text)"
        return None, None

    def scan_text(self, text):
        for token in _TOKEN.findall(_LINK_TARGET.sub("]", text)):
            reason = self.classify(token, self.workspace)
            if reason:
                return token, reason
        return None, None


def evaluator_access(calls_by_turn, *, workspace, plugin, condition_dir, trial_dir, work_root,
                     suite_dir=HERE, repo_root=ROOT, fixture_files=(), environ=None):
    """List actor tool calls that refer to evaluator material. A shell command is scanned
    without here-document bodies, here-string text, or Markdown link targets, and with its
    leading `cd` steps applied; written content, subagent prompts, and descriptions are
    not scanned."""
    environ = os.environ if environ is None else environ
    scope = _Scope(workspace, plugin, condition_dir, trial_dir, work_root, suite_dir, repo_root, fixture_files,
                   environ.get("HOME") or pathlib.Path.home())
    hits = []
    for turn, calls in calls_by_turn:
        for name, data in calls:
            for key, text in _fields(data):
                if key == "pattern" and name in ("Grep", "Glob"):
                    continue  # a search pattern, not a path; the path field is still scanned
                token, reason = scope.scan_command(text) if key == "command" else scope.scan_text(text)
                if reason:
                    hits.append({"turn": turn, "tool": name, "token": token, "reason": reason,
                                 "call": json.dumps(data, sort_keys=True)[:500]})
                    break
    return hits


# ---------------------------------------------------------------- freeze and prepare

def code_hashes():
    return {name: digest(HERE / name) for name in CODE_FILES}


def freeze(plugin, out, host, model, effort, timeout, judge_model, judge_effort, *, max_trials=5,
           suite_dir=HERE, executor=execute, home=None, environ=None):
    if host not in HOSTS:
        raise ValueError(f"host must be one of {HOSTS}")
    suite_dir = pathlib.Path(suite_dir).resolve()
    out = check_output_location(out)
    lock = load_json(suite_dir / "suite.lock.json")
    names = sorted(set(SUITE_FILES) | set(lock))
    for name, expected in lock.items():
        if digest(suite_dir / name) != expected:
            raise ValueError(f"{name} does not match suite.lock.json; do not run or silently refresh the lock")
    problems = validate_scenarios(load_json(suite_dir / "scenarios.json"), (suite_dir / "rubric.md").read_text())
    if problems:
        raise ValueError("invalid suite content: " + "; ".join(problems))
    if "pass-marks.json" in names:
        problems = validate_pass_marks(load_json(suite_dir / "pass-marks.json"),
                                       load_json(suite_dir / "scenarios.json"))
        if problems:
            raise ValueError("invalid pass-marks.json: " + "; ".join(problems))
    out.mkdir(parents=True, exist_ok=False)
    shutil.copytree(plugin, out / "plugin", ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".git"))
    for name in names:
        (out / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(suite_dir / name, out / name)
    for name, expected in lock.items():
        if digest(out / name) != expected:
            raise ValueError(f"copied {name} does not match suite.lock.json")
    plugin_path = str(out / "plugin")
    condition = {
        "host": host, "model": model, "effort": effort, "timeout_seconds": timeout, "max_trials": max_trials,
        "judge_model": judge_model, "judge_effort": judge_effort, "judge_prompt_sha256": JUDGE_PROMPT_SHA256,
        "cli_version": cli_version(host, executor),
        "judge_cli_version": cli_version("claude", executor),
        "plugin_path": plugin_path, "plugin_hashes": hashes(out / "plugin"),
        "suite_hashes": {name: digest(out / name) for name in names}, "code_hashes": code_hashes(),
        "ambient_instruction_hashes": ambient_instruction_hashes(host, home, environ),
        "frozen_at_unix": time.time(),
    }
    if host == "claude":
        condition["allowed_tools"] = claude_allowed_tools()
        condition["claude_settings"] = CLAUDE_SETTINGS
        condition["shell_env"] = dict(CLAUDE_SHELL_ENV)
        condition["permission_config"] = {"permission_mode": "dontAsk", "setting_sources": "project",
                                          "strict_mcp_config": True, "settings": CLAUDE_SETTINGS,
                                          "allowed_tools": claude_allowed_tools(),
                                          "shell_env": dict(CLAUDE_SHELL_ENV)}
        condition["permissions"] = ("--permission-mode dontAsk; allowed_tools for file, skill, subagent, and "
                                    "Bash tools; every Bash command runs in the Claude Code sandbox, writing only "
                                    "to the workspace and the sandbox temp directory, with no network; Write and "
                                    "Edit refused outside the workspace; refused calls listed in denied_actions")
        condition["isolation"] = ("Workspace under a work root with no CLAUDE.md or AGENTS.md in any ancestor; "
                                  "--setting-sources project and --strict-mcp-config (no user settings, no MCP "
                                  "servers); frozen plugin via --plugin-dir, required in every init event; "
                                  "parent-session CLAUDE_CODE_* variables removed. Ambient instruction files: none.")
    else:
        condition["allowed_tools"] = None
        condition["claude_settings"] = None
        condition["permission_config"] = {"sandbox": "workspace-write", "ignore_user_config": True,
                                          "features": ["multi_agent"], "approval_bypass": False}
        condition["permissions"] = "workspace-write sandbox; no approval bypass; --ignore-user-config"
        condition["isolation"] = ("Workspace under a work root with no CLAUDE.md or AGENTS.md in any ancestor; "
                                  "skill loaded by path from the frozen plugin; Codex still loads the global "
                                  "AGENTS.md, recorded by hash in ambient_instruction_hashes.")
    save(out / "condition.json", condition)
    return out


def load_condition(condition, *, require_code=False):
    """Load condition.json after checking the frozen plugin and suite. With require_code,
    also refuse when run.py, checks.py, or compare.py changed after freeze (used before an
    actor runs). Grading, judging, and reporting record the difference instead."""
    condition = pathlib.Path(condition).resolve()
    data = load_json(condition / "condition.json")
    if hashes(condition / "plugin") != data["plugin_hashes"]:
        raise ValueError("frozen plugin changed after freeze")
    if any(digest(condition / name) != value for name, value in data["suite_hashes"].items()):
        raise ValueError("frozen suite changed after freeze")
    if require_code and code_hashes() != data["code_hashes"]:
        raise ValueError("run.py, checks.py, or compare.py changed after freeze; freeze a new condition")
    data["code_changed_since_freeze"] = sorted(k for k, v in code_hashes().items() if data["code_hashes"].get(k) != v)
    data["dir"] = str(condition)
    data["sha256"] = digest(condition / "condition.json")
    return data


def prepare(condition, scenario, trial, out, work_root=None, *, guard=check_work_root):
    cond = load_condition(condition, require_code=True)
    if not 1 <= trial <= cond["max_trials"]:
        raise ValueError(f"trial must be between 1 and {cond['max_trials']}")
    scenarios = load_json(pathlib.Path(cond["dir"]) / "scenarios.json")
    if scenario not in scenarios:
        raise ValueError(f"unknown scenario {scenario!r}")
    case = scenarios[scenario]
    work_root = guard(work_root or default_work_root())
    out = check_output_location(out)
    if out.is_relative_to(work_root):
        raise ValueError("trial output must be outside the work root so actors cannot read it")
    out.mkdir(parents=True, exist_ok=False)
    work_root.mkdir(parents=True, exist_ok=True)
    workspace = work_root / f"{scenario}-t{trial}-{uuid.uuid4().hex[:8]}"
    workspace.mkdir()
    git(workspace, "init", "--quiet")
    for key, value in (("user.name", FIXTURE_AUTHOR[0]), ("user.email", FIXTURE_AUTHOR[1]),
                       ("commit.gpgsign", "false"), ("tag.gpgsign", "false")):
        git(workspace, "config", key, value)
    for name, content in case["files"].items():
        target = workspace / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    git(workspace, "add", "-A")
    git(workspace, "-c", f"user.name={FIXTURE_AUTHOR[0]}", "-c", f"user.email={FIXTURE_AUTHOR[1]}",
        "-c", "commit.gpgsign=false", "commit", "--quiet", "--no-verify", "--allow-empty", "-m", "Fixture")
    inputs = turn_inputs(cond["host"], cond["plugin_path"], case)
    for index, text in enumerate(inputs, 1):
        (out / f"turn-{index}.input.txt").write_text(text)
    save(out / "run.json", {
        "condition": cond["dir"], "condition_sha256": cond["sha256"], "host": cond["host"],
        "scenario": scenario, "trial": trial, "turns": len(inputs), "workspace": str(workspace),
        "work_root": str(work_root), "actor_role": "coordinator",
        "input_hashes": {f"turn-{i}.input.txt": digest(out / f"turn-{i}.input.txt") for i in range(1, len(inputs) + 1)},
        "initial_hashes": hashes(workspace), "initial_commits": commit_count(workspace),
        "initial_git": git_state(workspace),
        "code_hashes": code_hashes()})
    return out


# ---------------------------------------------------------------- run

def _text(value):
    if isinstance(value, bytes):
        return value.decode(errors="replace")
    return value or ""


def run_turn(cond, meta, trial_dir, index, session, executor):
    workspace = pathlib.Path(meta["workspace"])
    prompt = (trial_dir / f"turn-{index}.input.txt").read_text()
    host = cond["host"]
    args = claude_command(cond, session) if host == "claude" else codex_command(cond, workspace, session)
    env, removed = actor_env()
    shell_env = dict(cond.get("shell_env") or {}) if host == "claude" else {}
    env.update(shell_env)
    record = {"turn": index, "command": args, "resumed_session": session, "session": session,
              "status": "setup-blocked", "removed_env": removed, "set_env": shell_env,
              "started_at_unix": time.time()}
    stdout = stderr = ""
    started = time.monotonic()
    try:
        proc = executor(args, input=prompt, text=True, capture_output=True, cwd=workspace,
                        timeout=cond["timeout_seconds"], env=env)
        stdout, stderr = _text(proc.stdout), _text(proc.stderr)
        record["exit_code"] = proc.returncode
        if host == "claude":
            parsed = parse_claude(stdout, cond["plugin_path"])
            if not parsed["init_seen"]:
                record["error"] = "no init event; the host did not start a session"
            elif not parsed["plugin_ok"]:
                record["error"] = (f"init event lusona plugin paths {parsed['plugin_paths']} are not exactly "
                                   f"the frozen plugin {cond['plugin_path']}")
            elif parsed["init_model"] != cond["model"]:
                record["error"] = (f"init event model {parsed['init_model']!r} differs from the condition model "
                                   f"{cond['model']!r}")
            elif proc.returncode == 0 and parsed["result_ok"] and parsed["reply"] is not None:
                record["status"] = "captured"
            else:
                record["status"] = "inconclusive"
                record["error"] = "session started but the turn did not finish with a successful result"
        else:
            parsed = parse_codex(stdout)
            if not parsed["session"]:
                record["error"] = "no thread.started event; the host did not start a session"
            elif proc.returncode == 0 and parsed["completed"] and not parsed["failed"] and parsed["reply"] is not None:
                record["status"] = "captured"
            else:
                record["status"] = "inconclusive"
                record["error"] = f"session started but the turn did not complete: {parsed['failed']}"
        record.update({k: v for k, v in parsed.items() if k not in ("init_seen", "result_ok", "completed")})
        record["session"] = parsed["session"] or session
    except subprocess.TimeoutExpired as error:
        stdout, stderr = _text(error.stdout), _text(error.stderr)
        record["status"] = "inconclusive"
        record["error"] = f"timeout after {cond['timeout_seconds']} s; partial transcript kept"
    except OSError as error:
        record["error"] = f"launch failed: {error}"
    finally:
        record["elapsed_seconds"] = time.monotonic() - started
        (trial_dir / f"turn-{index}.stdout.jsonl").write_text(stdout)
        (trial_dir / f"turn-{index}.stderr.txt").write_text(stderr)
        save(trial_dir / f"turn-{index}.result.json", record)
    return record


def commits_added(before, after):
    """Commits in the after set S that were not in the before set. Branches, tags, and
    stashes without a new commit add none. Falls back to the reachable-count growth for
    trials prepared before the commit set was recorded."""
    if before.get("commits") is not None and after.get("commits") is not None:
        return len(set(after["commits"]) - set(before["commits"]))
    if before.get("all_count") is None or after.get("all_count") is None:
        return None
    return max(0, after["all_count"] - before["all_count"])


def changed_between(before, after):
    return {"added": sorted(after.keys() - before.keys()),
            "modified": sorted(k for k in before.keys() & after.keys() if before[k] != after[k]),
            "deleted": sorted(before.keys() - after.keys())}


def run_trial(trial_dir, *, executor=execute, outer_status=outer_repo_state, codex_sessions=None, home=None,
              environ=None):
    """Run every turn once. codex_sessions is the Codex sessions directory (default
    $CODEX_HOME/sessions or ~/.codex/sessions), read for worker counts. home and environ
    locate ambient instruction files (defaults: the user's home and environment)."""
    trial_dir = pathlib.Path(trial_dir).resolve()
    meta = load_json(trial_dir / "run.json")
    cond = load_condition(meta["condition"], require_code=True)
    if cond["sha256"] != meta["condition_sha256"]:
        raise ValueError("condition.json changed after prepare")
    if (trial_dir / "trial.json").exists() or list(trial_dir.glob("turn-*.result.json")):
        raise ValueError("trial already ran; failed or blocked trials are kept and never retried")
    for name, value in meta["input_hashes"].items():
        if digest(trial_dir / name) != value:
            raise ValueError(f"{name} changed after prepare")
    workspace = pathlib.Path(meta["workspace"])
    if hashes(workspace) != meta["initial_hashes"]:
        raise ValueError("workspace changed between prepare and run")
    outer_before = outer_status()
    started = time.monotonic()
    turns, status, session, version, blocked = [], "captured", None, None, None
    try:
        version = cli_version(cond["host"], executor)
    except (OSError, subprocess.SubprocessError) as error:
        version, status, blocked = f"unavailable: {error}", "setup-blocked", f"CLI unavailable: {error}"
    if status == "captured" and version != cond["cli_version"]:
        status, blocked = "setup-blocked", f"CLI version {version!r} differs from the frozen {cond['cli_version']!r}"
    ambient = ambient_instruction_hashes(cond["host"], home, environ)
    if status == "captured" and ambient != cond["ambient_instruction_hashes"]:
        status, blocked = "setup-blocked", (f"ambient instruction files (AGENTS.md) changed since freeze: "
                                            f"{ambient} != {cond['ambient_instruction_hashes']}")
    if status == "captured":
        for index in range(1, meta["turns"] + 1):
            record = run_turn(cond, meta, trial_dir, index, session, executor)
            turns.append(record)
            if record["status"] != "captured":
                status = record["status"]
                break
            session = record["session"]
    outer_after = outer_status()
    calls = [(t["turn"], tool_calls(cond["host"], (trial_dir / f"turn-{t['turn']}.stdout.jsonl").read_text()))
             for t in turns]
    access = evaluator_access(calls, workspace=workspace, plugin=cond["plugin_path"], condition_dir=cond["dir"],
                              trial_dir=trial_dir, work_root=meta["work_root"],
                              fixture_files=meta["initial_hashes"].keys(), environ=environ)
    if access:
        status = "invalid"
    after = hashes(workspace)
    changed = changed_between(meta["initial_hashes"], after)
    files = {}
    for path in changed["added"] + changed["modified"]:
        try:
            files[path] = (workspace / path).read_text()
        except (UnicodeDecodeError, OSError):
            pass
    git_before = meta.get("initial_git") or {"all_count": meta["initial_commits"]}
    git_after = git_state(workspace)
    commits_after = git_after["all_count"]
    log = git(workspace, "log", "--format=%H %an <%ae> %s", check=False)
    (trial_dir / "workspace-git-log.txt").write_text(log.stdout + log.stderr)
    artifacts = trial_dir / "artifacts"
    shutil.copytree(workspace, artifacts, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
                    symlinks=True)
    captured = [t for t in turns if t["status"] == "captured"]
    claude = cond["host"] == "claude"
    workers = ([t.get("workers") for t in turns] if turns else [None])
    reviewers = [t.get("reviewer_seen") for t in turns] if turns else [None]
    work = [t.get("work_workers") for t in turns] if turns else [None]
    if not claude and turns:
        thread = next((t.get("session") for t in turns if t.get("session")), None)
        count, reviewer, work_count, summary = codex_rollout_workers(thread, codex_sessions or default_codex_sessions())
        save(trial_dir / "codex-rollout-summary.json", summary)
        workers, reviewers, work = [count], [reviewer], [work_count]
    last = turns[-1] if turns else {}
    cost = last.get("cost_usd") if claude and last.get("status") == "captured" else None
    trial = {
        "scenario": meta["scenario"], "host": cond["host"], "trial": meta["trial"], "status": status,
        "replies": [t.get("reply") for t in captured],
        "turn_texts": [t.get("texts") or [] for t in captured],
        "changed": changed, "files": files,
        "commits_added": commits_added(git_before, git_after),
        "refs_changed": (git_before.get("head"), git_before.get("refs")) != (git_after["head"], git_after["refs"]),
        "outer_changed": outer_before != outer_after,
        "workers": None if any(w is None for w in workers) else sum(workers),
        "work_workers": None if any(w is None for w in work) else sum(work),
        "reviewer_seen": True if any(r is True for r in reviewers) else (None if any(r is None for r in reviewers) else False),
        "denied_actions": [d for t in turns for d in t.get("denied_actions") or []],
        "evaluator_access": access,
        "cost_usd": cost,
        "condition": cond["dir"], "condition_sha256": cond["sha256"],
        "capture": {
            "cli_version": version, "expected_cli_version": cond["cli_version"], "model": cond["model"],
            "effort": cond["effort"], "elapsed_seconds": time.monotonic() - started,
            "cost_basis": ("Claude Code total_cost_usd of the last turn, which is cumulative for the session"
                           if claude else "Codex reports token usage only"),
            "turns": [{k: t.get(k) for k in ("turn", "status", "exit_code", "error", "session", "usage", "cost_usd",
                                             "turn_cost_usd",
                                             "elapsed_seconds", "workers", "subagents_spawned", "tool_calls",
                                             "item_types")} for t in turns],
            "hashes_before": meta["initial_hashes"], "hashes_after": after,
            "workspace": str(workspace), "git_before": git_before, "git_after": git_after,
            "outer_digest_before": state_digest(outer_before), "outer_digest_after": state_digest(outer_after),
            "outer_changed_paths": sorted(k for k in set(outer_before) | set(outer_after)
                                          if outer_before.get(k) != outer_after.get(k))[:200]
            if isinstance(outer_before, dict) and isinstance(outer_after, dict) else None,
            "isolation": {"work_root": meta["work_root"],
                          "init": next((t.get("init") for t in turns if t.get("init")), None) if claude else None,
                          "ambient_instruction_hashes": cond["ambient_instruction_hashes"]},
            "usage_scope": "Root CLI reported usage per turn; worker usage may be excluded.",
        },
    }
    if blocked:
        trial["capture"]["error"] = blocked
    save(trial_dir / "trial.json", trial)
    return trial


# ---------------------------------------------------------------- grade and judge

def _trial_context(trial_dir):
    trial_dir = pathlib.Path(trial_dir).resolve()
    trial = load_json(trial_dir / "trial.json")
    cond = load_condition(trial["condition"])
    case = load_json(pathlib.Path(cond["dir"]) / "scenarios.json")[trial["scenario"]]
    return trial_dir, trial, cond, case


def save_provenance(trial_dir, step):
    """Record which code graded a trial: sha256 of run.py, checks.py, compare.py now."""
    save(pathlib.Path(trial_dir) / f"{step}-provenance.json",
         {"step": step, "code_hashes": code_hashes(), "at_unix": time.time()})


def derive_work_workers(trial_dir, trial):
    """work_workers for a trial captured before the field existed: from the Claude Code
    transcripts or the Codex rollout summary; None when neither gives it."""
    if trial["host"] == "claude":
        turns = sorted(trial_dir.glob("turn-*.stdout.jsonl"))
        if not turns:
            return None
        cond_plugin = load_json(trial_dir / "run.json").get("condition", "")
        return sum(parse_claude(t.read_text(), cond_plugin)["work_workers"] for t in turns)
    summary_path = trial_dir / "codex-rollout-summary.json"
    if not summary_path.exists():
        return None
    spawns = load_json(summary_path).get("spawns")
    if spawns is None or not all(isinstance(s.get("task_name"), str) and s["task_name"] for s in spawns):
        return None
    return sum(1 for s in spawns if not _mentions_review(s["task_name"]))


def grade(trial_dir):
    trial_dir, trial, _, case = _trial_context(trial_dir)
    if "work_workers" not in trial:
        trial = dict(trial, work_workers=derive_work_workers(trial_dir, trial))
    computed = checks.evaluate(trial, case)
    save(trial_dir / "computed.json", computed)
    save_provenance(trial_dir, "grade")
    return computed


def build_judge_prompt(rubric_text, scenario, criteria, turns, turn_texts, changed, files):
    """turn_texts holds, per turn, every root assistant text message in order."""
    section = rubric_section(rubric_text, scenario) or ""
    criteria_text = "\n\n".join(criterion_text(section, c) for c in criteria)
    transcript = []
    for index, turn in enumerate(turns, 1):
        texts = turn_texts[index - 1] if index - 1 < len(turn_texts) else []
        texts = [texts] if isinstance(texts, str) else [t for t in texts or [] if t is not None]
        if texts:
            messages = "\n\n".join(f"#### Actor message {n} of turn {index}\n\n{text}"
                                    for n, text in enumerate(texts, 1))
        else:
            messages = "(no reply captured)"
        transcript.append(f"## Turn {index}\n\n### User\n\n{turn}\n\n### Actor messages, in order; the last "
                          f"is the final reply\n\n{messages}")
    changes = [f"Added: {', '.join(changed.get('added', [])) or 'none'}",
               f"Modified: {', '.join(changed.get('modified', [])) or 'none'}",
               f"Deleted: {', '.join(changed.get('deleted', [])) or 'none'}"]
    for path, content in sorted(files.items()):
        changes.append(f"\n## File `{path}`\n\n````\n{content}\n````")
    rubric = f"{rubric_preamble(rubric_text)}\n\n## Scenario {scenario}"
    return JUDGE_TEMPLATE.format(rubric=rubric, criteria=criteria_text, transcript="\n\n".join(transcript),
                                 changes="\n".join(changes))


def judge_command(cond):
    return ["claude", "-p", "--model", cond["judge_model"], "--effort", cond["judge_effort"],
            "--setting-sources", "project", "--strict-mcp-config", "--permission-mode", "dontAsk",
            "--output-format", "json", "--no-session-persistence"]


def parse_judgment(stdout, criteria):
    """Return per-criterion results; malformed output makes every criterion inconclusive."""
    def everything(reason):
        return {c: {"result": "inconclusive", "evidence": reason} for c in criteria}
    try:
        envelope = json.loads(stdout)
        text = envelope["result"] if isinstance(envelope, dict) else None
        if not isinstance(text, str):
            return everything("judge envelope has no result text")
        text = text.strip()
        fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL)
        data = json.loads(fenced.group(1) if fenced else text)
    except (json.JSONDecodeError, TypeError, KeyError) as error:
        return everything(f"judge output malformed: {error}")
    if not isinstance(data, dict):
        return everything("judge output is not a JSON object")
    out = {}
    for criterion in criteria:
        value = data.get(criterion)
        if isinstance(value, dict) and value.get("result") in JUDGED_STATES:
            out[criterion] = {"result": value["result"], "evidence": str(value.get("evidence", ""))}
        else:
            out[criterion] = {"result": "inconclusive", "evidence": "judge gave no valid result for this criterion"}
    return out


def _call_judge(cond, prompt, out_dir, stem, executor, work_root, guard):
    work_root = guard(work_root or default_work_root())
    cwd = work_root / f"judge-{uuid.uuid4().hex[:8]}"
    cwd.mkdir(parents=True)
    (out_dir / f"{stem}.prompt.txt").write_text(prompt)
    args = judge_command(cond)
    record = {"command": args, "cwd": str(cwd), "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()}
    stdout = stderr = ""
    try:
        proc = executor(args, input=prompt, text=True, capture_output=True, cwd=cwd,
                        timeout=cond["timeout_seconds"], env=actor_env()[0])
        stdout, stderr, record["exit_code"] = _text(proc.stdout), _text(proc.stderr), proc.returncode
    except subprocess.TimeoutExpired as error:
        stdout, stderr, record["error"] = _text(error.stdout), _text(error.stderr), "judge timeout"
    except OSError as error:
        record["error"] = f"judge launch failed: {error}"
    finally:
        (out_dir / f"{stem}.stdout.json").write_text(stdout)
        (out_dir / f"{stem}.stderr.txt").write_text(stderr)
        try:
            cwd.rmdir()
        except OSError:
            record["cwd_left"] = "judge directory not empty; kept for inspection"
    try:
        envelope = json.loads(stdout)
        record.update({"usage": envelope.get("usage"), "cost_usd": envelope.get("total_cost_usd")})
    except (json.JSONDecodeError, AttributeError):
        pass
    save(out_dir / f"{stem}.call.json", record)
    return stdout


def require_judge_template(cond):
    if cond["judge_prompt_sha256"] != JUDGE_PROMPT_SHA256:
        raise ValueError("judge prompt template changed after freeze; freeze a new condition")


def judge(trial_dir, *, executor=execute, work_root=None, guard=check_work_root):
    trial_dir, trial, cond, case = _trial_context(trial_dir)
    require_judge_template(cond)
    rubric_text = (pathlib.Path(cond["dir"]) / "rubric.md").read_text()
    criteria = rubric_criteria(rubric_section(rubric_text, trial["scenario"]))
    if not criteria:
        judged = {}
    elif trial["status"] != "captured":
        state = trial["status"] if trial["status"] in ("setup-blocked", "invalid") else "inconclusive"
        judged = {c: {"result": state, "evidence": f"trial status is {trial['status']}; judge not called"}
                  for c in criteria}
    else:
        recorded = trial.get("turn_texts") or []
        turn_texts = []
        for index, reply in enumerate(trial["replies"]):
            texts = list(recorded[index]) if index < len(recorded) else []
            if reply is not None and (not texts or texts[-1] != reply):
                texts.append(reply)
            turn_texts.append(texts)
        prompt = build_judge_prompt(rubric_text, trial["scenario"], criteria, case["turns"], turn_texts,
                                    trial["changed"], trial["files"])
        stdout = _call_judge(cond, prompt, trial_dir, "judge", executor, work_root, guard)
        judged = parse_judgment(stdout, criteria)
    save(trial_dir / "judged.json", judged)
    save_provenance(trial_dir, "judge")
    return judged


def calibrate(condition, cases_path, out, *, executor=execute, work_root=None, guard=check_work_root):
    cond = load_condition(condition)
    require_judge_template(cond)
    rubric_text = (pathlib.Path(cond["dir"]) / "rubric.md").read_text()
    out = check_output_location(out)
    cases = load_json(cases_path)
    out.mkdir(parents=True, exist_ok=False)
    rows, matches = [], 0
    for index, case in enumerate(cases, 1):
        criterion = case["criterion"]
        files = case.get("files") or {}
        changed = {"added": [], "modified": sorted(files), "deleted": []}
        prompt = build_judge_prompt(rubric_text, case["scenario"], [criterion], case.get("turns") or [],
                                    [[r] for r in case.get("replies") or [case.get("reply")]], changed, files)
        stem = f"case-{index:02d}-{re.sub(r'[^A-Za-z0-9_.-]', '_', str(case.get('id', index)))}"
        got = parse_judgment(_call_judge(cond, prompt, out, stem, executor, work_root, guard), [criterion])[criterion]
        match = got["result"] == case["expected"]
        matches += match
        rows.append({"id": case.get("id", index), "scenario": case["scenario"], "criterion": criterion,
                     "expected": case["expected"], "judged": got["result"], "evidence": got["evidence"],
                     "match": match})
    summary = {"matches": matches, "total": len(rows), "judge_model": cond["judge_model"],
               "judge_effort": cond["judge_effort"], "judge_prompt_sha256": JUDGE_PROMPT_SHA256,
               "cases_sha256": digest(cases_path), "mismatches": [r for r in rows if not r["match"]], "cases": rows}
    save(out / "calibration.json", summary)
    lines = [f"# Judge calibration", "", f"Agreement: {matches} / {len(rows)}", "",
             f"Judge: {cond['judge_model']} at {cond['judge_effort']} effort; prompt template sha256 "
             f"`{JUDGE_PROMPT_SHA256}`.", ""]
    if summary["mismatches"]:
        lines += ["| Case | Criterion | Expected | Judged | Judge evidence |", "| --- | --- | --- | --- | --- |"]
        lines += [f"| {r['id']} | {r['criterion']} | {r['expected']} | {r['judged']} | "
                  f"{r['evidence'].replace('|', '/')} |" for r in summary["mismatches"]]
    else:
        lines.append("No mismatches.")
    (out / "calibration.md").write_text("\n".join(lines) + "\n")
    return summary


# ---------------------------------------------------------------- report, reference, compare

def combined_results(trial_dir):
    trial_dir, trial, cond, case = _trial_context(trial_dir)
    if not (trial_dir / "computed.json").exists():
        raise ValueError(f"{trial_dir} has no computed.json; run grade first")
    computed = load_json(trial_dir / "computed.json")
    judged_path = trial_dir / "judged.json"
    judged = load_json(judged_path) if judged_path.exists() else None
    criteria = rubric_criteria(rubric_section((pathlib.Path(cond["dir"]) / "rubric.md").read_text(), trial["scenario"]))
    applicable = set(case.get("checks") or [])
    results = {}
    for check in CHECK_IDS:
        if check not in applicable:
            unlisted = computed.get(check) or {}
            # AC8: a computed C8 fail (outer repository changed) counts even when C8 is not listed.
            results[check] = unlisted if check == "C8" and unlisted.get("result") == "fail" else \
                {"result": "not-applicable", "evidence": "check not listed for this scenario"}
            continue
        own = [c for c in criteria if c.split(".", 1)[0] == check]
        judged_part = None
        if own:
            if judged is None:
                judged_part = {"result": "inconclusive", "evidence": "not judged"}
            else:
                judged_part = checks.combine(*[
                    {"result": judged[c]["result"], "evidence": f"{c}: {judged[c]['evidence']}"} if c in judged
                    else {"result": "inconclusive", "evidence": f"{c}: missing from judged.json"} for c in own])
        computed_part = computed.get(check)
        if computed_part is None and judged_part is None:
            results[check] = {"result": "inconclusive", "evidence": "no computed part and no judged criterion"}
        else:
            results[check] = checks.combine(computed_part, judged_part)
    return trial, cond, results, judged is not None


def report(run_dir, out):
    run_dir, out = pathlib.Path(run_dir).resolve(), check_output_location(out)
    trial_files = sorted(run_dir.rglob("trial.json"))
    if not trial_files:
        raise ValueError(f"no trial.json under {run_dir}")
    seen = {}
    for path in trial_files:
        trial = load_json(path)
        key = (trial["host"], trial["scenario"], trial["trial"])
        if key in seen:
            raise ValueError(f"duplicate trial {key}: {seen[key]} and {path.parent}; a report needs one directory "
                             "per host, scenario, and trial")
        seen[key] = path.parent
    counts, trials, grading = {}, [], []
    for path in trial_files:
        trial, cond, results, was_judged = combined_results(path.parent)
        # Only the grade step decides the computed results; judge-provenance.json stays a
        # record of the judge step and is not merged here.
        record = path.parent / "grade-provenance.json"
        if record.exists():
            hashes_used = load_json(record)["code_hashes"]
            if hashes_used not in grading:
                grading.append(hashes_used)
        host_counts = counts.setdefault(trial["host"], {c: {s: 0 for s in STATES} for c in CHECK_IDS})
        for check, value in results.items():
            host_counts[check][value["result"]] += 1
        turns = trial.get("capture", {}).get("turns") or []
        trials.append({"dir": str(path.parent), "host": trial["host"], "scenario": trial["scenario"],
                       "trial": trial["trial"], "status": trial["status"], "judged": was_judged,
                       "condition": cond["dir"], "condition_sha256": trial["condition_sha256"],
                       "outer_changed": trial["outer_changed"], "commits_added": trial["commits_added"],
                       "refs_changed": trial.get("refs_changed"), "changed": trial.get("changed"),
                       "code_changed_since_freeze": cond["code_changed_since_freeze"],
                       "elapsed_seconds": trial.get("capture", {}).get("elapsed_seconds"),
                       "cost_usd": trial.get("cost_usd"),
                       "results": results})
    out.mkdir(parents=True, exist_ok=True)
    counts["grading_code_hashes"] = grading
    save(out / "report.json", counts)
    save(out / "report-trials.json", trials)
    (out / "report.md").write_text(render_report(counts, trials))
    return counts


def render_report(counts, trials):
    lines = ["# Loop conformance report", "",
             "Counts are trials per result. Graded = pass + fail. Inconclusive, setup-blocked, and "
             "not-applicable trials are excluded from graded counts.", ""]
    for host in sorted(h for h in counts if h in HOSTS):
        lines += [f"## {host}", "",
                  "| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for check in CHECK_IDS:
            c = counts[host][check]
            lines.append(f"| {check} | {c['pass']} | {c['fail']} | {c['pass'] + c['fail']} | {c['inconclusive']} | "
                         f"{c['setup-blocked']} | {c['not-applicable']} | {c['invalid']} |")
        lines.append("")
    letters = {"pass": "P", "fail": "F", "inconclusive": "I", "setup-blocked": "B", "not-applicable": "-",
               "invalid": "X"}
    lines += ["## Trials", "", "P pass, F fail, I inconclusive, B setup-blocked, X invalid, - not applicable.", "",
              "| Host | Scenario | Trial | Status | Judged | Outer changed | Seconds | " + " | ".join(CHECK_IDS) + " |",
              "| --- | --- | --- | --- | --- | --- | --- | " + " | ".join("---" for _ in CHECK_IDS) + " |"]
    for t in sorted(trials, key=lambda t: (t["host"], t["scenario"], t["trial"])):
        seconds = f"{t['elapsed_seconds']:.0f}" if isinstance(t["elapsed_seconds"], (int, float)) else ""
        lines.append(f"| {t['host']} | {t['scenario']} | {t['trial']} | {t['status']} | {'yes' if t['judged'] else 'no'} | "
                     f"{'yes' if t['outer_changed'] else 'no'} | {seconds} | "
                     + " | ".join(letters[t["results"][c]["result"]] for c in CHECK_IDS) + " |")
    drift = sorted({name for t in trials for name in t.get("code_changed_since_freeze") or []})
    if drift:
        lines += ["", f"Warning: {', '.join(drift)} changed after the condition was frozen. Captures used the "
                  "frozen code; grading and this report used the current code."]
    invalid = [t for t in trials if t["status"] == "invalid"]
    lines += ["", "## Evaluator-material access", ""]
    lines += ([f"- {t['host']} {t['scenario']} trial {t['trial']} is invalid; see evaluator_access in "
               f"{t['dir']}/trial.json" for t in invalid] or ["No trial accessed evaluator material."])
    outer = [t for t in trials if t["outer_changed"]]
    lines += ["", "## Outer repository", ""]
    lines += ([f"- Files of the suite's repository changed during {t['host']} {t['scenario']} trial {t['trial']} "
               f"(status {t['status']}): {t['dir']}" for t in outer]
              or ["No trial changed files of the suite's repository."])
    excluded = [t for t in trials if t["status"] in ("inconclusive", "setup-blocked", "invalid")]
    lines += ["", "## Boundary evidence of excluded trials", "",
              "Informational: these trials are not counted as pass or fail.", ""]
    for t in sorted(excluded, key=lambda t: (t["host"], t["scenario"], t["trial"])):
        changed = t.get("changed") or {}
        paths = [f"{kind} {p}" for kind in ("added", "modified", "deleted") for p in changed.get(kind, [])]
        lines.append(f"- {t['host']} {t['scenario']} {t['trial']} ({t['status']}): commits_added "
                     f"{t['commits_added']}, refs_changed {t.get('refs_changed')}, outer_changed "
                     f"{t['outer_changed']}, changed paths: {', '.join(paths) or 'none'}")
    if not excluded:
        lines.append("No excluded trials.")
    lines += ["", "## Non-pass evidence", ""]
    for t in sorted(trials, key=lambda t: (t["host"], t["scenario"], t["trial"])):
        for check in CHECK_IDS:
            value = t["results"][check]
            if value["result"] in ("fail", "inconclusive", "setup-blocked", "invalid"):
                evidence = value["evidence"].replace("\n", " ")[:300]
                lines.append(f"- {t['host']} {t['scenario']} {t['trial']} {check} {value['result']}: {evidence}")
    return "\n".join(lines) + "\n"


REFERENCE_CONDITION_FIELDS = comparison.CONDITION_FIELDS + comparison.WARNING_FIELDS + (
    "plugin_hashes", "code_hashes", "timeout_seconds", "max_trials", "permissions", "isolation")


def run_record(report_path, condition):
    """Build a reference-shaped record from report.json for the condition's host."""
    report_path = pathlib.Path(report_path).resolve()
    cond = load_condition(condition)
    counts = load_json(report_path)
    if cond["host"] not in counts:
        raise ValueError(f"report has no trials for host {cond['host']}")
    trials_path = report_path.parent / "report-trials.json"
    host_trials = [t for t in load_json(trials_path) if t["host"] == cond["host"]]
    foreign = [t["dir"] for t in host_trials if t["condition_sha256"] != cond["sha256"]]
    if foreign:
        raise ValueError(f"trials from another condition are in this report: {foreign[:3]}")
    return {"host": cond["host"], "condition": {k: cond.get(k) for k in REFERENCE_CONDITION_FIELDS},
            "counts": counts[cond["host"]], "trials": len(host_trials),
            "scenario_trials": sorted({(t["scenario"], t["trial"]) for t in host_trials}),
            "grading_code_hashes": counts.get("grading_code_hashes") or []}


def make_reference(report_path, condition, out):
    record = run_record(report_path, condition)
    record["created_at_unix"] = time.time()
    out = pathlib.Path(out)
    if out.exists():
        raise FileExistsError(f"{out} exists; remove it deliberately before storing a new reference")
    out.parent.mkdir(parents=True, exist_ok=True)
    save(out, record)
    return record


def compare_run(reference_path, report_path, condition):
    reference = load_json(reference_path)
    candidate = run_record(report_path, condition)
    outcome = comparison.compare(reference, candidate)
    out = pathlib.Path(report_path).resolve().parent
    save(out / "compare.json", outcome)
    (out / "compare.md").write_text(comparison.render(outcome))
    return outcome


# ---------------------------------------------------------------- CLI

def main(argv=None):
    """Run one subcommand; a refused operation prints its reason and exits with status 2."""
    try:
        return _main(argv)
    except (ValueError, FileExistsError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


def _main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    p = sub.add_parser("freeze", help="copy the plugin and suite into a new condition directory")
    p.add_argument("--plugin", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path, required=True)
    p.add_argument("--host", choices=HOSTS, required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--effort", required=True)
    p.add_argument("--timeout", type=int, default=900)
    p.add_argument("--judge-model", required=True)
    p.add_argument("--judge-effort", required=True)
    p.add_argument("--max-trials", type=int, default=5)
    p = sub.add_parser("prepare", help="create one trial workspace and its frozen inputs")
    p.add_argument("--condition", type=pathlib.Path, required=True)
    p.add_argument("--scenario", required=True)
    p.add_argument("--trial", type=int, required=True)
    p.add_argument("--work-root", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path, required=True)
    p = sub.add_parser("run", help="run every turn of a prepared trial and write trial.json")
    p.add_argument("--trial", type=pathlib.Path, required=True)
    p = sub.add_parser("grade", help="write computed.json for a trial")
    p.add_argument("--trial", type=pathlib.Path, required=True)
    p = sub.add_parser("judge", help="write judged.json for a trial, or run judge calibration")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--trial", type=pathlib.Path)
    group.add_argument("--calibration", type=pathlib.Path)
    p.add_argument("--condition", type=pathlib.Path, help="required with --calibration")
    p.add_argument("--out", type=pathlib.Path, help="new output directory, required with --calibration")
    p.add_argument("--work-root", type=pathlib.Path)
    p = sub.add_parser("report", help="aggregate graded trials into report.json and report.md")
    p.add_argument("--run", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path, required=True)
    p = sub.add_parser("reference", help="store a reference file for one host")
    p.add_argument("--report", type=pathlib.Path, required=True)
    p.add_argument("--condition", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path, required=True)
    p = sub.add_parser("compare", help="compare a report with a stored reference")
    p.add_argument("--reference", type=pathlib.Path, required=True)
    p.add_argument("--report", type=pathlib.Path, required=True)
    p.add_argument("--condition", type=pathlib.Path, required=True)
    args = parser.parse_args(argv)
    if args.action == "freeze":
        print(freeze(args.plugin, args.out, args.host, args.model, args.effort, args.timeout,
                     args.judge_model, args.judge_effort, max_trials=args.max_trials))
    elif args.action == "prepare":
        print(prepare(args.condition, args.scenario, args.trial, args.out, args.work_root))
    elif args.action == "run":
        trial = run_trial(args.trial)
        print(json.dumps({k: trial[k] for k in ("scenario", "host", "trial", "status", "changed",
                                                "commits_added", "outer_changed", "workers")}, indent=2))
    elif args.action == "grade":
        print(json.dumps(grade(args.trial), indent=2))
    elif args.action == "judge" and args.calibration:
        if not args.condition or not args.out:
            parser.error("--calibration needs --condition and --out")
        summary = calibrate(args.condition, args.calibration, args.out, work_root=args.work_root)
        print(f"agreement {summary['matches']} / {summary['total']}")
        for row in summary["mismatches"]:
            print(f"mismatch {row['id']} {row['criterion']}: expected {row['expected']}, judged {row['judged']}")
    elif args.action == "judge":
        print(json.dumps(judge(args.trial, work_root=args.work_root), indent=2))
    elif args.action == "report":
        report(args.run, args.out)
        print((pathlib.Path(args.out) / "report.md").read_text())
    elif args.action == "reference":
        record = make_reference(args.report, args.condition, args.out)
        print(f"reference for {record['host']} written to {args.out}")
    else:
        outcome = compare_run(args.reference, args.report, args.condition)
        print(comparison.render(outcome))
        return {"pass": 0, "fail": 1, "flagged": 1, "refused": 2, "insufficient": 3}[outcome["status"]]
    return 0


if __name__ == "__main__":
    sys.exit(main())
