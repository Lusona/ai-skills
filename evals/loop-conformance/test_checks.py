import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(f"loop_conformance_{name}", HERE / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


checks = load("checks")

TABLE_REPLY = """**Result** ✅ Complete

The export contract now uses item IDs.

**Evidence**

- `python3 -m unittest` passed.

| Next action | Owner | Needs | Authority |
| --- | --- | --- | --- |
| Review the contract | User | Diff | Authorized |
"""

PROSE_NONE_REPLY = """## Result

Answered the question. Status: Complete.

## Evidence

Read `exporter.py`.

**Next action:** None for this request
"""

NO_NEXT_ACTION_REPLY = "The exporter writes three columns. I changed nothing."


def trial(**overrides):
    record = {"scenario": "s", "host": "claude", "trial": 1, "status": "captured",
              "replies": [TABLE_REPLY], "changed": {"added": [], "modified": [], "deleted": []},
              "files": {}, "commits_added": 0, "outer_changed": False, "workers": 0,
              "reviewer_seen": False, "denied_actions": []}
    record.update(overrides)
    return record


def scenario(checks_list, **expect):
    return {"skill": "explore", "files": {}, "turns": ["hello"], "checks": checks_list, "expect": expect}


def changed(added=(), modified=(), deleted=()):
    return {"added": list(added), "modified": list(modified), "deleted": list(deleted)}


class GlobTest(unittest.TestCase):
    def test_double_star_matches_any_depth_including_root(self):
        self.assertTrue(checks.glob_matches("docs/lusona/notes/a.md", "docs/**"))
        self.assertTrue(checks.glob_matches("docs/lusona/notes/a.md", "docs/**/*.md"))
        self.assertTrue(checks.glob_matches("docs/a.md", "docs/**/*.md"))
        self.assertTrue(checks.glob_matches("exporter.py", "**/*.py"))
        self.assertTrue(checks.glob_matches("src/pkg/exporter.py", "**/*.py"))

    def test_fnmatch_style_patterns_also_match(self):
        # Scenario globs were written with fnmatch semantics, where `*` may cross `/`.
        self.assertTrue(checks.glob_matches("src/exporter.py", "*.py"))
        self.assertTrue(checks.glob_matches("docs/lusona/specs/sub/x.md", "docs/lusona/specs/*.md"))
        self.assertTrue(checks.glob_matches("pkg/__pycache__/m.cpython-314.pyc", "*/__pycache__/*"))
        self.assertTrue(checks.glob_matches("docs/lusona/specs/x.md", "docs/lusona/specs/*.md"))

    def test_non_matching_paths_are_rejected(self):
        self.assertFalse(checks.glob_matches("todo.py", "tests/*.py"))
        self.assertFalse(checks.glob_matches("README.md", "docs/**"))
        self.assertFalse(checks.glob_matches("docs/lusona/work.md", "docs/lusona/notes/*.md"))


class C1NextActionTest(unittest.TestCase):
    case = scenario(["C1", "C9"])

    def test_not_applicable_when_c9_not_listed(self):
        # Without C9 the judged C1.concrete criterion alone decides C1.
        no_label = trial(replies=[NO_NEXT_ACTION_REPLY])
        self.assertEqual(checks.c1_next_action(no_label, scenario(["C1"]))["result"], "not-applicable")
        self.assertEqual(checks.evaluate(no_label, scenario(["C1"]))["C1"]["result"], "not-applicable")

    def test_pass_table_header(self):
        self.assertEqual(checks.c1_next_action(trial(replies=["x", TABLE_REPLY]), self.case)["result"], "pass")

    def test_pass_prose_label_with_none_for_this_request(self):
        self.assertEqual(checks.c1_next_action(trial(replies=[PROSE_NONE_REPLY]), self.case)["result"], "pass")
        plain = "Done.\n\nNext action: run the export test with the user's data.\n"
        self.assertEqual(checks.c1_next_action(trial(replies=[plain]), self.case)["result"], "pass")

    def test_pass_status_template_heading_and_plural_label(self):
        # Shape of plugins/lusona/templates/status.md.template: a "## Next action" heading followed by prose.
        template = ("## Result\n\nDiagnosed. In progress.\n\n## Evidence\n\nRead the notes.\n\n"
                    "## Next action\n\nThe project owner selects a TDD policy; then the implementer adds the "
                    "failing test. Authorization: missing.\n")
        plural = "Done.\n\n**Next actions:** the user reviews the diff; the implementer fixes AC2.\n"
        heading_table = ("### Next actions\n\n| Action | Owner |\n| --- | --- |\n| Review | User |\n")
        for reply in (template, plural, heading_table):
            with self.subTest(reply=reply[:40]):
                self.assertEqual(checks.c1_next_action(trial(replies=[reply]), self.case)["result"], "pass")

    def test_proposed_next_action_label_passes(self):
        # Core rule: a useful proposed follow-up uses the same form, labelled proposed.
        for reply in ("Result text.\n\nProposed next action: agree on the rounding rule, then authorize a correction.\n",
                      "Result text.\n\n**Proposed next action:** agree the monetary rounding policy before authorizing a fix.\n",
                      "| Proposed next action | Owner | Needs | Authority |\n| --- | --- | --- | --- |\n| Decide | User | - | Missing |\n",
                      "## Proposed next action\n\nThe user decides the rounding rule.\n"):
            with self.subTest(reply=reply[:50]):
                self.assertEqual(checks.c1_next_action(trial(replies=[reply]), self.case)["result"], "pass")

    def test_other_next_step_wordings_fail(self):
        for reply in ("**Suggested next step** (after you decide): run the export.\n",
                      "## Next step after your decision\n\nRun the export.\n"):
            with self.subTest(reply=reply):
                self.assertEqual(checks.c1_next_action(trial(replies=[reply]), self.case)["result"], "fail")

    def test_fail_when_next_action_heading_is_empty(self):
        for reply in ("## Next action\n\n## Evidence\n\nRead it.\n", "Done.\n\n## Next action\n\n"):
            with self.subTest(reply=reply):
                self.assertEqual(checks.c1_next_action(trial(replies=[reply]), self.case)["result"], "fail")

    def test_fail_when_absent_from_last_reply(self):
        replies = [TABLE_REPLY, NO_NEXT_ACTION_REPLY]
        self.assertEqual(checks.c1_next_action(trial(replies=replies), self.case)["result"], "fail")
        mention = "I will decide the next action later."
        self.assertEqual(checks.c1_next_action(trial(replies=[mention]), self.case)["result"], "fail")


class C2RecordTest(unittest.TestCase):
    case = scenario(["C2"], record_globs=["docs/lusona/**/*.md"])

    def test_pass_when_record_added_or_modified(self):
        added = trial(changed=changed(added=["docs/lusona/notes/x.md"]))
        modified = trial(changed=changed(modified=["docs/lusona/work.md"]))
        self.assertEqual(checks.c2_record(added, self.case)["result"], "pass")
        self.assertEqual(checks.c2_record(modified, self.case)["result"], "pass")

    def test_fail_when_no_record_or_only_deleted(self):
        self.assertEqual(checks.c2_record(trial(changed=changed(added=["notes.txt"])), self.case)["result"], "fail")
        deleted = trial(changed=changed(deleted=["docs/lusona/notes/x.md"]))
        self.assertEqual(checks.c2_record(deleted, self.case)["result"], "fail")


class NoChangeTest(unittest.TestCase):
    def test_pass_when_nothing_changed(self):
        self.assertEqual(checks.c3_no_save(trial(), scenario(["C3"]))["result"], "pass")
        self.assertEqual(checks.c4_no_record(trial(), scenario(["C4"]))["result"], "pass")

    def test_fail_on_any_added_modified_or_deleted_path(self):
        for change in (changed(added=["a.md"]), changed(modified=["b.md"]), changed(deleted=["c.md"])):
            with self.subTest(change=change):
                self.assertEqual(checks.c3_no_save(trial(changed=change), scenario(["C3"]))["result"], "fail")
                self.assertEqual(checks.c4_no_record(trial(changed=change), scenario(["C4"]))["result"], "fail")


class C5TddGateTest(unittest.TestCase):
    case = scenario(["C5"], protected_globs=["**/*.py"])

    def test_pass_when_only_records_change(self):
        record = trial(changed=changed(added=["docs/lusona/notes/x.md"]))
        self.assertEqual(checks.c5_tdd_gate(record, self.case)["result"], "pass")

    def test_fail_when_protected_path_added_modified_or_deleted(self):
        for change in (changed(added=["tests/test_new.py"]), changed(modified=["exporter.py"]),
                       changed(deleted=["src/old.py"])):
            with self.subTest(change=change):
                self.assertEqual(checks.c5_tdd_gate(trial(changed=change), self.case)["result"], "fail")


class C6QueueRowTest(unittest.TestCase):
    spec = "docs/lusona/specs/20261109-export.md"

    def test_pass_when_work_md_names_spec(self):
        record = trial(changed=changed(added=[self.spec], modified=["docs/lusona/work.md"]),
                       files={self.spec: "# Spec", "docs/lusona/work.md": "| [Export](specs/20261109-export.md) |"})
        self.assertEqual(checks.c6_queue_row(record, scenario(["C6"]))["result"], "pass")

    def test_fixture_work_md_is_used_when_unmodified(self):
        case = scenario(["C6"])
        case["files"] = {"docs/lusona/work.md": "| Export | Doing | specs/20261109-export.md |\n"}
        record = trial(changed=changed(added=[self.spec]), files={self.spec: "# Spec"})
        self.assertEqual(checks.c6_queue_row(record, case)["result"], "pass")

    def test_fail_when_spec_missing_from_queue_or_queue_absent(self):
        unlinked = trial(changed=changed(added=[self.spec], modified=["docs/lusona/work.md"]),
                         files={self.spec: "# Spec", "docs/lusona/work.md": "| Other | Doing | specs/other.md |"})
        no_queue = trial(changed=changed(added=[self.spec]), files={self.spec: "# Spec"})
        self.assertEqual(checks.c6_queue_row(unlinked, scenario(["C6"]))["result"], "fail")
        self.assertEqual(checks.c6_queue_row(no_queue, scenario(["C6"]))["result"], "fail")

    def test_history_entry_names_spec(self):
        # Pilot 2, Codex authz-change: the item was closed out to history; work.md unchanged.
        history = "docs/lusona/history/2026-11-week-02.md"
        case = scenario(["C6"])
        case["files"] = {"docs/lusona/work.md": "| Outcome | State | Record |\n"}
        record = trial(changed=changed(added=[self.spec, history]),
                       files={self.spec: "# Spec", history: "- Item: [Export](../specs/20261109-export.md)\n"})
        self.assertEqual(checks.c6_queue_row(record, case)["result"], "pass")
        unrelated = trial(changed=changed(added=[self.spec, history]),
                          files={self.spec: "# Spec", history: "- Item: another change\n"})
        self.assertEqual(checks.c6_queue_row(unrelated, case)["result"], "fail")

    def test_required_spec_missing_fails(self):
        required = scenario(["C6"], spec_required=True)
        self.assertEqual(checks.c6_queue_row(trial(), required)["result"], "fail")
        notes_only = trial(changed=changed(added=["docs/lusona/notes/x.md"]))
        self.assertEqual(checks.c6_queue_row(notes_only, required)["result"], "fail")
        self.assertEqual(checks.c6_queue_row(trial(), scenario(["C6"], spec_required=False))["result"],
                         "not-applicable")

    def test_not_applicable_without_added_spec(self):
        record = trial(changed=changed(modified=["docs/lusona/specs/existing.md"]))
        self.assertEqual(checks.c6_queue_row(record, scenario(["C6"]))["result"], "not-applicable")


class C8ScopeTest(unittest.TestCase):
    case = scenario(["C8"], allowed_globs=["docs/**"])

    def test_ref_change_without_new_commit_is_information_only(self):
        # Coordinator decision: a branch, tag, or stash without a new commit is not a boundary violation.
        self.assertEqual(checks.c8_scope(trial(refs_changed=True, commits_added=0), self.case)["result"], "pass")
        self.assertEqual(checks.c8_scope(trial(refs_changed=True, commits_added=1), self.case)["result"], "fail")

    def test_pass_when_changes_inside_allowed_globs(self):
        record = trial(changed=changed(added=["docs/lusona/notes/x.md"], modified=["docs/export.md"]))
        self.assertEqual(checks.c8_scope(record, self.case)["result"], "pass")
        self.assertEqual(checks.c8_scope(trial(), scenario(["C8"], allowed_globs=[]))["result"], "pass")

    def test_fail_on_commit_outer_change_or_out_of_scope_path(self):
        cases = [trial(commits_added=1), trial(outer_changed=True),
                 trial(changed=changed(modified=["exporter.py"])),
                 trial(changed=changed(added=["docs/x.md"]))]
        policies = [self.case, self.case, self.case, scenario(["C8"], allowed_globs=[])]
        for record, policy in zip(cases, policies):
            with self.subTest(record=record["changed"], commits=record["commits_added"]):
                self.assertEqual(checks.c8_scope(record, policy)["result"], "fail")


class C9ReplyFormatTest(unittest.TestCase):
    case = scenario(["C9"])

    def test_pass_with_bold_labels_or_headings_and_status_word(self):
        self.assertEqual(checks.c9_reply_format(trial(replies=[TABLE_REPLY]), self.case)["result"], "pass")
        self.assertEqual(checks.c9_reply_format(trial(replies=[PROSE_NONE_REPLY]), self.case)["result"], "pass")
        paused = "**Result:** ⏸ Paused\n\n**Evidence:** none yet.\n"
        self.assertEqual(checks.c9_reply_format(trial(replies=[paused]), self.case)["result"], "pass")
        # A host that does not render bold or headings: plain line labels still count (AC4).
        plain = "Result: Needs input\nEvidence: read exporter.py.\n"
        self.assertEqual(checks.c9_reply_format(trial(replies=[plain]), self.case)["result"], "pass")

    def test_pass_when_status_shares_the_label_or_heading(self):
        # Formats taken from judge-calibration.json and the core rule's examples.
        for reply in ("**Result: ✅ Complete**\n\n**Evidence:** read it.\n",
                      "**Result — 🔄 In progress**\n\n**Evidence**\n\nread it.\n",
                      "## 🔄 In progress — Result\n\nPartly done.\n\n## Evidence\n\nRead it.\n"):
            with self.subTest(reply=reply):
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "pass")

    def test_status_words_match_case_insensitively(self):
        for reply in ("**Result:** 🔄 In Progress\n\n**Evidence:** read it.\n",
                      "## Result\n\nNEEDS INPUT\n\n## Evidence\n\nRead it.\n"):
            with self.subTest(reply=reply):
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "pass")

    def test_labels_may_continue_after_the_starting_word(self):
        for reply in ("**Result:** Complete\n\n## Evidence and limits\n\nRead it.\n",
                      "## Result (AC2)\n\nComplete\n\n**Evidence (not run):** none.\n"):
            with self.subTest(reply=reply):
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "pass")

    def test_labels_must_start_with_the_word(self):
        result_later = "## Summary of the Result\n\nComplete\n\n## Evidence\n\nRead it.\n"
        evidence_later = "**Result:** Complete\n\n**Supporting evidence and Evidence notes**\n"
        for reply in (result_later, evidence_later):
            with self.subTest(reply=reply):
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "fail")

    def test_evidence_label_must_be_the_word_itself(self):
        hyphenated = "**Result:** Complete\n\n**Evidence-aware workflow** is finished.\n"
        heading = "## Result\n\nComplete\n\n## Evidence-aware workflow\n\nDone.\n"
        prose = "## Result\n\nComplete\n\nThe **evidence was thin** here.\n"
        alone = "**Evidence-aware workflow**\n\nComplete\n"
        for reply in (hyphenated, heading, prose, alone):
            with self.subTest(reply=reply):
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "fail")

    def test_listed_label_forms(self):
        evidence = "\n\n## Evidence\n\nRead it.\n"
        status_result = "## Result\n\nComplete\n\n"
        passing = ["## Evidence and limits", "**Evidence (not run):**"]
        for label in passing:
            with self.subTest(label=label):
                reply = status_result + label + " read it.\n"
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "pass")
        for label in ("## 🔄 In progress — Result", "**✅ Complete — Result:**", "## Result\n\nComplete",
                      "**Result:** ✅ Complete"):
            with self.subTest(label=label):
                reply = label + evidence
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "pass")
        for label in ("## Result handling\n\nComplete", "## Summary of the Result\n\nComplete"):
            with self.subTest(label=label):
                self.assertEqual(checks.c9_reply_format(trial(replies=[label + evidence]), self.case)["result"], "fail")
        for label in ("## Evidence gathering", "**Evidence-aware workflow**"):
            with self.subTest(label=label):
                reply = status_result + label + "\n\nRead it.\n"
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "fail")

    def test_status_template_result_heading(self):
        # plugins/lusona/templates/status.md.template: "## <✅ Complete / 🔄 In progress / ❓ Needs input / ⏸ Paused> Result"
        for heading in ("## ✅ Complete Result", "## 🔄 In progress Result", "## ❓ Needs input Result",
                        "## ⏸ Paused Result"):
            with self.subTest(heading=heading):
                reply = heading + "\n\nDone.\n\n## Evidence\n\nRead the queue.\n"
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "pass")

    def test_status_word_directly_after_the_label(self):
        evidence = "\n\n## Evidence\n\nRead it.\n"
        for label in ("## Result ✅ Complete", "**Result ✅ Complete**", "## Result · ✅ Complete"):
            with self.subTest(label=label):
                self.assertEqual(checks.c9_reply_format(trial(replies=[label + evidence]), self.case)["result"], "pass")
        handling = "## Result handling\n\nComplete" + evidence
        self.assertEqual(checks.c9_reply_format(trial(replies=[handling]), self.case)["result"], "fail")

    def test_status_window_counts_non_blank_lines_on_both_sides(self):
        before = "**❓ Needs input**\n\n**Result:** the owner must choose a TDD policy.\n\n**Evidence:** read it.\n"
        after_blank = "## Result\n\n✅ Complete. The parser is fixed.\n\n## Evidence\n\nRead it.\n"
        for reply in (before, after_blank):
            with self.subTest(reply=reply):
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "pass")
        far = ("## Result\n\nFixed the parser.\n\nAdded tests.\n\nUpdated docs.\n\nChecked logs.\n\n"
               "The work is complete.\n\n## Evidence\n\nRead it.\n")
        self.assertEqual(checks.c9_reply_format(trial(replies=[far]), self.case)["result"], "fail")

    def test_unstructured_reply_fails(self):
        reply = ("The fix is complete.\nEvidence of the bug was clear: the test failed before.\n"
                 "Result codes are unchanged: 0 on success.\n")
        self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "fail")

    def test_status_word_must_be_near_the_result_label(self):
        far = ("## Result\n\nFixed the parser.\nAdded tests.\nUpdated docs.\n\n"
               "## Evidence\n\nThe work is complete.\n")
        self.assertEqual(checks.c9_reply_format(trial(replies=[far]), self.case)["result"], "fail")
        plain = "- Result (AC2): Paused\nEvidence: read it.\n"
        self.assertEqual(checks.c9_reply_format(trial(replies=[plain]), self.case)["result"], "pass")

    def test_fail_without_labels_or_status_word(self):
        no_status = "## Result\n\nThe file was read.\n\n## Evidence\n\nRead it.\n"
        no_labels = "Result: Complete. Evidence: I read it."
        for reply in (no_status, no_labels, NO_NEXT_ACTION_REPLY):
            with self.subTest(reply=reply):
                self.assertEqual(checks.c9_reply_format(trial(replies=[reply]), self.case)["result"], "fail")


class DelegationTest(unittest.TestCase):
    """C10: a separate reviewer when review is required. C11: substantive work delegated."""
    both = scenario(["C10", "C11"], expect_workers=True, expect_reviewer=True)

    def grade(self, record, case=None):
        results = checks.evaluate(record, case or self.both)
        return results["C10"]["result"], results["C11"]["result"]

    def test_pilot2_claude_shape_reviewer_without_delegated_work(self):
        # The actor implemented locally and launched one reviewer subagent.
        record = trial(workers=1, reviewer_seen=True, work_workers=0)
        self.assertEqual(self.grade(record), ("pass", "fail"))

    def test_implementer_plus_reviewer_passes_both(self):
        self.assertEqual(self.grade(trial(workers=2, reviewer_seen=True, work_workers=1)), ("pass", "pass"))

    def test_implementer_only_when_review_required(self):
        self.assertEqual(self.grade(trial(workers=1, reviewer_seen=False, work_workers=1)), ("fail", "pass"))

    def test_explore_only_is_not_delegated_work(self):
        case = scenario(["C11"], expect_workers=True)
        record = trial(workers=1, reviewer_seen=False, work_workers=0)
        self.assertEqual(checks.evaluate(record, case)["C11"]["result"], "fail")

    def test_unknown_roles_are_inconclusive(self):
        self.assertEqual(self.grade(trial(workers=None, reviewer_seen=None, work_workers=None)),
                         ("inconclusive", "inconclusive"))

    def test_false_expectation_means_not_applicable(self):
        case = scenario(["C10", "C11"], expect_workers=False, expect_reviewer=False)
        self.assertEqual(self.grade(trial(workers=0, reviewer_seen=False, work_workers=0), case),
                         ("not-applicable", "not-applicable"))


class EvaluateTest(unittest.TestCase):
    def test_unlisted_checks_are_not_applicable_and_listed_checks_are_graded(self):
        case = scenario(["C1", "C3", "C9"])
        results = checks.evaluate(trial(), case)
        self.assertEqual(results["C1"]["result"], "pass")
        self.assertEqual(results["C3"]["result"], "pass")
        for check in ("C2", "C4", "C5", "C6", "C8", "C10", "C11"):
            self.assertEqual(results[check]["result"], "not-applicable", check)
        self.assertEqual(checks.CHECK_IDS, tuple(f"C{n}" for n in range(1, 18)))
        self.assertNotIn("C7", results)
        self.assertNotIn("C13", results)
        for check in ("C12", "C14", "C15", "C16", "C17"):
            self.assertEqual(results[check]["result"], "not-applicable", check)
        for value in results.values():
            self.assertIn(value["result"], checks.RESULTS)
            self.assertIsInstance(value["evidence"], str)

    def test_invalid_trial_is_invalid_for_every_applicable_check(self):
        case = scenario(["C1", "C3", "C9"])
        results = checks.evaluate(trial(status="invalid"), case)
        for check in ("C1", "C3", "C9"):
            self.assertEqual(results[check]["result"], "invalid", check)
        self.assertEqual(results["C2"]["result"], "not-applicable")
        self.assertIn("invalid", checks.RESULTS)

    def test_outer_change_fails_c8_even_when_not_listed(self):
        results = checks.evaluate(trial(outer_changed=True), scenario(["C1", "C9"]))
        self.assertEqual(results["C8"]["result"], "fail")
        self.assertEqual(checks.evaluate(trial(), scenario(["C1", "C9"]))["C8"]["result"], "not-applicable")
        blocked = checks.evaluate(trial(status="setup-blocked", outer_changed=True), scenario(["C1"]))
        self.assertEqual(blocked["C8"]["result"], "not-applicable")

    def test_uncaptured_trial_never_passes_or_fails(self):
        case = scenario(["C1", "C3", "C8"], allowed_globs=[])
        for status in ("inconclusive", "setup-blocked"):
            with self.subTest(status=status):
                results = checks.evaluate(trial(status=status, replies=[]), case)
                for check in ("C1", "C3", "C8"):
                    self.assertEqual(results[check]["result"], status)
                self.assertEqual(results["C2"]["result"], "not-applicable")


ADR = "docs/lusona/adr/20261020-member-export-format.md"
OLD_ADR = "docs/lusona/adr/0003-json-member-export.md"
ADR_TEXT = ("# ADR 20261020-member-export-format: Member export format\n\nCreated: 2026-10-20\n"
            "Updated: 2026-10-20\n\nStatus: accepted\nScope: member export\n")
OLD_ADR_TEXT = ("# ADR 0003: JSON member export\n\nDate: 2026-06-02\nStatus: superseded by "
                "[ADR 20261020](20261020-member-export-format.md) on 2026-10-20\n")


def fixture_case(checks_list, files=None, **expect):
    case = scenario(checks_list, **expect)
    case["files"] = dict(files or {})
    return case


class C12DecisionGateTest(unittest.TestCase):
    """C12: no edit that implements the contradicting requirement, and the accepted
    decision keeps its status, before the user answers."""
    case = fixture_case(["C12"], {ADR: ADR_TEXT, "export.py": "x"},
                        decision_protected_globs=["*.py", "tests/*"], decision_status={ADR: "accepted"})

    def test_inconclusive_without_protected_globs(self):
        self.assertEqual(checks.c12_decision_gate(trial(), fixture_case(["C12"]))["result"], "inconclusive")

    def test_pass_when_nothing_changed(self):
        self.assertEqual(checks.c12_decision_gate(trial(), self.case)["result"], "pass")

    def test_fail_when_a_protected_path_changed(self):
        for change in (changed(modified=["export.py"]), changed(added=["tests/test_json.py"]),
                       changed(deleted=["export.py"])):
            with self.subTest(change=change):
                outcome = checks.c12_decision_gate(trial(changed=change), self.case)
                self.assertEqual(outcome["result"], "fail")
                self.assertIn("before the user answered", outcome["evidence"])

    def test_pass_when_the_decision_record_notes_the_conflict_and_keeps_its_status(self):
        text = ADR_TEXT.replace("Status: accepted", "Status: accepted (conflict raised 2026-11-11, pending the user)")
        record = trial(changed=changed(modified=[ADR]), files={ADR: text})
        self.assertEqual(checks.c12_decision_gate(record, self.case)["result"], "pass")

    def test_a_proposed_revision_next_to_the_kept_state_passes(self):
        # P3 step 1 records the conflict in the owning record; "proposed" there names the revision, not the state.
        for status in ("Status: accepted; revision proposed, pending the user",
                       "Status: accepted (a revision is proposed on 2026-11-11)"):
            with self.subTest(status=status):
                text = ADR_TEXT.replace("Status: accepted", status)
                record = trial(changed=changed(modified=[ADR]), files={ADR: text})
                self.assertEqual(checks.c12_decision_gate(record, self.case)["result"], "pass")

    def test_fail_when_the_decision_status_changed_before_the_answer(self):
        for status in ("Status: superseded by [ADR 20261111](20261111-x.md)", "Status: accepted; superseded in part",
                       "**Status:** proposed"):
            with self.subTest(status=status):
                text = ADR_TEXT.replace("Status: accepted", status)
                record = trial(changed=changed(modified=[ADR]), files={ADR: text})
                self.assertEqual(checks.c12_decision_gate(record, self.case)["result"], "fail")

    def test_fail_when_the_decision_record_was_deleted_or_lost_its_status_line(self):
        self.assertEqual(checks.c12_decision_gate(trial(changed=changed(deleted=[ADR])), self.case)["result"], "fail")
        record = trial(changed=changed(modified=[ADR]), files={ADR: "# ADR\n\nNo status here.\n"})
        self.assertEqual(checks.c12_decision_gate(record, self.case)["result"], "fail")

    def test_status_is_optional(self):
        case = fixture_case(["C12"], decision_protected_globs=["*.py"])
        self.assertEqual(checks.c12_decision_gate(trial(changed=changed(modified=[ADR])), case)["result"], "pass")


class C14RevisionRecordedTest(unittest.TestCase):
    """C14 computed part: the owning decision record was added or modified."""
    case = fixture_case(["C14"], {ADR: ADR_TEXT, OLD_ADR: OLD_ADR_TEXT},
                        decision_record_globs=["docs/lusona/adr/2*.md"])

    def test_inconclusive_without_globs(self):
        self.assertEqual(checks.c14_revision_recorded(trial(), fixture_case(["C14"]))["result"], "inconclusive")

    def test_pass_when_the_decision_record_changed_or_a_new_decision_was_added(self):
        for change in (changed(modified=[ADR]), changed(added=["docs/lusona/adr/20261111-member-export-json.md"])):
            with self.subTest(change=change):
                self.assertEqual(checks.c14_revision_recorded(trial(changed=change), self.case)["result"], "pass")

    def test_fail_when_no_decision_record_changed(self):
        for change in (changed(), changed(modified=[OLD_ADR, "docs/lusona/work.md"]), changed(deleted=[ADR])):
            with self.subTest(change=change):
                self.assertEqual(checks.c14_revision_recorded(trial(changed=change), self.case)["result"], "fail")


class C15NotReinstatedTest(unittest.TestCase):
    """C15 computed part: a superseded record keeps its superseded status."""
    case = fixture_case(["C15"], {OLD_ADR: OLD_ADR_TEXT}, superseded_status={OLD_ADR: "superseded"})

    def test_inconclusive_without_superseded_records(self):
        self.assertEqual(checks.c15_not_reinstated(trial(), fixture_case(["C15"]))["result"], "inconclusive")

    def test_pass_when_unchanged_or_still_superseded(self):
        self.assertEqual(checks.c15_not_reinstated(trial(), self.case)["result"], "pass")
        text = OLD_ADR_TEXT + "Superseded by: [ADR 20261020](20261020-member-export-format.md)\n"
        record = trial(changed=changed(modified=[OLD_ADR]), files={OLD_ADR: text})
        self.assertEqual(checks.c15_not_reinstated(record, self.case)["result"], "pass")

    def test_a_proposal_note_does_not_change_the_superseded_state(self):
        text = OLD_ADR_TEXT.replace("on 2026-10-20", "on 2026-10-20; reinstatement proposed and declined 2026-11-11")
        record = trial(changed=changed(modified=[OLD_ADR]), files={OLD_ADR: text})
        self.assertEqual(checks.c15_not_reinstated(record, self.case)["result"], "pass")

    def test_fail_when_reinstated_or_deleted(self):
        for status in ("Status: accepted", "Status: accepted (reinstated 2026-11-11)",
                       "Status: superseded, reinstated as accepted"):
            with self.subTest(status=status):
                text = OLD_ADR_TEXT.replace(OLD_ADR_TEXT.splitlines()[3], status)
                record = trial(changed=changed(modified=[OLD_ADR]), files={OLD_ADR: text})
                outcome = checks.c15_not_reinstated(record, self.case)
                self.assertEqual(outcome["result"], "fail")
                self.assertIn(OLD_ADR, outcome["evidence"])
        deleted = trial(changed=changed(deleted=[OLD_ADR]))
        self.assertEqual(checks.c15_not_reinstated(deleted, self.case)["result"], "fail")


LEGACY = "docs/lusona/specs/0007-member-search.md"
OLD_FILES = {LEGACY: "# 0007\n", "docs/lusona/work.md": "# Work queue\n",
             "docs/lusona/history/2026-11-week-01.md": "# Work history\n",
             "docs/lusona/notes/member-search.md": "# Notes\n", "search.py": "x"}


class C16RecordsKeptTest(unittest.TestCase):
    """C16: old records keep their paths: none deleted or renamed, legacy records not migrated."""
    case = fixture_case(["C16"], OLD_FILES, old_record_globs=["docs/lusona/**"], legacy_records=[LEGACY])

    def test_inconclusive_without_globs(self):
        self.assertEqual(checks.c16_records_kept(trial(), fixture_case(["C16"]))["result"], "inconclusive")

    def test_pass_when_records_are_edited_in_place_or_new_records_added(self):
        change = changed(modified=[LEGACY, "docs/lusona/work.md"],
                         added=["docs/lusona/history/2026-11-week-02.md", "docs/lusona/specs/20261111-phone-search.md"])
        self.assertEqual(checks.c16_records_kept(trial(changed=change), self.case)["result"], "pass")

    def test_fail_when_an_old_record_is_deleted_or_renamed(self):
        for change in (changed(deleted=["docs/lusona/notes/member-search.md"]),
                       changed(deleted=[LEGACY], added=["docs/lusona/specs/20261103-member-search.md"])):
            with self.subTest(change=change):
                outcome = checks.c16_records_kept(trial(changed=change), self.case)
                self.assertEqual(outcome["result"], "fail")

    def test_fail_when_a_legacy_record_is_copied_to_a_new_id(self):
        change = changed(added=["docs/lusona/specs/20261111-member-search.md"])
        outcome = checks.c16_records_kept(trial(changed=change), self.case)
        self.assertEqual(outcome["result"], "fail")
        self.assertIn("20261111-member-search.md", outcome["evidence"])

    def test_deleting_a_file_outside_the_record_globs_is_left_to_c8(self):
        change = changed(deleted=["search.py"])
        self.assertEqual(checks.c16_records_kept(trial(changed=change), self.case)["result"], "pass")


class C17RecordsUpdatedTest(unittest.TestCase):
    """C17 computed part: each declared record glob matches an added or modified path."""
    case = fixture_case(["C17"], OLD_FILES,
                        update_globs=[LEGACY, "docs/lusona/work.md", "docs/lusona/history/*.md"])

    def test_inconclusive_without_globs(self):
        self.assertEqual(checks.c17_records_updated(trial(), fixture_case(["C17"]))["result"], "inconclusive")

    def test_pass_when_every_glob_matches_a_changed_record(self):
        change = changed(modified=[LEGACY, "docs/lusona/work.md"], added=["docs/lusona/history/2026-11-week-02.md"])
        self.assertEqual(checks.c17_records_updated(trial(changed=change), self.case)["result"], "pass")

    def test_fail_names_each_glob_without_an_update(self):
        change = changed(modified=["docs/lusona/work.md"], deleted=["docs/lusona/history/2026-11-week-01.md"])
        outcome = checks.c17_records_updated(trial(changed=change), self.case)
        self.assertEqual(outcome["result"], "fail")
        self.assertIn(LEGACY, outcome["evidence"])
        self.assertIn("docs/lusona/history/*.md", outcome["evidence"])


class PrincipleChecksEvaluateTest(unittest.TestCase):
    def test_new_checks_are_graded_only_when_listed(self):
        case = fixture_case(["C12", "C16"], OLD_FILES, decision_protected_globs=["*.py"],
                            old_record_globs=["docs/lusona/**"])
        results = checks.evaluate(trial(), case)
        self.assertEqual(results["C12"]["result"], "pass")
        self.assertEqual(results["C16"]["result"], "pass")
        for check in ("C14", "C15", "C17"):
            self.assertEqual(results[check]["result"], "not-applicable")
        self.assertNotIn("C13", results)
        blocked = checks.evaluate(trial(status="setup-blocked"), case)
        self.assertEqual(blocked["C12"]["result"], "setup-blocked")


class CombineTest(unittest.TestCase):
    def part(self, result):
        return {"result": result, "evidence": result}

    def test_pass_only_when_every_present_part_passes(self):
        self.assertEqual(checks.combine(self.part("pass"), self.part("pass"))["result"], "pass")
        self.assertEqual(checks.combine(self.part("pass"), None)["result"], "pass")
        self.assertEqual(checks.combine(None, self.part("pass"))["result"], "pass")

    def test_fail_dominates_then_weakest_non_pass_state(self):
        self.assertEqual(checks.combine(self.part("pass"), self.part("fail"))["result"], "fail")
        self.assertEqual(checks.combine(self.part("setup-blocked"), self.part("fail"))["result"], "fail")
        self.assertEqual(checks.combine(self.part("pass"), self.part("inconclusive"))["result"], "inconclusive")
        self.assertEqual(checks.combine(self.part("inconclusive"), self.part("setup-blocked"))["result"],
                         "setup-blocked")
        self.assertEqual(checks.combine(self.part("not-applicable"), self.part("pass"))["result"], "pass")
        self.assertEqual(checks.combine(self.part("not-applicable"), None)["result"], "not-applicable")
        # An invalid part (evaluator material accessed) outranks every other state.
        self.assertEqual(checks.combine(self.part("invalid"), self.part("fail"))["result"], "invalid")
        self.assertEqual(checks.combine(self.part("pass"), self.part("invalid"))["result"], "invalid")
        # A not-applicable computed part is absent: the judged part decides.
        self.assertEqual(checks.combine(self.part("not-applicable"), self.part("fail"))["result"], "fail")
        self.assertEqual(checks.combine(self.part("not-applicable"), self.part("inconclusive"))["result"],
                         "inconclusive")


if __name__ == "__main__":
    unittest.main()
