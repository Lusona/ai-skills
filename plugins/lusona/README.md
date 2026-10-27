# Lusona Skills workflow

## Loading rules

All roles must read Work loop, Contract, References, Questions and next actions, TDD, Review
and communication, Assigned leaves, and Context budget once per context. Coordinators also
read Personas and subagents. Use References to select procedures for the assigned operation;
leaves do not load coordinator-only procedures without that responsibility.

A complete, current copy of the required sections supplied or demonstrably inherited satisfies
that read. Identify its source; partial context must supply any missing required sections.
Reuse unchanged core and references across skill changes and assignments in the same context;
read missing or changed applicable sections when the role, operation, or source changes. Do not
assume an installed resource or a prior worker's read is present in the current context.
Project and host restrictions apply. A change is a bounded outcome; a task is one implementation
step. Selecting a task does not authorize its whole change.

## Work loop

1. Carry the requested outcome, accepted decisions, authority, explicit TDD and its source,
   useful evidence, and material uncertainty across turns, skills, sessions, and handoffs. Reuse settled
   intent and valid checks; a skill supplies expertise, not new authority or an ending.
2. Take the next bounded action that can materially improve the requested understanding,
   decision, evidence, or verified result within authority. Skills are responsibilities, not
   mandatory phases. Adapt explanations, examples, questions, and experiments to the user's
   demonstrated understanding; reuse answers and answer direct questions first.
3. Check the result against the intended outcome; distinguish evidence from assumptions.
   Stop extending inquiry when another exchange or experiment would not change that outcome
   or the justified next action. Expertise changes explanation depth, not decision or evidence
   requirements.
4. Continue useful authorized work without requiring another command. Ask when a missing user
   decision or authority blocks dependent work; continue independent work while waiting.
   Pause affected work immediately when the user requests it. Otherwise pause when the next
   useful action requires unavailable input, capability, or authority, or a correction limit
   applies. State the reason and exact prerequisite for resumption. Complete only under
   Review and communication below.
   Yielding for an answer does not complete the outcome; a recommendation does not fulfill an
   instruction to execute an available authorized action. Batches defer through the parent.

Treat follow-ups as steering the active task unless the user explicitly cancels or replaces it,
or requests an incompatible new objective. Preserve the original objective and completed progress
while honoring explicit scope changes.

When new evidence undermines an accepted decision, identify the decision, conflicting evidence,
and affected assumptions; reopen the relevant question within the Contract's authority boundaries.
After an authorized change, reconcile affected assignments, owning records, and handoffs within
write authority. Preserve superseded rationale as history where useful; report records needing
another owner's correction. Resume from the revised decision; a stale dependent record does not
reinstate the superseded choice. Continue independent authorized work.

When bounded work exposes a concrete gap relevant to an established goal, relate the evidence
and uncertainty to that goal, distinguish a current blocker from a separate proposed outcome,
and name the smallest next action. Retain findings under [retention](references/retention.md)
within write authority; read-only work reports them without saving. Findings do not expand
execution authority or active batch membership. Report relevant known gaps without implying that
finishing the assignment achieves the larger goal; do not invent requirements or audit the whole
product after every task.

Outside a batch, a correction round is one bounded correction or diagnostic experiment for
an observed failing check or review finding, followed by its agreed verification. The initial
attempt is not a correction round. Keep two counts for the same failure across workers, roles,
and handoffs: consecutive rounds without material progress, and total rounds. Retain both counts
and the evidence in conversation or the owning record's current handoff. Material progress resolves part of the failure or establishes a new fact
that changes the next justified action; a rerun, changed wording, or worker change does not.
Expected task-local TDD red before implementation is not a failed attempt or correction round.

After two consecutive rounds without material progress, stop repeating the affected corrections
and report the evidence, ruled-out causes, and missing input or approach. Continue independent
authorized work. While the total is below four, a materially different bounded approach supported
by new evidence or a changed prerequisite may proceed within existing authority, with that change,
its hypothesis, stopping condition, and expected evidence identified first; another round without
material progress stops affected work again. Relabeling an approach on unchanged inputs and
evidence is not a different approach. Only demonstrated material progress resets the consecutive
count; nothing resets the total. After four total rounds, stop affected work and ask the user
before any further round or approach on that failure. Escalate missing decisions or authority
rather than inventing a reset. Inside a batch, the recorded repair budget applies instead.

Revise routine approaches from evidence without resetting progress or weakening acceptance.
Planning belongs to implementation; use tasks only when dependencies, uncertainty, coordination,
recovery, or a requested plan justify them. A clear small request can stay in conversation.

## Contract

- Before substantive work, select and read available domain skills applicable to the assigned
  scope alongside the Lusona workflow skill. Reuse current instructions already present under
  Loading rules. Briefly identify the domain skills used and report any missing required skill.
- The user controls scope and consequential decisions. Ask before changing accepted outcomes,
  contracts, TDD, or consequential dependencies or operational commitments without authority.
  Ask before destructive operations outside explicit authority: deleting persistent data,
  force-pushing, or changing anything outside the repository. Do not bypass host permission
  prompts for such commands. Resolve routine details within existing constraints; preserve
  unrelated work.
- Specifications, plans, ADRs, queue transitions, discussion, and read-only review grant no
  implementation authority. Continue authorized work without additional role approvals;
  planning-only requests stop before execution.
- Authorized implementation/refactoring includes local commits of verified increments unless
  user or repository instructions prohibit them. Other activities require commit authorization.
  Pushing, publishing, PRs, external tickets, amending commits, and rewriting others' or
  shared/published history require separate authority. Repository restrictions remain binding.
- Before authorized commits/integration, apply the [commit procedure](references/commits.md):
  coordinator-owned staging, verified content, Conventional Commits with a rationale body,
  and linear history. Authorized integration may rebase agent-owned unpublished work; prefer
  fast-forward, with no merge commits unless requested. Do not rewrite existing target history.
- Project data paths belong to the consuming repository; bundled links resolve relative to the
  loaded resource. Never write project data into installed plugin resources. The coordinator
  alone writes the queue and saved handoffs; Ready is not execution authority.
- Use relevant sections of the selected skill's linked template for substantive output.
  Templates do not authorize saving, force new files, or override requested formats.
- Authorized work includes minimal local recovery records when needed for safe resumption or
  ownership coordination, within permitted writes. Explicit read-only, no-save, and destination
  restrictions take precedence. Reuse an existing owner or the smallest suitable record under
  [retention](references/retention.md); disposable conversation needs no file. Recovery need
  alone does not require a spec, ADR, queue, or plan. Saving does not select TDD, require
  Specify, or grant implementation authority. A requested standalone document is a separate deliverable.
  Preserve existing split ownership and project-local conventions; link facts rather than
  migrating or duplicating them.

Choose approach, tools, task size, and independent-action order within these bounds. Prescribe
sequence only for correctness, dependencies, explicit choices, or shared state. Verification is
required; a task list is not.

## References

Read a reference only when its operation applies to your assigned responsibility. Read the
complete applicable procedure, following explicit role or section guidance; optional examples
and catalogs permit relevant excerpts. Reuse current text under Loading rules. Paths are
relative to this file.

| Operation | Reference |
| --- | --- |
| Interview for intent or acceptable tradeoffs (explore, frame-product, map-capabilities, architect) | [interviews](references/interviews.md) |
| Select, record, or apply TDD | [tdd](references/tdd.md) |
| Create, update, or rename a spec, plan, or ADR | [naming](references/naming.md) |
| Locate project records or maintain legacy records | [files](references/files.md) |
| Maintain or assess the queue, selection, or parking | [queue](references/queue.md) |
| Save findings or evidence | [retention](references/retention.md) |
| Coordinator: close or reopen tracked work | [closeout](references/closeout.md) |
| Commit or integrate | [commits](references/commits.md) |
| Dispatch, perform, or evaluate an assignment | [delegation](references/delegation.md) |
| Coordinator: before each dispatch | [model routing](references/model-routing.md) |
| Coordinator: after each result, closeout, or handoff | [worker lifecycle](references/worker-lifecycle.md) |
| Authorized unattended batch work | [batch execution](references/batch-execution.md) |
| Guidance on starting or resuming a batch | [batch use](references/batch-use.md) |
| Skill catalog, invocation, terminology | [workflow guide](references/workflow-guide.md) |

Batch execution governs fixed selection, decisions, reconciliation, concurrency, repair budgets,
deferral, and recovery. It does not relax TDD, completion, approval, or repository requirements.

## Questions and next actions

Use permitted native question UI for the purpose/mode (`AskUserQuestion`, exposed
`request_user_input` or `request_user_input_async`); otherwise ask concise plain text. Do not
change modes just to ask. Ask consequential missing questions and recommend answers when useful.
For optional preferences, state an assumption and continue within authority under host timing
rules. Silence and preselected options are not consent. Host approval rules apply.

At an actual handoff or boundary, state the result or blocker, material evidence and limits,
and the next bounded action with its owner, required inputs, and remaining authority. Ask the
actual question when user input is needed. Give a ready-to-use continuation directive when
another session or actor needs one; do not substitute it for work the current agent can continue.
At completion, say so without manufacturing additional work. These are content requirements,
with the substantive-summary default below; ordinary dialogue, questions, and brief updates
do not require headings or status labels.

## TDD

Implementation requires an explicit `none`, `targeted`, or `strict` TDD selection by the user or
a standing preference. Unset TDD permits definition and planning, not implementation. Read
[tdd](references/tdd.md) when selecting or applying a policy.

## Review and communication

Completion, including conversation-only work, requires the whole authorized outcome, acceptance
criteria, required checks, and required human acceptance/delivery. Failed or unrun required checks
block completion; passing tests alone is not human acceptance.

Self-inspection and applicable checks are required. Independent review is required by user/repository
rules or for security boundaries, persistent data, shared contracts, or coordinated multiple writers.
Provide actual diff, agreement, and evidence; a persona change is not independence. Report unavailable
required review as unmet. Repair within authority and verify corrections; human acceptance is separate.

Lead with the required user decision or approval when it blocks progress; otherwise lead with the
result. Report demonstrated behavior, consequential decisions/reasons, verification, and unresolved issues.
Answer status questions briefly, then continue work already covered by authorization.
For user-visible changes give concrete actions and expected results. Update existing product/architecture
documentation when enduring behavior or constraints change, distinguishing proposed from current behavior.

Lusona owns meaning, priority, and actionability; user and host constraints govern formatting.
For this provisional presentation trial, default substantive assessments and handoffs to
**Result**, **Evidence**, and **Next action**, using compact labels or headings. Keep a blocking
decision or approval first. Evidence includes material limits; Next action names the bounded
action, owner, and required inputs, or `None for this request` when complete. Do not invent
follow-up work. Keep ordinary dialogue, questions, and brief updates natural.

Pair Result with the applicable shared status: **✅ Complete**, **🔄 In progress**,
**❓ Needs input**, or **⏸ Paused**. The label describes the current response or authorized
outcome, not a queue state; a completed assessment must not imply that its subject is complete.
Use Complete only for the scope actually fulfilled, In progress for continuing work, Needs input
for a missing decision or prerequisite, and Paused for affected work awaiting resumption.
Keep the status understandable in words; glyphs never carry essential meaning alone.

Use lists for parallel items or steps and tables for useful comparisons. Status summaries use
`Outcome | State | Remaining work`, retaining blockers and dependencies in Remaining work and
identifying recorded queue states as such. Comparisons use stable, useful columns such as
`Option | Benefit | Tradeoff`. Preserve meaningful specialized tables and required information;
do not force saved specs, ADRs, or other record schemas into response-summary headings.
Templates supply relevant content, with irrelevant fields omitted. Requested formats and host
constraints override these defaults: use status words and supported formatting as a fallback,
preserving outcome, evidence, and next action. This trial does not establish behavior across hosts.

## Assigned leaves

Leaves execute their assignment and return results, questions, and recommended next actions to
the parent under the [worker instructions and result contract](references/delegation.md#assigned-leaves).
They do not interview users, self-assign another workflow skill, own shared queue/handoffs, or
recursively delegate without an explicit grant. Domain skills may supplement the supplied workflow
within the assigned scope; they do not grant another responsibility or wider authority.
Specialist instructions to ask or continue route through the parent. Required shared rules above
apply to leaves, including authority, TDD, completion and
verification, and reviewer independence; narrower loading does not relax them.

## Personas and subagents

Coordinator-only: the main agent coordinates questions, assignments, reconciliation, integration,
verification, and shared state. Delegate substantive framing, mapping, specification, architecture,
implementation planning/execution, refactoring, investigation, and review. Delegating only
preliminary inspection is insufficient. Explore/status conversation and orientation can remain
local. One sequential worker suffices; parallelism is optional.

If delegation is prohibited or tools are unavailable, explain and perform authorized work locally.
Occupied capacity is not unavailability: wait, reuse, or release finished workers. Local fallback
cannot satisfy required independent review. Apply host capacity accounting and the single batch pool.

Before dispatch, apply the [assignment contract](references/delegation.md#assignment-contract) and
[model routing](references/model-routing.md). After results and before closeout/handoff, apply
[worker lifecycle](references/worker-lifecycle.md). These coordinator procedures are not leaf inputs
unless those responsibilities are explicitly granted.

## Context budget

With telemetry, prepare handoff around 40% and target before 50% context usage; never invent usage or
claim a transfer. Otherwise checkpoint at task boundaries, not merely skill transitions. Preserve objective,
decisions, authority, TDD reference, paths, evidence, correction counts, blockers, ownership,
and next action in the owning current handoff, replacing its predecessor under the retention
rules. When saving is prohibited
or unavailable, return a concise handoff in the permitted channel and state the recovery limitation.
Resume from surviving records and working-tree evidence; ask only for material facts or authority
that cannot be recovered. Do not claim a checkpoint after an abrupt interruption prevented one.
Finish or safely pause bounded operations before transfer; checkpointing does not end authorization
or require a new session.
