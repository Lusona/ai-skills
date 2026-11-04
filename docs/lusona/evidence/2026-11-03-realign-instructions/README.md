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
| After (historical) | [after.md](after.md) | Earlier dirty-tree observation, HEAD 545b6e0; preserved with its original file hashes |
| Final reviewed revision | [final-ea99970.md](final-ea99970.md) | Complete measure.py output for clean plugin revision ea99970, plus pinned baseline/final skill, checker, and routing counts |

Method: [measure.py](measure.py). Words are whitespace-separated tokens, the unit of `wc -w`.
Core sections are split on level-2 headings. The scenario is a spec-linked `implement` with one
delegated worker, no failures, and no spec creation; the file lists are in the script. The
coordinator's after run adds `references/handoff.md` because the coordinator reads it before the
handoff at the end of an implement (spec decision, 2026-11-03).

## Result

The current comparable result is baseline 545b6e0 versus final reviewed revision ea99970.
Role counts and plugin totals are in [baseline.md](baseline.md) and
[final-ea99970.md](final-ea99970.md); the final run's supplemental pinned-revision table
verifies every summary row, including whole-file, skill, checker, and routing counts.
The chronologically earlier dirty-tree run [after.md](after.md) remains historical evidence.

| Measure | Baseline 545b6e0 | Final ea99970 |
| --- | --- | --- |
| Coordinator, representative implement | 6,277 | 6,036 |
| Worker, representative implement | 3,607 | 3,239 |
| Core sections required for every role | 1,309 | 1,194 |
| Core README, all sections and preamble | 1,675 | 1,566 |
| Fourteen skills together | 9,203 | 7,446 |
| All plugin Markdown files | 26,787 in 47 files | 25,482 in 48 files |
| Restated core clauses in skills (revised wrapped-line checker) | 29 | 0 |
| Routing table occurrences (checker) | 1 (status; none in guide) | 1 (guide) |

The original single-line checker found 27 baseline restatements in [red.md](red.md).
Its 29 total findings include two table-ownership findings; that total is distinct from the
revised checker's 29 restatement matches. The final run retains the revised comparison method.

## Summary correction, 2026-11-03

The previous summary mixed earlier observations with unsupported or mislabeled values. The
historical run files remain unchanged; this correction uses a new run pinned to the reviewed
revision rather than replacing their observations. The exact cause of each stale value is
not established.

| Previous summary claim | Correction and evidence |
| --- | --- |
| After coordinator 5,993; worker 3,195; required core 1,157 | These match the earlier dirty-tree [after.md](after.md); final ea99970 is 6,036; 3,239; 1,194. |
| Whole core README before 1,640; after 1,358 | Baseline 1,640 counts section bodies only, excluding headings and preamble. Whole-file baseline is 1,675. The historical after run reports whole-file 1,529 and section bodies 1,494, so it does not support 1,358. Final whole-file count is 1,566. |
| After fourteen skills 7,438 | Pinned final total is 7,446. The old summary did not identify a supporting run for 7,438. |
| After all Markdown 25,435 in 49 files | Historical after output is 25,408 in 48 files; final is 25,482 in 48 files. Neither supports the old summary pair. |
| Baseline two files holding a routing table | Revised checker on pinned baseline finds one occurrence in status; final finds one in the guide. |

Correction round 1 resolved the summary inconsistency with a new pinned run and verification of
every table value; consecutive rounds without material progress: 0; total correction rounds: 1.

## Interpretation and limits

- The worker set fell by 368 words and the coordinator set by 241 under the declared scenario.
  The coordinator manifest includes whole references and the added handoff reference; retention
  is 877 words at final ea99970 versus 803 at baseline, an increase of 74. This scenario does
  not imply that every reference is loaded before every dispatch or commit.
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
