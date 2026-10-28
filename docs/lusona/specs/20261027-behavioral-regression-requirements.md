# Spec 20261027-behavioral-regression-requirements: Behavioral regression requirements

Created: 2026-10-27
Updated: 2026-10-27

Kind: contributor requirements and evaluation documentation
Work item: [Completion record](../history/2026-10-week-04.md#2026-10-27--behavioral-regression-requirements)

## Agreement

- User and problem: contributors and maintainers need a consistent, proportionate way to
  establish whether a skill change achieves its intended behavior while preserving relevant
  boundaries. A representative prompt and structural checks alone do not establish regression coverage.
- Desired behavior: contributors select relevant cases, preserve interpretable evidence,
  obtain independent outcome grades, and report results and limits in a form maintainers can assess.
- Scope: contribution and evaluation guidance, the pull request evidence requirements,
  reusable examples, and a bounded exercise demonstrating selection and assessment of evidence.
  Reuse the [existing evaluation assets](../../../evals/evidence-aware/README.md) and
  [evidence procedure](../../../plugins/lusona/references/evidence.md) where applicable.
- Constraints: preserve explicit TDD selection, user authority, truthful completion, and
  proportional process. Keep requirements with their existing owners and link instead of
  duplicating them. Canonical workflow changes, if needed, belong under `plugins/lusona/`.
- Completion: AC1–AC7 are satisfied, independent review of the requirements and exercise
  evidence is complete, and applicable repository checks pass. Installation and interactive
  behavior remain untested unless separately exercised; no release or deployment is required.

Excluded: changing delegation, context-loading, authorization, or TDD defaults; adding startup
hooks; a general evaluation framework; mandatory CI enforcement; universal host coverage;
performance benchmarking; unrelated catalog corrections; commits and publication.

### Acceptance criteria

- [x] AC1 — Proportionate case selection. For a skill behavior change, a contributor identifies
  the observable change, affected boundaries, and why the selected cases cover them. Include a
  positive case and a relevant negative or boundary case. Include multi-turn coverage when
  correctness depends on steering, retained authority, or resumption. Shared instruction changes
  cover affected responsibilities with a justified representative selection. Cases may satisfy
  multiple needs; every case and host need not run for every contribution. Editorial changes
  preserving behavior may use content/link checks with a recorded rationale.
- [x] AC2 — Interpretable comparison. Before trials, record cases and outcome criteria,
  baseline/candidate identifiers or hashes, host/version, model/reasoning settings, relevant
  capabilities and permissions, exact inputs, and a finite run budget and stopping condition.
  Use an unchanged baseline captured before relevant edits or recoverable from a pinned snapshot.
  Preserve relevant conditions except for the intended change; disclose mismatches and restrict
  resulting claims. Multi-turn cases preserve their sequence within the same trial session.
  Actors do not receive evaluator rubrics, prior outcomes, or desired answers.
- [x] AC3 — Independent grading. A person or agent independent of the actor grades retained
  conversation, observable actions, and resulting artifacts against the frozen criteria.
  Evaluate outcomes and boundaries, not prescribed wording, headings, tool order, or question
  counts. Use deterministic state checks where useful. Retain evaluator identity, evidence
  locations, rationale, and unresolved disagreement. A successful process exit is not a pass.
- [x] AC4 — Honest results and limits. Report pass, fail, inconclusive, or setup-blocked for
  attempted trials and explicitly identify planned but unrun trials. Setup errors, missing
  capabilities, timeouts, incomplete captures, and unresolved grading disagreement cannot
  become passing evidence or behavioral red. Observed authority or scope violations fail the
  applicable trial. Summaries include unfavorable and incomplete results, unrun required checks,
  and host/model limits. Preserve earlier attempts and record the reason and authority for
  retries or budget changes. Do not infer missing usage, total cost, or statistical significance.
- [x] AC5 — Explicit test-first evidence. Record the selected TDD policy and its source;
  distinguish named test-first behaviors from regression coverage. For behavior subject to
  test-first sequencing, demonstrate the intended baseline failure before changing relevant
  instructions, then obtain matched candidate evidence. Passing baseline cases remain
  characterization coverage. Setup failures, textual disagreement, or weakened criteria are
  not red evidence. Resolve an infeasible selected sequence before substituting another;
  behavior-preserving clarification does not require a manufactured failure. TDD `none` does
  not remove the requirement for relevant behavioral verification.
- [x] AC6 — Durable, reviewable contribution evidence. Contributor guidance and the pull request
  template request TDD policy, selected cases and rationale, condition identifiers, independent
  grades, outcome summary, exact evidence references, and limitations. Editorial-only changes
  can explain why behavioral trials are unnecessary. Retain enough provenance and access
  information to inspect claims; material evidence or a durable reference survives scratch
  cleanup. Do not require large transcripts in Git or leave disposable `tmp/` as the only
  support for a lasting claim. Routine verification stays with its existing owner.
- [x] AC7 — Demonstrated usability. A bounded exercise records expected and observed assessments
  of synthetic or retained records: a valid matched comparison; incompatible comparison
  conditions; setup failure presented as behavioral red; a pass claim without independent
  evidence; and an editorial-only change eligible for static checks. At least one example
  includes multi-turn evidence. The exercise demonstrates case selection and evidence assessment,
  not installed-host adherence. It may reuse fixtures without creating a runner or making live
  model calls. Relevant content/link and whitespace checks pass; manifest/catalog, packaging,
  and executable checks apply when their files or contracts are affected. Required checks that
  cannot run remain unmet.

### Decisions and uncertainty

- Accepted by the user: the bounded scope is behavioral regression requirements; TDD is targeted.
- Accepted acceptance criteria: the user's subsequent `lusona:implement` request accepts
  AC1–AC7 and authorizes this bounded implementation with the selected targeted TDD policy.
- Routine implementation choices: document placement, case identifiers, and evidence format.
  Reuse current assets; a new validator is not a required deliverable.
- No runtime improvement or reduced cost is claimed. Current assets support a useful starting
  point, not proof of coverage across all skills, models, or installations.

### TDD policy

- Level: targeted, explicitly selected by the user for this change.
- Test-first behaviors: any new or changed executable selection or evidence-validation behavior,
  if implementation introduces it. Name those behaviors and observe relevant failures before
  changing executable code, then verify green.
- Requirement prose and examples receive content review and the AC7 exercise; do not add tests
  that merely mirror their wording or manufacture a failing cycle for documentation.
- Any runtime skill behavior change introduced within this scope must name its test-first
  behavior and establish actual baseline/candidate evidence under AC5 before adoption.
- Required regression coverage: relevant existing evaluation-runner tests if its behavior
  changes, the positive and invalid-evidence cases in AC7, and applicable repository checks.

## Verification approach

Use the existing [outcome rubric](../../../evals/evidence-aware/rubric.md) and
[contribution guidance](../../../CONTRIBUTING.md) as inputs to the revised requirements.
Keep evaluator criteria separate from any acting agent's input. Independently review the
requirements and exercise evidence for contradictory rules, unsupported claims, and disproportionate
burden. This exercise does not require a live-call budget. If live trials later become necessary,
record scenarios, conditions, maximum trials, per-turn limits, stopping conditions, and effective
execution authority before running them. Specification alone authorizes no such trials.

## Execution

- Update contributor guidance and the pull request template; retain existing evaluation
  assets and runtime defaults. Documentation and examples need no manufactured red/green cycle.
- Create five synthetic evidence packets and an evaluator-only key before assessment. Have
  an independent contributor-role worker apply the requirements without reading the key, then
  independently grade its responses and review the actual diff against AC1–AC7.
- Retain exact exercise inputs, observed assessments, independent grades, and limits in durable
  records. Check affected links, whitespace, package contents, and native manifests/catalogs.

## Evidence

- Definition: inspected contributor instructions, pull request template, evaluation runner and
  tests, six synthetic scenarios, outcome rubric, and shared evidence retention rules.
- Existing assets already support frozen conditions, resumed turns, independent grading, and
  preservation of unfavorable results. This change makes their relevant practices reusable in
  contributor requirements; it does not replace the existing suite or rewrite historical results.
- Definition validation: checked scope consistency, observable criteria, TDD compatibility,
  and evidence limits. Local links, AC1–AC7 identifiers, dates, selected TDD, requested wording
  constraints, placeholders, and whitespace checks pass, including `git diff --check`.
- Implementation: contribution requirements and the pull request evidence fields are updated;
  [five synthetic packets and a separate review key](../../../evals/regression-requirements/README.md)
  provide the AC7 exercise. No executable or runtime skill changes were needed, so targeted TDD
  is satisfied through the prescribed content review and exercise without a fabricated red cycle.
- [Run 001](../evidence/2026-10-27-behavioral-regression-requirements/runs/001/README.md)
  retains frozen inputs, the exact contributor assessment, independent grading/diff review,
  provenance, and verification. Four packet assessments pass; Packet C partially fails because
  its recovery advice omits resolution of an already-broken test-first sequence. The original
  response and key remain unchanged; the run records corrected advice separately. No retry or
  five-clean-passes claim was made. Independent review found no actionable implementation defects.
- AC1–AC6 are mapped to the implemented requirements in the independent review; AC7 is satisfied
  by the observed exercise and retained discrepancy, not a claim of flawless assessor behavior.
  Native plugin/catalog validation, package generation, archive source/exclusion checks, affected
  links/anchors, and whitespace pass. Existing unrelated edits are preserved.
- No installed-host or CLI behavioral trials were performed; installation and interactive behavior
  remain untested. Assessor key separation is instructional and self-reported, not independently
  proven from a full tool transcript. No runtime, performance, or cross-model improvement is claimed.

## Current handoff

- Authorized work: implement AC1–AC7, from the user's `lusona:implement` request, with previously
  selected targeted TDD. No commit or publication authority.
- Completed: AC1–AC7, contribution guidance, PR fields, bounded exercise, independent grading
  and diff review, repository checks, and retained partial-failure reconciliation. History owns
  archived state. No further human acceptance or delivery gate is required by the agreement.
- Remaining: none for the authorized implementation. Installation/runtime behavior is outside
  this change's verification scope and has not been claimed.
- Try it: use CONTRIBUTING's Behavioral evidence section and the pull request template to select
  and report evidence; the exercise README explains how to assess the synthetic records without
  exposing the reviewer key. Expected outcome: proportionate coverage and explicit evidence limits.
- Correction rounds: one during initial authorship restored the existing script-TDD sentence
  and clarified human/agent assessment wording; material progress, consecutive no-progress 0,
  total 1. No assessment retry has occurred.
- Exercise limitation: Packet C's recovery recommendation partially failed independent grading;
  this is retained evidence, not an implementation correction round or a silently repaired trial.
- Next action: none for this request. Changes are local and uncommitted.
