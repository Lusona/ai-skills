# Work queue

Read when maintaining or assessing tracked state, selection, or parking.

The coordinator alone updates queue and saved handoff state during authorized work. The queue
tracks whole outcomes, not individual coding tasks; Ready does not authorize execution.
Prefer finishing active work before starting another item. A blocker or pending acceptance
need not prevent independent work already authorized by the user, provided writers and unfinished
changes remain safely separated. Blocked is a flag with its reason and next action.
Use [batch execution](batch-execution.md) for unattended multi-item scheduling and recovery.

Keep separate **Active queue** and **Icebox** sections. Icebox holds deliberately parked
outcomes with their lifecycle state, completion condition, evidence links, and a short parking
reason or revisit condition. Move rows rather than copying them. Park or reactivate work only
within explicit user direction; a revisit condition prompts reconsideration, not automatic revival.
Icebox is excluded from active planning and default batch selection, including “all current queue
items.” Explicitly selecting parked work for execution reactivates it; discussing it does not.
Before parking started work, stop its writers and preserve isolated changes and a recovery handoff.
Parking does not complete work, erase blockers, or reset batch repair counts. A batch deferral
alone does not move an item to Icebox. Existing queues without sections remain active queues;
add sections when next updating them without silently parking existing rows.

| State | Meaning | Owning procedure |
| --- | --- | --- |
| Ideas | Possible outcome | [specify](../skills/specify/SKILL.md) |
| Ready | Accepted definition and selected TDD | [specify](../skills/specify/SKILL.md) |
| Doing | Authorized implementation | [implement](../skills/implement/SKILL.md) |
| Review | Evidence ready for review or acceptance | [implement](../skills/implement/SKILL.md), [review](../skills/review/SKILL.md) |
| Done | Agreed completion condition met | [implement](../skills/implement/SKILL.md) |

The coordinator creates a missing queue from [its template](../templates/work.md) when workflow
tracking is needed and moves selected authorized implementation or refactoring to Doing when it starts.
A recovery note alone does not require a queue, full spec, or history entry; do not enroll
untracked conversation solely because it needs retention. Update an existing tracked item
when applicable without creating records solely to satisfy a skill.
Move work to Review when evidence is ready; list outstanding checks explicitly.
Done requires the whole item's completion condition, acceptance criteria, required checks, and
any required acceptance or delivery. Failed or unrun required checks block completion; passing
tests do not establish human acceptance. Return rejected work to Doing for authorized correction,
or Ideas/Ready when scope needs reconsideration. A transition does not authorize fixes.
Completed items stay Done unless explicitly reopened; separately requested refactoring may use
its own item. Reviews recommend a state without writing the queue unless saving is authorized.

Before removing a completed row or reopening archived work, the coordinator applies
[closeout](closeout.md), preserving history and affected links.
