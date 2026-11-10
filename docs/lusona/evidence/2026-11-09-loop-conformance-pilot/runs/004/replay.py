"""Verify the retained offline audit against run 003's local raw archive.

Run from the repository root. This verifies hashes, capture fidelity, and computed
grades; semantic audit fields require reading the replies and rubric.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import zipfile

root = Path.cwd()
audit = json.loads(Path(__file__).with_name("audit.json").read_text())
archive = root / audit["source"]
assert hashlib.sha256(archive.read_bytes()).hexdigest() == audit["source_sha256"]
for name, expected in audit["instrument_sha256"].items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected, name
spec = importlib.util.spec_from_file_location("checks", root / "evals/loop-conformance/checks.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)
scenarios = json.loads((root / "evals/loop-conformance/scenarios.json").read_text())
turn_count = 0
with zipfile.ZipFile(archive) as source:
    for row in audit["rows"]:
        prefix = row["archive_prefix"]
        trial = json.loads(source.read(prefix + "trial.json"))
        computed = json.loads(source.read(prefix + "computed.json"))
        judged = json.loads(source.read(prefix + "judged.json"))
        assert hashlib.sha256(trial["replies"][-1].encode()).hexdigest() == row["final_reply_sha256"]
        scenario = scenarios[trial["scenario"]]
        assert checks.c9_reply_format(trial, scenario) == computed["C9"] == row["c9"]
        assert checks.c1_next_action(trial, scenario) == computed["C1"] == row["c1_computed"]
        assert judged["C1.concrete"] == row["c1_judged"]
        for number, reply in enumerate(trial["replies"], 1):
            events = [json.loads(line) for line in source.read(prefix + f"turn-{number}.stdout.jsonl").decode().splitlines() if line.strip()]
            if trial["host"] == "codex":
                finals = [e["item"]["text"] for e in events if e.get("type") == "item.completed" and e.get("item", {}).get("type") == "agent_message"]
            else:
                finals = [e["result"] for e in events if e.get("type") == "result" and e.get("result") is not None]
            assert finals[-1] == reply, (row["id"], number)
            turn_count += 1
print(f"Verified {len(audit['rows'])} trial hashes and C1/C9 grades; {turn_count} original turn replies match capture.")
