# TDD and verification

Read when selecting, recording or applying a TDD level.

## Selection

- Implementation requires a level selected explicitly by the user or a standing preference. There is no implicit default.
- A standing preference is recorded in the project's `docs/lusona/README.md` or in its agent instructions (`CLAUDE.md` or `AGENTS.md`).
- Record the level and its source in the owning change record. When saving is prevented, state them in the reply.
- While the level is unset, define and plan only. A request that states its intended behavior and scope needs no definition first.
- When the level is unset, recommend a level and ask the user.
- When the selected sequence is infeasible, obtain a revised level from the user before using another approach.
- Do not change the selected level to fit an approach.

| Level | Requirement |
| --- | --- |
| `none` | No test-first requirement; agreed verification and repository checks still apply |
| `targeted` | Test first for named behaviors |
| `strict` | Test first for every new or changed testable behavior |

## Applying the level

- Under `targeted`, name the test-first behaviors.
- Required regression coverage is separate from test-first sequencing.
- For each test-first behavior, observe the intended failure before changing production code. Then verify the passing behavior.
- Record red and green evidence. A setup failure or a skipped failing run is not red evidence.
- Under `none`, run the agreed checks. Add coverage when the agreement requires it or no existing check exercises the change.
- Test through observable interfaces.
- Reuse existing coverage that exercises the change.
- Do not write tests that only restate the implementation.
- Do not weaken assertions to fit a new structure.

## Behavior-preserving changes

- A behavior-preserving restructuring starts green and stays green.
- Under `targeted` or `strict`, first add missing coverage for the affected boundary.
- A characterization test passes on existing behavior and exercises the affected path.
- Do not write a test only to obtain a failing run. Do not claim a red/green cycle that did not occur.

## Ownership and reuse

- Reuse a valid check result when its inputs are unchanged.
- Broaden or repeat a check only for changed inputs, failures or a named unresolved risk.
