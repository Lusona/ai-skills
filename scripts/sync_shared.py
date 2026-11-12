#!/usr/bin/env python3
"""Generate shared source text into each skill's marked regions.

Each ``PLUGIN_DIR/skills/*/SKILL.md`` holds one region per shared source file::

    <!-- lusona:begin NAME -->
    ...generated text...
    <!-- lusona:end NAME -->

NAME is the basename of a ``SOURCE_DIR/*.md`` file without ``.md``. Each marker is a whole
line; the first line after the begin marker that starts with the end marker ends the region,
and any other text on that line is a problem (it is not skipped for a later marker). Sync replaces each
region body with that file's content; a body always ends with one newline.

Without ``--check``, every skill is validated first; when any skill lacks a region for a
source file, has an unterminated or duplicate region, or has a region without a source
file, nothing is written and the exit status is 1. With ``--check``, nothing is written;
the exit status is 1 when any skill has such a problem or a region body differs from its
source.

Word limit: a source named in ``WORD_LIMITS`` must not hold more whitespace-separated words
than its limit (the count ``wc -w`` gives). An over-limit source is a finding in both modes,
and without ``--check`` nothing is written.

Usage: sync_shared.py --source SOURCE_DIR PLUGIN_DIR [--check]
In this repository the sources live in repository-level ``shared/`` (not packaged; spec
20261111 decision 13): ``python3 scripts/sync_shared.py --source shared plugins/lusona [--check]``.
Exit status 0 when in sync (or synced); 1 with ``path: finding`` lines; 2 when the source
directory has no ``.md`` file or the plugin directory has no ``SKILL.md``.
"""
import argparse
import re
import sys
from pathlib import Path

BEGIN = re.compile(r'^<!-- lusona:begin ([a-z0-9-]+) -->\n', re.MULTILINE)
END = '<!-- lusona:end {name} -->'
# Source stem -> maximum words. Set by the user 2026-11-11 for the every-task block, which is
# copied into every skill (docs/lusona/notes/voice-limits-measurement.md, decision 10).
WORD_LIMITS = {'every-task': 300}


def normalized(text):
    """Source text as it appears in a region body: ends with exactly one newline."""
    return text.rstrip('\n') + '\n'


def regions(text):
    """Return ({name: (body_start, body_end)}, problems) for one file's text."""
    found, problems = {}, []
    for match in BEGIN.finditer(text):
        name = match.group(1)
        end_marker = END.format(name=name)
        end = text.find('\n' + end_marker, match.end() - 1)
        line_end = text.find('\n', end + 1) if end != -1 else -1
        marker_line = text[end + 1:line_end if line_end != -1 else len(text)]
        if end == -1:
            problems.append(f'region {name} has no end marker')
        elif marker_line != end_marker:
            problems.append(f'region {name} end marker line has extra text')
        elif name in found:
            problems.append(f'region {name} appears more than once')
        else:
            found[name] = (match.end(), end + 1)
    return found, problems


def sources(source_dir):
    return {p.stem: normalized(p.read_text(encoding='utf-8'))
            for p in sorted(Path(source_dir).glob('*.md'))}


def plan(source, plugin):
    """Return ({skill_path: new_text}, findings) without writing."""
    shared = sources(source)
    updates, findings = {}, []
    for name, limit in sorted(WORD_LIMITS.items()):
        words = len(shared.get(name, '').split())
        if words > limit:
            findings.append(f'{Path(source) / (name + ".md")}: {words} words exceeds {limit}')
    plugin = Path(plugin)
    for skill in sorted(plugin.glob('skills/*/SKILL.md')):
        label = skill.relative_to(plugin)
        text = skill.read_text(encoding='utf-8')
        found, problems = regions(text)
        problems += [f'region {n} has no source file' for n in found if n not in shared]
        problems += [f'missing region {n}' for n in shared if n not in found]
        if problems:
            findings += [f'{label}: {p}' for p in problems]
            continue
        new = text
        for name, (start, end) in sorted(found.items(), key=lambda item: -item[1][0]):
            new = new[:start] + shared[name] + new[end:]
        if new != text:
            updates[skill] = new
            findings += [f'{label}: region {n} differs from source' for n, (s, e) in found.items()
                         if text[s:e] != shared[n]]
    return updates, findings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--source', required=True, help='directory of shared NAME.md files')
    parser.add_argument('plugin', help='plugin directory containing skills/*/SKILL.md')
    parser.add_argument('--check', action='store_true', help='report differences; write nothing')
    args = parser.parse_args(argv)
    plugin = Path(args.plugin)
    if not sources(args.source):
        print(f'no .md source files in {args.source}')
        return 2
    if not list(plugin.glob('skills/*/SKILL.md')):
        print(f'no skills/*/SKILL.md in {plugin}')
        return 2
    updates, findings = plan(args.source, plugin)
    if args.check:
        for finding in findings:
            print(finding)
        print('Shared regions in sync.' if not findings else f'{len(findings)} finding(s).')
        return 1 if findings else 0
    errors = [f for f in findings if not f.endswith('differs from source')]
    if errors:
        for finding in errors:
            print(finding)
        print(f'{len(errors)} error(s); nothing written.')
        return 1
    for skill, text in updates.items():
        skill.write_text(text, encoding='utf-8')
        print(f'synced {skill.relative_to(plugin)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
