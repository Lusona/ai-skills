#!/usr/bin/env python3
"""Tests for scripts/check_instructions.py against the canonical plugin and fixtures."""
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/lusona'
spec = importlib.util.spec_from_file_location('check_instructions', ROOT / 'scripts/check_instructions.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

CATALOG = """
| Skill | Persona and responsibility | Output |
| --- | --- | --- |
| [a](../skills/a/SKILL.md) | x | y |
| [b](../skills/b/SKILL.md) | x | y |
| [c](../skills/c/SKILL.md) | x | y |
"""
ROUTING = """
| Evidence or gap | Action | Inputs |
| --- | --- | --- |
| need a | [a](../skills/a/SKILL.md) | i |
| need b | [b](../skills/b/SKILL.md) | i |
| need c | [c](../skills/c/SKILL.md) | i |
"""
DISPATCH = """
| Responsibility | Inputs and dispatch condition |
| --- | --- |
| [a](../skills/a/SKILL.md) | when x |
| [b](../skills/b/SKILL.md) | when y |
| [c](../skills/c/SKILL.md) | when z |
"""


class InstructionTests(unittest.TestCase):
    def setUp(self):
        (ROOT / 'tmp').mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='instructions-test-', dir=ROOT / 'tmp')
        self.copy = Path(self.temporary.name) / 'lusona'
        shutil.copytree(PLUGIN, self.copy)

    def tearDown(self):
        self.temporary.cleanup()

    # Canonical sources (AC2, AC4)
    def test_skills_do_not_restate_core_clauses(self):
        findings = check.restated_clauses(PLUGIN)
        self.assertEqual(findings, [], '\n'.join(f'{p}:{n}: {m}' for p, n, m in findings))

    def test_workflow_guide_owns_catalog_and_routing_tables(self):
        self.assertEqual(check.table_findings(PLUGIN), [])

    # Checker behavior (fixtures)
    def test_rejects_duplicate_catalog_table(self):
        with (self.copy / 'references/files.md').open('a') as f:
            f.write(CATALOG)
        self.assertIn('catalog table duplicated in references/files.md', check.table_findings(self.copy))

    def test_rejects_duplicate_routing_table(self):
        with (self.copy / 'skills/status/SKILL.md').open('a') as f:
            f.write(ROUTING)
        self.assertIn('routing table duplicated in skills/status/SKILL.md', check.table_findings(self.copy))

    def test_requires_routing_table_in_guide(self):
        guide = self.copy / 'references/workflow-guide.md'
        text = guide.read_text()
        kept = [t for t in check.tables(text) if check.classify(*t) == 'routing']
        if kept:
            lines = text.splitlines()
            # remove routing table lines by rewriting without any table whose header matches
            out, skip = [], False
            for i, line in enumerate(lines):
                if line.startswith('|') and check.ROUTING_HEADER.search(line.split('|')[1]):
                    skip = True
                if skip and not line.startswith('|'):
                    skip = False
                if not skip:
                    out.append(line)
            guide.write_text('\n'.join(out) + '\n')
        self.assertIn('routing table missing from references/workflow-guide.md',
                      check.table_findings(self.copy))

    def test_allows_batch_dispatch_conditions(self):
        with (self.copy / 'skills/batch/SKILL.md').open('a') as f:
            f.write(DISPATCH)
        findings = [f for f in check.table_findings(self.copy) if 'skills/batch' in f]
        self.assertEqual(findings, [])

    def test_link_text_is_not_a_restatement(self):
        skill = self.copy / 'skills/explore/SKILL.md'
        skill.write_text('# Explore\n\nSee [does not authorize](../../README.md#contract).\n')
        self.assertEqual([f for f in check.restated_clauses(self.copy) if 'explore' in str(f[0])], [])

    def test_frontmatter_description_is_exempt(self):
        skill = self.copy / 'skills/explore/SKILL.md'
        skill.write_text('---\nname: explore\ndescription: Discussion does not authorize implementation.\n---\n\n# Explore\n')
        self.assertEqual([f for f in check.restated_clauses(self.copy) if 'explore' in str(f[0])], [])

    def test_wrapped_restatement_is_found(self):
        skill = self.copy / 'skills/explore/SKILL.md'
        skill.write_text('---\nname: explore\n---\n# Explore\n\nA long sentence so that discussion does not\nauthorize implementation.\n')
        self.assertEqual([(f[0], f[1], f[2]) for f in check.restated_clauses(self.copy) if 'explore' in str(f[0])],
                         [(Path('skills/explore/SKILL.md'), 6, 'does not authorize')])

    def test_wrapped_link_text_is_not_a_restatement(self):
        skill = self.copy / 'skills/explore/SKILL.md'
        skill.write_text('# Explore\n\nSee [why discussion does not\nauthorize work](../../README.md#contract).\n')
        self.assertEqual([f for f in check.restated_clauses(self.copy) if 'explore' in str(f[0])], [])

    def test_restatement_outside_link_is_found(self):
        skill = self.copy / 'skills/explore/SKILL.md'
        skill.write_text('---\nname: explore\n---\n# Explore\n\nDiscussion does not authorize implementation.\n')
        self.assertEqual([(f[0], f[1]) for f in check.restated_clauses(self.copy) if 'explore' in str(f[0])],
                         [(Path('skills/explore/SKILL.md'), 6)])


if __name__ == '__main__':
    unittest.main()
