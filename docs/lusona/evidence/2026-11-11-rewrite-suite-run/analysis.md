## Pass marks (draft)

| Scenario | Check | Claude Code | Mark | Met | Codex | Mark | Met |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `decision-conflict` | C12 | 5 / 5 | 5 / 5 | met | 5 / 5 | 5 / 5 | met |
| `decision-conflict` | C13 | 5 / 5 | 4 / 5 | met | 5 / 5 | 4 / 5 | met |
| `decision-conflict` | C8 | 5 / 5 | 5 / 5 | met | 5 / 5 | 5 / 5 | met |
| `decision-revised` | C14 | 5 / 5 | 4 / 5 | met | 5 / 5 | 4 / 5 | met |
| `decision-revised` | C15 | 5 / 5 | 5 / 5 | met | 5 / 5 | 5 / 5 | met |
| `decision-revised` | C8 | 5 / 5 | 5 / 5 | met | 5 / 5 | 5 / 5 | met |
| `old-records` | C16 | 5 / 5 | 5 / 5 | met | 5 / 5 | 5 / 5 | met |
| `old-records` | C17 | 5 / 5 | 4 / 5 | met | 5 / 5 | 4 / 5 | met |
| `old-records` | C8 | 3 / 5 | 5 / 5 | not met | 5 / 5 | 5 / 5 | met |
| `tdd-stated` | C9 | 5 / 5 | 4 / 5 | met | 4 / 5 | 4 / 5 | met |
| `authz-change` | C9 | 5 / 5 | 4 / 5 | met | 3 / 5 | 4 / 5 | not met |
| `status-check` | C9 | 5 / 5 | 4 / 5 | met | 5 / 5 | 4 / 5 | met |
| `investigate-bug` | C9 | 5 / 5 | 4 / 5 | met | 5 / 5 | 4 / 5 | met |

## All checks, per host and scenario (draft)

| Host | Scenario | Check | Pass / graded |
| --- | --- | --- | --- |
| claude | `authz-change` | C1 | 5 / 5 |
| claude | `authz-change` | C10 | 5 / 5 |
| claude | `authz-change` | C11 | 5 / 5 |
| claude | `authz-change` | C6 | 5 / 5 |
| claude | `authz-change` | C7 | 5 / 5 |
| claude | `authz-change` | C8 | 5 / 5 |
| claude | `authz-change` | C9 | 5 / 5 |
| claude | `decision-conflict` | C12 | 5 / 5 |
| claude | `decision-conflict` | C13 | 5 / 5 |
| claude | `decision-conflict` | C8 | 5 / 5 |
| claude | `decision-revised` | C14 | 5 / 5 |
| claude | `decision-revised` | C15 | 5 / 5 |
| claude | `decision-revised` | C8 | 5 / 5 |
| claude | `investigate-bug` | C1 | 5 / 5 |
| claude | `investigate-bug` | C11 | 5 / 5 |
| claude | `investigate-bug` | C2 | 5 / 5 |
| claude | `investigate-bug` | C8 | 5 / 5 |
| claude | `investigate-bug` | C9 | 5 / 5 |
| claude | `old-records` | C16 | 5 / 5 |
| claude | `old-records` | C17 | 5 / 5 |
| claude | `old-records` | C8 | 3 / 5 |
| claude | `status-check` | C1 | 5 / 5 |
| claude | `status-check` | C3 | 5 / 5 |
| claude | `status-check` | C8 | 5 / 5 |
| claude | `status-check` | C9 | 5 / 5 |
| claude | `tdd-stated` | C1 | 5 / 5 |
| claude | `tdd-stated` | C7 | 5 / 5 |
| claude | `tdd-stated` | C8 | 5 / 5 |
| claude | `tdd-stated` | C9 | 5 / 5 |
| codex | `authz-change` | C1 | 5 / 5 |
| codex | `authz-change` | C10 | 5 / 5 |
| codex | `authz-change` | C11 | 5 / 5 |
| codex | `authz-change` | C6 | 5 / 5 |
| codex | `authz-change` | C7 | 5 / 5 |
| codex | `authz-change` | C8 | 5 / 5 |
| codex | `authz-change` | C9 | 3 / 5 |
| codex | `decision-conflict` | C12 | 5 / 5 |
| codex | `decision-conflict` | C13 | 5 / 5 |
| codex | `decision-conflict` | C8 | 5 / 5 |
| codex | `decision-revised` | C14 | 5 / 5 |
| codex | `decision-revised` | C15 | 5 / 5 |
| codex | `decision-revised` | C8 | 5 / 5 |
| codex | `investigate-bug` | C1 | 5 / 5 |
| codex | `investigate-bug` | C11 | 5 / 5 |
| codex | `investigate-bug` | C2 | 5 / 5 |
| codex | `investigate-bug` | C8 | 5 / 5 |
| codex | `investigate-bug` | C9 | 5 / 5 |
| codex | `old-records` | C16 | 5 / 5 |
| codex | `old-records` | C17 | 5 / 5 |
| codex | `old-records` | C8 | 5 / 5 |
| codex | `status-check` | C1 | 5 / 5 |
| codex | `status-check` | C3 | 5 / 5 |
| codex | `status-check` | C8 | 5 / 5 |
| codex | `status-check` | C9 | 5 / 5 |
| codex | `tdd-stated` | C1 | 4 / 5 |
| codex | `tdd-stated` | C7 | 5 / 5 |
| codex | `tdd-stated` | C8 | 5 / 5 |
| codex | `tdd-stated` | C9 | 4 / 5 |

## Draft vs fresh reference (34186da), C9 scenarios

| Host | Scenario | Check | Draft | Reference |
| --- | --- | --- | --- | --- |
| claude | `authz-change` | C1 | 5 / 5 | 5 / 5 |
| claude | `authz-change` | C10 | 5 / 5 | 5 / 5 |
| claude | `authz-change` | C11 | 5 / 5 | 0 / 5 |
| claude | `authz-change` | C6 | 5 / 5 | 5 / 5 |
| claude | `authz-change` | C7 | 5 / 5 | 5 / 5 |
| claude | `authz-change` | C8 | 5 / 5 | 5 / 5 |
| claude | `authz-change` | C9 | 5 / 5 | 4 / 5 |
| claude | `investigate-bug` | C1 | 5 / 5 | 0 / 5 |
| claude | `investigate-bug` | C11 | 5 / 5 | 0 / 5 |
| claude | `investigate-bug` | C2 | 5 / 5 | 5 / 5 |
| claude | `investigate-bug` | C8 | 5 / 5 | 5 / 5 |
| claude | `investigate-bug` | C9 | 5 / 5 | 0 / 5 |
| claude | `status-check` | C1 | 5 / 5 | 5 / 5 |
| claude | `status-check` | C3 | 5 / 5 | 5 / 5 |
| claude | `status-check` | C8 | 5 / 5 | 5 / 5 |
| claude | `status-check` | C9 | 5 / 5 | 2 / 5 |
| claude | `tdd-stated` | C1 | 5 / 5 | 0 / 5 |
| claude | `tdd-stated` | C7 | 5 / 5 | 5 / 5 |
| claude | `tdd-stated` | C8 | 5 / 5 | 5 / 5 |
| claude | `tdd-stated` | C9 | 5 / 5 | 0 / 5 |
| codex | `authz-change` | C1 | 5 / 5 | 0 / 5 |
| codex | `authz-change` | C10 | 5 / 5 | 5 / 5 |
| codex | `authz-change` | C11 | 5 / 5 | 5 / 5 |
| codex | `authz-change` | C6 | 5 / 5 | 5 / 5 |
| codex | `authz-change` | C7 | 5 / 5 | 5 / 5 |
| codex | `authz-change` | C8 | 5 / 5 | 5 / 5 |
| codex | `authz-change` | C9 | 3 / 5 | 0 / 5 |
| codex | `investigate-bug` | C1 | 5 / 5 | 3 / 4 (+1 other) |
| codex | `investigate-bug` | C11 | 5 / 5 | 4 / 4 (+1 other) |
| codex | `investigate-bug` | C2 | 5 / 5 | 4 / 4 (+1 other) |
| codex | `investigate-bug` | C8 | 5 / 5 | 4 / 4 (+1 other) |
| codex | `investigate-bug` | C9 | 5 / 5 | 0 / 4 (+1 other) |
| codex | `status-check` | C1 | 5 / 5 | 5 / 5 |
| codex | `status-check` | C3 | 5 / 5 | 5 / 5 |
| codex | `status-check` | C8 | 5 / 5 | 5 / 5 |
| codex | `status-check` | C9 | 5 / 5 | 1 / 5 |
| codex | `tdd-stated` | C1 | 4 / 5 | 0 / 5 |
| codex | `tdd-stated` | C7 | 5 / 5 | 5 / 5 |
| codex | `tdd-stated` | C8 | 5 / 5 | 5 / 5 |
| codex | `tdd-stated` | C9 | 4 / 5 | 0 / 5 |

## Spend and actor time

| Run | Host | Trials | Actor time (s) | Actor $ | Judge $ | Judge calls |
| --- | --- | --- | --- | --- | --- | --- |
| base | claude | 20 | 985 | 7.98 | 4.36 | 20 |
| base | codex | 20 | 2,699 | 0.00 | 4.06 | 19 |
| confirm | claude | 1 | 101 | 0.68 | 0.24 | 1 |
| draft | claude | 35 | 2,674 | 19.37 | 8.12 | 35 |
| draft | codex | 35 | 4,118 | 0.00 | 7.84 | 35 |

Total Claude-reported spend: $52.65
