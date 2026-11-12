# Voice pass 2026-11-11: applied wording edits

210 edits in 48 files. Each keeps the trigger, action and scope of the original text.


## plugins/lusona/references/closeout.md

- Before: give each dated item its own heading, outcome, completion and evidence section, and optional related records.
  After: give each dated item its own heading, an Outcome section, a Completion and evidence section, and an optional Related records section.

- Before: 5. Move unique queue facts into their owning records.
  After: 5. Move facts that exist only in the queue row into their owning records.

- Before: Change records and notes do not repeat it.
  After: Do not repeat it in change records or notes.

- Before: - Leave the history entry unchanged as a historical fact.
  After: - Leave the history entry unchanged.


## plugins/lusona/references/commits.md

- Before: - Do not mark completion early to fit a commit boundary.
  After: - Do not mark completion before its condition is met to fit a commit boundary.

- Before: Never include them through a blanket add or commit.
  After: Never stage or commit them with an add-all or commit-all command.

- Before: It does not authorize commits or integration where those are forbidden.
  After: This rule does not authorize commits or integration where those are forbidden.

- Before: - Refresh commit identities and review evidence that changed inputs invalidate.
  After: - Refresh the commit identities and the review evidence that changed inputs invalidate.

- Before: Do not fall back to a merge commit.
  After: Do not create a merge commit instead.


## plugins/lusona/references/completion.md

- Before: Nearby links were not audited.
  After: The other links in the same guide were not audited.


## plugins/lusona/references/corrections.md

- Before: one bounded correction or diagnostic experiment for
  After: one bounded correction or diagnostic probe for

- Before: It must rest on new evidence or a changed prerequisite.
  After: It requires new evidence or a changed prerequisite.


## plugins/lusona/references/delegation.md

- Before: Apply the other sections only when the assignment grants those responsibilities.
  After: Apply each other section only when the assignment grants the responsibilities that section covers.

- Before: - Delegate the substantive specialist outcome, not only an inspection.
  After: - Delegate the specialist outcome, not only an inspection.

- Before: Wait for, reuse or release finished leaves.
  After: Wait for working leaves; reuse or release finished ones.

- Before: - The relevant workflow and domain skills.
  After: - The workflow and domain skills that apply to the assignment.

- Before: That text satisfies loading.
  After: That text satisfies the read requirement.

- Before: - For each setting, inherit it when those constraints require it or its control is unavailable. Still select the other supported settings. Report when this prevents the selected routing.
  After: - Inherit a setting when a user model choice or host restriction requires it, or when its control is unavailable. Still select the other supported settings. Report when inheritance prevents the selected routing.

- Before: no less capable model suffices.
  After: no less capable model is adequate.

- Before: - Do not drop a selected override without reporting it, to keep full history.
  After: - When you drop a selected override to keep full history, report it.

- Before: or when the change touches security boundaries, persistent data, shared contracts, or coordinated multiple writers.
  After: or when the change affects security boundaries, persistent data or shared contracts, or has multiple coordinated writers.

- Before: and carry its results into your result.
  After: and include its results in your result.

- Before: - Route missing or contradictory context, questions
  After: - Report missing or contradictory context, questions

- Before: Leave the result unresolved until established.
  After: Leave the result unresolved until that information or evidence establishes it.

- Before: Serialize dependent work and mutable checks.
  After: Serialize dependent work and checks that use mutable resources.

- Before: or a concrete unresolved risk.
  After: or a named unresolved risk.

- Before: select a stronger model when allowed
  After: select a more capable model when allowed


## plugins/lusona/references/evidence.md

- Before: - Uncertainty alone does not start a study.
  After: - Uncertainty alone does not start a study (a measurement or experiment).

- Before: - A diagnostic probe belongs to [investigate](../skills/investigate/SKILL.md).
  After: - Use [investigate](../skills/investigate/SKILL.md) for a diagnostic probe.

- Before: resource limits still bind a study.
  After: resource limits still apply to a study.

- Before: - Save material decision evidence before handoff or completion without a separate save request.
  After: - Save material decision evidence before handoff or completion. Do not wait for a save request.

- Before: New material decision evidence lives in the consuming project's `docs/lusona/evidence/`:
  After: Save new material decision evidence in the consuming project's `docs/lusona/evidence/`:

- Before: - relevant inputs and environment;
  After: - inputs and environment;

- Before: - Specs, notes, ADRs and history link the exact evidence files or runs for the claims they rely on.
  After: - In specs, notes, ADRs and history, link each claim to the exact evidence files or runs it relies on.

- Before: - A short conclusion never replaces its material method, provenance and results.
  After: - Do not replace the material method, provenance and results with a conclusion.


## plugins/lusona/references/files.md

- Before: only to adopt this terminology.
  After: only to adopt the plugin's terms.

- Before: decisions, TDD, evidence, authorization
  After: decisions, the TDD level, evidence, authorization


## plugins/lusona/references/interviews.md

- Before: return focused questions and their decision impact before dependent synthesis.
  After: return focused questions, and the decision each one affects, before writing a synthesis that depends on the answers.

- Before: - Evidence gathering that does not depend on the answers continues meanwhile.
  After: - Meanwhile, continue gathering evidence that does not depend on the answers.

- Before: - Silence or a preselected option is not consent. Host approval rules apply.
  After: - Do not treat silence or a preselected option as consent. Follow the host's approval rules.

- Before: - Repository behavior does not establish what the user wants or understands.
  After: - Do not infer what the user wants or understands from repository behavior.

- Before: - Explain choices with concrete scenarios at the user's level. Invite reactions that develop the shared understanding.
  After: - Explain choices with concrete scenarios. Ask the user to react to each scenario.

- Before: Do not only fill artifact fields.
  After: Do not ask questions only to fill record fields.

- Before: - Reflect each consequential interpretation and offer correction before settling the output.
  After: - State each consequential interpretation to the user and ask for correction before settling the output.

- Before: - Drafting a document does not answer an open intent question.
  After: - Do not draft a document in place of asking an open intent question.

- Before: | Future experience | Move beyond a proposed feature |
  After: | Future experience | Establish the future a proposed feature serves |

- Before: | Ambition and initial scope | Keep the product's long view |
  After: | Ambition and initial scope | Separate the long-term ambition from the initial scope |

- Before: | Context reuse | Build on settled answers |
  After: | Context reuse | Reuse settled answers |

- Before: Technique: move from a proposed feature to a desired future.
  After: Technique: ask what future the proposed feature serves.

- Before: Technique: do not let the first delivery become the whole product definition.
  After: Technique: do not define the whole product from the first delivery.

- Before: Technique: let the correction change both the next question and the proposed capability.
  After: Technique: after a correction, revise both the next question and the proposed capability.


## plugins/lusona/references/naming.md

- Before: creates the record exclusively from its template. Both commands accept an optional `YYYY-MM-DD` creation date; otherwise they use local today.
  After: creates the record from its template. Both commands accept an optional `YYYY-MM-DD` creation date; without one, they use today's date in the local timezone.

- Before: - Branch on status and exit code. The diagnostic wording is descriptive only.
  After: - Branch on status and exit code, not on the `message` text.

- Before: - Completion dates stay in history. Spec and plan headers do not repeat the queue state.
  After: - Record completion dates only in history. Do not repeat the queue state in spec or plan headers.

- Before: - Renaming existing records or adopting the new headers requires an authorized migration that preserves dates, evidence and links. Normal work does not start one.
  After: - Rename existing records or adopt the new headers only in an authorized migration that preserves dates, evidence and links. Do not start one during normal work.

- Before: - Choose by the agent's available shell, not only the operating system.
  After: - Choose by the shell the agent runs in, not by the operating system alone.


## plugins/lusona/references/queue.md

- Before: - A read-only assessment reports gaps without repairing them.
  After: - In a read-only assessment, report gaps; do not repair them.

- Before: - A review recommends a state without writing the queue.
  After: - In a review, recommend a state; do not write the queue.

- Before: A revisit condition prompts reconsideration with the user, not automatic revival.
  After: When a revisit condition is met, ask the user whether to reactivate the item; do not reactivate it automatically.


## plugins/lusona/references/retention.md

- Before: - During authorized work beyond discussion, keep unresolved, supported, goal-relevant outcomes visible when the assignment closes. - To do that, link an existing open item, or add a distinct proposal to the queue. Create the queue from its template when absent.
  After: - When an assignment for authorized work beyond discussion closes, link each unresolved, supported, goal-relevant outcome to an existing open item, or add it to the queue as a distinct proposal. Create the queue from its template when absent.

- Before: - When another actor or session needs it, give a continuation directive. It does not replace authorized work you can take now.
  After: - When another actor or session must continue the work, give a continuation directive. The directive does not replace authorized work you can do now.

- Before: because of what it touches, not only because a user or repository rule requires review.
  After: because of what it affects, not only because a user or repository rule requires review.

- Before: - New measurement and experiment records live in `docs/lusona/evidence/`.
  After: - Save new measurement and experiment records in `docs/lusona/evidence/`.

- Before: findings without an owner | `docs
  After: findings without an owning record | `docs


## plugins/lusona/references/revisions.md

- Before: - Treat a follow-up request as steering of the current objective. Preserve progress and apply the scope change.
  After: - Treat a follow-up request as a scope change to the current objective, not as a new objective. Preserve progress and apply the change.

- Before: 2. Work with the user to one outcome:
  After: 2. Reach one outcome with the user:

- Before: - A stale record cannot reinstate a superseded choice. When a record still states a superseded choice,
  After: - When a record still states a superseded decision,


## plugins/lusona/references/tdd.md

- Before: - Do not change the agreed level to fit an approach.
  After: - Do not change the selected level to fit an approach.

- Before: tests that only mirror the implementation.
  After: tests that only restate the implementation.

- Before: exercises the relevant path.
  After: exercises the affected path.

- Before: - Do not manufacture a failing test.
  After: - Do not write a test only to obtain a failing run.


## plugins/lusona/references/visuals.md

- Before: - Pages are self-contained.
  After: - Write each page as a self-contained file.

- Before: Ask the user to choose by letter. - There is no click-capture server.
  After: Ask the user to choose by letter in the conversation; the pages do not capture clicks.

- Before: report the reference in the reply. Records never link draft pages.
  After: report the reference in the reply. Do not link draft pages from records.

- Before: - A user-supplied reference keeps its existing capture during specification.
  After: - During specification, keep a user-supplied reference as captured.


## plugins/lusona/references/workflow-guide.md

- Before: The table maps an observed need to a skill or a direct action. It separates responsibilities; it is not a required sequence.
  After: Choose the row that matches the observed need. The rows separate responsibilities; they are not a required sequence.


## plugins/lusona/skills/architect/SKILL.md

- Before: choose a technology without its consequences.
  After: choose a technology without stating its consequences.

- Before: Apply the practices relevant to the selected decision; they are not a checklist.
  After: Apply each practice that matches the selected decision; do not run them all as a checklist.

- Before: including a change-local one,
  After: including a change-specific one,

- Before: Carry coding and verification details into the spec's Execution section for [implement](../implement/SKILL.md). Carry the TDD policy forward unchanged.
  After: Put coding and verification details in the spec's Execution section for [implement](../implement/SKILL.md). Do not change the TDD policy.

- Before: or the product handoff for shared work.
  After: or the Current handoff in `docs/lusona/product.md` for shared work.

- Before: - Tie performance and availability choices to stated workloads or targets.
  After: - Base performance and availability choices on stated workloads or targets.


## plugins/lusona/skills/batch/SKILL.md

- Before: - Items held at a batch-wide phase barrier.
  After: - Items held until other items finish the same responsibility.

- Before: - Ambiguous selection blocks dispatch.
  After: - When the selection is ambiguous, do not dispatch.

- Before: - Freeze membership before execution. Discovered work stays outside it and needs a separate authorized selection.
  After: - Do not change the membership after execution starts. Do not add discovered work to it; discovered work needs a separate authorized selection.

- Before: or 5 when the user selects 5, reduced by host capacity.
  After: or 5 when the user selects 5, lowered to host capacity when that is smaller.

- Before: also consumes the pool.
  After: also occupies a pool slot.

- Before: unless the user grants another.
  After: unless the user grants a different number.

- Before: preliminary findings can inform unsettled definition but do not accept architecture |
  After: preliminary findings can inform unsettled definition; they do not make an architecture decision accepted |

- Before: reconcile any leaf that a granted leaf reports as not stopped.
  After: reconcile any leaf that a leaf with a delegation grant reports as not stopped.

- Before: Return to any responsibility; there is no batch-wide stage barrier.
  After: Return to any responsibility; do not hold an item until other items finish the same responsibility.

- Before: - An unrelated settled item advances while other definitions continue.
  After: - Advance an unrelated settled item while other items' definitions continue.

- Before: - New coupling stops the affected writers.
  After: - When new coupling appears, stop the affected writers.

- Before: the batch repair budget replaces its counts.
  After: the batch repair budget replaces the counts in corrections.

- Before: - Deferral releases scheduling capacity
  After: - Deferral releases execution capacity

- Before: - Dependents that need the missing result stay ineligible.
  After: - Keep dependents that need the missing result ineligible.

- Before: 5. As coordinator, write the batch record alone.
  After: 5. As coordinator, you are the only writer of the batch record.

- Before: with a usable start prompt.
  After: with a start prompt.


## plugins/lusona/skills/batch/references/assignments.md

- Before: 4. Keep the row to the truthful lifecycle state,
  After: 4. Limit the row to the actual lifecycle state,

- Before: of the current batch handoff so it stays resumable.
  After: of the current batch handoff.

- Before: - An idle leaf still needs a reuse or shutdown decision. Reconcile any leaf that a granted leaf reports as not stopped.
  After: - Decide for each idle leaf whether to reuse it or shut it down. Reconcile any leaf that a leaf with a delegation grant reports as not stopped.


## plugins/lusona/skills/batch/references/authority.md

- Before: - Do not synchronize items into workflow phases.
  After: - Do not hold an item until other items finish the same responsibility.

- Before: - Several selected items can be Doing
  After: - More than one selected item can be Doing

- Before: - New coupling stops affected work for reconciliation before rescheduling.
  After: - When new coupling appears, stop the affected work and reconcile it before rescheduling.


## plugins/lusona/skills/batch/references/deferral-and-resumption.md

- Before: keeps its truthful queue state and blocker.
  After: keeps its actual queue state and blocker.

- Before: stop all affected continuation.
  After: stop all affected work.

- Before: 12. Unresolved deferrals stay excluded until
  After: 12. Keep unresolved deferrals excluded until

- Before: - Report completed history links, deferred and unfinished queue and evidence links, unresolved decisions
  After: - Report history links of completed items, queue and evidence links of deferred and unfinished items, unresolved decisions

- Before: every selected item complete, selection exhausted with deferrals, interrupted with resumable work, or unable to continue safely.
  After: all selected complete, selection exhausted with deferrals, interrupted, or unsafe to continue.


## plugins/lusona/skills/batch/references/integration.md

- Before: 10. Unrun checks and unavailable review block Done.
  After: 10. Do not move the item to Done while a check is unrun or review is unavailable.

- Before: - A later integration requires assessing affected earlier behavior.
  After: - After a later integration, assess the earlier behavior it affects.


## plugins/lusona/skills/batch/references/leaf-rules.md

- Before: - Return the assignment result as soon as the assignment completes, blocks or ends incomplete, before waiting or ending.
  After: - When the assignment completes, blocks or ends incomplete, return the assignment result before waiting or ending.


## plugins/lusona/skills/batch/references/repairs.md

- Before: another approach costs a round from the same item.
  After: another approach charges a round to the same item.

- Before: - A missing consequential decision or authority defers the item at once.
  After: - When a consequential decision or authority is missing, defer the item at once.

- Before: - An interrupted round stays charged.
  After: - Keep an interrupted round charged.

- Before: - Uncertain progress stays charged.
  After: - Keep a round charged when its progress is uncertain.

- Before: - Exhaustion defers the item and its unfinished dependents.
  After: - When the rounds are exhausted, defer the item and its unfinished dependents.


## plugins/lusona/skills/batch/references/workspaces.md

- Before: - A clean checkout of HEAD alone can omit required inputs.
  After: - Do not treat a clean checkout of HEAD as the complete starting content.


## plugins/lusona/skills/design/SKILL.md

- Before: scale fidelity to the question.
  After: match fidelity to the question.

- Before: - Alternatives manufactured for a settled request,
  After: - Alternatives offered for a settled request,

- Before: - Ask only missing questions that change the visual.
  After: - Ask only questions whose answers would change the visual.

- Before: in the browser before agreement.
  After: in the browser before the user agrees.

- Before: Without an owner, create notes
  After: Without an owning record, create notes

- Before: is the owner's basename or notes slug.
  After: is the owning record's basename or notes slug.


## plugins/lusona/skills/experiment/SKILL.md

- Before: Tie each to the decision.
  After: State how each relates to the decision.


## plugins/lusona/skills/explore/SKILL.md

- Before: - As coordinator, keep the conversation with the user.
  After: - As coordinator, conduct the conversation with the user yourself.

- Before: A bounded action advances or tests the vision; it does not replace it.
  After: A bounded action advances or tests the vision; the action does not replace the vision.

- Before: - Explain unfamiliar terms at the user's level.
  After: - Explain unfamiliar terms to match the understanding the user has shown.

- Before: could change the direction, ask that question.
  After: could change the direction, ask the user for it.

- Before: Save it in the existing owner, using relevant sections
  After: Save it in the existing owning record, using relevant sections

- Before: 6. Without an owner, save it in notes
  After: 6. Without an owning record, save it in notes


## plugins/lusona/skills/frame-product/SKILL.md

- Before: Let delivery constraints shape the first outcome without redefining the ambition.
  After: Apply delivery constraints to the first outcome, not to the ambition.

- Before: - Develop the mature experience: whose day changes, what they can accomplish, and the lasting value.
  After: - Develop the mature experience: who benefits, what they can accomplish, and the lasting value.

- Before: - Capture the principles that guide
  After: - Record the principles that guide

- Before: Save it in the existing owner or notes.
  After: Save it in the existing owning record or notes.


## plugins/lusona/skills/implement/SKILL.md

- Before: decompose the change only as far as it needs,
  After: decompose the change only to the depth the decision criteria below require,

- Before: sections of the [change record](../../templates/spec.md.template).
  After: sections of the [spec template](../../templates/spec.md.template).

- Before: - Fix routine plan omissions inline; add no approval gate.
  After: - Fix routine plan omissions inline; add no approval step.

- Before: 9. When setup discovery yields reusable execution or verification steps,
  After: 9. When you find reusable execution or verification steps during setup,

- Before: 10. Record results, check and review evidence, limitations and the current handoff
  After: 10. Record the results, the evidence from checks and reviews, the limitations and the current handoff


## plugins/lusona/skills/investigate/SKILL.md

- Before: Inference is labelled as inference.
  After: Label inference as inference.

- Before: Read the carried hypotheses,
  After: Read the recorded hypotheses,

- Before: for the study boundary.
  After: for the Study entry rules.

- Before: evidence, conclusion and the smallest next action.
  After: evidence, conclusion and the next bounded action.

- Before: or in minimal notes when no owner exists.
  After: or in minimal notes when no owning record exists.

- Before: - No useful authorized experiment remains:
  After: - No authorized distinguishing experiment remains:


## plugins/lusona/skills/map-capabilities/SKILL.md

- Before: Do not write specifications, tasks, tickets or queue entries.
  After: Do not write specifications, tasks, tickets or queue rows.

- Before: write only the concise context the map needs.
  After: write only the context the map needs.

- Before: Do not create specs, tasks, tickets, queue entries or a document per capability.
  After: Do not create specs, tasks, tickets, queue rows or a document per capability.

- Before: Save it in the existing owner or notes.
  After: Save it in the existing owning record or notes.

- Before: Tie each capability to a user outcome and a boundary.
  After: Give each capability a user outcome and a boundary.


## plugins/lusona/skills/measure/SKILL.md

- Before: - Responsibility: valid instruments, comparable observations, and conclusions no stronger than the evidence.
  After: - Responsibility: use valid instruments, collect comparable observations, and state conclusions no stronger than the evidence.

- Before: An encouraging observation is a candidate gain
  After: A favorable observation is a candidate gain

- Before: Reuse an existing owner;
  After: Reuse an existing owning record;


## plugins/lusona/skills/refactor/SKILL.md

- Before: - A manufactured failing test or a claimed red/green cycle.
  After: - A test written only to obtain a failing run, or a claimed red/green cycle.

- Before: sections of the [change record](../../templates/spec.md.template).
  After: sections of the [spec template](../../templates/spec.md.template).

- Before: - Under `none`, verification is still required.
  After: - Under `none`, still verify the restructuring.


## plugins/lusona/skills/review/SKILL.md

- Before: Include relevant new files, not only tracked diffs.
  After: Include new files that belong to the change, not only tracked diffs.

- Before: - When work can overlap or repeat, inspect
  After: - When operations can run concurrently or more than once, inspect

- Before: As coordinator with several reviewers,
  After: As coordinator with more than one reviewer,

- Before: or concise notes when no owner exists,
  After: or concise notes when no owning record exists,


## plugins/lusona/skills/specify/SKILL.md

- Before: blocks a useful definition,
  After: blocks the definition,

- Before: - Agree what completion means, including
  After: - Agree the completion condition, including

- Before: This check adds no review cycle or approval gate.
  After: Do not add a review cycle or an approval step for this check.


## plugins/lusona/skills/status/SKILL.md

- Before: - As coordinator, keep the conversation with the user.
  After: - As coordinator, conduct the conversation with the user yourself.

- Before: - A stale or conflicting record corrected silently.
  After: - A stale or conflicting record corrected instead of reported.

- Before: - Missing Lusona records do not mean no progress. Use the available project evidence; do not require setup.
  After: - When Lusona records are missing, assess progress from the available project evidence; do not require setup.

- Before: Without project evidence, total remaining work is unknown.
  After: Without project evidence, report total remaining work as unknown.

- Before: and give a usable prompt.
  After: and give a prompt.


## plugins/lusona/templates/adr.md.template

- Before: needs: <only when relevant>
  After: needs: <or none>


## plugins/lusona/templates/batch.md.template

- Before: waiting agents still consume host capacity
  After: waiting leaves still consume host capacity

- Before: <identity; model override when relevant>
  After: <identity; model override, or none>

- Before: Replace this section at bounded task boundaries;
  After: Replace this section at each task boundary;

- Before: no silent selection or budget expansion
  After: no selection or budget expansion without the user's authority


## plugins/lusona/templates/brainstorm.md.template

- Before: <Desired future and useful horizon, when relevant. Distinguish
  After: <Desired future and useful horizon. Distinguish

- Before: only when actually accepted>
  After: only when accepted>


## plugins/lusona/templates/evidence.md.template

- Before: <Smallest useful action or missing input,
  After: <Next bounded action or missing input,

- Before: Record unfavorable and null results where material. Preserve observations; add visible corrections with reasons rather than silently replacing earlier results.
  After: Record unfavorable and null results where material. Preserve observations; add each correction and its reason beside the original result instead of replacing it.


## plugins/lusona/templates/history.md.template

- Before: Keep each entry concise; link the change record, existing plan, notes, or ADR that owns the detail.
  After: Do not copy detail into an entry; link the change record, existing plan, notes, or ADR that owns it.


## plugins/lusona/templates/notes.md.template

- Before: link an existing owning record when available>
  After: link the owning record when one exists>

- Before: required when the Lusona retention rule says so;
  After: required under "Spec and queue requirement" in the retention reference;

- Before: instead of appending a session diary.
  After: instead of appending an entry per session.

- Before: if another document becomes its owner.
  After: when another record becomes its owner.

- Before: or deferred with reason; when applicable>
  After: or deferred with reason>

- Before: and supporting evidence; when applicable>
  After: and supporting evidence>

- Before: Replace it as work progresses.
  After: Replace it at each update.


## plugins/lusona/templates/product.md.template

- Before: workflow state lives in the queue.
  After: workflow state is recorded in the queue.

- Before: and usable continuation prompt>
  After: and continuation directive>


## plugins/lusona/templates/review.md.template

- Before: <only relevant suggestions, separate from required corrections>
  After: <suggestions, separate from required corrections, or none>

- Before: no fixes, commits, or deployment are authorized by this review.>
  After: this review authorizes no fixes, commits, or deployment.>


## plugins/lusona/templates/spec.md.template

- Before: state lives there>
  After: state is recorded there>

- Before: ticket link when relevant>
  After: ticket link, or none>

- Before: the Lusona retention rule says so;
  After: "Spec and queue requirement" in the retention reference says so;

- Before: User and host formatting constraints apply.
  After: Follow user and host formatting constraints.

- Before: <relevant ADR links; omit when unnecessary>
  After: <ADR links, or none>

- Before: Optional; bug fixes only.
  After: Bug fixes only; otherwise omit this section.

- Before: An explicit planning-only request stops before implementation.
  After: For an explicit planning-only request, stop before implementation.

- Before: agreed shared contracts; omit when unnecessary>
  After: agreed shared contracts, or none>

- Before: Replace as work progresses.
  After: Replace at each update.

- Before: for user-visible work; omit when irrelevant>
  After: for user-visible work; otherwise omit>

- Before: deployment work; omit when irrelevant>
  After: deployment work; otherwise omit>

- Before: <relevant paths/diff base and active ownership; omit when unnecessary>
  After: <paths/diff base and active ownership, or none>


## plugins/lusona/templates/status.md.template

- Before: Workflow-only orientation uses relevant portions without a repository audit.
  After: For workflow-only orientation, use the sections the question needs; do not audit the repository.


## plugins/lusona/templates/visual-reference.md.template

- Before: Apply the Lusona visual rules.
  After: Apply the visuals reference.

- Before: keep the HTML source alone.
  After: retain only the HTML source.


## plugins/lusona/templates/work.md.template

- Before: Prefer finishing active work before starting another item.
  After: Finish active work before starting another item, unless the user authorized independent work.

- Before: remain safely separated.
  After: stay separated.

- Before: Rows are ordered by priority within each state.
  After: Order rows by priority within each state.

- Before: safely deferred items release
  After: deferred items release

- Before: Completion requirements remain.
  After: Completion requirements still apply.


# Reverted: 23 edits that changed a condition or criterion

These were applied and then reverted. The file text is the original. Each needs a decision before it changes.

- `plugins/lusona/references/closeout.md`
  Current: 2. Record a compact entry in
  Proposed: 2. Record an entry in

- `plugins/lusona/references/commits.md`
  Current: - Do not discard meaningful commit boundaries only
  Proposed: - Do not discard commit boundaries only

- `plugins/lusona/references/commits.md`
  Current: only when explicitly selected or required by the project's workflow.
  Proposed: only when the user explicitly selects it or the project's workflow requires it.

- `plugins/lusona/references/delegation.md`
  Current: 8. Reuse adequate checks on unchanged inputs.
  Proposed: 8. Reuse a valid check result when its inputs are unchanged.

- `plugins/lusona/references/interviews.md`
  Current: Keep a narrow question narrow.
  Proposed: Do not expand a narrow question into a broader interview.

- `plugins/lusona/references/tdd.md`
  Current: - Reuse adequate existing coverage.
  Proposed: - Reuse existing coverage that exercises the change.

- `plugins/lusona/references/visuals.md`
  Current: wireframe for structure, closer styling for look and feel.
  Proposed: wireframe for structure, platform or project-theme styling for appearance.

- `plugins/lusona/skills/architect/SKILL.md`
  Current: - Where several components can update
  Proposed: - Where more than one component can update

- `plugins/lusona/skills/frame-product/SKILL.md`
  Current: - Set a useful horizon without requiring a calendar date.
  Proposed: - Set a horizon from the user's context; do not require a calendar date.

- `plugins/lusona/skills/map-capabilities/SKILL.md`
  Current: the mature experience and a useful first delivery enable.
  Proposed: the mature experience and a first delivery enable.

- `plugins/lusona/skills/refactor/SKILL.md`
  Current: - Do not fix a discovered bug silently.
  Proposed: - Do not fix a discovered bug.

- `plugins/lusona/skills/review/SKILL.md`
  Current: Do not turn every diff into a full audit.
  Proposed: Do not run every practice on every diff.

- `plugins/lusona/skills/specify/SKILL.md`
  Current: label the assumptions that matter.
  Proposed: label the assumptions that could change the outcome.

- `plugins/lusona/templates/brainstorm.md.template`
  Current: <!-- Use for a substantive synthesis, not every turn. Omit irrelevant or empty sections. Apply core recording authority and retention: save substantive synthesis, alternatives, decisions, and open questions in the existing owner or concise notes once useful to guide work or resume, without waiting for a save request. Update for material changes before handoff or completion. Ordinary dialogue and disposable discussion stay in conversation.
  Proposed: <!-- Use when the synthesis meets a "When to save" condition in the retention reference, not every turn. Omit empty sections. Save the synthesis, alternatives, decisions and open questions in the existing owning record, or in notes when none exists, without waiting for a save request. Update the saved text before handoff or completion when one of its items changed. Do not save discussion that meets no "When to save" condition.

- `plugins/lusona/templates/brainstorm.md.template`
  Current: A completed discussion may suggest a useful follow-up. If none is warranted, state: None for this request, with a brief reason.>
  Proposed: When the discussion is complete, propose a follow-up that serves the agreed outcome, or state: None for this request, with a one-sentence reason.>

- `plugins/lusona/templates/evidence.md.template`
  Current: A small result can stay in one dated file;
  Proposed: A single-run result can stay in one dated file;

- `plugins/lusona/templates/evidence.md.template`
  Current: omit for ordinary measurements when irrelevant.
  Proposed: omit for a measurement that declares no trial design.

- `plugins/lusona/templates/spec.md.template`
  Current: <confirmed paths versus proposed new paths when useful; ADR references>
  Proposed: <confirmed paths; proposed new paths labeled as proposals; ADR references>

- `plugins/lusona/templates/spec.md.template`
  Current: Detail the next useful increment; keep later steps concise.
  Proposed: Detail the next increment; expand later steps only to resolve a dependency or answer a planning request.

- `plugins/lusona/templates/spec.md.template`
  Current: Include tasks only when useful; a straightforward change needs no task list.
  Proposed: Include tasks only under the Execution conditions above; clear work needs no task list.

- `plugins/lusona/templates/spec.md.template`
  Current: or recovery makes them useful,
  Proposed: or recovery needs them,

- `plugins/lusona/templates/spec.md.template`
  Current: required inputs, useful skill prompt if needed>
  Proposed: required inputs; continuation directive when another actor or session must continue>

- `plugins/lusona/templates/work.md.template`
  Current: write a compact entry in
  Proposed: write an entry in
