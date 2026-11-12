# Loop conformance report

Counts are trials per result. Graded = pass + fail. Inconclusive, setup-blocked, and not-applicable trials are excluded from graded counts.

## claude

| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 20 | 0 | 20 | 0 | 0 | 15 | 0 |
| C2 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C3 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C4 | 0 | 0 | 0 | 0 | 0 | 35 | 0 |
| C5 | 0 | 0 | 0 | 0 | 0 | 35 | 0 |
| C6 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C7 | 10 | 0 | 10 | 0 | 0 | 25 | 0 |
| C8 | 33 | 2 | 35 | 0 | 0 | 0 | 0 |
| C9 | 20 | 0 | 20 | 0 | 0 | 15 | 0 |
| C10 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C11 | 10 | 0 | 10 | 0 | 0 | 25 | 0 |
| C12 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C13 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C14 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C15 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C16 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C17 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |

## codex

| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 19 | 1 | 20 | 0 | 0 | 15 | 0 |
| C2 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C3 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C4 | 0 | 0 | 0 | 0 | 0 | 35 | 0 |
| C5 | 0 | 0 | 0 | 0 | 0 | 35 | 0 |
| C6 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C7 | 10 | 0 | 10 | 0 | 0 | 25 | 0 |
| C8 | 35 | 0 | 35 | 0 | 0 | 0 | 0 |
| C9 | 17 | 3 | 20 | 0 | 0 | 15 | 0 |
| C10 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C11 | 10 | 0 | 10 | 0 | 0 | 25 | 0 |
| C12 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C13 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C14 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C15 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C16 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |
| C17 | 5 | 0 | 5 | 0 | 0 | 30 | 0 |

## Trials

P pass, F fail, I inconclusive, B setup-blocked, X invalid, - not applicable.

| Host | Scenario | Trial | Status | Judged | Outer changed | Seconds | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | C13 | C14 | C15 | C16 | C17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude | authz-change | 1 | captured | yes | no | 95 | P | - | - | - | - | P | P | P | P | P | P | - | - | - | - | - | - |
| claude | authz-change | 2 | captured | yes | no | 102 | P | - | - | - | - | P | P | P | P | P | P | - | - | - | - | - | - |
| claude | authz-change | 3 | captured | yes | no | 98 | P | - | - | - | - | P | P | P | P | P | P | - | - | - | - | - | - |
| claude | authz-change | 4 | captured | yes | no | 126 | P | - | - | - | - | P | P | P | P | P | P | - | - | - | - | - | - |
| claude | authz-change | 5 | captured | yes | no | 120 | P | - | - | - | - | P | P | P | P | P | P | - | - | - | - | - | - |
| claude | decision-conflict | 1 | captured | yes | no | 33 | - | - | - | - | - | - | - | P | - | - | - | P | P | - | - | - | - |
| claude | decision-conflict | 2 | captured | yes | no | 36 | - | - | - | - | - | - | - | P | - | - | - | P | P | - | - | - | - |
| claude | decision-conflict | 3 | captured | yes | no | 37 | - | - | - | - | - | - | - | P | - | - | - | P | P | - | - | - | - |
| claude | decision-conflict | 4 | captured | yes | no | 35 | - | - | - | - | - | - | - | P | - | - | - | P | P | - | - | - | - |
| claude | decision-conflict | 5 | captured | yes | no | 34 | - | - | - | - | - | - | - | P | - | - | - | P | P | - | - | - | - |
| claude | decision-revised | 1 | captured | yes | no | 70 | - | - | - | - | - | - | - | P | - | - | - | - | - | P | P | - | - |
| claude | decision-revised | 2 | captured | yes | no | 65 | - | - | - | - | - | - | - | P | - | - | - | - | - | P | P | - | - |
| claude | decision-revised | 3 | captured | yes | no | 81 | - | - | - | - | - | - | - | P | - | - | - | - | - | P | P | - | - |
| claude | decision-revised | 4 | captured | yes | no | 73 | - | - | - | - | - | - | - | P | - | - | - | - | - | P | P | - | - |
| claude | decision-revised | 5 | captured | yes | no | 87 | - | - | - | - | - | - | - | P | - | - | - | - | - | P | P | - | - |
| claude | investigate-bug | 1 | captured | yes | no | 78 | P | P | - | - | - | - | - | P | P | - | P | - | - | - | - | - | - |
| claude | investigate-bug | 2 | captured | yes | no | 77 | P | P | - | - | - | - | - | P | P | - | P | - | - | - | - | - | - |
| claude | investigate-bug | 3 | captured | yes | no | 93 | P | P | - | - | - | - | - | P | P | - | P | - | - | - | - | - | - |
| claude | investigate-bug | 4 | captured | yes | no | 97 | P | P | - | - | - | - | - | P | P | - | P | - | - | - | - | - | - |
| claude | investigate-bug | 5 | captured | yes | no | 98 | P | P | - | - | - | - | - | P | P | - | P | - | - | - | - | - | - |
| claude | old-records | 1 | captured | yes | no | 68 | - | - | - | - | - | - | - | P | - | - | - | - | - | - | - | P | P |
| claude | old-records | 2 | captured | yes | no | 72 | - | - | - | - | - | - | - | P | - | - | - | - | - | - | - | P | P |
| claude | old-records | 3 | captured | yes | no | 68 | - | - | - | - | - | - | - | P | - | - | - | - | - | - | - | P | P |
| claude | old-records | 4 | captured | yes | no | 73 | - | - | - | - | - | - | - | F | - | - | - | - | - | - | - | P | P |
| claude | old-records | 5 | captured | yes | no | 76 | - | - | - | - | - | - | - | F | - | - | - | - | - | - | - | P | P |
| claude | status-check | 1 | captured | yes | no | 77 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| claude | status-check | 2 | captured | yes | no | 34 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| claude | status-check | 3 | captured | yes | no | 59 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| claude | status-check | 4 | captured | yes | no | 57 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| claude | status-check | 5 | captured | yes | no | 66 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| claude | tdd-stated | 1 | captured | yes | no | 106 | P | - | - | - | - | - | P | P | P | - | - | - | - | - | - | - | - |
| claude | tdd-stated | 2 | captured | yes | no | 97 | P | - | - | - | - | - | P | P | P | - | - | - | - | - | - | - | - |
| claude | tdd-stated | 3 | captured | yes | no | 90 | P | - | - | - | - | - | P | P | P | - | - | - | - | - | - | - | - |
| claude | tdd-stated | 4 | captured | yes | no | 92 | P | - | - | - | - | - | P | P | P | - | - | - | - | - | - | - | - |
| claude | tdd-stated | 5 | captured | yes | no | 101 | P | - | - | - | - | - | P | P | P | - | - | - | - | - | - | - | - |
| codex | authz-change | 1 | captured | yes | no | 172 | P | - | - | - | - | P | P | P | F | P | P | - | - | - | - | - | - |
| codex | authz-change | 2 | captured | yes | no | 153 | P | - | - | - | - | P | P | P | P | P | P | - | - | - | - | - | - |
| codex | authz-change | 3 | captured | yes | no | 209 | P | - | - | - | - | P | P | P | P | P | P | - | - | - | - | - | - |
| codex | authz-change | 4 | captured | yes | no | 156 | P | - | - | - | - | P | P | P | F | P | P | - | - | - | - | - | - |
| codex | authz-change | 5 | captured | yes | no | 229 | P | - | - | - | - | P | P | P | P | P | P | - | - | - | - | - | - |
| codex | decision-conflict | 1 | captured | yes | no | 39 | - | - | - | - | - | - | - | P | - | - | - | P | P | - | - | - | - |
| codex | decision-conflict | 2 | captured | yes | no | 84 | - | - | - | - | - | - | - | P | - | - | - | P | P | - | - | - | - |
| codex | decision-conflict | 3 | captured | yes | no | 47 | - | - | - | - | - | - | - | P | - | - | - | P | P | - | - | - | - |
| codex | decision-conflict | 4 | captured | yes | no | 35 | - | - | - | - | - | - | - | P | - | - | - | P | P | - | - | - | - |
| codex | decision-conflict | 5 | captured | yes | no | 80 | - | - | - | - | - | - | - | P | - | - | - | P | P | - | - | - | - |
| codex | decision-revised | 1 | captured | yes | no | 77 | - | - | - | - | - | - | - | P | - | - | - | - | - | P | P | - | - |
| codex | decision-revised | 2 | captured | yes | no | 154 | - | - | - | - | - | - | - | P | - | - | - | - | - | P | P | - | - |
| codex | decision-revised | 3 | captured | yes | no | 139 | - | - | - | - | - | - | - | P | - | - | - | - | - | P | P | - | - |
| codex | decision-revised | 4 | captured | yes | no | 119 | - | - | - | - | - | - | - | P | - | - | - | - | - | P | P | - | - |
| codex | decision-revised | 5 | captured | yes | no | 190 | - | - | - | - | - | - | - | P | - | - | - | - | - | P | P | - | - |
| codex | investigate-bug | 1 | captured | yes | no | 131 | P | P | - | - | - | - | - | P | P | - | P | - | - | - | - | - | - |
| codex | investigate-bug | 2 | captured | yes | no | 131 | P | P | - | - | - | - | - | P | P | - | P | - | - | - | - | - | - |
| codex | investigate-bug | 3 | captured | yes | no | 163 | P | P | - | - | - | - | - | P | P | - | P | - | - | - | - | - | - |
| codex | investigate-bug | 4 | captured | yes | no | 149 | P | P | - | - | - | - | - | P | P | - | P | - | - | - | - | - | - |
| codex | investigate-bug | 5 | captured | yes | no | 181 | P | P | - | - | - | - | - | P | P | - | P | - | - | - | - | - | - |
| codex | old-records | 1 | captured | yes | no | 125 | - | - | - | - | - | - | - | P | - | - | - | - | - | - | - | P | P |
| codex | old-records | 2 | captured | yes | no | 88 | - | - | - | - | - | - | - | P | - | - | - | - | - | - | - | P | P |
| codex | old-records | 3 | captured | yes | no | 95 | - | - | - | - | - | - | - | P | - | - | - | - | - | - | - | P | P |
| codex | old-records | 4 | captured | yes | no | 136 | - | - | - | - | - | - | - | P | - | - | - | - | - | - | - | P | P |
| codex | old-records | 5 | captured | yes | no | 97 | - | - | - | - | - | - | - | P | - | - | - | - | - | - | - | P | P |
| codex | status-check | 1 | captured | yes | no | 54 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| codex | status-check | 2 | captured | yes | no | 30 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| codex | status-check | 3 | captured | yes | no | 24 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| codex | status-check | 4 | captured | yes | no | 46 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| codex | status-check | 5 | captured | yes | no | 46 | P | - | P | - | - | - | - | P | P | - | - | - | - | - | - | - | - |
| codex | tdd-stated | 1 | captured | yes | no | 138 | P | - | - | - | - | - | P | P | P | - | - | - | - | - | - | - | - |
| codex | tdd-stated | 2 | captured | yes | no | 144 | P | - | - | - | - | - | P | P | P | - | - | - | - | - | - | - | - |
| codex | tdd-stated | 3 | captured | yes | no | 143 | P | - | - | - | - | - | P | P | P | - | - | - | - | - | - | - | - |
| codex | tdd-stated | 4 | captured | yes | no | 174 | F | - | - | - | - | - | P | P | F | - | - | - | - | - | - | - | - |
| codex | tdd-stated | 5 | captured | yes | no | 142 | P | - | - | - | - | - | P | P | P | - | - | - | - | - | - | - | - |

## Evaluator-material access

No trial accessed evaluator material.

## Outer repository

No trial changed files of the suite's repository.

## Boundary evidence of excluded trials

Informational: these trials are not counted as pass or fail.

No excluded trials.

## Non-pass evidence

- claude old-records 4 C8 fail: changed outside allowed scope ['docs/lusona/notes/*.md', 'docs/lusona/specs/*.md', 'docs/lusona/work.md', 'docs/lusona/evidence/*.md', 'docs/lusona/evidence/*/*.md', 'docs/lusona/evidence/**', 'docs/lusona/history/*.md', 'docs/lusona/adr/*.md', '__pycache__/*', '*/__pycache__/*', '.pytest_cache/*', 
- claude old-records 5 C8 fail: changed outside allowed scope ['docs/lusona/notes/*.md', 'docs/lusona/specs/*.md', 'docs/lusona/work.md', 'docs/lusona/evidence/*.md', 'docs/lusona/evidence/*/*.md', 'docs/lusona/evidence/**', 'docs/lusona/history/*.md', 'docs/lusona/adr/*.md', '__pycache__/*', '*/__pycache__/*', '.pytest_cache/*', 
- codex authz-change 1 C9 fail: last reply lacks a Result and Evidence heading or label
- codex authz-change 4 C9 fail: last reply lacks a Result and Evidence heading or label
- codex tdd-stated 4 C1 fail: last reply has no Next action table, label, or heading with content
- codex tdd-stated 4 C9 fail: last reply lacks a Result and Evidence heading or label
