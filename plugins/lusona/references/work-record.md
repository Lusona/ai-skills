# Work-record helpers

Use [Bash](../scripts/work-record.sh) in a Bash environment, or
[PowerShell](../scripts/work-record.ps1) in a native Windows PowerShell environment.
Choose from the agent's available shell, not just the operating system: a Windows WSL
session uses Bash. Resolve the helper from the loaded plugin, never from the consuming
project's current directory. From a skill, the paths are `../../scripts/work-record.sh`
and `../../scripts/work-record.ps1`.

Both helpers use the same commands, arguments, statuses, and exit codes. Run `help` for
the command list. Pass absolute project paths in the executing shell's filesystem;
PowerShell returns native absolute paths. History paths are project-relative and use `/`.
PowerShell emits UTF-8 output, including JSON paths; subprocess callers should decode it as UTF-8.
Do not pass a Windows drive path to a WSL helper or reinterpret returned paths in another shell.

```bash
bash /resolved/plugin/scripts/work-record.sh help
```

```powershell
powershell.exe -NoProfile -File "C:\resolved\plugin\scripts\work-record.ps1" help
```

The PowerShell helper targets Windows PowerShell 5.1 and PowerShell 7; use `pwsh`
in place of `powershell.exe` for PowerShell 7. Follow the host's script execution policy;
do not change policy automatically when execution is blocked. Report the blocked command
and required environment instead. The helpers use bundled templates and do not require Python.

For record identity and creation responses, apply [naming](naming.md); for notes and
history, apply [retention](retention.md) and [closeout](closeout.md). After initialization,
fill the relevant template sections within the existing work authorization.
