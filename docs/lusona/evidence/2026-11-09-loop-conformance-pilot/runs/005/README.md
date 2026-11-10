# Run 005 — completion-rule and C1 calibration correction, 2026-11-09

Owner: [completion-reply spec](../../../../specs/20261109-completion-reply-conformance.md).
Preceding diagnosis: [offline audit run 004](../004/README.md).

## Design and authority

The user's Implement invocation authorized targeted TDD and the specified finite validation:
six new paired calibration cases against the original rubric, then those six plus the existing
16 controls against the corrected rubric. At most 28 judge calls and $10 total; stop at either
cap or an unmet candidate result. No actor trials, full reference run, retry-to-pass, installation,
commit, or publication. All expected labels and six focused inputs were frozen before baseline
calls and production edits. This tests semantic grading, not actor conformance.

[Focused inputs](focused-cases.json) and [provenance](focused-provenance.md) identify three
negative/positive pairs: two-turn implementation completion, completion with independent review,
and action only in saved notes. Pair members differ only in the final next/no-action statement.
Derived cases require fresh baseline observations; prior archived grades are not substituted.

## Method

Use the existing `run.py` calibration interface, one case per invocation, through a task-local
sequential driver. It records every call before launch, appends the supported Claude CLI
`--max-budget-usd` with the remaining aggregate allowance, accounts returned cost after each call,
and stops on missing cost, inconclusive output, cap, or candidate mismatch. Prompts and judgment
parsing are the existing harness's; the budget wrapper is identical between phases. Scratch
conditions and outputs are under `tmp/completion-reply-implementation/`; isolated judge working
directories use the harness's existing `~/.cache/lusona-evals` root. No actor is invoked.

Judge: `claude-fable-5-2`, medium effort. Model, effort, prompt template, focused case inputs,
and expected labels stay matched between phases. [Baseline condition](baseline-condition.json)
pins plugin/suite/code hashes, CLI versions, and judge settings. [Candidate condition](candidate-condition.json), [usage ledger](budget.json), and
[provenance](provenance.json) retain final settings, commands, hashes, and costs. Baseline
core/rubric were frozen before production edits. The candidate evaluated the six focused cases
first, followed by the original 16 controls; each case used a fresh judge process.

## Baseline observations

[Baseline summary](baseline-summary.json): 5 / 6 agreement; six calls, $1.2092664 reported cost.

- `c1-fail-authz-completion-review`: expected fail, judged pass. The judge explicitly calls
  this a “pass by implication only” because review completion matches the old passing example.
  This is the intended test-first failure.
- Silent two-turn implementation completion and notes-only action are correctly rejected;
  these are passing characterization coverage, not red evidence.
- All three explicit current-final next/no-action counterparts pass.

## Candidate observations and verification

[Candidate summary](candidate-summary.json): **22 / 22** agreement. The same six focused
cases improved from 5 / 6 baseline agreement to 6 / 6; the 16 unchanged controls all matched.
The previously incorrect authz-completion pass is now a fail, with the judge citing the missing
explicit statement. These are single judgments per input and phase, not a reliability estimate.

- Calls: 6 baseline + 22 candidate = **28**, no retries or excluded outcomes.
- Reported cost: baseline $1.2092664 + candidate $4.0419848 = **$5.2512512**, below $10.
- [Repository checks](repository-tests.txt): 21 instruction/package tests passed.
- [Suite checks](suite-tests.txt): 122 tests passed, including unchanged C1/C9 behavior,
  calibration plumbing, suite integrity, and comparison compatibility.
- [Package build](package-check.txt) passed native identity/version, catalog, links, and
  packaging exclusions. Claude plugin and marketplace validation both passed. The plugin
  validator's advisory about an installation line is unrelated and does not change its verdict.
- Independent reviewer `completion_review`: no actionable findings in the five production
  files. Verified frozen pair isolation, original 16 controls, source provenance, per-case raw
  prompts/judgments/hashes/costs, preserved overrides, and unchanged parsers/reference files.
- Implementation changed canonical core, rubric, calibration, suite lock, and suite README.
  The historical reference and computed C1/C9 checks were not modified.

## Retained artifacts and reproduction limits

`raw.zip` holds the full baseline/candidate conditions, every prompt, stdout/stderr, call record,
case input, and the task-local driver at original repository-relative paths. Its SHA-256 is in
[provenance](provenance.json). Like run 003's raw archive, it is git-ignored and retained only
on this machine. Small per-case summaries, cases, conditions, costs, and verification logs are
retained alongside this README. The [driver copy](calibrate_bounded.py) is the original script
written for `tmp/completion-reply-implementation/`; it must be restored there, not executed from
this evidence directory. It creates fresh phase outputs and does not overwrite prior results.
Its ledger has exhausted the 28-call allowance; a new model run needs new authority.

Original execution commands, from repository root:

```sh
python3 tmp/completion-reply-implementation/calibrate_bounded.py baseline tmp/completion-reply-implementation/worker/focused-cases.json
python3 tmp/completion-reply-implementation/calibrate_bounded.py candidate tmp/completion-reply-implementation/candidate-cases.json
```

Both conditions were made with the existing `run.py freeze` command, host `claude`, actor metadata
`claude-opus-5-5`/high (no actor invocation), judge `claude-fable-5-2`/medium, timeout 180 seconds.
The budget wrapper adds the supported spend option to each judge command; the ledger records
the actual command and available allowance, while ordinary harness call records retain the
unwrapped command. This wrapper is not a production runner change.

## Conclusion and limits

The correction passes AC1–AC5: completion coverage is explicit and the corrected semantic
rubric grades all 22 declared cases as expected. The one observed baseline grading error was
corrected without losing the retained controls. Independent review and required checks passed.
No actor trial, installation, or interactive behavior test ran; improved actor compliance is
unmeasured. New suite hashes prevent a matched comparison with the historical reference.
No commits or publication were authorized or performed.

The initial investigation used one diagnostic round; implementation added no correction round
beyond expected task-local TDD red. Total 1, consecutive without progress 0.

