#!/usr/bin/env python3
"""Tests for scripts/check_rule_inventory.py against the W15 inventory note and copies of it."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/check_rule_inventory.py'
NOTE = ROOT / 'docs/lusona/notes/rule-inventory-34186da.md'


def run(note=NOTE):
    return subprocess.run([sys.executable, str(SCRIPT), str(note), '34186da'], cwd=ROOT,
                          capture_output=True, text=True)


class RuleInventoryTests(unittest.TestCase):
    def setUp(self):
        (ROOT / 'tmp').mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='rule-inventory-test-', dir=ROOT / 'tmp')

    def tearDown(self):
        self.temporary.cleanup()

    def test_note_covers_every_source_including_per_skill_reference(self):
        # N7: skills/batch/references/execution.md is a baseline reference source.
        result = run()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertRegex(result.stdout, r'(?m)^execution: 167 lines, \d+ content lines, 0 uncovered, ')
        self.assertIn('TOTAL: 22 files', result.stdout)

    def test_missing_per_skill_rows_fail(self):
        text = NOTE.read_text(encoding='utf-8')
        kept = ''.join(line for line in text.splitlines(keepends=True) if not line.startswith('| execution-'))
        note = Path(self.temporary.name) / 'note.md'
        note.write_text(kept, encoding='utf-8')
        result = run(note)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn('execution: no rows', result.stdout)

    def test_altered_row_text_fails(self):
        text = NOTE.read_text(encoding='utf-8')
        line = next(l for l in text.splitlines() if l.startswith('| execution-001 |'))
        cells = line.split(' | ')
        cells[2] = 'Text that is not in the source.'
        note = Path(self.temporary.name) / 'note.md'
        note.write_text(text.replace(line, ' | '.join(cells)), encoding='utf-8')
        result = run(note)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("execution: rule text not found verbatim in its line range: ['execution-001']", result.stdout)


if __name__ == '__main__':
    unittest.main()
