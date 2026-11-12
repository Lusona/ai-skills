#!/usr/bin/env python3
"""Tests for scripts/check_skill_template.py against fixture plugins in temporary directories.

The live plugin is not asserted here: it predates the template and fails by design.
"""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/check_skill_template.py'
spec = importlib.util.spec_from_file_location('check_skill_template', SCRIPT)
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

PERSONA = """## Persona and judgment

**Persona**: {name} worker.

- Responsibility: do {name}.
- Decision criteria: smallest change.
- **Evidence**: inspected files.
- Failure modes: guessing.
"""


def skill_text(name, other, extra_links=''):
    return f"""---
name: {name}
description: Do {name} work and record it. Use when {name} is needed. Not for {other} work; use {other}.
---

# {name.title()}

<!-- lusona:begin every-task -->
Every-task rules. Before dispatch, read [delegation](../../references/shared.md).
<!-- lusona:end every-task -->

{PERSONA.format(name=name)}
## Establish the input

Read the request.{extra_links}

## {name.title()} practices

Check things.

## Work and record

Do the work.

## Final reply

<!-- lusona:begin final-reply -->
**Result**: Complete.
<!-- lusona:end final-reply -->

Valid next actions: {other}.
"""


class Fixture(unittest.TestCase):
    """A plugin with two skills in the target shape.

    - references/shared.md: linked by both skills (inside the every-task region).
    - skills/alpha/references/own.md: linked only by alpha.
    """

    def setUp(self):
        (ROOT / 'tmp').mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='skill-template-test-', dir=ROOT / 'tmp')
        self.plugin = Path(self.temporary.name) / 'lusona'
        self.write('README.md', '# Plugin\n')
        self.write('skills/alpha/SKILL.md',
                   skill_text('alpha', 'beta', ' Before X, read [own](references/own.md).'))
        self.write('skills/beta/SKILL.md', skill_text('beta', 'alpha'))
        self.write('references/shared.md', '# Shared\n\nText.\n')
        self.write('skills/alpha/references/own.md', '# Own\n\nText.\n')
        self.write('templates/spec.md.template', '# Spec\n')
        self.write('templates/page.html', 'x\n' * 1000)
        self.write('scripts/tool.sh', 'x\n' * 1000)

    def tearDown(self):
        self.temporary.cleanup()

    def write(self, relative, text):
        path = self.plugin / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def read(self, relative):
        return (self.plugin / relative).read_text()

    def edit(self, relative, old, new):
        text = self.read(relative)
        self.assertIn(old, text)
        self.write(relative, text.replace(old, new, 1))

    def all_findings(self):
        return (check.template_findings(self.plugin) + check.readme_findings(self.plugin)
                + check.reference_findings(self.plugin) + check.bare_path_findings(self.plugin)
                + check.size_findings(self.plugin))


class ConformingFixtureTests(Fixture):
    def test_conforming_fixture_has_no_findings(self):
        self.assertEqual(self.all_findings(), [])

    def test_cli_exit_zero_on_conforming_fixture(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.plugin)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_cli_exit_one_with_prefixed_findings(self):
        self.write('references/orphan.md', '# Orphan\n')
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.plugin)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('reference: references/orphan.md', result.stdout)

    def test_cli_exit_two_without_skills(self):
        empty = Path(self.temporary.name) / 'empty'
        empty.mkdir()
        result = subprocess.run([sys.executable, str(SCRIPT), str(empty)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)


class TemplateTests(Fixture):
    """Check 1: AC11 (20261110 AC1, AC2, AC5, AC6)."""

    def assertFinding(self, fragment):
        findings = check.template_findings(self.plugin)
        self.assertTrue(any(fragment in f for f in findings), findings)
        self.assertTrue(all('skills/alpha/SKILL.md' in f for f in findings), findings)

    def test_missing_name(self):
        self.edit('skills/alpha/SKILL.md', 'name: alpha\n', '')
        self.assertFinding('frontmatter name')

    def test_missing_description(self):
        self.edit('skills/alpha/SKILL.md', 'description: Do alpha', 'summary: Do alpha')
        self.assertFinding('frontmatter description')

    def test_description_without_action_text(self):
        self.edit('skills/alpha/SKILL.md', 'description: Do alpha work and record it. ', 'description: ')
        self.assertFinding('action')

    def test_description_without_use_when(self):
        self.edit('skills/alpha/SKILL.md', 'Use when alpha is needed. ', '')
        self.assertFinding('Use when')

    def test_description_without_not_for(self):
        self.edit('skills/alpha/SKILL.md', 'Not for beta work; use beta.', '')
        self.assertFinding('Not for')

    def test_not_for_before_use_when(self):
        self.edit('skills/alpha/SKILL.md',
                  'Use when alpha is needed. Not for beta work; use beta.',
                  'Not for beta work; use beta. Use when alpha is needed.')
        self.assertFinding('Use when')

    def test_not_for_without_skill(self):
        self.edit('skills/alpha/SKILL.md', 'Not for beta work; use beta.', 'Not for beta work.')
        self.assertFinding('names no skill')

    def test_not_for_names_missing_skill(self):
        self.edit('skills/alpha/SKILL.md', '; use beta.', '; use gamma.')
        self.assertFinding('gamma')

    def test_not_for_names_itself(self):
        self.edit('skills/alpha/SKILL.md', '; use beta.', '; use alpha.')
        self.assertFinding('names itself')

    def test_not_for_accepts_several_skills(self):
        self.write('skills/gamma/SKILL.md', skill_text('gamma', 'alpha'))
        self.edit('skills/alpha/SKILL.md', '; use beta.', '; use beta, or for gamma work use gamma.')
        self.assertEqual([f for f in check.template_findings(self.plugin) if 'alpha' in f], [])

    def test_missing_h1(self):
        self.edit('skills/alpha/SKILL.md', '# Alpha\n', '')
        self.assertFinding('H1')

    def test_text_between_h1_and_block(self):
        self.edit('skills/alpha/SKILL.md', '# Alpha\n', '# Alpha\n\nIntro.\n')
        self.assertFinding('every-task')

    def test_missing_every_task_region(self):
        text = self.read('skills/alpha/SKILL.md')
        start = text.index('<!-- lusona:begin every-task')
        end = text.index('<!-- lusona:end every-task -->\n') + len('<!-- lusona:end every-task -->\n')
        self.write('skills/alpha/SKILL.md', text[:start] + text[end:])
        self.assertFinding('every-task')

    def test_missing_persona_section(self):
        self.edit('skills/alpha/SKILL.md', '## Persona and judgment', '## Role')
        self.assertFinding('Persona and judgment')

    def test_missing_persona_field(self):
        for field, line in [('Persona', '**Persona**: alpha worker.\n'),
                            ('Responsibility', '- Responsibility: do alpha.\n'),
                            ('Decision criteria', '- Decision criteria: smallest change.\n'),
                            ('Evidence', '- **Evidence**: inspected files.\n'),
                            ('Failure modes', '- Failure modes: guessing.\n')]:
            with self.subTest(field=field):
                original = self.read('skills/alpha/SKILL.md')
                self.edit('skills/alpha/SKILL.md', line, '')
                self.assertFinding(f'field {field}')
                self.write('skills/alpha/SKILL.md', original)

    def test_field_outside_persona_section_does_not_count(self):
        self.edit('skills/alpha/SKILL.md', '- Failure modes: guessing.\n', '')
        self.edit('skills/alpha/SKILL.md', 'Check things.', 'Failure modes: guessing.')
        self.assertFinding('field Failure modes')

    def test_missing_establish_section(self):
        self.edit('skills/alpha/SKILL.md', '## Establish the input', '## Input')
        self.assertFinding('Establish')

    def test_practices_section_is_optional(self):
        self.edit('skills/alpha/SKILL.md', '## Alpha practices\n\nCheck things.\n\n', '')
        self.assertEqual(check.template_findings(self.plugin), [])

    def test_missing_record_section(self):
        self.edit('skills/alpha/SKILL.md', '## Work and record', '## Work')
        self.assertFinding('and record')

    def test_sections_out_of_order(self):
        text = self.read('skills/alpha/SKILL.md')
        practices = '## Alpha practices\n\nCheck things.\n\n'
        record = '## Work and record\n\nDo the work.\n\n'
        text = text.replace(practices + record, record + practices)
        self.write('skills/alpha/SKILL.md', text)
        self.assertFinding('order')

    def test_extra_section_is_a_finding(self):
        self.edit('skills/alpha/SKILL.md', '## Final reply', '## Notes\n\nX.\n\n## Final reply')
        self.assertFinding('Notes')

    def test_final_reply_not_last(self):
        with (self.plugin / 'skills/alpha/SKILL.md').open('a') as f:
            f.write('\n## Work and record\n\nAgain.\n')
        self.assertFinding('Final reply')

    def test_final_reply_without_region(self):
        text = self.read('skills/alpha/SKILL.md')
        start = text.index('<!-- lusona:begin final-reply')
        end = text.index('<!-- lusona:end final-reply -->\n') + len('<!-- lusona:end final-reply -->\n')
        self.write('skills/alpha/SKILL.md', text[:start] + text[end:])
        self.assertFinding('final-reply')

    def test_final_reply_without_next_actions(self):
        self.edit('skills/alpha/SKILL.md', 'Valid next actions: beta.\n', '')
        self.assertFinding('next actions')

    def test_headings_inside_regions_and_fences_are_ignored(self):
        self.edit('skills/alpha/SKILL.md', 'Every-task rules.', 'Every-task rules.\n\n## Inside region\n')
        self.edit('skills/alpha/SKILL.md', 'Do the work.', 'Do the work.\n\n```\n## Inside fence\n```')
        self.assertEqual(check.template_findings(self.plugin), [])


class ExtraSectionExceptionTests(Fixture):
    """A4 (user, 2026-11-11): batch and status may add H2 sections; order and last Final reply still apply."""

    EXTRA = '## Dispatch\n\nX.\n\n## Final reply'

    def add(self, name):
        self.write(f'skills/{name}/SKILL.md', skill_text(name, 'alpha'))
        self.edit(f'skills/{name}/SKILL.md', '## Final reply', self.EXTRA)

    def findings_for(self, name):
        return [f for f in check.template_findings(self.plugin) if f'skills/{name}/' in f]

    def test_extra_section_in_batch_passes(self):
        self.add('batch')
        self.assertEqual(self.findings_for('batch'), [])

    def test_extra_section_in_status_passes(self):
        self.add('status')
        self.assertEqual(self.findings_for('status'), [])

    def test_same_extra_section_in_other_skill_fails(self):
        self.add('gamma')
        self.assertTrue(any('unexpected section "## Dispatch"' in f for f in self.findings_for('gamma')))

    def test_extra_section_after_final_reply_in_status_fails(self):
        self.write('skills/status/SKILL.md', skill_text('status', 'alpha') + '\n## Dispatch\n\nX.\n')
        findings = self.findings_for('status')
        self.assertTrue(any('must be the last section' in f for f in findings), findings)
        self.assertFalse(any('unexpected section' in f for f in findings), findings)

    def test_required_section_still_required_in_batch(self):
        self.add('batch')
        self.edit('skills/batch/SKILL.md', '## Work and record', '## Work')
        self.assertTrue(any('and record' in f for f in self.findings_for('batch')))


class ReadmeTests(Fixture):
    """Check 2: AC10 README independence."""

    def test_skill_link_to_plugin_readme(self):
        self.edit('skills/alpha/SKILL.md', 'Read the request.', 'Read the [core](../../README.md#rules).')
        findings = check.readme_findings(self.plugin)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn('skills/alpha/SKILL.md:', findings[0])

    def test_reference_link_to_plugin_readme(self):
        self.write('references/shared.md', '# Shared\n\nSee [README](../README.md).\n')
        self.assertEqual(len(check.readme_findings(self.plugin)), 1)

    def test_per_skill_reference_link_resolving_to_plugin_readme(self):
        self.write('skills/alpha/references/own.md', '# Own\n\nSee [README](../../../README.md).\n')
        self.assertEqual(len(check.readme_findings(self.plugin)), 1)

    def test_named_readme_paths(self):
        for text in ('Read `plugins/lusona/README.md` first.', 'Read ../../README.md first.',
                     'Read `../README.md` first.'):
            with self.subTest(text=text):
                self.write('references/shared.md', f'# Shared\n\n{text}\n')
                self.assertEqual(len(check.readme_findings(self.plugin)), 1, text)

    def test_project_readme_link_is_allowed(self):
        self.edit('skills/alpha/SKILL.md', 'Read the request.',
                  'Read the project [README](docs/lusona/README.md) and `docs/lusona/README.md`.')
        self.assertEqual(check.readme_findings(self.plugin), [])


class ReferenceTests(Fixture):
    """Check 3: AC14 and ADR P-a."""

    def test_unlinked_plugin_reference_reported_once(self):
        self.write('references/orphan.md', '# Orphan\n')
        findings = check.reference_findings(self.plugin)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn('references/orphan.md', findings[0])
        self.assertIn('not linked', findings[0])

    def test_unlinked_per_skill_reference(self):
        self.write('skills/beta/references/orphan.md', '# Orphan\n')
        findings = check.reference_findings(self.plugin)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn('skills/beta/references/orphan.md', findings[0])

    def test_plugin_reference_linked_by_one_skill(self):
        self.write('references/single.md', '# Single\n')
        self.edit('skills/alpha/SKILL.md', 'Read the request.', 'Before X, read [single](../../references/single.md).')
        findings = check.reference_findings(self.plugin)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn('references/single.md', findings[0])
        self.assertIn('1 SKILL.md', findings[0])

    def test_per_skill_reference_linked_by_other_skill(self):
        self.edit('skills/beta/SKILL.md', 'Read the request.',
                  'Before X, read [own](../alpha/references/own.md).')
        findings = check.reference_findings(self.plugin)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn('skills/alpha/references/own.md', findings[0])
        self.assertIn('skills/beta/SKILL.md', findings[0])

    def test_reference_linking_reference(self):
        self.write('references/shared.md', '# Shared\n\nSee [own](../skills/alpha/references/own.md).\n')
        findings = check.reference_findings(self.plugin)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn('links reference', findings[0])

    def test_link_without_trigger_is_a_finding(self):
        # N3, reviewer fixture tmp/w13b/f4: "Related: [visuals](...)" in every linking skill.
        self.write('references/single.md', '# Single\n')
        for name in ('alpha', 'beta'):
            self.edit(f'skills/{name}/SKILL.md', 'Read the request.',
                      'Read the request.\n\n- Related: [single](../../references/single.md).')
        findings = check.reference_findings(self.plugin)
        self.assertEqual(findings, [f'reference: references/single.md: skills/{name}/SKILL.md links it in no '
                                    f'trigger sentence (Before, After, When, If, At, As ...; AC14)'
                                    for name in ('alpha', 'beta')])

    def test_trigger_in_another_sentence_does_not_count(self):
        self.write('references/single.md', '# Single\n')
        for name in ('alpha', 'beta'):
            self.edit(f'skills/{name}/SKILL.md', 'Read the request.',
                      'Before work, read the request. See [single](../../references/single.md).')
        findings = check.reference_findings(self.plugin)
        self.assertEqual(len(findings), 2, findings)
        self.assertTrue(all('links it in no trigger sentence' in f for f in findings), findings)

    def test_each_linking_skill_needs_a_trigger_sentence(self):
        self.write('references/single.md', '# Single\n')
        self.edit('skills/alpha/SKILL.md', 'Read the request.',
                  'Read [single](../../references/single.md) before merging.')
        self.edit('skills/beta/SKILL.md', 'Read the request.', 'Related: [single](../../references/single.md).')
        findings = check.reference_findings(self.plugin)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn('references/single.md: skills/beta/SKILL.md links it in no trigger sentence', findings[0])

    def test_one_trigger_sentence_per_skill_is_enough(self):
        self.write('references/single.md', '# Single\n')
        for name in ('alpha', 'beta'):
            self.edit(f'skills/{name}/SKILL.md', 'Read the request.',
                      'Before merging, read [single](../../references/single.md). '
                      'Related: [single](../../references/single.md).')
        self.assertEqual(check.reference_findings(self.plugin), [])

    def test_trigger_forms(self):
        self.write('references/single.md', '# Single\n')
        self.edit('skills/beta/SKILL.md', 'Read the request.', 'Before X, read [single](../../references/single.md).')
        for sentence in ('Before merging, read [single](../../references/single.md).',
                         'After each result, read [single](../../references/single.md).',
                         'When a test fails, read [single](../../references/single.md).',
                         'While waiting, read [single](../../references/single.md).',
                         'Until approved, follow [single](../../references/single.md).',
                         'If a test fails, read [single](../../references/single.md).',
                         'At 40% context use, read [single](../../references/single.md).',
                         'As a leaf, return the fields from [single](../../references/single.md).',
                         '**Saving.** If saving fails, read [single](../../references/single.md).',
                         'Read [single](../../references/single.md) when a test fails.',
                         '| Merge | Before merging, read [single](../../references/single.md) |'):
            with self.subTest(sentence=sentence):
                self.write('skills/alpha/SKILL.md', skill_text('alpha', 'beta',
                           ' Before X, read [own](references/own.md).\n\n' + sentence))
                self.assertEqual(check.reference_findings(self.plugin), [])

    def test_clause_start_words_elsewhere_are_not_triggers(self):
        self.write('references/single.md', '# Single\n')
        self.edit('skills/beta/SKILL.md', 'Read the request.', 'Before X, read [single](../../references/single.md).')
        for sentence in ('Look at [single](../../references/single.md).',
                         'Use it as written in [single](../../references/single.md).',
                         'Read [single](../../references/before.md) and [single](../../references/single.md).'):
            with self.subTest(sentence=sentence):
                self.write('skills/alpha/SKILL.md', skill_text('alpha', 'beta',
                           ' Before X, read [own](references/own.md).\n\n' + sentence))
                findings = [f for f in check.reference_findings(self.plugin) if 'trigger' in f]
                self.assertEqual(len(findings), 1, findings)

    def test_per_skill_reference_needs_trigger(self):
        self.edit('skills/alpha/SKILL.md', ' Before X, read [own](references/own.md).', ' See [own](references/own.md).')
        findings = check.reference_findings(self.plugin)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn('skills/alpha/references/own.md: skills/alpha/SKILL.md links it in no trigger sentence', findings[0])

    def test_reference_anchor_to_itself_is_allowed(self):
        self.write('references/shared.md', '# Shared\n\nSee [above](#shared) and [self](shared.md#shared).\n')
        self.assertEqual(check.reference_findings(self.plugin), [])

    def test_link_with_title_and_anchor_counts(self):
        self.write('references/single.md', '# Single\n')
        self.edit('skills/alpha/SKILL.md', 'Read the request.',
                  'Before X, read [single](../../references/single.md#part "Title").')
        self.edit('skills/beta/SKILL.md', 'Read the request.', 'Before X, read [single](../../references/single.md).')
        self.assertEqual(check.reference_findings(self.plugin), [])


class BarePathTests(Fixture):
    """Check 4: bare reference paths that do not resolve from the file."""

    def test_backticked_plugin_level_bare_path(self):
        self.edit('skills/alpha/SKILL.md', 'Read the request.', 'Read `references/shared.md`.')
        findings = check.bare_path_findings(self.plugin)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn('skills/alpha/SKILL.md:', findings[0])
        self.assertIn('references/shared.md', findings[0])

    def test_plain_text_bare_path_in_reference(self):
        self.write('references/shared.md', '# Shared\n\nThen read references/other.md.\n')
        self.assertEqual(len(check.bare_path_findings(self.plugin)), 1)

    def test_bare_path_inside_region(self):
        self.edit('skills/alpha/SKILL.md', 'Every-task rules.', 'Every-task rules: references/shared.md.')
        self.assertEqual(len(check.bare_path_findings(self.plugin)), 1)

    def test_resolving_per_skill_bare_path_is_allowed(self):
        self.edit('skills/alpha/SKILL.md', 'Read the request.', 'Read `references/own.md`.')
        self.assertEqual(check.bare_path_findings(self.plugin), [])

    def test_resolving_plugin_level_bare_path_is_a_finding(self):
        # N2, reviewer fixture tmp/w13b/f3: the path resolves but names a plugin-level file.
        for text in ('Read `../../references/shared.md`.', 'Read ../../references/shared.md first.'):
            with self.subTest(text=text):
                self.write('skills/beta/SKILL.md', skill_text('beta', 'alpha'))
                self.edit('skills/beta/SKILL.md', 'Read the request.', text)
                findings = check.bare_path_findings(self.plugin)
                self.assertEqual(len(findings), 1, findings)
                self.assertIn('skills/beta/SKILL.md:', findings[0])
                self.assertIn('../../references/shared.md', findings[0])
                self.assertIn('plugin-level', findings[0])

    def test_unresolved_plugin_level_bare_path_in_skill_without_own_copy(self):
        # Reviewer fixture tmp/w13b/f3b: `references/x.md` where the skill folder has no such file.
        self.edit('skills/beta/SKILL.md', 'Read the request.', 'Read `references/shared.md`.')
        findings = check.bare_path_findings(self.plugin)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn('does not resolve', findings[0])

    def test_bare_path_from_reference_to_sibling_skill_folder_is_a_finding(self):
        self.write('skills/alpha/references/own.md', '# Own\n\nSee ../../beta/references/x.md.\n')
        self.write('skills/beta/references/x.md', '# X\n')
        self.assertEqual(len(check.bare_path_findings(self.plugin)), 1)

    def test_link_target_is_exempt(self):
        self.edit('skills/beta/SKILL.md', 'Read the request.', 'Read [x](references/missing.md).')
        self.assertEqual(check.bare_path_findings(self.plugin), [])

    def test_link_text_is_exempt(self):
        self.edit('skills/beta/SKILL.md', 'Read the request.',
                  'Read [`references/shared.md`](../../references/shared.md).')
        self.assertEqual(check.bare_path_findings(self.plugin), [])

    def test_repository_prefixed_path_is_a_finding(self):
        self.edit('skills/beta/SKILL.md', 'Read the request.', 'Read `plugins/lusona/references/shared.md`.')
        self.assertEqual(len(check.bare_path_findings(self.plugin)), 1)


class SizeTests(Fixture):
    """Check 5: S4 line ceilings."""

    def pad(self, relative, lines):
        text = self.read(relative)
        self.write(relative, text + 'x\n' * (lines - len(text.splitlines())))

    def test_boundaries(self):
        for relative, limit in [('skills/alpha/SKILL.md', 500), ('references/shared.md', 200),
                                ('skills/alpha/references/own.md', 200),
                                ('templates/spec.md.template', 100), ('templates/plain.md', 100)]:
            with self.subTest(path=relative):
                if not (self.plugin / relative).exists():
                    self.write(relative, '# T\n')
                self.pad(relative, limit)
                self.assertEqual(check.size_findings(self.plugin), [])
                self.pad(relative, limit + 1)
                findings = check.size_findings(self.plugin)
                self.assertEqual(len(findings), 1, findings)
                self.assertIn(relative, findings[0])
                self.assertIn(f'{limit + 1} lines', findings[0])
                self.pad(relative, limit)
                self.write(relative, '\n'.join(self.read(relative).splitlines()[:limit]) + '\n')


if __name__ == '__main__':
    unittest.main()
