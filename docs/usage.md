# Using Lusona Skills

[Back to the README](../README.md) · [Workflow details](workflow.md) · [Installation](../INSTALL.md)

Describe what you need. The agent can recommend the next skill and ask for missing decisions;
you do not need to memorize the catalog. Use these details when you want to choose a skill
or make a more specific request.

[Host invocation](#host-invocation) · [Optional setup](#optional-setup) · [Choose a skill](#choose-a-skill) · [Example requests](#example-requests) · [More specific requests](#more-specific-requests)

## Host invocation

Install the complete native plugin using [INSTALL.md](../INSTALL.md), then start a new session
in your project. Installation, updates, removal, and host testing caveats are maintained there.

Invoke the skill in your host, then state what you need:

| Host | Invocation |
| --- | --- |
| Claude Code | `/lusona:<skill>`, for example `/lusona:status` |
| Codex CLI | `$lusona:<skill>`, for example `$lusona:status` |
| Codex desktop app | `$lusona:<skill>` or `/lusona:<skill>`, or select it from the skill UI |
| Cursor | Type `/` in Agent chat and select the skill |
| Xcode | Type `/` in an agent conversation and select the installed skill |
| Antigravity App and CLI | `/<skill>`, for example `/status` |
| Antigravity standalone IDE | Inspect **Customizations** and name the Lusona skill in your request |

## Optional setup

Run **setup** if you want to prepare project records and standing preferences. It creates
`docs/lusona/` and the work queue, asks for optional TDD and model tier preferences, and proposes
agent instructions. It writes those instructions only after you confirm the exact text.
Setup is optional; every skill creates the records its work needs.

## Choose a skill

These groups describe reader intent, not stages. Use only the skills the work needs. An
authorized change with clear behavior and scope can go directly to **implement** without
**specify**. The agent can change skills without asking you to direct each transition.

### Orient or define a direction

| Skill | Use when | Output |
| --- | --- | --- |
| [setup](../plugins/lusona/skills/setup/SKILL.md) | You want to prepare a project for Lusona | Project records and agent instructions |
| [status](../plugins/lusona/skills/status/SKILL.md) | You need progress, remaining work, or a place to resume | Assessment and next action |
| [explore](../plugins/lusona/skills/explore/SKILL.md) | You want to compare directions or options before choosing | Clearer understanding or recommendation |
| [frame-product](../plugins/lusona/skills/frame-product/SKILL.md) | A product's audience, problem, vision, or boundaries need definition | Product brief |
| [map-capabilities](../plugins/lusona/skills/map-capabilities/SKILL.md) | Coverage, dependencies, or delivery order need clarification | Capability map |

### Define a change

| Skill | Use when | Output |
| --- | --- | --- |
| [specify](../plugins/lusona/skills/specify/SKILL.md) | Behavior, scope, or acceptance criteria need definition | Spec and acceptance criteria |
| [architect](../plugins/lusona/skills/architect/SKILL.md) | A lasting technical decision about boundaries, contracts, or ownership is open | Architecture decision record |
| [design](../plugins/lusona/skills/design/SKILL.md) | A screen, flow, state, or relationship must be seen to be judged | Inspectable visual reference |

### Implement or review

| Skill | Use when | Output |
| --- | --- | --- |
| [implement](../plugins/lusona/skills/implement/SKILL.md) | You authorize a bounded change, or request only a plan | Verified change, or proposed approach |
| [refactor](../plugins/lusona/skills/refactor/SKILL.md) | Code has a structural problem and behavior must stay the same | Restructured code and regression evidence |
| [review](../plugins/lusona/skills/review/SKILL.md) | A diff needs review against intended behavior | Findings without implementation edits |
| [batch](../plugins/lusona/skills/batch/SKILL.md) | You explicitly authorize unattended work on selected queue items | Integrated outcomes and resumable batch record |

### Resolve an uncertainty

| Skill | Use when | Output |
| --- | --- | --- |
| [investigate](../plugins/lusona/skills/investigate/SKILL.md) | A cause, observed behavior, or feasibility question needs evidence | Supported findings |
| [measure](../plugins/lusona/skills/measure/SKILL.md) | A decision needs a baseline, benchmark, or comparable observations | Measurement and uncertainty |
| [experiment](../plugins/lusona/skills/experiment/SKILL.md) | An intervention or alternative needs a bounded trial | Adopt, reject, refine, or inconclusive result |

The [workflow guide](../plugins/lusona/references/workflow-guide.md) gives the full routing table,
skill responsibilities, and terminology.

## Example requests

After invoking the skill or selecting it in your host's UI, describe the outcome:

- **status:** What remains in this project, and what should we do next?
- **explore:** Compare ways to let customers invite their team. Keep the comparison in chat.
- **investigate:** Find why expired invitations are still accepted. Do not change production behavior.
- **review:** Review this diff for regressions. Report findings without editing the implementation.
- **design:** Show two invitation-screen options before we choose one. Do not implement them yet.

A status request assesses and recommends; it does not authorize new implementation. Once you
authorize a bounded change, the agent continues within that scope and asks for decisions it
cannot make under the existing agreement.

## More specific requests

Name the skill, outcome or input record, authorized scope, and completion criteria. For
implementation, also select a TDD level and state any delivery boundary:

> **implement:** Add invitation expiry after seven days. Preserve existing accepted invitations.
> Done means: invitations older than seven days are rejected, accepted invitations are unchanged,
> and the test suite passes. Use TDD level `targeted` for the expiry boundary. Verify locally; do not deploy.

A request for discussion or design can set different boundaries, such as keeping a comparison
in chat or producing visual options without implementing them. A planning-only request to
**implement** ends with a proposed approach; it does not authorize code changes.

You can state constraints in ordinary language. If testing requirements or another necessary
decision are missing, the agent asks. See [scope and testing](workflow.md#scope-and-testing)
for the details, including the three TDD levels and standing preferences.

For resumption, name the saved work:

> Continue investigating invitation expiry from the saved findings. Check the retained
> reproduction against the current build. Do not change production behavior.

See [records and resumption](workflow.md#records-and-resumption) for what another session retains.
