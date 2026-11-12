# Record names, headers and helper commands

Read before creating, updating or renaming a spec, plan, ADR, notes or history record, or before running the work-record helper.

## Record names

- New specs and ADRs use `YYYYMMDD-functional-name.md`, for example `specs/20260926-add-python-support.md` or `adr/20260926-python-runtime.md`.
- The complete basename is the record ID.
- The prefix is the creation date in the local timezone. It is not a sequence or a priority.
- Preserve the ID and filename on later edits.
- An existing spec and its execution record keep their shared basename.
- Do not create an execution record for a new change.
- Choose a descriptive functional slug. Normalize a title into a slug with `slug`.
- Reuse an item's existing slug.

## Creating a spec or ADR

Create each spec with `init-change` and each ADR with `init-adr`. The helper generates the name, checks the destination and creates the record from its template. Both commands accept an optional `YYYY-MM-DD` creation date; without one, they use today's date in the local timezone. They return one JSON object on stdout with `status`, `path` and `message`:

| Status | Exit code | Agent action |
| --- | --- | --- |
| `created` | 0 | Use the returned absolute path; fill the title and the template sections the work has content for. |
| `conflict` | 3 | Inspect the existing path. Resume only if it is the intended existing record and ownership permits it; for distinct work choose a more specific functional slug and retry. |
| `error` | 1 | Correct the reported input or filesystem problem before retrying; `path` is empty if no destination was resolved. |

- Branch on status and exit code, not on the `message` text.
- Creation never overwrites or silently resumes an existing path, including a symlink or directory.
- Identical inputs resolve to the same path. There is no automatic numeric or random suffix, and no shared counter.
- Independent records can be created concurrently without a shared allocator.
- Exclusive creation stops two writers from claiming the same path in one filesystem. Isolated branches can still create the same basename.
- Before integration, reconcile record identity, ownership and affected links. Do not combine unrelated records automatically.
- As a leaf, return queue updates and shared handoff changes to the coordinator. Do not edit files that another writer owns.
- After initialization, fill the template sections the work has content for, within the existing work authority.

## Headers

- The helper fills the record ID and the initial Created and Updated dates.
- After an edit that changes a record's content, run `stamp-header FILE [YYYY-MM-DD]`. Created never changes; only Updated changes.
- `stamp-header` requires exactly one `Created:` and one `Updated:` field, each holding a valid date or `<YYYY-MM-DD>`.
- `stamp-header` rejects invalid headers and dates that move backwards.
- Do not stamp a record you only read.
- Record completion dates only in history. Do not repeat the queue state in spec or plan headers.
- An ADR keeps its decision status, scope, authority and supersession references.

## Existing and legacy records

- Existing filenames and headers remain valid, including execution records.
- Do not invent a number or creation date for an old record.
- Rename existing records or adopt the new headers only in an authorized migration that preserves dates, evidence and links.
- Use `next-change` and `next-adr` only for existing numbered workflows. Never use them to name a new record.
- Legacy sequence commands are read-only, ignore dated records and reserve nothing. They keep their existing sequence validation.
- Legacy numbered filenames use `NNNN-lowercase-slug.md`. `README.md` is ignored.
- Change scans ignore legacy filenames unless they begin with a digit.
- A legacy spec and its execution record with matching basenames share a number. Conflicting slugs are rejected.

## Running the helper

- Use [Bash](../scripts/work-record.sh) in a Bash environment. Use [PowerShell](../scripts/work-record.ps1) in a native Windows PowerShell environment.
- Choose by the shell the agent runs in, not by the operating system alone. A Windows WSL session uses Bash.
- Resolve the helper from the loaded plugin, never from the consuming project's current directory. Use the absolute path of the linked script.
- Both helpers use the same commands, arguments, statuses and exit codes.
- Bash `help` prints a short reminder. PowerShell `help` prints usage.
- Pass absolute project paths in the executing shell's filesystem. PowerShell returns native absolute paths.
- History paths are project-relative and use `/`.
- PowerShell emits UTF-8 output, including JSON paths. A subprocess caller decodes it as UTF-8.
- Do not pass a Windows drive path to a WSL helper. Do not reinterpret returned paths in another shell.
- The PowerShell helper targets Windows PowerShell 5.1 and PowerShell 7. For PowerShell 7, use `pwsh` in place of `powershell.exe`.
- Follow the host's script execution policy. When execution is blocked, do not change the policy; report the blocked command and the required environment.
- The helpers use bundled templates and do not require Python.

```bash
bash /resolved/plugin/scripts/work-record.sh slug 'Add invitation expiry'
```

```powershell
powershell.exe -NoProfile -File "C:\resolved\plugin\scripts\work-record.ps1" slug 'Add invitation expiry'
```

## Commands and arguments

Pass a command followed by its arguments to the resolved helper. Quote titles and paths that contain spaces. `DATE` is `YYYY-MM-DD` and defaults to today in the local timezone.

| Command | Arguments | Result |
| --- | --- | --- |
| `slug` | `TITLE` | Print a lowercase ASCII change slug |
| `history-path` | `[DATE]` | Print the project-relative weekly history path |
| `init-history` | `PROJECT_ROOT [DATE]` | Create a weekly history file if absent |
| `init-notes` | `PROJECT_ROOT SLUG` | Create an item's notes file if absent |
| `init-change` | `PROJECT_ROOT SLUG [DATE]` | Create a new `YYYYMMDD-slug` spec |
| `init-adr` | `PROJECT_ROOT SLUG [DATE]` | Create a new `YYYYMMDD-slug` ADR |
| `next-adr` | `PROJECT_ROOT` | Legacy: print the next four-digit ADR number |
| `next-change` | `PROJECT_ROOT` | Legacy: print the next change number, including execution records |
| `stamp-header` | `FILE [DATE]` | Initialize Created and update Updated |
| `help` | None | Show help; `-h` and `--help` are aliases |

- Weeks are month-local: 01 covers days 1–7, 02 covers 8–14, through 05 for 29–end.
- `init-history` and `init-notes` print the absolute path and preserve existing regular files.
- Initialization never overwrites or merges records.
