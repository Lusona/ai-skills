# Spec <change-id>: <name>

Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>

Kind: feature | bug fix | refactor | other
Work item: <queue item or historical completion entry; state lives there; omit for untracked work>
Context: <existing product, issue, or ticket link when relevant>

Use relevant sections only. This change record owns agreement, optional execution, evidence,
and one current handoff. A clear small request can stay in conversation. Preserve existing
split records in place; do not copy their evidence here or require a companion plan.
Implement/refactor can create this record directly; Specify is not a prerequisite. A minimal
recovery note does not require this full structure. User and host formatting constraints apply.

## Agreement

- User and problem:
- Desired behavior or structural outcome:
- Scope and exclusions:
- Accepted constraints and invariants: <required behavior, compatibility, technical constraints, and sources>
- Completion condition: <including human acceptance or delivery only when required>

### Acceptance criteria

- [ ] AC1: <Observable result and relevant failure or boundary behavior>

### Decisions and uncertainty

- Accepted decisions and source: <link existing constraints rather than repeat them>
- Assumptions and unresolved questions: <distinguish technical questions from user decisions>
- Architecture: <relevant ADR links; omit when unnecessary>

### TDD policy

- Level: unset | none | targeted | strict
- Selected by user: <request or standing preference; unset until selected>
- Test-first behaviors: <named behaviors for targeted; changed testable behavior for strict>
- Required regression coverage: <independent of test-first sequencing>

### Bug evidence

Optional; bug fixes only.

- Expected and observed behavior:
- Reproduction and impact: <steps, environment, frequency; unknowns explicit>
- Evidence and cause: <reported/reproduced; confirmed cause or hypothesis; links>

## Execution

Optional. Add steps when sequencing, dependencies, uncertainty, coordination, or recovery
makes them useful, when a long run's earlier context will be summarized before it finishes, or
when a plan is requested. Detail the next useful increment; keep later
steps concise. Revise the approach from evidence within the agreement and authorization. Reuse valid
results and update changed facts; do not add a log entry for every loop iteration.
An explicit planning-only request stops before implementation.

- Approach and open technical questions: <provisional; use experiments when needed>
- Verification: <confirmed commands or manual actions → expected results; label unverified checks>

### T1: <Bounded observable outcome>

Include tasks only when useful; a straightforward change needs no task list.

- Acceptance criteria: <IDs or exact references; do not restate requirements>
- Dependencies and interfaces: <required inputs/results and agreed shared contracts; omit when unnecessary>
- Scope and constraints: <confirmed paths versus proposed new paths when useful; ADR references>
- Verification: <command/action → expected result; include expected error status/output when applicable>
- Ownership: <delegated persona, write/check boundaries, expected evidence; omit for local work>
- [ ] Complete — evidence: <reference to actual results below; a completed task list alone is not success>

## Evidence

Record actual results even when no execution steps were needed. Link evidence owned elsewhere.

- Checks and outcomes: <expected and actual result; red/green when selected TDD requires it>
- Review: <findings, corrections and verification; independent reviewer or unmet requirement when required>
- Remaining verification and limitations: <failed, unrun, or environment-blocked checks>
- Changes: <relevant diff/paths; commit hash or uncommitted status when useful>

## Current handoff

Replace as work progresses. Keep authority here and evidence above rather than copying it.

- Authorized work: <scope and source; a listed task or proposed approach is not authorization>
- Completed and remaining work: <references; include blockers and pending decisions>
- Try it: <location, actions, expected result for user-visible work; omit when irrelevant>
- Human acceptance and delivery: <actual status and evidence when required>
- Recovery: <method and limitations for persistent-data or deployment work; omit when irrelevant>
- Resume context: <relevant paths/diff base and active ownership; omit when unnecessary>
- Correction rounds: <failure, consecutive and total counts, last material progress; omit when none>
- Next action: <owner, bounded action, required inputs, useful skill prompt if needed>
