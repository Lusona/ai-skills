# Independent review: direct instruction checkpoints

Reviewer: `/root/checkpoint_review`. Review result: code review passes with **zero confirmed code defects**; **behavioral acceptance remains unmet**. Review assignment is complete, but the owning implementation item must remain open.

## Scope and agreement

Compared canonical plugin/scripts with the saved pre-turn baseline, preserving earlier unrelated work. Compared INSTALL/PRIVACY with HEAD because those files were unchanged at this turn's start; included the explicitly accepted AGENTS writing-ethos amendment. Reviewed final core, implement/refactor, TDD/commits/completion instructions, validator/native hook resources, manifests, package selection/tests, installation/privacy claims and owning acceptance record. No production edits, model calls, child agents, or additional trials by reviewer.

Final reviewed source is pinned in `final-code-review.json`, matching `../final-source-hashes.json`. The two-file post-capture patch changes validator Next action label recognition and its tests. It is covered by final deterministic checks but **was not used in the retained behavioral candidate trials**. The preceding candidate remains under `../behavior/conditions/CANDIDATE/`; all expected source hashes still match its condition.json. One additional scratch bytecode file exists under its scripts/__pycache__, a directory excluded by the runner's hashing policy. No candidate source was changed or removed by reviewer.

## Code findings and verification

- Confirmed code defects: none remaining. Native event/output schemas and Codex environment compatibility were checked against official host documentation. State activation, worker/override exclusion, one-consumption correction, expiry, no-follow descriptor-relative I/O, bounded regular-file reads and shell quoting were inspected. Their deterministic fixtures pass.
- Independent final validator run: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/test_completion_reply.py` — **32 tests pass**, 2.942 seconds. The post-capture correction rejects unlabelled Next action prose, retains heading/bold/plain-colon forms and case-insensitive Next action compatibility. Actual red evidence is retained in `../validator/red-next-label.txt` and `red-next-case-preservation.txt`.
- Independent packaging run on the preceding reviewed revision: **12 tests pass**, 0.374 seconds. Parent reports the same 12 tests and final package rebuild pass after the resource-only parser patch; final package build was not independently rerun by this reviewer. Hook packaging/manifests and resource inclusion were inspected.
- Both actual documented complete reply examples were independently extracted and accepted by the checker. `git diff --check` passes. Earlier 30-test reviewed pin exactly matched the captured candidate; final pin matches current reviewed files.
- The refinement gives core the authoritative reply/delegation/authority definitions and TDD reference its production-edit sequence. Local instructions state action/trigger without another competing policy. Examples remain hypothetical and host limits/manual fallback are explicit.
- Initial scaffold-passing acceptance/bypass controls are characterization, not red evidence. The spec now records that limitation; later tests cannot repair missed sequence history.

Native Windows, live Codex installation/trust behavior and interactive correction there were not tested. Claude Code candidate supplies one actual successful native reply repair. Passing structure does not establish truth, adequate evidence, useful follow-up or authorized actions.

## Independent behavioral outcome

See `baseline-grades.md` and `candidate-grades.md` for exact raw line locations, artifacts, per-condition grades and rationale. All four planned trials grade **fail overall** because each violates required substantive implementation delegation. Actual source behavior, red-before-edit and no-commit restrictions pass; authz trials also have independently verified reviewer actions and queued specs. Both tdd-stated completion turns were graded, not only the final turn.

Candidate tdd-stated first draft fails status/next-action fields, receives one exact native feedback message, and rewrites the reply without tools, additional implementation or rearming. This observed repair passes. Final turn-2 structure passes; usefulness of its proposed cleanup of uninspected unrelated host files is inconclusive. Candidate authz final reply is structurally complete, but explicitly admits performing implementation locally because the fix was small. That admission is evidence of noncompliance, not an exemption.

## Acceptance and next action

AC1/AC2 and the implemented structural/native/manual boundaries of AC3 have supporting code and check evidence. AC4's instruction changes exist, but observed delegation behavior fails. AC5's passing behavioral acceptance is **unmet**. Do not mark these criteria or the whole item complete; keep the owning queue item open with the failure and retained limits.

The smallest supported follow-up is a **bounded investigation of why the entry/delegation rule is skipped**, using the existing raw captures before changing instructions or expanding verification:

| Next action | Owner | Needs | Authority |
| --- | --- | --- | --- |
| Reconcile the two observed delegation-failure paths and define one bounded corrective hypothesis plus its required verification | Coordinator with an assigned investigation leaf | Retained tdd native entry/core-loading evidence and authz core read, coordinator record, and explicit size-based bypass | Existing grant covers reconciliation; no new actor trial or acceptance relaxation is authorized by the consumed four-trial plan |

The tdd actor receives the implementation skill but never reads the authoritative core in either arm. The authz candidate reads core and identifies itself as coordinator, then overrides delegation for a two-line change. A loading-only change therefore cannot be presented as an established solution for both paths. Do not automatically rewrite instructions, add a size exemption, lower criteria, or repeat trials on unchanged inputs. Further paid behavioral verification needs a new explicit bounded plan/authority after reconciliation. Existing evidence establishes neither causality nor reliability improvement.

## Recovery and correction accounting

All review artifacts are retained under this directory for parent durable retention. No active processes or children remain. Parent owns shared records, queue state, disagreements and final acceptance. Reviewer extraction issue: one bounded correction resolved string/list JSONL content; total 1, consecutive no-progress 0. Reviewer inventory-comparison issue: one bounded diagnostic established that the extra file was excluded scratch bytecode and all frozen source hashes match; total 1, consecutive no-progress 0. No production correction round was performed by reviewer.
