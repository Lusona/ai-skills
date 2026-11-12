# Workflow guide

Read before explaining the workflow, a skill's responsibility or a workflow term, and before choosing the skill for the next action or for a batch item. Read only the section you need.

## Loop principles

| ID | Principle |
| --- | --- |
| P1 | Non-sequential: select the next skill from the unresolved need; any skill may follow any other |
| P2 | Refinement: compare each result with the intended outcome; carry outcome, decisions, authority, TDD level, evidence and uncertainty into the next pass |
| P3 | Prior decisions are inputs: when new input contradicts a decision, state the conflict and revisit it with the user |
| P4 | Recorded invalidation: mark a superseded decision with date and source, and keep its rationale |
| P5 | Evidence over assertion: claim behavior and completion only from observed checks |
| P6 | Authority stays with the user: specs, plans, ADRs and queue states do not authorize implementation |
| P7 | Continue bounded work: take the next authorized action unprompted; pause only affected work |
| P8 | Every reply names the next action and its owner, or states that none remains and why |

## Skills

| Skill | Persona and responsibility | Output |
| --- | --- | --- |
| [explore](../skills/explore/SKILL.md) | Discussion partner: selective questions, domain context, scenarios and tradeoffs | [Discussion synthesis](../templates/brainstorm.md.template) in the owning record or notes, when the synthesis meets a save condition in retention |
| [status](../skills/status/SKILL.md) | Workflow guide: current evidence, dependencies, next action, total known remainder | Read-only [status assessment](../templates/status.md.template) |
| [batch](../skills/batch/SKILL.md) | Batch coordinator: authorized selected outcomes, dependencies and ownership | Coordinator-owned [batch record](../templates/batch.md.template), linking owning evidence |
| [frame-product](../skills/frame-product/SKILL.md) | Product strategist: long-term vision, users, problem, outcomes, boundaries | [Product brief](../templates/product.md.template) |
| [map-capabilities](../skills/map-capabilities/SKILL.md) | Product planner: long-term capability coverage, dependencies, delivery order | Capability map in the [product template](../templates/product.md.template) |
| [specify](../skills/specify/SKILL.md) | Change analyst: one change's observable behavior and acceptance | [Change agreement and TDD level](../templates/spec.md.template) |
| [design](../skills/design/SKILL.md) | Visual designer: UI mockups, screen flows and diagrams using existing context and references | Inspectable drafts and chosen [visual references](../templates/visual-reference.md.template), linked from the owning record or notes |
| [architect](../skills/architect/SKILL.md) | Architect: responsibilities, interfaces, data ownership, tradeoffs | Shared or change-specific [ADRs](../templates/adr.md.template) |
| [implement](../skills/implement/SKILL.md) | Engineer: planning, implementation, explicit TDD and assigned verification | Code and evidence in the owning record or [notes](../templates/notes.md.template) |
| [review](../skills/review/SKILL.md) | Reviewer: defects and verification gaps in the actual diff | [Review findings](../templates/review.md.template), without silent fixes |
| [refactor](../skills/refactor/SKILL.md) | Maintainer: concrete structural improvement preserving behavior | Code and regression evidence in the owning record or [notes](../templates/notes.md.template) |
| [investigate](../skills/investigate/SKILL.md) | Investigator: bounded technical uncertainty | [Investigation findings](../templates/notes.md.template) in the owning record or notes |
| [measure](../skills/measure/SKILL.md) | Measurement analyst: magnitude, quality, cost or change that a decision depends on | [Measurement evidence](../templates/evidence.md.template) with method and limitations |
| [experiment](../skills/experiment/SKILL.md) | Experimenter: evaluate an intervention or alternatives | [Experiment evidence](../templates/evidence.md.template) with design and exact runs |

- Skills supply expertise, not authority or mandatory phases.
- Use each skill's linked template for its output. Apply the sections the work has content for, in the reply or in the existing owning record.
- Preserve project-local conventions.
- In Claude Code, invoke a skill as `/lusona:<skill>`. In other hosts, use the host's skill interface.
- A prompt that invokes a skill names the skill, the selected outcome or input record, and the authorized scope.

## Routing

Choose the row that matches the observed need. The rows separate responsibilities; they are not a required sequence.

| Evidence or gap | Action | Inputs |
| --- | --- | --- |
| Start or resume unattended selected work | [batch](../skills/batch/SKILL.md) | Exact selection or batch record, and execution authority |
| Explore possibilities or tradeoffs | [explore](../skills/explore/SKILL.md) | The idea or decision |
| Product audience, outcome or boundaries unclear | [frame-product](../skills/frame-product/SKILL.md) | The missing decision |
| Capabilities or delivery order unclear | [map-capabilities](../skills/map-capabilities/SKILL.md) | Product context |
| Change behavior or acceptance criteria unclear | [specify](../skills/specify/SKILL.md) | The selected outcome |
| UI mockup, screen flow or diagram needed | [design](../skills/design/SKILL.md) | Existing UI, references and the visual question |
| Consequential technical design, contract or ownership decision unresolved | [architect](../skills/architect/SKILL.md) | That decision and accepted constraints |
| Cause or technical feasibility unknown | [investigate](../skills/investigate/SKILL.md) | One bounded question |
| Magnitude, quality, cost or change to establish | [measure](../skills/measure/SKILL.md) | The decision the result informs and a reference |
| Proposed intervention or alternatives to test | [experiment](../skills/experiment/SKILL.md) | Declared criteria, budget and stopping condition |
| Defined work needs decomposition or execution, or behavior needs changing or a defect needs correcting | [implement](../skills/implement/SKILL.md) | The selected outcome, explicit TDD and authorization; a planning-only request stops before implementation |
| Implementation needs review or verification | [review](../skills/review/SKILL.md) when independent review is required, otherwise name the missing check | The actual diff, intended behavior and evidence |
| Authorized structural improvement preserving observable behavior | [refactor](../skills/refactor/SKILL.md) | The behavior and interfaces to preserve |
| Required acceptance or delivery remains | Name the exact action and owner | The recorded completion condition |
| Requested scope complete | State completion; propose a follow-up that serves the agreed outcome, or state that none remains and why | Established goals and observed findings; follow-up authority stays separate |

- Routine design choices stay with implement or refactor.
- A measurement or experiment inside authorized work needs no new user request.
- Moving from one skill to another needs no new approval.
- Discussion and read-only review grant no implementation authority.

## Terminology

| Term | Meaning |
| --- | --- |
| Product | The overall system and its intended outcomes |
| Capability | Something the product enables users to do |
| Change | A bounded outcome: a feature, bug fix, refactor or other deliverable |
| Task | One verifiable implementation step within a change |
| Assignment | Bounded work the coordinator gives to a leaf |
| Coordinator | The agent responsible for the user conversation, delegation, integration and verification |
| Leaf | An agent executing one assignment |
| Writer | A coordinator or leaf that holds write ownership of files, a workspace or a record |
| Queue state | Ideas, Ready, Doing, Review or Done; a row parked in Icebox keeps its queue state |
| Execution record | An existing file in `docs/lusona/plans/` that holds a change's execution steps apart from its spec; not created for new changes |
| Accepted decision | A decision recorded as accepted, by the user or under existing authorization, with its source; the Decisions rule applies to it |
| Settled decision | An accepted decision, or a routine decision recorded within delegated authority |
| Skill prompt | Text that invokes a skill; it names the skill, the selected outcome or input record, and the authorized scope |
| Continuation directive | An instruction for another actor or session that must continue the work |

- A change can contain one task.
- Use only the skills that the change's unresolved work needs. Definition, planning, implementation and review are responsibilities, not mandatory phases.
- Selecting one task for implementation does not authorize the rest of its change.
