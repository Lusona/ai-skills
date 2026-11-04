# Evidence: realign instructions with goals

Question: does the change for
[Realign instructions with goals](../../specs/20261103-realign-instructions-with-goals.md)
reduce what each role loads and remove restated rules, without weakening any boundary rule?
Decision informed: acceptance of AC2, AC4, AC6, and AC7.

## Runs

| Run | File | Content |
| --- | --- | --- |
| Baseline | [baseline.md](baseline.md) | Words loaded per role before edits, HEAD 545b6e0, clean plugin tree; file hashes |
| Red | [red.md](red.md) | AC2/AC4 checks failing against the baseline sources: 27 restated clauses in 13 skills, routing table missing from the guide and present in status; 6 fixture tests passing |
| Green | [green.md](green.md) | Instruction tests, checker, package tests, work-record tests, package build, native validation, whitespace, and link checks after edits, plus the recheck after review corrections |
| After | [after.md](after.md) | Words loaded per role after edits and review corrections, same method, with the new handoff reference added to the coordinator set |

Method: [measure.py](measure.py). Words are whitespace-separated tokens, the unit of `wc -w`.
Core sections are split on level-2 headings. The scenario is a spec-linked `implement` with one
delegated worker, no failures, and no spec creation; the file lists are in the script. The
coordinator's after run adds `references/handoff.md` because the coordinator reads it before the
handoff at the end of an implement (spec decision, 2026-11-03).

## Result

| Measure | Before | After |
| --- | --- | --- |
| Coordinator, representative implement | 6,277 | 5,993 |
| Worker, representative implement | 3,607 | 3,195 |
| Core sections required for every role | 1,309 | 1,157 |
| Core README, all sections | 1,640 | 1,358 |
| Fourteen skills together | 9,203 | 7,438 |
| All plugin Markdown files | 26,787 in 47 files | 25,435 in 49 files |
| Restated core clauses in skills (checker) | 27 single-line; 29 with wrapped-line matching | 0 |
| Files holding a routing table | 2 (status, none in guide) | 1 (guide) |

## Interpretation and limits

- The worker set fell more than the coordinator set because the coordinator still reads every
  reference before dispatch and before commit, and retention grew by 84 words to own the
  proportional-records rule once.
- Word counts are not token counts, latency, or cost. No such claim is made.
- The checker's phrase list is a floor for AC2; the independent review covers restatements in
  other words.
- Static checks only. No agent behavior trials were run; the change is intended to be
  behavior-preserving, and the review checks that every removed sentence has a retained owner.
- Independent review (fresh read-only agent, given the diff, the agreement, and this evidence):
  AC1–AC7 met; no removed sentence without a retained owner. Two P2 text defects were corrected
  (stale Work loop cross-reference in the core's Personas section; root README still describing
  saving "even for small work"). Observations kept as is: frame-product and map-capabilities
  express the brief/map rule as a conditional owned by the core's "ask before unauthorized
  changes to accepted outcomes"; templates restate retention's three spec triggers because
  copied templates cannot link plugin files; the checker's routing detection needs a matching
  header, so it is a floor.
- User review, second round: three general clauses still duplicated the core (experiment's
  scope-change approval, implement's user-visible verification and documentation update,
  architect's ADR requirement); removed, specialist procedure kept. The checker missed phrases
  wrapped across lines; it now matches across whitespace with two regression tests, and finds
  29 restatements in the baseline sources instead of 27 (`git stash` of tracked edits, new
  checker). The recheck appears at the end of green.md.
