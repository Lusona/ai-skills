#!/usr/bin/env python3
"""Check Lusona skill files against the skill template and the reference layout.

Spec 20261111-loop-principles-and-skill-rewrite (AC10, AC11, AC14, S4) and ADR
20261111-skill-file-layout-and-shared-sources (layout, P-a, P-b). Five checks over a
plugin directory; each finding line starts with the check name:

1. ``template``: each ``skills/*/SKILL.md`` has frontmatter ``name`` and ``description``;
   the description has action text, then "Use when", then "Not for ... use <skill>" naming
   other existing skill directories; the body starts with an H1 followed by the
   ``every-task`` region; the H2 sections follow ``SECTIONS`` (skills in
   ``EXTRA_SECTIONS_ALLOWED_FOR`` may add sections); ``## Persona and judgment``
   has every field in ``PERSONA_FIELDS``; ``## Final reply`` is last, holds the
   ``final-reply`` region and text outside it (the skill's valid next actions).
2. ``readme``: no SKILL.md or reference links to the plugin README or names it by one of
   the paths in ``README_PATH``. Links to a project ``docs/lusona/README.md`` are allowed.
3. ``reference``: every reference is linked directly from a SKILL.md; a plugin-level
   reference from at least ``MIN_PLUGIN_REFERENCE_USERS`` SKILL.md files; a per-skill
   reference only from its own skill's SKILL.md; no reference links another reference.
   Links inside generated regions count as SKILL.md links.
   Trigger (AC14): each SKILL.md that links a reference holds at least one link to it in a
   trigger sentence; other links to it in that SKILL.md may stand in any sentence.
   Sentences are split at ".", "!" or "?" followed by whitespace, at table cell separators,
   and at paragraph, list item, heading and table row boundaries; a leading bold label
   ("**Saving.**") is ignored. A sentence is a trigger sentence when, with link targets
   removed, it contains a word from ``TRIGGER_WORDS`` (for example "Before merging, read
   [x](...)" or "read [x](...) when a test fails"), or a clause starts with a word from
   ``TRIGGER_CLAUSE_WORDS`` ("If ...", "At 40% context use, ...", "As a leaf, ..."); a clause
   starts at the sentence start or after ",", ";", ":" or "(".
4. ``bare-path``: a path ending in ``references/<file>.md`` outside a Markdown link, unless it
   resolves to a file inside the naming file's own ``skills/<skill>/`` folder (ADR decision 3:
   plugin-level files are named only by Markdown links; bare per-skill paths are allowed).
   A path that does not resolve, or resolves to a plugin-level or other skill's file, is a
   finding. Whole links (text and target) are exempt, because the target is what a host
   resolves.
5. ``size``: line ceilings in ``SIZE_LIMITS``; scripts and ``.html`` templates are exempt.

Usage: check_skill_template.py [PLUGIN_DIR]   (default plugins/lusona)
Exit status 0 when clean; 1 with findings; 2 when PLUGIN_DIR has no skills/*/SKILL.md.
"""
import re
import sys
from pathlib import Path

# Template (20261110 "Skill template", decision 2). Each entry: (label, title pattern,
# required). H2 sections must appear in this order; a title matching none is a finding
# unless EXTRA_SECTIONS_ALLOWED.
SECTIONS = [
    ('## Persona and judgment', r'Persona and judgment', True),
    ('## Establish <input>', r'Establish\b.*', True),
    ('## <Domain> practices', r'.*\bpractices', False),
    ('## <Procedure> and record', r'.*\band record', True),
    ('## Final reply', r'Final reply', True),
]
EXTRA_SECTIONS_ALLOWED = False
# Skills that may add H2 sections beyond SECTIONS (A4, user decision 2026-11-11). Required
# sections, their order, and "## Final reply" as the last section still apply.
EXTRA_SECTIONS_ALLOWED_FOR = {'batch', 'status'}
PERSONA_SECTION = 'Persona and judgment'
FINAL_SECTION = 'Final reply'
PERSONA_FIELDS = ['Persona', 'Responsibility', 'Decision criteria', 'Evidence', 'Failure modes']
FRONTMATTER_FIELDS = ['name', 'description']
USE_WHEN = 'Use when'
NOT_FOR = 'Not for'
NOT_FOR_SKILL = re.compile(r'\buse\s+(?:the\s+)?`?([a-z][a-z0-9-]*)`?', re.IGNORECASE)
EVERY_TASK_REGION = 'every-task'
FINAL_REPLY_REGION = 'final-reply'

# README independence (AC10).
README_PATH = re.compile(r'(?<![\w./-])(?:plugins/lusona/|(?:\.\./)+)README\.md')

# Reference placement (ADR decision 1-2, P-a).
MIN_PLUGIN_REFERENCE_USERS = 2

# Trigger sentences (AC14); see check 3 in the module docstring.
TRIGGER_WORDS = re.compile(r'\b(?:before|after|when|whenever|while|until|once|during|unless)\b', re.I)
TRIGGER_CLAUSE_WORDS = re.compile(r'(?:^|[,;:(]\s*)(?:if|at|as|on)\b', re.I)
SENTENCE_BREAK = re.compile(r'(?<=[.!?])\s+|\s*(?<!\\)\|\s*')
BOLD_LABEL = re.compile(r'^\*\*[^*]+\*\*\s*')
LIST_ITEM = re.compile(r'^\s*(?:[-*+]|\d+[.)])\s+')

# Bare paths (ADR decision 3).
BARE_REFERENCE = re.compile(r'(?<![\w./-])((?:[\w.-]+/)*references/[\w.-]+\.md)')

# Size ceilings (S4): glob -> maximum lines.
SIZE_LIMITS = [
    ('skills/*/SKILL.md', 500),
    ('references/*.md', 200),
    ('skills/*/references/*.md', 200),
    ('templates/*.md', 100),
    ('templates/*.md.template', 100),
]

BEGIN = re.compile(r'^<!-- lusona:begin ([a-z0-9-]+) -->$')
END = '<!-- lusona:end {name} -->'
LINK = re.compile(r'\[([^\]]*)\]\(\s*([^)\s]*)(?:\s+"[^"]*")?\s*\)')
FENCE = re.compile(r'^\s*(```|~~~)')


def skills(plugin):
    return sorted(Path(plugin).glob('skills/*/SKILL.md'))


def references(plugin):
    plugin = Path(plugin)
    return sorted(plugin.glob('references/*.md')) + sorted(plugin.glob('skills/*/references/*.md'))


def rel(path, plugin):
    return Path(path).resolve().relative_to(Path(plugin).resolve()).as_posix()


def line_of(text, offset):
    return text.count('\n', 0, offset) + 1


def split_frontmatter(lines):
    """Return (fields, index of first body line). Supports folded continuation lines."""
    if not lines or lines[0].strip() != '---':
        return {}, 0
    fields, key = {}, None
    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == '---':
            return fields, i + 1
        match = re.match(r'^([A-Za-z_-]+):\s*(.*)$', line)
        if match:
            key, value = match.group(1), match.group(2).strip()
            fields[key] = '' if value in ('>', '|', '>-', '|-') else value.strip('"\'')
        elif key and line.startswith((' ', '\t')):
            fields[key] = (fields[key] + ' ' + line.strip()).strip()
    return {}, 0


def regions(lines, start=0):
    """Return {name: (begin_index, end_index)} for complete regions in lines[start:]."""
    found = {}
    for i in range(start, len(lines)):
        match = BEGIN.match(lines[i].strip())
        if match and match.group(1) not in found:
            end_marker = END.format(name=match.group(1))
            for j in range(i + 1, len(lines)):
                if lines[j].strip() == end_marker:
                    found[match.group(1)] = (i, j)
                    break
    return found


def masked(lines, start, spans):
    """Indices of lines that are inside a region (markers included) or a fenced block."""
    hidden = set()
    for begin, end in spans.values():
        hidden.update(range(begin, end + 1))
    fence = None
    for i in range(start, len(lines)):
        if i in hidden:
            continue
        match = FENCE.match(lines[i])
        if fence:
            hidden.add(i)
            if match and match.group(1) == fence:
                fence = None
        elif match:
            fence = match.group(1)
            hidden.add(i)
    return hidden


def description_findings(description, own, names):
    found = []
    use = description.find(USE_WHEN)
    not_for = description.find(NOT_FOR)
    if use == -1:
        found.append(f'description lacks "{USE_WHEN}"')
    elif not description[:use].strip():
        found.append(f'description lacks action text before "{USE_WHEN}"')
    if not_for == -1:
        found.append(f'description lacks "{NOT_FOR}"')
        return found
    if use != -1 and not_for < use:
        found.append(f'description: "{USE_WHEN}" must precede "{NOT_FOR}"')
    named = NOT_FOR_SKILL.findall(description[not_for:])
    if not named:
        found.append(f'description: "{NOT_FOR}" names no skill (expected "use <skill>")')
    for name in named:
        if name == own:
            found.append(f'description: "{NOT_FOR}" names itself ({name})')
        elif name not in names:
            found.append(f'description: "{NOT_FOR}" names missing skill {name}')
    return found


def skill_findings(path, names):
    own = path.parent.name
    lines = path.read_text(encoding='utf-8').splitlines()
    fields, body = split_frontmatter(lines)
    found = [f'missing frontmatter {key}' for key in FRONTMATTER_FIELDS if not fields.get(key)]
    if fields.get('description'):
        found += description_findings(fields['description'], own, names)

    spans = regions(lines, body)
    hidden = masked(lines, body, spans)
    content = [i for i in range(body, len(lines)) if lines[i].strip()]
    if not content or not lines[content[0]].startswith('# '):
        found.append('missing H1 as the first body line')
    every = spans.get(EVERY_TASK_REGION)
    if not every:
        found.append(f'missing {EVERY_TASK_REGION} region')
    elif len(content) < 2 or not lines[content[0]].startswith('# ') or content[1] != every[0]:
        found.append(f'{EVERY_TASK_REGION} region must directly follow the H1')

    headings = [(i, lines[i][3:].strip()) for i in range(body, len(lines))
                if i not in hidden and lines[i].startswith('## ')]
    positions = []
    for i, title in headings:
        index = next((k for k, (_, pattern, _) in enumerate(SECTIONS)
                      if re.fullmatch(pattern, title)), None)
        if index is None:
            if not (EXTRA_SECTIONS_ALLOWED or own in EXTRA_SECTIONS_ALLOWED_FOR):
                found.append(f'unexpected section "## {title}"')
            continue
        if positions and index <= positions[-1][1]:
            found.append(f'section order: "## {title}" after "## {positions[-1][2]}"')
        positions.append((i, index, title))
    present = {index for _, index, _ in positions}
    found += [f'missing section "{label}"' for k, (label, _, required) in enumerate(SECTIONS)
              if required and k not in present]
    if headings and headings[-1][1] != FINAL_SECTION and any(t == FINAL_SECTION for _, t in headings):
        found.append(f'"## {FINAL_SECTION}" must be the last section')

    def section(title):
        for n, (i, heading) in enumerate(headings):
            if heading == title:
                return i + 1, headings[n + 1][0] if n + 1 < len(headings) else len(lines)
        return None

    persona = section(PERSONA_SECTION)
    if persona:
        text = '\n'.join(lines[i] for i in range(*persona) if i not in hidden)
        for field in PERSONA_FIELDS:
            label = re.escape(field)
            pattern = rf'^\s*(?:[-*+]\s+)?(?:\*\*{label}(?::\*\*|\*\*:?)|{label}:)'
            if not re.search(pattern, text, re.MULTILINE):
                found.append(f'missing field {field} in "## {PERSONA_SECTION}"')
    final = section(FINAL_SECTION)
    if final:
        region = spans.get(FINAL_REPLY_REGION)
        if not region or not final[0] <= region[0] < final[1]:
            found.append(f'"## {FINAL_SECTION}" lacks the {FINAL_REPLY_REGION} region')
        if not any(lines[i].strip() for i in range(*final) if i not in hidden):
            found.append(f'"## {FINAL_SECTION}" lists no valid next actions outside the region')
    return found


def template_findings(plugin):
    names = {path.parent.name for path in skills(plugin)}
    return [f'template: {rel(path, plugin)}: {finding}'
            for path in skills(plugin) for finding in skill_findings(path, names)]


def links(text):
    """Yield (match, target path without anchor) for each Markdown link."""
    for match in LINK.finditer(text):
        target = match.group(2).split('#', 1)[0]
        if target and not re.match(r'^[a-z]+:', target) and not target.startswith('/'):
            yield match, target


def blank(text, spans):
    chars = list(text)
    for start, end in spans:
        for k in range(start, end):
            if chars[k] != '\n':
                chars[k] = ' '
    return ''.join(chars)


def readme_findings(plugin):
    plugin = Path(plugin)
    readme = (plugin / 'README.md').resolve()
    found = []
    for path in skills(plugin) + references(plugin):
        text = path.read_text(encoding='utf-8')
        spans = []
        for match, target in links(text):
            spans.append(match.span(2))
            if (path.parent / target).resolve() == readme or README_PATH.fullmatch(target):
                found.append(f'readme: {rel(path, plugin)}:{line_of(text, match.start())}: '
                             f'links the plugin README ({match.group(2)})')
        for match in README_PATH.finditer(blank(text, spans)):
            found.append(f'readme: {rel(path, plugin)}:{line_of(text, match.start())}: '
                         f'names the plugin README ({match.group(0)})')
    return found


def sentence_spans(text):
    """Yield (start, end) character offsets of each sentence (see check 3 in the docstring)."""
    unit_start = None
    offset = 0
    units = []
    for line in text.split('\n') + ['']:
        stripped = line.strip()
        starts_unit = (not stripped or stripped.startswith(('#', '|', '<!--'))
                       or LIST_ITEM.match(line) or FENCE.match(line))
        if starts_unit and unit_start is not None:
            units.append((unit_start, offset - 1 if offset else 0))
            unit_start = None
        if stripped and unit_start is None:
            unit_start = offset
        if stripped.startswith(('#', '|', '<!--')) or FENCE.match(line):
            units.append((unit_start, offset + len(line)))
            unit_start = None
        offset += len(line) + 1
    for start, end in units:
        position = start
        for match in SENTENCE_BREAK.finditer(text, start, end):
            yield position, match.start()
            position = match.end()
        yield position, end


def is_trigger_sentence(sentence):
    sentence = LINK.sub(lambda m: m.group(1), sentence.strip())
    sentence = BOLD_LABEL.sub('', LIST_ITEM.sub('', sentence))
    return bool(TRIGGER_WORDS.search(sentence) or TRIGGER_CLAUSE_WORDS.search(sentence))


def reference_findings(plugin):
    plugin = Path(plugin)
    refs = {path.resolve(): rel(path, plugin) for path in references(plugin)}
    users = {ref: [] for ref in refs}
    untriggered = {ref: [] for ref in refs}
    for skill in skills(plugin):
        text = skill.read_text(encoding='utf-8')
        linked = {(skill.parent / t).resolve() for _, t in links(text)} & set(users)
        triggered = set()
        for start, end in sentence_spans(text):
            sentence = text[start:end]
            if is_trigger_sentence(sentence):
                triggered.update((skill.parent / t).resolve() for _, t in links(sentence))
        for target in linked:
            users[target].append(rel(skill, plugin))
            if target not in triggered:
                untriggered[target].append(rel(skill, plugin))
    found = []
    for ref, name in refs.items():
        linkers = sorted(set(users[ref]))
        for skill in sorted(untriggered[ref]):
            found.append(f'reference: {name}: {skill} links it in no trigger sentence '
                         f'(Before, After, When, If, At, As ...; AC14)')
        if name.startswith('skills/'):
            own = f'skills/{name.split("/")[1]}/SKILL.md'
            others = [s for s in linkers if s != own]
            if others:
                found.append(f'reference: {name}: per-skill reference linked from {", ".join(others)}; '
                             f'move it to references/ (P-b)')
            elif not linkers:
                found.append(f'reference: {name}: not linked from any SKILL.md')
        elif not linkers:
            found.append(f'reference: {name}: not linked from any SKILL.md')
        elif len(linkers) < MIN_PLUGIN_REFERENCE_USERS:
            found.append(f'reference: {name}: plugin-level reference linked from {len(linkers)} SKILL.md '
                         f'({", ".join(linkers)}); move it to that skill\'s references/ (P-b)')
        text = Path(ref).read_text(encoding='utf-8')
        for match, target in links(text):
            resolved = (Path(ref).parent / target).resolve()
            if resolved in refs and resolved != ref:
                found.append(f'reference: {name}:{line_of(text, match.start())}: links reference '
                             f'{refs[resolved]}; link it from SKILL.md instead (P-a)')
    return found


def bare_path_findings(plugin):
    plugin = Path(plugin)
    found = []
    for path in skills(plugin) + references(plugin):
        text = path.read_text(encoding='utf-8')
        scanned = blank(text, [m.span() for m in LINK.finditer(text)])
        parts = Path(rel(path, plugin)).parts
        own = (plugin / parts[0] / parts[1]).resolve() if parts[0] == 'skills' else None
        for match in BARE_REFERENCE.finditer(scanned):
            where = f'bare-path: {rel(path, plugin)}:{line_of(text, match.start())}: {match.group(1)}'
            target = (path.parent / match.group(1)).resolve()
            if not target.exists():
                found.append(f'{where} does not resolve from this file; use a Markdown link')
            elif own is None or own not in target.parents:
                found.append(f'{where} names a plugin-level or other skill\'s file; use a Markdown link')
    return found


def size_findings(plugin):
    plugin = Path(plugin)
    found = []
    for pattern, limit in SIZE_LIMITS:
        for path in sorted(plugin.glob(pattern)):
            count = len(path.read_text(encoding='utf-8').splitlines())
            if count > limit:
                found.append(f'size: {rel(path, plugin)}: {count} lines > {limit}')
    return found


CHECKS = [template_findings, readme_findings, reference_findings, bare_path_findings, size_findings]


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    plugin = Path(argv[0]) if argv else Path('plugins/lusona')
    if not skills(plugin):
        print(f'no skills/*/SKILL.md in {plugin}')
        return 2
    counts = {}
    for check in CHECKS:
        findings = check(plugin)
        counts[check.__name__.replace('_findings', '').replace('_', '-')] = len(findings)
        for finding in findings:
            print(finding)
    total = sum(counts.values())
    if not total:
        print('Skill template checks passed.')
        return 0
    print(f'{total} finding(s): ' + ', '.join(f'{name} {n}' for name, n in counts.items()))
    return 1


if __name__ == '__main__':
    sys.exit(main())
