import importlib.util
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCRATCH = ROOT / "tmp/loop-conformance-build"

spec = importlib.util.spec_from_file_location("loop_conformance_run", HERE / "run.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

CLAUDE_VERSION = "2.1.321 (Claude Code)"
CODEX_VERSION = "codex-cli 0.167.0"

SCENARIOS = {
    "explore-a": {
        "skill": "explore",
        "files": {"docs/lusona/README.md": "# Project\n", "app.py": "print('x')\n"},
        "turns": ["What storage should we use?", "What would you do?"],
        "checks": ["C1", "C2", "C7", "C8", "C9", "C10"],
        "expect": {"record_globs": ["docs/lusona/notes/*.md"], "allowed_globs": ["docs/lusona/**"],
                   "expect_workers": True, "expect_reviewer": True},
    },
    "greet": {"skill": "explore", "files": {"README.md": "hi\n"}, "turns": ["Hello"], "checks": ["C4"], "expect": {}},
}
RUBRIC = """# Rubric preamble

Grade each criterion as pass, fail, or inconclusive.

## explore-a

### C1.concrete

Required: a named next step and owner.

### C7.continues

Required: continues without asking for a command.

## greet

No judged criterion.

## other

### C2.content

SECRET-OTHER-SECTION
"""
GOOD_REPLY = ("**Result** ✅ Complete\n\n**Evidence**\n\nSaved notes.\n\n"
              "| Next action | Owner | Needs | Authority |\n| --- | --- | --- | --- |\n| Decide | User | - | - |\n")


def init_event(session, plugin_path):
    return {"type": "system", "subtype": "init", "session_id": session, "model": "test-model",
            "permissionMode": "dontAsk", "mcp_servers": [], "tools": ["Task", "Read"],
            "plugins": [{"name": "lusona", "path": plugin_path, "source": "lusona@inline"},
                        {"name": "cc-plugin-telemetry", "path": "builtin"}]}


def result_event(session, text, denials=()):
    return {"type": "result", "subtype": "success", "is_error": False, "session_id": session, "result": text,
            "usage": {"output_tokens": 10}, "total_cost_usd": 0.01, "permission_denials": list(denials),
            "subagent_stats": {"spawned": 1}}


def jsonl(*events):
    return "\n".join(json.dumps(e) for e in events) + "\n"


class FakeHost:
    """Records calls and answers --version; each turn is a callable(args, kwargs) -> stdout."""

    def __init__(self, turns, version=CLAUDE_VERSION, judge_stdout=None):
        self.turns, self.version, self.calls, self.judge_stdout = list(turns), version, [], judge_stdout

    def __call__(self, args, **kwargs):
        if args[-1] == "--version":
            version = self.version if args[0] != "claude" else CLAUDE_VERSION if self.version.startswith("codex") else self.version
            return subprocess.CompletedProcess(args, 0, version + "\n", "")
        self.calls.append((args, kwargs))
        if "--output-format" in args and args[args.index("--output-format") + 1] == "json":
            return subprocess.CompletedProcess(args, 0, self.judge_stdout, "")
        turn = self.turns.pop(0)
        return turn(args, kwargs)


class RunnerTestBase(unittest.TestCase):
    host = "claude"

    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.temp = pathlib.Path(tempfile.mkdtemp(prefix="test-", dir=SCRATCH))
        self.addCleanup(shutil.rmtree, self.temp, True)
        self.suite = self.temp / "suite"
        self.suite.mkdir()
        (self.suite / "scenarios.json").write_text(json.dumps(SCENARIOS, indent=2))
        (self.suite / "rubric.md").write_text(RUBRIC)
        lock = {n: runner.digest(self.suite / n) for n in ("scenarios.json", "rubric.md")}
        (self.suite / "suite.lock.json").write_text(json.dumps(lock))
        self.plugin = self.temp / "source-plugin"
        (self.plugin / "skills/explore").mkdir(parents=True)
        (self.plugin / "skills/explore/SKILL.md").write_text("# Explore\n")
        (self.plugin / "scripts").mkdir()
        (self.plugin / "scripts/work-record.sh").write_text("#!/bin/sh\n")
        self.work_root = self.temp / "work"
        self.condition = self.temp / "condition"
        self.outer = ["clean", "clean"]

    def guard(self, path):
        return pathlib.Path(path).resolve()

    def outer_status(self):
        return self.outer.pop(0)

    def freeze(self, version=None, home=None):
        version = version or (CLAUDE_VERSION if self.host == "claude" else CODEX_VERSION)
        return runner.freeze(self.plugin, self.condition, self.host, "test-model", "high", 30, "judge-model",
                             "medium", suite_dir=self.suite, executor=FakeHost([], version), home=home or self.temp,
                             environ={})

    def prepare(self, scenario="explore-a", trial=1, name="trial"):
        return runner.prepare(self.condition, scenario, trial, self.temp / name, self.work_root, guard=self.guard)

    def run_trial(self, trial_dir, host):
        return runner.run_trial(trial_dir, executor=host, outer_status=self.outer_status, home=self.temp, environ={})


class WorkRootTest(unittest.TestCase):
    def test_refuses_repository_and_system_tmp(self):
        with self.assertRaisesRegex(ValueError, "CLAUDE.md|AGENTS.md"):
            runner.check_work_root(ROOT / "tmp/loop-conformance-build/work")
        with self.assertRaisesRegex(ValueError, "temporary"):
            runner.check_work_root("/tmp/lusona-evals")

    def test_accepts_cache_directory_without_instruction_ancestors(self):
        home = pathlib.Path.home()
        if any((d / n).exists() for d in (home, *home.parents) for n in ("CLAUDE.md", "AGENTS.md")):
            self.skipTest("home directory has an instruction file ancestor")
        path = home / ".cache/lusona-evals/never-created"
        self.assertEqual(runner.check_work_root(path), path.resolve())
        self.assertFalse(path.exists())

    def test_default_work_root_uses_xdg_cache_home(self):
        old = os.environ.get("XDG_CACHE_HOME")
        os.environ["XDG_CACHE_HOME"] = "/srv/cache"
        try:
            self.assertEqual(runner.default_work_root(), pathlib.Path("/srv/cache/lusona-evals"))
        finally:
            if old is None:
                del os.environ["XDG_CACHE_HOME"]
            else:
                os.environ["XDG_CACHE_HOME"] = old


class SuiteContentTest(unittest.TestCase):
    def test_repository_scenarios_and_rubric_are_valid(self):
        scenarios, rubric = HERE / "scenarios.json", HERE / "rubric.md"
        if not scenarios.exists() or not rubric.exists():
            self.skipTest("suite content not present")
        data = json.loads(scenarios.read_text())
        self.assertEqual(runner.validate_scenarios(data, rubric.read_text()), [])
        self.assertGreaterEqual(len(data), 10)
        covered = {c for case in data.values() for c in case["checks"]}
        self.assertEqual(covered, set(runner.CHECK_IDS))

    def test_repository_calibration_cases_name_rubric_criteria(self):
        cases, rubric = HERE / "judge-calibration.json", HERE / "rubric.md"
        if not cases.exists() or not rubric.exists():
            self.skipTest("suite content not present")
        text = rubric.read_text()
        for case in json.loads(cases.read_text()):
            with self.subTest(case=case.get("id")):
                self.assertIn(case["criterion"], runner.rubric_criteria(runner.rubric_section(text, case["scenario"])))
                self.assertIn(case["expected"], ("pass", "fail"))
                self.assertIsInstance(case["replies"], list)

    def test_rubric_parsing(self):
        self.assertEqual(runner.rubric_criteria(runner.rubric_section(RUBRIC, "explore-a")),
                         ["C1.concrete", "C7.continues"])
        self.assertEqual(runner.rubric_criteria(runner.rubric_section(RUBRIC, "greet")), [])
        self.assertIsNone(runner.rubric_section(RUBRIC, "missing"))
        self.assertNotIn("##", runner.rubric_preamble(RUBRIC))

    def test_validation_accepts_boolean_spec_required_only(self):
        good = {"x": {"skill": "specify", "files": {}, "turns": ["hi"], "checks": ["C6"],
                      "expect": {"spec_required": True}}}
        self.assertEqual(runner.validate_scenarios(good), [])
        bad = {"x": {"skill": "specify", "files": {}, "turns": ["hi"], "checks": ["C6"],
                     "expect": {"spec_required": "yes"}}}
        self.assertTrue(any("spec_required" in p for p in runner.validate_scenarios(bad)))
        missing = {"x": {"skill": "implement", "files": {}, "turns": ["hi"], "checks": ["C10", "C11"], "expect": {}}}
        problems = runner.validate_scenarios(missing)
        self.assertTrue(any("C10 needs expect.expect_reviewer" in p for p in problems), problems)
        self.assertTrue(any("C11 needs expect.expect_workers" in p for p in problems), problems)

    def test_ignored_paths(self):
        for path in (".git/HEAD", "pkg/__pycache__/m.pyc", ".pytest_cache/v/cache/nodeids", "x.pyc"):
            self.assertTrue(runner.ignored(path), path)
        self.assertFalse(runner.ignored("docs/lusona/notes/pytest_cache.md"))

    def test_validation_reports_missing_expectations(self):
        bad = {"x": {"skill": "explore", "files": {}, "turns": ["hi"], "checks": ["C2", "C11"], "expect": {}}}
        problems = runner.validate_scenarios(bad, RUBRIC)
        self.assertTrue(any("record_globs" in p for p in problems))
        self.assertTrue(any("C11" in p for p in problems))
        self.assertTrue(any("rubric" in p for p in problems))


    def test_validation_requires_expectations_of_the_principle_checks(self):
        bad = {"x": {"skill": "implement", "files": {}, "turns": ["hi"],
                     "checks": ["C12", "C13", "C14", "C15", "C16", "C17"], "expect": {}}}
        problems = runner.validate_scenarios(bad, RUBRIC.replace("## other", "## x\n\nNo judged criterion.\n\n## other"))
        for needed in ("C12 needs expect.decision_protected_globs", "C14 needs expect.decision_record_globs",
                       "C15 needs expect.superseded_status", "C16 needs expect.old_record_globs",
                       "C17 needs expect.update_globs", "C13 needs a judged criterion"):
            self.assertTrue(any(needed in p for p in problems), (needed, problems))
        wrong = {"x": {"skill": "implement", "files": {}, "turns": ["hi"], "checks": ["C12", "C15", "C16"],
                       "expect": {"decision_protected_globs": ["*.py"], "decision_status": ["accepted"],
                                  "superseded_status": {}, "old_record_globs": ["docs/**"],
                                  "legacy_records": "docs/lusona/specs/0001-a.md"}}}
        problems = runner.validate_scenarios(wrong)
        for needed in ("expect.decision_status", "expect.superseded_status", "expect.legacy_records"):
            self.assertTrue(any(needed in p for p in problems), (needed, problems))
        good = {"x": {"skill": "implement", "files": {}, "turns": ["hi"], "checks": ["C12", "C14", "C15", "C16", "C17"],
                      "expect": {"decision_protected_globs": ["*.py"], "decision_status": {"a.md": "accepted"},
                                 "decision_record_globs": ["docs/lusona/adr/*.md"],
                                 "superseded_status": {"b.md": "superseded"}, "old_record_globs": ["docs/**"],
                                 "legacy_records": ["docs/lusona/specs/0001-a.md"], "update_globs": ["docs/**"]}}}
        self.assertEqual(runner.validate_scenarios(good), [])

    def test_pass_marks_validation(self):
        marks = {"marks": [{"scenario": "explore-a", "check": "C2", "trials": 5,
                            "min_pass": {"claude": 4, "codex": 4}, "reason": "Judged content."}]}
        self.assertEqual(runner.validate_pass_marks(marks, SCENARIOS), [])
        bad = {"marks": [{"scenario": "explore-a", "check": "C4", "trials": 5, "min_pass": {"claude": 6}, "reason": ""},
                         {"scenario": "missing", "check": "C1", "trials": 5,
                          "min_pass": {"claude": 1, "codex": 1}, "reason": "x"}]}
        problems = runner.validate_pass_marks(bad, SCENARIOS)
        for needed in ("explore-a C4: check not listed", "explore-a C4: min_pass.claude", "explore-a C4: min_pass.codex",
                       "explore-a C4: reason", "missing C1: unknown scenario"):
            self.assertTrue(any(needed in p for p in problems), (needed, problems))
        duplicate = {"marks": marks["marks"] * 2}
        self.assertTrue(any("duplicate" in p for p in runner.validate_pass_marks(duplicate, SCENARIOS)))

    def test_repository_pass_marks_cover_the_principle_scenarios(self):
        path, scenarios = HERE / "pass-marks.json", HERE / "scenarios.json"
        data, cases = json.loads(path.read_text()), json.loads(scenarios.read_text())
        self.assertEqual(runner.validate_pass_marks(data, cases), [])
        marked = {(m["scenario"], m["check"]) for m in data["marks"]}
        for sid in ("decision-conflict", "decision-revised", "old-records"):
            for check in cases[sid]["checks"]:
                self.assertIn((sid, check), marked)
        self.assertIn("pass-marks.json", json.loads((HERE / "suite.lock.json").read_text()))
        self.assertIn("pass-marks.json", runner.EVALUATOR_NAMES)

class FreezeAndPrepareTest(RunnerTestBase):
    def test_freeze_records_condition_and_detects_mutation(self):
        self.freeze()
        data = runner.load_condition(self.condition)
        self.assertEqual(data["cli_version"], CLAUDE_VERSION)
        self.assertEqual(data["ambient_instruction_hashes"], {})
        self.assertEqual(data["judge_prompt_sha256"], runner.JUDGE_PROMPT_SHA256)
        self.assertEqual(data["allowed_tools"], ["Read", "Edit", "Write", "Skill", "Task", "Agent", "Bash"])
        self.assertTrue(data["claude_settings"]["sandbox"]["enabled"])
        self.assertFalse(data["claude_settings"]["sandbox"]["allowUnsandboxedCommands"])
        self.assertTrue(data["claude_settings"]["permissions"]["blockWritesOutsideWorkingDirectories"])
        self.assertEqual(data["permission_config"]["settings"], data["claude_settings"])
        self.assertEqual(data["permission_config"]["shell_env"], {"CLAUDE_CODE_SHELL": "/bin/bash"})
        self.assertEqual(data["shell_env"], {"CLAUDE_CODE_SHELL": "/bin/bash"})
        self.assertNotIn(str(self.condition), json.dumps(data["permission_config"]),
                         "permission_config must not depend on the condition path")
        self.assertEqual(set(data["suite_hashes"]), {"scenarios.json", "rubric.md", "suite.lock.json"})
        (self.condition / "plugin/skills/explore/SKILL.md").write_text("changed")
        with self.assertRaisesRegex(ValueError, "plugin changed"):
            runner.load_condition(self.condition)

    def test_freeze_refuses_lock_mismatch(self):
        (self.suite / "rubric.md").write_text(RUBRIC + "\nedited\n")
        with self.assertRaisesRegex(ValueError, "suite.lock.json"):
            self.freeze()
        self.assertFalse(self.condition.exists(), "a refused freeze leaves no condition directory")

    def test_freeze_refuses_invalid_pass_marks(self):
        (self.suite / "pass-marks.json").write_text(json.dumps(
            {"marks": [{"scenario": "greet", "check": "C1", "trials": 5, "min_pass": {"claude": 5, "codex": 5},
                        "reason": "x"}]}))
        lock = json.loads((self.suite / "suite.lock.json").read_text())
        lock["pass-marks.json"] = runner.digest(self.suite / "pass-marks.json")
        (self.suite / "suite.lock.json").write_text(json.dumps(lock))
        with self.assertRaisesRegex(ValueError, "pass-marks.json"):
            self.freeze()
        self.assertFalse(self.condition.exists())

    def test_codex_ambient_agents_file_is_hashed_through_symlink(self):
        self.host = "codex"
        home = self.temp / "home"
        (home / ".codex").mkdir(parents=True)
        (home / "shared").mkdir()
        (home / "shared/AGENTS.md").write_text("global rules\n")
        (home / ".codex/AGENTS.md").symlink_to(home / "shared/AGENTS.md")
        self.freeze(home=home)
        data = runner.load_condition(self.condition)
        target = str((home / "shared/AGENTS.md").resolve())
        self.assertEqual(data["ambient_instruction_hashes"], {target: runner.digest(home / "shared/AGENTS.md")})
        self.assertIsNone(data["allowed_tools"])

    def test_prepare_creates_committed_fixture_outside_trial_dir(self):
        self.freeze()
        trial_dir = self.prepare()
        meta = json.loads((trial_dir / "run.json").read_text())
        workspace = pathlib.Path(meta["workspace"])
        self.assertTrue(workspace.is_relative_to(self.work_root.resolve()))
        self.assertEqual(meta["initial_commits"], 1)
        self.assertEqual(sorted(meta["initial_hashes"]), ["app.py", "docs/lusona/README.md"])
        self.assertFalse((workspace / "rubric.md").exists())
        self.assertFalse((workspace / "AGENTS.md").exists())
        self.assertEqual(runner.git(workspace, "config", "commit.gpgsign").stdout.strip(), "false")
        first = (trial_dir / "turn-1.input.txt").read_text()
        self.assertEqual(first, "/lusona:explore What storage should we use?\n")
        self.assertEqual((trial_dir / "turn-2.input.txt").read_text(), "What would you do?\n")
        for trial in (2, 5):
            self.prepare(trial=trial, name=f"t{trial}")
        with self.assertRaisesRegex(ValueError, "between 1 and 5"):
            self.prepare(trial=6, name="t6")
        with self.assertRaises(FileExistsError):
            self.prepare()

    def test_prepare_refuses_output_inside_work_root(self):
        self.freeze()
        with self.assertRaisesRegex(ValueError, "outside the work root"):
            runner.prepare(self.condition, "greet", 1, self.work_root / "trial", self.work_root, guard=self.guard)

    def test_codex_first_turn_points_at_frozen_skill_without_rubric(self):
        self.host = "codex"
        self.freeze()
        first = (self.prepare() / "turn-1.input.txt").read_text()
        self.assertIn(f"{self.condition}/plugin/skills/explore/SKILL.md", first)
        self.assertTrue(first.endswith("What storage should we use?\n"))
        self.assertNotIn("rubric", first.lower())


class ClaudeRunTest(RunnerTestBase):
    def test_two_turns_resume_one_session_and_record_evidence(self):
        self.freeze()
        trial_dir = self.prepare()
        workspace = pathlib.Path(json.loads((trial_dir / "run.json").read_text())["workspace"])
        plugin = str(self.condition / "plugin")

        def turn1(args, kwargs):
            (workspace / "__pycache__").mkdir()
            (workspace / "__pycache__/app.cpython-314.pyc").write_bytes(b"\0")
            task = {"type": "assistant", "parent_tool_use_id": None, "message": {"content": [
                {"type": "tool_use", "id": "t1", "name": "Task",
                 "input": {"description": "Review the notes", "prompt": "Check the draft"}}]}}
            nested = {"type": "assistant", "parent_tool_use_id": "t1", "message": {"content": [
                {"type": "tool_use", "id": "t2", "name": "Task", "input": {"description": "nested"}}]}}
            writer = {"type": "assistant", "parent_tool_use_id": None, "message": {"content": [
                {"type": "tool_use", "id": "t0", "name": "Agent",
                 "input": {"description": "Draft the notes", "prompt": "Write a draft for later review"}}]}}
            return subprocess.CompletedProcess(args, 0, jsonl(init_event("s-1", plugin), writer, task, task, nested,
                                                              result_event("s-1", "First reply")), "")

        def turn2(args, kwargs):
            (workspace / "docs/lusona/notes").mkdir(parents=True)
            (workspace / "docs/lusona/notes/storage.md").write_text("# Storage\n")
            denial = {"tool_name": "Bash", "tool_use_id": "b1", "tool_input": {"command": "git push"}}
            return subprocess.CompletedProcess(args, 0, jsonl(init_event("s-1", plugin),
                                                              result_event("s-1", GOOD_REPLY, [denial])), "")

        host = FakeHost([turn1, turn2])
        trial = self.run_trial(trial_dir, host)
        first_args, first_kwargs = host.calls[0]
        second_args, _ = host.calls[1]
        self.assertNotIn("--resume", first_args)
        self.assertEqual(second_args[second_args.index("--resume") + 1], "s-1")
        for flag in ("--setting-sources", "--strict-mcp-config", "--plugin-dir"):
            self.assertIn(flag, first_args)
        self.assertEqual(json.loads(first_args[first_args.index("--settings") + 1]),
                         json.loads((self.condition / "condition.json").read_text())["claude_settings"])
        self.assertEqual(first_args[first_args.index("--permission-mode") + 1], "dontAsk")
        self.assertEqual(first_args[first_args.index("--allowedTools") + 1:], trial_cond_tools(self.condition))
        self.assertEqual(first_kwargs["cwd"], workspace)
        self.assertEqual(first_kwargs["input"], "/lusona:explore What storage should we use?\n")
        self.assertEqual(first_kwargs["env"]["CLAUDE_CODE_SHELL"], "/bin/bash")
        self.assertFalse(any(k.startswith("CLAUDE_CODE_") and k not in runner.KEEP_ENV | {"CLAUDE_CODE_SHELL"}
                             for k in first_kwargs["env"]))
        self.assertEqual(trial["status"], "captured")
        self.assertEqual(trial["replies"], ["First reply", GOOD_REPLY])
        self.assertEqual(trial["changed"], {"added": ["docs/lusona/notes/storage.md"], "modified": [], "deleted": []})
        self.assertEqual(trial["files"], {"docs/lusona/notes/storage.md": "# Storage\n"})
        self.assertEqual(trial["commits_added"], 0)
        self.assertFalse(trial["outer_changed"])
        self.assertEqual(trial["workers"], 2)
        self.assertTrue(trial["reviewer_seen"])
        self.assertEqual(trial["denied_actions"][0]["tool_input"]["command"], "git push")
        self.assertEqual(sorted(trial["capture"]["hashes_before"]), ["app.py", "docs/lusona/README.md"])
        self.assertIn("docs/lusona/notes/storage.md", trial["capture"]["hashes_after"])
        self.assertNotIn("__pycache__/app.cpython-314.pyc", trial["capture"]["hashes_after"])
        for name in ("turn-1.stdout.jsonl", "turn-2.stderr.txt", "turn-2.result.json", "workspace-git-log.txt",
                     "artifacts/docs/lusona/notes/storage.md"):
            self.assertTrue((trial_dir / name).exists(), name)
        computed = runner.grade(trial_dir)
        for check in ("C1", "C2", "C8", "C9", "C10"):
            self.assertEqual(computed[check]["result"], "pass", (check, computed[check]))
        with self.assertRaisesRegex(ValueError, "never retried"):
            self.run_trial(trial_dir, FakeHost([]))

    def test_code_change_after_freeze_blocks_capture_but_not_grading(self):
        from unittest import mock
        self.freeze()
        trial_dir = self.prepare(scenario="greet")
        plugin = str(self.condition / "plugin")
        self.run_trial(trial_dir, FakeHost([lambda a, k: subprocess.CompletedProcess(
            a, 0, jsonl(init_event("s", plugin), result_event("s", "Hi")), "")]))
        changed = dict(runner.code_hashes(), **{"checks.py": "different"})
        with mock.patch.object(runner, "code_hashes", return_value=changed):
            with self.assertRaisesRegex(ValueError, "changed after freeze"):
                self.prepare(scenario="greet", trial=2, name="second")
            self.assertEqual(runner.grade(trial_dir)["C4"]["result"], "pass")
            runner.report(trial_dir, self.temp / "report")
        self.assertIn("checks.py changed after the condition was frozen", (self.temp / "report/report.md").read_text())

    def test_session_cost_is_last_cumulative_total(self):
        # Pilot evidence: turn 1 total 0.2885; resumed turn 2 total 0.3748 = 0.2885 + 0.0863 (since last result).
        self.freeze()
        trial_dir = self.prepare()
        plugin = str(self.condition / "plugin")

        def turn(total, since, text):
            event = result_event("s-1", text)
            event.update({"total_cost_usd": total, "model_usage_since_last_result": {"m": {"costUSD": since}}})
            return lambda a, k: subprocess.CompletedProcess(a, 0, jsonl(init_event("s-1", plugin), event), "")

        trial = self.run_trial(trial_dir, FakeHost([turn(0.2885, 0.2885, "one"), turn(0.3748, 0.0863, GOOD_REPLY)]))
        self.assertEqual(trial["cost_usd"], 0.3748)
        self.assertEqual([t["turn_cost_usd"] for t in trial["capture"]["turns"]], [0.2885, 0.0863])
        runner.grade(trial_dir)
        runner.report(trial_dir, self.temp / "report")
        rows = json.loads((self.temp / "report/report-trials.json").read_text())
        self.assertEqual(rows[0]["cost_usd"], 0.3748)

    def test_plugin_path_mismatch_blocks_and_stops(self):
        self.freeze()
        trial_dir = self.prepare()

        def wrong_plugin(args, kwargs):
            return subprocess.CompletedProcess(args, 0, jsonl(init_event("s-1", "/elsewhere/plugin"),
                                                              result_event("s-1", GOOD_REPLY)), "")

        host = FakeHost([wrong_plugin, wrong_plugin])
        trial = self.run_trial(trial_dir, host)
        self.assertEqual(trial["status"], "setup-blocked")
        self.assertEqual(len(host.calls), 1)
        computed = runner.grade(trial_dir)
        self.assertEqual(computed["C1"]["result"], "setup-blocked")
        self.assertEqual(computed["C4"]["result"], "not-applicable")

    def test_timeout_is_inconclusive_and_launch_failure_is_setup_blocked(self):
        self.freeze()

        def timeout(args, kwargs):
            raise subprocess.TimeoutExpired(args, 30, output='{"type": "system"}\n', stderr="partial")

        def missing(args, kwargs):
            raise FileNotFoundError("claude not found")

        timed = self.run_trial(self.prepare(name="timed"), FakeHost([timeout]))
        self.outer = ["clean", "clean"]
        blocked = self.run_trial(self.prepare(name="blocked"), FakeHost([missing]))
        self.assertEqual(timed["status"], "inconclusive")
        self.assertIn("partial", (self.temp / "timed/turn-1.stderr.txt").read_text())
        self.assertEqual(blocked["status"], "setup-blocked")

    def test_failed_result_after_start_is_inconclusive(self):
        self.freeze()

        def error(args, kwargs):
            event = result_event("s-1", "API error")
            event.update({"subtype": "error_during_execution", "is_error": True})
            return subprocess.CompletedProcess(args, 1, jsonl(init_event("s-1", str(self.condition / "plugin")), event), "")

        self.assertEqual(self.run_trial(self.prepare(), FakeHost([error]))["status"], "inconclusive")

    def test_cli_version_change_blocks_before_any_turn(self):
        self.freeze()
        host = FakeHost([], version="2.1.999 (Claude Code)")
        trial = self.run_trial(self.prepare(), host)
        self.assertEqual(trial["status"], "setup-blocked")
        self.assertEqual(host.calls, [])
        self.assertIn("differs", trial["capture"]["error"])

    def test_duplicate_plugin_entry_or_model_mismatch_blocks(self):
        self.freeze()
        plugin = str(self.condition / "plugin")

        def twice(args, kwargs):
            event = init_event("s", plugin)
            event["plugins"].append({"name": "lusona", "path": "/elsewhere/plugin"})
            return subprocess.CompletedProcess(args, 0, jsonl(event, result_event("s", "Hi")), "")

        def other_model(args, kwargs):
            event = init_event("s", plugin)
            event["model"] = "claude-haiku-5-5"
            return subprocess.CompletedProcess(args, 0, jsonl(event, result_event("s", "Hi")), "")

        self.assertEqual(self.run_trial(self.prepare(scenario="greet", name="twice"), FakeHost([twice]))["status"],
                         "setup-blocked")
        self.outer = ["clean", "clean"]
        blocked = self.run_trial(self.prepare(scenario="greet", name="model"), FakeHost([other_model]))
        self.assertEqual(blocked["status"], "setup-blocked")
        self.assertIn("model", json.loads((self.temp / "model/turn-1.result.json").read_text())["error"])

    def test_review_word_after_underscore_or_hyphen_is_a_reviewer(self):
        for value in ("review", "reviewer", "Code-review", "review_delete", "delete_review", "Delete_Review"):
            with self.subTest(value=value):
                self.assertTrue(runner._mentions_review(value))
        for value in ("preview", "PREVIEW", "page_preview", "interview"):
            with self.subTest(value=value):
                self.assertFalse(runner._mentions_review(value))
        agent = jsonl({"type": "assistant", "parent_tool_use_id": None, "message": {"content": [
            {"type": "tool_use", "id": "a1", "name": "Agent",
             "input": {"description": "Run delete_review checks", "subagent_type": "general-purpose"}}]}})
        parsed = runner.parse_claude(agent, "/p")
        self.assertEqual((parsed["reviewer_seen"], parsed["work_workers"]), (True, 0))

    def test_reviewer_detection_uses_description_and_type_only(self):
        def agent(**data):
            return jsonl({"type": "assistant", "parent_tool_use_id": None, "message": {"content": [
                {"type": "tool_use", "id": "a1", "name": "Agent", "input": data}]}})

        implementer = agent(description="Implement AC2", subagent_type="general-purpose",
                            prompt="Write the code; it will get an independent review later.")
        self.assertFalse(runner.parse_claude(implementer, "/p")["reviewer_seen"])
        self.assertFalse(runner.parse_claude(agent(description="Preview the page"), "/p")["reviewer_seen"])
        self.assertTrue(runner.parse_claude(agent(description="x", subagent_type="code-reviewer"), "/p")["reviewer_seen"])
        self.assertTrue(runner.parse_claude(agent(description="Review the diff"), "/p")["reviewer_seen"])

    def test_explore_subagent_is_never_a_reviewer(self):
        events = [{"type": "assistant", "parent_tool_use_id": None, "message": {"content": [
            {"type": "tool_use", "id": "a1", "name": "Agent",
             "input": {"description": "Implement AC2", "subagent_type": "general-purpose"}},
            {"type": "tool_use", "id": "a2", "name": "Agent",
             "input": {"description": "Review existing tests", "subagent_type": "Explore"}}]}}]
        parsed = runner.parse_claude(jsonl(*events), "/p")
        self.assertEqual((parsed["workers"], parsed["reviewer_seen"]), (2, False))
        self.assertEqual(parsed["work_workers"], 1, "the implementer counts; the Explore subagent does not")
        case = {"checks": ["C10"], "expect": {"expect_workers": True, "expect_reviewer": True}}
        record = {"workers": parsed["workers"], "reviewer_seen": parsed["reviewer_seen"]}
        self.assertEqual(runner.checks.c10_reviewer(record, case)["result"], "fail")

    def test_turn_texts_keep_every_root_text_block(self):
        self.freeze()
        trial_dir = self.prepare(scenario="greet")
        plugin = str(self.condition / "plugin")
        texts = [{"type": "assistant", "parent_tool_use_id": None, "message": {"content": [{"type": "text", "text": t}]}}
                 for t in ("First I read the notes.", "Final answer.")]
        nested = {"type": "assistant", "parent_tool_use_id": "w", "message": {"content": [{"type": "text", "text": "worker"}]}}
        host = FakeHost([lambda a, k: subprocess.CompletedProcess(
            a, 0, jsonl(init_event("s", plugin), texts[0], nested, texts[1], result_event("s", "Final answer.")), "")])
        trial = self.run_trial(trial_dir, host)
        self.assertEqual(trial["turn_texts"], [["First I read the notes.", "Final answer."]])
        self.assertEqual(trial["replies"], ["Final answer."])
        prompt = runner.build_judge_prompt(RUBRIC, "explore-a", ["C1.concrete"], ["Hello"], trial["turn_texts"],
                                           trial["changed"], trial["files"])
        self.assertIn("Actor message 1 of turn 1\n\nFirst I read the notes.", prompt)
        self.assertIn("Actor message 2 of turn 1\n\nFinal answer.", prompt)

    def git_trial(self, name, operation):
        trial_dir = self.prepare(scenario="greet", name=name)
        workspace = pathlib.Path(json.loads((trial_dir / "run.json").read_text())["workspace"])
        plugin = str(self.condition / "plugin")

        def call(args, kwargs):
            operation(workspace)
            return subprocess.CompletedProcess(args, 0, jsonl(init_event("s", plugin), result_event("s", "Hi")), "")

        self.outer = ["clean", "clean"]
        return self.run_trial(trial_dir, FakeHost([call]))

    def test_new_commits_are_counted_and_ref_only_changes_are_not(self):
        self.freeze()
        worktree = self.temp / "wt"

        def amend(ws):
            runner.git(ws, "commit", "--quiet", "--amend", "--allow-empty", "-m", "amended")

        def side_branch(ws):
            runner.git(ws, "switch", "--quiet", "-c", "side")
            runner.git(ws, "commit", "--quiet", "--allow-empty", "-m", "side")
            runner.git(ws, "switch", "--quiet", "-")

        def in_worktree(ws):
            runner.git(ws, "worktree", "add", "--quiet", "-b", "wt", str(worktree))
            runner.git(worktree, "commit", "--quiet", "--allow-empty", "-m", "worktree")

        def reset_away(ws):
            runner.git(ws, "commit", "--quiet", "--allow-empty", "-m", "removed later")
            runner.git(ws, "reset", "--quiet", "--hard", "HEAD~1")

        def stash(ws):
            (ws / "README.md").write_text("stashed edit\n")
            runner.git(ws, "stash", "--quiet")

        def detached_worktree(ws):
            runner.git(ws, "worktree", "add", "--quiet", "--detach", str(self.temp / "wt-detached"))
            runner.git(self.temp / "wt-detached", "commit", "--quiet", "--allow-empty", "-m", "detached")

        cases = [("amend", amend, 1, True), ("side", side_branch, 1, True), ("worktree", in_worktree, 1, True),
                 ("detached", detached_worktree, 1, False),
                 ("reset", reset_away, 1, False),
                 ("branch", lambda ws: runner.git(ws, "branch", "keep"), 0, True),
                 ("tag", lambda ws: runner.git(ws, "tag", "v1"), 0, True),
                 ("stash", stash, 0, True),
                 ("gc", lambda ws: runner.git(ws, "gc", "--quiet"), 0, False),
                 ("none", lambda ws: None, 0, False)]
        case = {"skill": "explore", "files": {}, "turns": ["x"], "checks": ["C8"], "expect": {"allowed_globs": []}}
        for name, operation, added, refs in cases:
            with self.subTest(name=name):
                trial = self.git_trial(name, operation)
                self.assertEqual(trial["commits_added"], added)
                self.assertEqual(trial["refs_changed"], refs)
                self.assertEqual(runner.checks.c8_scope(trial, case)["result"], "fail" if added else "pass")

    def test_actor_commit_and_outer_change_are_recorded(self):
        self.freeze()
        trial_dir = self.prepare(scenario="greet")
        workspace = pathlib.Path(json.loads((trial_dir / "run.json").read_text())["workspace"])
        plugin = str(self.condition / "plugin")

        def commit(args, kwargs):
            (workspace / "README.md").write_text("changed\n")
            runner.git(workspace, "commit", "--quiet", "-am", "actor commit")
            return subprocess.CompletedProcess(args, 0, jsonl(init_event("s", plugin), result_event("s", "Hi")), "")

        self.outer = ["clean", " M README.md"]
        trial = self.run_trial(trial_dir, FakeHost([commit]))
        self.assertEqual(trial["commits_added"], 1)
        self.assertTrue(trial["outer_changed"])
        self.assertEqual(trial["changed"]["modified"], ["README.md"])
        self.assertIn("actor commit", (trial_dir / "workspace-git-log.txt").read_text())


class OutputLocationTest(RunnerTestBase):
    def test_outputs_inside_the_repository_must_be_git_ignored(self):
        self.assertEqual(runner.check_output_location(ROOT / "tmp/loop-conformance/x"),
                         (ROOT / "tmp/loop-conformance/x").resolve())
        outside = pathlib.Path.home() / ".cache/lusona-evals-outputs/x"
        self.assertEqual(runner.check_output_location(outside), outside.resolve())
        refused = HERE / "runs/x"
        with self.assertRaisesRegex(ValueError, "not ignored"):
            runner.check_output_location(refused)
        self.freeze()
        with self.assertRaisesRegex(ValueError, "not ignored"):
            runner.prepare(self.condition, "greet", 1, refused, self.work_root, guard=self.guard)
        with self.assertRaisesRegex(ValueError, "not ignored"):
            runner.freeze(self.plugin, HERE / "conditions-x", "claude", "m", "high", 30, "j", "medium",
                          suite_dir=self.suite, executor=FakeHost([]), home=self.temp, environ={})
        with self.assertRaisesRegex(ValueError, "not ignored"):
            runner.report(self.temp, HERE / "report-x")
        with self.assertRaisesRegex(ValueError, "not ignored"):
            runner.calibrate(self.condition, self.temp / "none.json", HERE / "calibration-x")
        for name in ("runs", "conditions-x", "report-x", "calibration-x"):
            self.assertFalse((HERE / name).exists(), name)


class OuterRepositoryTest(unittest.TestCase):
    def test_content_state_sees_edits_hidden_from_porcelain(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        repo = pathlib.Path(tempfile.mkdtemp(prefix="outer-", dir=SCRATCH))
        self.addCleanup(shutil.rmtree, repo, True)
        runner.git(repo, "init", "--quiet")
        (repo / "a.txt").write_text("one\n")
        runner.git(repo, "add", "a.txt")
        runner.git(repo, "-c", "user.name=t", "-c", "user.email=t@t.invalid", "-c", "commit.gpgsign=false",
                   "commit", "--quiet", "-m", "base")
        (repo / "a.txt").write_text("two\n")
        (repo / "untracked").mkdir()
        (repo / "untracked/x.txt").write_text("x\n")
        before = runner.outer_repo_state(repo)
        porcelain = runner.git(repo, "status", "--porcelain").stdout
        (repo / "a.txt").write_text("three\n")
        after_edit = runner.outer_repo_state(repo)
        self.assertNotEqual(before, after_edit, "editing an already-modified file")
        (repo / "untracked/y.txt").write_text("y\n")
        after_add = runner.outer_repo_state(repo)
        self.assertNotEqual(after_edit, after_add, "adding a file inside an already-untracked directory")
        self.assertEqual(porcelain, runner.git(repo, "status", "--porcelain").stdout,
                         "porcelain output alone does not show either change")
        (repo / "a.txt").unlink()
        self.assertEqual(runner.outer_repo_state(repo)["a.txt"], "absent")


class EvaluatorAccessTest(RunnerTestBase):
    def read_turns(self, trial_dir, *calls):
        plugin = str(self.condition / "plugin")
        blocks = [{"type": "tool_use", "id": f"r{i}", "name": name, "input": data} for i, (name, data) in enumerate(calls)]
        event = {"type": "assistant", "parent_tool_use_id": None, "message": {"content": blocks}}
        return FakeHost([lambda a, k: subprocess.CompletedProcess(
            a, 0, jsonl(init_event("s", plugin), event, result_event("s", "Hi")), "")])

    def test_reading_condition_rubric_invalidates_trial(self):
        self.freeze()
        trial_dir = self.prepare(scenario="greet")
        host = self.read_turns(trial_dir, ("Read", {"file_path": str(self.condition / "rubric.md")}))
        trial = self.run_trial(trial_dir, host)
        self.assertEqual(trial["status"], "invalid")
        self.assertEqual(len(trial["evaluator_access"]), 1)
        self.assertIn("rubric.md", json.dumps(trial["evaluator_access"]))
        self.assertEqual(runner.grade(trial_dir)["C4"]["result"], "invalid")
        judge_host = FakeHost([], judge_stdout="unused")
        runner.judge(trial_dir, executor=judge_host, work_root=self.work_root, guard=self.guard)
        self.assertEqual(judge_host.calls, [])
        counts = runner.report(trial_dir, self.temp / "report")
        self.assertEqual(counts["claude"]["C4"]["invalid"], 1)
        self.assertIn("| Invalid |", (self.temp / "report/report.md").read_text())

    def test_bash_access_to_suite_files_or_another_trial_invalidates_trial(self):
        self.freeze()
        other = self.prepare(scenario="greet", name="other")
        other_workspace = json.loads((other / "run.json").read_text())["workspace"]
        cases = [("Bash", {"command": "cat ../../suite/scenarios.json"}),
                 ("Bash", {"command": f"ls {HERE}/reference/"}),
                 ("Grep", {"pattern": "x", "path": f"{other_workspace}/README.md"}),
                 ("Bash", {"command": "find / -name judge-calibration.json"})]
        for index, call in enumerate(cases):
            with self.subTest(call=call):
                self.outer = ["clean", "clean"]
                trial_dir = self.prepare(scenario="greet", trial=1, name=f"t{index}")
                self.assertEqual(self.run_trial(trial_dir, self.read_turns(trial_dir, call))["status"], "invalid")

    def test_plugin_and_workspace_reads_are_legitimate(self):
        self.freeze()
        trial_dir = self.prepare(scenario="greet")
        workspace = json.loads((trial_dir / "run.json").read_text())["workspace"]
        host = self.read_turns(trial_dir,
                               ("Read", {"file_path": str(self.condition / "plugin/README.md")}),
                               ("Read", {"file_path": f"{workspace}/README.md"}),
                               ("Bash", {"command": f"bash {self.condition}/plugin/scripts/work-record.sh slug 'x'"}),
                               ("Bash", {"command": "cat README.md && git status"}),
                               ("Write", {"file_path": f"{workspace}/notes.md",
                                          "content": "The suite reads scenarios.json and rubric.md."}))
        trial = self.run_trial(trial_dir, host)
        self.assertEqual(trial["status"], "captured")
        self.assertEqual(trial["evaluator_access"], [])

    def test_reviewer_false_positive_cases_are_not_invalid(self):
        self.freeze()
        heredoc = "cat > docs/note.md <<'EOF'\nSee the [Work queue](../work.md).\nEOF"
        cases = [("Bash", {"command": heredoc}),
                 ("Bash", {"command": "cd tests && cat ../README.md"}),
                 ("Agent", {"description": "Draft notes", "prompt": "Follow [the contract](../README.md#contract)."}),
                 ("Bash", {"command": "python3 - <<<'print(\"../../x\")'"}),
                 ("Bash", {"command": "cat > docs/lusona/specs/x.md <<'EOF'\n[Work queue](../work.md) ../work.md\nEOF"}),
                 ("Bash", {"command": "tee docs/n.md <<EOF\nsee ../../elsewhere\nEOF"}),
                 ("Grep", {"pattern": "def .*\\(..", "path": "."}),
                 ("Glob", {"pattern": "../**/*.md"}),
                 ("Bash", {"command": "pushd tests && cat ../README.md && popd"})]
        for index, call in enumerate(cases):
            with self.subTest(call=call):
                self.outer = ["clean", "clean"]
                trial_dir = self.prepare(scenario="greet", name=f"ok{index}")
                trial = self.run_trial(trial_dir, self.read_turns(trial_dir, call))
                self.assertEqual(trial["status"], "captured", trial["evaluator_access"])

    def test_interpreter_heredoc_code_is_not_read_as_relative_paths(self):
        self.freeze()
        snippets = ["print(Path('tally') / '..' / 'README.md')", "os.path.join(here, '..')", "from .. import x",
                    "print('see ../notes for details')", "os.listdir('..')"]
        for index, snippet in enumerate(snippets):
            with self.subTest(snippet=snippet):
                self.outer = ["clean", "clean"]
                trial_dir = self.prepare(scenario="greet", name=f"code{index}")
                call = ("Bash", {"command": f"python3 - <<'EOF'\nimport os\n{snippet}\nEOF"})
                trial = self.run_trial(trial_dir, self.read_turns(trial_dir, call))
                self.assertEqual(trial["status"], "captured", trial["evaluator_access"])
        self.outer = ["clean", "clean"]
        trial_dir = self.prepare(scenario="greet", name="shell-body")
        call = ("Bash", {"command": "bash <<EOF\nls ..\nEOF"})
        self.assertEqual(self.run_trial(trial_dir, self.read_turns(trial_dir, call))["status"], "invalid")

    def test_wrapped_interpreters_receive_code_bodies(self):
        self.freeze()
        rubric = ROOT / "evals/loop-conformance/rubric.md"
        wrappers = ["timeout 60 python3 -", "/usr/bin/env python3 -", "uv run python -", "python3.14 -"]
        for index, wrapper in enumerate(wrappers):
            for body, expected in (("print(Path('tally') / '..')", "captured"),
                                   (f"print(open('{rubric}').read())", "invalid")):
                with self.subTest(wrapper=wrapper, expected=expected):
                    self.outer = ["clean", "clean"]
                    trial_dir = self.prepare(scenario="greet", name=f"wrap{index}-{expected}")
                    call = ("Bash", {"command": f"{wrapper} <<'EOF'\nfrom pathlib import Path\n{body}\nEOF"})
                    trial = self.run_trial(trial_dir, self.read_turns(trial_dir, call))
                    self.assertEqual(trial["status"], expected, trial["evaluator_access"])
        self.outer = ["clean", "clean"]
        trial_dir = self.prepare(scenario="greet", name="wrapped-shell")
        call = ("Bash", {"command": "timeout 60 bash <<EOF\nls ..\nEOF"})
        self.assertEqual(self.run_trial(trial_dir, self.read_turns(trial_dir, call))["status"], "invalid")

    def test_heredoc_receiver_skips_wrappers(self):
        for before, receiver in (("timeout 60 python3 - ", "python3"), ("/usr/bin/env FOO=1 python3 - ", "python3"),
                                 ("A=1 env B=2 node ", "node"), ("nice -n 5 ruby ", "ruby"), ("time perl ", "perl"),
                                 ("uv run python - ", "python"), ("cd x && timeout 5s bash ", "bash"),
                                 ("cat > out.md ", "cat"), ("> out.md ", "")):
            with self.subTest(before=before):
                self.assertEqual(runner._heredoc_receiver(before), receiver)

    def test_parent_directory_and_repository_paths_are_invalid(self):
        self.freeze()
        rubric = ROOT / "evals/loop-conformance/rubric.md"
        cases = [("Bash", {"command": "ls .."}),
                 ("Bash", {"command": "ls ../.."}),
                 ("Bash", {"command": "cd .. && ls"}),
                 ("Bash", {"command": "pushd .. && ls"}),
                 ("Bash", {"command": f"python3 - <<'EOF'\nprint(open('{rubric}').read())\nEOF"}),
                 ("Bash", {"command": "grep x <<< 'hi'; cat ../other-ws/README.md"}),
                 ("Grep", {"pattern": "x", "path": ".."}),
                 ("Read", {"file_path": str(ROOT / "docs/lusona/work.md")}),
                 ("Bash", {"command": f"cat {ROOT}/plugins/lusona/README.md"})]
        for index, call in enumerate(cases):
            with self.subTest(call=call):
                self.outer = ["clean", "clean"]
                trial_dir = self.prepare(scenario="greet", name=f"bad{index}")
                self.assertEqual(self.run_trial(trial_dir, self.read_turns(trial_dir, call))["status"], "invalid")

    def test_glob_reaching_other_workspaces_is_flagged(self):
        home = self.temp / "home"
        work_root = home / ".cache/lusona-evals"
        workspace, other = work_root / "a-t1-1", work_root / "b-t1-2"
        for directory in (workspace, other):
            directory.mkdir(parents=True)
            (directory / "README.md").write_text("x")
        plugin = self.temp / "cond/plugin"
        plugin.mkdir(parents=True)
        environ = {"HOME": str(home)}
        for command in ("ls $HOME/.cache/lusona-evals/*/README.md", "ls ~/.cache/lusona-*/*",
                        "cat ${HOME}/.cache/lusona-evals/b-t1-2/README.md"):
            with self.subTest(command=command):
                hits = runner.evaluator_access([(1, [("Bash", {"command": command})])], workspace=workspace,
                                               plugin=plugin, condition_dir=plugin.parent, trial_dir=self.temp / "t",
                                               work_root=work_root, repo_root=self.temp / "repo", environ=environ)
                self.assertEqual(len(hits), 1, command)
        own = runner.evaluator_access([(1, [("Bash", {"command": "ls ./*.md"})])], workspace=workspace, plugin=plugin,
                                      condition_dir=plugin.parent, trial_dir=self.temp / "t", work_root=work_root,
                                      repo_root=self.temp / "repo", environ=environ)
        self.assertEqual(own, [])

    def test_codex_command_items_are_scanned(self):
        self.host = "codex"
        self.freeze()
        trial_dir = self.prepare(scenario="greet")
        item = {"id": "c", "type": "command_execution", "command": f"cat {self.condition}/condition.json"}
        events = [{"type": "thread.started", "thread_id": "t"}, {"type": "item.completed", "item": item},
                  {"type": "item.completed", "item": {"type": "agent_message", "text": "rubric.md is mentioned only in text"}},
                  {"type": "turn.completed"}]
        host = FakeHost([lambda a, k: subprocess.CompletedProcess(a, 0, jsonl(*events), "")], version=CODEX_VERSION)
        trial = self.run_trial(trial_dir, host)
        self.assertEqual(trial["status"], "invalid")
        self.assertEqual(len(trial["evaluator_access"]), 1)


def trial_cond_tools(condition):
    return json.loads((condition / "condition.json").read_text())["allowed_tools"]


class CodexRunTest(RunnerTestBase):
    host = "codex"

    def codex_turn(self, thread, text, items=()):
        events = [{"type": "thread.started", "thread_id": thread}, {"type": "turn.started"}]
        events += [{"type": "item.completed", "item": item} for item in items]
        events += [{"type": "item.completed", "item": {"id": "m", "type": "agent_message", "text": text}},
                   {"type": "turn.completed", "usage": {"input_tokens": 5}}]
        return lambda args, kwargs: subprocess.CompletedProcess(args, 0, jsonl(*events), "")

    def test_resume_by_thread_and_hidden_workers_are_null(self):
        self.freeze()
        host = FakeHost([self.codex_turn("th-1", "one"), self.codex_turn("th-1", GOOD_REPLY)], version=CODEX_VERSION)
        trial = self.run_trial(self.prepare(), host)
        self.assertEqual(trial["status"], "captured")
        self.assertEqual(host.calls[1][0][-3:], ["resume", "th-1", "-"])
        self.assertIn("--ignore-user-config", host.calls[0][0])
        self.assertEqual(trial["replies"], ["one", GOOD_REPLY])
        self.assertIsNone(trial["workers"])
        self.assertIsNone(trial["reviewer_seen"])
        self.assertEqual(runner.grade(self.temp / "trial")["C10"]["result"], "inconclusive")

    # Item shape copied from the pilot (codex-cli 0.167.0, runs/pilot/codex/explore-save/1): the
    # exec JSONL showed only this wait call, while the session rollout held one spawn_agent call.
    WAIT = {"id": "item_14", "type": "collab_tool_call", "tool": "wait", "sender_thread_id": "th-1",
            "receiver_thread_ids": [], "prompt": "", "agents_states": {}, "status": "completed"}

    def test_exec_jsonl_alone_never_sets_a_worker_count(self):
        parsed = runner.parse_codex(jsonl({"type": "thread.started", "thread_id": "th-1"},
                                          {"type": "item.started", "item": dict(self.WAIT, status="in_progress")},
                                          {"type": "item.completed", "item": self.WAIT},
                                          {"type": "item.completed", "item": {"type": "agent_message", "text": "x"}},
                                          {"type": "turn.completed"}))
        self.assertIsNone(parsed["workers"])
        self.assertIsNone(parsed["reviewer_seen"])
        self.assertEqual(parsed["item_types"]["collab_tool_call"], 1)

    def rollout(self, sessions, thread, task_names):
        rows = [{"type": "session_meta", "payload": {"id": thread}},
                {"type": "response_item", "payload": {"type": "function_call", "name": "exec", "arguments": "{}"}}]
        rows += [{"type": "response_item", "payload": {"type": "function_call", "name": "spawn_agent",
                  "arguments": json.dumps({"task_name": name, "model": "m", "message": "gAAAAencrypted"})}}
                 for name in task_names]
        rows.append({"type": "response_item", "payload": {"type": "function_call", "name": "wait_agent",
                     "arguments": "{}"}})
        folder = sessions / "2026/11/09"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / f"rollout-2026-11-09T15-38-04-{thread}.jsonl").write_text(jsonl(*rows))

    def run_with_rollout(self, task_names, name):
        sessions = self.temp / f"sessions-{name}"
        sessions.mkdir()
        if task_names is not None:
            self.rollout(sessions, "th-1", task_names)
        self.outer = ["clean", "clean"]
        trial_dir = self.prepare(scenario="greet", name=name)
        host = FakeHost([self.codex_turn("th-1", GOOD_REPLY, [self.WAIT])], version=CODEX_VERSION)
        return runner.run_trial(trial_dir, executor=host, outer_status=self.outer_status, codex_sessions=sessions,
                                home=self.temp, environ={})

    def test_ambient_agents_change_blocks_before_turn_one(self):
        home = self.temp / "home"
        (home / ".codex").mkdir(parents=True)
        (home / ".codex/AGENTS.md").write_text("rules v1\n")
        self.freeze(home=home)
        trial_dir = self.prepare(scenario="greet")
        (home / ".codex/AGENTS.md").write_text("rules v2\n")
        host = FakeHost([self.codex_turn("th-1", "x")], version=CODEX_VERSION)
        trial = runner.run_trial(trial_dir, executor=host, outer_status=self.outer_status, home=home, environ={})
        self.assertEqual(trial["status"], "setup-blocked")
        self.assertEqual(host.calls, [])
        self.assertIn("AGENTS.md", trial["capture"]["error"])

    def test_spawn_named_with_underscore_before_review_is_a_reviewer(self):
        self.freeze()
        trial = self.run_with_rollout(["delete_review"], "underscore")
        self.assertEqual((trial["workers"], trial["reviewer_seen"], trial["work_workers"]), (1, True, 0))

    def test_workers_come_from_spawn_calls_in_the_session_rollout(self):
        self.freeze()
        reviewed = self.run_with_rollout(["review_diff"], "reviewed")
        self.assertEqual((reviewed["workers"], reviewed["reviewer_seen"], reviewed["work_workers"]), (1, True, 0))
        self.assertTrue((self.temp / "reviewed/codex-rollout-summary.json").is_file())
        other = self.run_with_rollout(["storage_options", "preview_page"], "other")
        self.assertEqual((other["workers"], other["work_workers"]), (2, 2))
        self.assertIsNone(other["reviewer_seen"], "spawn messages are encrypted; no review name is not proof")
        none = self.run_with_rollout([], "none")
        self.assertEqual((none["workers"], none["reviewer_seen"]), (0, False))
        missing = self.run_with_rollout(None, "missing")
        self.assertEqual((missing["workers"], missing["reviewer_seen"], missing["work_workers"]), (None, None, None))


class JudgeAndReportTest(RunnerTestBase):
    def captured_trial(self, name, reply, trial=1):
        trial_dir = self.prepare(trial=trial, name=name)
        workspace = pathlib.Path(json.loads((trial_dir / "run.json").read_text())["workspace"])
        plugin = str(self.condition / "plugin")

        def turn(text, write):
            def call(args, kwargs):
                if write:
                    (workspace / "docs/lusona/notes").mkdir(parents=True, exist_ok=True)
                    (workspace / "docs/lusona/notes/n.md").write_text("note\n")
                return subprocess.CompletedProcess(args, 0, jsonl(init_event("s", plugin), result_event("s", text)), "")
            return call

        self.outer = ["clean", "clean"]
        self.run_trial(trial_dir, FakeHost([turn("one", False), turn(reply, True)]))
        runner.grade(trial_dir)
        return trial_dir

    def envelope(self, payload):
        return json.dumps({"type": "result", "result": payload, "total_cost_usd": 0.02})

    def test_judge_parses_fenced_json_and_prompt_holds_only_own_section(self):
        self.freeze()
        trial_dir = self.captured_trial("trial", GOOD_REPLY)
        verdict = {"C1.concrete": {"result": "pass", "evidence": "names Decide"},
                   "C7.continues": {"result": "fail", "evidence": "asked for a command"}}
        host = FakeHost([], judge_stdout=self.envelope("```json\n" + json.dumps(verdict) + "\n```"))
        judged = runner.judge(trial_dir, executor=host, work_root=self.work_root, guard=self.guard)
        self.assertEqual(judged, verdict)
        args, kwargs = host.calls[0]
        self.assertNotIn("--plugin-dir", args)
        self.assertNotIn("--allowedTools", args)
        self.assertEqual(args[args.index("--model") + 1], "judge-model")
        prompt = kwargs["input"]
        self.assertIn("Required: a named next step and owner.", prompt)
        self.assertNotIn("SECRET-OTHER-SECTION", prompt)
        self.assertIn("docs/lusona/notes/n.md", prompt)
        self.assertIn(GOOD_REPLY.strip(), prompt)
        self.assertFalse(list(self.work_root.glob("judge-*")), "judge directory removed after the call")

    def test_malformed_judge_output_makes_every_criterion_inconclusive(self):
        self.freeze()
        trial_dir = self.captured_trial("trial", GOOD_REPLY)
        host = FakeHost([], judge_stdout=self.envelope("I think it passes."))
        judged = runner.judge(trial_dir, executor=host, work_root=self.work_root, guard=self.guard)
        self.assertEqual({v["result"] for v in judged.values()}, {"inconclusive"})
        self.assertEqual(set(judged), {"C1.concrete", "C7.continues"})
        partial = runner.parse_judgment(self.envelope(json.dumps({"C1.concrete": {"result": "maybe"}})),
                                        ["C1.concrete"])
        self.assertEqual(partial["C1.concrete"]["result"], "inconclusive")

    def test_scenario_without_criteria_skips_the_model_call(self):
        self.freeze()
        trial_dir = self.prepare(scenario="greet")
        plugin = str(self.condition / "plugin")
        self.run_trial(trial_dir, FakeHost([lambda a, k: subprocess.CompletedProcess(
            a, 0, jsonl(init_event("s", plugin), result_event("s", "Hi")), "")]))
        host = FakeHost([], judge_stdout="unused")
        self.assertEqual(runner.judge(trial_dir, executor=host, work_root=self.work_root, guard=self.guard), {})
        self.assertEqual(host.calls, [])
        self.assertEqual(json.loads((trial_dir / "judged.json").read_text()), {})

    def test_calibration_reports_agreement_and_mismatches(self):
        self.freeze()
        cases = [{"id": "a", "scenario": "explore-a", "criterion": "C1.concrete", "turns": ["q"], "replies": ["r"],
                  "reply": "r", "files": {}, "expected": "pass"},
                 {"id": "b", "scenario": "explore-a", "criterion": "C7.continues", "turns": ["q"], "replies": ["r"],
                  "reply": "r", "files": {"docs/x.md": "x"}, "expected": "fail"}]
        path = self.temp / "cases.json"
        path.write_text(json.dumps(cases))
        host = FakeHost([], judge_stdout=self.envelope(json.dumps(
            {"C1.concrete": {"result": "pass", "evidence": "ok"}, "C7.continues": {"result": "pass", "evidence": "ok"}})))
        summary = runner.calibrate(self.condition, path, self.temp / "calibration", executor=host,
                                   work_root=self.work_root, guard=self.guard)
        self.assertEqual((summary["matches"], summary["total"]), (1, 2))
        self.assertEqual([m["id"] for m in summary["mismatches"]], ["b"])
        self.assertIn("1 / 2", (self.temp / "calibration/calibration.md").read_text())
        self.assertNotIn("C7.continues", host.calls[0][1]["input"].split("# Criteria to grade")[1].split("# Scripted")[0])

    def test_outer_change_fails_unlisted_c8_in_report(self):
        self.freeze()
        trial_dir = self.prepare(scenario="greet", name="runs/g")
        plugin = str(self.condition / "plugin")
        self.outer = [{"a.txt": "1"}, {"a.txt": "2"}]
        trial = runner.run_trial(trial_dir, executor=FakeHost([lambda a, k: subprocess.CompletedProcess(
            a, 0, jsonl(init_event("s", plugin), result_event("s", "Hi")), "")]),
            outer_status=self.outer_status, home=self.temp, environ={})
        self.assertTrue(trial["outer_changed"])
        self.assertEqual(trial["capture"]["outer_changed_paths"], ["a.txt"])
        runner.grade(trial_dir)
        counts = runner.report(self.temp / "runs", self.temp / "report")
        self.assertEqual(counts["claude"]["C8"]["fail"], 1)
        self.assertIn("runs/g", (self.temp / "report/report.md").read_text().split("## Outer repository")[1])

    def test_report_refuses_duplicate_trials(self):
        self.freeze()
        self.captured_trial("runs/a", GOOD_REPLY, trial=1)
        self.captured_trial("runs/b", GOOD_REPLY, trial=1)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            runner.report(self.temp / "runs", self.temp / "report")
        self.assertNotEqual(runner.main(["report", "--run", str(self.temp / "runs"), "--out", str(self.temp / "r2")]), 0)

    def test_grading_code_hashes_hold_grade_step_hashes_only(self):
        self.freeze()
        trial_dir = self.captured_trial("runs/a", GOOD_REPLY)
        grade_hashes = json.loads((trial_dir / "grade-provenance.json").read_text())["code_hashes"]
        judged_by_other_code = dict(grade_hashes, **{"checks.py": "0" * 64})
        runner.save(trial_dir / "judge-provenance.json", {"step": "judge", "code_hashes": judged_by_other_code})
        counts = runner.report(self.temp / "runs", self.temp / "report")
        self.assertEqual(counts["grading_code_hashes"], [grade_hashes])
        reference = runner.make_reference(self.temp / "report/report.json", self.condition, self.temp / "ref.json")
        self.assertEqual(reference["grading_code_hashes"], [grade_hashes])

    def test_grading_provenance_reaches_report_and_reference(self):
        self.freeze()
        trial_dir = self.captured_trial("runs/a", GOOD_REPLY)
        provenance = json.loads((trial_dir / "grade-provenance.json").read_text())
        self.assertEqual(provenance["code_hashes"], runner.code_hashes())
        counts = runner.report(self.temp / "runs", self.temp / "report")
        self.assertEqual(counts["grading_code_hashes"], [runner.code_hashes()])
        self.assertIn("claude", counts)
        reference = runner.make_reference(self.temp / "report/report.json", self.condition, self.temp / "ref.json")
        self.assertEqual(reference["condition"]["cli_version"], CLAUDE_VERSION)
        self.assertEqual(reference["condition"]["judge_cli_version"], CLAUDE_VERSION)
        self.assertEqual(reference["grading_code_hashes"], [runner.code_hashes()])

    def test_report_lists_boundary_evidence_of_excluded_trials(self):
        self.freeze()
        trial_dir = self.prepare(scenario="greet", name="runs/blocked")
        workspace = pathlib.Path(json.loads((trial_dir / "run.json").read_text())["workspace"])

        def wrong_plugin(args, kwargs):
            (workspace / "stray.txt").write_text("x")
            return subprocess.CompletedProcess(args, 0, jsonl(init_event("s", "/elsewhere"), result_event("s", "Hi")), "")

        self.run_trial(trial_dir, FakeHost([wrong_plugin]))
        runner.grade(trial_dir)
        counts = runner.report(self.temp / "runs", self.temp / "report")
        self.assertEqual(counts["claude"]["C4"]["setup-blocked"], 1)
        markdown = (self.temp / "report/report.md").read_text()
        section = markdown.split("## Boundary evidence of excluded trials")[1]
        self.assertIn("stray.txt", section)

    def test_report_reference_and_compare(self):
        self.freeze()
        runs = self.temp / "runs"
        good = self.captured_trial("runs/a", GOOD_REPLY, trial=1)
        bad = self.captured_trial("runs/b", "No labels here.", trial=2)
        verdict = {"C1.concrete": {"result": "pass", "evidence": "x"}, "C7.continues": {"result": "pass", "evidence": "y"}}
        runner.judge(good, executor=FakeHost([], judge_stdout=self.envelope(json.dumps(verdict))),
                     work_root=self.work_root, guard=self.guard)
        counts = runner.report(runs, self.temp / "report")
        self.assertEqual(set(counts) - {"grading_code_hashes"}, {"claude"})
        c1, c7, c4 = counts["claude"]["C1"], counts["claude"]["C7"], counts["claude"]["C4"]
        self.assertEqual((c1["pass"], c1["fail"]), (1, 1))
        self.assertEqual((c7["pass"], c7["inconclusive"]), (1, 1), "unjudged trial is inconclusive for C7")
        self.assertEqual(c4["not-applicable"], 2)
        self.assertEqual(set(counts["claude"]["C1"]), set(runner.STATES))
        markdown = (self.temp / "report/report.md").read_text()
        self.assertIn("| C1 | 1 | 1 | 2 |", markdown)
        reference_path = self.temp / "reference/claude.json"
        runner.make_reference(self.temp / "report/report.json", self.condition, reference_path)
        with self.assertRaises(FileExistsError):
            runner.make_reference(self.temp / "report/report.json", self.condition, reference_path)
        outcome = runner.compare_run(reference_path, self.temp / "report/report.json", self.condition)
        self.assertEqual(outcome["status"], "insufficient")
        self.assertTrue((self.temp / "report/compare.md").exists())
        stored = json.loads(reference_path.read_text())
        stored["condition"]["model"] = "other-model"
        reference_path.write_text(json.dumps(stored))
        self.assertEqual(runner.compare_run(reference_path, self.temp / "report/report.json", self.condition)["status"],
                         "refused")


if __name__ == "__main__":
    unittest.main()
