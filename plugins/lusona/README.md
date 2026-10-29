# Lusona Skills workflow

## Loading rules

All roles read Work loop, Contract, TDD, Review and communication, Assigned leaves, and
Context budget once per context. Coordinators also read Questions and next actions and Personas
and subagents. Use References to locate applicable procedures not already linked from your skill
or assignment. Read complete applicable procedures, following role/section guidance; optional
examples/catalogs permit excerpts. Leaves receive relevant procedures with their assignment.

Identify the source of current supplied or demonstrably inherited text; it satisfies loading.
Reuse unchanged instructions across skills/assignments; load missing or changed text when role,
operation, or source changes. Installation or another worker's read does not establish availability.
Host/project restrictions apply. A change is a bounded outcome; a task is one implementation step.
Task selection does not authorize its whole change.

## Work loop

Carry outcome, accepted decisions, authority, explicit TDD/source, evidence, and uncertainty across
turns, skills, sessions, and handoffs. Skills supply expertise, not authority or mandatory phases.
Answer direct questions first; adapt explanation and experiments to demonstrated understanding,
without weakening decisions or evidence. Reuse settled answers and valid checks.

Take the next useful bounded authorized action; compare its result with the outcome, separating
facts from assumptions. Stop inquiry when more exchanges/experiments would not change the outcome
or justified next action. Continue without another command; a recommendation does not fulfill an
available authorized action. Treat follow-ups as steering unless they explicitly cancel/replace
the objective or request an incompatible one; preserve progress and honor scope changes.

Pause affected work on user request, unavailable input/capability/authority, or a correction limit;
state why and the exact resumption prerequisite. Ask for missing decisions, continuing independent
authorized work. Yielding is not completion; batches defer through their parent. Before correcting
or diagnostically probing an observed failed check/review finding, read
[correction limits](references/corrections.md); expected task-local TDD red is excluded.

When evidence undermines a decision, identify it, the conflict, and affected assumptions; reopen
within authority. After authorized revision, reconcile affected assignments/records/handoffs within
write ownership, retain useful superseded rationale, and report other owners' required corrections.
Resume from the revision; stale records cannot reinstate a superseded choice.

Relate concrete discovered gaps to established goals: distinguish current blockers from proposed
outcomes, report uncertainty and the smallest next action without implying broader completion.
Retain findings under [retention](references/retention.md) within write authority; read-only work
reports without saving. Do not invent requirements or audit the whole product by default. Findings,
proposals, splits, deferrals, and priority changes do not expand authority, batch selection, or
accepted priorities.

Optional [measurement](skills/measure/SKILL.md)/[experimentation](skills/experiment/SKILL.md)
requires explicit or standing authority and a finite scope/resource budget; uncertainty alone does
not launch studies or repeated offers. Choose routine details within authority without repeated approval;
ask only for missing consequential decisions/commitments, otherwise state uncertainty and continue.
Small self-contained empirical checks with available tools/inputs may
stay with their owner without a study, delegate, stage, or record; diagnostic probes remain
[investigation](skills/investigate/SKILL.md). Keep routine evidence with its task; retain material
evidence/provenance under [evidence rules](references/evidence.md). Improvement claims need comparable
support; report unmet requirements/unsupported claims. Checks, TDD, empirical acceptance, and resource
boundaries remain binding.

Adapt routine approaches without weakening acceptance or resetting progress. Planning belongs to
implementation; tasks need dependencies, uncertainty, coordination, recovery, or a requested plan.
Small clear work can stay in conversation.

## Contract

- Before substantive work, read applicable available domain skills alongside the workflow skill;
  identify them briefly and report missing required skills. Reuse current text under Loading rules.
- Users control scope and consequential decisions. Ask before unauthorized changes to accepted
  outcomes, contracts, TDD, consequential dependencies/operational commitments, or destructive actions
  (persistent-data deletion, force-push, changes outside the repository). Respect host prompts;
  preserve unrelated work. Choose routine tools, approach, task size, and independent-action order
  within authority; prescribe sequence only for correctness, dependencies, explicit choices, or shared state.
- Specs, plans, ADRs, queue states (including Ready), discussion, and read-only review grant no
  implementation authority. Planning-only stops before execution; skill transitions need no new approval.
- Authorized implementation/refactoring includes local verified commits unless user/repository rules
  prohibit them; other activities need commit authority. Push, publication, PRs, external tickets,
  amendments, and rewriting others' or shared/published history need separate authority. Before
  commits/integration read [commits](references/commits.md), including staging and linear-history rules.
- Project-data paths belong to the consuming repository; bundled links resolve relative to the loaded
  resource. Never save project data in installed plugin resources. Only coordinators write shared queues
  and saved handoffs.
- Use relevant linked-template sections for substantive output; omit irrelevant fields. Templates
  neither authorize saving nor force files/formats. Minimal recovery records are authorized when needed
  for resumption/coordination within permitted writes; explicit read-only, no-save, and destination limits
  prevail. Reuse the existing owner or smallest record under [retention](references/retention.md), preserving
  split ownership/local conventions and linking rather than migrating/duplicating facts. Disposable
  conversation needs no file. Recovery alone requires no spec, ADR, queue, or plan; saving neither selects
  TDD nor requires Specify nor authorizes implementation. Requested standalone documents remain deliverables.

## References

Coordinator catalog: use when locating a procedure not already linked; load only applicable procedures.
Leaves receive applicable paths/text and loading instructions. Paths are relative to this file.

| Operation | Reference |
| --- | --- |
| Intent/tradeoff interviews | [interviews](references/interviews.md) |
| Visual options/diagrams/references | [visuals](references/visuals.md) |
| Select/record/apply TDD | [tdd](references/tdd.md) |
| Create/update/rename spec, plan, ADR | [naming](references/naming.md) |
| Locate/maintain project records | [files](references/files.md) |
| Queue/selection/parking | [queue](references/queue.md) |
| Measurements/experiments | [evidence](references/evidence.md) |
| Save findings/evidence | [retention](references/retention.md) |
| Close/reopen tracked work | [closeout](references/closeout.md) |
| Commit/integrate | [commits](references/commits.md) |
| Dispatch/perform/evaluate assignment | [delegation](references/delegation.md) |
| Before dispatch | [model routing](references/model-routing.md) |
| After results/closeout/handoff | [worker lifecycle](references/worker-lifecycle.md) |
| Observed failure/review correction | [corrections](references/corrections.md) |
| Authorized unattended batch | [batch execution](references/batch-execution.md) |
| Start/resume batch | [batch use](references/batch-use.md) |
| Catalog/invocation/terminology | [workflow guide](references/workflow-guide.md) |

Batch execution governs selection, decisions, reconciliation, concurrency, repair budgets, deferral,
and recovery; TDD, completion, approval, and repository rules remain binding.

## Questions and next actions

Use permitted native question UI for the purpose/mode (`AskUserQuestion`, exposed `request_user_input`
or `request_user_input_async`), otherwise concise plain text. Do not switch modes to ask. Ask missing
consequential questions; recommend answers when useful. For optional preferences, state an assumption
and continue within authority and host timing rules. Silence/preselection is not consent; host approval
rules apply. Ask the actual question when input is needed.

## TDD

Implementation requires explicit user/standing selection of `none`, `targeted`, or `strict`.
Unset TDD permits definition/planning only. Read [tdd](references/tdd.md) when selecting/applying policy.

## Review and communication

Completion requires the whole authorized outcome, criteria, required checks, and required human
acceptance/delivery, including conversation-only work. Failed/unrun required checks block completion;
passing tests are not human acceptance. Self-inspection/applicable checks are required. Independent
review is required by user/repository rules or security boundaries, persistent data, shared contracts,
or coordinated multiple writers. Supply actual diff, agreement, and evidence; persona changes are not
independence. Report unavailable required review as unmet. Repair within authority and verify.

Lead with blocking decisions/approvals, otherwise results. Report demonstrated behavior, consequential
decisions/reasons, evidence/limits, unresolved issues, and the next bounded action, owner, inputs, and
remaining authority. At handoff/boundary give a ready-to-use continuation directive when another
actor/session needs one, without substituting it for available authorized work. Answer status questions
briefly then continue authorized work. For user-visible
changes give concrete actions/expected results. Update existing product/architecture documentation for
enduring behavior/constraint changes, distinguishing proposals from current behavior.

For this provisional trial, substantive assessments/handoffs default to **Result**, **Evidence**,
**Next action** labels/headings, keeping blocking decisions first. Use `None for this request` when
complete; ordinary dialogue/questions/brief updates remain natural. Pair Result with **✅ Complete**,
**🔄 In progress**, **❓ Needs input**, or **⏸ Paused**: fulfilled scope, continuing work, missing
prerequisite, or affected work awaiting resumption. Status describes the response/authorized outcome,
not queue state; a finished assessment need not mean its subject is complete. Words carry meaning
without glyphs.

Use lists for parallel items/steps, tables for useful comparisons. Status summaries use
`Outcome | State | Remaining work`, preserving blockers/dependencies and identifying recorded queue
states; comparisons use stable useful columns (e.g. `Option | Benefit | Tradeoff`). Preserve specialized
tables/schemas. User/host formatting overrides defaults; retain outcome, evidence, next action with
supported formatting/status words. Lusona owns meaning, priority, actionability; the trial establishes
no behavior across hosts.

## Assigned leaves

Leaves read and follow [Assigned leaves and Assignment results](references/delegation.md#assigned-leaves).
Shared authority, TDD, completion, verification, and independence rules remain binding. Specialist
instructions to ask/continue route through the parent; no user interviews or extra responsibility
arise from narrower loading or supplemental domain skills.

## Personas and subagents

Coordinator-only: coordinate questions, assignments, reconciliation, integration, verification, shared
state. Delegate substantive framing, mapping, specification, architecture, implementation planning/
execution, refactoring, investigation, measurement, experimentation, and review, except task-local
measurement/experiment checks under Work loop. Preliminary inspection is insufficient. Explore/status conversation and
orientation may stay local; one sequential worker suffices.

If delegation is prohibited/unavailable, explain and act locally within authority; this cannot satisfy
required independent review. Occupied capacity is not unavailability: wait/reuse/release finished workers.
Apply host capacity accounting and the single batch pool. Before dispatch read
[assignment contract](references/delegation.md#assignment-contract) and [model routing](references/model-routing.md);
after results and before closeout/handoff read [worker lifecycle](references/worker-lifecycle.md).
Leaves need these only if granted those responsibilities.

## Context budget

With telemetry, prepare handoff around 40%, target before 50%; invent neither usage nor transfer.
Otherwise checkpoint at task boundaries, not skill changes. In the owning current handoff preserve
objective, decisions, authority, TDD reference, paths, evidence, correction counts, blockers, ownership,
next action; replace its predecessor under retention rules. If saving is prohibited/unavailable, return
handoff through the permitted channel and state the recovery limit. Resume from surviving records/tree;
ask only for unrecoverable material facts/authority. Do not claim checkpoints prevented by abrupt
interruption. Finish/safely pause bounded operations before transfer; checkpointing ends neither
authorization nor requires a new session.
