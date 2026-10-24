---
name: refactor
description: Refactor implemented product code in bounded increments while preserving observable behavior and compatibility. Use when existing code has a concrete structural problem; use implement for new behavior and bug fixes.
---

# Refactor

Apply [core loading rules](../../README.md#loading-rules) for your role, including all
required shared sections unless their current text is already supplied or loaded.
Read linked procedures only when their operation applies.
Persona: maintenance engineer, focused on simpler structure with stable observable behavior.
Work on existing implementation.

A small refactor may stay in the conversation. When recovery or coordination needs a saved
owner, create or update [the change record](../../templates/spec.md) directly under
[naming](../../references/naming.md) and [retention](../../references/retention.md), using only
relevant sections. A clear authorized request does not require Specify first. Use existing
execution records in place. Do not create a product-wide cleanup backlog from incidental findings.

- Inspect the working tree, relevant implementation, callers, and tests. Preserve unrelated
  changes. Identify a concrete structural problem and its consequence, such as duplicated
  business rules or dependencies that prevent testing a boundary. Name the bounded target,
  intended structural result, and observable behavior and interfaces that must remain stable.
- Distinguish refactoring from defect correction or new behavior. If the requested outcome
  changes behavior, route that part to [implement](../implement/SKILL.md),
  or [specify](../specify/SKILL.md) if scope is unsettled. Do not silently
  fix discovered bugs or expand into adjacent modules. No change is valid when the proposed
  abstraction or rewrite has no demonstrated benefit.
- Use reversible increments with focused regression checks; record sequencing only when useful.
  Prefer a local change over a speculative framework or rewrite. Resolve routine implementation
  choices independently; ask through the permitted native question tool when a consequential
  decision exceeds existing authority or changes the selected TDD policy.
- Apply the [TDD rules](../../references/tdd.md) for behavior-preserving restructuring. If TDD is
  unset, ask before editing implementation; inspection and planning can continue. A separately
  authorized behavior change follows the test-first sequence in [implement](../implement/SKILL.md).
- Establish the relevant baseline before edits. Report pre-existing failures and distinguish
  them from regressions; resolve failures that prevent verifying the affected behavior before
  proceeding with dependent changes. With TDD `none`, verification remains required.
- A planning request ends with the plan. A refactoring implementation request authorizes
  its bounded scope without another approval after planning. For work needing workflow tracking,
  the coordinator applies the [queue rules](../../references/queue.md); recovery recording alone
  does not require tracking. Do not reopen Done work implicitly.
- Run regression checks at boundaries where failures can be attributed. Independent assignments
  may run in parallel; dependent work waits for verified prerequisites. Preserve public contracts,
  persisted formats, and user-visible behavior.
- Inspect the final diff for unintended behavior changes and unnecessary abstractions. Run
  agreed and required checks, and obtain independent review when the core requires it. Update
  existing enduring product or architecture documentation when affected. The coordinator
  records the structural result, baseline and final evidence, limitations, and current handoff
  under the [retention rules](../../references/retention.md).

## Commit verified increments

Establish and preserve the passing baseline, satisfy the selected coverage policy, and run
required regression checks, then apply the [commit procedure](../../references/commits.md),
subject to user and repository restrictions.

Apply [Context budget](../../README.md#context-budget) at each verified structural increment.

## Next action

Continue the next authorized increment while the structural objective remains unmet; resolve
a failed or missing check before dependent edits. At the authorized boundary, name required
review, acceptance, or delivery with its diff scope and preservation constraints.
