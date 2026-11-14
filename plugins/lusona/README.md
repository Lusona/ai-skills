# Lusona plugin catalog

For the product overview, workflow, skills and installation, see the
[repository README](https://github.com/lusona/ai-skills/blob/main/README.md).

This is a human catalog of bundled resources. No skill requires reading it. Each `SKILL.md`
contains the task rules and links its references with the point at which to read them.

## References

| Reference | Purpose |
| --- | --- |
| [closeout](references/closeout.md) | Closing tracked work and updating enduring documentation |
| [commits](references/commits.md) | Staging, commits and integration |
| [completion](references/completion.md) | Final reply examples |
| [corrections](references/corrections.md) | Failed checks, review findings and correction limits |
| [delegation](references/delegation.md) | Assignments, model routing, independent review and leaf lifecycle |
| [evidence](references/evidence.md) | Measurement and experiment evidence |
| [files](references/files.md) | Project record layout and compatibility |
| [interviews](references/interviews.md) | Questions about intent, priorities and tradeoffs |
| [naming](references/naming.md) | Record names and helper commands |
| [queue](references/queue.md) | Specs, queue states, selection and parking |
| [retention](references/retention.md) | Saving findings, evidence and handoffs |
| [revisions](references/revisions.md) | Revisiting accepted decisions and changing objectives |
| [tdd](references/tdd.md) | TDD levels and verification |
| [visuals](references/visuals.md) | Visual options and chosen references |
| [workflow-guide](references/workflow-guide.md) | Loop principles, skill responsibilities and terminology |
| [batch: assignments](skills/batch/references/assignments.md) | Batch assignments and results |
| [batch: authority](skills/batch/references/authority.md) | Batch authorization, decisions and scheduling |
| [batch: deferral-and-resumption](skills/batch/references/deferral-and-resumption.md) | Deferrals, resumption and stopping a batch |
| [batch: integration](skills/batch/references/integration.md) | Serialized integration and interrupted-transfer recovery |
| [batch: leaf-rules](skills/batch/references/leaf-rules.md) | Leaf responsibilities inside a batch |
| [batch: repairs](skills/batch/references/repairs.md) | Repair budgets and corrective rounds |
| [batch: start-and-resume](skills/batch/references/start-and-resume.md) | Starting and resuming batch prompts |
| [batch: workspaces](skills/batch/references/workspaces.md) | Workspace selection and change transfers |

## Templates

Skills link these templates for their output records.

- [adr.md.template](templates/adr.md.template): architecture decision record.
- [agents-section.md.template](templates/agents-section.md.template): Lusona section for a project's agent instructions.
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
(PowerShell) create the work queue, dated specs, ADRs, notes and history files, and stamp record headers. The
[naming](references/naming.md) reference lists their commands.
