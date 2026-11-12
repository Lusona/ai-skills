# Closeout

Read as coordinator before closing or reopening tracked work, before removing a Done row, and before updating product or architecture documentation after an enduring change.

## Close an item

1. Confirm the whole item meets its agreed completion condition. Closeout does not waive required checks, acceptance, delivery or authorization.
2. Record an entry in `docs/lusona/history/YYYY-MM-week-NN.md`.
3. Under Completed items, give each dated item its own heading, an Outcome section, a Completion and evidence section, and an optional Related records section.
4. When the project already uses another history format that keeps those facts and stable links, keep that format.
5. Move facts that exist only in the queue row into their owning records.
6. Update links that point to the queue row.
7. Verify the history entry and the updated links.
8. Remove the queue row only after step 7 passes.

- After closeout, history owns the archived state. Do not repeat it in change records or notes.
- Untracked work needs no history entry. Save its substantive outputs under the retention rules.

## History file

- Create a missing history file with the work-record helper command `init-history`.
- When the work was completed before today, pass its actual completion date.
- `init-history` loads the [history template](../templates/history.md.template) and fills its period. In a new file, copy the template's commented item structure for each completed outcome.
- Keep existing history records and link targets intact.
- The helper does not record evidence. Record the completion evidence yourself.

## Reopen an item

- Restore the item's queue row and current state to the queue.
- Link the row to its historical completion entry.
- Leave the history entry unchanged.
- Read history only when it relates to the selected work.

## Enduring changes

- When a change alters enduring behavior or constraints, update the existing product and architecture documentation.
- Mark proposals as proposals, separate from current behavior.
