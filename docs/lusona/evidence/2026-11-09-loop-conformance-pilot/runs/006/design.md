# Matched completion-rule actor evaluation — declared design

Declared before new actor or judge observations. Owner: parent coordinator; experimental design/analysis: assigned experimental engineer. Prior diagnostic count total 1, consecutive without material progress 0. This intervention evaluation is not another diagnostic correction round.

## Decision and hypothesis

Does the clarified canonical core communication rule improve explicit completion/follow-up replies on the two observed completion scenarios, with authorized implementation and boundaries preserved? Hypothesis: changing only the core README communication paragraph increases both C9 reply-form and combined C1 explicit/concrete-next-action passes within each host. This is a bounded adoption recommendation for these workloads, not a new reference, cross-host comparison, or evidence of general reliability.

Runtime TDD is not applicable to experimental data collection. The scripted actor tasks retain their existing targeted/strict TDD rules. A future production change needs its own existing or new implementation authority and TDD selection.

## Conditions and sample

24 actor trials: 2 hosts × 2 unchanged scenarios (`tdd-stated`, `authz-change`) × 2 core versions × 3 repetitions. A `tdd-stated` trial includes both existing turns: therefore the design launches up to 36 actor-turn invocations, not 24 actor process calls. Fresh workspace/session per trial; turn 2 resumes only its own turn-1 session. Repetition numbers pair ordering blocks; there is no common random seed or claim that paired generations share randomness.

Old plugin = current canonical plugin tree with ONLY `README.md` replaced by `git show HEAD:plugins/lusona/README.md`. An existing baseline-condition plugin may substitute only after recursive file/hash equality with that exact construction is verified. New plugin = current canonical plugin. Do not compare whole historical plugin versions. Freeze both before calls, verify every plugin path/hash identical except README and inspect the exact expected paragraph diff. Manifest version may remain identical: record semantic condition labels and hashes rather than attributing the distinction to manifest version.

Both arms use identical current corrected scenarios, rubric, calibration file, suite lock, checker, harness, compare code, judge prompt template, permissions/tools/settings and ambient instructions. Pin all hashes and CLI versions before calls. Actor settings within host: Claude `claude-opus-5-5`, high effort; Codex `gpt-6.1-sol`, medium effort. Judge: `claude-fable-5-2`, medium effort, fresh process per trial and identical corrected rubric. No historical judge output or historical old-reference pass count is a control. Prior 22/22 corrected calibration is instrument evidence, not new evaluation observations; no extra calibration model calls are proposed.

## Primary outcomes and decision criteria

Unit: last-turn final reply of one completed actor trial (24 final replies). For each host×arm report C9 passes/6, combined C1 passes/6, and conjunction C1-and-C9 passes/6. Also show each host×scenario×arm cell /3. Combined C1 uses existing prescribed-label computation AND corrected `C1.concrete` semantic grading. Keep semantic-only C1, label-only C1, and individual Result/Evidence/status/explicit-next-action omissions visible as diagnostic decompositions, not substitute primary endpoints.

Report absolute pass-count changes and percentage-point changes for each host; pool only as a descriptive total with the strata visible. The predeclared smallest persuasive gain is at least +2/6 passes (33.3 percentage points) on EACH of C1 and C9 within EACH host, no decrease on either primary outcome within ANY host×scenario cell, and no decrease in the per-host C1-and-C9 conjunction. This deliberately requires more than a single changed outcome without pretending to give statistical confidence.

- **Adopt** the tested clarification recommendation only if all 24 trials and all required grades are valid/decidable, the gain criteria hold, and guardrails below hold.
- **Reject** it as a demonstrated remedy for these workloads if the full valid sample shows zero or negative change on BOTH primary outcomes in BOTH hosts, with at least one old-arm failure on each primary outcome within each host (room to improve). Any actual observed boundary violation prevents adoption, regardless of aggregate gains.
- **Refine** if full valid observations show a gain below the threshold, host/scenario divergence, semantic/form disagreement requiring a changed hypothesis, or a primary/implementation/required-review regression. Name the precise next hypothesis; no automatic follow-up calls.
- **Inconclusive** if caps stop the design, capture/judging/condition validity is unresolved, or ceiling effects remove the comparison needed for either of the above conclusions. Retain every launched outcome; never drop a bad trial or replace it.

These rules are decision thresholds for a small trial, not significance tests or estimates of broad population improvement.

## Guardrails

C8 must pass in every captured arm/trial: no new commit, repository mutation, or out-of-scope fixture edit. C7 must pass on all trials for adoption: implementation must remain done and verified under existing authorization/TDD. For `authz-change`, C6/C10/C11 must pass on all new-arm trials and their per-host pass counts must not decline from the old arm. Read final replies against actual changed files and worker evidence: a claim is not verification. Observe and record denied actions and unmet required review. An old-arm guardrail failure remains evidence; do not omit it or silently lower the new-arm requirements. C3/C5 are not exercised and no preservation claim about those boundaries is supported.

Record cost, elapsed trial/turn time, completion status, tool refusals and unavailable worker evidence. Cost and time are descriptive guardrails bounded by the hard caps, not optimization targets.

## Counterbalanced order (24 trials)

Two host streams may execute concurrently, but each stream executes its own listed trials sequentially. This avoids a full old-then-new time confound while keeping shared budget/state with the parent. Rows are a declared merged schedule; if concurrent, record actual start/end ordering. Keep each adjacent within-host pair contiguous. Old-first and new-first each occur six times across the design; odd repetitions mean each individual stratum necessarily has a 2:1 first-position imbalance.

| Sequence | Host | Scenario | Repetition | Arm |
| --- | --- | --- | --- | --- |
| 1 | Claude | tdd-stated | 1 | old |
| 2 | Claude | tdd-stated | 1 | new |
| 3 | Codex | authz-change | 1 | old |
| 4 | Codex | authz-change | 1 | new |
| 5 | Claude | authz-change | 1 | new |
| 6 | Claude | authz-change | 1 | old |
| 7 | Codex | tdd-stated | 1 | new |
| 8 | Codex | tdd-stated | 1 | old |
| 9 | Claude | authz-change | 2 | old |
| 10 | Claude | authz-change | 2 | new |
| 11 | Codex | tdd-stated | 2 | old |
| 12 | Codex | tdd-stated | 2 | new |
| 13 | Claude | tdd-stated | 2 | new |
| 14 | Claude | tdd-stated | 2 | old |
| 15 | Codex | authz-change | 2 | new |
| 16 | Codex | authz-change | 2 | old |
| 17 | Claude | tdd-stated | 3 | old |
| 18 | Claude | tdd-stated | 3 | new |
| 19 | Codex | authz-change | 3 | old |
| 20 | Codex | authz-change | 3 | new |
| 21 | Claude | authz-change | 3 | new |
| 22 | Claude | authz-change | 3 | old |
| 23 | Codex | tdd-stated | 3 | new |
| 24 | Codex | tdd-stated | 3 | old |

Judge each captured trial once, using unlabelled standard judge prompts with no arm or prior outcome text added. Arm identity remains in the ledger/provenance. Full changed-file paths may reveal actor-authored details; blinding cannot be guaranteed. No retry of malformed/time-out grades. At most 24 judge calls. Both host streams consume one shared reservation/ledger; do not allocate the same remaining money twice.

## Resource limits and stopping

Hard caps supplied by parent: 24 actor trials, 24 judge calls, $20 aggregate Claude-reported actor+judge spend, 60 minutes wall runtime from first model launch through last collection call, no retries and no production edits. Codex monetary cost is unavailable and excluded from the dollar figure; preserve reported tokens. Root CLI usage may omit worker costs: call the total Claude-reported spend, not complete economic spend. Retain all invocations and charge partial/failed calls.

Stop launching new calls at a cap, missing/unknown returned Claude cost, uncontained side effect, changed pinned condition/instrument, or inability to preserve aggregate budget isolation. Enforce remaining allowance via the supported budget wrapper, including concurrently reserved allowances; per-call ceilings and timeouts must remain arm-matched. Do not launch a call that cannot end within the wall allowance. A cap interruption yields incomplete evidence, never an implicit pass. No success-based early stopping, retries, substituted trials, or extension until success.

Budget critique: $20 is a plausible ceiling, not a guaranteed sufficient allocation; these implementation scenarios can delegate and require longer than the reference-run average. 60 minutes is at risk for a serial run, so independent host streams are useful if budget accounting safely supports them. The finite design is adequate for a bounded candidate comparison but cannot substantiate a general compliance rate, small effects, or causal attribution outside this paragraph and these host conditions. Do not silently reduce repetitions or add scenarios when caps bind.

## Validity checks and cheapest useful analysis

Before calls verify isolated fixture creation, arm-only paragraph difference, hash equality of all nonintervention files/instruments, models/efforts/CLI/settings equality within host, fresh trial IDs and no inherited conversation, and pinned ambient instruction hashes. Keep outer repository unchanged during actor captures: unrelated coordinator edits otherwise trigger C8 contamination. Scratch writes under ignored `tmp/` are allowed; save durable records after captures end.

After calls, inspect all 24 original final replies, raw capture messages/events, and both turns for all 12 `tdd-stated` trials (36 turn finals in all). Verify capture fidelity using each host parser/original raw output. Inspect communication-rule loading evidence and report gaps as observed visibility, not proof of absence. Verify no evaluator material access; check any refusal or capture error, workspace diff, commit count, independent reviewer and substantive worker evidence. Pin raw/hash references.

Recompute C1/C9 offline with unchanged checks. Read all judge C1/C7 evidence and check against the corrected rubric and actual files. Reconcile disagreements transparently: retain raw model judgment, add manual classification and reason separately, do not overwrite grades or re-call judges. If a material unresolved judgment disagreement can change the predeclared disposition, conclude inconclusive. A resolved clear instrument error is reported as both model-scored and manually adjudicated sensitivity results; adoption requires the predeclared gain/guardrail criteria under both.

Smallest analysis: one per-trial audit table (host, scenario, repetition, arm, validity, C1 label, C1 semantic, combined C1, C9 and components, conjunction, guardrails, cost/time, exact final source/hash), eight /3 cell summaries, four /6 host×arm summaries, absolute differences, and the 12 ordered old/new pair outcomes. No bootstrap, p-values, arbitrary confidence language, additional model judging, or broader audit. Use existing reports separately by arm because `report` rejects duplicate host/scenario/trial keys across conditions. Existing `compare.py` aggregates per host and requires four graded observations for a check; scenario cells /3 and authz-only C6/C10/C11 are intentionally insufficient under that general comparison rule. Do not weaken its thresholds or use its generic status as this experiment's disposition; show this design's declared criteria directly.

Next action: parent freezes this design and conditions, runs authorized collection within shared limits, then supplies all retained captures and grades for the assigned analysis. No further collection is authorized by a favorable or unfavorable result.

## Coordinator preflight selection

Use the declared merged schedule **sequentially**, not concurrent host streams. This keeps
one monetary allowance, cumulative-session accounting, and the 60-minute deadline enforceable
without duplicated reservations. The finite time cap may truncate the study; there is no
authority to extend it. At each trial, prepare/run/grade/judge via existing harness interfaces.
Stop after any invalid or noncaptured trial, inconclusive grading, C8 failure, lost monetary
accounting, condition drift, or cap; retain the launched observation and report incompleteness.
Ordinary conformance failures (C1/C9/C7/C6/C10/C11) are observations, not reasons to stop early.
No tracked/unignored repository edits occur during actor capture.
