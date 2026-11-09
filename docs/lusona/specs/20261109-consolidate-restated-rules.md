# Spec 20261109-consolidate-restated-rules: Consolidate restated rules

Created: 2026-11-09
Updated: 2026-11-09

Kind: refactor
Work item: [Historical completion](../history/2026-11-week-02.md#2026-11-09--consolidate-restated-rules)
Context: follows [20261108-consolidate-record-helper-instructions](20261108-consolidate-record-helper-instructions.md)

## Agreement

- User and problem: the user invoked `lusona:refactor` after repeated explicitness and
  consistency passes. Those passes left the same rule stated in several canonical files.
  Each extra copy must be kept in step by hand, and several copies already state different
  conditions from their owner.
- Structural outcome: each rule in the families below has one owning statement. A copy is
  removed, or reduced to a pointer plus its local consequence, only when it passes the
  removal test. Copies that state different conditions take their conditions from the owner.
- Scope: canonical references and skills under `plugins/lusona/`, in five rule families:
  1. Save restrictions: explicit read-only, no-save, destination limits, and write permissions
     prevail. Owner: [core Contract](../../../plugins/lusona/README.md#contract).
  2. A spec requires queue tracking; direct work without a spec uses notes. Owners: core
     Contract, [queue](../../../plugins/lusona/references/queue.md), and
     [retention](../../../plugins/lusona/references/retention.md) for what notes retain.
  3. Load timing for worker lifecycle and model routing. Owner: core Personas and subagents.
  4. Batch pool, repair rounds, and incremental reporting. Owners:
     [batch execution](../../../plugins/lusona/references/batch-execution.md) and the batch
     skill's [execution reference](../../../plugins/lusona/skills/batch/references/execution.md).
  5. Conditions for adding tasks or an execution section. Owner: core Work loop.
- Exclusions: templates (their text is copied into consuming-project records), scripts,
  manifests, versions, `CHANGELOG.md`, the root `README.md` and its translations, evaluation
  sources, and the unrelated untracked note. No commit, push, or publication.
- Constraints: observable workflow behavior stays the same except for the authorized
  alignment below. Preserve loading paths, anchors, and links. Keep every local consequence.
- Completion condition: AC1–AC6 pass, including independent review. No human acceptance or
  delivery step is required beyond the user's reading of the result.

### Removal test

A sentence is removed only if all hold. Otherwise it stays, and the failing condition is recorded.

1. Owner loaded: every reader of the copy also loads the owner under the
   [core Loading rules](../../../plugins/lusona/README.md#loading-rules) at the time the copy applies.
2. No local addition: the copy adds no consequence that the owner lacks. A local consequence
   (what to report, where to state it) stays.
3. Same conditions: the copy's conditions match the owner's. When they differ, the copy takes
   its condition from the owner by pointer or by the owner's term, under the alignment decision.
4. No evidence dependence: the commit that added the copy does not cite behavioral evidence
   for that placement. If it does, the copy stays, because static checks cannot show equivalence.

### Acceptance criteria

- [x] AC1: Every removed sentence has an identified owner that all readers of the removed
  sentence load, and the removal loses no consequence. Traced per sentence in the matrix.
- [x] AC2: Every save-restriction copy that stated its condition differently from the core
  Contract now takes its condition from the Contract and keeps its local consequence.
- [x] AC3: Copies that fail the removal test are unchanged, with the failing condition recorded.
- [x] AC4: Templates, scripts, manifests, versions, changelog, root README, translations, and
  evaluation sources are unchanged.
- [x] AC5: Baseline and candidate characterization, the instruction checker, unit tests,
  package build with link validation, native plugin validation, and `git diff --check` pass.
- [x] AC6: Independent review of the actual diff against AC1–AC5 has no unresolved actionable finding.

### Decisions and uncertainty

- Breadth, selected by the user on 2026-11-09: all qualifying families, one verified increment
  at a time, under one spec and queue row.
- Differing conditions, selected by the user on 2026-11-09: “Align to the owner”. Each differing
  copy takes the owner's conditions. This is an authorized correction, not refactoring.
  Rationale for treating the save-restriction alignment as rule-preserving: every reader of a
  copy already loads the core Contract, so the owner's conditions already bind that reader.
- Family 5 is open. The core Work loop lists dependencies, uncertainty, coordination, recovery,
  or a requested plan. Retention and implement also list a long run whose earlier context will
  be summarized, and the unchanged spec template lists it too. Those copies date from `215cdfd`;
  the core sentence was added later in `6bcd4b0` without that condition. Literal alignment
  would delete a condition that the template still states. Decision, selected by the user on
  2026-11-09: “Add it to the core”. The core Work loop sentence gains the long-run condition,
  and retention points to the core instead of listing conditions. The copies and the template
  also list “sequencing”, which the core lacks; the coordinator adds it in the same edit so the
  core, retention, implement, and the spec template state one list. Implement already states
  every condition across `skills/implement/SKILL.md:34-38` and stays unchanged.
- Independent review is required: these are shared procedure contracts.

### TDD policy

- Level: targeted
- Selected by user: this session, 2026-11-09, through the native question dialog.
- Test-first behaviors: rule availability for each affected sentence. A source-traced
  characterization matrix is written before edits and repeated on the candidate. For each
  sentence it records the owner, the readers that load both, the local addition kept, and
  the condition match. Characterization starts green; no manufactured failing test.
- Required regression coverage: `scripts/check_instructions.py`, `scripts.test_instructions`,
  `scripts.test_package`, package build with link validation, native plugin validation.

## Execution

One sequential writer; families 1, 2, 4 in that order, then family 5 after the decision.
Family 3 is assessed but expected to fail the removal test. Line numbers are baseline
`99009ef` lines. The writer applies the removal test to each candidate and may conclude “keep”.

| Family | Candidate (baseline location) | Expected disposition |
| --- | --- | --- |
| 1 | `references/retention.md:24-27` | Remove; `:6` already points to the core |
| 1 | `references/retention.md:48` | Align condition; keep “report the unowned follow-up” |
| 1 | `references/queue.md:43-44` | Align condition; keep “report the missing tracking” |
| 1 | `references/evidence.md:21` first clause | Remove; `:20` already cites the core restrictions |
| 1 | `references/tdd.md:8` | Align condition; keep “use conversation” |
| 1 | `references/corrections.md:11` | Align condition; remove only if no local consequence remains |
| 1 | `references/handoff.md:8-9` | Align condition; keep “state the recovery limit” |
| 1 | `references/visuals.md:56-57` | Align condition; keep “report the reference in the response” |
| 1 | `skills/experiment/SKILL.md:25` | Align condition; keep “declares it in conversation” |
| 1 | `skills/explore/SKILL.md:19` | Keep; added by `33975db` with behavioral evidence |
| 2 | `references/retention.md:34-35` | Remove the copy of the Contract and of queue reconciliation |
| 2 | `references/retention.md:36-39` | Keep; a notes-only reader does not load queue |
| 2 | `references/retention.md:20-21` and `:30-32` | Merge the two statements that direct work uses notes |
| 2 | `references/queue.md:31` and `:52-53` | Remove the second statement that a spec activates tracking |
| 2 | `references/queue.md:50-52` | Point to retention for what notes retain |
| 3 | `references/delegation.md:4-7`, core Personas, References rows | Keep; leaves with granted worker responsibilities do not load Personas; `a709728` placed these deliberately |
| 4 | `skills/batch/SKILL.md:66-68` | Reduce to the pointer to incremental reporting |
| 4 | `references/batch-execution.md:39-43` | Keep the worker obligation and pointer; remove parent steps stated in the execution reference |
| 4 | `skills/batch/SKILL.md:36` “share one pool” | Keep, after review: “the assignment pool” and “the shared pool” in the same file depend on it |
| 4 | Ceiling in `references/batch-use.md:25-27`, default rounds in `skills/batch/SKILL.md:39` | Keep; the reader has not loaded the owner when the value is needed |
| 5 | Core Work loop sentence, `references/retention.md:55-57` | Add sequencing and the long-run condition to the core; retention points to the core |
| 5 | `skills/implement/SKILL.md:34-38` | Keep unchanged; it already states every condition |

- Verification, run from the repository root:
  `python3 scripts/check_instructions.py` → “Instruction checks passed.”;
  `python3 -m unittest scripts.test_instructions scripts.test_package` → 21 tests OK;
  `python3 scripts/package.py --output tmp/consolidate-restated-rules-package` → exit 0;
  `claude plugin validate plugins/lusona` and `claude plugin validate .claude-plugin/marketplace.json` → pass;
  `git diff --check` → no output.

## Evidence

Baseline: revision `99009ef636af825ab8ecdf623b008b5e25ed794f`, canonical plugin 2.0.4. Starting
untracked files: this spec and `docs/lusona/notes/instruction-removal-component-previews-verification-caching.md`.

- Baseline checks, coordinator, 2026-11-09: `python3 scripts/check_instructions.py` passed;
  `python3 -m unittest scripts.test_instructions scripts.test_package` ran 21 tests, OK;
  `git diff --check` produced no output.
- Coordinator read 47 of the 48 canonical Markdown sources under `plugins/lusona/` in full, and
  searched `references/interview-examples.md` for the family phrases (no match), before selecting
  the families. No new outright contradiction was found outside the differing conditions above.

### Characterization matrix

Baseline written by the writer leaf before any edit under `plugins/lusona/`; every quote and
line number was re-read from disk at `99009ef`. Paths are relative to `plugins/lusona/`.
Abbreviations: **Contract-R** = `README.md:85-88` (“Explicit read-only, no-save, destination
limits, and write permissions prevail; report prevented saving and provide the result through a
permitted channel. Delegated read-only workers return findings for the coordinator to save
within its authority.”). **Contract-T** = `README.md:89` (“Creating, updating, or using a spec
requires its queue tracking under queue.”). **All roles** = `README.md:5-6` requires every role
to read the Contract once per context. Baseline result for every row: the rule is stated at the
baseline location and at the owner, and each listed reader can reach both.

| ID | Baseline location | Rule stated | Owner | Readers of the copy and how each loads the owner | Local addition | Conditions match owner? | Adding commit; behavioral evidence for this placement? | Disposition | Candidate result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1-1 | `references/retention.md:24-26` | “Explicit no-save/read-only restrictions and write permissions prevail; report prevented saving and return the result through a permitted channel. A delegated read-only worker returns findings to its coordinator, which saves them within its own write authority.” | Contract-R | Any role saving findings; All roles. `retention.md:6` also links the Contract. | None | No: omits destination limits | `ebca32b`. Its evidence (`docs/lusona/evidence/2026-10-30-durable-records`) ran a Specify no-save case against the whole candidate; the same commit added the sentence to the Contract. Not placement-specific. | Remove | Removed. Rule available at `README.md:86-89`; `retention.md:6` still links it. No consequence lost. |
| F1-2 | `references/retention.md:48` | “When saving is restricted, report the unowned follow-up through a permitted channel.” | Contract-R | Any role closing an assignment; All roles | Names the object to report: the unowned follow-up | No: “restricted” | `5e39db8`; cites a consuming-project observation, no trial of this sentence | Align | Aligned at `retention.md:45`: “When saving is prevented, report the unowned follow-up through a permitted channel.” Local consequence kept. |
| F1-3 | `references/queue.md:43-44` | “These requirements remain subject to explicit no-save/read-only restrictions and write permissions. If saving is prohibited or unavailable, report the missing tracking through a permitted channel.” | Contract-R | Roles using a spec or the queue; All roles | Names the object to report: the missing tracking | No: omits destination limits; “prohibited or unavailable” | `61ec6da`. Its evidence (`2026-10-30-spec-queue`) ran a Specify no-save case against the whole candidate. Not placement-specific. | Align | Aligned at `queue.md:43-44`: condition is a link to the Contract plus “When saving is prevented”; “report the missing tracking through a permitted channel” kept. |
| F1-4 | `references/evidence.md:21` first clause | “Read-only/no-save restrictions prevail;” | Contract-R | Roles retaining material evidence; All roles. `evidence.md:20` already says “under retention and the core's write restrictions”. | None in this clause. The rest of the sentence (“saving does not authorize new collection, implementation, or external actions”) is local and stays. | No: omits destination limits and write permissions | `ebca32b`; as F1-1 | Remove clause | Clause removed. `evidence.md:20` still cites the core restrictions; `evidence.md:21` keeps “Saving does not authorize new collection, implementation, or external actions.” |
| F1-5 | `references/tdd.md:8` | “use conversation when saving is prohibited or unavailable.” | Contract-R | Roles selecting or recording TDD; All roles | Names the channel: conversation | No: “prohibited or unavailable” | `ebca32b`; as F1-1 | Align | Aligned at `tdd.md:8`: “when saving is prevented, use conversation.” Local consequence kept. |
| F1-6 | `references/corrections.md:11` | “use the permitted channel when saving is prohibited or unavailable.” | Contract-R | Roles correcting an observed failure; All roles | Applies the channel to correction counts and evidence, which Contract-R's “the result” does not plainly cover | No: “prohibited or unavailable” | `ebca32b`; as F1-1 | Align | Aligned at `corrections.md:11`: “when saving is prevented, use the permitted channel.” Kept, not removed, because of the local application to counts and evidence. |
| F1-7 | `references/handoff.md:8-9` | “If saving is prohibited or unavailable, return the handoff through the permitted channel and state the recovery limit.” | Contract-R | Roles checkpointing or handing off; All roles | “state the recovery limit” | No: “prohibited or unavailable” | `c00ca50` (refactor); no behavioral evidence | Align | Aligned at `handoff.md:8-9`: “If saving is prevented, return the handoff through the permitted channel and state the recovery limit.” |
| F1-8 | `references/visuals.md:56-57` | “within the core write authority and no-save restrictions; otherwise report the reference in the response.” | Contract-R | Roles retaining a chosen visual; All roles | “report the reference in the response” | No: omits read-only and destination limits; “otherwise” | `3c6f053`; message says follow-up behavioral validation is pending | Align | Aligned at `visuals.md:56-58`: condition is a link to the Contract (“core recording authority and restrictions”, the link text `retention.md:6` uses) plus “when saving is prevented, report the reference in the response.” |
| F1-9 | `skills/experiment/SKILL.md:25` | “No-save work declares it in conversation.” | Contract-R | Experiment role; All roles | Declares the trial design in conversation | No: “No-save” only | `6bcd4b0`; evidence is for the commit as a whole, not this sentence | Align | Aligned at `skills/experiment/SKILL.md:25`: “When saving is prevented, declare it in conversation.” |
| F1-10 | `skills/explore/SKILL.md:19` | “honor no-save/read-only restrictions.” | Contract-R | Explore role; All roles | None | No: omits destination limits and write permissions | `33975db`. Yes: the message says “Clarify when Explore saves reusable synthesis” and cites `2026-11-05-natural-next-action`, whose explore case tested saving. | Keep (fails test 4); outside the writer's ownership | Unchanged. |
| F2-1 | `references/retention.md:34-35` | “Creating, updating, or using a spec requires tracking under queue, regardless of the skill used.” | Contract-T; `references/queue.md:31` | Any role saving; All roles | None | Yes | `61ec6da`; evidence ran against the whole candidate, which stated the rule in the Contract and queue too. Not placement-specific. | Reduce to a pointer to queue | Reduced to a pointer at `retention.md:32`: “A spec's queue tracking follows the queue rules.” Rule available at `README.md:90` and `queue.md:31`. |
| F2-2 | `references/retention.md:35` | “Reconcile only the selected item, preserving lifecycle state, Icebox, and history.” | `references/queue.md:34-38` and `:40-41` | Applies only when a spec is used; Contract-T and `queue.md:3` require that reader to load queue | None | Yes | `61ec6da`; as F2-1 | Remove | Removed. Rule available at `queue.md:34-38` (reconcile the selected spec; preserve lifecycle state, Icebox placement, and history) and `queue.md:40-41` (do not scan or backfill unrelated specs). |
| F2-3 | `references/retention.md:36-38` | “Notes alone do not require tracking … Existing tracked work remains tracked.” | Itself for notes-only readers; `queue.md:53-54` restates part | A notes-only reader does not load queue | — | — | `61ec6da` | Keep (fails test 1) | Unchanged at `retention.md:33-35`. |
| F2-4 | `references/retention.md:20-21` and `:30-32` | “Other direct implement or refactor work without a spec uses notes.” and “Direct implement/refactor work without a spec may use notes for its agreement, decisions, explicit TDD/source, checks/evidence, and handoff. It can also create a spec directly without Specify; use only relevant template sections.” | Same file; one statement | Same reader reads both | `:30-32` lists what notes hold and allows creating a spec without Specify | No: `:20-21` says other direct work “uses notes”; `:30-32` says direct work “may use notes for” the listed items and that direct work, without the “Other” limit, can also create a spec | `5e39db8` (`:20-21`), `61ec6da` (`:30-32`); neither cites a trial of the duplicate wording | Merge at `:20-21`; `:14-20` unchanged | Merged at `retention.md:20-23`, as corrected in round 1: “Other direct implement or refactor work without a spec uses notes, which may hold its agreement, decisions, explicit TDD/source, checks/evidence, and handoff. Any direct implement or refactor work can also create a spec directly without Specify, using only relevant template sections.” This keeps “uses notes” from `5e39db8`, “may” for the listed contents, and the spec option for any direct work. `retention.md:30` keeps “Notes do not require a full spec or execution plan.” Lines 14-20 are byte-identical to baseline (`cmp` against `git show HEAD`). |
| F2-5 | `references/queue.md:52-53` | “Creating a spec activates the tracking requirement;” | `references/queue.md:31` (“Every new spec requires a row … regardless of which skill creates it.”) | Same file | None | Yes | `61ec6da`; as F2-1 | Remove clause; keep “existing tracked work remains tracked” | Clause removed. `queue.md:31` states the rule; `queue.md:51` keeps “Existing tracked work remains tracked.” |
| F2-6 | `references/queue.md:50-52` | “Direct work without a spec may remain untracked and retain agreement, decisions, TDD/source, checks/evidence, and handoff in notes under retention, which also states when a spec is required.” | `references/retention.md:30-32` | The role that saves those notes loads retention (`retention.md:3`; `README.md:82-84`) | “may remain untracked” stays | Yes | `61ec6da`; as F2-1 | Reduce to a pointer to retention | Reduced to a pointer at `queue.md:50-51`: “Direct work without a spec may remain untracked; retention states what its notes retain and when a spec is required.” The list is at `retention.md:21-22`. |
| F3-1 | `references/delegation.md:4-7`; `README.md:200-204`; `README.md:111-112`; `references/worker-lifecycle.md:3-5`; `references/model-routing.md:3` | Read model routing before dispatch; read worker lifecycle when responsible for workers or results, after results and before closing or handing off; leaves only for granted responsibilities | `README.md:200-204` (Personas and subagents) | Coordinators load Personas (`README.md:6`). Leaves do not; a leaf granted worker responsibilities reads `delegation.md` and the two procedure headers only. | `README.md:111-112` are catalog rows; the two procedure headers are each file's own read condition | Yes | `a709728` placed the delegation and core wording deliberately one day before baseline, with evaluation-harness changes | Keep all (fails test 1 for leaves; test 4) | Unchanged. Working-tree locations: `delegation.md:4-7`, `README.md:201-205`, `README.md:112-113`, `worker-lifecycle.md:3-5`, `model-routing.md:3`. |
| F4-1 | `skills/batch/SKILL.md:66-68` | “persist each result before further dispatch or waiting, and update its queue row only when its state, blocker, or next action changed, without waiting for batch closeout.” | `skills/batch/references/execution.md:48-53`, `:59-61` | Batch coordinator; `SKILL.md:40` requires reading the execution reference before dispatch, so it is loaded before any result arrives | None | No: the owner adds “After any in-progress serialized operation reaches a safe boundary” | `215cdfd` (initial extraction); no evidence | Reduce to the existing pointer | Reduced to the pointer at `skills/batch/SKILL.md:66`. Steps available at `skills/batch/references/execution.md:48-53` and `:59-61`. The owner sentence at `execution.md:49-52` was reworded in correction round 1 so that “Before further dispatch or waiting” governs inspect, persist, and the conditional row update; before that rewording the deadline attached only to the row update, and this removal would have lost “persist each result before further dispatch or waiting”. |
| F4-2 | `references/batch-execution.md:39-43` | “The parent applies incremental reporting, persisting the result and recovery pointers before further dispatch or waiting, and updating the item's `docs/lusona/work.md` row only when its state, blocker, or next action changed. Queue updates and eligible per-item closeout do not wait for batch-wide consolidation.” | `skills/batch/references/execution.md:48-53`, `:59-61` | Coordinator: loads the execution reference before dispatch. Assigned delegates: do not load it, and the parent steps do not apply to them; they need only “Workers report each assignment result as soon as it is available.” | Worker obligation in the first sentence stays | No: same omission as F4-1 | `215cdfd`; no evidence | Keep the worker sentence and pointer; remove parent steps | At `batch-execution.md:39-41`: worker sentence kept; “The parent applies incremental reporting to each result as it arrives.” Parent steps available at `skills/batch/references/execution.md:48-53`, `:59-61`. Depends on the same reworded owner sentence at `execution.md:49-52` as F4-1 for “persisting the result … before further dispatch or waiting”. |
| F4-3 | `skills/batch/SKILL.md:36` | “All responsibilities and nested grants share one pool.” | `references/batch-execution.md:32-33`, `:35` | Batch coordinator; `SKILL.md:10` requires reading batch execution at entry | None | Yes | `215cdfd`; no evidence | Keep (changed from Remove in correction round 1: “the assignment pool” at `SKILL.md:39` and “the shared pool” at `SKILL.md:69` depend on this sentence to introduce the pool) | Restored at `skills/batch/SKILL.md:36`; lines 36-37 are byte-identical to `HEAD`. `batch-execution.md:32-33` and `:35` also state the rule. |
| F4-4 | `references/batch-use.md:25-27` | Default ceiling four, five when selected, reduced by host capacity; shared ceiling | `skills/batch/SKILL.md:35-37` | Reader gives start or resume guidance (status role) and has not loaded the batch skill | — | — | `215cdfd` | Keep (fails test 1) | Unchanged. |
| F4-5 | `skills/batch/SKILL.md:39` | “Default to two corrective rounds per item.” | `skills/batch/references/execution.md:115-116` | The allowance is recorded when the batch is established, before `SKILL.md:40` requires the execution reference | — | — | `215cdfd` | Keep (fails test 1 at the time of use) | Unchanged. |
| F5-1 | `README.md:59-60` (Work loop) | “Planning belongs to implementation; tasks need dependencies, uncertainty, coordination, recovery, or a requested plan.” Lists 5 conditions: dependencies, uncertainty, coordination, recovery, requested plan. Lacks sequencing and the long run. | Itself; this is the owner. Reference list, unchanged: `templates/spec.md:56-58` states 7 conditions (sequencing, dependencies, uncertainty, coordination, recovery, a long run whose earlier context will be summarized before it finishes, a requested plan). | All roles read Work loop once per context (`README.md:5-6`) | — | No: the owner is the shortest list. `retention.md`, `skills/implement/SKILL.md`, and the template each state conditions it lacks. | `6bcd4b0`; evidence is for the commit as a whole, not this list. The copies with the long run date from `215cdfd`, before this sentence. | Edit the owner to list all 7 conditions (user decision “Add it to the core”, plus sequencing per the Decisions bullet) | Edited at `README.md:59-61`: “Planning belongs to implementation; tasks need sequencing, dependencies, uncertainty, coordination, recovery, a long run whose earlier context will be summarized before it finishes, or a requested plan.” Same 7 conditions as `templates/spec.md:56-58`. `README.md:62` (“Small clear work needs no task list; …”) and the `## Work loop` heading are unchanged; `diff` against the pre-edit copy shows only this sentence. |
| F5-2 | `references/retention.md:55-57` | “Add an execution section only when sequencing, dependencies, uncertainty, recovery, or a long run whose earlier context will be summarized before it finishes makes it useful; straightforward work needs no task list.” Lists 5 conditions: sequencing, dependencies, uncertainty, recovery, long run. Lacks coordination and a requested plan. | `README.md:59-60` for the conditions; `README.md:61` (“Small clear work needs no task list”) for the second clause | Any role saving a change record; All roles read Work loop | The subject: the execution section of a change record. The conditions and the no-task-list clause add nothing. | No: lacks coordination and a requested plan; “straightforward” where the owner says “Small clear” | `215cdfd` (initial extraction); no evidence | Reduce to a pointer that keeps the subject; remove the no-task-list clause | Reduced to a pointer at `retention.md:52-53`: “Add an execution section only when the core task conditions make it useful.”, linking `../README.md#work-loop`. Subject kept. The no-task-list clause is removed; the rule is available at `README.md:62`. `retention.md:54` (“Tasks reference acceptance criteria …”) is unchanged. |
| F5-3 | `skills/implement/SKILL.md:34-38` | “Choose planning depth from dependencies, uncertainty, coordination, and recovery needs, including a long run whose earlier context will be summarized before it finishes. … Add an optional execution section when sequencing helps. … expand later tasks only to resolve dependencies or meet an explicit planning request.” States all 7 conditions across the bullet. | `README.md:59-60` | Implement role; All roles read Work loop | Planning-depth procedure: outcome and checks, next useful increment, when to expand later tasks | Yes after the F5-1 edit (same 7 conditions) | `215cdfd`; no evidence | Keep unchanged (assignment; outside write ownership) | Unchanged; `git diff --stat -- plugins/lusona/skills/implement plugins/lusona/templates` is empty. |

Line numbers: the baseline columns use `99009ef` line numbers. The Candidate result column uses
working-tree line numbers after correction round 1. In the working tree Contract-R is
`README.md:86-89` and Contract-T is `README.md:90`, because the F5-1 edit added one line above them.

Line-number correction to the Execution table: the F1-1 sentence occupies `retention.md:24-26`.
Line 27 (“Reuse the existing owner; …”) is a different rule and is not part of this candidate.

### Candidate verification

Writer leaf, 2026-11-09, working tree on top of `99009ef`, run from the repository root.
The three per-family checks ran after family 1, after family 2, and after family 4, and passed
each time. Results on the final tree:

- `python3 scripts/check_instructions.py`: “Instruction checks passed.”, exit 0.
- `python3 -m unittest scripts.test_instructions scripts.test_package`: 21 tests, OK.
- `git diff --check`: no output, exit 0.
- `python3 scripts/package.py --output tmp/consolidate-restated-rules-package`: exit 0; built
  `lusona-2.0.4.zip` with its manifest, catalog, link, and content checks.
- `claude plugin validate plugins/lusona`: “Validation passed”, exit 0, with one advisory about
  an install line in the plugin README (not a failure; the README is unchanged).
- `claude plugin validate .claude-plugin/marketplace.json`: “Validation passed”, exit 0.
- `sed -n 14,20p plugins/lusona/references/retention.md` compared with the same lines of
  `git show HEAD:plugins/lusona/references/retention.md` using `cmp`: identical.
- `git diff HEAD --stat` over templates, scripts, `plugins/lusona/README.md`, root READMEs,
  `CHANGELOG.md`, `evals/`, and `scripts/`: empty.

`git diff --stat -- plugins/lusona`:

```text
 plugins/lusona/references/batch-execution.md |  6 ++----
 plugins/lusona/references/corrections.md     |  2 +-
 plugins/lusona/references/evidence.md        |  3 +--
 plugins/lusona/references/handoff.md         |  2 +-
 plugins/lusona/references/queue.md           | 12 +++++-------
 plugins/lusona/references/retention.md       | 16 ++++++----------
 plugins/lusona/references/tdd.md             |  2 +-
 plugins/lusona/references/visuals.md         |  5 +++--
 plugins/lusona/skills/batch/SKILL.md         |  8 +++-----
 plugins/lusona/skills/experiment/SKILL.md    |  2 +-
 10 files changed, 24 insertions(+), 34 deletions(-)
```

Not run: live agent-behavior trials, installation, interactive use, PowerShell, and
`agy plugin validate`. The static checks verify links, packaging, and six forbidden phrases in
skill bodies; rule preservation rests on the matrix above and on review of the diff. Family 5
is not edited.

Family 5, writer leaf, 2026-11-09, after the user decision “Add it to the core”. Rows F5-1 to
F5-3 were added to the matrix before the edit. This supersedes “Family 5 is not edited” and the
statement that `plugins/lusona/README.md` is unchanged, both above. Results on the final tree:

- `diff` of `plugins/lusona/README.md` against its pre-edit copy: one sentence changed
  (old line 60; new lines 60-61). `diff` of `references/retention.md` against its pre-edit copy:
  one sentence changed (old lines 51-53; new lines 51-52).
- `git diff --stat -- plugins/lusona/skills/implement plugins/lusona/templates`: empty.
- `python3 scripts/check_instructions.py`: “Instruction checks passed.”, exit 0.
- `python3 -m unittest scripts.test_instructions scripts.test_package`: 21 tests, OK.
- `git diff --check`: no output, exit 0.
- `python3 scripts/package.py --output tmp/consolidate-restated-rules-package-2`: exit 0; built
  `lusona-2.0.4.zip`.
- `claude plugin validate plugins/lusona`: “Validation passed”, exit 0.
- `claude plugin validate .claude-plugin/marketplace.json`: “Validation passed”, exit 0.

`git diff --stat -- plugins/lusona` after family 5:

```text
 plugins/lusona/README.md                     |  3 ++-
 plugins/lusona/references/batch-execution.md |  6 ++----
 plugins/lusona/references/corrections.md     |  2 +-
 plugins/lusona/references/evidence.md        |  3 +--
 plugins/lusona/references/handoff.md         |  2 +-
 plugins/lusona/references/queue.md           | 12 +++++-------
 plugins/lusona/references/retention.md       | 21 ++++++++-------------
 plugins/lusona/references/tdd.md             |  2 +-
 plugins/lusona/references/visuals.md         |  5 +++--
 plugins/lusona/skills/batch/SKILL.md         |  8 +++-----
 plugins/lusona/skills/experiment/SKILL.md    |  2 +-
 11 files changed, 28 insertions(+), 38 deletions(-)
```

Not run for family 5: live agent-behavior trials, installation, interactive use, PowerShell,
and `agy plugin validate`. The core sentence change adds two conditions under which tasks are
warranted; no trial measured its effect on planning behavior.

Correction round 1, writer leaf, 2026-11-09, from the independent review's three findings.

1. `skills/batch/references/execution.md:49-52` (owner of incremental reporting): reworded to
   “Before further dispatch or waiting, and after any in-progress serialized operation reaches a
   safe boundary, inspect the result and its evidence, persist the assignment outcome and
   recovery references, and, when the item's state, blocker, or next action changed, update its
   row in `docs/lusona/work.md`.” The deadline now governs inspect, persist, and the conditional
   row update. Every earlier element is kept. `diff` against the pre-correction copy shows only
   lines 49-52 changed; “Do not rewrite an unchanged row.” and the rest of the file are unchanged.
2. `references/retention.md:20-23`: the merge wording now reads “uses notes, which may hold …”
   and “Any direct implement or refactor work can also create a spec directly without Specify,
   using only relevant template sections.” Lines 14-20 are byte-identical to `HEAD` (`cmp`). The
   edit added one line, so later retention line numbers moved by one; the matrix is updated.
3. `skills/batch/SKILL.md:36-37`: restored “All responsibilities and nested grants share one
   pool.”; both lines are byte-identical to `HEAD`. Matrix row F4-3 is now Keep. The remaining
   diff in that file is F4-1 only.

Matrix fixes: Candidate result cells now use working-tree line numbers after this round
(Contract-R `README.md:86-89`, Contract-T `README.md:90`, Personas `README.md:201-205`, “the
shared pool” at `skills/batch/SKILL.md:69`); the F2-4 conditions cell no longer claims the two
statements were compatible; F4-1 and F4-2 record their dependence on the reworded owner.

Rerun on the final tree, from the repository root:

- `python3 scripts/check_instructions.py`: “Instruction checks passed.”, exit 0.
- `python3 -m unittest scripts.test_instructions scripts.test_package`: 21 tests, OK.
- `git diff --check`: no output, exit 0.
- `python3 scripts/package.py --output tmp/consolidate-restated-rules-package-3`: exit 0; built
  `lusona-2.0.4.zip`.
- `claude plugin validate plugins/lusona`: “Validation passed”, exit 0.
- `claude plugin validate .claude-plugin/marketplace.json`: “Validation passed”, exit 0.

`git diff --stat -- plugins/lusona` after correction round 1 (this supersedes the two listings above):

```text
 plugins/lusona/README.md                           |  3 ++-
 plugins/lusona/references/batch-execution.md       |  6 ++----
 plugins/lusona/references/corrections.md           |  2 +-
 plugins/lusona/references/evidence.md              |  3 +--
 plugins/lusona/references/handoff.md               |  2 +-
 plugins/lusona/references/queue.md                 | 12 +++++-------
 plugins/lusona/references/retention.md             | 22 +++++++++-------------
 plugins/lusona/references/tdd.md                   |  2 +-
 plugins/lusona/references/visuals.md               |  5 +++--
 plugins/lusona/skills/batch/SKILL.md               |  4 +---
 .../lusona/skills/batch/references/execution.md    |  8 ++++----
 plugins/lusona/skills/experiment/SKILL.md          |  2 +-
 12 files changed, 31 insertions(+), 40 deletions(-)
```

Correction counts for these review findings: one round, with material progress (all three
findings corrected and verified by the checks above). Consecutive rounds without material
progress: 0. Total rounds: 1. Not run: live agent-behavior trials, installation, interactive
use, PowerShell, and `agy plugin validate`.

### Independent review

Reviewer: a separate read-only leaf started without the coordinator's context (general-purpose
agent, Opus model), 2026-11-09. It read the Agreement, Removal test, criteria, and decisions,
judged every hunk of `git diff HEAD -- plugins/lusona` from the sources, and only then read the
matrix and candidate verification as claims to verify.

- First pass: no blocking finding. One should-fix: with both batch copies reduced to pointers,
  the deadline “persist before further dispatch or waiting” remained only in
  `skills/batch/references/execution.md:49-52`, where the phrase attached grammatically to the
  row update alone. Two optional findings: the retention merge changed “may use notes for” to
  “uses notes for” and narrowed the subject of “can also create a spec”; the batch skill's pool
  terms lost their introducing sentence. It also reported shifted line numbers in four matrix cells.
- Correction round 1 (writer): reworded the execution-reference sentence so the deadline governs
  inspect, persist, and the conditional row update; reworded the retention sentence to restore
  “may” and the unqualified subject; restored “All responsibilities and nested grants share one
  pool.” Matrix cells corrected. Consecutive rounds without material progress: 0; total: 1.
- Second pass: all three findings resolved, no new finding. AC1–AC4 pass. The other nine changed
  files match the first pass. The reviewer reran the instruction checker (passed), the 21 unit
  tests (OK), and `git diff --check` (no output). It did not rerun the package build or native
  plugin validation; the writer's results for those are in Candidate verification.
- After the review the coordinator changed one pronoun in `skills/experiment/SKILL.md:25`
  (“declare it” to “declare the design”), because “it” could be read as the prevention. The
  reviewer did not see this edit. `python3 -m unittest evals/evidence-aware/test_run.py` ran 8
  tests, OK; its suite lock pins no plugin file.
- Coordinator: inspected every hunk of the final diff, reran the instruction checker, the 21 unit
  tests, and `git diff --check` after the corrections, and accepted the result.

Limits: no live agent-behavior trial, installation, interactive use, PowerShell, or `agy`
validation was run. Two edits change stated conditions and were not measured: the aligned
save-restriction copies, and the core Work loop sentence, which now names sequencing and a long
run as conditions for tasks. Static characterization shows where each rule is stated; it does
not show agent compliance.

### Version and commit follow-up — 2026-11-09

The user requested “bump version and commit”. Applied patch version 2.0.5 to all five native
manifests and all five README version labels, and added the dated untagged-source changelog
entry. A local commit is authorized; push and publication are not. The independent review
covers the instruction diff; the coordinator inspected the metadata diff.

- `python3 -m unittest scripts.test_instructions scripts.test_package`: 21 tests OK after the bump.
- `python3 scripts/check_instructions.py`: passed.
- `python3 scripts/package.py --output tmp/lusona-2.0.5-release`: exit 0; archive `lusona-2.0.5.zip` produced.
- `claude plugin validate plugins/lusona` and `claude plugin validate .claude-plugin/marketplace.json`: passed.
- `agy plugin validate plugins/lusona --strict`: passed.
- `git diff --check`: no output.
- Installation and interactive behavior remain untested.

### Findings outside this scope

Not edited. Recorded for a possible follow-up.

- `references/tdd.md:7`, `skills/implement/SKILL.md:73-74`, and `references/model-routing.md:36`
  say “owning change record”, while retention lets notes own spec-free work, including its TDD.
- “shared handoffs” (batch skill, batch execution, batch use, naming), “queue and batch
  handoffs” (`references/queue.md:5`), and “the handoffs saved in them” (core Contract) name
  the same coordinator-only handoffs with three terms. The queue template has no handoff section.
- `references/retention.md:12` and `:27` both say to reuse the existing owner; `:3-4` and `:87`
  both point to closeout. `references/closeout.md:21-29` repeats week numbering and
  initialization rules that `references/work-record.md:52-54` and `references/retention.md:83-86` state.
- `references/retention.md:6-11` and `skills/explore/SKILL.md:17-19` restate the Contract's
  save-without-request rule. The explore copy was added with behavioral evidence (`33975db`).

## Current handoff

- Authorized work: completed as agreed; source: user request and answers on 2026-11-09. TDD
  targeted, selected by the user this session. The user then authorized the 2.0.5 version bump
  and a local commit. No push or publication is authorized.
- Completed and remaining work: AC1–AC6 pass. 12 files under `plugins/lusona/` changed, 31
  insertions and 40 deletions. Nothing remains in this scope.
- Resume context: diff base `99009ef`; all edits are uncommitted working-tree changes. Scratch
  and package output are under `tmp/consolidate-restated-rules*`.
- Workers: the writer and the reviewer returned completed assignments; no active operations,
  children, or write ownership. The host confirmed both runs ended.
- Correction rounds: review findings, consecutive 0, total 1; resolved.
- Next action: coordinator commits the verified increment. A follow-up for the findings outside this scope
  is an Ideas row in the queue.
