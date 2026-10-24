# Work queue

States: Ideas → Ready → Doing → Review → Done. Prefer finishing active work before
starting another item. Blockers or pending acceptance do not prevent independent authorized
work when writers and unfinished changes remain safely separated.
Rows are ordered by priority within each state.
Blocked is a flag with a reason and next action, not a separate state.
Explicit batch authorization may override scheduling defaults: safely deferred items release
execution capacity while retaining their actual state and blocker. Completion requirements remain.

## Active queue

| Item / change | State | Completion condition | Current blocker or next action |
| --- | --- | --- | --- |

No active work selected.

## Icebox

Parked outcomes are excluded from active planning and default batch selection. Move them
back to Active queue only on explicit reactivation; retain their lifecycle state and links.

| Item / change | State when parked | Completion condition | Parking reason / revisit condition |
| --- | --- | --- | --- |

No parked work.

## Record keeping

Keep one short row per open outcome across both sections. Agreement, optional execution steps, evidence,
and one current handoff belong in the linked change record; preserve existing split ownership.
Optional `notes/<change-slug>.md` holds durable findings without another owner; do not add
activity logs or evidence paragraphs here. Before removing a completed row, preserve its
completion condition and unique facts, write a compact entry in `history/YYYY-MM-week-NN.md`,
and verify its evidence links. History owns archived state; reopened work returns here with
a backlink to its historical completion entry.
