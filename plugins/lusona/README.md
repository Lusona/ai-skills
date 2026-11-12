# Lusona Skills

Lusona is a set of 14 skills for product and engineering work in Claude Code, Codex and other hosts.
Each skill covers one responsibility, such as specifying a change, implementing it or reviewing it.
The skills share one work loop, one record layout under `docs/lusona/` and one reply format.

This README is human documentation and a catalog. No skill requires reading it. Each `SKILL.md`
contains the rules that apply to every task. Each skill links the references it uses, with the
point at which to read each one.

For installation, see [INSTALL.md](https://github.com/lusona/ai-skills/blob/main/INSTALL.md).

![Lusona interaction loop and supporting commands](assets/workflow-loop.svg)

## The loop

The skills follow eight loop principles. The
[workflow guide](references/workflow-guide.md#loop-principles) defines them.

1. P1 Non-sequential: the next skill follows from the unresolved need, and any skill can follow any other.
2. P2 Refinement: each pass compares its result with the intended outcome and carries outcome, decisions, authority, TDD level, evidence and uncertainty forward.
3. P3 Prior decisions are inputs: when new input contradicts a decision, the agent states the conflict and revisits the decision with the user.
4. P4 Recorded invalidation: a superseded decision is marked with date and source, and its rationale is kept.
5. P5 Evidence over assertion: behavior and completion are claimed only from observed checks.
6. P6 Authority stays with the user: specs, plans, ADRs and queue states do not authorize implementation.
7. P7 Continue bounded work: the agent takes the next authorized action unprompted and pauses only the affected work.
8. P8 Every reply names the next action and its owner, or states that none remains and why.

## Skills

In Claude Code, invoke a skill as `/lusona:<skill>`. Other hosts use their own skill interface.

The [workflow guide](references/workflow-guide.md#skills) lists each skill with its persona, responsibility and output.

## References

Each skill links a reference with a trigger sentence. The table repeats each reference's own trigger.
Plugin-level references serve more than one skill. A per-skill reference serves one skill.

| Reference | Read when |
| --- | --- |
| [closeout](references/closeout.md) | As coordinator before closing or reopening tracked work, before removing a Done row, and before updating product or architecture documentation after an enduring change |
| [commits](references/commits.md) | Before staging, committing, rebasing or integrating changes |
| [completion](references/completion.md) | Before composing a task's final reply |
| [corrections](references/corrections.md) | Before correcting or probing an observed failed check or review finding |
| [delegation](references/delegation.md) | Before dispatching an assignment, after each leaf result, before closing or handing off responsibility for leaves, when deciding whether independent review is required, and as a leaf before returning a result |
| [evidence](references/evidence.md) | Before starting a measurement or experiment, and before producing or retaining a material measurement, evaluation or experiment |
| [files](references/files.md) | Before locating, creating or maintaining a project record under `docs/lusona/`, including a record from an earlier plugin version |
| [interviews](references/interviews.md) | Before asking the user about intent, priorities or acceptable tradeoffs that are unclear |
| [naming](references/naming.md) | Before creating, updating or renaming a spec, plan, ADR, notes or history record, or before running the work-record helper |
| [queue](references/queue.md) | Before creating, updating or using a spec, and before maintaining or assessing queue state, selection or parking |
| [retention](references/retention.md) | Before saving findings, evidence or a handoff, before choosing a record for them, before a checkpoint, and when context use reaches 40% |
| [revisions](references/revisions.md) | When new input contradicts an accepted decision, before recording the outcome of revisiting it, and before applying a follow-up request that changes the objective |
| [tdd](references/tdd.md) | When selecting, recording or applying a TDD level |
| [visuals](references/visuals.md) | Before offering visual options or a diagram, and before implementing or reviewing work whose owning record links a visual reference |
| [workflow-guide](references/workflow-guide.md) | Before explaining the workflow, a skill's responsibility or a workflow term, and before choosing the skill for the next action or for a batch item |
| [batch: assignments](skills/batch/references/assignments.md) | Before dispatching a batch assignment, and when a batch assignment result arrives |
| [batch: authority](skills/batch/references/authority.md) | Before recording a batch's authorization, before settling a routine decision inside a batch, and before deferring an item for a missing decision, authority or TDD level, or for new input that contradicts an accepted decision |
| [batch: deferral-and-resumption](skills/batch/references/deferral-and-resumption.md) | Before deferring a batch item, before continuing a recorded batch, and before stopping or completing a batch |
| [batch: integration](skills/batch/references/integration.md) | Before integrating a batch item's candidate, and before recovering an interrupted candidate or promotion |
| [batch: leaf-rules](skills/batch/references/leaf-rules.md) | As a leaf before starting a batch assignment, and as coordinator before writing one |
| [batch: repairs](skills/batch/references/repairs.md) | Before charging, dispatching, cancelling or resuming a repair round for a batch item, and before retrying after an environment failure |
| [batch: start-and-resume](skills/batch/references/start-and-resume.md) | Before asking the user to resolve a batch's selection, authority or TDD level, and before giving guidance on starting or resuming a batch |
| [batch: workspaces](skills/batch/references/workspaces.md) | Before the first production edit of a batch item, before choosing an item's workspace, and before transferring an item's changes |

## Templates

Skills link these templates for their output records.

- [adr.md.template](templates/adr.md.template): architecture decision record.
- [batch.md.template](templates/batch.md.template): batch record.
- [brainstorm.md.template](templates/brainstorm.md.template): discussion synthesis.
- [evidence.md.template](templates/evidence.md.template): measurement or experiment evidence.
- [history.md.template](templates/history.md.template): weekly history of closed work.
- [notes.md.template](templates/notes.md.template): notes and investigation findings.
- [product.md.template](templates/product.md.template): product brief and capability map.
- [review.md.template](templates/review.md.template): review findings.
- [spec.md.template](templates/spec.md.template): change specification.
- [status.md.template](templates/status.md.template): status assessment.
- [visual-page.html.template](templates/visual-page.html.template): page for visual options.
- [visual-reference.md.template](templates/visual-reference.md.template): chosen visual reference.
- [work.md.template](templates/work.md.template): work queue.

## Record helper

[work-record.sh](scripts/work-record.sh) (Bash) and [work-record.ps1](scripts/work-record.ps1)
(PowerShell) create dated specs, ADRs, notes and history files, and stamp record headers. The
[naming](references/naming.md) reference lists their commands.
