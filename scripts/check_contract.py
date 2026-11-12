#!/usr/bin/env python3
"""Check the Lusona public contract K1-K5 (spec 20261111, AC4-AC8) and AC15 (no manifest hooks).

Usage: check_contract.py [PLUGIN_DIR]  (default plugins/lusona)
Exit 0 when every contract item holds; exit 1 with one finding per line otherwise.

K2 (AC5) reads each item from the reference that defines it (DEFINING): every path in PATHS
from references/files.md, the ID form from references/naming.md, every queue state from
references/queue.md. A name found only in other files does not count. HTML comments and fenced
code blocks in the defining reference do not count. A path counts in the first cell of a table row
or in a prose sentence with no negation word; "Do not use docs/lusona/plans/" does not count.
Queue states count anywhere in the remaining text, prose included, because baseline 34186da names
Icebox only in prose. Limits: a path whose table row says it is removed still counts, and a queue
state whose table row was deleted still counts while prose names it.

K4 (AC7) reads the generated shared regions of each skills/*/SKILL.md (every-task and
final-reply, copies of the shared block and final-reply sources; spec decision 13). Decision 12
requires the vocabulary in skill, reference or shared text; these regions are shared text, so
requiring them satisfies both. One skill's two regions together must name every TDD level (in
backticks) and every reply status, and hold one prose sentence with a clause in which specs, plans,
ADRs and queue states all precede "do not", "does not", "must not", "cannot", "never" or a "n't"
contraction directly before "authorize" and the clause names implementation. "Users do not
authorize implementation lightly; specs, plans, ADRs and queue states do." does not count.

In addition, every contract Markdown clause (sentences split at ";", ":" and dashes) that names
those four and a form of "authori[sz]e" with any object is reported as an affirmative authority
sentence, unless a negation word stands within four words before that verb or the clause starts
with "No", "Neither" or "None". A negation elsewhere in the sentence ("when no question remains")
does not exempt it. A clause naming the four and ending in "do", "does", "can", "may", "will" or
"shall" in a sentence that uses "authorize" is reported too (the elliptical "...; specs, plans,
ADRs and queue states do."). A lead-in ending in ":" is read together with the list items that
follow it, so "These authorize implementation:" followed by "- specs", "- plans", "- ADRs",
"- queue states" is reported at the lead-in line. Limits: an affirmative spread over several
sentences, table cells, or a list without a ":" lead-in is not detected; a negation within four
words before the verb exempts the clause even when it negates something else.

K3 (AC6) compares the work-record test files with the baseline: each baseline line must remain,
and an added line holding an exit or return statement (exit, return, [Environment]::Exit) is a
finding, since it can end the tests before the assertions run.

Contract Markdown is every Markdown file in the plugin except the plugin README (not contract,
spec decision 3) and templates/ (exempt, spec decision 2). Catalogs and the work-record test
files are read from the repository root.
"""
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = '34186da'

# Contract inventory at baseline commit 34186da (git show 34186da:<path>).
# K1: skill directories under skills/; each SKILL.md frontmatter name equals its directory.
SKILLS = ('architect', 'batch', 'design', 'experiment', 'explore', 'frame-product', 'implement',
          'investigate', 'map-capabilities', 'measure', 'refactor', 'review', 'specify', 'status')
# K2: project data paths (references/files.md), record ID form (references/naming.md), queue
# states (references/queue.md); product.md, plans/, batches/, visuals/, README.md per decision 8.
PATHS = ('docs/lusona/README.md', 'docs/lusona/product.md', 'docs/lusona/work.md',
         'docs/lusona/specs/', 'docs/lusona/plans/', 'docs/lusona/batches/', 'docs/lusona/notes/',
         'docs/lusona/visuals/', 'docs/lusona/evidence/', 'docs/lusona/history/', 'docs/lusona/adr/')
ID_FORM = 'YYYYMMDD-'
QUEUE_STATES = ('Ideas', 'Ready', 'Doing', 'Review', 'Done', 'Icebox')
# Reference that defines each K2 item (AC5: "absent from the rewritten references that define them").
DEFINING = {'paths': 'references/files.md', 'id': 'references/naming.md', 'queue': 'references/queue.md'}
# K3: helper commands (scripts/work-record.sh and .ps1 dispatch; references/naming.md),
# JSON fields and statuses of init-change and init-adr. Exit codes 0/3/1 are exercised by
# scripts/test-work-record.sh and .ps1, whose baseline lines are compared below.
HELPERS = ('scripts/work-record.sh', 'scripts/work-record.ps1')
# Argument signatures and exit codes are recorded here; the check enforces only command and token
# presence, and the test-file comparison carries argument and exit-code behavior.
COMMANDS = {'slug': 'TITLE', 'history-path': '[DATE]', 'init-history': 'PROJECT_ROOT [DATE]',
            'init-notes': 'PROJECT_ROOT SLUG', 'init-change': 'PROJECT_ROOT SLUG [DATE]',
            'init-adr': 'PROJECT_ROOT SLUG [DATE]', 'next-adr': 'PROJECT_ROOT',
            'next-change': 'PROJECT_ROOT', 'stamp-header': 'FILE [DATE]', 'help': ''}
JSON_FIELDS = ('status', 'path', 'message')
EXIT_CODES = {'created': 0, 'conflict': 3, 'error': 1}
HELPER_TOKENS = (*JSON_FIELDS, *EXIT_CODES)
TEST_FILES = ('scripts/test-work-record.sh', 'scripts/test-work-record.ps1')
# K4: TDD levels (references/tdd.md), reply statuses (templates/status.md and README at
# baseline), authority rule (README Contract at baseline).
TDD_LEVELS = ('none', 'targeted', 'strict')
STATUSES = ('Complete', 'In progress', 'Needs input', 'Paused')
RECORD_TERMS = (r'\bspecs?\b', r'\bplans?\b', r'\badrs?\b', r'\bqueue\b')
AUTHORITY_TERMS = (*RECORD_TERMS, r'\bauthori', r'\bimplement')
NEGATED_AUTHORIZE = r"\b(?:(?:do|does|did|must|shall|will|can|may)\s+not|cannot|never|\w+n't)\s+authori[sz]e"
NEGATION = r"\b(?:not|never|cannot|no|none|neither|nor)\b|n't\b"
AUTHORIZE_VERB = re.compile(r'\bauthori[sz](?:e|es|ed|ing)\b', re.I)
NEGATION_BEFORE_VERB = re.compile(rf"(?:{NEGATION})(?:\W+\w+){{0,4}}?\W*$", re.I)
NEGATED_SUBJECT = re.compile(r'^\W*(?:no|neither|none)\b', re.I)
ELLIPTICAL_AFFIRMATIVE = re.compile(r'\b(?:do|does|can|may|will|shall)\W*$', re.I)
CLAUSE_BREAK = re.compile(r'[;:]|\s[-\u2013\u2014]+\s|\u2014')
HIDDEN = re.compile(r'<!--.*?-->|^ {0,3}(```|~~~).*?^ {0,3}\1[^\n]*$', re.S | re.M)
SHARED_REGIONS = ('every-task', 'final-reply')
EXIT_STATEMENT = re.compile(r'(?<![\w$-])(?:exit|return)\b|::exit\s*\(', re.I)
# K5: plugin name in native manifests and repository catalogs.
NAME = 'lusona'
NATIVE_MANIFESTS = ('.claude-plugin/plugin.json', '.codex-plugin/plugin.json')
CATALOGS = ('.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json',
            '.cursor-plugin/marketplace.json')


def contract_markdown(plugin):
    plugin = Path(plugin)
    return {path.relative_to(plugin).as_posix(): path.read_text()
            for path in sorted(plugin.rglob('*.md'))
            if path.relative_to(plugin).parts[0] != 'templates' and path != plugin / 'README.md'}


def has_word(text, word):
    return re.search(rf'(?<![\w-]){re.escape(word)}(?![\w-])', text) is not None


def skill_findings(plugin):
    findings = []
    for name in SKILLS:
        path = Path(plugin) / 'skills' / name / 'SKILL.md'
        if not path.is_file():
            findings.append(f'K1: skill directory missing: skills/{name}')
            continue
        match = re.match(r'---\n(.*?)\n---\n', path.read_text(), re.S)
        found = match and re.search(r'^name:\s*(.*?)\s*$', match.group(1), re.M)
        actual = found.group(1) if found else None
        if actual and len(actual) >= 2 and actual[0] == actual[-1] and actual[0] in '"\'':
            actual = actual[1:-1]
        if actual != name:
            findings.append(f'K1: skills/{name}/SKILL.md frontmatter name is {actual!r}, expected {name!r}')
    return findings


def visible(text):
    """Text with HTML comments and fenced code blocks blanked; newlines are kept."""
    return HIDDEN.sub(lambda m: re.sub(r'[^\n]', ' ', m.group(0)), text)


def defines_path(text, path):
    """True when path is in the first cell of a table row or in a prose sentence with no negation."""
    for line in text.splitlines():
        cells = line.strip().split('|')
        if line.strip().startswith('|') and len(cells) > 2 and path in cells[1]:
            return True
    return any(path in sentence and not re.search(NEGATION, sentence, re.I) for sentence in sentences(text))


def layout_findings(plugin):
    plugin = Path(plugin)
    texts = {}
    findings = []
    for key, relative in DEFINING.items():
        path = plugin / relative
        if path.is_file():
            texts[key] = visible(path.read_text())
        else:
            findings.append(f'K2: defining reference missing: {relative}')
    if 'paths' in texts:
        findings += [f'K2: path {path} absent from {DEFINING["paths"]}'
                     for path in PATHS if not defines_path(texts['paths'], path)]
    if 'id' in texts and ID_FORM not in texts['id']:
        findings.append(f'K2: record ID form YYYYMMDD-slug absent from {DEFINING["id"]}')
    if 'queue' in texts and not all(has_word(texts['queue'], state) for state in QUEUE_STATES):
        findings.append(f'K2: {DEFINING["queue"]} does not name every queue state: ' + ', '.join(QUEUE_STATES))
    return findings


def numbered_sentences(text):
    """(line, sentence) for prose sentences; table rows are skipped and each list item starts
    a new paragraph."""
    paragraph, start = [], None
    for number, line in enumerate(text.splitlines() + [''], 1):
        stripped = line.strip()
        item = re.match(r'(?:[-*+]|\d+[.)])\s+', stripped)
        if not stripped or stripped.startswith('|') or item:
            if paragraph:
                for sentence in re.split(r'(?<=[.!?])\s+', ' '.join(paragraph)):
                    yield start, sentence
            paragraph, start = [], None
            if item:
                stripped = stripped[item.end():]
            else:
                continue
        if start is None:
            start = number
        paragraph.append(stripped)


def sentences(text):
    return [sentence for _, sentence in numbered_sentences(text)]


def names_records(text):
    return all(re.search(term, text, re.I) for term in RECORD_TERMS)


def clauses(sentence):
    return CLAUSE_BREAK.split(sentence)


def states_rule(sentence):
    """True when a clause has the four record types before a negated "authorize" and names implementation."""
    for clause in clauses(sentence):
        match = re.search(NEGATED_AUTHORIZE, clause, re.I)
        if match and names_records(clause[:match.start()]) and re.search(r'\bimplement', clause, re.I):
            return True
    return False


def states_affirmative(sentence):
    """True when a clause names the four record types and an authorize verb that no nearby
    negation governs, or ends elliptically ("...queue states do.") in a sentence about authorizing."""
    for clause in clauses(sentence):
        if not names_records(clause) or NEGATED_SUBJECT.search(clause):
            continue
        for verb in AUTHORIZE_VERB.finditer(clause):
            if not NEGATION_BEFORE_VERB.search(clause[:verb.start()]):
                return True
        if (AUTHORIZE_VERB.search(sentence) and ELLIPTICAL_AFFIRMATIVE.search(clause)
                and not re.search(NEGATION, clause, re.I)):
            return True
    return False


def list_lead_ins(text):
    """(line, lead-in sentence followed by its list items) for each lead-in ending in ":"."""
    lines = text.splitlines()
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped.endswith(':') or stripped.startswith('|'):
            continue
        items = []
        for following in lines[number:]:
            item = re.match(r'\s*(?:[-*+]|\d+[.)])\s+(.*)', following)
            if item:
                items.append(item.group(1).strip())
            elif following.strip():
                break
        if items:
            lead = re.split(r'(?<=[.!?])\s+', re.sub(r'^(?:[-*+]|\d+[.)])\s+', '', stripped))[-1]
            yield number, lead[:-1] + ' ' + ', '.join(items) + '.'


def shared_texts(plugin):
    """{skill: text of its every-task and final-reply regions} for each skills/*/SKILL.md."""
    texts = {}
    for path in sorted(Path(plugin).glob('skills/*/SKILL.md')):
        text = path.read_text()
        bodies = [m.group(1) for name in SHARED_REGIONS for m in re.finditer(
            rf'(?ms)^<!-- lusona:begin {name} -->\n(.*?)^<!-- lusona:end {name} -->$', text)]
        texts[path.parent.name] = '\n\n'.join(bodies)
    return texts


def vocabulary_findings(plugin):
    shared = shared_texts(plugin).values()
    findings = []
    where = 'K4: shared every-task and final-reply regions'
    if not any(all(f'`{level}`' in text for level in TDD_LEVELS) for text in shared):
        findings.append(f'{where} do not name every TDD level: ' + ', '.join(TDD_LEVELS))
    if not any(all(has_word(text, status) for status in STATUSES) for text in shared):
        findings.append(f'{where} do not name every reply status: ' + ', '.join(STATUSES))
    if not any(states_rule(sentence) for text in shared for sentence in sentences(text)):
        findings.append(f'{where} have no sentence stating that specs, plans, ADRs and queue states '
                        'do not authorize implementation')
    for relative, text in contract_markdown(plugin).items():
        units = sorted([*numbered_sentences(text), *list_lead_ins(text)], key=lambda unit: unit[0])
        for number in dict.fromkeys(number for number, unit in units if states_affirmative(unit)):
            findings.append(f'K4: {relative}:{number}: sentence states that specs, plans, ADRs and '
                            'queue states authorize implementation')
    return findings


def helper_findings(plugin):
    findings = []
    for relative in HELPERS:
        path = Path(plugin) / relative
        if not path.is_file():
            findings.append(f'K3: helper missing: {relative}')
            continue
        text = path.read_text()
        findings += [f'K3: {relative} does not name command {c}' for c in COMMANDS if not has_word(text, c)]
        findings += [f'K3: {relative} does not name {t}' for t in HELPER_TOKENS if not has_word(text, t)]
    return findings


def assertion_lines(text):
    return Counter(line.strip() for line in text.splitlines()
                   if line.strip() and not line.strip().startswith('#'))


# Decision 22 (spec 20261111): helper-test lines may change only by the template rename
# `templates/<name>.md` -> `templates/<name>.md.template` (13 lines, tmp/w5c/test-diff.patch).
TEMPLATE_NAME = re.compile(r'(templates/[\w$]+\.md)\b(?!\.template)')


def renamed_template_line(line):
    return TEMPLATE_NAME.sub(r'\1.template', line)


def assertion_findings(baseline, current, label):
    lost = assertion_lines(baseline) - assertion_lines(current)
    added = assertion_lines(current) - assertion_lines(baseline)
    renamed = Counter({line: count for line, count in lost.items()
                       if renamed_template_line(line) != line})
    kept = Counter({line: min(count, added[renamed_template_line(line)])
                    for line, count in renamed.items()})
    lost -= kept
    added -= Counter({renamed_template_line(line): count for line, count in kept.items()})
    return ([f'K3: {label} lost baseline line: {line}' for line in sorted(lost.elements())]
            + [f'K3: {label} adds an exit or return line: {line}' for line in sorted(added.elements())
               if EXIT_STATEMENT.search(line.split(' #', 1)[0])])


def git_baseline(relative):
    return subprocess.run(['git', 'show', f'{BASELINE}:{relative}'], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout


def work_record_test_findings(root, read_baseline=git_baseline):
    findings = []
    for relative in TEST_FILES:
        try:
            baseline = read_baseline(relative)
        except (OSError, subprocess.CalledProcessError) as error:
            findings.append(f'K3: cannot read baseline {BASELINE}:{relative}: {error}')
            continue
        path = Path(root) / relative
        if not path.is_file():
            findings.append(f'K3: test file missing: {relative}')
            continue
        findings += assertion_findings(baseline, path.read_text(), relative)
    return findings


def manifest_findings(plugin, root):
    findings = []
    plugin, root = Path(plugin), Path(root)
    for relative in NATIVE_MANIFESTS:
        if not (plugin / relative).is_file():
            findings.append(f'K5: native manifest missing: {relative}')
    for path in sorted(plugin.glob('.*-plugin/plugin.json')):
        relative = path.relative_to(plugin).as_posix()
        try:
            name = json.loads(path.read_text()).get('name')
        except ValueError as error:
            findings.append(f'K5: {relative} is not valid JSON: {error}')
            continue
        if name != NAME:
            findings.append(f'K5: {relative} names {name!r}, expected {NAME!r}')
    for relative in CATALOGS:
        path = root / relative
        if not path.is_file():
            findings.append(f'K5: catalog missing: {relative}')
            continue
        try:
            entries = json.loads(path.read_text()).get('plugins') or []
        except ValueError as error:
            findings.append(f'K5: {relative} is not valid JSON: {error}')
            continue
        if not entries:
            findings.append(f'K5: {relative} lists no plugins')
        for entry in entries:
            if entry.get('name') != NAME:
                findings.append(f'K5: {relative} names {entry.get("name")!r}, expected {NAME!r}')
    return findings


def hooks_findings(plugin):
    """AC15 (20261110 AC10): no runtime hooks; no native manifest may declare `hooks`."""
    findings = []
    for path in sorted(Path(plugin).glob('.*-plugin/plugin.json')):
        try:
            declared = 'hooks' in json.loads(path.read_text())
        except ValueError:
            continue  # reported by manifest_findings
        if declared:
            findings.append(f'AC15: {path.relative_to(plugin).as_posix()} declares hooks')
    return findings


def check(plugin, root=ROOT):
    return (skill_findings(plugin) + layout_findings(plugin) + helper_findings(plugin)
            + work_record_test_findings(root) + vocabulary_findings(plugin) + manifest_findings(plugin, root)
            + hooks_findings(plugin))


if __name__ == '__main__':
    findings = check(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'plugins/lusona')
    print('\n'.join(findings))
    sys.exit(1 if findings else 0)
