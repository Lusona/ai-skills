# Run 008 — offline audit of instruction loading, 2026-11-10

Owner: [completion-reply notes](../../../../notes/completion-reply-conformance.md).
Sources: [run 003](../003/README.md), [run 006](../006/README.md), [run 007](../007/README.md)
raw archives. This audit reads existing transcripts only. It is not an actor run.

## Question

How often does the root agent receive the core README and the applicable references? The answer
informs whether rules defined only in the core can be relied on, or must also appear in the
injected skill text.

## Method and provenance

- [audit_loading.py](audit_loading.py) reads every root-agent transcript in the three archives:
  148 trials (run 003: 120; run 006: 24; run 007: 4). A plugin file counts as returned when tool
  output shown to the root agent contains at least 3 of that file's unique lines (stripped lines
  of 40 or more characters that occur in no other file of the same plugin snapshot). A README
  section counts when at least 2 of its unique lines appear. Output: [rows.json](rows.json).
- Plugin snapshots: run 003 uses commit `42b8145` (plugin 2.0.5); runs 006 and 007 use the
  condition plugins stored in their archives.
- [summarize.py](summarize.py) produces [summary.md](summary.md). Rules for when a reference
  applies are quoted from the 2.0.5 core in its docstring.
- Instrument check: the communication-section flag agrees with the run 004 manual audit on all
  40 trials it covered, and with run 006's recorded loading pattern on all 24 trials. A plain
  search of every event in the 33 Claude transcripts without a core read finds no
  `plugin/README.md` path, core heading or core opening sentence.
- Run from the repository root:

  ```sh
  mkdir -p tmp/loading-audit/plugin-42b8145
  git archive 42b8145 plugins/lusona | tar -x -C tmp/loading-audit/plugin-42b8145
  python3 docs/lusona/evidence/2026-11-09-loop-conformance-pilot/runs/008/audit_loading.py > tmp/loading-audit/rows.json
  python3 docs/lusona/evidence/2026-11-09-loop-conformance-pilot/runs/008/summarize.py tmp/loading-audit/rows.json
  ```

- SHA-256: run 003 `raw.zip` `50662599…`, run 006 `raw.zip` `8cde31e4…`, run 007 `raw.zip`
  `6a0d78d9…`; `audit_loading.py` `d181f9be…`; `summarize.py` `0a448771…`;
  `rows.json` `cccd6de6…`. Repository HEAD `9f2260f`. The raw archives are git-ignored and exist
  only on the machine that ran the trials.

## Observations

Core README returned to the root agent. Claude's rate depends on the scenario: 10 of its 12
run 003 cells are 0/5 or 5/5, so pooled rates reflect the scenario mix. Run 003 is the only
balanced sample: 35/60, or 35/55 without `greeting`, where skipping the core is defensible.
Runs 006 and 007 contain one always-read and one never-read scenario.

| Host | Run 003 | Run 006 | Run 007 | All | All 10 sections (run 003) |
| --- | --- | --- | --- | --- | --- |
| Claude Code | 35/60 | 6/12 | 2/4 | 43/76 | 26/60 |
| Codex | 60/60 | 12/12 | — | 72/72 | 60/60 |

- Claude never returned the core in `explore-no-save`, `review-readonly`, `greeting` (0/5 each)
  or `tdd-stated` (0/13 across runs 003, 006 and 007); `investigate-bug` 1/5, `status-check` 4/5.
  It returned the core 5/5 in `explore-save`, `workflow-question`, `tdd-unset`, `refactor-unset`,
  `specify-change` and `authz-change` (13/13 across runs). `workflow-question` and `tdd-unset`
  were mostly partial reads (0/5 and 1/5 complete).
- When Claude read the core, it was the first plugin file returned in 38 of 43 trials; in the other
  5 it followed `tdd.md` or `retention.md`. In the 15 `explore-no-save`, `review-readonly` and
  `greeting` trials and 2 `tdd-stated` trials, no plugin file was returned at all.
- Codex returned its SKILL.md in 72/72 trials. Its harness prompt names the SKILL.md path and asks
  for "applicable linked instructions"; Claude receives the skill through a slash command. The
  hosts' loading rates are therefore not comparable as host behavior.

References, when the triggering operation occurred (root agent, all runs unless stated):

| Rule from the core | Claude | Codex |
| --- | --- | --- |
| `delegation.md` before the first worker dispatch | 16/17 | 36/36 |
| `model-routing.md` before the first worker dispatch | 15/17 | 36/36 |
| `worker-lifecycle.md` when workers were dispatched | 9/17 | 36/36 |
| `tdd.md` in implement or refactor trials | 34/36 | 32/32 |
| `retention.md` when a `docs/lusona/` record was saved | 37/37 | 46/46 |
| `queue.md` when a spec was added or changed | 18/18 | 16/16 |

- These rows count only trials where the operation occurred, so they omit operations the agent
  never performed. Claude saved a record in `tdd-stated` 5/5 in run 003, 2/6 in run 006 and 0/2
  in run 007; the trials without a record also did not read `retention.md`.
- Claude dispatched workers in 17 of 43 trials that returned the core (`authz-change` 13/13,
  `specify-change` 4/5) and in 0 of 33 that did not. This is an association: dispatch occurred in
  only two scenarios, and both always returned the core. The 33 trials include
  13 `tdd-stated`, 4 `investigate-bug` and 5 `review-readonly` trials, whose skills
  cover work the core assigns to delegates. `investigate-bug` trial 2 read the core and also
  did not dispatch.
- C9 association (Claude, from run 004 and run 006 grades): core returned 16 trials, 12 passed;
  core not returned 16 trials, 0 passed. Core reading coincides with scenario, so this is an
  association, not a measured effect.

## Limitations

- Only tool output in the transcripts is counted. Claude's slash-command skill body, system
  context and any other injected text are not recorded. Worker reads are excluded; Codex worker
  transcripts are encrypted.
- The 3-line threshold counts partial reads (for example `grep` or `sed` ranges) as returned when
  they show at least 3 unique lines. Reading a file does not establish that its rules were applied.
- Reference applicability is conditioned on the agent performing the operation. When the core
  was skipped, operations such as worker dispatch did not occur, so the reference rows do not
  count those omissions.
- Runs 001 and 002 (7 pilot trials, older plugin) are excluded. Small samples per scenario;
  no significance claim.

## Conclusion

Missing instruction text is concentrated in the core README on Claude Code: no trace of it
appears in 33 of 76 Claude trials, decided by scenario (run 003 balanced sample: 35/60 received). Once an operation occurred, the references it triggers were read in
most trials on both hosts; `worker-lifecycle.md` on Claude (9/17) is the exception. Codex
received the core in every trial under its harness prompt.
