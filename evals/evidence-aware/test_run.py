import importlib.util
import json
import os
import pathlib
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import unittest


HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]


class HarnessTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("evaluation_run", HERE / "run.py")
        cls.runner = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.runner)

    def setUp(self):
        (ROOT / "tmp/evidence-aware-eval").mkdir(parents=True, exist_ok=True)
        self.temp = pathlib.Path(tempfile.mkdtemp(dir=ROOT / "tmp/evidence-aware-eval"))
        self.addCleanup(shutil.rmtree, self.temp)
        self.plugin = self.temp / "source-plugin"
        (self.plugin / "skills/implement").mkdir(parents=True)
        (self.plugin / "skills/implement/SKILL.md").write_text("# Implement\n")
        self.condition = self.temp / "baseline"

    def freeze(self):
        self.runner.freeze(self.plugin, self.condition, "test-model", "medium", 30)

    def test_frozen_condition_uses_snapshot_and_detects_mutation(self):
        self.freeze()
        (self.plugin / "skills/implement/SKILL.md").write_text("new source")
        data = self.runner.load_condition(self.condition)
        self.assertEqual((self.condition / "plugin/skills/implement/SKILL.md").read_text(), "# Implement\n")
        (self.condition / "plugin/skills/implement/SKILL.md").write_text("changed snapshot")
        with self.assertRaisesRegex(ValueError, "changed"):
            self.runner.load_condition(self.condition)
        self.assertEqual(data["model"], "test-model")

    def test_trial_isolated_and_rubric_not_exposed(self):
        self.freeze()
        first = self.runner.prepare(self.condition, "simple", 1, self.temp / "first")
        second = self.runner.prepare(self.condition, "simple", 2, self.temp / "second")
        (first / "workspace/README.md").write_text("trial mutation")
        self.assertNotEqual((second / "workspace/README.md").read_text(), "trial mutation")
        self.assertFalse((first / "workspace/rubric.md").exists())
        self.assertNotIn("grading", (first / "turn-1.input.txt").read_text().lower())
        with self.assertRaisesRegex(ValueError, "trial"):
            self.runner.prepare(self.condition, "simple", 4, self.temp / "fourth")
        with self.assertRaises(FileExistsError):
            self.runner.prepare(self.condition, "simple", 1, self.temp / "first")

    def test_resume_uses_same_session_and_setup_failure_is_retained(self):
        self.freeze()
        run = self.runner.prepare(self.condition, "revision", 1, self.temp / "run")
        first_command = self.runner.command(self.runner.load_condition(self.condition), run, None)
        resumed = self.runner.command(self.runner.load_condition(self.condition), run, "test-session")
        self.assertNotIn("--ephemeral", first_command)
        self.assertEqual(resumed[-3:], ["resume", "test-session", "-"])
        result = self.runner.capture(run, executor=lambda *args, **kwargs: (_ for _ in ()).throw(FileNotFoundError("missing codex")))
        self.assertEqual(result["status"], "setup-blocked")
        self.assertTrue((run / "turn-1.result.json").is_file())
        self.assertTrue((run / "turn-1.before.json").is_file())
        self.assertTrue((run / "turn-1.after.json").is_file())
        with self.assertRaisesRegex(ValueError, "previous"):
            self.runner.capture(run)

    def test_successive_turns_capture_exact_inputs_session_and_artifacts(self):
        self.freeze()
        run = self.runner.prepare(self.condition, "revision", 1, self.temp / "run")
        calls = []

        def executor(args, **kwargs):
            calls.append((args, kwargs["input"]))
            (run / "workspace/docs/lusona/notes/export-inventory.md").write_text(f"observed turn {len(calls)}")
            return subprocess.CompletedProcess(args, 0, '\n'.join([
                json.dumps({"type": "thread.started", "thread_id": "same-session"}),
                json.dumps({"type": "turn.completed", "usage": {"input_tokens": 100, "output_tokens": 20}})
            ]), "")

        first = self.runner.capture(run, executor=executor)
        second = self.runner.capture(run, executor=executor)
        self.assertEqual(first["status"], "captured")
        self.assertEqual(second["resumed_session"], "same-session")
        self.assertEqual(calls[1][0][-3:], ["resume", "same-session", "-"])
        self.assertEqual(calls[1][1], (run / "turn-2.input.txt").read_text())
        self.assertEqual((run / "turn-1.artifacts/docs/lusona/notes/export-inventory.md").read_text(), "observed turn 1")
        self.assertEqual((run / "turn-2.artifacts/docs/lusona/notes/export-inventory.md").read_text(), "observed turn 2")
        self.assertEqual(second["usage"], {"input_tokens": 100, "output_tokens": 20})
        self.assertEqual(second["runner_sha256"], self.runner.digest(run / "turn-2.runner.py"))
        self.assertEqual(json.loads((run / "run.json").read_text())["prepared_runner_sha256"], second["runner_sha256"])

    def test_timeout_stops_owned_descendant_before_artifact_snapshot(self):
        self.freeze()
        settings = self.runner.load_condition(self.condition)
        settings["timeout_seconds"] = 0.3
        self.runner.save(self.condition / "condition.json", settings)
        run = self.runner.prepare(self.condition, "simple", 1, self.temp / "run")
        child_code = (
            "import os, pathlib, signal, time; "
            "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
            "pathlib.Path('child.pid').write_text(str(os.getpid())); "
            "time.sleep(0.7); pathlib.Path('late-write.txt').write_text('still running')"
        )
        parent_code = (
            "import subprocess, sys, time; "
            f"subprocess.Popen([sys.executable, '-c', {child_code!r}]); "
            "print('partial stdout', flush=True); "
            "print('partial stderr', file=sys.stderr, flush=True); time.sleep(10)"
        )
        owned_executor = self.runner.capture.__defaults__[0]

        def local_executor(args, **kwargs):
            return owned_executor([sys.executable, "-c", parent_code], **kwargs)

        try:
            result = self.runner.capture(run, executor=local_executor)
            self.assertEqual(result["status"], "inconclusive")
            self.assertIn("partial stdout", (run / "turn-1.stdout.jsonl").read_text())
            self.assertIn("partial stderr", (run / "turn-1.stderr.txt").read_text())
            self.assertTrue((run / "workspace/child.pid").exists(), "descendant must have started")
            time.sleep(0.8)
            self.assertEqual(self.runner.hashes(run / "workspace"), json.loads((run / "turn-1.after.json").read_text()),
                             "descendant wrote after the final evidence snapshot")
            self.assertFalse((run / "workspace/late-write.txt").exists())
        finally:
            pid_file = run / "workspace/child.pid"
            if pid_file.exists():
                try:
                    os.kill(int(pid_file.read_text()), signal.SIGKILL)
                except ProcessLookupError:
                    pass

    def test_rollout_supplement_preserves_actual_calls_and_excludes_host_context(self):
        self.freeze()
        run = self.runner.prepare(self.condition, "revision", 1, self.temp / "run")
        session = "00000000-0000-0000-0000-000000000001"
        original_result = {"session": session, "status": "captured"}
        self.runner.save(run / "turn-1.result.json", original_result)
        sessions = self.temp / "sessions"
        sessions.mkdir()
        (sessions / "unrelated-session.jsonl").write_text("not JSON; must never be read")
        source = sessions / f"rollout-date-{session}.jsonl"
        call = {"type": "function_call", "name": "spawn_agent", "namespace": "collaboration",
                "arguments": '{"task_name":"inspect","message":"actual assignment"}', "call_id": "c1",
                "internal_chat_message_metadata_passthrough": {"host_private": "drop"}}
        events = [
            {"type": "session_meta", "payload": {"secret_host": "excluded"}},
            {"type": "response_item", "payload": {"type": "message", "role": "developer", "content": "secret developer"}},
            {"type": "response_item", "payload": {"type": "message", "role": "user", "content": "host-injected metadata"}},
            {"type": "response_item", "payload": {"type": "message", "role": "assistant", "content": "actual actor answer"}},
            {"type": "response_item", "payload": call},
            {"type": "response_item", "payload": {"type": "function_call_output", "call_id": "c1", "output": '{"task_name":"/root/inspect"}'}},
            {"type": "response_item", "payload": {"type": "custom_tool_call", "call_id": "c2", "name": "exec", "input": "actual code"}},
            {"type": "response_item", "payload": {"type": "custom_tool_call_output", "call_id": "c2", "output": "actual result"}},
            {"type": "event_msg", "payload": {"type": "item_completed", "thread_id": session,
                "item": {"type": "SubAgentActivity", "kind": "started", "agent_thread_id": "worker-1", "agent_path": "/root/inspect", "model": "test"}}}
        ]
        source.write_text("\n".join(json.dumps(e) for e in events) + "\n")
        first = self.runner.supplement(run, 1, sessions_root=sessions)
        self.assertEqual(first["status"], "captured")
        trace = pathlib.Path(first["trace"])
        first_bytes = trace.read_bytes()
        text = first_bytes.decode()
        self.assertIn("actual assignment", text)
        self.assertIn("actual result", text)
        self.assertIn("actual actor answer", text)
        self.assertNotIn("secret", text)
        self.assertNotIn("host-injected", text)
        self.assertNotIn("host_private", text)
        self.assertEqual(first["observed_tool_calls"], {"spawn_agent": 1, "exec": 1})
        self.assertEqual(first["observed_worker_threads"], 1)
        self.assertEqual(first["scope"], "cumulative-session-supplement")
        self.assertFalse(first["per_turn_snapshot"])
        source.write_text(source.read_text() + json.dumps({"type": "response_item", "payload": {
            "type": "function_call", "name": "followup_task", "arguments": "actual followup"}}) + "\n")
        second = self.runner.supplement(run, 1, sessions_root=sessions)
        self.assertNotEqual(first["trace"], second["trace"])
        self.assertEqual(trace.read_bytes(), first_bytes)
        self.assertEqual(json.loads((run / "turn-1.result.json").read_text()), original_result)

    def test_wrong_shaped_rollout_lines_keep_diagnostic_and_valid_partial_trace(self):
        self.freeze()
        run = self.runner.prepare(self.condition, "simple", 1, self.temp / "run")
        session = "00000000-0000-0000-0000-000000000002"
        self.runner.save(run / "turn-1.result.json", {"session": session, "status": "captured"})
        sessions = self.temp / "sessions"
        sessions.mkdir()
        rows = [[], {"type": "response_item", "payload": []},
                {"type": "event_msg", "payload": {"type": "item_completed", "item": []}},
                {"type": "response_item", "payload": {"type": [], "name": "bad"}},
                {"type": "response_item", "payload": {"type": "function_call", "name": "exec", "arguments": "actual"}}]
        (sessions / f"rollout-date-{session}.jsonl").write_text("\n".join(json.dumps(row) for row in rows) + "\n")
        result = self.runner.supplement(run, 1, sessions_root=sessions)
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["malformed_or_partial_lines"], 4)
        self.assertIn("incomplete", result["diagnostic"])
        self.assertIn("actual", pathlib.Path(result["trace"]).read_text())
        self.assertTrue(list(run.glob("turn-1.session-supplement-*.json")))


if __name__ == "__main__":
    unittest.main()
