---
name: implement
description: Implement an authorized bounded change with adaptive planning, explicit TDD, and verification. Also use for explicit planning-only requests, which end with a proposed approach and do not authorize implementation.
---

# Implement

Apply [core loading rules](../../README.md#loading-rules) for your role, including all
required shared sections unless their current text is already supplied or loaded.
Read linked procedures only when their operation applies.
Persona: implementation engineer, responsible for necessary decomposition, completing
authorized work, and verifying the agreed outcome.

A small change can stay in conversation. When recovery or coordination needs a saved owner,
create or update the combined
[change record template](../../templates/spec.md) at `docs/lusona/specs/<change-id>.md` under
the [naming rules](../../references/naming.md) and [retention rules](../../references/retention.md).
Use only relevant sections; a clear authorized request does not require Specify first.
Maintain existing separate plans in place; do not migrate records or create a companion plan by default.

Authorization for a selected task does not authorize the whole change. An implementation
request authorizes its stated scope, including necessary planning; skill transitions do not
require another approval or expand that scope. **An explicit planning-only request ends with
the proposed approach. Do not edit implementation or dependencies, execute the proposed change,
or treat readiness as authorization.** An unset TDD policy blocks implementation, not planning.

## Assess the agreement and current evidence

- Inspect the working tree, relevant code, callers, and tests. Preserve unrelated work.
  Read acceptance criteria, constraints, explicit TDD and its source, completion conditions,
  applicable ADRs, and existing evidence. Reuse settled decisions.
- Resolve missing behavior or scope through [specify](../specify/SKILL.md),
  consequential technical decisions through [architect](../architect/SKILL.md), and empirical
  uncertainty through [investigate](../investigate/SKILL.md) when needed. These are specialist
  responsibilities to delegate as needed, not mandatory stages. An assigned leaf returns an
  out-of-scope need to its parent.
- Apply the [TDD rules](../../references/tdd.md): record a supplied policy or standing
  preference, or recommend a level and ask before implementation. Continue useful independent
  inspection while awaiting decisions. Do not silently change agreed behavior, scope, or criteria.
- Choose planning depth from dependencies, uncertainty, coordination, and recovery needs,
  including a long run whose earlier context will be summarized before it finishes.
  Straightforward work needs an outcome and checks, not a manufactured task list. Add an
  optional execution section when sequencing helps. Detail the next useful increment; expand
  later tasks only to resolve dependencies or meet an explicit planning request.
- When tasks are useful, give each an observable outcome, scope, dependencies, and completion
  checks linked to criteria without repeating requirements. Confirm existing paths and commands;
  label proposals and unverified commands, and resolve command uncertainty before relying on a
  check. Establish consumed/produced interfaces, ownership,
  and mutable verification resources before dependent or concurrent work.
- Establish verification and recovery before authorized persistent-data or deployment operations,
  including migration ordering when needed. Plans do not authorize deployment.
- Before execution, check that scoped acceptance criteria have planned or existing verification
  and the next increment has expected results and no blocking ambiguity. Fix routine omissions
  inline without adding an approval gate. Revise the approach as evidence changes within authority.
- For planning-only work, report the proposed execution section, assumptions, unresolved decisions,
  verification approach, and concrete next action. Save only within authorized documentation scope;
  do not move the item to Doing. Stop before implementation.

## Implement and check bounded increments

- For work needing workflow tracking, the coordinator applies the
  [queue rules](../../references/queue.md). Recovery recording alone does not require tracking.
  Keep internal tasks out of queue rows.
- Follow the recorded TDD sequence in coherent bounded increments through observable interfaces,
  with red/green evidence for test-first behaviors.
- Resolve routine technical choices within authorization. Investigate uncertainty before escalating
  a decision. Ask about consequential choices beyond authority through the permitted native question
  tool; continue independent authorized work.
- Run agreed and applicable repository checks. Judge status and output against defined expected
  results, including explicitly required error behavior; an arbitrary nonzero exit is not success.
  Failed assertions and unrun required checks prevent completion. Report environmental blockers.
- Inspect each increment's evidence and choose the next action from remaining criteria or
  uncertainty; revisit clarification, design, or investigation when evidence requires it,
  preserving accepted constraints and authority. Inspect the final diff for defects, unintended changes, and unnecessary complexity.
  Obtain independent review when the core requires it; self-inspection does not satisfy it.
- Evaluate success against agreed behavior, not task completion. For user-visible work, provide
  where to try it, concrete actions, and expected results. Record human acceptance only when given.
  Update existing product or architecture documentation when enduring behavior changes.
- The coordinator records results, check and review evidence, limitations, and the current handoff
  in the owning change record under the [retention rules](../../references/retention.md), and
  applies [closeout](../../references/closeout.md) before removing a Done row. Batch records
  link per-change evidence.

## Commit verified increments

Complete the selected TDD sequence and required verification, then apply the
[commit procedure](../../references/commits.md), subject to user and repository restrictions.
Planning does not authorize commits.

Apply [Context budget](../../README.md#context-budget) at each verified task boundary.

## Next action

Continue the next authorized increment. At the authorized boundary, report behavior,
consequential decisions, evidence, and remaining uncertainty, and name any required review,
acceptance, delivery, or blocker with its inputs. Recommend [refactor](../refactor/SKILL.md)
only for a concrete structural problem.
