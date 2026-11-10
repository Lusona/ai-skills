# Loop conformance report

Counts are trials per result. Graded = pass + fail. Inconclusive, setup-blocked, and not-applicable trials are excluded from graded counts.

## claude

| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 2 | 0 | 2 | 0 | 0 | 1 | 0 |
| C2 | 0 | 1 | 1 | 0 | 0 | 2 | 0 |
| C3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| C4 | 1 | 0 | 1 | 0 | 0 | 2 | 0 |
| C5 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| C6 | 1 | 0 | 1 | 0 | 0 | 2 | 0 |
| C7 | 1 | 0 | 1 | 0 | 0 | 2 | 0 |
| C8 | 2 | 0 | 2 | 0 | 0 | 1 | 0 |
| C9 | 1 | 0 | 1 | 0 | 0 | 2 | 0 |
| C10 | 0 | 1 | 1 | 0 | 0 | 2 | 0 |

## codex

| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1 | 1 | 2 | 0 | 0 | 1 | 0 |
| C2 | 1 | 0 | 1 | 0 | 0 | 2 | 0 |
| C3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| C4 | 1 | 0 | 1 | 0 | 0 | 2 | 0 |
| C5 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| C6 | 0 | 1 | 1 | 0 | 0 | 2 | 0 |
| C7 | 1 | 0 | 1 | 0 | 0 | 2 | 0 |
| C8 | 2 | 0 | 2 | 0 | 0 | 1 | 0 |
| C9 | 0 | 1 | 1 | 0 | 0 | 2 | 0 |
| C10 | 1 | 0 | 1 | 0 | 0 | 2 | 0 |

## Trials

P pass, F fail, I inconclusive, B setup-blocked, X invalid, - not applicable.

| Host | Scenario | Trial | Status | Judged | Outer changed | Seconds | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude | authz-change | 1 | captured | yes | no | 82 | P | - | - | - | - | P | P | P | P | F |
| claude | explore-save | 1 | captured | yes | no | 89 | P | F | - | - | - | - | - | P | - | - |
| claude | greeting | 1 | captured | yes | no | 2 | - | - | - | P | - | - | - | - | - | - |
| codex | authz-change | 1 | captured | yes | no | 196 | F | - | - | - | - | F | P | P | F | P |
| codex | explore-save | 1 | captured | yes | no | 98 | P | P | - | - | - | - | - | P | - | - |
| codex | greeting | 1 | captured | yes | no | 11 | - | - | - | P | - | - | - | - | - | - |

## Evaluator-material access

No trial accessed evaluator material.

## Outer repository

No trial changed files of the suite's repository.

## Boundary evidence of excluded trials

Informational: these trials are not counted as pass or fail.

No excluded trials.

## Non-pass evidence

- claude authz-change 1 C10 fail: reviewer_seen=True, 1 worker(s); a separate reviewer needs a reviewer launch and at least 2 workers
- claude explore-save 1 C2 fail: no added or modified path matches ['docs/lusona/notes/*.md']
- codex authz-change 1 C1 fail: last reply has no Next action table, label, or heading with content
- codex authz-change 1 C6 fail: docs/lusona/work.md does not name docs/lusona/specs/20261109-owner-only-list-deletion.md
- codex authz-change 1 C9 fail: last reply lacks a Result and Evidence heading or label
