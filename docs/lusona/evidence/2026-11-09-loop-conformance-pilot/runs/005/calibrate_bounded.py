"""Task-local sequential calibration with an aggregate call and spend limit."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("loop_run", ROOT / "evals/loop-conformance/run.py")
run = importlib.util.module_from_spec(spec)
spec.loader.exec_module(run)
parser = argparse.ArgumentParser()
parser.add_argument("phase", choices=["baseline", "candidate"])
parser.add_argument("cases", type=Path)
args = parser.parse_args()
journal_path = HERE / "budget.json"
journal = json.loads(journal_path.read_text()) if journal_path.exists() else {
    "call_limit": 28, "usd_limit": 10.0, "calls": [], "spent_usd": 0.0,
    "authority": "2026-11-09 user Implement invocation on completion-reply-conformance spec"
}
phase_dir = HERE / args.phase
phase_dir.mkdir(exist_ok=False)
case_bytes = args.cases.read_bytes()
(phase_dir / "cases.json").write_bytes(case_bytes)
cases = json.loads(case_bytes)
summary = {"phase": args.phase, "cases_sha256": hashlib.sha256(case_bytes).hexdigest(), "rows": []}
condition = HERE / f"{args.phase}-condition"
for index, case in enumerate(cases, 1):
    remaining = journal["usd_limit"] - journal["spent_usd"]
    if len(journal["calls"]) >= journal["call_limit"] or remaining <= 0:
        raise SystemExit("Authorized calibration limit reached")
    single = phase_dir / f"input-{index:02d}.json"
    single.write_text(json.dumps([case], indent=2) + "\n")
    call = {"phase": args.phase, "case_id": case["id"], "budget_remaining_usd": remaining,
            "status": "started"}
    journal["calls"].append(call)
    run.save(journal_path, journal)

    def limited_executor(command, **kwargs):
        command = [*command, "--max-budget-usd", f"{remaining:.8f}"]
        call["actual_command"] = command
        run.save(journal_path, journal)
        return run.execute(command, **kwargs)

    output = phase_dir / f"case-{index:02d}"
    try:
        result = run.calibrate(condition, single, output, executor=limited_executor)
    except Exception as error:
        call.update(status="error", error=repr(error))
        run.save(journal_path, journal)
        raise
    records = [json.loads(p.read_text()) for p in output.glob("*.call.json")]
    if len(records) != 1 or records[0].get("cost_usd") is None:
        call["status"] = "unknown-cost"
        run.save(journal_path, journal)
        raise SystemExit("Calibration cost unavailable; stopped without retry")
    cost = records[0]["cost_usd"]
    journal["spent_usd"] += cost
    row = result["cases"][0]
    call.update(status="finished", cost_usd=cost, result=row)
    journal["judge_model"] = result["judge_model"]
    journal["judge_effort"] = result["judge_effort"]
    journal["judge_prompt_sha256"] = result["judge_prompt_sha256"]
    run.save(journal_path, journal)
    summary["rows"].append(row)
    summary["matches"] = sum(r["match"] for r in summary["rows"])
    run.save(phase_dir / "summary.json", summary)
    print(f"{args.phase} {index}/{len(cases)} {case['id']}: expected {row['expected']}, "
          f"judged {row['judged']}; total ${journal['spent_usd']:.4f}", flush=True)
    if journal["spent_usd"] >= journal["usd_limit"]:
        raise SystemExit("Spend cap reached; stopped")
    if row["judged"] == "inconclusive" or (args.phase == "candidate" and not row["match"]):
        raise SystemExit("Unmet calibration result; stopped without retry")
print(f"{args.phase}: {summary['matches']}/{len(cases)} agreement", flush=True)
