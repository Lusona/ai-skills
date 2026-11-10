#!/usr/bin/env python3
"""Summarize rows.json from audit_loading.py into loading rates.

Applicability rules are taken from the plugin 2.0.5 core and skill text:
- core README: every trial (every skill says "Apply the core").
- delegation.md and model-routing.md: before dispatching a worker ("Before dispatch read ...").
- tdd.md: implement/refactor scenarios ("Read tdd when selecting/applying policy").
- retention.md: trials that saved a docs/lusona record ("Save findings/evidence").
  Record rules count only trials where the operation occurred.
- queue.md: trials that added or changed a spec ("Creating, updating, or using a spec requires
  its queue tracking under queue").
- worker-lifecycle.md: trials that dispatched a worker (read after results).
"""
import collections
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path.cwd()  # run from the repository root: python3 <this file> rows.json
RUNS = ROOT / "docs/lusona/evidence/2026-11-09-loop-conformance-pilot/runs"
SKILL = {
    "explore-save": "explore", "explore-no-save": "explore", "review-readonly": "review",
    "greeting": "explore", "workflow-question": "status", "tdd-unset": "implement",
    "refactor-unset": "refactor", "tdd-stated": "implement", "specify-change": "specify",
    "status-check": "status", "investigate-bug": "investigate", "authz-change": "implement",
}
ALL_SECTIONS = 10

rows = json.load(open(sys.argv[1]))

# Changed files for the record-based rules, from each trial's trial.json.
ARCHIVES = {run: zipfile.ZipFile(RUNS / f"{run}/raw.zip") for run in ("003", "006", "007")}


def trial_prefix(r):
    if r["run"] == "003":
        return f"runs/reference-2.0.5/{r['host']}/{r['scenario']}/{r['trial']}/"
    if r["run"] == "006":
        return f"tmp/completion-actor-evaluation/runs/{r['condition']}/{r['host']}/{r['scenario']}/{r['trial']}/"
    return f"tmp/direct-instruction-checkpoints/behavior/runs/{r['condition']}/{r['scenario']}/{r['trial']}/"


changed = {}
for r in rows:
    t = json.loads(ARCHIVES[r["run"]].read(trial_prefix(r) + "trial.json"))
    c = t.get("changed") or {}
    changed[id(r)] = c.get("added", []) + c.get("modified", [])


def pct(a, b):
    return f"{a}/{b}" if b else "-"


print("## Core README returned to root agent, run 003, by scenario (5 trials per cell)")
print("| Scenario | Skill | Claude core | Claude all 10 sections | Codex core | Codex all 10 sections |")
print("| --- | --- | --- | --- | --- | --- |")
tot = collections.Counter()
for sc in SKILL:
    cells = []
    for host in ("claude", "codex"):
        rs = [r for r in rows if r["run"] == "003" and r["host"] == host and r["scenario"] == sc]
        core = sum(r["core"] for r in rs)
        full = sum(len(r["core_sections"]) == ALL_SECTIONS for r in rs)
        tot[(host, "core")] += core
        tot[(host, "full")] += full
        tot[(host, "n")] += len(rs)
        cells += [pct(core, len(rs)), pct(full, len(rs))]
    print(f"| {sc} | {SKILL[sc]} | " + " | ".join(cells) + " |")
print(f"| **Total** | | {pct(tot['claude','core'], tot['claude','n'])} | {pct(tot['claude','full'], tot['claude','n'])} "
      f"| {pct(tot['codex','core'], tot['codex','n'])} | {pct(tot['codex','full'], tot['codex','n'])} |")

print("\n## Core README, runs 006 and 007")
for run in ("006", "007"):
    for key in sorted({(r["condition"], r["host"], r["scenario"]) for r in rows if r["run"] == run}):
        rs = [r for r in rows if r["run"] == run and (r["condition"], r["host"], r["scenario"]) == key]
        print(f"- run {run} {key}: core {pct(sum(r['core'] for r in rs), len(rs))}")

print("\n## Codex skill file returned (Codex reads SKILL.md itself)")
rs = [r for r in rows if r["host"] == "codex"]
print(pct(sum(f"skills/{SKILL[r['scenario']]}/SKILL.md" in r["returned"] for r in rs), len(rs)))

print("\n## Rule-triggered references, all runs, root agent")
print("| Rule | Claude | Codex |")
print("| --- | --- | --- |")


def rule(name, applies, satisfied):
    cells = []
    for host in ("claude", "codex"):
        rs = [r for r in rows if r["host"] == host and applies(r)]
        cells.append(pct(sum(satisfied(r) for r in rs), len(rs)))
    print(f"| {name} | " + " | ".join(cells) + " |")


def before_dispatch(rel):
    return lambda r: rel in r["first_seen"] and r["first_seen"][rel] < r["first_dispatch"]


dispatched = lambda r: r["first_dispatch"] is not None
rule("delegation.md before first dispatch", dispatched, before_dispatch("references/delegation.md"))
rule("model-routing.md before first dispatch", dispatched, before_dispatch("references/model-routing.md"))
rule("worker-lifecycle.md when workers dispatched", dispatched,
     lambda r: "references/worker-lifecycle.md" in r["returned"])
rule("tdd.md in implement/refactor trials",
     lambda r: SKILL[r["scenario"]] in ("implement", "refactor"),
     lambda r: "references/tdd.md" in r["returned"])
saved = lambda r: any(p.startswith("docs/lusona/") for p in changed[id(r)])
rule("retention.md when a docs/lusona record was saved", saved,
     lambda r: "references/retention.md" in r["returned"])
spec = lambda r: any(p.startswith("docs/lusona/specs/") for p in changed[id(r)])
rule("queue.md when a spec was added or changed", spec,
     lambda r: "references/queue.md" in r["returned"])

print("\n## Dispatch and saving, by whether the core was returned (all runs)")
for host in ("claude", "codex"):
    for core in (True, False):
        rs = [r for r in rows if r["host"] == host and r["core"] == core]
        print(f"- {host} core={core}: {len(rs)} trials, dispatched {sum(dispatched(r) for r in rs)}, "
              f"saved a docs/lusona record {sum(saved(r) for r in rs)}")
rs = [r for r in rows if r["host"] == "claude" and r["scenario"] == "tdd-stated"]
for run in ("003", "006", "007"):
    sub = [r for r in rs if r["run"] == run]
    print(f"- claude tdd-stated run {run}: saved a record {sum(saved(r) for r in sub)}/{len(sub)}")

print("\n## Reference frequency, run 003 (trials returning each file / 60 per host)")
freq = {h: collections.Counter() for h in ("claude", "codex")}
for r in rows:
    if r["run"] == "003":
        for rel in r["returned"]:
            if rel.startswith("references/"):
                freq[r["host"]][rel] += 1
names = sorted(set(freq["claude"]) | set(freq["codex"]), key=lambda n: (-(freq["claude"][n] + freq["codex"][n]), n))
print("| Reference | Claude | Codex |")
print("| --- | --- | --- |")
for n in names:
    print(f"| {n.removeprefix('references/')} | {freq['claude'][n]} | {freq['codex'][n]} |")
