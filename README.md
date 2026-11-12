# Lusona Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Lusona is a set of 14 skills for product and engineering work with coding agents. Each skill
covers one responsibility, such as specifying, implementing or reviewing a change. All skills
follow the same eight loop principles, keep records under the project's `docs/lusona/`, and end
every task reply with a status, the evidence and the next action.

For Claude Code, Codex, [Cursor](INSTALL.md#cursor), [Xcode 27 coding agents](INSTALL.md#xcode), and [Google Antigravity App, CLI, and IDE](INSTALL.md#antigravity) · Checked-out source version **3.0.0**

> [!WARNING]
> Do not install Lusona using Vercel Skills (`npx skills@latest`); use the [native plugin installation](#installation).

Read why we built Lusona Skills: [Why we built Lusona Skills](https://blog.lusona.com/blog/why-we-built-lusona-skills/).

This README describes the source in this checkout. GitHub installation uses committed,
pushed sources; local changes do not establish a published release.

![Lusona work loop, guiding principles and skill groups](plugins/lusona/assets/workflow-loop.svg)

The circle shows how work continues: choose, act, check and repeat. Select skills from the
current need; any skill can follow any other.

## Index

- [Loop principles](#loop-principles)
- [Start and choose a skill](#start-and-choose-a-skill)
- [Authority and TDD level](#authority-and-tdd-level)
- [Decisions and revisions](#decisions-and-revisions)
- [Evidence and completion](#evidence-and-completion)
- [Records and resumption](#records-and-resumption)
- [Replies and next actions](#replies-and-next-actions)
- [Installation](#installation)
- [Reference](#reference)
- [Contributing](#contributing)
- [License](#license)
- [Development](#development)

## Loop principles

The loop is the cycle every skill works in: choose the next bounded action, act, check the
result, and repeat until the requested outcome is complete. Its purpose is to refine the
system and design as understanding develops. Every skill applies these eight principles. The
[workflow guide](plugins/lusona/references/workflow-guide.md#loop-principles) defines them.

| ID | Principle | What it means for you |
| --- | --- | --- |
| P1 | Non-sequential | The agent selects the next skill from the unresolved need. Any skill can follow any other, and a change uses only the skills its unresolved work needs. |
| P2 | Refinement | Each pass compares its result with the intended outcome and separates facts from assumptions. It carries the outcome, accepted decisions, authority, TDD level, evidence and uncertainty into the next pass. |
| P3 | Prior decisions are inputs | When new input contradicts an accepted decision, the agent neither rejects the input nor ignores the decision. It states the conflict and revisits the decision with you. |
| P4 | Recorded invalidation | A superseded decision is marked with date and source, and its rationale is kept. Affected records are reconciled, and a stale record cannot reinstate a superseded choice. |
| P5 | Evidence over assertion | The agent claims behavior and completion only from observed checks. A failed or unrun required check blocks completion. |
| P6 | Authority stays with the user | Specs, plans, ADRs and queue states do not authorize implementation. Changes to accepted outcomes, contracts, TDD level or consequential commitments need your decision. |
| P7 | Continue bounded work | The agent takes the next authorized action without another command, stops inquiry that cannot change the next action, and pauses only the affected work. |
| P8 | Every reply names the next action | Each task reply ends with one next action and its owner, or states that none remains and why. |

## Start and choose a skill

Start with **status** when you join a project, resume work or decide what needs attention. It
assesses the records and evidence it can read, lists all known remaining work and recommends
the next action. It also works when the project has no Lusona records yet. A status request
neither grants nor removes execution authority.

Choose the skill that matches the current need (P1). The rows are not a sequence: an authorized
request that states its intended behavior and scope goes to **implement** without **specify**.

| Skill | Use when |
| --- | --- |
| [status](plugins/lusona/skills/status/SKILL.md) | You want orientation, progress, what is left, or how to resume |
| [explore](plugins/lusona/skills/explore/SKILL.md) | You want to reason about a direction, option or future before choosing it |
| [frame-product](plugins/lusona/skills/frame-product/SKILL.md) | A product's audience, problem, vision, outcomes or boundaries are undefined or changing |
| [map-capabilities](plugins/lusona/skills/map-capabilities/SKILL.md) | Capability coverage, dependencies or delivery order need clarification |
| [specify](plugins/lusona/skills/specify/SKILL.md) | A change's intended behavior, scope or acceptance criteria need definition |
| [architect](plugins/lusona/skills/architect/SKILL.md) | A technical decision about boundaries, contracts or ownership with lasting consequences is open |
| [design](plugins/lusona/skills/design/SKILL.md) | A screen, flow, state or relationship must be seen to be judged or chosen |
| [implement](plugins/lusona/skills/implement/SKILL.md) | A change is authorized for implementation, or you want only a plan |
| [review](plugins/lusona/skills/review/SKILL.md) | A diff needs review against intended behavior before completion |
| [refactor](plugins/lusona/skills/refactor/SKILL.md) | Existing code has a concrete structural problem and behavior must stay the same |
| [investigate](plugins/lusona/skills/investigate/SKILL.md) | A cause, observed behavior or feasibility question needs evidence |
| [measure](plugins/lusona/skills/measure/SKILL.md) | A decision needs a baseline, benchmark or comparable observations |
| [experiment](plugins/lusona/skills/experiment/SKILL.md) | A decision to adopt, reject or refine an approach needs a trial |
| [batch](plugins/lusona/skills/batch/SKILL.md) | You authorize unattended work on selected queue items, or continue a recorded batch |

The [workflow guide](plugins/lusona/references/workflow-guide.md) lists each skill's persona and
output, the routing table and the terminology. Moving from one skill to another needs no new
approval, and you do not need to direct each transition.

Invoke a skill in your host:

- Claude Code: `/lusona:<skill>`, for example `/lusona:status`.
- Codex: select the Lusona skill from the skill UI.
- Cursor: type `/` in Agent chat and select the skill.
- Xcode: type `/` in an agent conversation and select the installed skill.
- Antigravity App and CLI: `/<skill>`, for example `/status`. In the standalone IDE, inspect
  **Customizations** and name the Lusona skill in your request.

[Install Lusona](#installation) before using these skills. A skill prompt names the skill,
the outcome or input record, and the authorized scope. For example:

> **status:** Assess this project from the available records and working tree. Tell me what
> remains and recommend where to start.

> **explore:** Help me compare invitation links and email-only invitations. Explain the
> consequences for our support team before we choose. Keep this discussion in chat; do not save files.

> **design:** Compare two invitation flows using our existing screens, navigation, and copy.
> Show the steps and the expired-invitation state, and explain each option’s tradeoff.
> Keep this to visual design; do not implement the UI.

> **implement:** Add invitation expiry after seven days. Preserve existing accepted invitations.
> Done means: invitations older than seven days are rejected, accepted invitations are unchanged,
> and the test suite passes. Use TDD level `targeted` for the expiry boundary. Verify locally; do not deploy.

## Authority and TDD level

You hold authority (P6). These rules apply in every skill:

- Specs, plans, ADRs and queue states do not authorize implementation. Discussion and read-only
  review do not authorize it either.
- Selecting one task for implementation does not authorize the rest of its change.
- The agent asks you before destructive actions and before changes to accepted outcomes,
  contracts, TDD level or consequential commitments.
- The agent commits, pushes or publishes only with your authority. Authorized implementation
  and refactoring include local commits.
- A planning-only request to **implement** ends with a proposed approach and does not
  authorize implementation.
- **batch** runs unattended work only on a fixed selection of queue items that you authorize
  explicitly. It uses at most 4 concurrent assignments, or 5 when you select 5, limited by host
  capacity, and a repair budget of 2 corrective rounds per item unless you grant another number.

Implementation requires an explicitly selected TDD level. There is no default.

| TDD level | Requirement |
| --- | --- |
| `none` | No test-first requirement; agreed verification and repository checks still apply |
| `targeted` | Test first for named behaviors |
| `strict` | Test first for every new or changed testable behavior |

Select the level in your request or as a standing preference in the project's
`docs/lusona/README.md` or agent instructions (`CLAUDE.md` or `AGENTS.md`), for example
`TDD: targeted for validation and persistence boundaries`. Until a level is selected, the agent
only defines and plans, then asks you, recommending a level. The agent records the level and
its source, and asks you for a revised level when the selected sequence is infeasible.

Within that authority, the agent continues without another command (P7). It takes the next
bounded action, runs a measurement or experiment inside authorized work without a new request,
and stops asking when the answers cannot change the next action. It asks through the host's
native question tool when available, recommends an answer, and treats neither silence nor a
preselected option as consent. While it waits, only the affected work pauses, and the agent
states what resumes it.

The agent that talks with you is the coordinator. It delegates specialist work to leaves at
every task size and integrates and verifies their results; when delegation is prohibited or
unavailable, it works locally and says so. See [delegation](plugins/lusona/references/delegation.md)
for assignments and [model routing](plugins/lusona/references/delegation.md#model-routing).

## Decisions and revisions

Accepted decisions are inputs to later work (P3). When a new requirement, specification,
measurement or experiment result contradicts an accepted decision, the agent:

1. States the decision, its source, the conflict and the affected assumptions, in the reply and
   in the owning record.
2. Gives you the options and a recommended answer.
3. Reaches one outcome with you: kept, revised in part, or superseded. Revisiting a decision
   does not authorize the change.
4. Records the outcome before work that depends on the decision continues.
5. Continues work that the conflict does not affect, within existing authority.

The record keeps the history of each decision (P4). A revised or superseded decision keeps its
text and rationale, marked with the date and the source of your answer; a superseded decision
links to its replacement. The agent updates dependent records, assignments and handoffs within
its write ownership, reports corrections that other owners must make, and resumes under the
revision. A record that still states a superseded decision is corrected or reported, not
followed. See [revisions](plugins/lusona/references/revisions.md).

A follow-up request changes the scope of the current objective and keeps its progress. It
replaces the objective only when it cancels or replaces it explicitly, or asks for an
incompatible one.

## Evidence and completion

The agent reports behavior only from observed checks and names unrun and failed checks (P5).
Completion requires the authorized outcome, its criteria, passing required checks, and any
required human acceptance. Passing tests do not establish human acceptance.

- **Test-first evidence.** For each test-first behavior, the agent observes the intended failure
  before changing production code, then the passing result. A setup failure is not evidence
  of the intended failure. See [TDD](plugins/lusona/references/tdd.md).
- **Correction limits.** After 2 consecutive correction rounds without material progress, the
  agent stops correcting that failure, reports the evidence and continues unaffected work. After
  4 total rounds it asks you before any further round. Inside a batch, the repair budget applies
  instead. See [corrections](plugins/lusona/references/corrections.md).
- **Independent review.** Review by an agent that did not write the change is required when
  your or the repository's rules require it, or when the change affects security boundaries,
  persistent data or shared contracts, or has multiple coordinated writers. Local work never
  satisfies it; when it is unavailable, the agent reports it as unmet.
- **Studies.** **investigate** answers diagnostic questions; **measure** and **experiment** are
  studies. Uncertainty alone does not start a study. A study that the request does not require
  needs your explicit or standing authority and a finite scope and resource budget. Evidence that
  a decision relies on is saved in the project's `docs/lusona/evidence/`. See
  [evidence](plugins/lusona/references/evidence.md).
- **Visual references.** **explore**, **specify**, **architect** and **design** offer 2-4
  visual options when a choice depends on layout, structure, flow or appearance. UI drafts open
  in the browser, or the agent reports the absolute HTML path; diagrams are fenced Mermaid.
  After you choose, the reference is kept in `docs/lusona/visuals/<record-id>/` with its binding
  items. **implement** reports the status of each binding item, and **review** reports each as
  met, unmet or unchecked. See [visuals](plugins/lusona/references/visuals.md).

## Records and resumption

The agent saves substantive outputs before handoff or completion without being asked: decisions,
agreements, evidence, findings, handoffs, and discussion syntheses that later work depends on.
Explanations and status updates that no later work depends on need no record. When saving is
prohibited, the agent reports what was not saved.

| Work | Record in the project's `docs/lusona/` |
| --- | --- |
| A change that requires a spec | `specs/<change-id>.md` and a row in `work.md` |
| Direct implementation or refactoring without a spec | `notes/<change-slug>.md` |
| Investigation, measurement or experiment | Notes, plus `evidence/` records |
| Consequential architecture decision | `adr/<YYYYMMDD>-<decision-slug>.md` |
| Product brief and capability map | `product.md` |
| Batch | `batches/<batch-slug>.md` |

A spec and its queue row are required in four cases. Size does not decide this.

- The skill defines changes in a spec, as **specify** does.
- You ask for a spec or tracking.
- A spec already exists for the change.
- The change needs independent review because of what it affects.

The queue states are Ideas, Ready, Doing, Review and Done; none authorizes implementation.
Icebox is a section of the queue for parked rows; a parked row keeps its queue state. See
[queue](plugins/lusona/references/queue.md).

Each owning record keeps one current handoff with the objective, decisions, authority, TDD level
and source, evidence, uncertainty, correction counts, blockers, ownership and the next action
(P2). When the host reports context use, the agent prepares a handoff at 40% and completes it
before 50%. On resumption, the agent reads the surviving records and the working tree, and asks
you only for authority or for a fact that changes the next action. Authorization carries across
handoffs. When an abrupt interruption prevents saving, the agent does not claim a checkpoint.
Records from earlier plugin versions stay valid and are updated in place. See
[retention](plugins/lusona/references/retention.md) and [files](plugins/lusona/references/files.md).

To resume, use **status** to assess what remains, or name the work to continue:

> Continue investigating invitation expiry from the saved findings. Check the retained
> reproduction against the current build. Do not change production behavior.

## Replies and next actions

Every task reply ends with the same form (P8); greetings and acknowledgments do not. The status
is **✅ Complete** (requested scope fulfilled), **🔄 In progress** (authorized work continues),
**❓ Needs input** (a prerequisite is missing) or **⏸ Paused** (affected work waits for a stated
prerequisite). Status describes the reply, not the queue state. Hypothetical reply, not evidence
that work occurred:

> **Result:** ❓ Needs input: Choose the TDD level before implementation starts. The spec and
> acceptance criteria are recorded.
>
> **Evidence:** No checks were run; the change is defined, not implemented.
>
> | Next action | Owner | Needs | Authority |
> | --- | --- | --- | --- |
> | Select `none`, `targeted` or `strict`; `targeted` is recommended for the parser change | user | The recorded spec | TDD level not selected |

- The owner is the user, the coordinator or a named skill. The Authority column says
  `Authorized` or names the missing authority.
- A blocking decision or approval comes first. The reply adds **Decisions:** when it made a
  consequential decision, and **Open issues:** when issues remain.
- When the scope is complete and a follow-up serves the agreed outcome, the reply proposes it
  and states the missing authority. When no action remains, it says
  `**Next action:** None for this request` with a one-sentence reason.
- A continuation directive for another session goes in a blockquote below the table.
- The reply keeps the required labels and fields unless you or the host explicitly require an
  incompatible format. A preference for brevity does not remove them. In an adapted format, the
  outcome, evidence, status and next action remain. See the
  [completion examples](plugins/lusona/references/completion.md).

## Installation

Choose your host. Install from the public [lusona/ai-skills](https://github.com/lusona/ai-skills)
repository over HTTPS; no GitHub credentials are required to download it.

### Antigravity

Install directly from GitHub:

```bash
agy plugin install https://github.com/lusona/ai-skills.git
```

The URL installs Lusona from the repository-root manifest. For App and standalone IDE use,
inspect **Customizations** after this global CLI install. The [Antigravity installation guide](INSTALL.md#antigravity)
covers local checkouts, portable packages, updates, removal, and verification limits. It records
a GitHub installation check with Antigravity CLI 1.4.12 on Linux for Lusona 1.4.0; App and IDE
interactive behavior has not been tested.

### Claude Code

```bash
claude plugin marketplace add https://github.com/lusona/ai-skills.git
claude plugin install lusona@lusona-ai-skills --scope user
```

### Codex

```bash
codex plugin marketplace add https://github.com/lusona/ai-skills.git
codex plugin add lusona@lusona-ai-skills
```

### Cursor

Open **Customize > From GitHub Repository**, enter `https://github.com/lusona/ai-skills`,
then install **Lusona Skills** for your project or user. In Agent chat, type `/` to find
Lusona's skills. See the [Cursor installation steps](INSTALL.md#cursor)
for links to Cursor's current documentation and testing status.

### Xcode

In Xcode 27, open **Settings > Intelligence > Agents > Plug-ins > Add Plug-in**.
Choose **Add from URL**, enter `https://github.com/lusona/ai-skills`, and select
Lusona's skills to install. See the [Xcode installation steps](INSTALL.md#xcode)
for setup, local imports, and version details.

Start a new session in your project after installation. For local checkout installation,
portable packages, updates, and removal, see the [installation guide](INSTALL.md).
Choose one catalog source: local checkout or GitHub.

## Reference

- [Changelog](CHANGELOG.md)
- [Installation and removal](INSTALL.md)
- [Privacy policy](PRIVACY.md)
- [Terms of use](TERMS.md)
- [Plugin catalog: skills, references and templates](plugins/lusona/README.md)
- [Loop principles, skills, routing and terminology](plugins/lusona/references/workflow-guide.md)
- [TDD level and verification](plugins/lusona/references/tdd.md)
- [Batch coordination](plugins/lusona/skills/batch/SKILL.md)
- [Records, retention and handoff](plugins/lusona/references/retention.md)
- [Closeout and reopening](plugins/lusona/references/closeout.md)
- [Delegation](plugins/lusona/references/delegation.md)
- [Intent interviews](plugins/lusona/references/interviews.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution scope, local checks, and pull
requests. Use the [bug and feature request forms](https://github.com/lusona/ai-skills/issues/new/choose)
to report problems or propose improvements. The `@lusona/core` team owns repository review.

## License

Skills, templates, documentation, and scripts are available under the [MIT License](LICENSE).

## Development

Canonical workflow sources live in `plugins/lusona/`. Consuming-project data belongs under that
project's `docs/lusona/`; the empty queue structure is `plugins/lusona/templates/work.md.template`.

Plugin record helpers use Bash or PowerShell ([runtime requirements](INSTALL.md#requirements)).
Python 3 is required only for packaging and Python evaluations, not for plugin use.

```bash
claude plugin validate plugins/lusona
claude plugin validate .claude-plugin/marketplace.json
python3 scripts/package.py
```

The package builder checks native manifest names and versions, links, catalog paths, and file
selection. All native manifests must use the same version. It writes to repository-local
`tmp/lusona-package/` and refuses to overwrite an existing output directory; use
`--output tmp/<new-directory>` for another build. Neither installation nor packaging
initializes project records.

The every-task rules and the reply form in each `SKILL.md` are generated from the repository's
`shared/` directory. Edit them there and run `python3 scripts/sync_shared.py --source shared
plugins/lusona`; add `--check` to verify without writing.
