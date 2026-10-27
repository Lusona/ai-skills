# Work-record helpers

Use [Bash](../scripts/work-record.sh) in a Bash environment, or
[PowerShell](../scripts/work-record.ps1) in a native Windows PowerShell environment.
Choose from the agent's available shell, not just the operating system: a Windows WSL
session uses Bash. Resolve the helper from the loaded plugin, never from the consuming
project's current directory. From a skill, the paths are `../../scripts/work-record.sh`
and `../../scripts/work-record.ps1`.

Both helpers use the same commands, arguments, statuses, and exit codes. Use the command
reference below; Bash `help` prints a short reminder, while PowerShell `help` prints usage.
Pass absolute project paths in the executing shell's filesystem;
PowerShell returns native absolute paths. History paths are project-relative and use `/`.
PowerShell emits UTF-8 output, including JSON paths; subprocess callers should decode it as UTF-8.
Do not pass a Windows drive path to a WSL helper or reinterpret returned paths in another shell.

```bash
bash /resolved/plugin/scripts/work-record.sh slug 'Add invitation expiry'
```

```powershell
powershell.exe -NoProfile -File "C:\resolved\plugin\scripts\work-record.ps1" slug 'Add invitation expiry'
```

The PowerShell helper targets Windows PowerShell 5.1 and PowerShell 7; use `pwsh`
in place of `powershell.exe` for PowerShell 7. Follow the host's script execution policy;
do not change policy automatically when execution is blocked. Report the blocked command
and required environment instead. The helpers use bundled templates and do not require Python.

For record identity and creation responses, apply [naming](naming.md); for notes and
history, apply [retention](retention.md) and [closeout](closeout.md). After initialization,
fill the relevant template sections within the existing work authorization.

## Commands and arguments

Pass a command followed by its arguments to the resolved helper. Quote titles and paths
containing spaces. `DATE` is `YYYY-MM-DD` and defaults to today in the local timezone.

| Command | Arguments | Result |
| --- | --- | --- |
| `slug` | `TITLE` | Print a lowercase ASCII change slug |
| `history-path` | `[DATE]` | Print the project-relative weekly history path |
| `init-history` | `PROJECT_ROOT [DATE]` | Create a weekly history file if absent |
| `init-notes` | `PROJECT_ROOT SLUG` | Create an item's notes file if absent |
| `init-change` | `PROJECT_ROOT SLUG [DATE]` | Create a new `YYYYMMDD-slug` spec |
| `init-adr` | `PROJECT_ROOT SLUG [DATE]` | Create a new `YYYYMMDD-slug` ADR |
| `next-adr` | `PROJECT_ROOT` | Legacy: print the next four-digit ADR number |
| `next-change` | `PROJECT_ROOT` | Legacy: print the next change number, including plans |
| `stamp-header` | `FILE [DATE]` | Initialize Created and update Updated |
| `help` | None | Show help; `-h` and `--help` are aliases |

Weeks are month-local: 01 covers days 1–7, 02 covers 8–14, through 05 for 29–end.
`init-history` and `init-notes` print the absolute path and preserve existing regular
files. Reuse an item's existing slug; initialization never overwrites or merges records.

`init-change` and `init-adr` print JSON with `status`, `path`, and `message` fields:
`created` (exit 0), `conflict` (exit 3), or `error` (exit 1). They reject existing paths,
including symlinks. New specs and ADRs use the creation date and a functional slug;
no counter is shared. Diagnostic wording is descriptive; branch on status and exit code.

Legacy sequence commands are read-only, ignore dated records, and reserve nothing.
Legacy numbered filenames use `NNNN-lowercase-slug.md`; `README.md` is ignored.
Change scans ignore legacy filenames unless they begin with a digit. Matching legacy
spec/plan basenames share a number; conflicting slugs are rejected.

Header stamping requires exactly one `Created:` and `Updated:` field, each containing
a valid date or `<YYYY-MM-DD>`. Existing Created dates never change.
