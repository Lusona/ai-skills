# Retention and handoff

Read before saving findings, evidence or a handoff, before choosing a record for them, before a checkpoint, and when context use reaches 40%.

## When to save

- An output is substantive when later work or another session depends on it: a decision, an agreement, evidence, a finding, a handoff, or a discussion synthesis that meets the next rule.
- In discussion, save a synthesis when it holds at least one of these:
  - reusable alternatives and tradeoffs;
  - a supported preference;
  - a change in understanding that alters a decision or next action;
  - an open question and the next step needed to resume.
- Save it as soon as it holds one of them. Update it when one of them changes.
- Do not defer all saving to the end of the conversation.
- Consolidate evidence, queue and handoff edits at the end of each increment and before handoff, completion or a pause.
- Write only changed facts. Do not write every turn, and do not refresh records only because a skill ended.
- Save authorization, blockers, ownership changes and batch recovery state when another session needs them to continue.
- These saves are working-tree edits, not commit boundaries. Commit them with the increment they belong to.
- Missing directories or a missing queue do not waive saving. Create the record directories within permitted writes.

## No-record cases

- Explanations, greetings, acknowledgments, questions and status updates that no later work or other session depends on need no record.
- Discussion alone requires no spec, queue item, plan, decision or TDD selection.
- Saving does not select a TDD level, does not require `specify`, and does not authorize implementation.
- A requested standalone document remains a deliverable in the location the user named.

## Record choice

Reuse the existing owning record. Without one, choose by this table.

| Work | Record |
| --- | --- |
| A change that requires a spec (next section) | Spec in `docs/lusona/specs/` and its queue row |
| Direct implement or refactor work without a spec | `docs/lusona/notes/<change-slug>.md`, holding its agreement, decisions, TDD level and source, checks, evidence and handoff |
| Investigation, measurement or experiment | Notes, plus evidence records in `docs/lusona/evidence/` |
| Exploration decisions, open questions or findings without an owning record | `docs/lusona/notes/<change-slug>.md` |
| Consequential architecture decision | ADR in `docs/lusona/adr/` |
| Delegated assignment or handoff within one session | Notes or the owning record |

- Any direct implement or refactor work may also create a spec without `specify`, using only the template sections the work has content for.
- Notes do not require a full spec or execution plan. An Ideas item needs no spec yet.
- Link notes from the queue row or the owning record when one exists.
- In notes, keep only the outcome, authority, TDD level and source when set, decisions, evidence, open questions, ownership, correction counts when any, and the next action. Omit fields that do not apply.

## Spec and queue requirement

- A spec and its queue row are required when any of these holds:
  - The skill in use defines changes in a spec; `specify` defines every change in one.
  - The user requests a spec or tracking.
  - A spec already exists for the change.
  - The change requires independent review because of what it affects, not only because a user or repository rule requires review. The spec records the acceptance criteria before implementation starts.
- Size and scope do not decide whether a spec is required.
- Notes alone do not require tracking. Do not add spec-free work to the queue, and do not restore deleted records, only to save recovery context.
- An Ideas row for a distinct follow-up does not put the current work in the queue.

## Queue index and follow-ups

- Keep `docs/lusona/work.md` an index of open outcomes: one row per item, linking its owning records, with a one-sentence completion condition and the current blocker or next action.
- Keep task evidence, measurements, decisions and activity narration out of the queue.
- Parking an item in Icebox is neither completion nor archival in history.
- Relate each concrete gap you find to an established goal. Separate current blockers from proposed outcomes.
- Report the uncertainty and the next bounded action, without implying that the action completes the goal.
- Do not invent requirements. Do not audit the whole product unless the user asks.
- When an assignment for authorized work beyond discussion closes, link each unresolved, supported outcome that serves an established goal to an existing open item, or add it to the queue as a distinct proposal. Create the queue from its template when absent.
- When saving is prevented, report the unowned follow-up in the reply.
- Reference the owning evidence once. Do not leave the only next action inside a completed item's record.
- Give each proposal its evidence, uncertainty and next action. Give a deferred proposal a reason or a revisit condition.
- A proposal does not authorize execution or join an active batch.
- Findings, proposals, splits, deferrals and priority changes do not expand authority, batch selection or accepted priorities.

## Record content

- Record each fact once.
- A new change record owns the accepted scope, acceptance criteria, TDD level, optional execution steps, verification evidence, and one current handoff that each update replaces.
- For an existing spec or execution record, keep its established ownership.
- Tasks reference acceptance criteria. They do not restate them.
- Save routine verification evidence in the change record, with or without tasks.
- Save new measurement and experiment records in `docs/lusona/evidence/`. Change records, notes and history link the exact runs they rely on.
- Leave existing evidence and notes in place. Do not migrate them to adopt a new layout.
- Split a new record only for separate ownership, reuse or readability. Keep the links and one owner for each fact.
- Keep the facts needed to resume, explain a decision, reproduce a result, or avoid repeating an investigation. Omit routine narration.
- When a finding is refuted, correct it beside the original claim and revise the resulting recommendation.
- When a fact gains a change record or ADR owner, replace the notes copy with a link.

## Create notes

- Create new notes with the work-record helper command `init-notes`.
- Reuse an existing item slug. For a new item, derive the slug with the helper command `slug`.
- `init-notes` loads the bundled notes template and fills its slug.
- The helper does not record evidence or establish completion.
- Do not create project data only for orientation or installation.

## Handoff and checkpoint

- Write the handoff into the owning record's current handoff. Replace its predecessor.
- The handoff carries the objective, decisions, authority, TDD level and source, paths, evidence, uncertainty, correction counts, blockers, ownership and the next action.
- Carry outcome, accepted decisions, authority, TDD level, evidence and uncertainty across turns, skills, sessions and handoffs.
- When saving is prevented, return the handoff in the reply and state what cannot be recovered.
- Before transfer, finish or pause each bounded operation in a recoverable state.
- When another actor or session must continue the work, give a continuation directive. The directive does not replace authorized work you can do now.
- Do not claim a checkpoint that an abrupt interruption prevented.
- A checkpoint does not end authorization and does not require a new session.

## Resume

- Resume from the surviving records and the working tree.
- Ask the user only for authority, or for a fact that changes the next action, when the records cannot supply it.

## Context budget

- When the host reports context use, prepare a handoff at 40% and complete it before 50%.
- Do not estimate usage the host does not report. Do not claim a transfer that did not happen.
- Without usage telemetry, checkpoint at task boundaries, not at skill changes.
