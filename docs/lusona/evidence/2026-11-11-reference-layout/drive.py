#!/usr/bin/env python3
"""Round-robin driver with budget guard and declared curtailment rule."""
import json, subprocess, sys
from pathlib import Path

W4 = Path(__file__).resolve().parent
sys.path.insert(0, str(W4))
import w4  # noqa: E402

N, BUDGET, CAP = 5, 20.0, 1.50


def fixed(r, k):
    m = N - k
    return r >= 4 or r + m <= 1 or (r >= 2 and r + m <= 3)


def spent():
    total = 0.0
    for d in w4.RUNS.iterdir():
        if d.name.startswith(("claude", "probe-claude")):
            for line in (d / "stdout.jsonl").read_text().splitlines():
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if e.get("type") == "result" and e.get("total_cost_usd"):
                    total += e["total_cost_usd"]
    return total


def series(host, cond):
    rows = [w4.analyze(d) for d in sorted(w4.RUNS.glob(f"{host}-{cond}-*"))]
    return len(rows), sum(r["class"] == "resolved" for r in rows)


log = open(W4 / "drive.log", "a")
for n in range(1, N + 1):
    for host in ("claude", "codex") if n % 2 else ("codex", "claude"):
        for cond in w4.CONDS:
            if (w4.RUNS / f"{host}-{cond}-{n}").exists():
                continue
            k, r = series(host, cond)
            if fixed(r, k):
                print(f"curtailed {host} {cond} at {k} trials ({r} resolved)", file=log, flush=True)
                continue
            if host == "codex":
                ck, _ = series("claude", cond)
                if k >= max(ck, n):
                    pass
            if host == "claude" and spent() + CAP > BUDGET:
                print(f"budget stop before {host} {cond} {n}: spent {spent():.3f}", file=log, flush=True)
                continue
            out = w4.launch(host, f"{host}-{cond}-{n}",
                            f"/w4fix:release-note {w4.TASK}\n" if host == "claude" else
                            f"Use the release-note skill at {w4.FIX / cond}/skills/release-note/SKILL.md.\n\n{w4.TASK}\n",
                            w4.FIX / cond)
            row = w4.analyze(out)
            print(json.dumps({k2: row.get(k2) for k2 in ("trial", "status", "class", "applied", "cost_usd",
                                                           "searches_before", "first_path_call")}), file=log, flush=True)
print(f"done; claude spent {spent():.3f}", file=log, flush=True)
