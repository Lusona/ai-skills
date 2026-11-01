# Install Lusona Skills

Lusona provides thirteen product and engineering workflow skills for Claude Code,
Codex, Cursor, Xcode's coding agents, and Google Antigravity App, CLI, and standalone IDE.
Claude Code and Codex use the `lusona` plugin from the `lusona-ai-skills` marketplace in the
public [lusona/ai-skills repository](https://github.com/lusona/ai-skills).
Antigravity installs the full `plugins/lusona/` directory from GitHub, a local checkout,
or a portable package.

The display name is **Lusona Skills**. The plugin identifier and Claude Code
command namespace remain `lusona`, for example `/lusona:status`.

## Requirements

- For Claude Code/Codex installation: Git and the selected host with plugin support.
- For Cursor installation: a current Cursor release with plugin support.
- For Xcode installation: Xcode 27 with a coding agent enabled in Intelligence settings.
- For Antigravity: the App, CLI (`agy`), or standalone IDE with native plugin support.
  The CLI requires its own host setup/authentication for agent sessions.
- Network access to GitHub for installation and updates from the repository.

Creating workflow records uses the bundled Bash or PowerShell helper. Use Bash in a
Unix or WSL shell, or Windows PowerShell 5.1 / PowerShell 7 in a native Windows shell;
see [helper invocation](plugins/lusona/references/work-record.md). Python is required only for
building packages and running the repository's Python evaluations, not for plugin use.

Lusona requires no API keys, tokens, or other credentials. Its bundled helpers create
project records locally; they do not download or execute remote scripts.

The marketplace commands below use HTTPS to download the public repository. If you prefer SSH
and have GitHub SSH access configured, substitute
`git@github.com:lusona/ai-skills.git` for the HTTPS URL.

## Antigravity

Use the full native plugin directory for **Antigravity App, CLI, or standalone IDE**.
Lusona's manifest is `plugins/lusona/.antigravity-plugin/plugin.json`; `skills/`,
`README.md`, `references/`, `templates/`, `scripts/`, and `assets/` stay at the plugin root.
Copying individual skills loses the shared resources they require. Resource paths in a
loaded skill resolve relative to that skill, not your project's working directory.

### Install from GitHub

Install the plugin directly; no local checkout is required:

```bash
agy plugin install https://github.com/lusona/ai-skills.git
agy plugin list --json
```

The repository URL installs through the root Antigravity manifest, including the
repository files. The verified 1.4.0 root installation also includes project records.
The root `.antigravity-plugin/plugin.json` points skill discovery to
`plugins/lusona/skills/`; the manifest inside `plugins/lusona/` makes that directory
independently installable for local or portable-package installation.
Antigravity's documented marketplace commands support its official marketplace;
this repository does not add a custom Antigravity marketplace catalog.

### Local checkout or portable package

Alternatively, clone the repository using [local checkout setup](#install-from-a-local-checkout).
From its root, validate and install the complete plugin:

```bash
agy plugin validate --strict "$PWD/plugins/lusona"
agy plugin install "$PWD/plugins/lusona"
agy plugin list --json
```

For a portable package, extract the ZIP into a durable location and pass the absolute
path to its `lusona-ai-skills/plugins/lusona/` directory instead. Packages exclude
repository project records.

### Antigravity CLI

After installation, check that `lusona` is enabled and that the listed skills match the canonical
`plugins/lusona/skills/` directories (currently thirteen). Start a new project session;
open `/plugin` to inspect the installation and type `/` to discover skill commands.
Invoke `/status` to request a workflow explanation. For a defined change, invoke
`/implement` and supply the outcome, acceptance criteria, TDD policy, and authority.
These commands use skill names, without the Claude Code `/lusona:` prefix.

### Antigravity App

Use the CLI GitHub installation above for a global install, then inspect
**Customizations > Installed** in the App. Google's documentation describes App/CLI
plugin synchronization; verify Lusona is enabled and inspect its **Skills** tab.
Alternatively, place the complete plugin folder at either of these paths:

- Project scope: `<project-root>/.agents/plugins/lusona/`.
- Global scope: `~/.gemini/config/plugins/lusona/`.

Use a file manager to copy `plugins/lusona/`, including hidden manifest directories,
to an unused destination. If Lusona is already present, follow [updates](#updates)
instead of merging copies. Start a new conversation in the project, type `/` to find
`status`, and invoke `/status`. You can also explicitly ask to use Lusona's `status` skill.

### Standalone Antigravity IDE

The CLI GitHub installation above uses the global plugin location. Inspect the IDE's
active components to confirm it has loaded Lusona. Alternatively, copy the complete plugin
directory to `<project-root>/.agents/plugins/lusona/` for project scope, or
`~/.gemini/config/plugins/lusona/` for all IDE windows, using the full-directory copy
instructions above.

Open the agent side panel's **Customizations** dropdown and inspect the loaded Lusona
skills. Start a new project conversation and ask the agent to use Lusona's `status`
skill to explain the workflow. For implementation, name Lusona's `implement` skill and
state the outcome, acceptance criteria, TDD policy, and authority.

### Verification status and sources

Documentation checked **2026-10-31** against Google's [Plugins guide](https://antigravity.google/docs/plugins/),
[Build plugins guide](https://antigravity.google/docs/build-plugins/), and
[Agent skills guide](https://antigravity.google/docs/skills).
Checked with **Antigravity CLI 1.4.12 on Linux** after publication: the explicit GitHub subdirectory
URL installed and enabled native **Lusona 1.4.0**, discovering all thirteen skills.
Shared README, references, templates, scripts and assets were present; strict validation
reported no findings. The installed plugin contained no project records.

The repository-root `.git` URL also installed 1.4.0, but copied repository project records
because it selected the new root manifest. The primary command above uses the repository-root URL as requested. Local and portable
installation of `plugins/lusona/` excludes those repository records.
Earlier isolated GitHub checks used published 1.3.2 through Claude compatibility; those
historical observations do not describe the current root-manifest installation behavior.

For the native **1.4.0** source and portable plugin in this checkout, strict validation
passed, discovering all thirteen skills. Earlier native lifecycle checks used version
**1.3.2** and a synthetic **1.3.3** update in a network-isolated environment with disposable
configuration: install, enabled-plugin/skill listing, reinstallation, and removal passed. The bundled Bash
helper created a spec in the consuming test project; project records and unrelated
configuration were preserved during update/removal. The real user configuration was untouched.
The repository-root manifest also discovers all thirteen skills. Root validation passes
with a warning that the repository's `AGENTS.md` is not a plugin rule; strict validation
therefore fails at the checkout root. The packaged root passes strict validation because
repository instructions and project records are excluded from the package.
Model-driven `status`/`specify` invocation and shared-resource loading by an agent have
not been tested. App and standalone IDE installation and interactive behavior have not
been tested. Static/package validation and CLI lifecycle checks do not establish those
interactive behaviors.

## Claude Code

Run these commands in your terminal:

```bash
claude plugin marketplace add https://github.com/lusona/ai-skills.git
claude plugin install lusona@lusona-ai-skills --scope user
```

The user scope makes Lusona available across your projects. Start a new Claude Code
session in your project, then run `/lusona:status` for a workflow explanation or
an assessment of current work.

For host-specific options, see the [Claude Code plugin guide](https://code.claude.com/docs/en/discover-plugins).

## Codex

Run these commands in your terminal:

```bash
codex plugin marketplace add https://github.com/lusona/ai-skills.git
codex plugin add lusona@lusona-ai-skills
```

Start a new Codex session in your project and select Lusona's `status` skill from
the skill UI. Ask it to explain the workflow or assess your project's current work.

For marketplace configuration options, see the [OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins).

## Cursor

1. Open **Customize** in Cursor's sidebar and choose **From GitHub Repository**.
2. Enter `https://github.com/lusona/ai-skills` to import the marketplace.
3. Find **Lusona Skills**, select **Install**, and choose project or user scope.
4. Start a new Agent chat in your project. Type `/`, search for Lusona's `status`
   skill, and select it to explain the workflow or assess current work.

Install the whole plugin so its shared references, templates, and scripts stay
available. The repository's `.cursor-plugin/marketplace.json` points to
`plugins/lusona/`; that directory contains Cursor's plugin manifest and the skills.
GitHub imports require these files to be committed and pushed first.

See Cursor's [repository installation instructions](https://cursor.com/docs/skills#installing-skills-from-a-repository),
[plugin guide](https://cursor.com/docs/plugins), and
[plugin manifest reference](https://cursor.com/docs/reference/plugins).
Checked against Cursor's documentation on October 26, 2026; installation and skill
invocation in Cursor have not been tested as part of this update.

## Xcode

In Xcode 27:

1. Open **Xcode > Settings > Intelligence** and enable a coding agent if needed.
2. Under **Agents**, click **Plug-ins**, then **Add Plug-in**.
3. Choose **Add from URL**, click **Continue**, and enter
   `https://github.com/lusona/ai-skills`.
4. Continue to component selection, select Lusona's skills, and click **Install**.
5. Open a new agent conversation in your project. Type `/` to find the installed
   skills, then select Lusona's `status` skill.

For a local import, clone this repository and use the file import option to select
`plugins/lusona/`. Keep the full plugin directory, including references and templates.

Xcode uses its own agent configuration directories; installing through a standalone
CLI does not establish an Xcode installation. Agent support began in Xcode 26.3;
these plug-in UI instructions target Xcode 27.

See Apple's [agent setup](https://developer.apple.com/documentation/xcode/setting-up-coding-intelligence),
[plug-in installation guide](https://developer.apple.com/documentation/xcode/extending-and-customizing-agents),
and [Xcode 27 release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes?changes=latest_minor).
These steps follow Apple's documentation; Lusona installation and invocation in Xcode
have not been tested as part of this documentation update.

## First use

Installation registers the skills. You choose what work to authorize in your project.
For example, select `explore` and ask:

> Help me compare invitation links and email-only invitations. Explain the tradeoffs.
> Keep this discussion in chat; do not save files.

For a defined change, select `implement` and describe the outcome, acceptance criteria,
TDD policy, and limits:

> Add invitation expiry after seven days. Preserve accepted invitations.
> Done means: expired invitations are rejected and the test suite passes.
> Use targeted TDD for the expiry boundary. Verify locally; do not deploy.

You can start with any skill that fits your request. See the
[command reference](plugins/lusona/references/workflow-guide.md#skills) for all thirteen skills and the
[batch examples](plugins/lusona/references/batch-use.md) for authorized unattended work.

During authorized work, the agent saves project records under that project's
`docs/lusona/` when needed. Installation does not create or migrate project documents.
Keep project records in your project; installed templates and references remain plugin
resources. You can put project-specific preferences in `docs/lusona/README.md` or your
agent instructions. No startup hooks are required.

## Install from a local checkout

Use a checkout to inspect or modify the plugin before installing it:

```bash
git clone https://github.com/lusona/ai-skills.git
cd ai-skills
```

From the repository root, run the pair for Claude Code or Codex below. For Antigravity,
use the [local-directory steps](#local-checkout-or-portable-package):

```bash
claude plugin marketplace add "$PWD"
claude plugin install lusona@lusona-ai-skills --scope user
```

```bash
codex plugin marketplace add "$PWD"
codex plugin add lusona@lusona-ai-skills
```

Keep the checkout available for updates. Choose one source for the
`lusona-ai-skills` marketplace: GitHub or a local directory. If you registered it
before, inspect `claude plugin marketplace list` or `codex plugin marketplace list`
before changing its source.

To try the plugin for one Claude Code session from the repository root:

```bash
claude --plugin-dir "$PWD/plugins/lusona"
```

## Portable package

To build a package, run this from the repository root with Python 3:

```bash
python3 scripts/package.py
```

Find the catalog in `tmp/lusona-package/lusona-ai-skills/` and the versioned ZIP
beside it. Extract the ZIP into a durable location, then register the extracted
`lusona-ai-skills` directory using the local installation commands above. The package
includes the native manifests for Claude Code/Codex, Cursor, and Antigravity, plus skills
and bundled resources; it excludes project records.
The local CLI commands above apply to Claude Code and Codex; use the GitHub import
steps for Cursor. For Antigravity App, CLI, and standalone IDE, use the extracted
`lusona-ai-skills/plugins/lusona/` directory with the [Antigravity steps](#antigravity).

## Vercel skills installer

The Vercel Skills installer is not supported. It installs individual skill
directories without the shared resources Lusona requires. Use the native plugin
installation for [Claude Code](#claude-code), [Codex](#codex), [Cursor](#cursor), [Xcode](#xcode), or [Antigravity](#antigravity).

## Updates

For a Claude Code or Codex GitHub installation, refresh the marketplace and update the plugin:

```bash
claude plugin marketplace update lusona-ai-skills
claude plugin update lusona@lusona-ai-skills --scope user
```

```bash
codex plugin marketplace upgrade lusona-ai-skills
codex plugin add lusona@lusona-ai-skills
```

For a local installation, update your checkout or extracted package first, then
rerun your host's plugin install command. Start a new session after updating.
Plugin updates leave your project's documents in place.

For an Antigravity GitHub installation, reinstall from the same plugin URL:

```bash
agy plugin install https://github.com/lusona/ai-skills.git
agy plugin list --json
```

For a local install, update the source checkout or extract a new package into a separate
directory, then reinstall that complete plugin with `agy plugin install` and inspect
`agy plugin list --json`. CLI 1.4.12 has no `agy plugin update` command.
For manually copied App/IDE plugins, close affected sessions, preserve any local plugin
changes, move only the existing `lusona/` plugin directory aside, and copy the new complete
directory into its place. Do not merge old and new skill files. Reopen the App/IDE and
inspect active skills; check each surface you use. Keep project `docs/lusona/` records and
unrelated plugins/configuration in place.

Manage Xcode's installation separately under **Settings > Intelligence > Agents > Plug-ins**.
Manage Cursor's installed plugin and available updates from **Customize**.

## Removal

For a Claude Code or Codex installation, run the command for your host:

```bash
claude plugin uninstall lusona@lusona-ai-skills --scope user
```

```bash
codex plugin remove lusona@lusona-ai-skills
```

For a native Antigravity CLI installation:

```bash
agy plugin uninstall lusona
agy plugin list --json
```

In the App, inspect **Customizations > Installed** and use Lusona's menu to uninstall.
For a manually copied App/IDE installation, remove only the `lusona/` directory you
placed under the project's `.agents/plugins/` or `~/.gemini/config/plugins/`.
Do not remove the containing plugin/configuration directory. Shared global locations
can affect more than one surface; reopen each surface to confirm removal.

Your project documents remain after removal. Preserve `docs/lusona/` and unrelated host
configuration/plugins.
For Cursor, manage or uninstall Lusona from **Customize**.

## Document compatibility

If you used an earlier Lusona version, keep existing project records in place.
The agent can use split specs and plans, combined specs, `docs/lusona/features/`,
and `docs/agent/` records. Read an existing Feature map as the capability map;
there is no need to rename it or create a duplicate.

New saved changes use one `docs/lusona/specs/<change-id>.md` record for the agreement,
any useful execution detail, evidence, and current handoff. Consequential architecture
decisions stay in linked ADRs. See [document names and headers](plugins/lusona/references/naming.md)
for the current format and [project files](plugins/lusona/references/files.md) for legacy records.
Request migration as a separate change if you want it.
