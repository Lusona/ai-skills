# Install Lusona

Lusona provides eleven product and engineering workflow skills for Claude Code,
Codex, and Xcode's coding agents. For CLI installation, use the `lusona` plugin from the `lusona-ai-skills` marketplace in the
public [lusona/ai-skills repository](https://github.com/lusona/ai-skills).

## Requirements

- For CLI installation: Git and either Claude Code or Codex with plugin support.
- For Xcode installation: Xcode 27 with a coding agent enabled in Intelligence settings.
- Network access to GitHub for installation and updates from the repository.

The commands below use HTTPS, so you do not need GitHub credentials to download the
public repository. If you prefer SSH and have GitHub SSH access configured, substitute
`git@github.com:lusona/ai-skills.git` for the HTTPS URL.

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
[command reference](references/workflow-guide.md#skills) for all eleven skills and the
[batch examples](references/batch-use.md) for authorized unattended work.

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

From the repository root, run the pair for your host:

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
includes both hosts' manifests, skills, and bundled resources; it excludes project records.

## Updates

For a CLI GitHub installation, refresh the marketplace and update the plugin:

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

Manage Xcode's installation separately under **Settings > Intelligence > Agents > Plug-ins**.

## Removal

For a CLI installation, run the command for your host:

```bash
claude plugin uninstall lusona@lusona-ai-skills --scope user
```

```bash
codex plugin remove lusona@lusona-ai-skills
```

Your project documents remain after removal.

## Document compatibility

If you used an earlier Lusona version, keep existing project records in place.
The agent can use split specs and plans, combined specs, `docs/lusona/features/`,
and `docs/agent/` records. Read an existing Feature map as the capability map;
there is no need to rename it or create a duplicate.

New saved changes use one `docs/lusona/specs/<change-id>.md` record for the agreement,
any useful execution detail, evidence, and current handoff. Consequential architecture
decisions stay in linked ADRs. See [document names and headers](references/naming.md)
for the current format and [project files](references/files.md) for legacy records.
Request migration as a separate change if you want it.
