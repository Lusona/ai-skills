# Final measurement: reviewed revision ea99970

Question and scenario: compare the representative spec-linked implement with one delegated worker, no failures, and no spec creation against baseline 545b6e0. This run supersedes the topic summary’s current comparison, while historical runs remain unchanged.

Method: execute the existing `measure.py` from the repository root with Python 3. Words are whitespace-separated tokens; section counts exclude level-2 headings and the core preamble. The whole README count includes both. The optional coordinator handoff reference is counted when present. No plugin files differ from the pinned final revision.

## Provenance

- Baseline revision: `545b6e05146844911dd91a9f8ecb1f276c0dc9aa`.
- Final revision: `ea9997095fa116e2902f06bc8d12b132283a09c5`.
- Python: `Python 3.14.9`.
- Instrument `measure.py` SHA-256: `c6c4e22cfba149196ac3816cd3d455af09f057188f2445db38866692a32cf22c`.
- Revised instrument `scripts/check_instructions.py` SHA-256: `96194d93814ab2c383165b4d3b658267f82908b1c5833d95ab9376fd534fd400`.

## Complete measure.py output

Command: `python3 docs/lusona/evidence/2026-11-03-realign-instructions/measure.py "Final reviewed revision, 2026-11-03"`

## Final reviewed revision, 2026-11-03: HEAD ea99970, plugin tree clean

### Coordinator

| File (sections) | Words |
| --- | --- |
| `plugins/lusona/README.md` | 1,566 |
| `plugins/lusona/skills/implement/SKILL.md` | 609 |
| `plugins/lusona/references/tdd.md` | 320 |
| `plugins/lusona/references/retention.md` | 877 |
| `plugins/lusona/references/queue.md` | 651 |
| `plugins/lusona/references/delegation.md` | 545 |
| `plugins/lusona/references/model-routing.md` | 382 |
| `plugins/lusona/references/worker-lifecycle.md` | 268 |
| `plugins/lusona/references/commits.md` | 704 |
| `plugins/lusona/references/handoff.md` | 114 |
| **Total** | **6,036** |

### Worker

| File (sections) | Words |
| --- | --- |
| `plugins/lusona/README.md §Loading rules, Work loop, Contract, TDD, Review and communication, Assigned leaves, Context budget` | 1,194 |
| `plugins/lusona/skills/implement/SKILL.md` | 609 |
| `plugins/lusona/references/tdd.md` | 320 |
| `plugins/lusona/references/retention.md` | 877 |
| `plugins/lusona/references/delegation.md §Assigned leaves, Assignment results` | 239 |
| **Total** | **3,239** |

### Core sections

| File (sections) | Words |
| --- | --- |
| `plugins/lusona/README.md §Loading rules` | 152 |
| `plugins/lusona/README.md §Work loop` | 339 |
| `plugins/lusona/README.md §Contract` | 307 |
| `plugins/lusona/README.md §References` | 172 |
| `plugins/lusona/README.md §Questions and next actions` | 61 |
| `plugins/lusona/README.md §TDD` | 20 |
| `plugins/lusona/README.md §Review and communication` | 306 |
| `plugins/lusona/README.md §Assigned leaves` | 41 |
| `plugins/lusona/README.md §Personas and subagents` | 104 |
| `plugins/lusona/README.md §Context budget` | 29 |
| **Total** | **1,531** |

All plugin Markdown files: 25,482 words in 48 files

### File hashes

- `plugins/lusona/README.md` 5b68f6886a99492b
- `plugins/lusona/skills/implement/SKILL.md` db0055ab855620d8
- `plugins/lusona/references/tdd.md` de0e0fc3595863cc
- `plugins/lusona/references/retention.md` a3adf780fb3c06bb
- `plugins/lusona/references/queue.md` 0843dcefec9d110d
- `plugins/lusona/references/delegation.md` 6d41e9838b1de212
- `plugins/lusona/references/model-routing.md` d0088743b71d0ad7
- `plugins/lusona/references/worker-lifecycle.md` 2b3a5b7492050150
- `plugins/lusona/references/commits.md` 6d01c2a0d014684c
- `plugins/lusona/references/handoff.md` 272d35cd19e6e652

## Supplemental pinned-revision verification

Inputs are read with `git ls-tree -r --name-only <revision> plugins/lusona` and `git show <revision>:<path>`; no checkout or plugin mutation is used. Word totals use `len(text.split())`. Role totals use the unchanged manifests and `sections()` in `measure.py`, skipping absent optional files. Required core sections use `WORKER_CORE_SECTIONS`. Skill totals include all fourteen `skills/*/SKILL.md` files, including frontmatter. Markdown totals include every `.md` under the plugin.

Restatement counts apply the revised checker’s `body`, `LINK`, and `RESTATED` to each skill body. Routing owners apply its `tables` and `classify` to all plugin Markdown. These are structural observations, not a claim that the checker detects every semantic duplication. The original single-line checker’s 27 baseline matches remain the historical observation in `red.md`; 29 is the revised wrapped-line matcher’s result on the same pinned baseline.

| Measure | Baseline 545b6e0 | Final ea99970 |
| --- | --- | --- |
| Coordinator words | 6,277 | 6,036 |
| Worker words | 3,607 | 3,239 |
| Required core section words | 1,309 | 1,194 |
| Whole core README words | 1,675 | 1,566 |
| Fourteen skills, words | 9,203 | 7,446 |
| All plugin Markdown, words | 26,787 in 47 files | 25,482 in 48 files |
| Restated clauses, revised wrapped matcher | 29 | 0 |
| Routing table occurrences and owners | 1: `plugins/lusona/skills/status/SKILL.md` | 1: `plugins/lusona/references/workflow-guide.md` |

### Skill inputs and hashes

| Revision | Skill file | Words | SHA-256 |
| --- | --- | --- | --- |
| `545b6e0` | `plugins/lusona/skills/architect/SKILL.md` | 897 | `c6648d1b99a25301c2052b90da3a3e7b24babe3514c5adbf0bf81bc844c7e3e1` |
| `545b6e0` | `plugins/lusona/skills/batch/SKILL.md` | 973 | `0f1ea2e3b8584408a35030d78e4bfa52f51a0e0c676fb750e73b0ff348e72794` |
| `545b6e0` | `plugins/lusona/skills/design/SKILL.md` | 517 | `55b0042c056b8263b316c551c6124f215713f6019925f69eba995503f27325e3` |
| `545b6e0` | `plugins/lusona/skills/experiment/SKILL.md` | 452 | `3c8e5238167fb144bb0b9e5b84d3a20861dedb4f500e771c432e84ec9112ce92` |
| `545b6e0` | `plugins/lusona/skills/explore/SKILL.md` | 473 | `588e76687481e65a63a222145b2fe7d6fc318932615b1ebcb7a3be4cd98c8670` |
| `545b6e0` | `plugins/lusona/skills/frame-product/SKILL.md` | 341 | `3fdfa2e8184f6ecc4334b04f85b7b623f22505c164d84a39c74a940c8a50f018` |
| `545b6e0` | `plugins/lusona/skills/implement/SKILL.md` | 952 | `cd0410d3d7f2a8433e23db8452b521c2bc53844a06e089463bef9071297aa7d2` |
| `545b6e0` | `plugins/lusona/skills/investigate/SKILL.md` | 534 | `75829ba596623ab294a4587350f5a36b19351b676ad0886e4009531311483d97` |
| `545b6e0` | `plugins/lusona/skills/map-capabilities/SKILL.md` | 422 | `dc45a71a6a1dd08a6e35e5a2f3fe506865c86a7d48ca37c73cf5835b1ee19ae9` |
| `545b6e0` | `plugins/lusona/skills/measure/SKILL.md` | 455 | `dae6d960395573ab7d36e821613394b300fea7715d5684347360db78a8c2572a` |
| `545b6e0` | `plugins/lusona/skills/refactor/SKILL.md` | 625 | `924306c3c7374a173c337306b2dba40b15a325f74ecba1590211b1bb2389897b` |
| `545b6e0` | `plugins/lusona/skills/review/SKILL.md` | 890 | `bc4fc965ccca69092b468bb361b4e4a48faae8b688bf4c9d493d31509f0fdad9` |
| `545b6e0` | `plugins/lusona/skills/specify/SKILL.md` | 794 | `e9263931b2515d796d6af0565537b6436f9b150bc493683e0abbe907efd33863` |
| `545b6e0` | `plugins/lusona/skills/status/SKILL.md` | 878 | `65eb9ead1efe7431ea36cf8837bae9c08c43d179edb53b8acab4cddb6360718b` |
| `ea99970` | `plugins/lusona/skills/architect/SKILL.md` | 783 | `9cf67532ba29de79daacd77fab74b87964058abc19e3fb4470d3341fc0cc3906` |
| `ea99970` | `plugins/lusona/skills/batch/SKILL.md` | 926 | `1011aa5ca354579324cbdbf943cbb5ec20c82a95b60bb575fc8efaf417d3fe26` |
| `ea99970` | `plugins/lusona/skills/design/SKILL.md` | 453 | `644107e1de5fa7303ed3df549f1fc9338052a432f453acfac2600a0f4c2a58dc` |
| `ea99970` | `plugins/lusona/skills/experiment/SKILL.md` | 363 | `4d8b712b02b1f99ed4f73a5c641349d863d6ec9b2d341969bac627ae4b3843a6` |
| `ea99970` | `plugins/lusona/skills/explore/SKILL.md` | 413 | `192645b789058324c7ff723581d2a4d89f8ccea8f577b829ebd850d21dbbd16b` |
| `ea99970` | `plugins/lusona/skills/frame-product/SKILL.md` | 280 | `988b0758e731474e8e05e17c902ea23229e5d42bb35ace6345ecca5a502d0234` |
| `ea99970` | `plugins/lusona/skills/implement/SKILL.md` | 609 | `db0055ab855620d8ab44f695ee1a017078291d44cc821be59b46f52c821f365a` |
| `ea99970` | `plugins/lusona/skills/investigate/SKILL.md` | 464 | `2602f8123834fa2175731c8e874cdad4a58ed04dffabdb970b173f69e5df6672` |
| `ea99970` | `plugins/lusona/skills/map-capabilities/SKILL.md` | 366 | `4e0d920f1225ef8742f9c936554bd993b648a4c8d258342dec4a10b9087e62f7` |
| `ea99970` | `plugins/lusona/skills/measure/SKILL.md` | 358 | `8e601a829e1766b2d967976957f513b18372e6c40681e0c17e2e28189f55aaa2` |
| `ea99970` | `plugins/lusona/skills/refactor/SKILL.md` | 430 | `a3e0f550e0d0889d1a4e226981466721742a17fffa132d499a17cd264927dbdc` |
| `ea99970` | `plugins/lusona/skills/review/SKILL.md` | 758 | `4ca1a83bf3216b18d104049917e6a7aa7f8debe30087fd7156f7e83019c8729e` |
| `ea99970` | `plugins/lusona/skills/specify/SKILL.md` | 619 | `7f2031826007f1612dcaa7faefdd2aee3c1e8a821aeb32d0c5087ac73577812c` |
| `ea99970` | `plugins/lusona/skills/status/SKILL.md` | 624 | `1c489c4db90e25889e891f2178ae6385207406d45cf9aeb64f358c0b010dd1ee` |

## Interpretation and limitations

The pinned final coordinator total is 241 words below baseline; the worker total is 368 words below baseline. Required core sections decrease by 115 words, the whole core README by 109, and the fourteen skills by 1,757. These counts do not measure model tokens, latency, cost, or agent behavior. The final run is comparable to baseline under the declared scenario; `after.md` is an earlier dirty-tree observation and does not identify the final reviewed artifacts.
