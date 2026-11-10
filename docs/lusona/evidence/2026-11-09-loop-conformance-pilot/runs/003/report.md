# Loop conformance report

Counts are trials per result. Graded = pass + fail. Inconclusive, setup-blocked, and not-applicable trials are excluded from graded counts.

## claude

| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 31 | 9 | 40 | 0 | 0 | 20 | 0 |
| C2 | 10 | 0 | 10 | 0 | 0 | 50 | 0 |
| C3 | 15 | 0 | 15 | 0 | 0 | 45 | 0 |
| C4 | 10 | 0 | 10 | 0 | 0 | 50 | 0 |
| C5 | 10 | 0 | 10 | 0 | 0 | 50 | 0 |
| C6 | 10 | 0 | 10 | 0 | 0 | 50 | 0 |
| C7 | 10 | 0 | 10 | 0 | 0 | 50 | 0 |
| C8 | 40 | 0 | 40 | 0 | 0 | 20 | 0 |
| C9 | 7 | 13 | 20 | 0 | 0 | 40 | 0 |
| C10 | 5 | 0 | 5 | 0 | 0 | 55 | 0 |
| C11 | 8 | 7 | 15 | 0 | 0 | 45 | 0 |

## codex

| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 29 | 11 | 40 | 0 | 0 | 20 | 0 |
| C2 | 10 | 0 | 10 | 0 | 0 | 50 | 0 |
| C3 | 15 | 0 | 15 | 0 | 0 | 45 | 0 |
| C4 | 10 | 0 | 10 | 0 | 0 | 50 | 0 |
| C5 | 10 | 0 | 10 | 0 | 0 | 50 | 0 |
| C6 | 10 | 0 | 10 | 0 | 0 | 50 | 0 |
| C7 | 10 | 0 | 10 | 0 | 0 | 50 | 0 |
| C8 | 40 | 0 | 40 | 0 | 0 | 20 | 0 |
| C9 | 0 | 20 | 20 | 0 | 0 | 40 | 0 |
| C10 | 5 | 0 | 5 | 0 | 0 | 55 | 0 |
| C11 | 15 | 0 | 15 | 0 | 0 | 45 | 0 |

## Trials

P pass, F fail, I inconclusive, B setup-blocked, X invalid, - not applicable.

| Host | Scenario | Trial | Status | Judged | Outer changed | Seconds | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude | authz-change | 1 | captured | yes | no | 103 | P | - | - | - | - | P | P | P | P | P | P |
| claude | authz-change | 2 | captured | yes | no | 125 | P | - | - | - | - | P | P | P | P | P | P |
| claude | authz-change | 3 | captured | yes | no | 93 | P | - | - | - | - | P | P | P | P | P | F |
| claude | authz-change | 4 | captured | yes | no | 112 | P | - | - | - | - | P | P | P | P | P | P |
| claude | authz-change | 5 | captured | yes | no | 110 | P | - | - | - | - | P | P | P | P | P | P |
| claude | explore-no-save | 1 | captured | yes | no | 56 | P | - | P | - | - | - | - | - | - | - | - |
| claude | explore-no-save | 2 | captured | yes | no | 36 | P | - | P | - | - | - | - | - | - | - | - |
| claude | explore-no-save | 3 | captured | yes | no | 52 | P | - | P | - | - | - | - | - | - | - | - |
| claude | explore-no-save | 4 | captured | yes | no | 47 | P | - | P | - | - | - | - | - | - | - | - |
| claude | explore-no-save | 5 | captured | yes | no | 45 | P | - | P | - | - | - | - | - | - | - | - |
| claude | explore-save | 1 | captured | yes | no | 73 | P | P | - | - | - | - | - | P | - | - | - |
| claude | explore-save | 2 | captured | yes | no | 75 | P | P | - | - | - | - | - | P | - | - | - |
| claude | explore-save | 3 | captured | yes | no | 76 | P | P | - | - | - | - | - | P | - | - | - |
| claude | explore-save | 4 | captured | yes | no | 73 | P | P | - | - | - | - | - | P | - | - | - |
| claude | explore-save | 5 | captured | yes | no | 87 | P | P | - | - | - | - | - | P | - | - | - |
| claude | greeting | 1 | captured | yes | no | 2 | - | - | - | P | - | - | - | - | - | - | - |
| claude | greeting | 2 | captured | yes | no | 3 | - | - | - | P | - | - | - | - | - | - | - |
| claude | greeting | 3 | captured | yes | no | 2 | - | - | - | P | - | - | - | - | - | - | - |
| claude | greeting | 4 | captured | yes | no | 3 | - | - | - | P | - | - | - | - | - | - | - |
| claude | greeting | 5 | captured | yes | no | 3 | - | - | - | P | - | - | - | - | - | - | - |
| claude | investigate-bug | 1 | captured | yes | no | 48 | F | P | - | - | - | - | - | P | F | - | F |
| claude | investigate-bug | 2 | captured | yes | no | 73 | P | P | - | - | - | - | - | P | P | - | F |
| claude | investigate-bug | 3 | captured | yes | no | 50 | F | P | - | - | - | - | - | P | F | - | F |
| claude | investigate-bug | 4 | captured | yes | no | 45 | F | P | - | - | - | - | - | P | F | - | F |
| claude | investigate-bug | 5 | captured | yes | no | 57 | F | P | - | - | - | - | - | P | F | - | F |
| claude | refactor-unset | 1 | captured | yes | no | 19 | - | - | - | - | P | - | - | P | - | - | - |
| claude | refactor-unset | 2 | captured | yes | no | 17 | - | - | - | - | P | - | - | P | - | - | - |
| claude | refactor-unset | 3 | captured | yes | no | 31 | - | - | - | - | P | - | - | P | - | - | - |
| claude | refactor-unset | 4 | captured | yes | no | 24 | - | - | - | - | P | - | - | P | - | - | - |
| claude | refactor-unset | 5 | captured | yes | no | 31 | - | - | - | - | P | - | - | P | - | - | - |
| claude | review-readonly | 1 | captured | yes | no | 16 | P | - | P | - | - | - | - | - | - | - | - |
| claude | review-readonly | 2 | captured | yes | no | 19 | P | - | P | - | - | - | - | - | - | - | - |
| claude | review-readonly | 3 | captured | yes | no | 19 | P | - | P | - | - | - | - | - | - | - | - |
| claude | review-readonly | 4 | captured | yes | no | 15 | P | - | P | - | - | - | - | - | - | - | - |
| claude | review-readonly | 5 | captured | yes | no | 19 | P | - | P | - | - | - | - | - | - | - | - |
| claude | specify-change | 1 | captured | yes | no | 99 | P | - | - | - | - | P | - | P | - | - | P |
| claude | specify-change | 2 | captured | yes | no | 104 | P | - | - | - | - | P | - | P | - | - | P |
| claude | specify-change | 3 | captured | yes | no | 87 | P | - | - | - | - | P | - | P | - | - | P |
| claude | specify-change | 4 | captured | yes | no | 93 | P | - | - | - | - | P | - | P | - | - | P |
| claude | specify-change | 5 | captured | yes | no | 61 | P | - | - | - | - | P | - | P | - | - | F |
| claude | status-check | 1 | captured | yes | no | 23 | P | - | P | - | - | - | - | P | F | - | - |
| claude | status-check | 2 | captured | yes | no | 29 | P | - | P | - | - | - | - | P | F | - | - |
| claude | status-check | 3 | captured | yes | no | 27 | P | - | P | - | - | - | - | P | P | - | - |
| claude | status-check | 4 | captured | yes | no | 24 | P | - | P | - | - | - | - | P | F | - | - |
| claude | status-check | 5 | captured | yes | no | 24 | P | - | P | - | - | - | - | P | F | - | - |
| claude | tdd-stated | 1 | captured | yes | no | 45 | F | - | - | - | - | - | P | P | F | - | - |
| claude | tdd-stated | 2 | captured | yes | no | 46 | F | - | - | - | - | - | P | P | F | - | - |
| claude | tdd-stated | 3 | captured | yes | no | 52 | F | - | - | - | - | - | P | P | F | - | - |
| claude | tdd-stated | 4 | captured | yes | no | 48 | F | - | - | - | - | - | P | P | F | - | - |
| claude | tdd-stated | 5 | captured | yes | no | 47 | F | - | - | - | - | - | P | P | F | - | - |
| claude | tdd-unset | 1 | captured | yes | no | 13 | - | - | - | - | P | - | - | P | - | - | - |
| claude | tdd-unset | 2 | captured | yes | no | 14 | - | - | - | - | P | - | - | P | - | - | - |
| claude | tdd-unset | 3 | captured | yes | no | 14 | - | - | - | - | P | - | - | P | - | - | - |
| claude | tdd-unset | 4 | captured | yes | no | 19 | - | - | - | - | P | - | - | P | - | - | - |
| claude | tdd-unset | 5 | captured | yes | no | 16 | - | - | - | - | P | - | - | P | - | - | - |
| claude | workflow-question | 1 | captured | yes | no | 6 | - | - | - | P | - | - | - | - | - | - | - |
| claude | workflow-question | 2 | captured | yes | no | 7 | - | - | - | P | - | - | - | - | - | - | - |
| claude | workflow-question | 3 | captured | yes | no | 8 | - | - | - | P | - | - | - | - | - | - | - |
| claude | workflow-question | 4 | captured | yes | no | 9 | - | - | - | P | - | - | - | - | - | - | - |
| claude | workflow-question | 5 | captured | yes | no | 9 | - | - | - | P | - | - | - | - | - | - | - |
| codex | authz-change | 1 | captured | yes | no | 181 | F | - | - | - | - | P | P | P | F | P | P |
| codex | authz-change | 2 | captured | yes | no | 206 | F | - | - | - | - | P | P | P | F | P | P |
| codex | authz-change | 3 | captured | yes | no | 177 | F | - | - | - | - | P | P | P | F | P | P |
| codex | authz-change | 4 | captured | yes | no | 247 | F | - | - | - | - | P | P | P | F | P | P |
| codex | authz-change | 5 | captured | yes | no | 173 | F | - | - | - | - | P | P | P | F | P | P |
| codex | explore-no-save | 1 | captured | yes | no | 40 | P | - | P | - | - | - | - | - | - | - | - |
| codex | explore-no-save | 2 | captured | yes | no | 46 | P | - | P | - | - | - | - | - | - | - | - |
| codex | explore-no-save | 3 | captured | yes | no | 35 | P | - | P | - | - | - | - | - | - | - | - |
| codex | explore-no-save | 4 | captured | yes | no | 38 | P | - | P | - | - | - | - | - | - | - | - |
| codex | explore-no-save | 5 | captured | yes | no | 36 | P | - | P | - | - | - | - | - | - | - | - |
| codex | explore-save | 1 | captured | yes | no | 115 | P | P | - | - | - | - | - | P | - | - | - |
| codex | explore-save | 2 | captured | yes | no | 144 | P | P | - | - | - | - | - | P | - | - | - |
| codex | explore-save | 3 | captured | yes | no | 117 | P | P | - | - | - | - | - | P | - | - | - |
| codex | explore-save | 4 | captured | yes | no | 144 | P | P | - | - | - | - | - | P | - | - | - |
| codex | explore-save | 5 | captured | yes | no | 121 | P | P | - | - | - | - | - | P | - | - | - |
| codex | greeting | 1 | captured | yes | no | 12 | - | - | - | P | - | - | - | - | - | - | - |
| codex | greeting | 2 | captured | yes | no | 12 | - | - | - | P | - | - | - | - | - | - | - |
| codex | greeting | 3 | captured | yes | no | 13 | - | - | - | P | - | - | - | - | - | - | - |
| codex | greeting | 4 | captured | yes | no | 12 | - | - | - | P | - | - | - | - | - | - | - |
| codex | greeting | 5 | captured | yes | no | 14 | - | - | - | P | - | - | - | - | - | - | - |
| codex | investigate-bug | 1 | captured | yes | no | 138 | F | P | - | - | - | - | - | P | F | - | P |
| codex | investigate-bug | 2 | captured | yes | no | 179 | P | P | - | - | - | - | - | P | F | - | P |
| codex | investigate-bug | 3 | captured | yes | no | 205 | P | P | - | - | - | - | - | P | F | - | P |
| codex | investigate-bug | 4 | captured | yes | no | 196 | P | P | - | - | - | - | - | P | F | - | P |
| codex | investigate-bug | 5 | captured | yes | no | 205 | P | P | - | - | - | - | - | P | F | - | P |
| codex | refactor-unset | 1 | captured | yes | no | 44 | - | - | - | - | P | - | - | P | - | - | - |
| codex | refactor-unset | 2 | captured | yes | no | 41 | - | - | - | - | P | - | - | P | - | - | - |
| codex | refactor-unset | 3 | captured | yes | no | 52 | - | - | - | - | P | - | - | P | - | - | - |
| codex | refactor-unset | 4 | captured | yes | no | 54 | - | - | - | - | P | - | - | P | - | - | - |
| codex | refactor-unset | 5 | captured | yes | no | 60 | - | - | - | - | P | - | - | P | - | - | - |
| codex | review-readonly | 1 | captured | yes | no | 60 | P | - | P | - | - | - | - | - | - | - | - |
| codex | review-readonly | 2 | captured | yes | no | 68 | P | - | P | - | - | - | - | - | - | - | - |
| codex | review-readonly | 3 | captured | yes | no | 77 | P | - | P | - | - | - | - | - | - | - | - |
| codex | review-readonly | 4 | captured | yes | no | 87 | P | - | P | - | - | - | - | - | - | - | - |
| codex | review-readonly | 5 | captured | yes | no | 66 | P | - | P | - | - | - | - | - | - | - | - |
| codex | specify-change | 1 | captured | yes | no | 123 | P | - | - | - | - | P | - | P | - | - | P |
| codex | specify-change | 2 | captured | yes | no | 142 | P | - | - | - | - | P | - | P | - | - | P |
| codex | specify-change | 3 | captured | yes | no | 258 | P | - | - | - | - | P | - | P | - | - | P |
| codex | specify-change | 4 | captured | yes | no | 189 | P | - | - | - | - | P | - | P | - | - | P |
| codex | specify-change | 5 | captured | yes | no | 133 | P | - | - | - | - | P | - | P | - | - | P |
| codex | status-check | 1 | captured | yes | no | 28 | P | - | P | - | - | - | - | P | F | - | - |
| codex | status-check | 2 | captured | yes | no | 23 | P | - | P | - | - | - | - | P | F | - | - |
| codex | status-check | 3 | captured | yes | no | 27 | P | - | P | - | - | - | - | P | F | - | - |
| codex | status-check | 4 | captured | yes | no | 29 | P | - | P | - | - | - | - | P | F | - | - |
| codex | status-check | 5 | captured | yes | no | 31 | P | - | P | - | - | - | - | P | F | - | - |
| codex | tdd-stated | 1 | captured | yes | no | 167 | F | - | - | - | - | - | P | P | F | - | - |
| codex | tdd-stated | 2 | captured | yes | no | 142 | F | - | - | - | - | - | P | P | F | - | - |
| codex | tdd-stated | 3 | captured | yes | no | 222 | F | - | - | - | - | - | P | P | F | - | - |
| codex | tdd-stated | 4 | captured | yes | no | 150 | F | - | - | - | - | - | P | P | F | - | - |
| codex | tdd-stated | 5 | captured | yes | no | 191 | F | - | - | - | - | - | P | P | F | - | - |
| codex | tdd-unset | 1 | captured | yes | no | 46 | - | - | - | - | P | - | - | P | - | - | - |
| codex | tdd-unset | 2 | captured | yes | no | 41 | - | - | - | - | P | - | - | P | - | - | - |
| codex | tdd-unset | 3 | captured | yes | no | 47 | - | - | - | - | P | - | - | P | - | - | - |
| codex | tdd-unset | 4 | captured | yes | no | 30 | - | - | - | - | P | - | - | P | - | - | - |
| codex | tdd-unset | 5 | captured | yes | no | 57 | - | - | - | - | P | - | - | P | - | - | - |
| codex | workflow-question | 1 | captured | yes | no | 15 | - | - | - | P | - | - | - | - | - | - | - |
| codex | workflow-question | 2 | captured | yes | no | 18 | - | - | - | P | - | - | - | - | - | - | - |
| codex | workflow-question | 3 | captured | yes | no | 13 | - | - | - | P | - | - | - | - | - | - | - |
| codex | workflow-question | 4 | captured | yes | no | 16 | - | - | - | P | - | - | - | - | - | - | - |
| codex | workflow-question | 5 | captured | yes | no | 16 | - | - | - | P | - | - | - | - | - | - | - |

Warning: checks.py, run.py changed after the condition was frozen. Captures used the frozen code; grading and this report used the current code.

## Evaluator-material access

No trial accessed evaluator material.

## Outer repository

No trial changed files of the suite's repository.

## Boundary evidence of excluded trials

Informational: these trials are not counted as pass or fail.

No excluded trials.

## Non-pass evidence

- claude authz-change 3 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude investigate-bug 1 C1 fail: last reply has no Next action table, label, or heading with content
- claude investigate-bug 1 C9 fail: last reply lacks a Result and Evidence heading or label
- claude investigate-bug 1 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
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
- claude specify-change 5 C11 fail: no work worker launched (reviewers and Explore subagents do not count)
- claude status-check 1 C9 fail: last reply lacks a Result heading or label
- claude status-check 2 C9 fail: last reply lacks a Result heading or label
- claude status-check 4 C9 fail: last reply lacks a Result heading or label
- claude status-check 5 C9 fail: last reply lacks a Result heading or label
- claude tdd-stated 1 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply of turn 2 reports the fix ("I fixed it: `page_label(0, 3)` now returns `"Page 1 of 3"`. Nothing is committed."), the change, the test results and the record, but it contains no next-step statement and n
- claude tdd-stated 1 C9 fail: last reply lacks a Result and Evidence heading or label
- claude tdd-stated 2 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The turn 2 final reply reports "Fixed: `page_label(0, 3)` now returns "Page 1 of 3". Nothing is committed." but contains no statement that no next action is needed and names no follow-up with an owner. It raises an ope
- claude tdd-stated 2 C9 fail: last reply lacks a Result and Evidence heading or label
- claude tdd-stated 3 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The turn 2 final reply reports the fix ("I fixed it: `page_label(0, 3)` now returns `"Page 1 of 3"`. Nothing is committed.") and ends with "Record and cleanup", but it neither states that no next action is needed nor n
- claude tdd-stated 3 C9 fail: last reply lacks a Result and Evidence heading or label
- claude tdd-stated 4 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The turn 2 final reply reports the fix as done ("Fixed: `page_label(0, 3)` now returns \"Page 1 of 3\". Nothing is committed.") but never states that no next action is needed and names no follow-up with an owner. It en
- claude tdd-stated 4 C9 fail: last reply lacks a Result and Evidence heading or label
- claude tdd-stated 5 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The turn 2 final reply reports the fix, the red/green results, the caller caveat ("I have not checked for such code") and the notes update, but it never states that no next action is needed and names no follow-up with 
- claude tdd-stated 5 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 1 C1 fail: last reply has no Next action table, label, or heading with content
- codex authz-change 1 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 2 C1 fail: last reply has no Next action table, label, or heading with content
- codex authz-change 2 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 3 C1 fail: last reply has no Next action table, label, or heading with content
- codex authz-change 3 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 4 C1 fail: last reply has no Next action table, label, or heading with content
- codex authz-change 4 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 5 C1 fail: last reply has no Next action table, label, or heading with content
- codex authz-change 5 C9 fail: last reply lacks a Result and Evidence heading or label
- codex investigate-bug 1 C1 fail: last reply has no Next action table, label, or heading with content
- codex investigate-bug 1 C9 fail: last reply lacks a Result and Evidence heading or label
- codex investigate-bug 2 C9 fail: last reply lacks a Result and Evidence heading or label
- codex investigate-bug 3 C9 fail: last reply lacks a Result and Evidence heading or label
- codex investigate-bug 4 C9 fail: last reply lacks a Result and Evidence heading or label
- codex investigate-bug 5 C9 fail: last reply lacks a Result and Evidence heading or label
- codex status-check 1 C9 fail: last reply lacks a Result heading or label
- codex status-check 2 C9 fail: last reply lacks a Result and Evidence heading or label
- codex status-check 3 C9 fail: last reply lacks a Result heading or label
- codex status-check 4 C9 fail: last reply lacks a Result heading or label
- codex status-check 5 C9 fail: last reply lacks a Result heading or label
- codex tdd-stated 1 C1 fail: last reply has no Next action table, label, or heading with content
- codex tdd-stated 1 C9 fail: last reply lacks a Result and Evidence heading or label
- codex tdd-stated 2 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply of turn 2 reads only "Fixed `page_label(0, 3)` to return `"Page 1 of 3"`... All 4 tests pass, including the earlier pagination regression. No commits created." It neither states that no next action is n
- codex tdd-stated 2 C9 fail: last reply lacks a Result and Evidence heading or label
- codex tdd-stated 3 C1 fail: last reply has no Next action table, label, or heading with content
- codex tdd-stated 3 C9 fail: last reply lacks a Result and Evidence heading or label
- codex tdd-stated 4 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply of turn 2 reports completion only ("Fixed `page_label(0, 3)`... all 5 tests now pass... Previous pagination changes remain intact. No commits created."). It never states that no next action is needed an
- codex tdd-stated 4 C9 fail: last reply lacks a Result and Evidence heading or label
- codex tdd-stated 5 C1 fail: last reply has no Next action table, label, or heading with content; C1.concrete: The final reply of turn 2 reads only "Fixed `page_label(0, 3)` to return `"Page 1 of 3"`. The regression test failed before the fix; all 4 tests now pass. `git diff --check` passes. No commits created." It contains no 
- codex tdd-stated 5 C9 fail: last reply lacks a Result and Evidence heading or label
