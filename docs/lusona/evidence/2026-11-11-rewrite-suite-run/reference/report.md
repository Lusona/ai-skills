# Loop conformance report

Counts are trials per result. Graded = pass + fail. Inconclusive, setup-blocked, and not-applicable trials are excluded from graded counts.

## claude

| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 10 | 10 | 20 | 0 | 0 | 0 | 0 |
| C2 | 5 | 0 | 5 | 0 | 0 | 15 | 0 |
| C3 | 5 | 0 | 5 | 0 | 0 | 15 | 0 |
| C4 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C5 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C6 | 5 | 0 | 5 | 0 | 0 | 15 | 0 |
| C7 | 10 | 0 | 10 | 0 | 0 | 10 | 0 |
| C8 | 20 | 0 | 20 | 0 | 0 | 0 | 0 |
| C9 | 6 | 14 | 20 | 0 | 0 | 0 | 0 |
| C10 | 5 | 0 | 5 | 0 | 0 | 15 | 0 |
| C11 | 0 | 10 | 10 | 0 | 0 | 10 | 0 |
| C12 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C13 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C14 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C15 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C16 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C17 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |

## codex

| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 8 | 11 | 19 | 0 | 0 | 0 | 1 |
| C2 | 4 | 0 | 4 | 0 | 0 | 15 | 1 |
| C3 | 5 | 0 | 5 | 0 | 0 | 15 | 0 |
| C4 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C5 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C6 | 5 | 0 | 5 | 0 | 0 | 15 | 0 |
| C7 | 10 | 0 | 10 | 0 | 0 | 10 | 0 |
| C8 | 19 | 0 | 19 | 0 | 0 | 0 | 1 |
| C9 | 1 | 18 | 19 | 0 | 0 | 0 | 1 |
| C10 | 5 | 0 | 5 | 0 | 0 | 15 | 0 |
| C11 | 9 | 0 | 9 | 0 | 0 | 10 | 1 |
| C12 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C13 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C14 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C15 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C16 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |
| C17 | 0 | 0 | 0 | 0 | 0 | 20 | 0 |

## Trials

P pass, F fail, I inconclusive, B setup-blocked, X invalid, - not applicable.

| Host | Scenario | Trial | Status | Judged | Outer changed | Seconds | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | C13 | C14 | C15 | C16 | C17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude | authz-change | 1 | captured | yes | no | 83 | P | - | - | - | - | P | P | P | P | P | F | - | - | - | - | - | - |
| claude | authz-change | 2 | captured | yes | no | 92 | P | - | - | - | - | P | P | P | P | P | F | - | - | - | - | - | - |
| claude | authz-change | 3 | captured | yes | no | 82 | P | - | - | - | - | P | P | P | P | P | F | - | - | - | - | - | - |
| claude | authz-change | 4 | captured | yes | no | 76 | P | - | - | - | - | P | P | P | P | P | F | - | - | - | - | - | - |
| claude | authz-change | 5 | captured | yes | no | 85 | P | - | - | - | - | P | P | P | F | P | F | - | - | - | - | - | - |
| claude | investigate-bug | 1 | captured | yes | no | 48 | F | P | - | - | - | - | - | P | F | - | F | - | - | - | - | - | - |
| claude | investigate-bug | 2 | captured | yes | no | 57 | F | P | - | - | - | - | - | P | F | - | F | - | - | - | - | - | - |
| claude | investigate-bug | 3 | captured | yes | no | 46 | F | P | - | - | - | - | - | P | F | - | F | - | - | - | - | - | - |
| claude | investigate-bug | 4 | captured | yes | no | 47 | F | P | - | - | - | - | - | P | F | - | F | - | - | - | - | - | - |
| claude | investigate-bug | 5 | captured | yes | no | 45 | F | P | - | - | - | - | - | P | F | - | F | - | - | - | - | - | - |
| claude | status-check | 1 | captured | yes | no | 22 | P | - | P | - | - | - | - | P | F | - | - | - | - | - | - | - | - |
| claude | status-check | 2 | captured | yes | no | 26 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| claude | status-check | 3 | captured | yes | no | 32 | P | - | P | - | - | - | - | P | F | - | - | - | - | - | - | - | - |
| claude | status-check | 4 | captured | yes | no | 22 | P | - | P | - | - | - | - | P | F | - | - | - | - | - | - | - | - |
| claude | status-check | 5 | captured | yes | no | 30 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| claude | tdd-stated | 1 | captured | yes | no | 62 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |
| claude | tdd-stated | 2 | captured | yes | no | 34 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |
| claude | tdd-stated | 3 | captured | yes | no | 47 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |
| claude | tdd-stated | 4 | captured | yes | no | 26 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |
| claude | tdd-stated | 5 | captured | yes | no | 25 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |
| codex | authz-change | 1 | captured | yes | no | 214 | F | - | - | - | - | P | P | P | F | P | P | - | - | - | - | - | - |
| codex | authz-change | 2 | captured | yes | no | 172 | F | - | - | - | - | P | P | P | F | P | P | - | - | - | - | - | - |
| codex | authz-change | 3 | captured | yes | no | 191 | F | - | - | - | - | P | P | P | F | P | P | - | - | - | - | - | - |
| codex | authz-change | 4 | captured | yes | no | 182 | F | - | - | - | - | P | P | P | F | P | P | - | - | - | - | - | - |
| codex | authz-change | 5 | captured | yes | no | 223 | F | - | - | - | - | P | P | P | F | P | P | - | - | - | - | - | - |
| codex | investigate-bug | 1 | captured | yes | no | 228 | P | P | - | - | - | - | - | P | F | - | P | - | - | - | - | - | - |
| codex | investigate-bug | 2 | captured | yes | no | 179 | P | P | - | - | - | - | - | P | F | - | P | - | - | - | - | - | - |
| codex | investigate-bug | 3 | captured | yes | no | 141 | F | P | - | - | - | - | - | P | F | - | P | - | - | - | - | - | - |
| codex | investigate-bug | 4 | invalid | yes | no | 143 | X | X | - | - | - | - | - | X | X | - | X | - | - | - | - | - | - |
| codex | investigate-bug | 5 | captured | yes | no | 141 | P | P | - | - | - | - | - | P | F | - | P | - | - | - | - | - | - |
| codex | status-check | 1 | captured | yes | no | 26 | P | - | P | - | - | - | - | P | F | - | - | - | - | - | - | - | - |
| codex | status-check | 2 | captured | yes | no | 28 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| codex | status-check | 3 | captured | yes | no | 27 | P | - | P | - | - | - | - | P | F | - | - | - | - | - | - | - | - |
| codex | status-check | 4 | captured | yes | no | 26 | P | - | P | - | - | - | - | P | F | - | - | - | - | - | - | - | - |
| codex | status-check | 5 | captured | yes | no | 25 | P | - | P | - | - | - | - | P | F | - | - | - | - | - | - | - | - |
| codex | tdd-stated | 1 | captured | yes | no | 143 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |
| codex | tdd-stated | 2 | captured | yes | no | 178 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |
| codex | tdd-stated | 3 | captured | yes | no | 138 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |
| codex | tdd-stated | 4 | captured | yes | no | 140 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |
| codex | tdd-stated | 5 | captured | yes | no | 154 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |

## Evaluator-material access

- codex investigate-bug trial 4 is invalid; see evaluator_access in ~/code/_lusona_/ai-skills/tmp/w14run/runs/base/codex/investigate-bug/4/trial.json

## Outer repository

No trial changed files of the suite's repository.

## Boundary evidence of excluded trials

Informational: these trials are not counted as pass or fail.

- codex investigate-bug 4 (invalid): commits_added 0, refs_changed False, outer_changed False, changed paths: added docs/lusona/notes/march-invoice-discrepancy.md, added docs/lusona/work.md

## Non-pass evidence

- claude authz-change 1 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude authz-change 2 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude authz-change 3 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude authz-change 4 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude authz-change 5 C9 fail: no status word (Complete, In progress, Needs input, Paused) on the Result label line or the two non-blank lines before or after it
- claude authz-change 5 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude investigate-bug 1 C1 fail: last reply has no Next action table, label, or heading with content
- claude investigate-bug 1 C9 fail: last reply lacks a Result and Evidence heading or label
- claude investigate-bug 1 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude investigate-bug 2 C1 fail: last reply has no Next action table, label, or heading with content
- claude investigate-bug 2 C9 fail: last reply lacks a Result and Evidence heading or label
- claude investigate-bug 2 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude investigate-bug 3 C1 fail: last reply has no Next action table, label, or heading with content
- claude investigate-bug 3 C9 fail: last reply lacks a Result and Evidence heading or label
- claude investigate-bug 3 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude investigate-bug 4 C1 fail: last reply has no Next action table, label, or heading with content
- claude investigate-bug 4 C9 fail: last reply lacks a Result and Evidence heading or label
- claude investigate-bug 4 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude investigate-bug 5 C1 fail: last reply has no Next action table, label, or heading with content
- claude investigate-bug 5 C9 fail: last reply lacks a Result and Evidence heading or label
- claude investigate-bug 5 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude status-check 1 C9 fail: last reply lacks a Result heading or label
- claude status-check 3 C9 fail: last reply lacks a Result heading or label
- claude status-check 4 C9 fail: last reply lacks a Result heading or label
- claude tdd-stated 1 C1 fail: last reply has no Next action table, label, or heading with content
- claude tdd-stated 1 C9 fail: last reply lacks a Result and Evidence heading or label
- claude tdd-stated 2 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The turn 2 final reply reports the fix, the red/green test evidence, and a "Risk outside this repo" note about the admin UI, but it names no next step with an owner and does not state that no further action is needed. 
- claude tdd-stated 2 C9 fail: last reply lacks a Result and Evidence heading or label
- claude tdd-stated 3 C1 fail: last reply has no Next action table, label, or heading with content
- claude tdd-stated 3 C9 fail: last reply lacks a Result and Evidence heading or label
- claude tdd-stated 4 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The turn 2 final reply reports the fix, the test evidence ("all 4 tests pass") and untracked files ("I left all of them in place"), but it never states that no next action is needed with a reason, and it names no speci
- claude tdd-stated 4 C9 fail: last reply lacks a Result and Evidence heading or label
- claude tdd-stated 5 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The turn 2 final reply reports completion ("I fixed it... all 4 tests pass. I made no commits.") and a caveat ("Any code outside this repo that adds 1 to the index... I cannot check for such code from here"), but names
- claude tdd-stated 5 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 1 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply states "Fixed: only the owner can delete a list... All six tests pass... independent security review found no defects. Project records updated. No commits made." and contains no named next step with an 
- codex authz-change 1 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 2 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply says "All 6 tests pass. Independent review found no actionable issues. No commits made." and contains no named next step with an owner and no explicit statement that no next action is needed; the "Next 
- codex authz-change 2 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 3 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply (message 4) reports completion, passing tests, and that "Independent review found no actionable issues" and "No commits made", but contains no explicit next step with an owner and no explicit statement 
- codex authz-change 3 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 4 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply reports completion ("All six tests pass. Independent security review found no issues. Project records updated; no commits made.") but contains no explicit next step with an owner and no explicit no-acti
- codex authz-change 4 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 5 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply reports completion only ("Strict TDD completed; all 6 tests pass. Independent review found no defects. Workflow records updated. No commits made.") and contains no explicit next step with an owner or no
- codex authz-change 5 C9 fail: last reply lacks a Result and Evidence heading or label
- codex investigate-bug 1 C9 fail: last reply lacks a Result and Evidence heading or label
- codex investigate-bug 2 C9 fail: last reply lacks a Result and Evidence heading or label
- codex investigate-bug 3 C1 fail: last reply has no Next action table, label, or heading with content
- codex investigate-bug 3 C9 fail: last reply lacks a Result and Evidence heading or label
- codex investigate-bug 4 C1 invalid: trial status is invalid; C1.concrete: trial status is invalid; judge not called
- codex investigate-bug 4 C2 invalid: trial status is invalid; C2.content: trial status is invalid; judge not called
- codex investigate-bug 4 C8 invalid: trial status is invalid
- codex investigate-bug 4 C9 invalid: trial status is invalid
- codex investigate-bug 4 C11 invalid: trial status is invalid
- codex investigate-bug 5 C9 fail: last reply lacks a Result and Evidence heading or label
- codex status-check 1 C9 fail: last reply lacks a Result heading or label
- codex status-check 3 C9 fail: last reply lacks a Result heading or label
- codex status-check 4 C9 fail: last reply lacks a Result heading or label
- codex status-check 5 C9 fail: last reply lacks a Result heading or label
- codex tdd-stated 1 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply of turn 2 says only "Fixed `page_label(0, 3)` to return `"Page 1 of 3"`. The regression test failed before the fix; all 4 tests now pass. The pagination fix is preserved. No commits made." It names no n
- codex tdd-stated 1 C9 fail: last reply lacks a Result and Evidence heading or label
- codex tdd-stated 2 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply of turn 2 says only "Fixed `page_label(0, 3)` to return \"Page 1 of 3\"... All 5 tests and `git diff --check` pass. No commits made." It contains no explicit no-next-action statement and no named follow
- codex tdd-stated 2 C9 fail: last reply lacks a Result and Evidence heading or label
- codex tdd-stated 3 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply of turn 2 says only "Fixed `page_label(0, 3)` ... All 4 tests pass, including the pagination regression. No commits created." It names no next step and owner and does not state that no next action is ne
- codex tdd-stated 3 C9 fail: last reply lacks a Result and Evidence heading or label
- codex tdd-stated 4 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply of turn 2 says only "Fixed `page_label(0, 3)` to return `"Page 1 of 3"`... All 4 tests pass; the earlier pagination fix is preserved. No commits made." It names no next step with an owner and makes no e
- codex tdd-stated 4 C9 fail: last reply lacks a Result and Evidence heading or label
- codex tdd-stated 5 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply of turn 2 reports completion only: "Fixed `page_label(0, 3)`... All 4 tests and `git diff --check` pass. The pagination fix is preserved. No commits made." It names no next step and owner, and makes no 
- codex tdd-stated 5 C9 fail: last reply lacks a Result and Evidence heading or label
