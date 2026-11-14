# Install Lusona Skills

Choose your host: [Antigravity](#antigravity), [Claude Code](#claude-code),
[Codex](#codex), [Cursor](#cursor), or [Xcode](#xcode).

Install the full **Lusona Skills** plugin (`lusona`). Individual skill directories
lack the shared references, templates, and scripts they need.

## Requirements

- A supported host with plugin support. Xcode requires version 27 and an enabled
  coding agent under **Settings > Intelligence**.
- Git for Claude Code and Codex installation; GitHub access for downloads and updates.
- Bash on Unix or WSL, or Windows PowerShell 5.1 / PowerShell 7 on Windows, for
  creating project records. See [helper requirements](plugins/lusona/references/naming.md#running-the-helper).

Lusona needs no credentials of its own. Complete your host's setup and authentication
before using its agent. Python 3 is needed only to build packages or run repository
checks.

For marketplace installation over SSH, replace the HTTPS repository URL with
`git@github.com:lusona/ai-skills.git`. This requires configured GitHub SSH access.

## Antigravity

### Install from GitHub

```bash
agy plugin install https://github.com/lusona/ai-skills.git
agy plugin list --json
```

This installs globally. Check that `lusona` is enabled. The root URL also copies
repository files, including Lusona's development records. To exclude those records, use a
[local or portable plugin](#local-checkout-or-portable-package).

### Antigravity CLI

Start a new session in your project. Open `/plugin` to inspect the installation,
then run `/status` to explain the workflow or assess current work. Antigravity uses
skill names such as `/status`, without the `/lusona:` prefix.

### Antigravity App

After the CLI install, open **Customizations > Installed**, check that Lusona is
enabled, and inspect its **Skills** tab. Start a new project conversation and run
`/status`.

### Standalone Antigravity IDE

After the CLI install, open **Customizations** in the agent side panel and check
that Lusona's skills appear. Start a new project conversation and ask the agent to
use Lusona's `status` skill.

For manual App or IDE installation, copy the complete `plugins/lusona/` directory,
including hidden files, to one of these locations:

| Scope | Destination |
| --- | --- |
| Current project | `<project-root>/.agents/plugins/lusona/` |
| All projects | `~/.gemini/config/plugins/lusona/` |

If the destination already exists, follow [Updates](#updates). Restart the host
and check its loaded skills.

App/IDE installation, interactive behavior, and agent-driven skill invocation and
shared-resource loading have not been tested. See Google's
[plugin guide](https://antigravity.google/docs/plugins/) and
[skill guide](https://antigravity.google/docs/skills).

### Local checkout or portable package

From a [local checkout](#install-from-a-local-checkout), run:

```bash
agy plugin validate --strict "$PWD/plugins/lusona"
agy plugin install "$PWD/plugins/lusona"
agy plugin list --json
```

For a [portable package](#portable-package), use the absolute path to the extracted
`lusona-ai-skills/plugins/lusona/` directory instead. Keep the installed source
directory available.

## Claude Code

```bash
claude plugin marketplace add https://github.com/lusona/ai-skills.git
claude plugin install lusona@lusona-ai-skills --scope user
```

This installs Lusona for all your projects. Start a new session in your project
and run `/lusona:status`.

See the [Claude Code plugin guide](https://code.claude.com/docs/en/discover-plugins)
for other installation scopes.

## Codex

```bash
codex plugin marketplace add https://github.com/lusona/ai-skills.git
codex plugin add lusona@lusona-ai-skills
```

Start a new session in your project and invoke `$lusona:status`, or select Lusona's
`status` skill in the skill UI. The desktop app also accepts `/lusona:status`.

See the [OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins)
for marketplace options.

## Cursor

1. Open **Customize > From GitHub Repository**.
2. Enter `https://github.com/lusona/ai-skills`.
3. Select **Lusona Skills**, click **Install**, and choose project or user scope.
4. Start a new Agent chat. Type `/` and select Lusona's `status` skill.

These steps follow [Cursor's plugin documentation](https://cursor.com/docs/plugins).
Installation and skill invocation have not been tested in Cursor.

## Xcode

1. In Xcode 27, open **Settings > Intelligence** and enable a coding agent.
2. Under **Agents > Plug-ins**, click **Add Plug-in**.
3. Choose **Add from URL**, click **Continue**, and enter
   `https://github.com/lusona/ai-skills`.
4. Select Lusona's skills and click **Install**.
5. Start a new agent conversation. Type `/` and select Lusona's `status` skill.

For a local import, choose the file import option and select the complete
`plugins/lusona/` directory from your checkout. Xcode manages its own installation;
a standalone CLI install does not install the plugin in Xcode.

These steps follow [Apple's plug-in guide](https://developer.apple.com/documentation/xcode/extending-and-customizing-agents).
Installation and skill invocation have not been tested in Xcode.

## First use

Run `status` to explain the workflow or assess your project. In a new project,
optionally run `setup`: `/lusona:setup` in Claude Code, `$lusona:setup` in Codex,
or `setup` in your host's skill UI.

Setup creates `docs/lusona/` and the work queue. It asks you to approve the exact
text before adding Lusona instructions to `AGENTS.md` or an import to `CLAUDE.md`.
Setup is optional; each skill creates the records it needs.

Select `explore` to discuss an idea, or `implement` for a defined change. For example:

> Add invitation expiry after seven days. Preserve accepted invitations.
> Done means expired invitations are rejected and the test suite passes.
> Use targeted TDD for the expiry boundary. Verify locally; do not deploy.

See the [skill reference](plugins/lusona/references/workflow-guide.md#skills) for
all skills. Project records are saved under your project's `docs/lusona/` during
work; installation alone does not create them.

## Install from a local checkout

```bash
git clone https://github.com/lusona/ai-skills.git
cd ai-skills
```

Run the commands for your host from the repository root.

**Claude Code:**

```bash
claude plugin marketplace add "$PWD"
claude plugin install lusona@lusona-ai-skills --scope user
```

**Codex:**

```bash
codex plugin marketplace add "$PWD"
codex plugin add lusona@lusona-ai-skills
```

For Antigravity, use the [local plugin commands](#local-checkout-or-portable-package).
For Xcode, use the [file import option](#xcode). Keep the checkout available for updates.

Use one marketplace source: GitHub or a local directory. Before switching, inspect
`claude plugin marketplace list` or `codex plugin marketplace list`.

To try Lusona for one Claude Code session without registering a marketplace:

```bash
claude --plugin-dir "$PWD/plugins/lusona"
```

## Portable package

From the repository root:

```bash
python3 scripts/package.py
```

The output is `tmp/lusona-package/lusona-ai-skills/`, with a versioned ZIP beside
it. The builder requires a new output directory; for another build, pass
`--output tmp/another-package`.

Extract the ZIP to a location you will keep, then install:

- **Claude Code or Codex:** run the [local checkout commands](#install-from-a-local-checkout)
  from the extracted `lusona-ai-skills/` directory, skipping the clone step.
- **Antigravity:** install the extracted `lusona-ai-skills/plugins/lusona/` directory.
- **Cursor:** use the [GitHub installation](#cursor).

Packages include the full plugin and shared resources, and exclude repository
project records.

## Updates

**Claude Code:**

```bash
claude plugin marketplace update lusona-ai-skills
claude plugin update lusona@lusona-ai-skills --scope user
```

**Codex:**

```bash
codex plugin marketplace upgrade lusona-ai-skills
codex plugin add lusona@lusona-ai-skills
```

**Antigravity:** reinstall from the same URL:

```bash
agy plugin install https://github.com/lusona/ai-skills.git
agy plugin list --json
```

For local installs, update the checkout or extract a new package, then rerun your
host's install command. For manually copied App/IDE plugins, close the host, save
any local changes, and replace only the `lusona/` directory. Do not merge old and
new files.

Manage **Cursor** updates in **Customize** and **Xcode** updates in
**Settings > Intelligence > Agents > Plug-ins**.

Start a new session after updating. Keep your project's `docs/lusona/` records in place.

## Removal

**Claude Code:**

```bash
claude plugin uninstall lusona@lusona-ai-skills --scope user
```

**Codex:**

```bash
codex plugin remove lusona@lusona-ai-skills
```

**Antigravity CLI:**

```bash
agy plugin uninstall lusona
agy plugin list --json
```

In **Antigravity App**, uninstall Lusona from **Customizations > Installed**.
For a manual App/IDE install, remove only the `lusona/` directory you copied.
A global installation may be shared by the App and IDE; reopen both to check removal.

Manage **Cursor** plugins in **Customize** and **Xcode** plugins in
**Settings > Intelligence > Agents > Plug-ins**.

Removal leaves your project documents in place. Keep `docs/lusona/` and unrelated
plugins and host configuration.

## Vercel skills installer

The Vercel Skills installer is unsupported: it copies individual skills without
their shared resources. Use your host's plugin installation above.

## Document compatibility

Keep existing project records in place. Lusona can read older split specs and plans,
combined specs, `docs/lusona/features/`, and `docs/agent/` records. No migration or
renaming is required. See [project files](plugins/lusona/references/files.md) for
legacy formats and [document naming](plugins/lusona/references/naming.md) for new records.
