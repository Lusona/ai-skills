#!/usr/bin/env python3
"""Run one host's share of a loop-conformance run, trial by trial, with a shared spend cap.

Scratch driver for the coordinator; not part of the suite. It calls the suite's run.py
subcommands (prepare, run, grade, judge) for every scenario and trial number, in trial-major
order so a stopped run stays balanced. It never retries: an existing trial directory is skipped.

usage: driver.py HOST CONDITION RUN_DIR CAP_USD SCENARIOS [TRIALS]

Adapted from run 003 for the W14 suite run: SCENARIOS is a comma-separated subset of the
condition's scenarios, and the spend cap is checked against the sum of every spend-*.json in
the sibling run directories (RUN_DIR/../*/spend-*.json), so confirmation, draft and reference
trials share one cap.
"""
import json
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[2]
RUN_PY = ROOT / "evals/loop-conformance/run.py"


def spend_of(trial_dir):
    """Claude-reported dollars for one trial: actor session cost plus its judge call."""
    total = 0.0
    trial = trial_dir / "trial.json"
    if trial.exists():
        total += json.loads(trial.read_text()).get("cost_usd") or 0.0
    judge = trial_dir / "judge.stdout.json"
    if judge.exists():
        try:
            total += json.loads(judge.read_text()).get("total_cost_usd") or 0.0
        except ValueError:
            pass
    return total


def total_spend(run_dir):
    return sum(json.loads(p.read_text())["usd"] for p in run_dir.parent.glob("*/spend-*.json"))


def main(argv):
    host, condition, run_dir, cap = argv[1], pathlib.Path(argv[2]), pathlib.Path(argv[3]), float(argv[4])
    wanted = argv[5].split(",")
    trials = int(argv[6]) if len(argv) > 6 else 5
    run_dir.mkdir(parents=True, exist_ok=True)
    log = (run_dir / f"driver-{host}.log").open("a")
    spend_file = run_dir / f"spend-{host}.json"
    known = list(json.loads((condition / "scenarios.json").read_text()))
    missing = [s for s in wanted if s not in known]
    if missing:
        raise SystemExit(f"unknown scenarios: {missing}")
    scenarios = wanted
    spent = json.loads(spend_file.read_text())["usd"] if spend_file.exists() else 0.0

    def say(text):
        log.write(f"{time.strftime('%H:%M:%S')} {text}\n")
        log.flush()

    say(f"start host={host} condition={condition} trials={trials} cap={cap} scenarios={len(scenarios)}")
    for number in range(1, trials + 1):
        for scenario in scenarios:
            if (run_dir / "STOP").exists():
                say("STOP file present; exiting")
                return 3
            if total_spend(run_dir) >= cap:
                (run_dir / "STOP").write_text(f"spend cap {cap} reached at {total_spend(run_dir):.2f}\n")
                say("spend cap reached; exiting")
                return 3
            out = run_dir / host / scenario / str(number)
            if out.exists():
                say(f"skip existing {scenario} {number}")
                continue
            started = time.time()
            steps = [("prepare", ["prepare", "--condition", str(condition), "--scenario", scenario,
                                  "--trial", str(number), "--out", str(out)]),
                     ("run", ["run", "--trial", str(out)]),
                     ("grade", ["grade", "--trial", str(out)]),
                     ("judge", ["judge", "--trial", str(out)])]
            codes = {}
            for name, args in steps:
                proc = subprocess.run([sys.executable, str(RUN_PY), *args], cwd=ROOT,
                                      stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                codes[name] = proc.returncode
                if proc.returncode != 0:
                    say(f"  {name} exit={proc.returncode} {proc.stderr.strip()[-300:]}")
                    if name == "prepare":
                        break
            cost = spend_of(out)
            spent += cost
            spend_file.write_text(json.dumps({"usd": spent}))
            status, outer = "?", "?"
            if (out / "trial.json").exists():
                record = json.loads((out / "trial.json").read_text())
                status, outer = record.get("status"), record.get("outer_changed")
            say(f"done {scenario} {number} status={status} outer_changed={outer} codes={codes} seconds={time.time() - started:.0f} "
                f"cost={cost:.3f} host_total={spent:.2f} all_hosts={total_spend(run_dir):.2f}")
    say("finished all trials")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
