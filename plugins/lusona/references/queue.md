# Work queue

Read when creating, updating, or using a spec, or maintaining or assessing tracked state, selection, or parking.

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

Every new spec requires a row in `docs/lusona/work.md`, regardless of which skill creates it.
The coordinator creates a missing queue from [its template](../templates/work.md). Reconcile the
selected spec with its existing row or historical entry before adding anything; updates reuse
that item without duplication. New drafts start Ideas. Ready requires accepted scope and criteria,
an explicitly selected TDD policy, and no blocking definition questions. Preserve existing
lifecycle state, Icebox placement, and history; an ordinary spec edit does not reset or reopen work.
When planning, implementing, or refactoring from an existing spec, repair its missing row before
planning handoff or execution, using supported current state. Do not scan or backfill unrelated specs
or restore archived completed items. Reopening requires explicit authority and [closeout](closeout.md).

These requirements remain subject to explicit no-save/read-only restrictions and write permissions.
If saving is prohibited or unavailable, report the missing tracking through a permitted channel.
Delegated workers return required queue changes to the coordinator; they do not write shared state.
Read-only assessment reports gaps without repairing them.

The coordinator moves selected authorized implementation or refactoring to Doing when execution
starts; planning-only work never enters Doing. Queue membership does not authorize implementation
or select TDD. Direct work without a spec may remain untracked and retain agreement, decisions,
TDD/source, checks/evidence, and handoff in notes under [retention](retention.md). Creating a spec
activates the tracking requirement; existing tracked work remains tracked. A recovery note alone
does not require a queue, full spec, or history entry.
Move work to Review when evidence is ready; list outstanding checks explicitly.
Done requires the whole item's completion condition, acceptance criteria, required checks, and
any required acceptance or delivery. Failed or unrun required checks block completion; passing
tests do not establish human acceptance. Return rejected work to Doing for authorized correction,
or Ideas/Ready when scope needs reconsideration. A transition does not authorize fixes.
Completed items stay Done unless explicitly reopened; separately requested refactoring may use
its own item. Reviews recommend a state without writing the queue unless saving is authorized.

Before removing a completed row or reopening archived work, the coordinator applies
[closeout](closeout.md), preserving history and affected links.
