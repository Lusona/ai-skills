# TDD and verification

Read when selecting, recording, or applying a TDD policy.

Implementation requires explicit user selection or a standing preference, with no implicit default.
A standing preference is recorded in the project's `docs/lusona/README.md` or its agent
instructions (`CLAUDE.md` or `AGENTS.md`). Record selection and source in the owning change
record or conversation. Unset TDD permits definition
and planning, not implementation; no definition phase is required for a clear request. When unset,
recommend a level and ask through the contract's question guidance.

| Level | Requirement |
| --- | --- |
| `none` | No test-first requirement; agreed verification and repository checks still apply |
| `targeted` | Test first for named behaviors |
| `strict` | Test first for every new or changed testable behavior |

- For targeted TDD, name the test-first behaviors. Required regression coverage is separate
  from test-first sequencing.
- For test-first behaviors, observe the intended failure before production changes, then verify
  passing behavior. Record red/green evidence; setup failures and skipped failing runs are not red
  evidence. Under `none`, run agreed checks and add coverage when it usefully verifies the change
  or is required.
- Test through observable interfaces. Reuse adequate coverage; avoid tests that merely mirror the
  implementation, and do not weaken assertions to fit a new structure.
- Behavior-preserving restructuring starts green and stays green. Under targeted or strict TDD,
  first add missing coverage for the affected boundary; characterization tests pass on existing
  behavior and must exercise the relevant path. Do not manufacture a failing test or claim a
  red/green cycle.
- If the selected sequence is infeasible, obtain a revised policy before substituting another
  approach. Do not silently change agreed TDD to fit an approach.

Implementation owns decomposition and evidence; refactoring owns behavior-preserving checks.
Reuse valid checks when inputs are unchanged; broaden or repeat them only for changed inputs,
failures, or concrete unresolved risks.
