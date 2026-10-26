#!/usr/bin/env python3
"""Small sequential capture harness. Semantic grading stays independent and manual."""
import argparse
from collections import Counter
import hashlib
import json
import os
import pathlib
import shutil
import signal
import subprocess
import time
import uuid

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RUNNER_SOURCE = pathlib.Path(__file__).read_bytes()
RUNNER_SHA256 = hashlib.sha256(RUNNER_SOURCE).hexdigest()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hashes(root):
    return {str(p.relative_to(root)): digest(p) for p in sorted(root.rglob("*"))
            if p.is_file() and ".git" not in p.relative_to(root).parts and "__pycache__" not in p.parts}


def save(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def local_output(path):
    path = pathlib.Path(path).resolve()
    if not path.is_relative_to(ROOT / "tmp/evidence-aware-eval"):
        raise ValueError("outputs must be under repo tmp/evidence-aware-eval")
    return path


def freeze(plugin, out, model, effort, timeout):
    out = local_output(out)
    out.mkdir(parents=True, exist_ok=False)
    shutil.copytree(plugin, out / "plugin")
    for name in ("scenarios.json", "rubric.md", "suite.lock.json"):
        shutil.copy2(HERE / name, out / name)
    for name, expected in json.loads((out / "suite.lock.json").read_text()).items():
        if digest(out / name) != expected:
            raise ValueError("suite changed after freeze; do not run or silently refresh the lock")
    save(out / "condition.json", {"model": model, "effort": effort, "timeout_seconds": timeout,
         "host": "Codex CLI; direct local skill loading (not plugin installation)",
         "permissions": "workspace-write; no approval bypass; no network requested",
         "tdd": "targeted; user authorization retained by coordinator",
         "frozen_at_unix": time.time(), "plugin_hashes": hashes(out / "plugin"),
         "suite_hashes": {n: digest(out / n) for n in ("scenarios.json", "rubric.md", "suite.lock.json")}})
    return out


def load_condition(condition):
    condition = pathlib.Path(condition).resolve()
    data = json.loads((condition / "condition.json").read_text())
    if hashes(condition / "plugin") != data["plugin_hashes"]:
        raise ValueError("frozen plugin changed")
    if any(digest(condition / n) != h for n, h in data["suite_hashes"].items()):
        raise ValueError("frozen suite changed")
    return data


def prepare(condition, scenario, trial, out):
    condition = pathlib.Path(condition).resolve()
    load_condition(condition)
    if trial not in (1, 2, 3):
        raise ValueError("trial must be 1, 2, or 3; frozen budget is three fresh trials")
    case = json.loads((condition / "scenarios.json").read_text())[scenario]
    out = local_output(out)
    out.mkdir(parents=True, exist_ok=False)
    workspace = out / "workspace"
    workspace.mkdir()
    subprocess.run(["git", "init", "--quiet", str(workspace)], check=True)
    for name, content in case["files"].items():
        target = workspace / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    (workspace / "AGENTS.md").write_text(
        "This is an isolated synthetic exercise. Write only within this workspace. "
        "Do not commit, install packages, use the network, or change host settings. "
        "Treat supplied frozen skill resources as read-only. User instructions define scope.\n")
    for index, prompt in enumerate(case["turns"], 1):
        prefix = (f"Use the Lusona {case['skill']} skill at "
                  f"{condition}/plugin/skills/{case['skill']}/SKILL.md and applicable linked instructions. "
                  "The synthetic workspace is your consuming project. Read only this workspace and the frozen plugin resources. "
                  "Do not inspect evaluator files, parent directories, rubrics, or other trials.\n\n") if index == 1 else ""
        (out / f"turn-{index}.input.txt").write_text(prefix + prompt + "\n")
    save(out / "run.json", {"condition": str(condition), "scenario": scenario,
         "trial": trial, "turns": len(case["turns"]), "prepared_runner_sha256": RUNNER_SHA256,
         "initial_hashes": hashes(workspace),
         "input_hashes": {p.name: digest(p) for p in out.glob("*.input.txt")}})
    return out


def command(settings, run, session):
    args = ["codex", "exec", "--ignore-user-config", "--enable", "multi_agent", "--sandbox", "workspace-write",
            "--json", "--model", settings["model"], "-c",
            "model_reasoning_effort=" + json.dumps(settings["effort"]),
            "-C", str(run / "workspace"), "--skip-git-repo-check"]
    return args + (["resume", session, "-"] if session else ["-"])


def execute(args, *, input, text, capture_output, cwd, timeout):
    """On timeout stop only our private process group before returning evidence."""
    with subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=text, cwd=cwd,
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


def supplement(run, turn, sessions_root=None):
    """Append independent, cumulative evidence from only the returned session UUID."""
    run = local_output(run)
    result = json.loads((run / f"turn-{turn}.result.json").read_text())
    session = result.get("session")
    stem = run / f"turn-{turn}.session-supplement-{time.time_ns()}"
    metadata = {"scope": "cumulative-session-supplement", "per_turn_snapshot": False,
                "captured_at_unix": time.time(), "session": session,
                "associated_result": f"turn-{turn}.result.json", "status": "unavailable",
                "runner_sha256": RUNNER_SHA256,
                "limits": "May include later resumed turns; not original per-turn evidence. Root CLI usage is not total worker cost. Tool arguments may be encrypted by the host; preserved as stored.",
                "prompt_sources": [p.name for p in sorted(run.glob("*.input.txt"))]}
    try:
        if str(uuid.UUID(session)) != session:
            raise ValueError("session is not a canonical returned UUID")
        sessions_root = pathlib.Path(sessions_root) if sessions_root else pathlib.Path.home() / ".codex/sessions"
        matches = list(sessions_root.rglob(f"rollout-*-{session}.jsonl"))
        if len(matches) != 1:
            raise ValueError(f"expected one rollout for the explicit UUID; found {len(matches)}")
        source = matches[0]
        raw = source.read_bytes()
        selected, workers, calls, malformed = [], set(), Counter(), 0
        tool_keys = {"type", "id", "status", "call_id", "name", "namespace", "arguments", "input", "output"}
        for number, line in enumerate(raw.splitlines(), 1):
            try:
                event = json.loads(line)
            except (json.JSONDecodeError, UnicodeDecodeError):
                malformed += 1
                continue
            if not isinstance(event, dict):
                malformed += 1
                continue
            if event.get("type") not in ("response_item", "event_msg"):
                continue
            if not isinstance(event.get("payload"), dict):
                malformed += 1
                continue
            payload = event.get("payload", {})
            kind = payload.get("type")
            if not isinstance(kind, str):
                malformed += 1
                continue
            filtered = None
            if event.get("type") == "response_item":
                if kind in {"function_call", "function_call_output", "custom_tool_call", "custom_tool_call_output"}:
                    filtered = {k: v for k, v in payload.items() if k in tool_keys}
                    if kind in {"function_call", "custom_tool_call"}:
                        name = payload.get("name", "unnamed")
                        if not isinstance(name, str):
                            malformed += 1
                            continue
                        calls[name] += 1
                elif kind == "message" and payload.get("role") == "assistant":
                    filtered = {k: v for k, v in payload.items() if k in {"type", "role", "content", "phase"}}
            elif event.get("type") == "event_msg":
                if kind == "item_completed" and not isinstance(payload.get("item"), dict):
                    malformed += 1
                    continue
                if kind == "item_completed" and payload["item"].get("type") == "SubAgentActivity":
                    item = payload["item"]
                    filtered = {"type": kind, "turn_id": payload.get("turn_id"), "item": {
                        k: v for k, v in item.items() if k in {"type", "id", "kind", "model", "reasoning_effort", "agent_thread_id", "agent_path"}}}
                    if isinstance(item.get("agent_thread_id"), str) and item["agent_thread_id"]:
                        workers.add(item["agent_thread_id"])
                elif kind in {"task_started", "task_complete"}:
                    filtered = {k: v for k, v in payload.items() if k in {
                        "type", "turn_id", "root_turn_id", "duration_ms", "time_to_first_token_ms"}}
            if filtered is not None:
                selected.append({"source_line": number, "timestamp": event.get("timestamp"),
                                 "type": event["type"], "payload": filtered})
        trace = pathlib.Path(str(stem) + ".jsonl")
        with trace.open("x") as stream:
            for event in selected:
                stream.write(json.dumps(event, sort_keys=True) + "\n")
        metadata.update({"status": "captured", "trace": str(trace), "trace_sha256": digest(trace),
                         "source_locator": str(source.relative_to(sessions_root)), "source_bytes_read": len(raw),
                         "filtered_events": len(selected), "malformed_or_partial_lines": malformed,
                         "observed_tool_calls": dict(calls), "observed_worker_threads": len(workers) if workers else None,
                         "worker_count_basis": "distinct observed SubAgentActivity agent_thread_id; unavailable when absent"})
        if malformed:
            metadata["status"] = "incomplete"
            metadata["diagnostic"] = f"Skipped {malformed} malformed, partial, or wrong-shaped lines; supplement incomplete."
    except (OSError, ValueError, TypeError) as error:
        metadata["error"] = str(error)
    save(pathlib.Path(str(stem) + ".json"), metadata)
    return metadata


def capture(run, executor=execute):
    run = pathlib.Path(run).resolve()
    meta = json.loads((run / "run.json").read_text())
    settings = load_condition(meta["condition"])
    index, session = 1, None
    while (run / f"turn-{index}.result.json").exists():
        previous = json.loads((run / f"turn-{index}.result.json").read_text())
        if previous["status"] != "captured" or not previous.get("session"):
            raise ValueError("previous turn did not complete capture; retain it and resolve setup before any new trial")
        session = previous["session"]
        index += 1
    if index > meta["turns"]:
        raise ValueError("all frozen turns already captured")
    prompt_path = run / f"turn-{index}.input.txt"
    if digest(prompt_path) != meta["input_hashes"][prompt_path.name]:
        raise ValueError("frozen trial input changed")
    args = command(settings, run, session)
    (run / f"turn-{index}.runner.py").write_bytes(RUNNER_SOURCE)
    save(run / f"turn-{index}.before.json", hashes(run / "workspace"))
    started = time.time()
    result = {"command": args, "started_at_unix": started, "status": "setup-blocked",
              "resumed_session": session, "session": session, "grading": "ungraded",
              "runner_sha256": RUNNER_SHA256}
    try:
        result["cli_version"] = subprocess.run(["codex", "--version"], text=True, capture_output=True).stdout.strip()
        proc = executor(args, input=prompt_path.read_text(), text=True, capture_output=True,
                        cwd=run / "workspace", timeout=settings["timeout_seconds"])
        (run / f"turn-{index}.stdout.jsonl").write_text(proc.stdout)
        (run / f"turn-{index}.stderr.txt").write_text(proc.stderr)
        result["exit_code"] = proc.returncode
        result["usage_scope"] = "Root CLI reported usage; not total worker cost."
        completed = False
        for line in proc.stdout.splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("type") == "thread.started":
                result["session"] = event["thread_id"]
            if event.get("type") == "turn.completed":
                completed = True
                result["usage"] = event.get("usage")
        if proc.returncode == 0 and completed and result["session"]:
            result["status"] = "captured"
    except subprocess.TimeoutExpired as error:
        result["status"] = "inconclusive"
        result["error"] = "host timeout; partial transcript retained"
        (run / f"turn-{index}.stdout.jsonl").write_text((error.stdout or b"").decode() if isinstance(error.stdout, bytes) else (error.stdout or ""))
        (run / f"turn-{index}.stderr.txt").write_text((error.stderr or b"").decode() if isinstance(error.stderr, bytes) else (error.stderr or ""))
    except OSError as error:
        result["error"] = str(error)
    finally:
        result["elapsed_seconds"] = time.time() - started
        save(run / f"turn-{index}.after.json", hashes(run / "workspace"))
        shutil.copytree(run / "workspace", run / f"turn-{index}.artifacts", ignore=shutil.ignore_patterns(".git"))
        save(run / f"turn-{index}.result.json", result)
    supplement(run, index)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    freeze_parser = sub.add_parser("freeze")
    freeze_parser.add_argument("--plugin", type=pathlib.Path, required=True)
    freeze_parser.add_argument("--out", type=pathlib.Path, required=True)
    freeze_parser.add_argument("--model", required=True)
    freeze_parser.add_argument("--effort", choices=["low", "medium", "high", "xhigh"], required=True)
    freeze_parser.add_argument("--timeout", type=int, default=300)
    prepare_parser = sub.add_parser("prepare")
    prepare_parser.add_argument("--condition", type=pathlib.Path, required=True)
    prepare_parser.add_argument("--scenario", required=True)
    prepare_parser.add_argument("--trial", type=int, required=True)
    prepare_parser.add_argument("--out", type=pathlib.Path, required=True)
    turn_parser = sub.add_parser("turn")
    turn_parser.add_argument("--run", type=pathlib.Path, required=True)
    supplement_parser = sub.add_parser("supplement")
    supplement_parser.add_argument("--run", type=pathlib.Path, required=True)
    supplement_parser.add_argument("--turn", type=int, required=True)
    args = vars(parser.parse_args())
    action = args.pop("action")
    if action == "freeze":
        result = str(freeze(**args))
    elif action == "prepare":
        result = str(prepare(**args))
    elif action == "supplement":
        result = supplement(**args)
    else:
        result = capture(**args)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
