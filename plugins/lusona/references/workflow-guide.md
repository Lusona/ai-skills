# Workflow guide

Read the relevant section for skill selection, invocation, or terminology; this catalog is not required for every assignment.

## Skills

| Skill | Persona and responsibility | Output |
| --- | --- | --- |
| [explore](../skills/explore/SKILL.md) | Discussion partner: selective questions, domain context, scenarios and tradeoffs | [Discussion synthesis](../templates/brainstorm.md) when useful; conversation by default |
| [status](../skills/status/SKILL.md) | Workflow guide: current evidence, dependencies, next action, total known remainder | Read-only [status assessment](../templates/status.md) |
| [batch](../skills/batch/SKILL.md) | Batch coordinator: authorized selected outcomes, dependencies, and ownership | Parent-owned [batch record](../templates/batch.md), linking owning evidence |
| [frame-product](../skills/frame-product/SKILL.md) | Product strategist: long-term vision, users, problem, outcomes, boundaries | [Product brief](../templates/product.md) |
| [map-capabilities](../skills/map-capabilities/SKILL.md) | Product planner: long-term capability coverage, dependencies, useful delivery sequence | Capability map in the [product template](../templates/product.md) |
| [specify](../skills/specify/SKILL.md) | Change analyst: one change's observable behavior and acceptance | [Change agreement and TDD policy](../templates/spec.md) |
| [architect](../skills/architect/SKILL.md) | Architect: responsibilities, interfaces, data ownership, tradeoffs | Shared or change-specific [ADRs](../templates/adr.md) |
| [implement](../skills/implement/SKILL.md) | Engineer: planning, implementation, explicit TDD, and assigned verification | Code and evidence in the [change record](../templates/spec.md) |
| [review](../skills/review/SKILL.md) | Reviewer: defects and verification gaps in the actual diff | [Review findings](../templates/review.md), without silent fixes |
| [refactor](../skills/refactor/SKILL.md) | Maintainer: concrete structural improvement preserving behavior | Code and regression evidence in the [change record](../templates/spec.md) |
| [investigate](../skills/investigate/SKILL.md) | Investigator: bounded technical uncertainty | [Investigation findings](../templates/notes.md) in conversation or the owning record |

For routing, use **investigate** when facts, causes, or feasibility are unknown and need
evidence; **architect** for consequential design, contract, or ownership choices and their
rationale; **refactor** for an authorized structural improvement that preserves observable
behavior and compatibility; and **implement** for changed behavior or defect correction.
This is a distinction of responsibilities, not a required sequence: routine design choices
stay with implementation or refactoring.

Use the linked template for each skill's substantive output under the
[shared presentation contract](../README.md#review-and-communication). Apply relevant sections in
conversation or in the existing owning document; omit irrelevant fields and keep short
answers short. Substantive assessments and handoffs default to Result, Evidence, and Next action
with the shared status words and glyphs; ordinary dialogue remains natural. This presentation
default does not replace specialized tables or saved record schemas. Templates do not authorize
saving, force new files, or require migration of existing records. Preserve user-requested
formats and project-local conventions.
Use [retention](retention.md) for recovery needs across all skills; conversation by default
does not mean request-only saving. Read-only review/status boundaries remain binding.

See [installation and compatibility](../INSTALL.md). In Claude Code, invoke
`/lusona:<skill>`; in other harnesses, use their exposed skill UI. A useful prompt names
the skill, selected outcome or input document, and authorized scope.

## Terminology

| Term | Meaning |
| --- | --- |
| Product | The overall system and its intended outcomes |
| Capability | Something the product enables users to do |
| Change | A bounded feature, bug fix, refactor, or other deliverable |
| Task | A verifiable implementation step within a change |
| Assignment | Bounded work delegated to a subagent |
| Coordinator | The parent agent responsible for delegation, integration, and verification |

A change can contain one task. Use only the skills needed for its unresolved work;
definition, planning, implementation, and review are responsibilities, not mandatory phases.
Selecting one task for implementation does not authorize the rest of its change.
