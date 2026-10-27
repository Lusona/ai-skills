# Contributing to Lusona

Contributions to the skills, documentation, tooling, and host integrations are welcome.
Start with the [README](README.md) for the workflow and
[installation guide](INSTALL.md) for local setup.

## Bugs and feature requests

Search [existing issues](https://github.com/lusona/ai-skills/issues) before opening one.
Use the bug report form for defects and the feature request form for proposed changes.
For a larger change, open an issue to discuss the outcome and scope before implementing it.
You can send small documentation fixes as a pull request without an issue.

For bugs, include the host and plugin versions, installation source, reproduction steps,
expected behavior, and actual behavior. For agent behavior, include the prompt and a
short transcript when possible. Remove credentials, private code, and personal data
from examples and logs.

For features, explain the problem, who encounters it, and what a successful result
would look like. Include alternatives or workarounds you have considered.

## Make a change

Fork the repository, clone your fork, and create a branch for one bounded change.
Read `AGENTS.md` before editing; it also applies when you use an agent to contribute.

By submitting a contribution, you agree to license it under this project's
[MIT License](LICENSE). Only contribute material you have the right to submit, and
retain any required third-party notices.

- Edit canonical workflow sources under `plugins/lusona/`.
- Keep skills focused, preserve explicit TDD and authorization boundaries, and give
  the agent a concrete next action.
- Resolve bundled resources relative to the loaded skill. A `docs/lusona/` path in
  workflow instructions refers to the consuming project.
- Keep consuming-project records and generated packages out of your contribution.
  Use repository-local `tmp/` for scratch files and package output.
- Keep the Spanish, German, Simplified Chinese, and Japanese READMEs in sync with
  `README.md` when changing public documentation. Use natural technical prose in
  each language; preserve command names, paths, and authorization rules. Check
  translated section links and keep the language links in each README.
- Keep the native manifests' plugin names and versions aligned. Coordinate release
  version changes with maintainers rather than bumping versions for each pull request.

## Verify your change

Use `mise` for tools when available. The package builder requires Python 3; native
plugin validation requires Claude Code.

From the repository root:

```bash
git diff --check
claude plugin validate plugins/lusona
claude plugin validate .claude-plugin/marketplace.json
python3 scripts/package.py
```

The package builder checks manifest identity and versions, catalog paths, resource
links, and package contents. It writes to `tmp/lusona-package/` and refuses to
overwrite an existing output directory. For another build, use a fresh directory:

```bash
python3 scripts/package.py --output tmp/my-change-package
```

For changes to the work-record helper, run its behavioral checks:

```bash
bash scripts/test-work-record.sh
```

Run the PowerShell helper's behavioral checks in Windows PowerShell 5.1 or PowerShell 7:

```powershell
powershell.exe -NoProfile -File scripts/test-work-record.ps1
```

Use `pwsh` instead of `powershell.exe` for PowerShell 7. Both helpers share templates
and must preserve the command and file-safety contract. Test native Windows separately
from PowerShell on macOS/Linux; passing on one platform does not establish the others.

For script behavior changes, add or update tests that exercise the affected behavior.
Choose and state a TDD policy (`none`, `targeted`, or `strict`); verification remains
required with `none`. Documentation changes need relevant content and link checks.

For skill behavior changes, try a representative request using the local plugin.
Report the host, request, expected outcome, and observed result. Do not claim a host
integration works based only on packaging checks. If a tool or host is unavailable,
state which checks you could not run.

## Open a pull request

Explain the problem, resulting behavior, scope, and verification evidence. Link the
related issue when there is one, and call out installation or interactive behavior
you have not tested. Keep unrelated edits in separate pull requests.

Use Conventional Commits for commit messages, with a body explaining why the change
is needed, for example `docs: clarify Xcode installation`. If you use an agent,
authorize commits explicitly; the repository instructions prohibit unrequested commits,
pushes, and publication.

The `@lusona/core` team owns review across the repository. Maintainers may request
changes to scope, behavior, or verification before merging.
