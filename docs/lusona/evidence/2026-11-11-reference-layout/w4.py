#!/usr/bin/env python3
"""W4 reference-layout experiment: fixtures, trials, analysis. Repo-local scratch only."""
import hashlib, json, os, re, shutil, subprocess, sys, time
from pathlib import Path

W4 = Path(__file__).resolve().parent
# Repository root: the nearest ancestor holding AGENTS.md (the script first ran from tmp/w4).
REPO = next(p for p in W4.parents if (p / "AGENTS.md").is_file())
FIX, WS, RUNS = W4 / "fixtures", W4 / "ws", W4 / "runs"
CONDS = ("L1-link", "L1-bare", "L2-link", "L2-bare")
TASK = "Write the release note for version 1.4.0. Change: fixed the login timeout."
CLAUDE_SETTINGS = {
    "sandbox": {"enabled": True, "autoAllowBashIfSandboxed": True, "allowUnsandboxedCommands": False,
                "failIfUnavailable": True, "network": {"allowedDomains": []}},
    "permissions": {"blockWritesOutsideWorkingDirectories": True},
    # Added after probe-claude-1: the repository CLAUDE.md above tmp/w4 reached the actor.
    "claudeMdExcludes": [str(REPO / "CLAUDE.md"), str(REPO / "AGENTS.md")],
}
STRIP_ENV = re.compile(r"^(CLAUDECODE|CLAUDE_PID|CLAUDE_EFFORT|CLAUDE_CODE_.*)$")
KEEP_ENV = {"CLAUDE_CODE_OAUTH_TOKEN", "CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX", "CLAUDE_CODE_USE_FOUNDRY"}
SKILL = """---
name: release-note
description: Write a release note into RELEASE.md. Use when the user asks for a release note.
---

# Release note

Write the release note to `RELEASE.md` in the project root.

Before writing the release note, read {ref}.

Use the version and changes the user gives. Do not ask questions.
"""
REF = """# Release-note format

The first line of every release note is exactly: `Format-ID: {marker}`
After it, a level-2 heading with the version, then one bullet per change.
"""


def marker(cond):
    return f"W4REF-{cond}-" + hashlib.sha256(("w4" + cond).encode()).hexdigest()[:8]


def make_fixtures():
    for cond in CONDS:
        root = FIX / cond
        if root.exists():
            shutil.rmtree(root)
        skill = root / "skills/release-note"
        skill.mkdir(parents=True)
        (root / ".claude-plugin").mkdir()
        (root / ".claude-plugin/plugin.json").write_text(json.dumps(
            {"name": "w4fix", "version": "0.0.1", "description": "W4 reference layout fixture"}, indent=2) + "\n")
        layout, form = cond.split("-")
        refdir = root / "references" if layout == "L1" else skill / "references"
        refdir.mkdir(parents=True)
        (refdir / "release-format.md").write_text(REF.format(marker=marker(cond)))
        if form == "link":
            target = "../../references/release-format.md" if layout == "L1" else "references/release-format.md"
            ref = f"[the release-note format]({target})"
        else:
            ref = "`references/release-format.md`"
        (skill / "SKILL.md").write_text(SKILL.format(ref=ref))


def make_ws(name):
    ws = WS / name
    if ws.exists():
        raise SystemExit(f"workspace exists: {ws}")
    ws.mkdir(parents=True)
    (ws / "CHANGES.txt").write_text("1.4.0: fixed the login timeout\n")
    g = ["git", "-C", str(ws), "-c", "user.name=w4", "-c", "user.email=w4@example.invalid", "-c", "commit.gpgsign=false"]
    subprocess.run(["git", "init", "-q", str(ws)], check=True)
    subprocess.run(g + ["add", "."], check=True)
    subprocess.run(g + ["commit", "-q", "-m", "fixture"], check=True)
    return ws


def env(host):
    e = {k: v for k, v in os.environ.items() if not (STRIP_ENV.match(k) and k not in KEEP_ENV)}
    if host == "claude":
        e["CLAUDE_CODE_SHELL"] = "/bin/bash"
    return e


def claude_cmd(plugin):
    return ["claude", "-p", "--plugin-dir", str(plugin), "--output-format", "stream-json", "--verbose",
            "--model", "claude-opus-5-5", "--effort", "high", "--setting-sources", "project",
            "--strict-mcp-config", "--settings", json.dumps(CLAUDE_SETTINGS, sort_keys=True),
            "--permission-mode", "dontAsk", "--max-budget-usd", "1.50",
            "--allowedTools", "Read", "Edit", "Write", "Skill", "Task", "Agent", "Bash"]


def codex_cmd(ws):
    return ["codex", "exec", "--ignore-user-config", "--sandbox", "workspace-write", "--json",
            "--model", "gpt-6.1-sol", "-c", 'model_reasoning_effort="medium"', "-C", str(ws),
            "--skip-git-repo-check", "-"]


def launch(host, name, prompt, plugin=None):
    ws = make_ws(name)
    out = RUNS / name
    out.mkdir(parents=True)
    args = claude_cmd(plugin or FIX / "L1-link") if host == "claude" else codex_cmd(ws)
    (out / "command.json").write_text(json.dumps({"args": args, "cwd": str(ws), "prompt": prompt}, indent=2))
    t0 = time.time()
    try:
        p = subprocess.run(args, input=prompt, text=True, capture_output=True, cwd=ws, env=env(host), timeout=900)
        rc, so, se = p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired as err:
        rc, so, se = "timeout", err.stdout or "", err.stderr or ""
        so = so.decode() if isinstance(so, bytes) else so
        se = se.decode() if isinstance(se, bytes) else se
    (out / "stdout.jsonl").write_text(so)
    (out / "stderr.txt").write_text(se)
    rel = ws / "RELEASE.md"
    meta = {"name": name, "host": host, "rc": rc, "seconds": round(time.time() - t0, 1),
            "release_md": rel.read_text() if rel.exists() else None}
    (out / "meta.json").write_text(json.dumps(meta, indent=2))
    return out


def events(text):
    for line in text.splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(e, dict):
            yield e


SEARCH = re.compile(r"""(^|[\s;&|("'])(ls|find|fd|tree|rg --files|grep -r|grep -R|rg)\b""")


def calls_claude(text):
    """Ordered list of (tool, input_text, output_text, is_error) for root-agent tool calls."""
    pending, order, out = {}, [], []
    init = None
    expanded = []
    result = None
    for e in events(text):
        t = e.get("type")
        if t == "system" and e.get("subtype") == "init":
            init = e
        if t == "result":
            result = e
        if e.get("parent_tool_use_id"):
            continue
        msg = e.get("message") or {}
        content = msg.get("content")
        if t == "user" and isinstance(content, str):
            expanded.append(content)
        if not isinstance(content, list):
            continue
        for c in content:
            if not isinstance(c, dict):
                continue
            if t == "assistant" and c.get("type") == "tool_use":
                pending[c["id"]] = (c.get("name"), json.dumps(c.get("input"), sort_keys=True))
                order.append(c["id"])
            elif t == "user" and c.get("type") == "tool_result":
                body = c.get("content")
                body = body if isinstance(body, str) else json.dumps(body)
                name, inp = pending.get(c.get("tool_use_id"), ("?", ""))
                out.append((name, inp, body, bool(c.get("is_error"))))
            elif t == "user" and c.get("type") == "text":
                expanded.append(c.get("text", ""))
    return out, init, result, expanded


def calls_codex(text):
    out, usage, err = [], None, None
    for e in events(text):
        if e.get("type") == "turn.completed":
            usage = e.get("usage")
        if e.get("type") in ("turn.failed", "error"):
            err = e
        item = e.get("item") if e.get("type") == "item.completed" else None
        if isinstance(item, dict) and item.get("type") == "command_execution":
            out.append(("shell", item.get("command") or "", item.get("aggregated_output") or "",
                        item.get("exit_code") not in (0, None)))
    return out, usage, err


def analyze(run_dir):
    run_dir = Path(run_dir)
    meta = json.loads((run_dir / "meta.json").read_text())
    host, name = meta["host"], meta["name"]
    cond = name.split("-", 1)[1].rsplit("-", 1)[0]
    mk = marker(cond)
    text = (run_dir / "stdout.jsonl").read_text()
    row = {"trial": name, "host": host, "condition": cond, "rc": meta["rc"]}
    if host == "claude":
        calls, init, result, expanded = calls_claude(text)
        plugins = [p.get("name") for p in (init or {}).get("plugins", [])] if init else []
        row["plugin_loaded"] = "w4fix" in plugins
        row["cost_usd"] = (result or {}).get("total_cost_usd")
        row["usage"] = (result or {}).get("usage")
        row["result_subtype"] = (result or {}).get("subtype")
        joined = "\n".join(expanded)
        bd = re.search(r"Base directory for this skill: (\S+)", joined)
        row["base_dir_given"] = bd.group(1) if bd else None
        row["skill_text_seen"] = "Before writing the release note" in joined
        row["marker_in_injected_text"] = mk in joined
        row["status"] = "captured" if init and row["plugin_loaded"] and result else "setup-blocked"
    else:
        calls, usage, err = calls_codex(text)
        row["cost_usd"] = None
        row["usage"] = usage
        row["error"] = err
        row["status"] = "captured" if usage else "setup-blocked"
    row["tool_calls"] = len(calls)
    first, returned_at, searches, paths = None, None, 0, []
    for i, (tool, inp, outp, iserr) in enumerate(calls):
        if returned_at is None and (tool in ("Glob", "Grep") or (tool in ("Bash", "shell") and SEARCH.search(inp))):
            if mk not in outp:
                searches += 1
        if "release-format" in inp:
            paths.append(inp[:300])
            if first is None:
                first = (i, inp[:300], mk in outp, iserr)
        if returned_at is None and mk in outp:
            returned_at = i
    row["returned"] = returned_at is not None
    row["first_path_call"] = first[1] if first else None
    row["first_path_returned"] = first[2] if first else False
    row["first_path_error"] = first[3] if first else None
    row["searches_before"] = searches
    row["calls_naming_reference"] = paths
    row["class"] = ("resolved" if first and first[2] else "recovered" if returned_at is not None else "not read")
    rel = meta.get("release_md") or ""
    row["applied"] = rel.splitlines()[:1] == [f"Format-ID: {mk}"] or rel.splitlines()[:1] == [f"`Format-ID: {mk}`"]
    row["release_first_line"] = rel.splitlines()[0] if rel else None
    return row


def main():
    cmd = sys.argv[1]
    if cmd == "fixtures":
        make_fixtures()
    elif cmd == "probe":
        host = sys.argv[2]
        prompt = ("Do not use any tools. List the file path of every instruction file (for example CLAUDE.md, "
                  "AGENTS.md, or similar project or user instructions) whose contents appear in your context, and "
                  "quote the first heading line of each verbatim. If there are none, reply NONE.\n")
        print(launch(host, f"probe-{host}-{sys.argv[3]}", prompt))
    elif cmd == "trial":
        host, cond, n = sys.argv[2], sys.argv[3], sys.argv[4]
        plugin = FIX / cond
        if host == "claude":
            prompt = f"/w4fix:release-note {TASK}\n"
        else:
            prompt = f"Use the release-note skill at {plugin}/skills/release-note/SKILL.md.\n\n{TASK}\n"
        out = launch(host, f"{host}-{cond}-{n}", prompt, plugin)
        print(json.dumps(analyze(out), indent=1))
    elif cmd == "analyze":
        rows = [analyze(d) for d in sorted(RUNS.iterdir()) if not d.name.startswith("probe")]
        print(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
