# Work records and retention

Read when saving findings or evidence. Closing or reopening tracked work is a separate
[coordinator procedure](closeout.md).

Apply the [core recording authority and restrictions](../README.md#contract). Save substantive
workflow outputs without waiting for the user to request a record. In discussion, save when a
synthesis captures reusable alternatives and tradeoffs, a supported preference, a meaningful
change in understanding, or an open question and next step needed to resume. Do this once the
synthesis is useful, and update it for material changes; do not defer all recording until the
conversation ends. Ordinary explanations, greetings, acknowledgments, and disposable questions
need no record. Use the existing owner or concise notes; discussion alone requires no spec,
queue item, plan, decision, or TDD selection. Save other substantive outputs before handoff or
completion. A spec and its queue row are required whenever the
workflow calls for a spec (Specify defines every change in one), the user requests a spec or
tracking, a spec already exists, or the change requires independent review for security
boundaries, persistent data, shared contracts, or coordinated multiple writers under
[Review and communication](../README.md#review-and-communication), so the reviewer has
acceptance criteria recorded before implementation starts; a blanket repository review rule
does not by itself require a spec. Size and scope do not decide this. Other direct implement or
refactor work without a spec uses notes. Investigations, measurements, and experiments use notes
and evidence records. Delegated assignments and handoffs within one session keep their handoff
in notes or the owning record. Brief status needs no record.
Explicit no-save/read-only restrictions and write permissions prevail;
report prevented saving and return the result through a permitted channel. A delegated read-only
worker returns findings to its coordinator, which saves them within its own write authority.
Reuse the existing owner; without one, use the smallest suitable notes or change record.
Keep only the outcome, authority and TDD source when applicable, decisions, useful evidence,
material open questions, ownership, correction counts when any, and next action needed to resume. Omit irrelevant fields.
Notes do not require a full spec or execution plan. Direct implement/refactor work without a spec
may use notes for its agreement, decisions, explicit TDD/source, checks/evidence, and handoff.
It can also create a spec directly without Specify; use only relevant template sections.

Creating, updating, or using a spec requires tracking under [queue](queue.md), regardless of the
skill used. Reconcile only the selected item, preserving lifecycle state, Icebox, and history.
Notes alone do not require tracking: do not enroll spec-free work or restore deleted records
merely to save recovery context; an Ideas row for a distinct follow-up does not enroll the
current work. Existing tracked work remains tracked.
Keep `work.md` as an index of open outcomes: one short row per item, linking its owning
records, with a concise completion condition and current blocker or next action. Keep task
evidence, measurements, decisions, and activity narration out of the queue. Icebox rows
remain open and retain evidence under the [queue rules](queue.md); parking
is separate from completion and historical archival.

During authorized work beyond discussion, tracked or not, keep unresolved supported
goal-relevant outcomes discoverable when the current assignment closes: link an existing open
item or add a distinct proposal under the queue rules, creating the queue from its template when
absent. When saving is restricted, report the unowned follow-up through a permitted channel. Reference the owning evidence once; do not leave the only next action buried
in completed work. Retain evidence, uncertainty, and a next action; deferred proposals need a
reason or revisit condition. A proposal does not authorize execution or join an active batch.

Record each fact once. New change records own accepted scope, acceptance criteria, explicit
TDD, optional execution steps, verification evidence, and one current handoff replaced as work
progresses. Preserve established ownership for existing separate specs and plans. ADRs own
consequential architecture decisions. Add an execution section only when sequencing,
dependencies, uncertainty, recovery, or a long run whose earlier context will be summarized
before it finishes makes it useful; straightforward work needs no task list.
Tasks reference acceptance criteria rather than restating them. Save routine verification
evidence directly in the change record whether or not it has tasks. For material measurements and experiments, follow
[evidence](evidence.md): new records live in `docs/lusona/evidence/`, and change records, notes,
and history link the exact runs they rely on. Existing evidence stays in place; do not migrate
it merely to adopt the new layout. Split a new record only for separate ownership,
reuse, or readability, retaining links and one owner for each fact. Use `notes/<change-slug>.md`
for useful exploration decisions, open questions, investigations or findings
without an existing owner; an Ideas item needs no premature spec. Link notes from the queue
or owning record when available. Retain facts
needed to resume, explain a decision, reproduce a result, or avoid repeating investigation;
omit routine narration. Correct refuted findings beside the original claim and revise the
resulting recommendation. If a fact gains a change record or ADR owner, replace the notes copy
with a link.

Consolidate ordinary evidence, queue, and handoff edits at meaningful boundaries and before
an intentional handoff or completion, including when pausing work. Missing directories or a queue
do not waive saving: create the needed record directories within permitted writes. Write only changed facts;
do not write every turn or refresh records solely because a skill stage ended. Save
authorization, blockers, ownership changes, and required
batch recovery state when needed for safe continuation. These saves are working-tree edits,
not commit boundaries; group them under the [commit procedure](commits.md).

Use the bundled work-record helper ([Bash](../scripts/work-record.sh) or
[PowerShell](../scripts/work-record.ps1)) for initial notes structure.
Resolve its path from the loaded plugin, not the consuming repository's current directory;
from a skill it is `../../scripts/work-record.sh`.
Follow [shell selection and invocation](work-record.md) for PowerShell paths and commands.

```bash
bash /resolved/plugin/scripts/work-record.sh slug "Work item title"
bash /resolved/plugin/scripts/work-record.sh init-notes /absolute/project/root work-item-title
```

```powershell
powershell.exe -NoProfile -File "C:\resolved\plugin\scripts\work-record.ps1" slug "Work item title"
powershell.exe -NoProfile -File "C:\resolved\plugin\scripts\work-record.ps1" init-notes "C:\project" work-item-title
```

Reuse an existing item slug; use `slug` for new names. Pass an explicit project root for
initialization; existing files are preserved. `init-notes` loads the bundled notes template and
fills its slug. The helper initializes records and returns paths; it does not record evidence
or establish completion. Do not initialize project data merely for orientation or installation.
For closing or reopening tracked work, the coordinator applies [closeout](closeout.md).
