#!/usr/bin/env python3
"""Tests for scripts/check_contract.py: each check fails on a deliberate fixture break."""
import importlib.util
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/lusona'
spec = importlib.util.spec_from_file_location('check_contract', ROOT / 'scripts/check_contract.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

CATALOGS = ('.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json',
            '.cursor-plugin/marketplace.json')


SHARED_EVERY = ('Specs, plans, ADRs and queue states do not authorize implementation. '
                'Select `none`, `targeted` or `strict`.')
SHARED_FINAL = 'Status: Complete, In progress, Needs input or Paused.'
NO_LEVELS = 'K4: shared every-task and final-reply regions do not name every TDD level: none, targeted, strict'
NO_STATUSES = ('K4: shared every-task and final-reply regions do not name every reply status: '
               'Complete, In progress, Needs input, Paused')
NO_AUTHORITY = ('K4: shared every-task and final-reply regions have no sentence stating that specs, '
                'plans, ADRs and queue states do not authorize implementation')


def baseline(path):
    return subprocess.run(['git', 'show', f'34186da:{path}'], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout


class ContractTests(unittest.TestCase):
    def setUp(self):
        (ROOT / 'tmp').mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='contract-test-', dir=ROOT / 'tmp')
        self.root = Path(self.temporary.name)
        self.copy = self.root / 'plugins/lusona'
        shutil.copytree(PLUGIN, self.copy)
        for catalog in CATALOGS:
            (self.root / catalog).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / catalog, self.root / catalog)

    def tearDown(self):
        self.temporary.cleanup()

    def add_regions(self, every=SHARED_EVERY, final=SHARED_FINAL, skill='implement'):
        """Replace the copy's generated regions in every skill with one pair in `skill`."""
        for path in self.copy.glob('skills/*/SKILL.md'):
            path.write_text(re.sub(r'(?ms)^<!-- lusona:begin ([a-z-]+) -->\n.*?^<!-- lusona:end \1 -->\n',
                                   '', path.read_text()))
        with (self.copy / f'skills/{skill}/SKILL.md').open('a') as f:
            f.write(f'\n<!-- lusona:begin every-task -->\n{every}\n<!-- lusona:end every-task -->\n\n'
                    f'<!-- lusona:begin final-reply -->\n{final}\n<!-- lusona:end final-reply -->\n')

    def replace(self, relative, old, new, count=0):
        path = self.copy / relative
        text = path.read_text()
        self.assertRegex(text, old, f'fixture precondition: {old!r} in {relative}')
        path.write_text(re.sub(old, new, text, count=count))

    # Real repository
    def test_real_plugin_satisfies_k1_k2_k3_k5(self):
        findings = (check.skill_findings(PLUGIN) + check.layout_findings(PLUGIN)
                    + check.helper_findings(PLUGIN) + check.work_record_test_findings(ROOT)
                    + check.manifest_findings(PLUGIN, ROOT))
        self.assertEqual(findings, [], '\n'.join(findings))

    def test_unbroken_fixture_has_no_k1_k2_k3_k5_findings(self):
        findings = (check.skill_findings(self.copy) + check.layout_findings(self.copy)
                    + check.helper_findings(self.copy) + check.manifest_findings(self.copy, self.root))
        self.assertEqual(findings, [], '\n'.join(findings))

    # AC4 (K1)
    def test_ac4_rejects_missing_skill(self):
        shutil.rmtree(self.copy / 'skills/measure')
        self.assertIn('K1: skill directory missing: skills/measure', check.skill_findings(self.copy))

    def test_ac4_rejects_renamed_skill(self):
        (self.copy / 'skills/review').rename(self.copy / 'skills/audit')
        self.assertIn('K1: skill directory missing: skills/review', check.skill_findings(self.copy))

    def test_ac4_rejects_frontmatter_name_mismatch(self):
        self.replace('skills/specify/SKILL.md', r'(?m)^name: specify$', 'name: define')
        self.assertIn("K1: skills/specify/SKILL.md frontmatter name is 'define', expected 'specify'",
                      check.skill_findings(self.copy))

    def test_ac4_accepts_quoted_frontmatter_name(self):
        for quoted in ('"specify"', "'specify'"):
            with self.subTest(name=quoted):
                path = self.copy / 'skills/specify/SKILL.md'
                path.write_text(re.sub(r'(?m)^name: .*$', f'name: {quoted}', path.read_text(), count=1))
                self.assertEqual(check.skill_findings(self.copy), [])

    def test_ac4_rejects_quoted_mismatched_name(self):
        self.replace('skills/specify/SKILL.md', r'(?m)^name: specify$', 'name: "define"')
        self.assertIn("K1: skills/specify/SKILL.md frontmatter name is 'define', expected 'specify'",
                      check.skill_findings(self.copy))

    def test_ac4_allows_additional_skill(self):
        extra = self.copy / 'skills/extra'
        extra.mkdir()
        (extra / 'SKILL.md').write_text('---\nname: extra\ndescription: x\n---\n')
        self.assertEqual(check.skill_findings(self.copy), [])

    # AC5 (K2)
    def test_ac5_rejects_missing_path(self):
        for path in self.copy.rglob('*.md'):
            path.write_text(path.read_text().replace('docs/lusona/batches/', 'docs/lusona/runs/'))
        self.assertIn('K2: path docs/lusona/batches/ absent from references/files.md',
                      check.layout_findings(self.copy))

    def test_ac5_path_removed_from_defining_reference_fails(self):
        # Reviewer fixture tmp/w13b/f8: the path stays named in other files.
        self.replace('references/files.md', r'docs/lusona/visuals/', 'docs/lusona/VISUALS-REMOVED/')
        corpus = '\n'.join(p.read_text() for p in self.copy.rglob('*.md'))
        self.assertIn('docs/lusona/visuals/', corpus, 'fixture precondition: path named elsewhere')
        self.assertEqual(check.layout_findings(self.copy),
                         ['K2: path docs/lusona/visuals/ absent from references/files.md'])

    def test_ac5_rejects_missing_defining_reference(self):
        (self.copy / 'references/files.md').unlink()
        findings = check.layout_findings(self.copy)
        self.assertIn('K2: defining reference missing: references/files.md', findings)

    def test_ac5_path_only_in_template_or_readme_does_not_count(self):
        for path in self.copy.rglob('*.md'):
            path.write_text(path.read_text().replace('docs/lusona/product.md', 'docs/lusona/brief.md'))
        (self.copy / 'templates/work.md').write_text('docs/lusona/product.md\n')
        (self.copy / 'README.md').write_text('docs/lusona/product.md\n')
        self.assertIn('K2: path docs/lusona/product.md absent from references/files.md',
                      check.layout_findings(self.copy))

    def test_ac5_rejects_missing_id_form(self):
        for path in self.copy.rglob('*.md'):
            path.write_text(path.read_text().replace('YYYYMMDD', 'YYYY-MM-DD'))
        self.assertIn('K2: record ID form YYYYMMDD-slug absent from references/naming.md',
                      check.layout_findings(self.copy))

    def test_ac5_id_form_removed_from_defining_reference_fails(self):
        path = self.copy / 'references/naming.md'
        path.write_text(path.read_text().replace('YYYYMMDD', 'YYYY-MM-DD'))
        (self.copy / 'references/extra.md').write_text('Use YYYYMMDD-slug.\n')
        self.assertEqual(check.layout_findings(self.copy),
                         ['K2: record ID form YYYYMMDD-slug absent from references/naming.md'])

    def test_ac5_rejects_missing_queue_state(self):
        self.replace('references/queue.md', r'\bReview\b', 'Verify')
        self.assertIn('K2: references/queue.md does not name every queue state: '
                      'Ideas, Ready, Doing, Review, Done, Icebox', check.layout_findings(self.copy))

    def test_ac5_queue_state_named_only_outside_defining_reference_fails(self):
        self.replace('references/queue.md', r'\bIcebox\b', 'Freezer')
        (self.copy / 'references/extra.md').write_text('Ideas, Ready, Doing, Review, Done, Icebox.\n')
        self.assertEqual(check.layout_findings(self.copy),
                         ['K2: references/queue.md does not name every queue state: '
                          'Ideas, Ready, Doing, Review, Done, Icebox'])

    def k2_extra_findings(self, relative, old, new):
        path = self.copy / relative
        text = path.read_text()
        self.assertIn(old, text, f'fixture precondition: {old!r} in {relative}')
        path.write_text(text.replace(old, new))
        return check.layout_findings(self.copy)

    def test_ac5_path_only_in_html_comment_fails(self):
        # Reviewer fixture tmp/w13v/b2a.
        findings = self.k2_extra_findings('references/files.md', 'docs/lusona/adr/', 'docs/lusona/decisions/')
        self.assertIn('K2: path docs/lusona/adr/ absent from references/files.md', findings)
        with (self.copy / 'references/files.md').open('a') as f:
            f.write('\n<!-- docs/lusona/adr/ removed -->\n')
        self.assertIn('K2: path docs/lusona/adr/ absent from references/files.md',
                      check.layout_findings(self.copy))

    def test_ac5_path_only_in_fenced_code_fails(self):
        # Reviewer fixture tmp/w13v/b2b.
        self.k2_extra_findings('references/files.md', 'docs/lusona/evidence/', 'docs/lusona/proof/')
        with (self.copy / 'references/files.md').open('a') as f:
            f.write('\n```text\ndocs/lusona/evidence/\n```\n')
        self.assertIn('K2: path docs/lusona/evidence/ absent from references/files.md',
                      check.layout_findings(self.copy))

    def test_ac5_path_only_in_negated_sentence_fails(self):
        # Reviewer fixture tmp/w13v/b2c.
        self.k2_extra_findings('references/files.md', 'docs/lusona/plans/', 'docs/lusona/steps/')
        with (self.copy / 'references/files.md').open('a') as f:
            f.write('\nDo not use docs/lusona/plans/; it is removed.\n')
        self.assertIn('K2: path docs/lusona/plans/ absent from references/files.md',
                      check.layout_findings(self.copy))

    def test_ac5_path_in_affirmative_prose_counts(self):
        self.k2_extra_findings('references/files.md', 'docs/lusona/plans/', 'docs/lusona/steps/')
        with (self.copy / 'references/files.md').open('a') as f:
            f.write('\nExisting execution records stay in docs/lusona/plans/.\n')
        self.assertEqual(check.layout_findings(self.copy), [])

    def test_ac5_id_form_only_in_html_comment_fails(self):
        path = self.copy / 'references/naming.md'
        path.write_text(path.read_text().replace('YYYYMMDD', 'YYYY-MM-DD') + '\n<!-- YYYYMMDD-slug -->\n')
        self.assertEqual(check.layout_findings(self.copy),
                         ['K2: record ID form YYYYMMDD-slug absent from references/naming.md'])

    def test_ac5_queue_state_named_in_prose_counts(self):
        # Reviewer fixture tmp/w13v/b2q: baseline 34186da names Icebox only in prose, so prose counts.
        path = self.copy / 'references/queue.md'
        text = path.read_text()
        path.write_text(re.sub(r'(?m)^\|\s*Icebox\s*\|.*\n', '', text))
        self.assertRegex(path.read_text(), r'\bIcebox\b', 'fixture precondition: prose names Icebox')
        self.assertEqual(check.layout_findings(self.copy), [])

    def test_ac5_queue_state_only_in_html_comment_fails(self):
        path = self.copy / 'references/queue.md'
        path.write_text(re.sub(r'\bIcebox\b', 'Freezer', path.read_text()) + '\n<!-- Icebox -->\n')
        self.assertEqual(check.layout_findings(self.copy),
                         ['K2: references/queue.md does not name every queue state: '
                          'Ideas, Ready, Doing, Review, Done, Icebox'])

    # AC6 (K3)
    def test_ac6_rejects_missing_helper(self):
        (self.copy / 'scripts/work-record.ps1').unlink()
        self.assertIn('K3: helper missing: scripts/work-record.ps1', check.helper_findings(self.copy))

    def test_ac6_rejects_missing_command(self):
        self.replace('scripts/work-record.sh', r'next-adr\|next-change\)', 'next-change)')
        self.assertIn('K3: scripts/work-record.sh does not name command next-adr',
                      check.helper_findings(self.copy))

    def test_ac6_command_match_is_hyphen_aware(self):
        path = self.copy / 'scripts/work-record.sh'
        path.write_text(path.read_text().replace('init-adr', 'init-adrs'))
        self.assertIn('K3: scripts/work-record.sh does not name command init-adr',
                      check.helper_findings(self.copy))

    def test_ac6_rejects_missing_conflict_status(self):
        path = self.copy / 'scripts/work-record.ps1'
        path.write_text(re.sub(r'(?<![\w-])conflict(?![\w-])', 'clash', path.read_text()))
        self.assertIn('K3: scripts/work-record.ps1 does not name conflict', check.helper_findings(self.copy))

    def test_ac6_rejects_removed_assertion(self):
        text = baseline('scripts/test-work-record.sh')
        line = "reject slug '!!!'\n"
        self.assertIn(line, text)
        findings = check.assertion_findings(text, text.replace(line, '', 1), 'scripts/test-work-record.sh')
        self.assertEqual(findings, ["K3: scripts/test-work-record.sh lost baseline line: reject slug '!!!'"])

    def test_ac6_rejects_weakened_case_list(self):
        text = baseline('scripts/test-work-record.ps1')
        weakened = re.sub(r"'01:01', '07:01', ", '', text, count=1)
        self.assertNotEqual(weakened, text)
        self.assertEqual(len(check.assertion_findings(text, weakened, 'scripts/test-work-record.ps1')), 1)

    def test_ac6_accepts_template_rename_lines(self):
        # Decision 22: the 13 helper-test lines changed by the `.template` rename are allowed.
        for relative in ('scripts/test-work-record.sh', 'scripts/test-work-record.ps1'):
            with self.subTest(file=relative):
                text = baseline(relative)
                renamed = re.sub(r'(templates/[\w$]+\.md)\b', r'\1.template', text)
                self.assertNotEqual(renamed, text)
                self.assertEqual(check.assertion_findings(text, renamed, relative), [])

    def test_ac6_rejects_other_change_on_a_renamed_template_line(self):
        text = 'cp "$repository/plugins/lusona/templates/spec.md" "$bundle/templates/spec.md"\n'
        for changed in ('cp "$repository/plugins/lusona/templates/spec.md.template" "$bundle/templates/x.md"\n',
                        'cp "$repository/plugins/lusona/templates/spec.md.template"\n',
                        'cp "$repository/plugins/lusona/templates/spec.md" "$bundle/templates/spec.md.template.template"\n'):
            with self.subTest(changed=changed):
                findings = check.assertion_findings(text, changed, 'x')
                self.assertEqual(len(findings), 1, findings)
                self.assertIn('lost baseline line', findings[0])

    def test_ac6_rejects_duplicate_assertion_removed_once(self):
        text = 'equal a b\nequal a b\n'
        self.assertEqual(len(check.assertion_findings(text, 'equal a b\n', 'x')), 1)

    def test_ac6_rejects_added_early_exit(self):
        # Reviewer fixture tmp/w13b/f7: `exit 0` inserted after the shell header.
        for relative, after in (('scripts/test-work-record.sh', 'set -euo pipefail\n'),
                                ('scripts/test-work-record.ps1', None)):
            with self.subTest(file=relative):
                text = baseline(relative)
                lines = text.splitlines(keepends=True)
                index = lines.index(after) + 1 if after else 1
                broken = ''.join(lines[:index] + ['exit 0\n'] + lines[index:])
                self.assertEqual(check.assertion_findings(text, broken, relative),
                                 [f'K3: {relative} adds an exit or return line: exit 0'])

    def test_ac6_rejects_added_exit_variants(self):
        text = baseline('scripts/test-work-record.sh')
        for line in ('return 0', 'true && exit', '[Environment]::Exit(0)', 'exit $status  # done'):
            with self.subTest(line=line):
                findings = check.assertion_findings(text, line + '\n' + text, 'x')
                self.assertEqual(len(findings), 1, findings)
                self.assertIn('adds an exit or return line', findings[0])

    def test_ac6_unchanged_test_files_have_no_exit_findings(self):
        for relative in ('scripts/test-work-record.sh', 'scripts/test-work-record.ps1'):
            text = baseline(relative)
            self.assertEqual(check.assertion_findings(text, text, relative), [])

    def test_ac6_ignores_comments_blank_lines_and_indentation(self):
        self.assertEqual(check.assertion_findings('# note\n\n  equal a b\n', 'equal a b\nequal c d\n', 'x'), [])

    def test_ac6_reports_unreadable_baseline(self):
        def fail(path):
            raise OSError('no git')
        findings = check.work_record_test_findings(ROOT, fail)
        self.assertEqual(len(findings), 2)
        self.assertTrue(all('cannot read baseline' in f for f in findings), findings)

    # AC7 (K4)
    def test_ac5_ac7_reject_empty_scope(self):
        for path in self.copy.rglob('*.md'):
            if path.relative_to(self.copy).parts[0] != 'templates' and path != self.copy / 'README.md':
                path.unlink()
        self.assertIn('K2: defining reference missing: references/files.md', check.layout_findings(self.copy))
        self.assertEqual(check.vocabulary_findings(self.copy), [NO_LEVELS, NO_STATUSES, NO_AUTHORITY])

    def test_ac7_accepts_vocabulary_in_shared_regions(self):
        self.add_regions()
        self.assertEqual(check.vocabulary_findings(self.copy), [])

    def test_ac7_accepts_singular_does_not_authorize(self):
        self.add_regions(every='A spec, plan, ADR or queue state does not authorize implementation. '
                               '`none`, `targeted`, `strict`.')
        self.assertEqual(check.vocabulary_findings(self.copy), [])

    def test_ac7_vocabulary_outside_regions_does_not_count(self):
        with (self.copy / 'skills/implement/SKILL.md').open('a') as f:
            f.write(f'\n{SHARED_EVERY}\n\n{SHARED_FINAL}\n')
        self.add_regions(every='Ask first.', final='Reply.')
        self.assertEqual(check.vocabulary_findings(self.copy), [NO_LEVELS, NO_STATUSES, NO_AUTHORITY])

    def test_ac7_statuses_only_in_reference_do_not_count(self):
        # N11: statuses only in references/completion.md do not satisfy AC7.
        (self.copy / 'references/completion.md').write_text(SHARED_FINAL + '\n')
        self.add_regions(final='Status: see the completion examples.')
        self.assertEqual(check.vocabulary_findings(self.copy), [NO_STATUSES])

    def test_ac7_status_only_in_template_or_readme_does_not_count(self):
        self.add_regions(final='Reply.')
        (self.copy / 'templates/status.md.template').write_text(SHARED_FINAL + '\n')
        (self.copy / 'README.md').write_text(SHARED_FINAL + '\n')
        self.assertEqual(check.vocabulary_findings(self.copy), [NO_STATUSES])

    def test_ac7_vocabulary_split_across_the_two_regions(self):
        self.add_regions(every=SHARED_FINAL, final=SHARED_EVERY)
        self.assertEqual(check.vocabulary_findings(self.copy), [])

    def test_ac7_rejects_missing_tdd_level(self):
        self.add_regions(every=SHARED_EVERY.replace('`strict`', '`full`'))
        self.assertEqual(check.vocabulary_findings(self.copy), [NO_LEVELS])

    def test_ac7_rejects_missing_status(self):
        self.add_regions(final='Status: Complete, In progress or Needs input.')
        self.assertEqual(check.vocabulary_findings(self.copy), [NO_STATUSES])

    def test_ac7_rejects_affirmative_authority_rule(self):
        # B1, reviewer fixture tmp/w13b/f1.
        self.add_regions(every='Specs, plans, ADRs and queue states authorize implementation. '
                               '`none`, `targeted`, `strict`.')
        findings = check.vocabulary_findings(self.copy)
        self.assertIn(NO_AUTHORITY, findings)
        self.assertIn('K4: skills/implement/SKILL.md:', '\n'.join(findings))

    def test_ac7_rejects_negation_not_on_authorize(self):
        self.add_regions(every='Do not skip this: specs, plans, ADRs and queue states authorize '
                               'implementation. `none`, `targeted`, `strict`.')
        self.assertIn(NO_AUTHORITY, check.vocabulary_findings(self.copy))

    def test_ac7_reports_affirmative_authority_sentence_anywhere(self):
        self.add_regions()
        (self.copy / 'references/extra.md').write_text(
            '# Extra\n\nQueue states, specs, plans and ADRs authorize implementation.\n')
        self.assertEqual(check.vocabulary_findings(self.copy),
                         ['K4: references/extra.md:3: sentence states that specs, plans, ADRs and queue '
                          'states authorize implementation'])

    def test_ac7_negated_sentence_is_not_reported_as_affirmative(self):
        self.add_regions()
        (self.copy / 'references/extra.md').write_text(
            'Specs, plans, ADRs and queue states never authorize implementation.\n'
            'Specs, plans, ADRs and queue states cannot authorize implementation.\n')
        self.assertEqual(check.vocabulary_findings(self.copy), [])

    def test_ac7_authority_terms_must_be_words(self):
        self.add_regions(every='Respect specific planning; ADR queue implementation authority does not '
                               'authorize. `none`, `targeted`, `strict`.')
        self.assertIn(NO_AUTHORITY, check.vocabulary_findings(self.copy))

    def test_ac7_authority_terms_in_table_row_do_not_count(self):
        self.add_regions(every='| Spec | Plan |\n| --- | --- |\n| ADR | queue states do not authorize '
                               'implementation |\n\n`none`, `targeted`, `strict`.')
        self.assertIn(NO_AUTHORITY, check.vocabulary_findings(self.copy))

    def test_ac7_rejects_missing_authority_rule(self):
        self.add_regions(every='Specs and plans do not authorize implementation. ADRs record decisions. '
                               '`none`, `targeted`, `strict`.')
        self.assertEqual(check.vocabulary_findings(self.copy), [NO_AUTHORITY])

    def extra_authority_findings(self, text):
        self.add_regions()
        (self.copy / 'references/extra.md').write_text(text)
        return check.vocabulary_findings(self.copy)

    def test_ac7_negation_with_other_subject_does_not_count(self):
        # Reviewer fixture tmp/w13v/b1g.
        self.add_regions(every='Users do not authorize implementation lightly; specs, plans, ADRs and '
                               'queue states do. `none`, `targeted`, `strict`.')
        findings = check.vocabulary_findings(self.copy)
        self.assertIn(NO_AUTHORITY, findings)
        self.assertTrue(any(f.startswith('K4: skills/implement/SKILL.md:') for f in findings), findings)

    def test_ac7_affirmative_beside_unrelated_negation_is_reported(self):
        # Reviewer fixture tmp/w13v/b1h.
        self.add_regions(every=SHARED_EVERY + ' Specs, plans, ADRs and queue states authorize '
                                              'implementation when no question remains.')
        findings = check.vocabulary_findings(self.copy)
        self.assertNotIn(NO_AUTHORITY, findings)
        self.assertEqual(len(findings), 1, findings)
        self.assertRegex(findings[0], r'^K4: skills/implement/SKILL\.md:\d+: sentence states')

    def test_ac7_affirmative_with_any_object_is_reported(self):
        # Reviewer fixture tmp/w13v/b1c.
        self.assertEqual(self.extra_authority_findings(
            '# Extra\n\nSpecs, plans, ADRs and queue states authorize code changes.\n'),
            ['K4: references/extra.md:3: sentence states that specs, plans, ADRs and queue '
             'states authorize implementation'])

    def test_ac7_affirmative_split_across_list_items_is_reported(self):
        # Reviewer fixture tmp/w13v/b1d.
        self.assertEqual(self.extra_authority_findings(
            '# Extra\n\nThese authorize implementation:\n\n- specs\n- plans\n- ADRs\n- queue states\n'),
            ['K4: references/extra.md:3: sentence states that specs, plans, ADRs and queue '
             'states authorize implementation'])

    def test_ac7_affirmative_after_leading_negated_clause_is_reported(self):
        self.assertEqual(len(self.extra_authority_findings(
            'When no question remains, specs, plans, ADRs and queue states authorize implementation.\n')), 1)

    def test_ac7_negated_forms_are_not_reported(self):
        self.assertEqual(self.extra_authority_findings(
            'No spec, plan, ADR or queue state authorizes implementation.\n\n'
            'Specs, plans, ADRs and queue states do not by themselves authorize implementation.\n\n'
            'Neither specs, plans, ADRs nor queue states authorize code changes.\n\n'
            'Implementation is not authorized by specs, plans, ADRs or queue states.\n\n'
            'These do not authorize implementation:\n\n- specs\n- plans\n- ADRs\n- queue states\n'), [])

    # AC8 (K5)
    def test_ac8_rejects_renamed_manifest(self):
        path = self.copy / '.codex-plugin/plugin.json'
        data = json.loads(path.read_text())
        data['name'] = 'lusona-skills'
        path.write_text(json.dumps(data))
        self.assertIn("K5: .codex-plugin/plugin.json names 'lusona-skills', expected 'lusona'",
                      check.manifest_findings(self.copy, self.root))

    def test_ac8_rejects_missing_native_manifest(self):
        shutil.rmtree(self.copy / '.claude-plugin')
        self.assertIn('K5: native manifest missing: .claude-plugin/plugin.json',
                      check.manifest_findings(self.copy, self.root))

    def test_ac8_rejects_renamed_catalog_entry(self):
        path = self.root / '.claude-plugin/marketplace.json'
        data = json.loads(path.read_text())
        data['plugins'][0]['name'] = 'other'
        path.write_text(json.dumps(data))
        self.assertIn("K5: .claude-plugin/marketplace.json names 'other', expected 'lusona'",
                      check.manifest_findings(self.copy, self.root))

    def test_ac8_rejects_missing_catalog(self):
        (self.root / '.cursor-plugin/marketplace.json').unlink()
        self.assertIn('K5: catalog missing: .cursor-plugin/marketplace.json',
                      check.manifest_findings(self.copy, self.root))


    # AC15 (20261110 AC10): no native manifest declares hooks
    def write_baseline_manifests(self):
        for host in ('claude', 'codex', 'cursor', 'antigravity'):
            relative = f'.{host}-plugin/plugin.json'
            (self.copy / relative).parent.mkdir(exist_ok=True)
            (self.copy / relative).write_text(baseline(f'plugins/lusona/{relative}'))

    def test_ac15_accepts_manifests_without_hooks(self):
        self.write_baseline_manifests()
        self.assertEqual(check.hooks_findings(self.copy), [])

    def test_ac15_rejects_manifest_declaring_hooks(self):
        self.write_baseline_manifests()
        for host in ('claude', 'codex', 'cursor', 'antigravity'):
            with self.subTest(host=host):
                path = self.copy / f'.{host}-plugin/plugin.json'
                original = path.read_text()
                data = json.loads(original)
                data['hooks'] = './hooks/completion.json'
                path.write_text(json.dumps(data))
                self.assertEqual(check.hooks_findings(self.copy),
                                 [f'AC15: .{host}-plugin/plugin.json declares hooks'])
                path.write_text(original)


if __name__ == '__main__':
    unittest.main()
