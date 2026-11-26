# Work item sizing

## 2026-11-25 — How small must a work item or task be?

Compared the canonical skills, references, shared text and record templates at `d99ad1d` against two questions. Must an agent split every separable outcome? Must it choose boundaries that allow parallel execution? This was a source inspection. Agent behavior was not tested.

### Evidence

- Specify recommends the smallest overall scope that solves the problem. It creates work items only on request. Each item must deliver a bounded observable outcome linked to acceptance criteria. The agent orders items by dependency and identifies independent items. [Specify](../../../plugins/lusona/skills/specify/SKILL.md#work-items)
- Implement chooses planning depth from dependencies, uncertainty, coordination and recovery. A single outcome and its checks can suffice. When tasks are needed, each has an observable result and completion checks. The same instruction applies when notes own the change. [Implement](../../../plugins/lusona/skills/implement/SKILL.md#planning-practices) and [notes template](../../../plugins/lusona/templates/notes.md.template)
- Parallel assignments require independence. Within a batch item, sharing a workspace also requires settled shared behavior, disjoint writes and separate mutable check resources. These rules assess an existing split. [Delegation](../../../plugins/lusona/references/delegation.md#coordinator-duties) and [batch workspaces](../../../plugins/lusona/skills/batch/references/workspaces.md#workspaces)

### Conclusion and next action

The rules permit one item to cover several separately verifiable outcomes. They give agents no stopping rule for subdivision or preference for an equally small split that enables parallel work.

Proposed for definition in specify and implement: split whenever each resulting unit has a distinct outcome and a check of its own. Stop when further division would leave a step verifiable only as part of its sibling. Among splits that meet this rule, prefer independent ownership and checks. For automatic work-item creation, revise the explicit user-request trigger in specify and the spec template together. Implementation requires separate authority.

## 2026-11-25 — Implementation agreement

The user accepted the proposed rule and authorized version 3.1.3 and local commits. This supersedes the request-only split trigger. Apply the rule in specify, implement and the spec template. Keep item selection and execution authority with the user.

Check three cases: a change containing two outcomes that can each be checked, a change with a single indivisible outcome, and two checkable outcomes where one depends on the other. The first should split automatically and identify parallel work, the second should stay whole, and the third should retain its dependency. Verify version alignment and package contents. Group the workflow change and release metadata in separate local commits.

The user selected TDD level `none` in this conversation on 2026-11-25.

Verification plan: one read-only Codex agent trial using the candidate skills directly. Apply specify and implement to each of the three cases above. Grade each case against its stated outcome, then stop. The coordinator grades the actor's output. This checks application of the instructions and makes no baseline comparison.

The candidate trial used a profile label and a separate reports CLI message (A), one settings button caption (B), and a new workspace ID command consumed by an executable tutorial (C). The actor produced two independent items with separate checks for A, no work-item table or task list for B, and two verified outcomes with the tutorial depending on the command for C. All three met the declared criteria.

Review prompted clarification of criterion mapping in an omitted table and selection in the final handoff. For the final source, repeat A–C once alongside the same scenarios at base `d99ad1d` using separate read-only Codex actors. Grade against the original criteria and check that scope already authorized can proceed. Stop after this pair. These are bounded checks of the instructions.

### Verification

The base and final actors both recognized that already authorized work can proceed directly to implement. At the base revision, the actor omitted the spec work-item table in all three cases because nobody asked to split. On the final source, the actor gave A two items with separate checks, omitted the table and task list for B, and gave C two items with the tutorial depending on the command. Both actors identified the execution dependency in C. The coordinator graded these single-run results. The trials exercised the canonical text directly. Installed discovery and live product execution were outside the trial.

The workflow editor used `gpt-6.2-sol` with medium reasoning. The three read-only trial actors used that model with low reasoning. An independent reviewer using the same model with medium reasoning audited the three workflow files and release changes against `docs/skill-audit.md`. The audit found two ambiguous instructions in specify. One correction round scoped criterion mapping to the table and clarified how selection and authorization determine the next action. The independent reviewer rechecked the corrected wording, matched trials and archived record and returned a passing audit. The queue row came from the prior investigation's proposal. It was already tracked when implementation began.

Against base `d99ad1d`, all 231 repository tests and 163 loop-conformance tests passed. Bash helper checks and 203 PowerShell 7 assertions passed. The shared-region, skill-template, voice, instruction, contract, baseline inventory and whitespace checks passed. Claude validated its plugin and marketplace. All five native manifest copies and five README notices report 3.1.3. The final ZIP passed its integrity check and contains the exact revised skills, template and manifests. Installation and native Windows runs were not tested.
