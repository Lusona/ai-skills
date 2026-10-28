# Spec 20261027-proportionate-evidence-work: Proportionate evidence work

Created: 2026-10-27
Updated: 2026-10-27

Kind: workflow simplification
Work item: [Work queue](../work.md)

## Agreement

Users need ordinary development to continue without unnecessary studies, delegation, or
paperwork. Contributors need verification proportionate to the behavior, risk, and claim.
Required correctness checks and truthful completion remain binding.

Scope: narrow study-entry and contribution-evidence requirements in their current owners,
including affected core/skill guidance, references, PR fields, and examples. Replace conflicting
rules rather than adding another process layer. This prospectively changes parts of the
[previous contribution requirements](20261027-behavioral-regression-requirements.md);
its completed work, frozen evidence, and historical results remain intact.

Excluded: broad core instruction reduction, general delegation redesign, a new policy taxonomy
or required configuration file, universal numeric budgets, a new evaluation framework, performance
benchmarking of Lusona, commits, and publication. Core loading/deduplication remains a separate
proposed follow-up. No latency or cost reduction is claimed from source changes alone.

### Acceptance criteria

- [x] AC1 — Discretionary studies. Ordinary design alternatives and optional uncertainty do
  not automatically launch measurements/experiments or block implementation for an unset study
  preference. Optional studies need an explicit request or applicable standing authority and
  a finite scope/resource budget. The agent may choose routine bounded execution details within
  that authority; an explicit request does not cause another approval round. Ask only for missing
  consequential decisions or commitments needed to proceed. Without optional-study authority,
  state relevant uncertainty and continue authorized work without repeatedly offering the study.
- [x] AC2 — Required evidence. Applicable correctness checks, selected TDD, and empirical
  acceptance criteria remain required. A claim of verified improvement needs comparable support.
  When required evidence cannot be obtained within authority, identify the unmet requirement or
  unsupported claim and continue independent work. Do not waive acceptance criteria, invent
  findings, or label a candidate gain verified. Required evidence follows existing resource
  and permission boundaries; it is not permission for an unbounded study.
- [x] AC3 — Task-local checks. Small, self-contained empirical checks using available tools
  and inputs may remain with the current task owner without an additional measurement or
  experiment delegate. Ordinary diagnostic probes remain investigation. Neither activity
  automatically creates a study, extra records, or workflow stage. Keep routine check evidence
  with its task; retain material decision evidence and provenance under existing ownership rules.
  Required independent review and the wider delegation contract remain unchanged.
- [x] AC4 — Proportionate contributions. Low-risk, noncomparative skill behavior changes may
  use relevant candidate-only checks with an explicit coverage rationale. Matched baseline and
  candidate evidence remains required for named test-first behaviors, comparative improvement
  claims, and changes to consequential shared boundaries such as authority, TDD, completion,
  trust, persistent data, or cross-worker ownership. Editorial behavior-preserving changes may
  use static checks. Metadata and PR fields apply to the chosen verification; absent comparison
  identifiers are not a defect when comparison is unnecessary. File count alone does not set risk.
- [x] AC5 — Evidence integrity. Freeze applicable cases and outcome criteria before trials.
  Independently grade semantic behavioral success using actual actions/artifacts, retaining
  outcomes, limits, and relevant unfavorable or unrun work. One qualified independent review
  may assess both the diff and those outcomes; do not require another reviewer solely for a label.
  Setup failure is not behavioral red, and later evidence cannot retroactively establish a
  missed test-first sequence. Preserve prior records and resolve infeasible selected sequencing.
- [x] AC6 — Consistent application. Current entry points and contributor guidance agree on
  AC1–AC5; obsolete blanket requirements are replaced or narrowed. No new mandatory preference
  interview, report, or configuration step is introduced. Bounded verification covers the cases
  below, with independent review and applicable links, manifests/catalogs, packaging, and
  repository checks passing. Required unrun checks remain unmet. Describe installation and
  interactive behavior as untested unless actually exercised.

### TDD and verification

- Level: **targeted**, explicitly selected by the user for this change.
- Test-first behaviors: optional design uncertainty does not initiate a study or require an
  unnecessary preference decision; an explicitly requested bounded study proceeds without
  redundant authorization; a low-risk noncomparative contribution accepts adequate candidate-only
  evidence. Observe intended baseline failures before changing the relevant instructions, then
  obtain matched candidate evidence. Retain passing baselines as characterization; never invent
  a failure. Resolve an infeasible selected sequence before substituting another.
- Regression coverage also includes task-local diagnosis/measurement, required empirical
  acceptance without evidence, comparative or consequential shared-boundary changes, and
  editorial-only changes. Cases may cover multiple criteria; a universal suite is unnecessary.
- Before implementation trials, declare the selected cases, conditions, finite run budget,
  stopping conditions, and effective execution authority. Reuse valid existing evidence and
  assessment infrastructure. This specification authorizes no trials or implementation.

## Decisions and evidence

- User-selected TDD is settled. The first simplification scope and AC1–AC6 are proposed for review;
  the broader core-reduction proposal is not included in this change.
- Source inspection confirms broad study triggers, obligatory specialist delegation, and a
  contribution protocol without a candidate-only behavioral path. Existing proportionality,
  resource, and routine-verification safeguards remain useful; actual runtime slowdown is unmeasured.
- Definition checks: scope and requirements checked for contradictions; local links/anchors,
  AC identifiers, selected TDD, dates, requested wording, and whitespace pass. No behavioral
  trials, implementation, or installation checks were performed during specification.
- Relevant owners: [core](../../../plugins/lusona/README.md),
  [measure](../../../plugins/lusona/skills/measure/SKILL.md),
  [experiment](../../../plugins/lusona/skills/experiment/SKILL.md),
  [contribution requirements](../../../CONTRIBUTING.md#behavioral-evidence), and
  [evidence retention](../../../plugins/lusona/references/evidence.md).

## Prototype refinement

The user's “refine it please” authorizes refinement of the proposed prototype following the
experiment. The [revised patch](../evidence/2026-10-27-proportionate-evidence-work/refinement/proposal.patch)
consolidates study entry in the shared core, replaces repeated skill rules with links, aligns
contributor/PR applicability, and clarifies reuse of adequate worker verification for unchanged
inputs. Changed inputs, failures, missing/unreliable evidence, and concrete unresolved risks
still justify reruns; independently required checks and review remain required.

Across eight affected sources, the draft is 6,539 whitespace words: 337 fewer than the tested
prototype and 10 fewer than baseline. This is not a general runtime reduction: plugin instructions
are 16 words above baseline, including core +48 and coordinator delegation +30, offset by four
shorter skill bodies. Counts are source size, not model tokens, latency, or cost.

Independent reviewer `/root/review_evidence_refinement` found no actionable source defects and
accepted the refinement-only proposal, conditional on finalized mechanical checks. Those checks
now pass: exact patch reconstruction, 522 links/anchors, four skill validators, native plugin and
catalog validation, packaging, and source hashes. A missing validator dependency was resolved
using existing local PyYAML; an over-specific heading checker was corrected. No dependencies
were installed. The native installation-line advisory remains. Exact changed sources, checks,
recoveries, counts, and review reconciliation are retained in the
[check archive](../evidence/2026-10-27-proportionate-evidence-work/refinement/checks.zip) and
[manifest](../evidence/2026-10-27-proportionate-evidence-work/refinement/manifest.json).

Targeted TDD remains unchanged. The original experiment is preserved byte-for-byte; its 6/6
candidate result applies only to the tested prototype. No new behavioral trial was run, and the
refinement does not yet demonstrate that duplicate verification stops in practice. Source review
and static checks do not replace required behavioral evidence. Installation and native interactive
behavior remain untested. No canonical sources were edited.

## Implementation and verification

The user invoked `lusona:implement`; the exact reviewed eight-file patch is applied. Source and
packaging-input identity checks establish that the prior passing mechanical checks apply to the
adopted files; they were reused without redundant execution. The existing manifest identity and
version remain aligned. All other canonical-before files are unchanged.

[Run 002](../evidence/2026-10-27-proportionate-evidence-work/runs/002/README.md) retains the completed
behavioral checks and independent review. Seven of eight initial candidate cases pass; the eighth
fails its frozen write-scope criterion because its raw task permitted an existing-spec update.
The original failure remains. A separately frozen, explicitly approved pair aligns the raw task
with that restriction: the old baseline fails by writing external scratch, while the implemented
candidate passes. The exact external artifact was retained and safely removed. Neither the 7/8
nor the 1/2 result has been rewritten as an all-pass suite.

Independent reviewer `/root/implementation_outcome_review` accepts the bounded implementation,
with no actionable source defect or current-candidate critical violation. AC1–AC6 are supported
by the retained source review, required-evidence/scope reconciliation, contribution comparison,
valid/stale verification checks, read-only and authority cases, and matching mechanical checks.
The implemented routine task runs its unittest once; the previous prototype ran it twice.
No causal or general efficiency claim follows from that observation.

Targeted TDD remains user-selected: the contribution baseline failure precedes relevant edits;
passing routine/local baselines remain characterization. New boundaries are regression coverage.
The two follow-up trials received explicit user approval after automatic review rejected the
modified prompt; no actor ran during either rejection. Partial blinding, scheduling/worker-model
variation, one observation per case, and untested installation/native interaction remain limits.

## Instruction footprint reduction

The user identified that the prior work did not fulfill the broader bloat concern, then explicitly
said “proceed” after agreeing that the existing context was sufficient for implementation. This
follow-on now includes the mandatory core/worker loading cleanup excluded from the original scope.
The earlier completed implementation and adverse evidence remain historical facts.

Scope: compress duplicated core and delegation prose, retain shared safeguards once, and make
operation-specific details conditional with explicit loading triggers. Preserve behavior, existing
presentation/status meaning, authority, TDD, correction budgets, review, ownership, retention,
native questions and concrete next actions. No commit, publication, new workflow phases or broad
skill-body rewrite. Existing targeted TDD carries forward; this is behavior-preserving cleanup,
so passing characterization remains passing rather than manufactured red.

- [x] F1 — Reduce the whole core and ordinary mandatory coordinator/leaf loading paths materially;
  report per-role, correction-active and commit-active paths and total plugin Markdown, using the
  current pre-cleanup source as baseline. Moving text alone must not inflate the claimed savings.
- [x] F2 — Every removed/moved obligation has a retained owner and applicable loading trigger;
  authority, scope, TDD, correction/worker budgets and completion requirements stay binding.
- [x] F3 — Frozen before/after decision responses preserve correction limits, leaf boundaries,
  evidence/review/capacity distinctions, and read-only continuation. Independent review checks
  actual responses and the source mapping; findings and limits remain visible.
- [x] F4 — Applicable links, anchors, native identity/catalogs, packaging and whitespace pass;
  preserve unrelated edits and prior evidence, and report installation/live-execution limits.

Baseline: core 2,551 words; ordinary implementation coordinator 5,204 and leaf 3,927 words;
all plugin Markdown 25,076 words. Method counts required source text once per loading path,
not runtime tokens, latency or total agent cost. Detailed correction rules are already included
in those baseline paths. Commit-active coordinator is 5,908 words. Frozen inputs and a small
four-scenario decision exercise are under `tmp/instruction-footprint-20261027/`. Baseline actor
returned four supported decisions before canonical edits; final independent grading is retained below.
The exercise uses one fresh baseline actor and one candidate actor with identical tasks/model,
then independent review. It assesses response decisions, not live filesystem/permission enforcement.
No external CLI trial or broad performance study is part of this cleanup.

Completed cleanup: core 2,551→1,585 words (−37.9%); ordinary coordinator path
5,204→3,764 (−27.7%); leaf 3,927→2,641 (−32.7%). Correction-active paths still fall 22.4%
for coordinators and 25.8% for leaves; commit-active coordinator falls 24.4%. Total plugin
Markdown falls 1,006 words to 24,070, so savings are not merely relocated text. These are
mandatory-path source-word floors, not measured tokens, complete task totals or runtime speed.

[Retained cleanup evidence](../evidence/2026-10-27-instruction-footprint/README.md) contains exact
sources/diff, role-count method, frozen cases, both actual actor responses, independent grades,
and mechanical checks. Both conditions pass all four decision cases. Independent reviewer
`/root/footprint_independent_review` found no actionable defects and recommends F1–F4 satisfied.
Conditional correction and commit triggers, leaf boundaries, review/capacity, authority/TDD,
question tools and output/status meaning remain intact. Final source/package/link/anchor/native
checks pass. No actual scenario execution, host-loading measurement or installation was tested.

## Current handoff

- Complete: the prior proportionate-evidence implementation and this explicitly authorized
  follow-on instruction reduction. AC1–AC6 and F1–F4 are reconciled; history owns completed state.
- Evidence: linked prior runs preserve adverse outcomes; the separate cleanup record preserves
  before/after source counts, passing characterization, independent review and final checks.
- Limits: source-word reductions are not token/latency/cost claims. Live execution, automatic
  host loading and installation remain untested. No human acceptance is inferred from checks.
- Recovery: frozen sources, actual decision responses, grades and checks retained durably;
  repo-local scratch retained. No active worker operations/children; separate host shutdown
  confirmation is unavailable for these completed subagents.
- Next action: none for the authorized cleanup. No commit, push or publication requested or
  performed. Further changes or installation require their own scope.
