#!/usr/bin/env python3
"""Count which Lusona plugin files reached the root actor in loop-conformance runs.

A file counts as returned when tool output shown to the root agent contains at least
MIN_LINES of that file's unique lines (stripped lines of 40+ characters that occur in
no other plugin file). Injected context (Claude slash-command skill bodies, system
prompts) is not in the transcripts and is not counted. Worker transcripts are excluded.

Run from the repository root after extracting the run 003 plugin snapshot:
  mkdir -p tmp/loading-audit/plugin-42b8145
  git archive 42b8145 plugins/lusona | tar -x -C tmp/loading-audit/plugin-42b8145
  python3 <this file> > rows.json
"""
import collections
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path.cwd()  # run from the repository root
RUNS = ROOT / "docs/lusona/evidence/2026-11-09-loop-conformance-pilot/runs"
SNAP_003 = ROOT / "tmp/loading-audit/plugin-42b8145/plugins/lusona"
MIN_LINES = 3
SECTION_MIN = 2
TEXT_SUFFIXES = (".md",)


def load_dir(base: Path) -> dict:
    return {
        str(p.relative_to(base)): p.read_text(encoding="utf-8")
        for p in base.rglob("*")
        if p.is_file() and p.suffix in TEXT_SUFFIXES
    }


def load_zip_dir(z: zipfile.ZipFile, prefix: str) -> dict:
    out = {}
    for name in z.namelist():
        if name.startswith(prefix) and name.endswith(TEXT_SUFFIXES):
            out[name[len(prefix):]] = z.read(name).decode("utf-8")
    return out


class Index:
    def __init__(self, files: dict):
        counts = collections.Counter()
        owner = {}
        for rel, text in files.items():
            for line in {l.strip() for l in text.splitlines()}:
                if len(line) >= 40:
                    counts[line] += 1
                    owner[line] = rel
        self.unique = collections.defaultdict(list)
        for line, n in counts.items():
            if n == 1:
                self.unique[owner[line]].append(line)
        self.section_of = {}
        section = "(preamble)"
        for raw in files["README.md"].splitlines():
            if raw.startswith("## "):
                section = raw[3:].strip()
            line = raw.strip()
            if counts.get(line) == 1:
                self.section_of[line] = section

    def match(self, text: str):
        files = {}
        for rel, lines in self.unique.items():
            hits = [l for l in lines if l in text]
            if hits:
                files[rel] = hits
        return files


def claude_events(lines):
    """Yield (kind, payload) for root-level events in order."""
    for raw in lines:
        e = json.loads(raw)
        if e.get("parent_tool_use_id"):
            continue
        msg = e.get("message")
        content = msg.get("content") if isinstance(msg, dict) else None
        if e.get("type") == "assistant" and isinstance(content, list):
            for c in content:
                if c.get("type") == "tool_use" and c.get("name") in ("Task", "Agent"):
                    yield "dispatch", c.get("input")
        if e.get("type") == "user" and isinstance(content, list):
            for c in content:
                if c.get("type") == "tool_result":
                    body = c.get("content")
                    if isinstance(body, list):
                        body = "\n".join(x.get("text", "") for x in body if isinstance(x, dict))
                    yield "output", body or ""


def codex_events(lines):
    for raw in lines:
        e = json.loads(raw)
        item = e.get("item") or {}
        kind = item.get("type")
        if e.get("type") == "item.started" and kind == "collab_tool_call":
            yield "dispatch", item
        if e.get("type") == "item.completed" and kind == "command_execution":
            yield "output", item.get("aggregated_output") or ""


def trial_sources():
    """Yield (run, condition, host, scenario, trial, zip, member prefix, index key)."""
    z3 = zipfile.ZipFile(RUNS / "003/raw.zip")
    for name in z3.namelist():
        m = re.match(r"(runs/reference-2\.0\.5/(claude|codex)/([^/]+)/(\d+)/)turn-1\.stdout\.jsonl$", name)
        if m:
            yield ("003", "2.0.5", m[2], m[3], int(m[4]), z3, m[1], ("003", None))
    z6 = zipfile.ZipFile(RUNS / "006/raw.zip")
    for name in z6.namelist():
        m = re.match(r"(tmp/completion-actor-evaluation/runs/(A|B)/(claude|codex)/([^/]+)/(\d+)/)turn-1\.stdout\.jsonl$", name)
        if m:
            yield ("006", m[2], m[3], m[4], int(m[5]), z6, m[1], ("006", f"{m[3]}-{m[2]}"))
    z7 = zipfile.ZipFile(RUNS / "007/raw.zip")
    for name in z7.namelist():
        m = re.match(r"(tmp/direct-instruction-checkpoints/behavior/runs/(BASELINE|CANDIDATE)/([^/]+)/(\d+)/)turn-1\.stdout\.jsonl$", name)
        if m:
            yield ("007", m[2], "claude", m[3], int(m[4]), z7, m[1], ("007", m[2]))


def get_index(cache, key, z):
    if key in cache:
        return cache[key]
    run, cond = key
    if run == "003":
        files = load_dir(SNAP_003)
    elif run == "006":
        files = load_zip_dir(z, f"tmp/completion-actor-evaluation/conditions/{cond}/plugin/")
    else:
        files = load_zip_dir(z, f"tmp/direct-instruction-checkpoints/behavior/conditions/{cond}/plugin/")
    cache[key] = Index(files)
    return cache[key]


def main():
    cache = {}
    rows = []
    seen = set()
    for run, cond, host, scenario, trial, z, prefix, key in trial_sources():
        if (run, cond, host, scenario, trial) in seen:
            continue
        seen.add((run, cond, host, scenario, trial))
        idx = get_index(cache, key, z)
        turns = sorted(n for n in z.namelist()
                       if n.startswith(prefix) and re.search(r"turn-\d+\.stdout\.jsonl$", n))
        hits = collections.defaultdict(set)
        first_seen = {}
        first_dispatch = None
        per_turn_core = []
        step = 0
        for turn_name in turns:
            lines = [l for l in z.read(turn_name).decode("utf-8").splitlines() if l.strip()]
            events = claude_events(lines) if host == "claude" else codex_events(lines)
            core_this_turn = set()
            for kind, payload in events:
                step += 1
                if kind == "dispatch":
                    if first_dispatch is None:
                        first_dispatch = step
                    continue
                for rel, found in idx.match(payload).items():
                    hits[rel].update(found)
                    if rel == "README.md":
                        core_this_turn.update(found)
                    if len(hits[rel]) >= min(MIN_LINES, len(idx.unique[rel])) and rel not in first_seen:
                        first_seen[rel] = step
            per_turn_core.append(len(core_this_turn) >= MIN_LINES)
        returned = sorted(first_seen)
        sections = collections.Counter(idx.section_of[l] for l in hits.get("README.md", ()))
        rows.append({
            "run": run, "condition": cond, "host": host, "scenario": scenario, "trial": trial,
            "turns": len(turns),
            "returned": returned,
            "core": "README.md" in first_seen,
            "core_turns": per_turn_core,
            "core_sections": sorted(s for s, n in sections.items() if n >= SECTION_MIN),
            "first_seen": first_seen,
            "first_dispatch": first_dispatch,
        })
    json.dump(rows, sys.stdout, indent=1)


if __name__ == "__main__":
    main()
