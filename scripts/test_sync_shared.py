#!/usr/bin/env python3
"""Tests for scripts/sync_shared.py against fixture plugins in temporary directories."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/sync_shared.py'

EVERY_TASK = 'Rule one.\nRule two.\n'
FINAL_REPLY = '**Result**: Complete.\n'


def skill_text(every='old block\n', final='old reply\n'):
    return ('---\nname: a\ndescription: x\n---\n\n# A\n\n'
            f'<!-- lusona:begin every-task -->\n{every}<!-- lusona:end every-task -->\n\n'
            '## Final reply\n\n'
            f'<!-- lusona:begin final-reply -->\n{final}<!-- lusona:end final-reply -->\n')


class SyncTests(unittest.TestCase):
    def setUp(self):
        (ROOT / 'tmp').mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='sync-shared-test-', dir=ROOT / 'tmp')
        base = Path(self.temporary.name)
        self.source = base / 'shared'
        self.plugin = base / 'lusona'
        self.source.mkdir()
        (self.source / 'every-task.md').write_text(EVERY_TASK)
        (self.source / 'final-reply.md').write_text(FINAL_REPLY)
        for name in ('a', 'b'):
            (self.plugin / 'skills' / name).mkdir(parents=True)
            (self.skill(name)).write_text(skill_text())

    def tearDown(self):
        self.temporary.cleanup()

    def skill(self, name):
        return self.plugin / 'skills' / name / 'SKILL.md'

    def run_sync(self, *extra):
        return subprocess.run([sys.executable, str(SCRIPT), '--source', str(self.source),
                               str(self.plugin), *extra], capture_output=True, text=True)

    def snapshot(self):
        return {p: p.read_bytes() for p in sorted(self.plugin.rglob('SKILL.md'))}

    def test_sync_replaces_region_bodies(self):
        result = self.run_sync()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.skill('a').read_text(), skill_text(EVERY_TASK, FINAL_REPLY))

    def test_sync_then_check_passes(self):
        self.assertEqual(self.run_sync().returncode, 0)
        result = self.run_sync('--check')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_sync_is_idempotent(self):
        self.run_sync()
        first = self.snapshot()
        self.run_sync()
        self.assertEqual(self.snapshot(), first)

    def test_source_without_trailing_newline_syncs_and_checks(self):
        (self.source / 'final-reply.md').write_text('No newline')
        self.assertEqual(self.run_sync().returncode, 0)
        self.assertIn('<!-- lusona:begin final-reply -->\nNo newline\n<!-- lusona:end final-reply -->',
                      self.skill('a').read_text())
        self.assertEqual(self.run_sync('--check').returncode, 0)

    def test_check_reports_differing_region_and_writes_nothing(self):
        before = self.snapshot()
        result = self.run_sync('--check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('skills/a/SKILL.md', result.stdout)
        self.assertIn('every-task', result.stdout)
        self.assertEqual(self.snapshot(), before)

    def test_check_reports_only_the_differing_skill(self):
        self.run_sync()
        self.skill('b').write_text(skill_text(EVERY_TASK, 'edited\n'))
        result = self.run_sync('--check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('skills/b/SKILL.md', result.stdout)
        self.assertNotIn('skills/a/SKILL.md', result.stdout)
        self.assertIn('final-reply', result.stdout)

    def test_check_reports_missing_region(self):
        self.run_sync()
        self.skill('b').write_text('---\nname: b\n---\n\n# B\n\n<!-- lusona:begin every-task -->\n'
                                   + EVERY_TASK + '<!-- lusona:end every-task -->\n')
        result = self.run_sync('--check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('skills/b/SKILL.md', result.stdout)
        self.assertIn('final-reply', result.stdout)

    def test_check_reports_unterminated_region(self):
        self.run_sync()
        text = self.skill('a').read_text().replace('<!-- lusona:end every-task -->\n', '')
        self.skill('a').write_text(text)
        result = self.run_sync('--check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('skills/a/SKILL.md', result.stdout)

    def test_check_rejects_end_marker_with_trailing_text(self):
        # N10, reviewer fixture tmp/w13b/s-trail.
        self.run_sync()
        text = self.skill('a').read_text().replace('<!-- lusona:end every-task -->\n',
                                                   '<!-- lusona:end every-task --> extra text\n')
        self.skill('a').write_text(text)
        result = self.run_sync('--check')
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn('skills/a/SKILL.md: region every-task end marker line has extra text', result.stdout)

    def test_trailing_text_marker_is_not_skipped_for_a_later_marker(self):
        self.run_sync()
        text = self.skill('a').read_text().replace(
            '<!-- lusona:end every-task -->\n',
            '<!-- lusona:end every-task -->x\nmore\n<!-- lusona:end every-task -->\n')
        self.skill('a').write_text(text)
        before = self.snapshot()
        result = self.run_sync()
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn('region every-task end marker line has extra text', result.stdout)
        self.assertEqual(self.snapshot(), before)

    def test_check_reports_region_without_source(self):
        self.run_sync()
        with self.skill('a').open('a') as f:
            f.write('<!-- lusona:begin unknown -->\nx\n<!-- lusona:end unknown -->\n')
        result = self.run_sync('--check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('unknown', result.stdout)

    def test_sync_rejects_skill_without_markers_and_writes_nothing(self):
        self.skill('b').write_text('---\nname: b\n---\n\n# B\n')
        before = self.snapshot()
        result = self.run_sync()
        self.assertEqual(result.returncode, 1)
        self.assertIn('skills/b/SKILL.md', result.stdout)
        self.assertEqual(self.snapshot(), before)

    # Word limit of the every-task block (user decision 2026-11-11: at most 300 words).
    def test_every_task_at_the_word_limit_passes(self):
        (self.source / 'every-task.md').write_text('word ' * 300 + '\n')
        self.assertEqual(self.run_sync().returncode, 0)
        self.assertEqual(self.run_sync('--check').returncode, 0)

    def test_check_reports_every_task_over_the_word_limit(self):
        self.run_sync()
        (self.source / 'every-task.md').write_text('word ' * 301 + '\n')
        result = self.run_sync('--check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('every-task.md: 301 words exceeds 300', result.stdout)

    def test_sync_rejects_every_task_over_the_word_limit_and_writes_nothing(self):
        (self.source / 'every-task.md').write_text('word ' * 301 + '\n')
        before = self.snapshot()
        result = self.run_sync()
        self.assertEqual(result.returncode, 1)
        self.assertIn('every-task.md: 301 words exceeds 300', result.stdout)
        self.assertEqual(self.snapshot(), before)

    def test_other_sources_have_no_word_limit(self):
        (self.source / 'final-reply.md').write_text('word ' * 400 + '\n')
        self.assertEqual(self.run_sync().returncode, 0)

    def test_missing_source_dir_is_usage_error(self):
        self.source = self.source.parent / 'absent'
        self.assertEqual(self.run_sync('--check').returncode, 2)

    def test_plugin_without_skills_is_usage_error(self):
        self.plugin = self.plugin.parent / 'empty'
        self.plugin.mkdir()
        self.assertEqual(self.run_sync('--check').returncode, 2)


if __name__ == '__main__':
    unittest.main()
