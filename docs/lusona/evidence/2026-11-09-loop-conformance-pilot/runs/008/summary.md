## Core README returned to root agent, run 003, by scenario (5 trials per cell)
| Scenario | Skill | Claude core | Claude all 10 sections | Codex core | Codex all 10 sections |
| --- | --- | --- | --- | --- | --- |
| explore-save | explore | 5/5 | 5/5 | 5/5 | 5/5 |
| explore-no-save | explore | 0/5 | 0/5 | 5/5 | 5/5 |
| review-readonly | review | 0/5 | 0/5 | 5/5 | 5/5 |
| greeting | explore | 0/5 | 0/5 | 5/5 | 5/5 |
| workflow-question | status | 5/5 | 0/5 | 5/5 | 5/5 |
| tdd-unset | implement | 5/5 | 1/5 | 5/5 | 5/5 |
| refactor-unset | refactor | 5/5 | 5/5 | 5/5 | 5/5 |
| tdd-stated | implement | 0/5 | 0/5 | 5/5 | 5/5 |
| specify-change | specify | 5/5 | 5/5 | 5/5 | 5/5 |
| status-check | status | 4/5 | 4/5 | 5/5 | 5/5 |
| investigate-bug | investigate | 1/5 | 1/5 | 5/5 | 5/5 |
| authz-change | implement | 5/5 | 5/5 | 5/5 | 5/5 |
| **Total** | | 35/60 | 26/60 | 60/60 | 60/60 |

## Core README, runs 006 and 007
- run 006 ('A', 'claude', 'authz-change'): core 3/3
- run 006 ('A', 'claude', 'tdd-stated'): core 0/3
- run 006 ('A', 'codex', 'authz-change'): core 3/3
- run 006 ('A', 'codex', 'tdd-stated'): core 3/3
- run 006 ('B', 'claude', 'authz-change'): core 3/3
- run 006 ('B', 'claude', 'tdd-stated'): core 0/3
- run 006 ('B', 'codex', 'authz-change'): core 3/3
- run 006 ('B', 'codex', 'tdd-stated'): core 3/3
- run 007 ('BASELINE', 'claude', 'authz-change'): core 1/1
- run 007 ('BASELINE', 'claude', 'tdd-stated'): core 0/1
- run 007 ('CANDIDATE', 'claude', 'authz-change'): core 1/1
- run 007 ('CANDIDATE', 'claude', 'tdd-stated'): core 0/1

## Codex skill file returned (Codex reads SKILL.md itself)
72/72

## Rule-triggered references, all runs, root agent
| Rule | Claude | Codex |
| --- | --- | --- |
| delegation.md before first dispatch | 16/17 | 36/36 |
| model-routing.md before first dispatch | 15/17 | 36/36 |
| worker-lifecycle.md when workers dispatched | 9/17 | 36/36 |
| tdd.md in implement/refactor trials | 34/36 | 32/32 |
| retention.md when a docs/lusona record was saved | 37/37 | 46/46 |
| queue.md when a spec was added or changed | 18/18 | 16/16 |

## Dispatch and saving, by whether the core was returned (all runs)
- claude core=True: 43 trials, dispatched 17, saved a docs/lusona record 26
- claude core=False: 33 trials, dispatched 0, saved a docs/lusona record 11
- codex core=True: 72 trials, dispatched 36, saved a docs/lusona record 46
- codex core=False: 0 trials, dispatched 0, saved a docs/lusona record 0
- claude tdd-stated run 003: saved a record 5/5
- claude tdd-stated run 006: saved a record 2/6
- claude tdd-stated run 007: saved a record 0/2

## Reference frequency, run 003 (trials returning each file / 60 per host)
| Reference | Claude | Codex |
| --- | --- | --- |
| retention.md | 31 | 44 |
| work-record.md | 27 | 34 |
| tdd.md | 25 | 31 |
| queue.md | 15 | 25 |
| delegation.md | 9 | 29 |
| model-routing.md | 9 | 29 |
| worker-lifecycle.md | 6 | 26 |
| files.md | 9 | 17 |
| naming.md | 10 | 16 |
| evidence.md | 10 | 15 |
| interviews.md | 5 | 15 |
| workflow-guide.md | 10 | 10 |
| corrections.md | 1 | 8 |
| handoff.md | 0 | 5 |
| closeout.md | 2 | 1 |
| commits.md | 3 | 0 |
