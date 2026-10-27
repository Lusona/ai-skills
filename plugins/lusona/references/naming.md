# Document names and headers

Read before creating, updating, or renaming spec, plan, or ADR records.

New specs and ADRs use `YYYYMMDD-functional-name.md`, such as
`specs/20260926-add-python-support.md` or `adr/20260926-python-runtime.md`.
The complete basename is the record ID. The prefix is the creation date in the local
timezone, not a sequence or priority. Preserve the ID and filename on later edits.
Existing spec/plan pairs retain their shared basename. Do not create a companion plan
for new changes by default.

Use the bundled work-record helper ([Bash](../scripts/work-record.sh) or
[PowerShell](../scripts/work-record.ps1)) to generate the name,
check the destination, and create the record exclusively from its template. Resolve the
helper relative to the loaded plugin, not the consuming project's working directory.
Choose a descriptive functional slug; use `slug` to normalize a title when needed.
Follow [shell selection and invocation](work-record.md) for the available environment.

```bash
bash /resolved/plugin/scripts/work-record.sh slug "Add Python support"
bash /resolved/plugin/scripts/work-record.sh init-change /absolute/project/root add-python-support
bash /resolved/plugin/scripts/work-record.sh init-adr /absolute/project/root python-runtime
```

```powershell
powershell.exe -NoProfile -File "C:\resolved\plugin\scripts\work-record.ps1" slug "Add Python support"
powershell.exe -NoProfile -File "C:\resolved\plugin\scripts\work-record.ps1" init-change "C:\project" add-python-support
powershell.exe -NoProfile -File "C:\resolved\plugin\scripts\work-record.ps1" init-adr "C:\project" python-runtime
```

Both creation commands accept an optional `YYYY-MM-DD` creation date; otherwise they
use local today. They return one JSON object on stdout with `status`, `path`, and `message`:

| Status | Exit code | Agent action |
| --- | --- | --- |
| `created` | 0 | Use the returned absolute path; fill the title and relevant template sections. |
| `conflict` | 3 | Inspect the existing path. Resume only if it is the intended existing record and ownership permits it; for distinct work choose a more specific functional slug and retry. |
| `error` | 1 | Correct the reported input or filesystem problem before retrying; `path` is empty if no destination was resolved. |

Creation never overwrites or silently resumes an existing path, including a symlink or
directory. Identical inputs resolve to the same path; there is no automatic numeric or
random suffix. Independent records can be created concurrently without a shared allocator.
Exclusive creation prevents two writers from claiming the same path in one filesystem;
isolated branches can still create the same basename. Reconcile record identity, ownership,
and affected links before integration; do not combine unrelated records automatically.
Queue updates, shared handoffs, and overlapping edits still require coordinated ownership.

The helper fills the record ID and initial Created/Updated dates. After substantive edits,
use `stamp-header FILE [YYYY-MM-DD]`; Created remains immutable and only Updated changes.
The command rejects invalid headers or dates that move backwards. Do not stamp on reads.
Completion dates remain in history; spec and plan headers do not duplicate queue state.
ADRs retain decision status, scope, authority, and supersession references.

Legacy `next-change` and `next-adr` remain available for existing numbered workflows only.
They ignore valid dated records and retain their existing sequence validation; they do not
reserve numbers and must not be used to name new records under this convention.

Existing filenames and headers, including separate plans, remain valid. Do not invent a number or creation
date for an old document. Renaming existing records or adopting the new headers requires
an authorized migration that preserves dates, evidence, and links; normal work does not
trigger one.
