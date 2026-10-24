# Closeout and reopening

Coordinator-only: read when closing or reopening tracked work. Conversation-only work needs
no history entry. Apply [retention](retention.md) only if saving or relocating evidence is needed.

When the whole item meets its agreed completion condition, record a compact entry in
`history/YYYY-MM-week-NN.md` using the [history template](../templates/history.md).
Under Completed items, each dated item has its own heading, outcome, completion and
evidence section, and optional related records. Preserve an existing project format when it
retains those facts and stable links. Preserve any unique queue facts in their
owning records, update links that targeted the removed row, and verify the history entry
and links before removing the queue row. This
closeout does not waive required checks, acceptance, delivery, or authorization. History then
owns archived state; change records and notes do not duplicate it. Reopening an item restores its row
and current state ownership to the queue with a backlink to its historical completion entry;
leave that entry as a historical fact. Read history only when relevant to the selected work.

Use the bundled [work-record helper](../scripts/work-record.sh) for history names, dates,
and initial structure. Resolve its path from the loaded plugin, not the consuming repository's
current directory; from a skill it is `../../scripts/work-record.sh`.

```bash
bash /resolved/plugin/scripts/work-record.sh history-path 2026-09-10
bash /resolved/plugin/scripts/work-record.sh init-history /absolute/project/root 2026-09-10
```

History uses month-local week numbers: 01 for days 1–7, 02 for 8–14, 03 for 15–21,
04 for 22–28, and 05 for 29–month end. September 10, 2026 belongs in
`2026-09-week-02.md`. The date defaults to local today; pass the actual completion date for
older work. Pass an explicit project root for initialization; existing files are preserved.
`init-history` loads the bundled history template and fills its period. Copy its commented
item structure for each completed outcome in new history files; keep existing records and
link targets intact. The helper initializes records and returns paths; the coordinator
records completion evidence and removes queue rows only after verifying preservation.
Do not initialize project data merely for orientation or installation.
