#!/usr/bin/env python3
"""Summaries for the W14 suite run: pass marks, draft vs reference, spend and time.

usage: analyze.py DRAFT_REPORT_TRIALS BASE_REPORT_TRIALS PASS_MARKS RUNS_DIR
Prints Markdown tables to stdout.
"""
import collections
import json
import pathlib
import sys

C9_SCENARIOS = ["tdd-stated", "authz-change", "status-check", "investigate-bug"]


def load(path):
    p = pathlib.Path(path)
    return json.loads(p.read_text()) if p.exists() else []


def counts(trials):
    """(host, scenario, check) -> Counter of results."""
    out = collections.defaultdict(collections.Counter)
    for t in trials:
        for check, res in t["results"].items():
            if res["result"] != "not-applicable":
                out[(t["host"], t["scenario"], check)][res["result"]] += 1
    return out


def fmt(c):
    if not c:
        return "-"
    graded = c["pass"] + c["fail"]
    extra = sum(v for k, v in c.items() if k not in ("pass", "fail"))
    return f"{c['pass']} / {graded}" + (f" (+{extra} other)" if extra else "")


def main(argv):
    draft, base = load(argv[1]), load(argv[2])
    marks = json.loads(pathlib.Path(argv[3]).read_text())["marks"]
    runs = pathlib.Path(argv[4])
    dc, bc = counts(draft), counts(base)

    print("## Pass marks (draft)\n")
    print("| Scenario | Check | Claude Code | Mark | Met | Codex | Mark | Met |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for m in marks:
        row = [f"`{m['scenario']}`", m["check"]]
        for host in ("claude", "codex"):
            c = dc.get((host, m["scenario"], m["check"]), collections.Counter())
            need = m["min_pass"][host]
            n = sum(c.values())
            met = "met" if c["pass"] >= need else ("not met" if n >= m["trials"] else f"not met ({n} of {m['trials']} trials run)")
            row += [f"{c['pass']} / {n}", f"{need} / {m['trials']}", met]
        print("| " + " | ".join(row) + " |")

    print("\n## All checks, per host and scenario (draft)\n")
    print("| Host | Scenario | Check | Pass / graded |")
    print("| --- | --- | --- | --- |")
    for key in sorted(dc):
        print(f"| {key[0]} | `{key[1]}` | {key[2]} | {fmt(dc[key])} |")

    print("\n## Draft vs fresh reference (34186da), C9 scenarios\n")
    print("| Host | Scenario | Check | Draft | Reference |")
    print("| --- | --- | --- | --- | --- |")
    keys = sorted({k for k in list(dc) + list(bc) if k[1] in C9_SCENARIOS})
    for key in keys:
        print(f"| {key[0]} | `{key[1]}` | {key[2]} | {fmt(dc.get(key))} | {fmt(bc.get(key))} |")

    print("\n## Spend and actor time\n")
    print("| Run | Host | Trials | Actor time (s) | Actor $ | Judge $ | Judge calls |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    total = 0.0
    for run in sorted(p for p in runs.iterdir() if p.is_dir()):
        for host in ("claude", "codex"):
            dirs = [d for d in (run / host).glob("*/*") if (d / "run.json").exists()]
            if not dirs:
                continue
            secs = actor = judge = 0.0
            calls = 0
            for d in dirs:
                tr = d / "trial.json"
                if tr.exists():
                    r = json.loads(tr.read_text())
                    actor += r.get("cost_usd") or 0.0
                    secs += (r.get("capture") or {}).get("elapsed_seconds") or 0.0
                js = d / "judge.stdout.json"
                if js.exists():
                    try:
                        judge += json.loads(js.read_text()).get("total_cost_usd") or 0.0
                        calls += 1
                    except ValueError:
                        pass
            total += actor + judge
            print(f"| {run.name} | {host} | {len(dirs)} | {secs:,.0f} | {actor:.2f} | {judge:.2f} | {calls} |")
    print(f"\nTotal Claude-reported spend: ${total:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
