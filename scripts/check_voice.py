#!/usr/bin/env python3
"""Check skill voice limits (V5, V6) in the Lusona plugin text.

Scanned files, relative to the plugin directory: ``skills/*/SKILL.md``,
``skills/*/references/**/*.md``, ``references/**/*.md``, ``shared/**/*.md`` when ``shared/`` exists,
``templates/*.md`` and ``templates/*.md.template``. Templates are checked for banned terms only, not for sentence length.

1. Banned terms. Each term in ``TERMS`` is matched as a whole word, case-insensitively.
   Words of a phrase may be separated by any whitespace, including a line wrap; the
   finding reports the line where the phrase starts. Excluded regions: YAML
   frontmatter other than the ``description`` value (folded continuation lines included),
   fenced code blocks, inline code, and Markdown link targets. Link text, the frontmatter
   ``description``, headings, table cells, block quotes and HTML comments are scanned.
2. Sentence length. The average number of words per sentence in a file must not exceed
   ``--max-avg-words``, and no sentence may exceed ``--max-sentence-words``. Sentences are counted in prose only: frontmatter (the description included), fenced code,
   headings and table rows are excluded; each list item starts a new sentence.

The banned list lives here so that plugin text never needs to name the banned words.

Usage: check_voice.py [PLUGIN_DIR] [--max-avg-words N] [--max-sentence-words N]
Exit status 0 when clean; 1 with ``path:line: finding`` lines; 2 when no file was
scanned (missing or wrong plugin directory).
"""
import argparse
import re
import sys
from pathlib import Path

# Accepted by the user 2026-11-11 (spec 20261111-loop-principles-and-skill-rewrite, W2,
# AC2; docs/lusona/notes/voice-limits-measurement.md).
DEFAULT_MAX_AVG_WORDS = 15
DEFAULT_MAX_SENTENCE_WORDS = 40

# Term -> regular expression for the accepted inflections. Accepted by the user
# 2026-11-11 (AC2).
TERMS = {
    # V5 hedges, named in the spec. "considered" is excluded: it is used as a
    # participle ("alternatives considered"), not as a hedge.
    'usually': r'usually',
    'consider': r'consider|considers|considering',
    'may want to': r'may\s+want\s+to',
    'try to': r'(?:try|tries|trying)\s+to',
    # Vague conditions, banned as hedges under V5 (user decision 2026-11-11).
    'as needed': r'as\s+needed',
    'when needed': r'when\s+needed',
    # Vague conditions found by the voice pass and accepted by the user 2026-11-11
    # (docs/lusona/notes/voice-limits-measurement.md, decision 5).
    # "when relevant", "when useful" and "if relevant" from that decision are covered by the
    # bare words below.
    'if needed': r'if\s+needed',
    'omit when unnecessary': r'omit\s+when\s+unnecessary',
    # Accepted by the user 2026-11-11, round 3 (same note, decision 14): two more vague
    # conditions, and bare qualifiers that carry no test. "relevance" and "usefulness" do not match.
    'when applicable': r'when\s+applicable',
    'if applicable': r'if\s+applicable',
    'relevant': r'relevant',
    'irrelevant': r'irrelevant',
    'useful': r'useful(?:ly)?',
    # Hedges proposed by the W2 analyst and accepted by the user 2026-11-11.
    'generally': r'generally',
    'typically': r'typically',
    'ideally': r'ideally',
    'perhaps': r'perhaps',
    'probably': r'probably',
    'possibly': r'possibly',
    'maybe': r'maybe',
    # V6 filler adjectives, with their -ly adverbs.
    'robust': r'robust(?:ly)?',
    'seamless': r'seamless(?:ly)?',
    'elegant': r'elegant(?:ly)?',
    'powerful': r'powerful(?:ly)?',
    'best-in-class': r'best-in-class',
    # V6 filler verbs, with their inflections.
    'leverage': r'leverage|leverages|leveraged|leveraging',
    'delve': r'delve|delves|delved|delving',
    'unlock': r'unlock|unlocks|unlocked|unlocking',
    'streamline': r'streamline|streamlines|streamlined|streamlining',
}
# Whole word: no letter or digit on either side. Hyphenated compounds
# ("over-leveraged") and underscore emphasis (_usually_) still match.
BOUNDARY_BEFORE, BOUNDARY_AFTER = r'(?<![A-Za-z0-9])', r'(?![A-Za-z0-9])'
PATTERNS = {term: re.compile(BOUNDARY_BEFORE + '(?:' + pattern + ')' + BOUNDARY_AFTER, re.IGNORECASE)
            for term, pattern in TERMS.items()}

LINK = re.compile(r'\[([^\]]*)\]\([^)]*\)')
LINK_TARGET = re.compile(r'(?<=\])\([^)]*\)')
FRONTMATTER_KEY = re.compile(r'^([A-Za-z_-]+):(.*)$')
INLINE_CODE = re.compile(r'`[^`\n]*`')
LIST_ITEM = re.compile(r'^([-*+]|\d+[.)])\s+')
ABBREVIATION = re.compile(r'^\(?(e\.g|i\.e|etc|vs|cf)\.$', re.IGNORECASE)
SENTENCE_END = re.compile(r'[.!?]["\')\]*_]*$')
WORD = re.compile(r'[A-Za-z0-9]')


def instruction_files(plugin):
    """Files checked for banned terms and sentence length."""
    plugin = Path(plugin)
    files = sorted(plugin.glob('skills/*/SKILL.md')) + sorted(plugin.glob('skills/*/references/**/*.md'))
    files += sorted(plugin.glob('references/**/*.md'))
    return files + sorted(plugin.glob('shared/**/*.md'))


def scanned_files(plugin):
    """Files checked for banned terms: instruction files and Markdown templates."""
    templates = Path(plugin).glob('templates/*.md')
    renamed = Path(plugin).glob('templates/*.md.template')
    return instruction_files(plugin) + sorted([*templates, *renamed])


def _blank(match):
    return re.sub(r'[^\n]', ' ', match.group(0))


def _without_blocks(text):
    """Blank frontmatter and fenced code blocks; keep every newline."""
    lines = text.split('\n')
    out, start = [], 0
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                out, start = [''] * (i + 1), i + 1
                break
    fence = None
    for line in lines[start:]:
        stripped = line.lstrip()
        if fence:
            out.append('')
            if stripped.startswith(fence):
                fence = None
        elif stripped.startswith('```') or stripped.startswith('~~~'):
            fence = stripped[:3]
            out.append('')
        else:
            out.append(line)
    return '\n'.join(out)


def _description_lines(lines):
    """{line index: text} for the frontmatter ``description`` value, key blanked."""
    found = {}
    if not lines or lines[0].strip() != '---':
        return found
    inside = False
    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == '---':
            return found
        match = FRONTMATTER_KEY.match(line)
        if match:
            inside = match.group(1) == 'description'
            if inside:
                found[i] = ' ' * (len(match.group(1)) + 1) + match.group(2)
        elif inside and line[:1] in (' ', '\t'):
            found[i] = line
    return {}


def term_text(text):
    """Text with every excluded region blanked; offsets and line numbers are kept."""
    lines = _without_blocks(text).split('\n')
    for i, value in _description_lines(text.split('\n')).items():
        lines[i] = value
    text = INLINE_CODE.sub(_blank, '\n'.join(lines))
    return LINK_TARGET.sub(_blank, text)


def terms_in(text):
    """Return sorted (line, term) for banned terms in one file's text."""
    scanned = term_text(text)
    found = []
    for term, pattern in PATTERNS.items():
        for match in pattern.finditer(scanned):
            found.append((scanned.count('\n', 0, match.start()) + 1, term))
    return sorted(found)


def sentence_lengths(text):
    """Return (first_line, word_count) for each prose sentence.

    Inline code counts as one word; link text counts and link targets do not.
    A sentence ends at a token ending in ".", "!" or "?" (closing quotes, brackets and
    emphasis markers allowed), except the abbreviations e.g., i.e., etc., vs., cf.
    A paragraph, list item, heading or table row also ends a sentence.
    """
    text = INLINE_CODE.sub('CODE', _without_blocks(text))
    text = LINK.sub(lambda m: m.group(1), text)
    sentences, words, first = [], 0, None

    def close():
        nonlocal words, first
        if words:
            sentences.append((first, words))
        words, first = 0, None

    for number, line in enumerate(text.split('\n'), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('|'):
            close()
            continue
        if LIST_ITEM.match(stripped):
            close()
            stripped = LIST_ITEM.sub('', stripped)
        stripped = stripped.lstrip('> ')
        for token in stripped.split():
            if WORD.search(token):
                if first is None:
                    first = number
                words += 1
            if SENTENCE_END.search(token) and not ABBREVIATION.match(token):
                close()
    close()
    return sentences


def term_findings(plugin):
    plugin = Path(plugin)
    return [(path.relative_to(plugin), number, term)
            for path in scanned_files(plugin)
            for number, term in terms_in(path.read_text(encoding='utf-8'))]


def length_findings(plugin, max_avg=DEFAULT_MAX_AVG_WORDS, max_sentence=DEFAULT_MAX_SENTENCE_WORDS):
    plugin = Path(plugin)
    findings = []
    for path in instruction_files(plugin):
        sentences = sentence_lengths(path.read_text(encoding='utf-8'))
        for number, words in sentences:
            if words > max_sentence:
                findings.append((path.relative_to(plugin), number,
                                 f'sentence of {words} words exceeds {max_sentence:g}'))
        counts = [n for _, n in sentences]
        average = sum(counts) / len(counts) if counts else 0
        if average > max_avg:
            findings.append((path.relative_to(plugin), 1,
                             f'average {average:.1f} words per sentence exceeds {max_avg:g}'))
    return findings


def main(argv=None):
    parser = argparse.ArgumentParser(description='Check skill voice limits.')
    parser.add_argument('plugin', nargs='?', default='plugins/lusona')
    parser.add_argument('--max-avg-words', type=float, default=DEFAULT_MAX_AVG_WORDS)
    parser.add_argument('--max-sentence-words', type=int, default=DEFAULT_MAX_SENTENCE_WORDS)
    args = parser.parse_args(argv)
    if not scanned_files(args.plugin):
        print(f'no skill, reference or shared files found under {args.plugin}', file=sys.stderr)
        return 2
    findings = term_findings(args.plugin) + length_findings(args.plugin, args.max_avg_words,
                                                            args.max_sentence_words)
    for path, number, message in findings:
        print(f'{path}:{number}: {message}')
    if findings:
        print(f'{len(findings)} finding(s).', file=sys.stderr)
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main())
