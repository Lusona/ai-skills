# Work queue

Read before creating, updating or using a spec, and before maintaining or assessing queue state, selection or parking.

## States

The queue in `docs/lusona/work.md` tracks whole outcomes, not individual coding tasks.

| State | Meaning | Owning skill |
| --- | --- | --- |
| Ideas | Possible outcome | [specify](../skills/specify/SKILL.md) |
| Ready | Accepted definition and selected TDD | [specify](../skills/specify/SKILL.md) |
| Doing | Authorized implementation | [implement](../skills/implement/SKILL.md) |
| Review | Verification evidence saved; review or acceptance remains | [implement](../skills/implement/SKILL.md), [review](../skills/review/SKILL.md) |
| Done | Agreed completion condition met | [implement](../skills/implement/SKILL.md) |

- Icebox is a section of the queue, not a queue state. It holds deliberately parked outcomes; each parked row keeps its queue state. The coordinator parks and reactivates rows on user direction.
- No state authorizes implementation, including Ready. Queue membership does not select a TDD level.
- Selecting one task for implementation does not authorize the rest of its change.
- Blocked is a flag on a row, with its reason and next action. It is not a state.

## Shared-state ownership

- As a leaf, return required queue changes and new rows to the coordinator.
- In a read-only assessment, report gaps; do not repair them.
- In a review, recommend a state; do not write the queue.
- When saving is prevented, report the missing tracking in the reply.

## Rows

- Every new spec needs a row in `docs/lusona/work.md`, whichever skill creates it.
- A follow-up found during untracked work gets an Ideas row that links the notes that found it.
- When the queue is missing, create it from the [queue template](../templates/work.md.template).
- Before adding a row, reconcile the selected spec with its existing row or history entry. Update that item; do not duplicate it.
- A new draft starts in Ideas.
- Ready requires accepted scope and criteria, an explicitly selected TDD level, and no blocking definition questions.
- Preserve existing queue state, Icebox placement and history. A spec edit alone does not reset or reopen work.
- When planning, implementing or refactoring from an existing spec without a row, add its row in the queue state that the evidence supports, before the planning handoff or before execution starts.
- Do not scan or backfill unrelated specs. Do not restore archived completed items.
- Direct work without a spec may stay untracked. Existing tracked work stays tracked.
- A recovery note alone does not require a queue row, full spec or history entry.

## Transitions

- Finish active work before starting another item, unless the user authorized independent work. A blocker or pending acceptance does not stop authorized independent work when writers and unfinished changes stay separated.
- Move selected authorized implementation or refactoring to Doing when execution starts. Planning-only work never enters Doing.
- Move work to Review when its verification evidence is saved in the owning record and review or acceptance remains. List outstanding checks explicitly.
- Move an item to Done only when its whole completion condition and acceptance criteria are met, its required checks pass, and any required acceptance or delivery has happened.
- Failed or unrun required checks block Done. Passing tests do not establish human acceptance.
- Return rejected work to Doing for authorized correction, or to Ideas or Ready when its scope needs reconsideration. A transition does not authorize fixes.
- Completed items stay Done unless explicitly reopened. A separately requested refactoring may use its own item.
- Reopening requires explicit authority.

## Icebox and parking

- Keep separate **Active queue** and **Icebox** sections.
- An Icebox row keeps its queue state, completion condition and evidence links, plus a one-sentence parking reason or revisit condition.
- Move rows between sections; do not copy them.
- Park or reactivate work only on explicit user direction. When a revisit condition is met, ask the user whether to reactivate the item; do not reactivate it automatically.
- Icebox rows are excluded from active planning and from default batch selection, including "all current queue items".
- Selecting parked work explicitly for execution reactivates it. Discussing it does not.
- Before parking started work, stop its writers and preserve isolated changes and a recovery handoff.
- Parking does not complete work, clear blockers or reset batch repair counts.
- A batch deferral alone does not move an item to Icebox.
- An existing queue without sections is an active queue. Add the sections at its next update without parking existing rows.
- Unattended multi-item scheduling and recovery belong to [batch](../skills/batch/SKILL.md).
