#!/usr/bin/env python3
"""Check a rule inventory note (W15, spec 20261111) against the sources at its baseline commit.

Usage: python3 scripts/check_rule_inventory.py [NOTE] [COMMIT]   (run from the repository root)
Defaults: docs/lusona/notes/rule-inventory-34186da.md, 34186da.

Checks, per source file (README, every references/*.md and every skills/*/references/*.md at
COMMIT, read with git show; a per-skill reference's stem is its file name, for example
`execution` for skills/batch/references/execution.md):
1. Coverage: every non-blank line that is not a heading or a table separator row
   (code-fence lines included) is inside at least one row's Lines range.
2. Verbatim: each row's Rule text (with \\| unescaped) occurs in the whitespace-joined source
   lines of its range, after removing list markers and blockquote markers from each line.
3. IDs: unique, `<stem>-NNN`, consecutive from 001 per file; every source file has a table.
Exit 0 when all checks pass, 1 otherwise.
"""
import re
import subprocess
import sys
from collections import defaultdict

note = sys.argv[1] if len(sys.argv) > 1 else "docs/lusona/notes/rule-inventory-34186da.md"
commit = sys.argv[2] if len(sys.argv) > 2 else "34186da"


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


paths = ["plugins/lusona/README.md"] + [
    p for p in git("ls-tree", "--name-only", commit, "plugins/lusona/references/").split()
    if p.endswith(".md")
] + [
    p for p in git("ls-tree", "-r", "--name-only", commit, "plugins/lusona/skills/").split()
    if re.fullmatch(r"plugins/lusona/skills/[^/]+/references/[^/]+\.md", p)
]
stem_of = {p: ("readme" if p.endswith("README.md") else p.rsplit("/", 1)[1][:-3]) for p in paths}
clash = sorted({s for s in stem_of.values() if list(stem_of.values()).count(s) > 1})
if clash:
    print("duplicate source stems:", clash)
    sys.exit(1)

CELL = re.compile(r"(?<!\\)\|")
rows = defaultdict(list)
ids = []
for line in open(note, encoding="utf-8"):
    m = re.match(r"^\| ([a-z-]+)-(\d{3}) \|", line)
    if not m:
        continue
    cells = [c.strip() for c in CELL.split(line.rstrip("\n"))[1:-1]]
    rid, lines_cell, rule = cells[0], cells[1], cells[2].replace("\\|", "|")
    lm = re.fullmatch(r"L(\d+)(?:-L(\d+))?", lines_cell)
    if not lm:
        print(f"{rid}: bad Lines cell {lines_cell!r}")
        continue
    a = int(lm.group(1))
    b = int(lm.group(2) or a)
    rows[m.group(1)].append((int(m.group(2)), a, b, rule, rid))
    ids.append(rid)

fail = 0
dupe = {i for i in ids if ids.count(i) > 1}
if dupe:
    fail += 1
    print("duplicate IDs:", sorted(dupe))

total_lines = total_rows = 0
for path in paths:
    stem = stem_of[path]
    src = git("show", f"{commit}:{path}").split("\n")
    if src and src[-1] == "":
        src = src[:-1]
    rs = rows.get(stem, [])
    if not rs:
        fail += 1
        print(f"{stem}: no rows")
        continue
    seqs = [r[0] for r in rs]
    if seqs != list(range(1, len(rs) + 1)):
        fail += 1
        print(f"{stem}: IDs not consecutive from 001")
    covered = set()
    for _, a, b, _, _ in rs:
        covered.update(range(a, b + 1))
    in_code = False
    need = []
    for n, l in enumerate(src, 1):
        s = l.strip()
        if s.startswith("```"):
            in_code = not in_code
            need.append(n)
            continue
        if not s or (not in_code and (s.startswith("#") or re.match(r"^\|\s*-{3}", s))):
            continue
        need.append(n)
    unc = [n for n in need if n not in covered]
    if unc:
        fail += 1
        print(f"{stem}: uncovered lines {unc}")
    bad = []
    for _, a, b, rule, rid in rs:
        if a < 1 or b > len(src) or a > b:
            bad.append(rid)
            continue
        parts = []
        for l in src[a - 1:b]:
            s = l.strip()
            s = re.sub(r"^>\s?", "", s)
            s = re.sub(r"^(-|\d+\.)\s+", "", s)
            if s:
                parts.append(s)
        joined = " ".join(parts)
        if " ".join(rule.split()) not in " ".join(joined.split()):
            bad.append(rid)
    if bad:
        fail += 1
        print(f"{stem}: rule text not found verbatim in its line range: {bad}")
    total_lines += len(need)
    total_rows += len(rs)
    print(f"{stem}: {len(src)} lines, {len(need)} content lines, {len(unc)} uncovered, {len(rs)} rows, {len(bad)} verbatim failures")

print(f"TOTAL: {len(paths)} files, {total_lines} content lines, {total_rows} rows, {'FAIL' if fail else 'PASS'}")
sys.exit(1 if fail else 0)
