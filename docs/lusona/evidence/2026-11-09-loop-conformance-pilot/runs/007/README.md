# Run 007 — direct instructions and scoped completion validation

Owner: [implementation spec](../../../../specs/20261109-direct-instruction-checkpoints.md).
Prior context: [run 006](../006/README.md). This is bounded implementation verification,
not a replacement reference or a reliability benchmark.

## Result

The four source changes are implemented, with the user's agreed balance of one authoritative
policy definition and useful short local instructions. Deterministic checks pass. **Behavioral
acceptance remains unmet:** both candidate tasks still perform substantive implementation in
the coordinator instead of delegating it. The implementation item remains open.

All three candidate final replies satisfy the structural format. One initially omitted its
status and valid next-action form; the native Stop hook requested exactly one rewrite. The actor
repaired that reply without further tool actions or re-arming. A compliant format does not
establish that the required process or a useful next action was followed.

## Method and provenance

[Design](design.md) and [exact cases](planned-cases.json) were frozen before calls. One Claude
Code trial per scenario (`tdd-stated`, `authz-change`) per arm: four trials and six actor-turn
calls. `tdd-stated` keeps its two turns in the same session. Host Claude Code 2.1.322,
model `claude-opus-5-5`, high effort. Existing suite prompts, fixtures, runner, checker and
rubric were unchanged. No model judge calls, retries, discarded cases or added trials.

The pre-edit baseline includes the earlier completion-rule correction. Candidate combines
revised instructions, examples and native hooks; this cannot identify their separate effects.
The root host's global instructions remained present in both arms, despite isolated fixture
workspaces. Source pins and full conditions/captures are retained in the raw archive.

The user requested a discussion pause during implementation, then explicitly resumed work.
The original 40-minute window had less than one fixed 600-second call allowance remaining.
A [prospective timing amendment](timing-amendment.md) gave only the two already-planned
candidate trials a fresh 30-minute window. Original design, collector and baseline ledger
remain intact. Four trials/six calls/$8 aggregate, fixed $2 cumulative per-session budget,
600 seconds per call and no retries stayed unchanged. This timing change is a protocol
qualification, not evidence of perfect condition equality.

## Observed behavior

| Condition | Baseline | Candidate |
| --- | --- | --- |
| Final reply structure, all turns | 1/3 | 3/3 after one native repair |
| Task behavior and matched fixture checks | Pass, 4 checks | Pass, 4 checks |
| Actual selected TDD sequence | Pass in both tasks | Pass in both tasks |
| Substantive implementation delegation | Fail in both tasks | Fail in both tasks |
| Independent security-change review | Pass | Pass |
| No added commit or outer-repository mutation | Pass | Pass |
| Overall semantic trial grade | 0/2 pass | 0/2 pass |

Independent [baseline grades](baseline-grades.md) and [candidate grades](candidate-grades.md)
retain actual tool actions, test ordering, native reviewer evidence, per-condition decisions
and exact capture references. The candidate's second `tdd-stated` next-action usefulness is
inconclusive: it proposes cleaning host files that were not inspected. Structural acceptance
does not resolve that semantic question.

The failed delegation has two observed paths:

- The `tdd-stated` captures show the skill injected but no read of the authoritative core.
  This is a loading gap in visible evidence, not proof of the actor's internal cause.
- The candidate `authz-change` actor reads the core, identifies itself as coordinator, and
  explicitly acknowledges bypassing implementation delegation because the fix was two lines.
  A loading-only change cannot be claimed to solve that case.

No policy relaxation, broader rewrite, extra actor calls or claim of improved general
reliability follows from these four trials.

## Native integration and deterministic verification

[Hook observations](hook-observations.json) and [native Stop events](native-stop-observations.json)
show three candidate SessionStart contexts, three explicit arm commands, four Stop invocations
including the repair continuation, and one blocking feedback message. The native
`stop_hook_error` notification in that sequence is the expected request to rewrite, not a
script crash. The corrected reply triggers no second repair.

The [static check receipt](static-checks.json) records 177 passing Python tests: 32 validator,
12 package, 11 instruction and 122 unchanged loop-suite tests. Instruction/skill/link checks,
package build, Claude plugin/marketplace validation and Antigravity source/extracted validation
also pass. Both actual hypothetical examples pass the standalone validator. Tests cover
unarmed/override/worker bypass, one-shot repair, expiry, session/cwd isolation and state-path
symlink handling. These fixtures do not prove live behavior on every host.

Targeted red/green logs preserve missing-field rejection and missing native repair before
implementation; positive acceptance/bypass controls initially passed the minimal scaffold and
are characterization, not individual red evidence. Three bounded parser corrections have
retained regression red/green: optional outer table pipes, Result/Evidence labels/status window,
and Next action label syntax. Packaging red showed hook resources missing from the archive.

Actor capture predates the final Next action label parser correction. Compare
[candidate source hashes](candidate-source-hashes.json) with [final source hashes](final-source-hashes.json):
only the validator and its tests changed after capture. The final correction has deterministic
and [independent code-review coverage](final-review.md); it has not received another actor trial. The earlier
captured candidate remains recoverable unchanged.

## Resources and limits

- Four captured trials, six actor calls, no retries/judges/cap stops/unrun trials.
- $1.7596393 Claude-reported spend: $0.8214538 baseline plus $0.9381855 candidate. Root CLI
  reports may not establish complete worker economic cost.
- Candidate collection: 122.27 seconds under its amended 30-minute window.
- One host/model, one repetition per scenario/arm. No significance, general reliability or
  cross-host claim. Initial-format compliance and successful repair are distinct observations.
- Live Codex hooks, native Windows hooks, user installation and publication were not tested.
  Hooks require Python 3, supported POSIX state operations, host trust and agent activation.
  Missing activation or unsupported/untrusted hooks leave manual checking in use.
- OpenAI's current public-directory route excludes plugins containing lifecycle hooks; the
  repository installation guide records this limitation. No publication was requested.

## Retention and next action

The original ledgers are retained as [baseline](baseline-ledger.json) and
[candidate](candidate-ledger.json), alongside declared design/amendment, source pins,
fixture checks and independent grades. Worker collection summaries reflect when they were
written and use their original scratch-relative paths, recoverable from the archive; the final
independent review and this record own reconciliation.

`raw.zip` is ignored and local to this machine. It preserves baseline/frozen candidate sources,
raw actor and native worker transcripts, fixture artifacts, collectors, red/green logs, review
artifacts and final source files. [Provenance](provenance.json) records hashes and archive integrity.
Scratch remains under `tmp/direct-instruction-checkpoints/`; isolated fixtures remain under
`~/.cache/lusona-evals/`. No actor process remains active.

Next action: define a bounded correction for the observed loading gap and explicit size-based
rule bypass, preserving the existing delegation policy. Candidate acceptance needs further
behavioral verification; the four-trial allocation is consumed. Do not silently extend this
sample or close the item on passing formatting/code checks alone.
