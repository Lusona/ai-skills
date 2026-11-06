# Workflow guide

Read the relevant section for skill selection, invocation, or terminology; this catalog and the routing table are not required for every assignment.

## Skills

| Skill | Persona and responsibility | Output |
| --- | --- | --- |
| [explore](../skills/explore/SKILL.md) | Discussion partner: selective questions, domain context, scenarios and tradeoffs | [Discussion synthesis](../templates/brainstorm.md) in the owning record or notes for substantive outcomes |
| [status](../skills/status/SKILL.md) | Workflow guide: current evidence, dependencies, next action, total known remainder | Read-only [status assessment](../templates/status.md) |
| [batch](../skills/batch/SKILL.md) | Batch coordinator: authorized selected outcomes, dependencies, and ownership | Parent-owned [batch record](../templates/batch.md), linking owning evidence |
| [frame-product](../skills/frame-product/SKILL.md) | Product strategist: long-term vision, users, problem, outcomes, boundaries | [Product brief](../templates/product.md) |
| [map-capabilities](../skills/map-capabilities/SKILL.md) | Product planner: long-term capability coverage, dependencies, useful delivery sequence | Capability map in the [product template](../templates/product.md) |
| [specify](../skills/specify/SKILL.md) | Change analyst: one change's observable behavior and acceptance | [Change agreement and TDD policy](../templates/spec.md) |
| [design](../skills/design/SKILL.md) | Visual designer: UI mockups, screen flows, and diagrams using existing context and references | Inspectable drafts and chosen [visual references](../templates/visual-reference.md), linked from the owning record or notes |
| [architect](../skills/architect/SKILL.md) | Architect: responsibilities, interfaces, data ownership, tradeoffs | Shared or change-specific [ADRs](../templates/adr.md) |
| [implement](../skills/implement/SKILL.md) | Engineer: planning, implementation, explicit TDD, and assigned verification | Code and evidence in the owning record or [notes](../templates/notes.md) |
| [review](../skills/review/SKILL.md) | Reviewer: defects and verification gaps in the actual diff | [Review findings](../templates/review.md), without silent fixes |
| [refactor](../skills/refactor/SKILL.md) | Maintainer: concrete structural improvement preserving behavior | Code and regression evidence in the owning record or [notes](../templates/notes.md) |
| [investigate](../skills/investigate/SKILL.md) | Investigator: bounded technical uncertainty | [Investigation findings](../templates/notes.md) in the owning record or notes |
| [measure](../skills/measure/SKILL.md) | Measurement analyst: decision-relevant magnitude, quality, cost, or change | [Measurement evidence](../templates/evidence.md) with method and limitations |
| [experiment](../skills/experiment/SKILL.md) | Experimenter: evaluate an intervention or alternatives | [Experiment evidence](../templates/evidence.md) with design and exact runs |

## Routing

Consult this table when skill selection is unclear. It maps an observed need to a skill or a
direct action; it is a distinction of responsibilities, not a required sequence. Routine design
choices stay with implementation or refactoring. Measurements and experiments within
existing authorized work need no new command and enter under the [study entry rules](evidence.md#study-entry).

| Evidence or gap | Action | Inputs |
| --- | --- | --- |
| Start or resume unattended selected work | [batch](../skills/batch/SKILL.md) | Exact selection or batch record, and execution authority |
| Explore possibilities or tradeoffs | [explore](../skills/explore/SKILL.md) | The idea or decision |
| Product audience, outcome, or boundaries unclear | [frame-product](../skills/frame-product/SKILL.md) | The missing decision |
| Capabilities or delivery order unclear | [map-capabilities](../skills/map-capabilities/SKILL.md) | Product context |
| Change behavior or acceptance criteria unclear | [specify](../skills/specify/SKILL.md) | The selected outcome |
| UI mockup, screen flow, or diagram needed | [design](../skills/design/SKILL.md) | Existing UI, references, and the visual question |
| Consequential technical design, contract, or ownership decision unresolved | [architect](../skills/architect/SKILL.md) | That decision and accepted constraints |
| Cause or technical feasibility unknown | [investigate](../skills/investigate/SKILL.md) | One bounded question |
| Magnitude, quality, cost, or change to establish | [measure](../skills/measure/SKILL.md) | The decision the result informs and a reference |
| Proposed intervention or alternatives to test | [experiment](../skills/experiment/SKILL.md) | Declared criteria, budget, and stopping condition |
| Defined work needs decomposition or execution, or changed behavior or defect correction | [implement](../skills/implement/SKILL.md) | The selected outcome, explicit TDD, and authorization; a planning-only request stops before implementation |
| Implementation needs review or verification | [review](../skills/review/SKILL.md) when warranted, or name the missing check | The actual diff, intended behavior, and evidence |
| Authorized structural improvement preserving observable behavior | [refactor](../skills/refactor/SKILL.md) | The behavior and interfaces to preserve |
| Required acceptance or delivery remains | Name the exact action and owner | The recorded completion condition |
| Requested scope complete | State completion; recommend a supported useful follow-up, or explicitly state none and why | Established goals and observed findings; follow-up authority remains separate |

Use the linked template for each skill's substantive output, applying relevant sections in
conversation or in the existing owning document. Format under the [shared presentation rules](../README.md#review-and-communication)
and save under [retention](retention.md). Preserve project-local conventions.

See [installation and compatibility](https://github.com/lusona/ai-skills/blob/main/INSTALL.md). In Claude Code, invoke
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
| Leaf | An agent executing one assignment; also called worker or delegate |

A change can contain one task. Use only the skills needed for its unresolved work;
definition, planning, implementation, and review are responsibilities, not mandatory phases.
Selecting one task for implementation does not authorize the rest of its change.
