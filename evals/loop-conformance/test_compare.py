import copy
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("loop_conformance_compare", HERE / "compare.py")
compare = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compare)


def counts(passed=0, failed=0, inconclusive=0, blocked=0, na=0):
    return {"pass": passed, "fail": failed, "inconclusive": inconclusive,
            "setup-blocked": blocked, "not-applicable": na}


def record(**check_counts):
    condition = {
        "host": "claude", "cli_version": "2.1.321 (Claude Code)", "judge_cli_version": "2.1.321 (Claude Code)",
        "model": "claude-opus-5-5",
        "effort": "high", "judge_model": "claude-fable-5-2", "judge_effort": "medium",
        "judge_prompt_sha256": "j1", "suite_hashes": {"scenarios.json": "s1", "rubric.md": "r1"},
        "ambient_instruction_hashes": {}, "plugin_hashes": {"README.md": "p1", "skills/a/SKILL.md": "p2"},
        "permission_config": {"permission_mode": "dontAsk", "allowed_tools": ["Read", "Edit"],
                              "settings": {"sandbox": {"enabled": True}}},
        "code_hashes": {"run.py": "c1", "checks.py": "c2", "compare.py": "c3"},
    }
    condition["max_trials"] = 5
    base = {"C1": counts(5), "C3": counts(5), "C5": counts(5), "C8": counts(5)}
    base.update(check_counts)
    trials = [["a", t] for t in range(1, 6)]
    return {"host": "claude", "condition": condition, "counts": base, "scenario_trials": trials,
            "grading_code_hashes": [{"run.py": "c1", "checks.py": "c2", "compare.py": "c3"}]}


class RefusalTest(unittest.TestCase):
    def test_plugin_hash_difference_is_reported_not_refused(self):
        reference, candidate = record(), record()
        candidate["condition"]["plugin_hashes"] = {"README.md": "p9", "skills/b/SKILL.md": "p3"}
        outcome = compare.compare(reference, candidate)
        self.assertEqual(outcome["status"], "pass")
        self.assertEqual(outcome["plugin_changes"],
                         {"modified": ["README.md"], "added": ["skills/b/SKILL.md"], "removed": ["skills/a/SKILL.md"]})

    def test_refuses_each_mismatched_plugin_independent_field(self):
        changes = {"suite_hashes": {"scenarios.json": "s2", "rubric.md": "r1"}, "host": "codex",
                   "model": "claude-fable-5-2", "effort": "low",
                   "judge_model": "other", "judge_effort": "high", "judge_prompt_sha256": "j2",
                   "ambient_instruction_hashes": {"/home/u/.agents/AGENTS.md": "a1"},
                   "permission_config": {"permission_mode": "dontAsk", "allowed_tools": ["Read", "Edit", "Bash(rm *)"],
                                         "settings": {"sandbox": {"enabled": True}}}}
        for field, value in changes.items():
            with self.subTest(field=field):
                candidate = record()
                candidate["condition"][field] = value
                outcome = compare.compare(record(), candidate)
                self.assertEqual(outcome["status"], "refused")
                self.assertTrue(any(field in reason for reason in outcome["reasons"]), outcome["reasons"])


class CliVersionTest(unittest.TestCase):
    def test_cli_version_differences_are_warnings_not_refusals(self):
        candidate = record()
        candidate["condition"]["cli_version"] = "2.1.400 (Claude Code)"
        candidate["condition"]["judge_cli_version"] = "2.1.401 (Claude Code)"
        outcome = compare.compare(record(), candidate)
        self.assertEqual(outcome["status"], "pass")
        warnings = " ".join(outcome["warnings"])
        for version in ("2.1.321 (Claude Code)", "2.1.400 (Claude Code)", "2.1.401 (Claude Code)"):
            self.assertIn(version, warnings)
        self.assertIn("2.1.400 (Claude Code)", compare.render(outcome))


class TrialSetTest(unittest.TestCase):
    def test_refuses_different_trial_sets_or_trial_budget(self):
        # Reviewer's case: reference 8 trials of a 10-trial budget, candidate 9 of 15.
        reference, candidate = record(), record()
        reference["scenario_trials"] = [["a", t] for t in range(1, 9)]
        reference["condition"]["max_trials"] = 10
        candidate["scenario_trials"] = [["a", t] for t in range(1, 10)]
        candidate["condition"]["max_trials"] = 15
        outcome = compare.compare(reference, candidate)
        self.assertEqual(outcome["status"], "refused")
        self.assertTrue(any("scenario_trials" in r for r in outcome["reasons"]), outcome["reasons"])
        self.assertTrue(any("max_trials" in r for r in outcome["reasons"]), outcome["reasons"])
        same_budget = record()
        same_budget["scenario_trials"] = [["a", t] for t in range(1, 5)]
        self.assertEqual(compare.compare(record(), same_budget)["status"], "refused")

    def test_different_grading_code_is_a_warning(self):
        candidate = record()
        candidate["grading_code_hashes"] = [{"run.py": "c1", "checks.py": "c9", "compare.py": "c3"}]
        outcome = compare.compare(record(), candidate)
        self.assertEqual(outcome["status"], "pass")
        self.assertTrue(any("checks.py" in w for w in outcome["warnings"]), outcome["warnings"])
        self.assertIn("checks.py", compare.render(outcome))


class RegressionRuleTest(unittest.TestCase):
    def test_boundary_fail_in_any_trial_fails_candidate(self):
        for check in ("C3", "C5", "C8"):
            with self.subTest(check=check):
                outcome = compare.compare(record(), record(**{check: counts(4, 1)}))
                self.assertEqual(outcome["status"], "fail")
                self.assertEqual(outcome["checks"][check]["status"], "fail")

    def test_boundary_fail_outranks_insufficient(self):
        outcome = compare.compare(record(), record(C3=counts(0, 1, inconclusive=4)))
        self.assertEqual(outcome["checks"]["C3"]["status"], "fail")
        self.assertEqual(outcome["status"], "fail")

    def test_drop_of_two_flags_and_drop_of_one_does_not(self):
        flagged = compare.compare(record(), record(C1=counts(3, 2)))
        self.assertEqual(flagged["status"], "flagged")
        self.assertEqual(flagged["checks"]["C1"]["status"], "flagged")
        steady = compare.compare(record(), record(C1=counts(4, 1)))
        self.assertEqual(steady["status"], "pass")
        self.assertEqual(steady["checks"]["C1"]["status"], "ok")

    def test_non_boundary_fail_without_drop_is_not_a_candidate_failure(self):
        reference = record(C9=counts(2, 3))
        outcome = compare.compare(reference, record(C9=counts(2, 3)))
        self.assertEqual(outcome["status"], "pass")

    def test_fewer_than_four_graded_trials_is_insufficient(self):
        outcome = compare.compare(record(), record(C1=counts(3, 0, inconclusive=2)))
        self.assertEqual(outcome["checks"]["C1"]["status"], "insufficient")
        self.assertEqual(outcome["status"], "insufficient")
        thin_reference = record(C1=counts(3, 0, blocked=2))
        self.assertEqual(compare.compare(thin_reference, record())["checks"]["C1"]["status"], "insufficient")

    def test_not_applicable_only_check_is_not_reported_as_passing(self):
        outcome = compare.compare(record(C6=counts(na=5)), record(C6=counts(na=5)))
        self.assertEqual(outcome["checks"]["C6"]["status"], "unavailable")
        self.assertNotEqual(outcome["checks"]["C6"]["status"], "ok")

    def test_check_ungraded_on_both_sides_is_unavailable_and_does_not_block_pass(self):
        # Codex-like: the host never exposes workers, so C10 is inconclusive in every trial.
        outcome = compare.compare(record(C10=counts(inconclusive=5)), record(C10=counts(inconclusive=5)))
        self.assertEqual(outcome["checks"]["C10"]["status"], "unavailable")
        self.assertEqual(outcome["status"], "pass")
        self.assertIn("| C10 |", compare.render(outcome))
        self.assertIn("unavailable", compare.render(outcome))

    def test_check_graded_on_one_side_only_is_insufficient(self):
        outcome = compare.compare(record(C10=counts(5)), record(C10=counts(inconclusive=5)))
        self.assertEqual(outcome["checks"]["C10"]["status"], "insufficient")
        self.assertEqual(outcome["status"], "insufficient")
        partial = compare.compare(record(C10=counts(1, 1, inconclusive=3)), record(C10=counts(2, 0, inconclusive=3)))
        self.assertEqual(partial["checks"]["C10"]["status"], "insufficient")

    def test_markdown_rendering_lists_status_and_each_check(self):
        outcome = compare.compare(record(), record(C1=counts(3, 2), C3=counts(4, 1)))
        text = compare.render(outcome)
        self.assertIn("Status: **fail**", text)
        for check in ("C1", "C3", "C5", "C8"):
            self.assertIn(f"| {check} |", text)
        refused = record()
        refused["condition"]["model"] = "other"
        self.assertIn("Status: **refused**", compare.render(compare.compare(record(), refused)))

    def test_inputs_are_not_mutated(self):
        reference, candidate = record(), record(C1=counts(3, 2))
        before = copy.deepcopy((reference, candidate))
        compare.compare(reference, candidate)
        self.assertEqual((reference, candidate), before)


if __name__ == "__main__":
    unittest.main()
