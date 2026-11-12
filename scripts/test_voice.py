#!/usr/bin/env python3
"""Tests for scripts/check_voice.py against fixture plugin trees."""
import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('check_voice', ROOT / 'scripts/check_voice.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

CLEAN = '---\nname: a\ndescription: Do a thing.\n---\n\n# A\n\nRead the spec. Run the tests.\n'
SKILL = Path('skills/a/SKILL.md')


class VoiceTests(unittest.TestCase):
    def setUp(self):
        (ROOT / 'tmp').mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='voice-test-', dir=ROOT / 'tmp')
        self.plugin = Path(self.temporary.name) / 'lusona'
        self.write(SKILL, CLEAN)
        self.write(Path('references/r.md'), '# R\n\nRead the queue.\n')

    def tearDown(self):
        self.temporary.cleanup()

    def write(self, relative, text):
        path = self.plugin / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')

    def body(self, text, relative=SKILL):
        self.write(relative, '---\nname: a\n---\n\n# A\n\n' + text)

    def terms(self):
        return [(str(p), n, t) for p, n, t in check.term_findings(self.plugin)]

    # Banned terms that must be found
    def test_finds_hedge_word(self):
        self.body('Usually run the tests.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'usually')])

    def test_finds_hedge_phrase(self):
        self.body('You may want to run the tests.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'may want to')])

    def test_finds_try_to(self):
        self.body('Try to run the tests.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'try to')])

    def test_finds_consider_case_insensitive(self):
        self.body('CONSIDER the callers.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'consider')])

    def test_finds_analyst_hedge(self):
        self.body('Tests typically pass.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'typically')])

    def test_finds_filler_adjective(self):
        self.body('Write a robust check.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'robust')])

    def test_finds_hyphenated_filler(self):
        self.body('Build a best-in-class check.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'best-in-class')])

    def test_finds_filler_verb_inflection(self):
        self.body('Run checks, leveraging the cache.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'leverage')])

    def test_finds_as_needed(self):
        self.body('Read the logs as needed.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'as needed')])

    def test_finds_wrapped_when_needed(self):
        self.body('Read the logs when\nneeded.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'when needed')])

    # Vague conditions added by the user decision of 2026-11-11 (voice pass).
    def test_finds_vague_conditions(self):
        for text, term in (('Link the ticket when relevant.\n', 'relevant'),
                           ('Add tasks when useful.\n', 'useful'),
                           ('Give a prompt if needed.\n', 'if needed'),
                           ('If relevant, recommend a state.\n', 'relevant'),
                           ('List the paths; omit when unnecessary.\n', 'omit when unnecessary')):
            with self.subTest(term=term):
                self.body(text)
                self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, term)])

    def test_finds_wrapped_vague_condition(self):
        self.body('Give a prompt if\nneeded.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'if needed')])

    def test_vague_condition_words_alone_are_allowed(self):
        self.body('Ask when the answer is needed. Record each applicable rule.\n')
        self.assertEqual(self.terms(), [])

    # Vague conditions and bare qualifiers added by the user decision of 2026-11-11 (round 3).
    def test_finds_applicable_conditions(self):
        for text, term in (('State the TDD level when applicable.\n', 'when applicable'),
                           ('Name the method if applicable.\n', 'if applicable')):
            with self.subTest(term=term):
                self.body(text)
                self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, term)])

    def test_finds_bare_qualifiers(self):
        for text, term in (('Inspect the relevant code.\n', 'relevant'),
                           ('Report decision-relevant results.\n', 'relevant'),
                           ('Omit irrelevant sections.\n', 'irrelevant'),
                           ('Recommend the smallest useful scope.\n', 'useful'),
                           ('Group the rows usefully.\n', 'useful')):
            with self.subTest(text=text):
                self.body(text)
                self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, term)])

    def test_words_containing_a_bare_qualifier_are_allowed(self):
        self.body('State the relevance of each link. Measure usefulness.\n')
        self.assertEqual(self.terms(), [])

    def test_finds_wrapped_phrase_at_first_line(self):
        self.body('Read the spec. You may want\nto run the tests.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'may want to')])

    def test_finds_term_in_underscore_emphasis(self):
        self.body('Run _usually_ twice.\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'usually')])

    def test_finds_term_in_table_cell(self):
        self.body('| Case | Action |\n| --- | --- |\n| x | Consider y |\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 9, 'consider')])

    def test_finds_term_in_nested_reference(self):
        self.write(Path('references/sub/r.md'), 'Delve into the logs.\n')
        self.assertEqual(self.terms(), [('references/sub/r.md', 1, 'delve')])

    def test_finds_term_in_skill_reference(self):
        self.write(Path('skills/x/references/sub/y.md'), 'Usually run this.\n')
        self.assertEqual(self.terms(), [('skills/x/references/sub/y.md', 1, 'usually')])

    def test_long_sentence_in_skill_reference_fails(self):
        self.write(Path('skills/x/references/y.md'), ' '.join(['word'] * 41) + '.\n')
        findings = check.length_findings(self.plugin, max_avg=100, max_sentence=40)
        self.assertEqual([(str(p), n, m) for p, n, m in findings],
                         [('skills/x/references/y.md', 1, 'sentence of 41 words exceeds 40')])

    def test_finds_term_in_shared_block(self):
        self.write(Path('shared/every-task.md'), 'Streamline the plan.\n')
        self.assertEqual(self.terms(), [('shared/every-task.md', 1, 'streamline')])

    def test_finds_term_in_html_comment(self):
        self.body('<!-- Usually skip this. -->\n')
        self.assertEqual(self.terms(), [('skills/a/SKILL.md', 7, 'usually')])

    # Text that must pass
    def test_clean_text_passes(self):
        self.assertEqual(self.terms(), [])

    def test_fenced_code_block_is_excluded(self):
        self.body('Run:\n\n```sh\n# usually robust\nleverage --try to\n```\n')
        self.assertEqual(self.terms(), [])

    def test_inline_code_is_excluded(self):
        self.body('Run `consider --robust`.\n')
        self.assertEqual(self.terms(), [])

    def test_link_text_is_scanned_and_target_excluded(self):
        # N4, reviewer fixture tmp/w13b/f5: "[a robust and seamless checklist](...)".
        self.body('Read [robust\nchecks](../usually.md).\n')
        self.assertEqual(self.terms(), [(str(SKILL), 7, 'robust')])

    def test_link_target_is_excluded(self):
        self.body('Read [checks](../usually-robust.md) and [x](https://example.com/leverage).\n')
        self.assertEqual(self.terms(), [])

    def test_frontmatter_description_is_scanned(self):
        # N4, reviewer fixture tmp/w13b/f5: "description: Usually consider and leverage this. ..."
        self.write(SKILL, '---\nname: a\ndescription: Usually consider a robust plan.\n---\n\n# A\n\nRun it.\n')
        self.assertEqual(self.terms(), [(str(SKILL), 3, 'consider'), (str(SKILL), 3, 'robust'),
                                        (str(SKILL), 3, 'usually')])

    def test_folded_and_quoted_frontmatter_description_is_scanned(self):
        self.write(SKILL, '---\nname: a\ndescription: >\n  Plan it.\n  Maybe leverage it.\n'
                          'other: robust\n---\n\n# A\n\nRun it.\n')
        self.assertEqual(self.terms(), [(str(SKILL), 5, 'leverage'), (str(SKILL), 5, 'maybe')])
        self.write(SKILL, '---\nname: a\ndescription: "Usually run it."\n---\n\n# A\n\nRun it.\n')
        self.assertEqual(self.terms(), [(str(SKILL), 3, 'usually')])

    def test_other_frontmatter_fields_are_excluded(self):
        self.write(SKILL, '---\nname: robust\nlicense: usually\ndescription: Do a thing.\n---\n\n# A\n\nRun it.\n')
        self.assertEqual(self.terms(), [])

    def test_description_is_not_counted_for_sentence_length(self):
        long = ' '.join(['word'] * 45) + '.'
        self.write(SKILL, f'---\nname: a\ndescription: {long}\n---\n\n# A\n\nRun it.\n')
        self.assertEqual(check.length_findings(self.plugin), [])

    def test_permission_may_and_participle_pass(self):
        self.body('Workers may run in parallel. Record alternatives considered.\n')
        self.assertEqual(self.terms(), [])

    def test_partial_words_pass(self):
        self.body('Reconsider unusually locked doors in trying times.\n')
        self.assertEqual(self.terms(), [])

    def test_templates_are_scanned_for_terms(self):
        self.write(Path('templates/t.md'), 'Usually run this.\n')
        self.assertEqual(self.terms(), [('templates/t.md', 1, 'usually')])

    def test_renamed_markdown_templates_are_scanned_for_terms(self):
        self.write(Path('templates/x.md.template'), 'Usually run this.\n')
        self.assertEqual(self.terms(), [('templates/x.md.template', 1, 'usually')])

    def test_html_templates_are_not_scanned(self):
        self.write(Path('templates/x.html.template'), '<p>Usually run this.</p>\n')
        self.write(Path('templates/x.html'), '<p>Usually run this.</p>\n')
        self.assertEqual(self.terms(), [])

    def test_templates_are_not_length_checked(self):
        self.write(Path('templates/t.md'), ' '.join(['word'] * 50) + '.\n')
        self.assertEqual(check.length_findings(self.plugin, max_avg=15), [])

    # Sentence length
    def test_sentence_lengths_skip_headings_tables_code(self):
        text = ('---\nname: a\n---\n# A heading with many words here\n\n'
                '| a | b |\n| --- | --- |\n\n```\nlong code line words\n```\n\n'
                'One two three. Four five,\ne.g. six.\n\n- Item one\n- Item two words\n')
        self.assertEqual([n for _, n in check.sentence_lengths(text)], [3, 4, 2, 3])

    def test_sentence_line_is_first_line(self):
        text = '# A\n\nOne two.\nThree four\nfive.\n'
        self.assertEqual(check.sentence_lengths(text), [(3, 2), (4, 3)])

    def test_long_average_fails(self):
        long = ' '.join(['word'] * 30) + '.\n'
        self.body(long + 'Short one.\n')
        findings = check.length_findings(self.plugin, max_avg=15)
        self.assertEqual([(str(p), n) for p, n, _ in findings], [('skills/a/SKILL.md', 1)])
        self.assertIn('average 16.0 words per sentence exceeds 15', findings[0][2])

    def test_long_sentence_fails_with_line(self):
        self.body('Short one. ' * 10 + '\n\n' + ' '.join(['word'] * 41) + '.\n')
        findings = check.length_findings(self.plugin, max_avg=15, max_sentence=40)
        self.assertEqual([(str(p), n, m) for p, n, m in findings],
                         [('skills/a/SKILL.md', 9, 'sentence of 41 words exceeds 40')])

    def test_sentence_at_maximum_passes(self):
        self.body('Short one. ' * 10 + '\n\n' + ' '.join(['word'] * 40) + '.\n')
        self.assertEqual(check.length_findings(self.plugin, max_avg=15, max_sentence=40), [])

    def test_short_average_passes(self):
        self.body('Read the spec. Run the tests.\n')
        self.assertEqual(check.length_findings(self.plugin, max_avg=15), [])

    # Command line
    def run_main(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = check.main([str(self.plugin), *args])
        return status, out.getvalue()

    def test_main_exit_zero_when_clean(self):
        self.assertEqual(self.run_main(), (0, ''))

    def test_main_exit_one_with_findings(self):
        self.body('Usually run the tests.\n')
        status, output = self.run_main()
        self.assertEqual(status, 1)
        self.assertIn('skills/a/SKILL.md:7: usually', output)

    def test_main_fails_when_nothing_is_scanned(self):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            status = check.main([str(self.plugin / 'missing')])
        self.assertEqual(status, 2)

    def test_main_accepts_max_avg_words(self):
        self.body('One two three four five six. Seven eight nine ten eleven twelve.\n')
        self.assertEqual(self.run_main('--max-avg-words', '5')[0], 1)
        self.assertEqual(self.run_main('--max-avg-words', '6')[0], 0)


if __name__ == '__main__':
    unittest.main()
