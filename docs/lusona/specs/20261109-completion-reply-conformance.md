# Spec 20261109-completion-reply-conformance: Completion replies and C1 grading

Created: 2026-11-09
Updated: 2026-11-09

Kind: bug fix
Work item: [Historical completion](../history/2026-11-week-02.md#2026-11-09--completion-reply-conformance)
Context: [diagnosis and decision](../notes/completion-reply-conformance.md),
[offline audit run 004](../evidence/2026-11-09-loop-conformance-pilot/runs/004/README.md)

## Agreement

- User and problem: Lusona users need completion replies that state the result, evidence,
  status, and next action. Existing actor replies omit required content, and the semantic
  judge sometimes treats completion or review success as an explicit no-action statement.
- Desired behavior: the core communication rule explicitly covers every substantive final
  reply to the user, including implementation completion and follow-up turns. The next-action
  or no-action statement must appear in that reply. C1 judges that meaning consistently.
- Scope: clarify the communication paragraph in [canonical core](../../../plugins/lusona/README.md#review-and-communication);
  correct [C1 rubric](../../../evals/loop-conformance/rubric.md) and
  [judge calibration](../../../evals/loop-conformance/judge-calibration.json), with the
  corresponding suite lock and directly affected validation documentation as needed.
- Exclusions: no broader workflow redesign, C9 relaxation/parser change, C1 label-computation
  change, actor study, full reference rerun, installation, commit, push, or publication.
- Accepted constraints: retain status meanings, next-action fields and prescribed form,
  proposed-follow-up authority requirements, user/host formatting overrides, and the
  exception for assignment results returned to a coordinator. Preserve evaluator-only
  isolation and historical reference/audit artifacts under the
  [suite contract](../../../evals/loop-conformance/README.md).
- Completion condition: AC1–AC5 verified, required repository checks and independent review
  complete, with actual limits recorded. Implementation authority is recorded in the current
  handoff. No additional human acceptance gate is required.

### Acceptance criteria

- [x] AC1: The core explicitly applies its Result/Evidence labels, status, and next-action
  defaults to substantive final replies, including implementation completion and follow-up
  replies. It requires the next/no-action statement in the reply itself; saved records and
  an earlier turn's statement do not substitute. Existing overrides and exceptions remain.
- [x] AC2: C1.concrete requires a specific next action and owner with supported authority,
  or an explicit statement that no next action is needed with a reason. Completion claims,
  passing tests, an independent review result, and a saved next action do not imply that
  statement. The `authz-change` passing example explicitly states no next action is needed.
- [x] AC3: Hand-labelled C1 calibration pairs distinguish silent implementation completion,
  completion reporting independent review, and a next action only in saved notes from
  equivalent replies with an explicit current-final next/no-action statement. Silent cases
  fail; explicit counterparts pass when the remaining C1 conditions hold. The `tdd-stated`
  pair retains its two-turn context so the previous reply does not substitute for the final
  reply. Existing valid proposed follow-ups with owner and authority still pass.
- [x] AC4: Actual judge calibration agrees with the frozen expected labels for the focused
  pairs and retained calibration controls. Record per-case judgments, evidence, settings,
  hashes, agreement, and any mismatches. Mocked judgments, fixture/schema checks, and wording
  assertions do not establish semantic agreement or red/green evidence.
- [x] AC5: Existing computed C1 and C9 behavior is preserved: substantive meaning under an
  alternative label still fails prescribed C1 form where C9 applies; missing required C9
  labels/status still fail; C1 remains judged-only where C9 does not apply. Refresh suite
  integrity hashes without replacing historical evidence. No comparison with the old
  reference is presented as matched after the rubric/calibration hashes change, and no actor
  improvement is claimed from this correction or judge calibration alone.

### Decisions and uncertainty

- Accepted: the smallest correction is both the rule clarification and C1 rubric/calibration
  correction, preserving C9 and computed C1. Source: the diagnosis linked above and the user's
  request to specify that correction.
- The wording's effect on actor compliance remains unknown. A later actor study would need
  its own bounded question, matched grading conditions, scope, and authority; it is not a
  prerequisite for completing this source and grading correction.
- Verification allowance authorized by the user's Implement invocation: six new focused cases, one
  baseline pass of those six and one candidate pass of all 22 cases (the existing 16 plus
  six), at most 28 judge calls and $10 total. Stop at either cap or an unmet candidate result;
  retain every outcome and do not retry to obtain passes. This allowance is covered by the
  user's 2026-11-09 Implement invocation following the specification and budget summary.
  No actor runs are authorized. No definition-blocking behavior or scope decision remains.

### TDD policy

- Level: targeted.
- Selected by user: explicit `TARGETED` selection in the 2026-11-09 specification request.
- Test-first behaviors: reject silent implementation completion, silent completion
  reporting independent review, and a next action present only in saved notes as
  C1.concrete passes. Freeze expected labels and focused
  inputs before production edits, observe at least one intended known silent-completion
  mismatch on unchanged production inputs, then verify corrected judgments. Existing exact
  archived failures can supply red only when inputs, rubric, settings, and provenance match;
  derived cases need their own observations. A baseline that already agrees is characterization
  evidence, not an invented red. If no intended mismatch is observed, report the defect as
  not reproduced in that check and resolve the selected TDD sequence before substituting
  another approach.
- Required regressions: explicit no-action passes with reasons; concrete proposed follow-ups
  with owner/authority; notes-only and previous-turn-only statements fail; existing computed
  C1/C9 tests and calibration controls remain valid. Preserve the distinction between
  semantic omission and form-only failure. These regressions do not require new tests that
  duplicate adequate existing coverage.

### Bug evidence

- Expected versus observed: substantive completion replies should follow core communication
  defaults. In 40 audited finals, all 33 C9 failures omit Result; 15 omit an explicit
  next/no-action statement, five contain a next action under an alternative label, and seven
  silent finals receive false semantic passes. No observed C9 failure is a parser false
  negative. Full inputs, environment, provenance, affected trials, and reproduction are
  retained in run 004; counts describe this sample only.
- Confirmed defect: inconsistent semantic grading of silent completion. The cause of actor
  omissions is unconfirmed. Neither missing loading nor a host override explains the whole
  sample; no benefit from the proposed wording has been measured.

## Verification

- Use the existing `run.py judge --calibration` interface with frozen conditions and case
  files for baseline/candidate judging. Keep judge model, effort, prompt template, case
  inputs, and expected labels matched; only the intended rubric changes between phases.
  The six-case focused file can be retained under repository-local `tmp/` with material
  results saved in the owning evidence record. No runner feature or actor invocation is
  required. The proposed finite allowance above bounds this check.
- `python3 -m unittest discover -s evals/loop-conformance -p 'test_*.py'` checks suite integrity,
  calibration plumbing, computed checks, and comparison boundaries. It does not verify
  semantic judge correctness. Run canonical instruction/link/package checks appropriate to
  the actual diff; do not update generated packages as source.
- Independently review the actual rule/rubric/calibration diff against AC1–AC5 and the raw
  calibration evidence. Preserve old reference/audit files; freeze new conditions after
  updating the suite lock rather than modifying prior conditions.

## Evidence

- [Run 005](../evidence/2026-11-09-loop-conformance-pilot/runs/005/README.md) owns the exact
  frozen inputs, source/settings hashes, per-case judgments, budget ledger, raw artifact
  reference, repository checks, and review findings.
- AC1–AC3: canonical core and C1 rubric clarified; six frozen calibration cases added after
  the existing 16 unchanged controls. Independent review verified the source and cases.
- AC4: fresh six-case baseline agreement 5/6; intended silent authz-completion false pass
  observed before production edits. Candidate focused agreement 6/6 and full calibration
  22/22. All 28 calls retained, no retries; total reported cost $5.2512512.
- AC5: computed C1/C9 and historical reference unchanged; 122 suite tests and 21 repository
  tests pass. Package, links, native plugin, and marketplace validation pass. New suite hashes
  are recorded; no matched historical comparison or actor-improvement claim is made.
- Independent reviewer `completion_review`: no actionable findings; verified all raw
  prompts, judgments, costs, case provenance, and preserved constraints.
- Definition received its inline contradiction/link check. During implementation, no actor
  trials, installation, or interactive behavior tests ran. Actor compliance is unmeasured.
  Changes remain uncommitted; no publication was requested.

## Current handoff

- Authorized work: the user's 2026-11-09 Implement invocation covered this spec, targeted TDD,
  and the 28-call/$10 calibration allowance. The authorized implementation is complete;
  the 28-call allowance is exhausted. No commits or publication were authorized.
- Completed: AC1–AC5, required checks, independent review, evidence retention, and closeout.
  Human acceptance was not an additional completion requirement. State is owned by history.
- Workers: implementation and independent review assignments completed and returned their
  results; no active operations or children remain. Host completion is observed, without
  claiming a separate capacity-release operation unavailable in the tool surface.
- Diagnostic history: total 1, consecutive without progress 0; no implementation correction
  round was added. Expected task-local TDD red is excluded.
- Recovery: material evidence is retained in run 005; scratch conditions, driver, outputs,
  and local package remain under `tmp/completion-reply-implementation/`. Raw archives are
  git-ignored local artifacts, with hashes and access paths in the evidence record.
- Next action: none to complete this implementation. An optional matched actor evaluation
  is a separate proposal in the work queue; it requires defined scope, budget, and authority.
