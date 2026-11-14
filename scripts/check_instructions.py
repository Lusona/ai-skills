#!/usr/bin/env python3
"""Check that canonical instructions state each rule once.

Two checks over ``plugins/lusona``:

1. Skills do not restate core contract clauses. Phrases that the core already owns
   must not appear in any ``skills/*/SKILL.md`` outside Markdown link text and outside
   generated ``<!-- lusona:begin NAME -->`` ... ``<!-- lusona:end NAME -->`` regions
   (shared text written by ``scripts/sync_shared.py``), including when Markdown wrapping
   splits a phrase across lines. A begin marker without its matching end marker is not
   a region.
2. The skill catalog table and the skill routing table exist once, in
   ``references/workflow-guide.md``. Batch-specific dispatch-condition tables are
   not routing tables and are allowed. A catalog is found by its rows, whatever its
   header: a table whose first cells link to the SKILL.md of at least half of the
   plugin's skills (and at least 3), or a table with header ``Skill`` and 3 such rows.
   Limit: a partial copy linking fewer than half of the skills under another header is
   not detected; the batch dispatch table links 5 of 15 skills.

Exit status 0 when both hold; 1 with findings otherwise. Run from the repository root
or pass the plugin directory as the first argument.
"""
import re
import sys
from pathlib import Path

PHRASES = [
    'without a separate save request',
    'does not authorize', 'do not authorize',
    'permitted native question tool', 'permitted question tool', 'native question tool',
]
# Words may be separated by any whitespace, including a line wrap.
RESTATED = re.compile('|'.join(r'\s+'.join(map(re.escape, p.split())) for p in PHRASES),
                      re.IGNORECASE)
LINK = re.compile(r'\[[^\]]*\]\([^)]*\)')
SKILL_LINK = re.compile(r'\]\([^)]*\bSKILL\.md[^)]*\)')
LINKED_SKILL = re.compile(r'\]\((?:[^)]*/)?([\w-]+)/SKILL\.md[^)]*\)')
# Generated region; the end marker must name the same region.
REGION = re.compile(r'^<!-- lusona:begin ([a-z0-9-]+) -->$'
                    r'(?:(?!^<!-- lusona:begin \1 -->$).)*?^<!-- lusona:end \1 -->$',
                    re.MULTILINE | re.DOTALL)
ROUTING_HEADER = re.compile(r'evidence|gap|need|situation', re.IGNORECASE)
GUIDE = Path('references/workflow-guide.md')


def body(text):
    """Return (first_line_number, body_text) excluding the YAML frontmatter.

    Frontmatter holds the host-facing name and description used for skill selection;
    it is not loaded as an instruction body, so restatement rules do not apply there.
    """
    lines = text.splitlines(keepends=True)
    start = 0
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                start = i + 1
                break
    return start + 1, ''.join(lines[start:])


def restated_clauses(plugin):
    """Find restated phrases in skill bodies, matching across wrapped lines.

    Generated regions and link text are blanked rather than removed so line numbers
    stay exact.
    """
    findings = []
    for skill in sorted(plugin.glob('skills/*/SKILL.md')):
        first, text = body(skill.read_text(encoding='utf-8'))
        blank = lambda m: re.sub(r'\S', ' ', m.group(0))
        unlinked = LINK.sub(blank, REGION.sub(blank, text))
        for match in RESTATED.finditer(unlinked):
            number = first + unlinked.count('\n', 0, match.start())
            findings.append((skill.relative_to(plugin), number, ' '.join(match.group(0).split())))
    return findings


def tables(text):
    """Yield (header_cells, rows) for each Markdown table."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i + 1]):
            header = [c.strip() for c in lines[i].strip('|').split('|')]
            rows = []
            i += 2
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip('|').split('|')])
                i += 1
            yield header, rows
        else:
            i += 1


def classify(header, rows, skill_count=0):
    if len(rows) < 3:
        return None
    if header and header[0].lower() == 'skill' and any(SKILL_LINK.search(r[0]) for r in rows):
        return 'catalog'
    linked = {m.group(1) for r in rows if r for m in LINKED_SKILL.finditer(r[0])}
    if skill_count and len(linked) >= max(3, (skill_count + 1) // 2):
        return 'catalog'
    second_links = sum(1 for r in rows if len(r) > 1 and SKILL_LINK.search(r[1]))
    if header and ROUTING_HEADER.search(header[0]) and second_links >= 3:
        return 'routing'
    return None


def table_owners(plugin):
    owners = {'catalog': [], 'routing': []}
    skill_count = len(list(plugin.glob('skills/*/SKILL.md')))
    for path in sorted(plugin.rglob('*.md')):
        for header, rows in tables(path.read_text(encoding='utf-8')):
            kind = classify(header, rows, skill_count)
            if kind:
                owners[kind].append(path.relative_to(plugin))
    return owners


def table_findings(plugin):
    findings = []
    for kind, paths in table_owners(plugin).items():
        if GUIDE not in paths:
            findings.append(f'{kind} table missing from {GUIDE}')
        for path in paths:
            if path != GUIDE:
                findings.append(f'{kind} table duplicated in {path}')
        if paths.count(GUIDE) > 1:
            findings.append(f'{kind} table appears {paths.count(GUIDE)} times in {GUIDE}')
    return findings


def main(argv):
    plugin = Path(argv[1]) if len(argv) > 1 else Path('plugins/lusona')
    failures = 0
    for path, number, phrase in restated_clauses(plugin):
        print(f'restated: {path}:{number}: "{phrase}"')
        failures += 1
    for finding in table_findings(plugin):
        print(f'tables: {finding}')
        failures += 1
    print('Instruction checks passed.' if not failures else f'{failures} finding(s).')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
