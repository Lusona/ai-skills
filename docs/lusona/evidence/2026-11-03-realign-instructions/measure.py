#!/usr/bin/env python3
"""Count words an agent loads for a representative implement with one worker.

Words are whitespace-separated tokens (same unit as `wc -w`). Core sections are
split on level-2 headings. Run from the repository root:

    python3 docs/lusona/evidence/2026-11-03-realign-instructions/measure.py [label]

Prints a Markdown table and the sha256 of every counted file.
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

PLUGIN = Path('plugins/lusona')
CORE = PLUGIN / 'README.md'

# Files each role reads for: spec-linked implement, one delegated worker, no failures,
# no spec creation. Lists are the measured scenario, not a loading rule.
COORDINATOR = [
    (CORE, None),
    (PLUGIN / 'skills/implement/SKILL.md', None),
    (PLUGIN / 'references/tdd.md', None),
    (PLUGIN / 'references/retention.md', None),
    (PLUGIN / 'references/queue.md', None),
    (PLUGIN / 'references/delegation.md', None),
    (PLUGIN / 'references/model-routing.md', None),
    (PLUGIN / 'references/worker-lifecycle.md', None),
    (PLUGIN / 'references/commits.md', None),
]
WORKER_CORE_SECTIONS = ['Loading rules', 'Work loop', 'Contract', 'TDD',
                        'Review and communication', 'Assigned leaves', 'Context budget']
WORKER = [
    (CORE, WORKER_CORE_SECTIONS),
    (PLUGIN / 'skills/implement/SKILL.md', None),
    (PLUGIN / 'references/tdd.md', None),
    (PLUGIN / 'references/retention.md', None),
    (PLUGIN / 'references/delegation.md', ['Assigned leaves', 'Assignment results']),
]
# File added by the change; the coordinator reads it before a handoff (spec decision
# 2026-11-03). Counted when present, so the baseline run before it existed is unaffected.
OPTIONAL = [
    (PLUGIN / 'references/handoff.md', None),
]
COORDINATOR += OPTIONAL


def sections(text):
    parts = re.split(r'(?m)^## (.+)$', text)
    out = {'': parts[0]}
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1]
    return out


def words(path, names):
    text = path.read_text(encoding='utf-8')
    if names is None:
        return len(text.split())
    secs = sections(text)
    missing = [n for n in names if n not in secs]
    if missing:
        raise SystemExit(f'{path}: missing sections {missing}')
    return sum(len(secs[n].split()) for n in names)


def report(label, manifest):
    rows, total = [], 0
    for path, names in manifest:
        if not path.exists():
            continue
        n = words(path, names)
        total += n
        rows.append((str(path) + ('' if names is None else ' §' + ', '.join(names)), n))
    print(f'\n### {label}\n')
    print('| File (sections) | Words |\n| --- | --- |')
    for name, n in rows:
        print(f'| `{name}` | {n:,} |')
    print(f'| **Total** | **{total:,}** |')
    return total


def main():
    label = sys.argv[1] if len(sys.argv) > 1 else 'measurement'
    head = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True,
                          text=True).stdout.strip()
    dirty = subprocess.run(['git', 'status', '--porcelain', '--', 'plugins/lusona'],
                           capture_output=True, text=True).stdout.strip()
    print(f'## {label}: HEAD {head}, plugin tree {"dirty" if dirty else "clean"}')
    report('Coordinator', COORDINATOR)
    report('Worker', WORKER)
    report('Core sections', [(CORE, [n]) for n in sections(CORE.read_text())
                             if n])
    all_md = sorted(PLUGIN.rglob('*.md'))
    print(f'\nAll plugin Markdown files: {sum(len(p.read_text().split()) for p in all_md):,} '
          f'words in {len(all_md)} files')
    print('\n### File hashes\n')
    seen = set()
    for path, _ in COORDINATOR + WORKER + OPTIONAL:
        if path in seen or not path.exists():
            continue
        seen.add(path)
        print(f'- `{path}` {hashlib.sha256(path.read_bytes()).hexdigest()[:16]}')


if __name__ == '__main__':
    main()
