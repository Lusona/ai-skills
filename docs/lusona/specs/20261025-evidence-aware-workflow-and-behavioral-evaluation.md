# Spec 20261025-evidence-aware-workflow-and-behavioral-evaluation: Revise decisions from evidence and retain discovered work

Created: 2026-10-25
Updated: 2026-10-25

Kind: workflow behavior and evaluation
Context: source audit in the authoring conversation.

## Agreement

Users should be able to investigate architectural choices, revise decisions when evidence changes,
and retain newly discovered work toward an established goal without fighting earlier records or
silently expanding implementation scope.

The user selected this scope on 2026-10-25: clarify decision revision and discovery; define behavioral
evaluations; evaluate delegation and context changes before adopting them. The user explicitly selected
targeted TDD. The subsequent “approved; $lusona:implement” instruction accepted this agreement and
authorized its implementation and bounded experiments; commits and publishing remain excluded.

In scope:

- Clarify evidence-triggered revision of accepted decisions and persistence of authorized corrections.
- Connect discoveries during bounded work to the established goal and appropriate retained records.
- Define and run a small reusable behavioral evaluation set when implementation is authorized.
- Compare task-dependent delegation and reduced mandatory context in isolated experimental variants;
  return evidence and a recommendation before changing either canonical default.

Out of scope: redesigning the workflow, a general evaluation platform, automatic backlog expansion,
competitor comparisons, changing TDD/authorization requirements, article edits, publishing, and commits.

Preserve bounded assignments, native question tools where permitted, concrete next actions,
independent review where required, and user control over consequential decisions. Edit canonical
workflow sources only under `plugins/lusona/`; keep experiments and generated packages in repo-local
`tmp/`. Do not copy private consuming-project data into fixtures or packages.

Completion means the criteria below are verified, required repository checks pass, and independent
review of the changed shared instructions is complete. Report behavioral limits and untested hosts.
A recommendation from an experiment does not authorize adoption of a new default.

### Acceptance criteria

- [x] AC1: When new evidence undermines an accepted decision, the agent identifies the decision,
  conflicting evidence, and affected assumptions. It can reopen the relevant question and continue
  independent authorized work. A consequential change beyond its authority requires a user decision;
  the agent neither treats the old decision as immutable nor silently replaces it. With unchanged
  evidence and intent, it reuses settled decisions without repeating the interview.
- [x] AC2: After an authorized decision change, the agent updates the relevant owning records and
  affected handoff within its write authority, preserves the old rationale as history where appropriate,
  and uses the new decision when resuming. An unchanged dependent record cannot silently restore the
  superseded choice. Records outside write authority are reported for reconciliation.
- [x] AC3: When an investigation, implementation, or review exposes a concrete gap relevant to an
  established goal, the agent relates it to that goal and distinguishes a current blocker from a
  separate proposed outcome. During authorized tracked work it retains the finding with evidence,
  uncertainty, and a next action, linking an existing item or adding a distinct proposal when warranted.
  A deferred item has a reason or revisit condition. It does not duplicate existing work, manufacture
  a spec for every finding, or execute new scope without authority. Read-only work reports findings
  without writing records. New findings do not silently join an active batch. Evidence refuting a
  retained finding is recorded beside the original claim and changes the resulting recommendation.
- [x] AC4: Completing a bounded assignment remains distinct from achieving the larger goal. The agent
  reports relevant known gaps without inventing requirements, auditing the entire product after every
  task, or reopening unrelated work. An authorized simple task with no material discovery completes
  without unnecessary planning records or further permission requests.
- [x] AC5: Behavioral regression cases cover an omitted useful option and a request to discuss
  architectural consequences during an interview. The agent revises the offered choices, explains
  tradeoffs, and resumes the existing objective and authorization without forcing a selection,
  restarting settled questions, or treating exploration as implementation permission.
- [x] AC6: Reusable scenarios and outcome rubrics cover AC1–AC5, including unchanged-decision,
  no-gap, read-only, and unauthorized-scope counterexamples. Baseline and candidate evidence records
  actual outcomes and relevant interaction, not required wording or a prescribed tool sequence.
  Failed, inconclusive, and setup-blocked trials remain visible.
- [x] AC7: Isolated comparisons vary delegation policy and mandatory context separately against the
  same reference version on relevant scenarios. Each comparison records quality, boundary violations,
  user interruptions, and available overhead measures, and produces a retain/change/inconclusive
  recommendation with limits. Neither experimental variant changes the canonical defaults in this
  change. Required independent review remains intact in every variant.
- [x] AC8: Changed canonical instructions have consistent references, valid native manifests/catalogs,
  and a successful package check excluding project records and experimental artifacts. Representative
  local-plugin behavior is exercised on a named host. Missing host capabilities or required checks
  are reported as unmet verification, not as success.

### TDD policy

- Level: targeted, selected explicitly by the user on 2026-10-25.
- Test-first behaviors: evidence-triggered decision revision and correction persistence (AC1–AC2),
  and retention of goal-relevant discoveries without scope expansion (AC3–AC4).
- Freeze the scenario inputs and outcome rubric, then run the current instructions before editing
  the relevant behavior. Retain failing transcripts and resulting state as red evidence; rerun the
  same checks after the change. Setup errors and evaluator disagreements are not behavioral red.
- If a baseline passes, retain it as characterization. Do not manufacture a failure or claim a
  reproduced bug from wording alone. Clarifications preserving that observed behavior stay green;
  a behavior change without feasible test-first evidence requires resolution of the TDD constraint
  before proceeding.
- Required regressions: AC5 and the negative/boundary cases in AC1–AC4. Comparison experiments do
  not require an experimental variant to win; an inconclusive or adverse result is valid evidence.

### Evaluation boundaries

Use synthetic, product-neutral fixtures and fresh contexts with enough raw evidence to perform each
assignment. Do not give the acting agent the desired answer or audit conclusions. Multi-turn cases
must preserve user steering and inspect resumption, not just a single proposed response.

Before trials, record the host, model/reasoning setting, skill version or content hash, task inputs,
permissions, selected TDD, expected outcomes, and trial budget. Use three independent trials per
selected scenario and condition for an initial descriptive comparison; report counts and individual
failures, not statistical significance. Keep conditions equivalent except for the tested change.
Do not expand the suite or trial budget merely to obtain a passing result.

Grade resulting records and actions as well as the conversation. An unauthorized consequential
change is a failure regardless of task completion or speed. Use human/independent transcript review
for semantic judgments and deterministic checks for observable state where useful. Report token/time
measures only when available. Do not treat a faster run as better when outcome quality worsens.

For the experimental variants, choose relevant probes before running: a small coherent assignment
and an assignment benefiting from independent investigation for delegation; a simple request and a
request requiring the conditionally loaded guidance for context. Reuse matched reference results
only when their inputs and versions match. Keep experimental variants out of distributed packages.

### Evidence and rationale

The source audit established instruction support, not reliable runtime compliance:

- [Architect](../../../plugins/lusona/skills/architect/SKILL.md) says not to reopen answered questions
  while also supporting ADR supersession. This is an ambiguity to clarify, not a reproduced failure.
- [Implement](../../../plugins/lusona/skills/implement/SKILL.md),
  [retention](../../../plugins/lusona/references/retention.md), and
  [status](../../../plugins/lusona/skills/status/SKILL.md) support adaptation and retained findings,
  but the trigger connecting a discovery to the larger goal is distributed.
- [The core](../../../plugins/lusona/README.md) mandates broad specialist delegation and loads
  substantial shared instructions. Their actual cost or harm has not been measured here.
- [Anthropic on context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
  supports testing minimal sufficient guidance and adding detail for observed failures.
- [Anthropic on agent-loop design](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop)
  supports task-dependent delegation and measured comparisons, not universal removal of subagents.
- [Anthropic on evaluations](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)
  supports repeated trials and evaluation of actual outcomes and interaction.

These references motivate the experiments; they do not establish that Lusona benefits from either
experimental change. Keep research rationale here rather than adding citation material to runtime skills.

## Execution and evidence

- Freeze six synthetic scenarios and separate outcome rubrics before baseline trials; preserve a
  content-hashed snapshot of the unchanged canonical plugin. Baseline precedes instruction edits.
- Run three fresh trials per scenario; use real resumed turns for revision and interview cases.
  Grade transcripts and resulting records, preserving setup failures separately from behavior failures.
- Make bounded canonical clarifications supported by baseline/source evidence, then run matched
  candidate trials. Compare isolated delegation and context variants on the preselected probes.
- Obtain independent review of instructions and evaluation evidence; run repository validation.
- Preflight: Claude Code 2.1.310 print mode reports “Not logged in”; no Claude behavioral result.
  Codex CLI 0.164.0 is authenticated and passed a read-only connectivity check. Its app server
  requires an outer-sandbox escalation; the CLI's own sandbox remains enabled.
- Native Claude plugin and marketplace validation passed before edits, with existing advisory
  warnings for a missing listing icon and installation line in the plugin README.

### Behavioral results

Frozen suite: [scenarios, rubric, lock and capture runner](../../../evals/evidence-aware/README.md).
Codex CLI 0.164.0, gpt-6.1-sol, medium reasoning, workspace-write, 600 seconds per turn;
three fresh trials per scenario, with three sequential turns for revision and interview.
Independent grading inspects actual actions and artifacts, not only final claims.

| Scenario | Baseline passes | Candidate passes | What the case establishes |
| --- | --- | --- | --- |
| Decision revision and resumed stale handoff | 3/3 | 3/3 | Authorized correction persists; unchanged decisions remain settled |
| Goal-relevant discovery | 0/3 | 3/3 | Supported unfinished work remains actionable after assignment closeout |
| Read-only finding | 3/3 | 3/3 | Report gaps without writing records |
| Simple task | 3/3 | 3/3 | Exact correction without invented scope, records, or approval requests |
| Missing interview option and architectural discussion | 3/3 | 3/3 | Revise choices and preserve objective without implying implementation permission |
| Refuted finding in fixed batch | 3/3 | 3/3 | Correct recommendation without deleting history or expanding the batch |

All 18 candidate trials pass independent grading; baseline passes 15/18. Baseline discovery failures are genuine test-first red:
the agent found the quantity-format incompatibility but left it only in completed evidence,
without an open actionable proposal. The bounded retention clarification produces three green
trials under the unchanged rubric. Baseline revision was already green characterization; this
work does not claim to have reproduced the author's historical revision failure.

Interview coverage has a further limit: all six baseline/candidate actors already offered caching
in turn 1. The frozen rubric permits this, so these passing trials demonstrate continued inclusion
and architectural discussion, not recovery from an actual omission by the acting agent.

The canonical change affects the core Work loop, Architect's settled-decision wording, and
Retention. Delegation, context-loading, TDD, and authorization defaults remain unchanged.
The reusable runner has seven passing local tests; two independent-review defects (timeout
child processes and malformed supplement records) were reproduced before their fixes.
Independent review of the canonical instruction diff found no actionable defects.

Local validation passed: changed links/anchors and Architect skill structure; native plugin
and marketplace validation; package build excluding project docs, evals, and tmp; diff whitespace.
Existing listing-icon/install-line advisories remain non-failing. The unrelated root copyright
attribution was preserved and mirrored into the bundled LICENSE to satisfy package validation.
Frozen candidate instruction bytes match canonical sources; LICENSE is the sole later difference.

Raw transcripts, per-turn artifact/hash snapshots, frozen conditions, independent grades, and
variant diffs remain under `tmp/evidence-aware-eval/`. Original failures are retained. The first
baseline turn predates automatic runner-source capture; its source is separately retained under
`setup/`, and it did not time out. Later turns record the executing runner source and hash.
CLI stdout omits collaboration activity, so separate filtered exact-session supplements capture
observable events. Supplements are labeled cumulative captures, not original turn snapshots.
Encrypted assignment arguments and total child costs are unavailable. A missing worker event
does not prove unavailable delegation. Reads are instruction-limited, not OS-isolated from the
rubric; writes are sandboxed. No rubric/sibling-trial inspection was observed.

These are small descriptive synthetic trials on one model/host, not statistical evidence or a
competitor comparison. Native installation and interactive UI behavior were not tested. Claude
Code 2.1.310 is unauthenticated, so there is no Claude behavioral result.

### Isolated policy comparisons

Both variants were frozen from the unchanged baseline, not the candidate. Inputs, rubric,
host/model/effort, permissions and three-trial budget match. Delegation changes only whether
substantive work must be delegated; required independent review remains intact. Context moves
recovery guidance to a conditional reference while preserving its requirements and delegation.
Mandatory core length falls from 2,249 to 2,083 whitespace-delimited words, with a 242-word
conditional resource. This is not a measurement of total model context saved.

| Probe | Baseline passes | Variant passes | Median wall seconds, baseline → variant | Median root input tokens, baseline → variant |
| --- | --- | --- | --- | --- |
| delegation: simple | 3/3 | 3/3 | 37.7 → 19.6 | 185,981 → 104,086 |
| delegation: discovery | 0/3 | 0/3 | 112.9 → 93.6 | 589,720 → 401,380 |
| context: simple | 3/3 | 3/3 | 37.7 → 60.4 | 185,981 → 158,388 |
| context: batch-refutation | 3/3 | 3/3 | 129.5 → 166.0 | 526,182 → 590,721 |

These are raw descriptive medians, not causal speed/cost estimates. Root tokens include repeated
and cached input and exclude complete worker costs. Trials ran with two concurrent isolated
workspaces. Delegation discovery trial 3 recorded 1,367.0 seconds and context simple trial 2
recorded 1,294.1 seconds despite successful CLI exits and a configured 600-second subprocess
timeout. The runner measures elapsed wall time separately from the subprocess deadline; the
cause of these anomalies is unestablished. All raw values remain, without replacement trials.

Delegation recommendation: **inconclusive; retain the canonical default**. Simple tasks pass
without observed spawn events in all three variant traces, versus observed workers in two
baseline traces. Discovery uses an observed worker in all three variant trials and preserves
independent review, but retains the baseline's three discovery failures. Trial 3 additionally
reads an installed writing skill outside the allowed frozen inputs: one observed read-boundary
violation and an uncontrolled instruction input. Its outcome remains a failure; do not attribute
that violation causally to the delegation policy. No additional user interruption was observed.

Context recommendation: **inconclusive; retain the canonical default**. All six context trials
pass. The batch probes load
conditional recovery guidance and preserve review and fixed membership. No boundary violation or
additional user interruption was observed in the context probes. Smaller mandatory
text does not establish less total context or better outcomes; timing is compromised and total
worker costs are unavailable. Do not adopt this experimental layout on these measurements.

Independent reports and per-trial measurements are in `tmp/evidence-aware-eval/grades/`, including
`comparison-delegation.json` and `comparison-context.json`. Experiments are excluded from packages;
their unfavorable and inconclusive findings are part of the result, not reasons to expand trials.

## Current handoff

- Implementation, all 48 prescribed behavioral trials, independent grading, and repository checks
  are complete. Baseline 15/18; candidate 18/18; delegation 3/6; context 6/6. Experimental failures
  and limits are retained; neither default was adopted. No further implementation is needed.
- Final evidence review found one reporting omission: interview trials had already included the
  purported missing option. That caveat is now recorded beside the results. No instruction change
  or rerun was needed. Seven local tests and canonical/package validation remain applicable.
- Authority was the approved spec, targeted TDD, and explicit OpenAI evaluation-input consent.
  No commits, publishing, article edits, or private-product inputs. Native installation and
  interactive UI verification remain untested, outside this representative CLI behavior check.
- All actor processes and worker assignments have returned. This host exposes no worker shutdown
  confirmation; no host-capacity release is claimed for `/root/claims_audit`,
  `/root/evaluation_setup`, or `/root/eval_runner_review`.
- Reporting correction verified; [history](../history/2026-10-week-04.md#2026-10-25--evidence-aware-workflow-and-behavioral-evaluation) owns archived state. Next action: none for this request.
