# Lusona Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Lusona gives coding agents a shared workflow for deciding what to build, making bounded
changes, and verifying the result. It keeps your decisions and constraints available across
sessions, makes missing decisions explicit, and requires evidence for claims of completion.

Its [workflow principles](docs/workflow.md#principles) keep you in control of scope and
consequential decisions while the agent carries authorized work through to a checked result.

Start with an idea, an existing project, or a specific problem.

> [!TIP]
> Already installed? Start with `/status` using the [command for your application](#2-get-a-recommendation).

## 1. Install for your application

Use only the instructions for your application. Complete its setup and authentication first.

**Claude Code** — run in a terminal:

```bash
claude plugin marketplace add https://github.com/lusona/ai-skills.git
claude plugin install lusona@lusona-ai-skills --scope user
```

**Codex** — run in a terminal:

```bash
codex plugin marketplace add https://github.com/lusona/ai-skills.git
codex plugin add lusona@lusona-ai-skills
```

**Antigravity** — run in a terminal:

```bash
agy plugin install https://github.com/lusona/ai-skills.git
agy plugin list --json
```

Check that `lusona` is enabled. In the App, check **Customizations > Installed**;
in the standalone IDE, check **Customizations** in the agent side panel.

**Cursor** — open **Customize > From GitHub Repository**, enter
`https://github.com/lusona/ai-skills`, select **Lusona Skills**, click **Install**,
and choose project or user scope.

**Xcode 27** — enable a coding agent in **Settings > Intelligence**. Under
**Agents > Plug-ins**, click **Add Plug-in > Add from URL > Continue**, enter
`https://github.com/lusona/ai-skills`, select Lusona's skills, and click **Install**.
A standalone CLI install does not install the plugin in Xcode.

> [!WARNING]
> Install the native plugin, not Vercel Skills (`npx skills@latest`); individual skills lack shared resources.

## 2. Get a recommendation

Start a new agent session in your project. Use **status** to assess an existing project;
use **explore** to discuss an idea for an empty project.

| Application | Invoke status |
| --- | --- |
| Claude Code | `/lusona:status` |
| Codex CLI | `$lusona:status` |
| Codex desktop app | `$lusona:status` or `/lusona:status`, or select `status` in the skill UI |
| Antigravity App and CLI | `/status` |
| Antigravity standalone IDE | Ask: `Use Lusona's status skill.` |
| Cursor or Xcode | Type `/` and select Lusona's `status` skill |

The examples below use Claude Code syntax. For other applications, use the invocation
method in the table; for **explore**, replace `status` with `explore`.

For an existing project:

```text
/lusona:status
Inspect this project and recommend one small next change based on its goals and current state.
Tell me what already exists and what is missing. Do not change files yet.
```

Expect an assessment of the current project and a recommended next action. If the agent needs
a decision, answer in plain language about your project and the behavior you want.

For an empty project, replace the bracketed text with your own idea before sending:

```text
/lusona:explore
I want to build [describe your project and who it is for]. Help me choose the first small change.
Do not change files yet.
```

## 3. Start the work

Once the recommendation matches what you want, reply:

```text
/lusona:implement
Implement that recommendation. Keep the scope limited to the agreed change.
Verify it locally. Do not commit or deploy.
```

The agent may ask you to settle missing behavior or choose a testing approach before implementing.
At the end, look for what changed, which checks ran and their results, and any remaining limits
or decisions. If a check could not run, the report should say so.

## Everyday use

These groups are choices, not required stages; start with **status** if you are unsure.

The `/name` commands below use the Antigravity App/CLI short form. In Claude Code use `/lusona:<name>`; in Codex CLI use `$lusona:<name>`. In other apps, use the same invocation method as in the status table above.

### Start or resume

| Command | Use it to |
| --- | --- |
| `/status` | Assess progress, remaining work, and the next action. |
| `/setup` | Optionally prepare project records and standing preferences. |

### Explore and plan

| Command | Use it to |
| --- | --- |
| `/explore` | Compare ideas or directions before choosing. |
| `/frame-product` | Define a product’s audience, problem, vision, and boundaries. |
| `/map-capabilities` | Map capabilities, dependencies, and delivery order. |

### Define a change

| Command | Use it to |
| --- | --- |
| `/specify` | Define one change’s behavior, scope, and acceptance criteria. |
| `/architect` | Resolve a lasting technical decision about boundaries, contracts, or ownership. |
| `/design` | Create UI mockups, flows, or diagrams to compare. |

### Build and check

| Command | Use it to |
| --- | --- |
| `/implement` | Implement an authorized bounded change, or request only a plan. |
| `/refactor` | Improve code structure while preserving behavior. |
| `/review` | Review a diff and report findings without editing the implementation. |
| `/batch` | Run explicitly authorized unattended work on a fixed selection of queue items. |

### Investigate and compare

| Command | Use it to |
| --- | --- |
| `/investigate` | Establish the cause, observed behavior, or feasibility with evidence. |
| `/measure` | Establish a baseline, benchmark, or comparable measurements. |
| `/experiment` | Test an intervention or compare alternatives in a bounded trial. |

Add constraints naturally, such as “keep the public API unchanged” or “do not commit yet.”

## More when you need it

- [Installation details](INSTALL.md): updates, removal, local packages, requirements, and host caveats.
  Antigravity App/IDE installation and interactive behavior, and Cursor/Xcode installation and
  invocation, have not been tested.
- [Usage guide](docs/usage.md): more examples, optional setup, and other skills.
- [Workflow details](docs/workflow.md): testing, evidence, and resuming work.
- [Why we built Lusona](https://blog.lusona.com/blog/why-we-built-lusona-skills/).

Checked-out source version: **3.1.0**. GitHub installation uses committed, pushed sources;
local changes do not establish a published release. See the [changelog](CHANGELOG.md).

[Contributing](CONTRIBUTING.md) · [Report an issue](https://github.com/lusona/ai-skills/issues/new/choose) · [Privacy](PRIVACY.md) · [Terms](TERMS.md) · [MIT License](LICENSE)
