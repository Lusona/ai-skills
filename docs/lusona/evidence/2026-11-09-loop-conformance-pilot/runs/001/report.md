# Loop conformance report

Counts are trials per result. Graded = pass + fail. Inconclusive, setup-blocked, and not-applicable trials are excluded from graded counts.

## claude

| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| C2 | 0 | 1 | 1 | 0 | 0 | 1 | 0 |
| C3 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| C4 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| C5 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| C6 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| C7 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| C8 | 1 | 1 | 2 | 0 | 0 | 0 | 0 |
| C9 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| C10 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |

## codex

| Check | Pass | Fail | Graded | Inconclusive | Setup-blocked | Not applicable | Invalid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| C2 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| C3 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| C4 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| C5 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| C6 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| C7 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| C8 | 2 | 0 | 2 | 0 | 0 | 0 | 0 |
| C9 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| C10 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |

## Trials

P pass, F fail, I inconclusive, B setup-blocked, X invalid, - not applicable.

| Host | Scenario | Trial | Status | Judged | Outer changed | Seconds | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude | explore-save | 1 | captured | yes | no | 71 | P | F | - | - | - | - | - | F | - | - |
| claude | tdd-unset | 1 | captured | yes | no | 20 | - | - | - | - | P | - | - | P | - | - |
| codex | explore-save | 1 | captured | yes | no | 139 | P | P | - | - | - | - | - | P | - | - |
| codex | tdd-unset | 1 | captured | yes | no | 46 | - | - | - | - | P | - | - | P | - | - |

## Evaluator-material access

No trial accessed evaluator material.

## Outer repository

No trial changed the outer repository's git status.

## Non-pass evidence

- claude explore-save 1 C2 fail: no added or modified path matches ['docs/lusona/notes/*.md']; C2.content: The only changed file is `notes/tally-storage-options.md`, which is not under `docs/lusona/notes/` as the criterion requires. Its content would otherwise meet all four items: the LibreOffice constraint ("This must keep working
- claude explore-save 1 C8 fail: changed outside allowed scope ['docs/lusona/notes/*.md', 'docs/lusona/specs/*.md', 'docs/lusona/work.md', 'docs/lusona/evidence/*.md', 'docs/lusona/evidence/*/*.md', 'docs/lusona/evidence/**', 'docs/lusona/history/*.md', 'docs/lusona/adr/*.md']: notes/tally-storage-options.md
