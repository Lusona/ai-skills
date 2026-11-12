# Rule inventory of the 34186da core README and references

Date: 2026-11-11. Work item W15 of [spec 20261111](../specs/20261111-loop-principles-and-skill-rewrite.md).
Baseline commit: `34186da`. Sources were read with `git show 34186da:<path>`, not from the working tree.

## Purpose

This note lists every rule-bearing sentence of the plugin README, the 20 plugin-level reference files and the one per-skill reference file (`skills/batch/references/execution.md`) at `34186da`.
Each row is tagged with the loop principles (P1-P8) it implements, the principles or voice rules (V1-V9) it conflicts with,
the contract item (K1-K5) it defines, and its row in the 20261110 core rule mapping.
AC13 uses this inventory as input: every row must later be kept, moved, or removed with a stated reason.
The discarded `drafts/rules.md` was not used.

## Sources

| File | Path at 34186da | Lines | Rows |
| --- | --- | --- | --- |
| readme | `plugins/lusona/README.md` | 211 | 187 |
| batch-execution | `plugins/lusona/references/batch-execution.md` | 57 | 54 |
| batch-use | `plugins/lusona/references/batch-use.md` | 39 | 24 |
| closeout | `plugins/lusona/references/closeout.md` | 29 | 27 |
| commits | `plugins/lusona/references/commits.md` | 65 | 58 |
| corrections | `plugins/lusona/references/corrections.md` | 26 | 20 |
| delegation | `plugins/lusona/references/delegation.md` | 70 | 57 |
| evidence | `plugins/lusona/references/evidence.md` | 71 | 49 |
| files | `plugins/lusona/references/files.md` | 43 | 36 |
| handoff | `plugins/lusona/references/handoff.md` | 12 | 11 |
| interview-examples | `plugins/lusona/references/interview-examples.md` | 123 | 25 |
| interviews | `plugins/lusona/references/interviews.md` | 26 | 28 |
| model-routing | `plugins/lusona/references/model-routing.md` | 39 | 32 |
| naming | `plugins/lusona/references/naming.md` | 47 | 42 |
| queue | `plugins/lusona/references/queue.md` | 62 | 63 |
| retention | `plugins/lusona/references/retention.md` | 83 | 75 |
| tdd | `plugins/lusona/references/tdd.md` | 36 | 32 |
| visuals | `plugins/lusona/references/visuals.md` | 92 | 66 |
| work-record | `plugins/lusona/references/work-record.md` | 67 | 56 |
| worker-lifecycle | `plugins/lusona/references/worker-lifecycle.md` | 30 | 27 |
| workflow-guide | `plugins/lusona/references/workflow-guide.md` | 71 | 57 |
| execution | `plugins/lusona/skills/batch/references/execution.md` | 167 | 141 |
| Total | | 1466 | 1167 |

## Conventions

- ID: `<file-stem>-NNN`, numbered in source order per file; the README stem is `readme`. IDs are fixed for this baseline.
- Lines: source line range at `34186da`. Several rows can share a line.
- Rule: verbatim source text. Line breaks are joined with single spaces, list markers (`- `, `1. `) and blockquote markers (`> `) are removed, and `|` is escaped as `\|`. A table row keeps its cell separators.
- Splitting: one row per sentence. A sentence with clauses joined by `; ` is split at each semicolon outside parentheses and code, because each clause states a separate rule. Four enumerations stay whole: evidence-024, delegation-018, delegation-019, visuals-057. Nine sentences that join two instructions with `and` or a comma are split at a listed point (`SPLITS` in `tmp/w15/segment.py`): readme-043/044/045, batch-execution-026/027, batch-execution-034/035, commits-023/024, commits-027/028, commits-045/046, tdd-021/022, worker-lifecycle-025/026.
- Grouping: each table row is one row (header rows have Kind `not a rule`). Each fenced code block, each blockquote, and each `**User:**`/`**Assistant:**` dialogue in interview-examples is one `example` row.
- Kind: `rule` = instructs or constrains agent behavior; `definition` = defines a term, state, format, or fact the rules rely on; `example` = illustration; `catalog` = index or lookup table row; `not a rule` = table header, connector ("For example:") or file preamble with no rule content. A sentence that says X does not authorize, establish, prove, count as, or require Y is a `rule`, because it constrains what the agent may conclude or do.
- Principles: P-IDs the row implements. `—` = no principle; 334 of 670 rule rows have none; most are operational detail (paths, helper behavior, formatting).
- Conflicts: P- or V-IDs the row contradicts or violates, with a reason of 12 words or fewer. Tests applied:
  - P1: the row fixes an order of skills or phases, or requires a skill regardless of the unresolved need.
  - P2: the row drops carried state (outcome, decisions, authority, TDD, evidence, uncertainty) at a handoff or between passes.
  - P3: the row lets a prior decision block new input, or limits revisiting a decision without the user.
  - P4: the row revises a decision without marking the superseded one with date and source, drops its rationale, or lets a stale record reinstate it.
  - P5: the row permits stating behavior or completion without an observed check.
  - P6: the row lets the agent change outcomes, contracts, TDD level or consequential commitments without the user, or treats a spec, plan, ADR or queue state as authorization.
  - P7: the row requires a new command or approval for bounded authorized work, pauses unaffected work, or omits the resumption prerequisite.
  - P8: the row lets a task reply end without a next action and owner, or with "none" and no reason.
  - V1: third-person address of a role or skill ("Leaves read", "The coordinator alone updates") instead of an imperative. Declarative policy statements are not tagged.
  - V2: preamble that describes the file or restates scope before the action.
  - V3 (script): the source sentence exceeds 40 words (decision 12 limit); every row split from that sentence is tagged. User decision 2026-11-11 (W15 review, relayed by the coordinator): V3 counts only sentences over 40 words; a sentence split at `;` or a listed split point is not a V3 finding by itself.
  - V4 (script): uses worker, subagent, teammate, child(ren), parent, or delegate (noun) for the terms Leaf or Coordinator defined in the workflow-guide Terminology table.
  - V5: banned hedge from `scripts/check_voice.py` (script), or a hand-tagged vague condition ("when useful", "by default", "proportionate").
  - V6: banned filler term (script), or a hand-tagged figurative phrase.
  - V7: vague size or count ("small", "large") with no number.
  - V8 (script): the row belongs to a duplicate group (see Summary); hand-tagged when the row only points to another file instead of stating the action.
  - V9: rationale or explanation in instruction text that does not change the action.
- Contract: K-ID when the row defines contract vocabulary, paths, or commands: K1 skill names or `/lusona:<skill>`; K2 `docs/lusona/` paths, `YYYYMMDD-slug` IDs, queue states and sections; K3 work-record helper commands, arguments, output, exit codes; K4 TDD levels, the four reply statuses, the authority rules naming specs, plans, ADRs or queue states.
- 20261110 row: the row number in the [Core rule mapping (AC8)](../specs/20261110-standard-skill-template-and-inline-rules.md#core-rule-mapping-ac8). That mapping covers only README rules, so every reference row is `none`; reference rows that restate a README rule are linked through a duplicate group instead.
- Coverage: `scripts/check_rule_inventory.py` (see Coverage check).
- Unreviewed rows: the `execution` rows were added 2026-11-11 (W13 correction N7) with Rule text segmented by the same rules (`tmp/w13fix/segment_exec.py`, which reuses `tmp/w15/segment.py` without `SPLITS`). Their Kind, Principles, Conflicts and Contract cells are `unreviewed` and are not tagged yet. The Summary tables below exclude these 141 rows.

## readme (`plugins/lusona/README.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| readme-001 | L5-L6 | All roles read Work loop, Contract, TDD, Review and communication, Assigned leaves, and Context budget once per context. | rule | — | V1: third-person role address, not imperative | — | 1 |
| readme-002 | L6-L7 | Coordinators also read Questions and next actions and Personas and subagents. | rule | — | V1: third-person role address, not imperative; V4: "subagents" used for Leaf or Coordinator | — | 1 |
| readme-003 | L7-L8 | Use References to locate applicable procedures not already linked from your skill or assignment. | rule | — | — | — | 1 |
| readme-004 | L8 | Read complete applicable procedures, following role/section guidance; | rule | — | V5: "following role/section guidance" names no condition | — | 1 |
| readme-005 | L8-L9 | optional examples/catalogs permit excerpts. | rule | — | — | — | 1 |
| readme-006 | L9 | Leaves receive relevant procedures with their assignment. | rule | — | V1: third-person role address, not imperative | — | 1 |
| readme-007 | L11 | Workflow role follows assigned responsibilities. | definition | — | — | — | 2 |
| readme-008 | L11-L12 | A separate host task or a prohibition on children does not establish a leaf role. | rule | — | V4: "children" used for Leaf or Coordinator | — | 2 |
| readme-009 | L12 | Assignments explicitly name the workflow role and responsibilities. | rule | — | V1: third-person statement of a coordinator duty | — | 2 |
| readme-010 | L14 | Identify the source of current supplied or demonstrably inherited text; | rule | P5 | — | — | 3 |
| readme-011 | L14 | it satisfies loading. | definition | — | — | — | 3 |
| readme-012 | L15 | Reuse unchanged instructions across skills/assignments; | rule | — | — | — | 3 |
| readme-013 | L15-L16 | load missing or changed text when role, operation, or source changes. | rule | — | — | — | 3 |
| readme-014 | L16 | Installation or another worker's read does not establish availability. | rule | P5 | V4: "worker" used for Leaf or Coordinator; V8: same policy stated in duplicate group D67 | — | 3 |
| readme-015 | L17 | Host/project restrictions apply. | rule | P6 | — | — | 4 |
| readme-016 | L17 | A change is a bounded outcome; | definition | — | V8: same policy stated in duplicate group D47 | — | 5 |
| readme-017 | L17 | a task is one implementation step. | definition | — | V8: same policy stated in duplicate group D47 | — | 5 |
| readme-018 | L18 | Task selection does not authorize its whole change. | rule | P6 | V8: same policy stated in duplicate group D46 | — | 5 |
| readme-019 | L20 | Select the next responsibility from the unresolved need; | rule | P1 | — | — | 6 |
| readme-020 | L20-L21 | when skill selection is unclear, consult the [routing table](references/workflow-guide.md#routing). | rule | P1 | V8: same policy stated in duplicate group D48 | — | 6 |
| readme-021 | L21-L22 | The table is not required reading for a role whose assignment is settled. | rule | P1 | V8: same policy stated in duplicate group D48 | — | 6 |
| readme-022 | L26-L27 | Carry outcome, accepted decisions, authority, explicit TDD/source, evidence, and uncertainty across turns, skills, sessions, and handoffs. | rule | P2 | — | — | 7 |
| readme-023 | L27 | Skills supply expertise, not authority or mandatory phases. | rule | P1, P6 | V8: same policy stated in duplicate group D45 | — | 7 |
| readme-024 | L28 | Answer direct questions first; | rule | — | V8: same policy stated in duplicate group D32 | — | 8 |
| readme-025 | L28-L29 | adapt explanation and experiments to demonstrated understanding, without weakening decisions or evidence. | rule | P5 | — | — | 8 |
| readme-026 | L29 | Reuse settled answers and valid checks. | rule | P2 | V8: same policy stated in duplicate group D33 | — | 8 |
| readme-027 | L31 | Take the next useful bounded authorized action; | rule | P7 | — | — | 9 |
| readme-028 | L31-L32 | compare its result with the outcome, separating facts from assumptions. | rule | P2, P5 | — | — | 9 |
| readme-029 | L32-L33 | Stop inquiry when more exchanges/experiments would not change the outcome or justified next action. | rule | P7 | V8: same policy stated in duplicate group D34 | — | 9 |
| readme-030 | L33 | Continue without another command; | rule | P7 | — | — | 9 |
| readme-031 | L33-L34 | a recommendation does not fulfill an available authorized action. | definition | P7 | — | — | 9 |
| readme-032 | L34-L35 | Treat follow-ups as steering unless they explicitly cancel/replace the objective or request an incompatible one; | rule | P2 | — | — | 9 |
| readme-033 | L35 | preserve progress and honor scope changes. | rule | P2 | — | — | 9 |
| readme-034 | L37 | Pause affected work on user request, unavailable input/capability/authority, or a correction limit; | rule | P7 | — | — | 10 |
| readme-035 | L38 | state why and the exact resumption prerequisite. | rule | P7 | — | — | 10 |
| readme-036 | L38-L39 | Ask for missing decisions, continuing independent authorized work. | rule | P7, P6 | V8: same policy stated in duplicate group D80 | — | 10 |
| readme-037 | L39 | Yielding is not completion; | rule | P7 | — | — | 10 |
| readme-038 | L39 | batches defer through their parent. | rule | P7 | V4: "their parent" used for Leaf or Coordinator | — | 10 |
| readme-039 | L39-L41 | Before correcting or diagnostically probing an observed failed check/review finding, read [correction limits](references/corrections.md); | rule | — | V8: same policy stated in duplicate group D19 | — | 11 |
| readme-040 | L41 | expected task-local TDD red is excluded. | rule | — | V8: same policy stated in duplicate group D20 | — | 11 |
| readme-041 | L43 | When evidence undermines a decision, identify it, the conflict, and affected assumptions; | rule | P3 | P3: trigger limited to evidence, not requirement, spec or measurement | — | 12 |
| readme-042 | L43-L44 | reopen within authority. | rule | P3, P6 | P3: reopens within authority, omits revisiting the decision with user | — | 12 |
| readme-043 | L44-L45 | After authorized revision, reconcile affected assignments/records/handoffs within write ownership, | rule | P4 | — | — | 12 |
| readme-044 | L45 | retain useful superseded rationale, | rule | P4 | P4: keeps only useful rationale, no date and source marking | — | 12 |
| readme-045 | L45 | and report other owners' required corrections. | rule | P4 | — | — | 12 |
| readme-046 | L46 | Resume from the revision; | rule | P4 | — | — | 12 |
| readme-047 | L46 | stale records cannot reinstate a superseded choice. | definition | P4 | — | — | 12 |
| readme-048 | L48-L49 | Relate concrete discovered gaps to established goals: distinguish current blockers from proposed outcomes, report uncertainty and the smallest next action without implying broader completion. | rule | P2 | — | — | 13 |
| readme-049 | L50 | Retain findings under [retention](references/retention.md) within write authority; | rule | — | — | — | 13 |
| readme-050 | L50-L51 | read-only work reports without saving. | rule | P6 | V8: same policy stated in duplicate group D49 | — | 13 |
| readme-051 | L51 | Do not invent requirements or audit the whole product by default. | rule | P6 | V5: "by default" leaves the exception unstated | — | 13 |
| readme-052 | L51-L53 | Findings, proposals, splits, deferrals, and priority changes do not expand authority, batch selection, or accepted priorities. | rule | P6 | — | — | 13 |
| readme-053 | L55 | Before starting a measurement or experiment, read [evidence rules](references/evidence.md). | rule | P5 | V8: same policy stated in duplicate group D27 | — | 14 |
| readme-054 | L56 | Choose routine details within authority without repeated approval; | rule | P6, P7 | — | — | 15 |
| readme-055 | L56-L57 | ask only for missing consequential decisions/commitments, otherwise state uncertainty and continue. | rule | P6, P7 | V8: same policy stated in duplicate group D62 | — | 15 |
| readme-056 | L59 | Adapt routine approaches without weakening acceptance or resetting progress. | rule | P2 | — | — | 16 |
| readme-057 | L59-L60 | Planning belongs to implementation; | definition | — | — | — | 16 |
| readme-058 | L60-L61 | tasks need sequencing, dependencies, uncertainty, coordination, recovery, a long run whose earlier context will be summarized before it finishes, or a requested plan. | rule | — | V8: same policy stated in duplicate group D63 | — | 16 |
| readme-059 | L62 | Small clear work needs no task list; | rule | — | V7: "small clear work" has no measurable bound | — | 16 |
| readme-060 | L62 | retain its substantive output under the Contract. | rule | — | — | — | 16 |
| readme-061 | L66 | Before substantive work, read applicable available domain skills alongside the workflow skill; | rule | — | — | — | 17 |
| readme-062 | L67 | identify them briefly and report missing required skills. | rule | P5 | — | — | 17 |
| readme-063 | L67 | Reuse current text under Loading rules. | rule | — | V8: same policy stated in duplicate group D71 | — | 17 |
| readme-064 | L68 | Users control scope and consequential decisions. | definition | P6 | — | — | 18 |
| readme-065 | L68-L70 | Ask before unauthorized changes to accepted outcomes, contracts, TDD, consequential dependencies/operational commitments, or destructive actions (persistent-data deletion, force-push, changes outside the repository). | rule | P6 | — | — | 18 |
| readme-066 | L70 | Respect host prompts; | rule | P6 | — | — | 18 |
| readme-067 | L71 | preserve unrelated work. | rule | P6 | V8: same policy stated in duplicate group D86 | — | 18 |
| readme-068 | L71-L72 | Choose routine tools, approach, task size, and independent-action order within authority; | rule | P6, P7 | — | — | 18 |
| readme-069 | L72 | prescribe sequence only for correctness, dependencies, explicit choices, or shared state. | rule | P1 | — | — | 18 |
| readme-070 | L73-L74 | Specs, plans, ADRs, queue states (including Ready), discussion, and read-only review grant no implementation authority. | rule | P6 | V8: same policy stated in duplicate group D04 | K4 | 19 |
| readme-071 | L74 | Planning-only stops before execution; | rule | P6 | V8: same policy stated in duplicate group D56 | — | 19 |
| readme-072 | L74 | skill transitions need no new approval. | rule | P1, P7 | — | — | 19 |
| readme-073 | L75-L76 | Authorized implementation/refactoring includes local verified commits unless user/repository rules prohibit them; | rule | P6 | V8: same policy stated in duplicate group D39 | — | 20 |
| readme-074 | L76 | other activities need commit authority. | rule | P6 | — | — | 20 |
| readme-075 | L76-L77 | Push, publication, PRs, external tickets, amendments, and rewriting others' or shared/published history need separate authority. | rule | P6 | V8: same policy stated in duplicate group D40 | — | 21 |
| readme-076 | L77-L78 | Before commits/integration read [commits](references/commits.md), including staging and linear-history rules. | rule | — | — | — | 22 |
| readme-077 | L79 | Project-data paths belong to the consuming repository; | rule | — | V8: same policy stated in duplicate group D10 | K2 | 23 |
| readme-078 | L79-L80 | bundled links resolve relative to the loaded resource. | definition | — | V8: same policy stated in duplicate group D11 | — | 23 |
| readme-079 | L80 | Never save project data in installed plugin resources. | rule | — | V8: same policy stated in duplicate group D10 | — | 23 |
| readme-080 | L80-L81 | Only coordinators write shared queues, batch records, and the handoffs saved in them; | rule | — | V1: third-person role statement, no trigger; V8: same policy stated in duplicate group D08 | — | 24 |
| readme-081 | L81-L82 | a leaf with write ownership of a change record or notes may update that record's current handoff and returns other handoff changes to the parent. | rule | — | V4: "the parent" used for Leaf or Coordinator | — | 24 |
| readme-082 | L83-L85 | Save substantive workflow outputs before handoff or completion, proportionate to the work, under [retention](references/retention.md), which owns the record choice, the spec and queue requirement, and the no-record cases. | rule | P7 | V5: "proportionate to the work" sets no checkable condition; V8: same policy stated in duplicate group D30 | — | 25 |
| readme-083 | L85-L86 | Save a substantive synthesis when it becomes useful to resume or guide work; | rule | P7 | V5: "when it becomes useful" is not a checkable trigger | — | 25 |
| readme-084 | L86 | do not wait for a save request or the end of the conversation. | rule | P7 | V8: same policy stated in duplicate group D30 | — | 25 |
| readme-085 | L86-L88 | Explicit read-only, no-save, destination limits, and write permissions prevail; | rule | P6 | — | — | 25 |
| readme-086 | L88 | report prevented saving and provide the result through a permitted channel. | rule | P5 | V8: same policy stated in duplicate group D31 | — | 25 |
| readme-087 | L89 | Delegated read-only workers return findings for the coordinator to save within its authority. | rule | — | V1: third-person role statement; V4: "workers" used for Leaf or Coordinator; V8: same policy stated in duplicate group D09 | — | 26 |
| readme-088 | L90 | Creating, updating, or using a spec requires its queue tracking under [queue](references/queue.md). | rule | — | V8: same policy stated in duplicate group D18 | — | 27 |
| readme-089 | L91 | Consequential architecture decisions require ADRs. | rule | — | V8: same policy stated in duplicate group D70 | — | 28 |
| readme-090 | L91-L92 | Saving neither selects TDD nor requires Specify nor authorizes implementation. | rule | P6 | — | — | 29 |
| readme-091 | L92 | Requested standalone documents remain deliverables. | rule | — | — | — | 29 |
| readme-092 | L96 | Coordinator catalog: use when locating a procedure not already linked; | rule | — | V2: "Coordinator catalog:" label restates section purpose | — | 30 |
| readme-093 | L96 | load only applicable procedures. | rule | — | V8: same policy stated in duplicate group D83 | — | 30 |
| readme-094 | L97 | Leaves receive applicable paths/text and loading instructions. | rule | — | V1: third-person role statement; V8: same policy stated in duplicate group D85 | — | 30 |
| readme-095 | L97 | Paths are relative to this file. | definition | — | — | — | 30 |
| readme-096 | L99 | \| Operation \| Reference \| | not a rule | — | — | — | 30 |
| readme-097 | L101 | \| Intent/tradeoff interviews \| [interviews](references/interviews.md) \| | catalog | — | — | — | 30 |
| readme-098 | L102 | \| Visual options/diagrams/references \| [visuals](references/visuals.md) \| | catalog | — | — | — | 30 |
| readme-099 | L103 | \| Select/record/apply TDD \| [tdd](references/tdd.md) \| | catalog | — | — | — | 30 |
| readme-100 | L104 | \| Create/update/rename spec, plan, ADR \| [naming](references/naming.md) \| | catalog | — | — | — | 30 |
| readme-101 | L105 | \| Locate/maintain project records \| [files](references/files.md) \| | catalog | — | — | — | 30 |
| readme-102 | L106 | \| Queue/selection/parking \| [queue](references/queue.md) \| | catalog | — | — | — | 30 |
| readme-103 | L107 | \| Measurements/experiments \| [evidence](references/evidence.md) \| | catalog | — | — | — | 30 |
| readme-104 | L108 | \| Save findings/evidence \| [retention](references/retention.md) \| | catalog | — | — | — | 30 |
| readme-105 | L109 | \| Close/reopen tracked work \| [closeout](references/closeout.md) \| | catalog | — | — | — | 30 |
| readme-106 | L110 | \| Commit/integrate \| [commits](references/commits.md) \| | catalog | — | — | — | 30 |
| readme-107 | L111 | \| Dispatch/perform/evaluate assignment \| [delegation](references/delegation.md) \| | catalog | — | — | — | 30 |
| readme-108 | L112 | \| Before dispatch \| [model routing](references/model-routing.md) \| | catalog | — | — | — | 30 |
| readme-109 | L113 | \| Responsible for workers/results: after results, before closing or handing off responsibility \| [worker lifecycle](references/worker-lifecycle.md) \| | catalog | — | V4: "workers" used for Leaf or Coordinator | — | 30 |
| readme-110 | L114 | \| Observed failure/review correction \| [corrections](references/corrections.md) \| | catalog | — | — | — | 30 |
| readme-111 | L115 | \| Checkpoint/handoff content \| [handoff](references/handoff.md) \| | catalog | — | — | — | 30 |
| readme-112 | L116 | \| Authorized unattended batch \| [batch execution](references/batch-execution.md) \| | catalog | — | — | — | 30 |
| readme-113 | L117 | \| Start/resume batch \| [batch use](references/batch-use.md) \| | catalog | — | — | — | 30 |
| readme-114 | L118 | \| Catalog/invocation/terminology \| [workflow guide](references/workflow-guide.md) \| | catalog | — | — | — | 30 |
| readme-115 | L120-L121 | Batch execution governs selection, decisions, reconciliation, concurrency, repair budgets, deferral, and recovery; | definition | — | — | — | 31 |
| readme-116 | L121 | TDD, completion, approval, and repository rules remain binding. | rule | P6 | — | — | 31 |
| readme-117 | L125 | Every skill must reach a natural concrete next step or explicitly state that none is needed. | rule | P8 | V6: filler adjective "natural" | — | 32 |
| readme-118 | L126-L127 | In substantive conversation, answer first, then ask the focused question, offer the supported proposal, or take the bounded authorized action that can improve the outcome. | rule | P7, P8 | — | — | 33 |
| readme-119 | L127-L128 | Do not wait for the user to request options, synthesis, saving, or continuation. | rule | P7 | V8: same policy stated in duplicate group D30 | — | 33 |
| readme-120 | L128-L129 | If further work would add no value to the request, stop and state that no next action is needed, with a brief reason. | rule | P8 | — | — | 32 |
| readme-121 | L129-L130 | Greetings and acknowledgments need no workflow boilerplate or invented follow-up. | rule | P8 | — | — | 32 |
| readme-122 | L130 | A proposed next step does not authorize its execution. | rule | P6 | V8: same policy stated in duplicate group D05 | — | 33 |
| readme-123 | L132-L133 | Use permitted native question UI for the purpose/mode (`AskUserQuestion`, exposed `request_user_input` or `request_user_input_async`), otherwise concise plain text. | rule | — | V8: same policy stated in duplicate group D55 | — | 34 |
| readme-124 | L133 | Do not switch modes to ask. | rule | — | — | — | 34 |
| readme-125 | L133-L134 | Ask missing consequential questions; | rule | P6 | — | — | 35 |
| readme-126 | L134 | recommend answers when useful. | rule | — | V5: "when useful" is not a checkable condition | — | 35 |
| readme-127 | L134-L135 | For optional preferences, state an assumption and continue within authority and host timing rules. | rule | P7 | — | — | 35 |
| readme-128 | L135 | Silence/preselection is not consent; | rule | P6 | V8: same policy stated in duplicate group D29 | — | 35 |
| readme-129 | L135-L136 | host approval rules apply. | rule | P6 | V8: same policy stated in duplicate group D66 | — | 35 |
| readme-130 | L136 | Ask the actual question when input is needed. | rule | — | — | — | 35 |
| readme-131 | L140 | Implementation requires explicit user/standing selection of `none`, `targeted`, or `strict`. | rule | P6 | V8: same policy stated in duplicate group D06 | K4 | 36 |
| readme-132 | L141 | Unset TDD permits definition/planning only. | rule | P6 | V8: same policy stated in duplicate group D07 | K4 | 36 |
| readme-133 | L141 | Read [tdd](references/tdd.md) when selecting/applying policy. | rule | — | V8: same policy stated in duplicate group D78 | — | 36 |
| readme-134 | L145-L146 | Completion requires the whole authorized outcome, criteria, required checks, and required human acceptance/delivery, including conversation-only work. | rule | P5 | V8: same policy stated in duplicate group D03 | — | 37 |
| readme-135 | L146 | Failed/unrun required checks block completion; | rule | P5 | V8: same policy stated in duplicate group D01 | — | 37 |
| readme-136 | L147 | passing tests are not human acceptance. | rule | P5 | V8: same policy stated in duplicate group D02 | — | 37 |
| readme-137 | L147 | Self-inspection/applicable checks are required. | rule | P5 | — | — | 37 |
| readme-138 | L147-L149 | Independent review is required by user/repository rules or security boundaries, persistent data, shared contracts, or coordinated multiple writers. | rule | P5 | V8: same policy stated in duplicate group D22 | — | 38 |
| readme-139 | L149 | Supply actual diff, agreement, and evidence; | rule | P5 | V8: same policy stated in duplicate group D69 | — | 38 |
| readme-140 | L149-L150 | persona changes are not independence. | rule | P5 | V8: same policy stated in duplicate group D21 | — | 38 |
| readme-141 | L150 | Report unavailable required review as unmet. | rule | P5 | V8: same policy stated in duplicate group D21 | — | 38 |
| readme-142 | L150 | Repair within authority and verify. | rule | P7 | — | — | 37 |
| readme-143 | L152 | Lead with blocking decisions/approvals, otherwise results. | rule | — | — | — | 39 |
| readme-144 | L152-L154 | Report demonstrated behavior, consequential decisions/reasons, evidence/limits, unresolved issues, and the next bounded action, owner, inputs, and remaining authority. | rule | P5, P8 | — | — | 39 |
| readme-145 | L154-L155 | At handoff/boundary give a ready-to-use continuation directive when another actor/session needs one, without substituting it for available authorized work. | rule | P7, P8 | — | — | 40 |
| readme-146 | L155-L156 | Answer status questions briefly then continue authorized work. | rule | P7 | — | — | 41 |
| readme-147 | L156-L157 | For user-visible changes give concrete actions/expected results. | rule | — | — | — | 41 |
| readme-148 | L157-L158 | Update existing product/architecture documentation for enduring behavior/constraint changes, distinguishing proposals from current behavior. | rule | — | — | — | 42 |
| readme-149 | L160-L161 | Substantive assessments and handoff replies addressed to the user default to **Result** and **Evidence** labels or headings followed by the next action, keeping blocking decisions first. | rule | P5, P8 | — | — | 43 |
| readme-150 | L162-L163 | When work remains, present the next action as a one-row table `Next action \| Owner \| Needs \| Authority`: the bounded action, its owner, required inputs, and remaining or missing authority, or `Authorized`. | rule | P8 | — | — | 44 |
| readme-151 | L164 | Use the same table for a useful proposed follow-up after the requested scope is complete; | rule | P8 | — | — | 44 |
| readme-152 | L165 | label it proposed and state any missing authority. | rule | P6, P8 | — | — | 44 |
| readme-153 | L165-L166 | Completion does not mean that no useful follow-up exists. | definition | P8 | — | — | 44 |
| readme-154 | L166-L167 | Put the continuation directive, when given, in a blockquote below the table. | rule | — | — | — | 44 |
| readme-155 | L167-L168 | Only when no useful next action is warranted, write the plain label **Next action:** `None for this request` without a table. | rule | P8 | P8: None form omits the reason that readme-120 requires | — | 44 |
| readme-156 | L169-L170 | Pair Result with **✅ Complete**, **🔄 In progress**, **❓ Needs input**, or **⏸ Paused**: fulfilled scope, continuing work, missing prerequisite, or affected work awaiting resumption. | rule | — | — | K4 | 45 |
| readme-157 | L170-L171 | Status describes the response or authorized outcome, not queue state; | definition | — | — | K4 | 45 |
| readme-158 | L171-L172 | a finished assessment need not mean its subject is complete. | definition | — | — | — | 45 |
| readme-159 | L172 | Words carry meaning without glyphs. | rule | — | V6: figurative statement that gives no action | — | 45 |
| readme-160 | L174 | Use lists for parallel items and steps, and tables for useful comparisons. | rule | — | — | — | 46 |
| readme-161 | L174-L176 | Status summaries use `Outcome \| State \| Remaining work`, preserving blockers and dependencies and identifying recorded queue states; | rule | — | — | — | 46 |
| readme-162 | L176 | comparisons use stable useful columns (e.g. `Option \| Benefit \| Tradeoff`). | rule | — | V5: "useful" columns sets no condition | — | 46 |
| readme-163 | L176-L177 | Preserve specialized tables and schemas. | rule | — | — | — | 46 |
| readme-164 | L177 | User and host formatting overrides these defaults; | rule | P6 | — | — | 46 |
| readme-165 | L177-L179 | retain outcome, evidence, and next action with supported formatting and status words, using **Next action:** with the same fields in prose where tables do not render. | rule | P8 | — | — | 46 |
| readme-166 | L179-L180 | Lusona owns meaning, priority, and actionability. | definition | — | V6: attributes ownership of meaning to Lusona, gives no action | — | 46 |
| readme-167 | L180-L181 | Assignment results returned to a coordinator use the fields in [Assignment results](references/delegation.md#assignment-results) instead. | rule | — | — | — | 47 |
| readme-168 | L185 | Leaves read and follow [Assigned leaves and Assignment results](references/delegation.md#assigned-leaves). | rule | — | V1: third-person role address; V8: same policy stated in duplicate group D77 | — | 48 |
| readme-169 | L186 | Shared authority, TDD, completion, verification, and independence rules remain binding. | rule | P5, P6 | — | — | 48 |
| readme-170 | L186-L187 | Specialist instructions to ask/continue route through the parent; | rule | P6 | V4: "the parent" used for Leaf or Coordinator | — | 48 |
| readme-171 | L187-L188 | no user interviews or extra responsibility arise from narrower loading or supplemental domain skills. | rule | P6 | V8: same policy stated in duplicate group D25; V8: same policy stated in duplicate group D26 | — | 48 |
| readme-172 | L192-L193 | Coordinator-only: coordinate questions, assignments, reconciliation, integration, verification, shared state. | rule | — | — | — | 49 |
| readme-173 | L193-L196 | Delegate substantive framing, mapping, specification, visual design, architecture, implementation planning/execution, refactoring, investigation, measurement, experimentation, and review, except task-local empirical checks under [study entry](references/evidence.md#study-entry). | rule | — | — | — | 49 |
| readme-174 | L196 | Preliminary inspection is insufficient. | rule | — | V8: same policy stated in duplicate group D68 | — | 49 |
| readme-175 | L196-L197 | Explore/status conversation and orientation may stay local; | rule | — | — | — | 49 |
| readme-176 | L197 | one sequential worker suffices. | definition | — | V4: "worker" used for Leaf or Coordinator | — | 49 |
| readme-177 | L199 | If delegation is prohibited/unavailable, explain and act locally within authority; | rule | P6 | — | — | 49 |
| readme-178 | L199-L200 | this cannot satisfy required independent review. | rule | P5 | — | — | 49 |
| readme-179 | L200 | Occupied capacity is not unavailability: wait/reuse/release finished workers. | definition | P7 | V4: "workers" used for Leaf or Coordinator | — | 50 |
| readme-180 | L201 | Apply host capacity accounting and the single batch pool. | rule | — | V8: same policy stated in duplicate group D65 | — | 50 |
| readme-181 | L201-L202 | Before dispatch read [assignment contract](references/delegation.md#assignment-contract) and [model routing](references/model-routing.md); | rule | — | V8: same policy stated in duplicate group D23 | — | 51 |
| readme-182 | L203-L204 | when responsible for workers or their results, read [worker lifecycle](references/worker-lifecycle.md) after results and before closing or handing off that responsibility. | rule | — | V4: "workers" used for Leaf or Coordinator; V8: same policy stated in duplicate group D23 | — | 51 |
| readme-183 | L205 | Leaves need these only if granted those responsibilities. | rule | — | V1: third-person role statement; V8: same policy stated in duplicate group D24 | — | 51 |
| readme-184 | L209 | With telemetry, prepare handoff around 40%, target before 50%; | rule | P7 | V5: "around 40%" is an approximate threshold | — | 52 |
| readme-185 | L209 | invent neither usage nor transfer. | rule | P5 | — | — | 52 |
| readme-186 | L210 | Otherwise checkpoint at task boundaries, not skill changes. | rule | P1 | — | — | 52 |
| readme-187 | L210-L211 | Before a checkpoint or handoff, read [handoff](references/handoff.md). | rule | — | V8: same policy stated in duplicate group D28 | — | 52 |

## batch-execution (`plugins/lusona/references/batch-execution.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| batch-execution-001 | L3 | Read for explicitly authorized unattended batch work, as coordinator or assigned delegate. | rule | — | V4: "assigned delegate" used for Leaf or Coordinator | — | none |
| batch-execution-002 | L5-L6 | These exceptions apply when the user explicitly authorizes unattended work on a fixed selection of queue outcomes. | rule | P6 | V2: restates scope ("These exceptions apply") before the action | — | none |
| batch-execution-003 | L6-L7 | Record the selection, decision authority, applicable TDD, completion conditions, concurrency limit, and finite per-item repair budget before execution. | rule | P6 | — | — | none |
| batch-execution-004 | L8 | Selecting work for discussion or planning alone is not batch implementation authority. | rule | P6 | — | — | none |
| batch-execution-005 | L9-L10 | Apply these rules to each delegated skill's questions, queue handling, delegation, and next action; | rule | — | — | — | none |
| batch-execution-006 | L10 | other contract and repository requirements remain binding. | rule | P6 | — | — | none |
| batch-execution-007 | L11-L12 | After each result, apply the [work loop](../README.md#work-loop) to each affected outcome and schedule its next eligible bounded action. | rule | P1, P2 | — | — | none |
| batch-execution-008 | L12 | Do not synchronize items into workflow phases; | rule | P1 | — | — | none |
| batch-execution-009 | L13 | shared dependencies, ownership, and required review still determine eligibility. | definition | P1 | — | — | none |
| batch-execution-010 | L15-L16 | The parent coordinator may settle routine details using existing project decisions and documented conservative assumptions within delegated authority. | rule | P6 | V5: "conservative assumptions" sets no checkable condition; V4: "parent coordinator" used for Leaf or Coordinator | — | none |
| batch-execution-011 | L16-L17 | Record the basis and authority of those decisions; | rule | P6 | — | — | none |
| batch-execution-012 | L17 | do not present them as direct user answers. | rule | P6 | — | — | none |
| batch-execution-013 | L17-L18 | Reconcile related definitions before accepting shared assumptions or making dependent architecture decisions. | rule | — | — | — | none |
| batch-execution-014 | L19 | Reconcile architecture outputs before dependent implementation decisions or assignments. | rule | — | — | — | none |
| batch-execution-015 | L19-L20 | Independent settled work can advance without waiting for the whole batch; | rule | P7 | — | — | none |
| batch-execution-016 | L20 | disjoint files do not prove independence. | rule | P5 | — | — | none |
| batch-execution-017 | L21-L23 | Definition, architecture, and implementation delegates return potential dependencies, shared assumptions, unresolved shared behavior, and newly discovered coupling to the parent rather than settling them locally, and record the basis of delegated routine decisions. | rule | P6 | V4: "delegates return" used for Leaf or Coordinator | — | none |
| batch-execution-018 | L24 | Each shared decision has one owner with all affected definitions as inputs; | rule | — | — | — | none |
| batch-execution-019 | L24-L25 | architecture runs in parallel only across compatible scopes. | rule | — | — | — | none |
| batch-execution-020 | L25-L26 | An unresolved potentially shared concern blocks affected design and implementation, not unrelated reconciled work. | rule | P7 | — | — | none |
| batch-execution-021 | L27-L28 | For a missing consequential decision, authority, or applicable TDD policy, return the gap to the parent. | rule | P6 | V4: "the parent" used for Leaf or Coordinator | — | none |
| batch-execution-022 | L28 | Record the question and defer affected work and its dependents; | rule | P7 | — | — | none |
| batch-execution-023 | L28-L29 | continue eligible independent work. | rule | P7 | V8: same policy stated in duplicate group D80 | — | none |
| batch-execution-024 | L29 | Delegates do not start user interviews. | rule | P6 | V4: "Delegates do" used for Leaf or Coordinator; V8: same policy stated in duplicate group D25 | — | none |
| batch-execution-025 | L29-L30 | The parent reports deferred questions for resumption. | rule | P7 | V1: third-person role statement; V4: "parent reports" used for Leaf or Coordinator | — | none |
| batch-execution-026 | L30 | Host approval rules still apply, | rule | P6 | V8: same policy stated in duplicate group D66 | — | none |
| batch-execution-027 | L30-L31 | and unanswered requests never count as consent. | rule | P6 | V8: same policy stated in duplicate group D29 | — | none |
| batch-execution-028 | L31 | Unset TDD still permits independent definition and planning. | rule | P6 | V8: same policy stated in duplicate group D07 | K4 | none |
| batch-execution-029 | L32-L33 | There is one parent coordinator and one concurrency pool across responsibilities and nested work, capped by host capacity. | definition | — | V4: "parent coordinator" used for Leaf or Coordinator | — | none |
| batch-execution-030 | L33-L34 | A delegated skill performs its assigned role and returns evidence to the parent; | rule | — | V1: third-person role statement; V4: "the parent" used for Leaf or Coordinator | — | none |
| batch-execution-031 | L34-L35 | it does not independently start another assignment, spawn more agents, or manage shared state. | rule | P6 | — | — | none |
| batch-execution-032 | L35 | Additional delegation requires a parent grant from that same pool. | rule | P6 | V4: "a parent" used for Leaf or Coordinator | — | none |
| batch-execution-033 | L35-L36 | The parent alone updates queue/shared handoffs and integrates results. | rule | — | V1: third-person role statement; V4: "parent alone" used for Leaf or Coordinator; V8: same policy stated in duplicate group D08 | — | none |
| batch-execution-034 | L36-L37 | Workers may create records within their assigned ownership using the helper | rule | — | — | — | none |
| batch-execution-035 | L37 | and must report naming conflicts. | rule | — | — | — | none |
| batch-execution-036 | L38 | Review delegates remain read-only; | rule | P6 | V4: "Review delegates" used for Leaf or Coordinator | — | none |
| batch-execution-037 | L38 | the parent schedules authorized repairs separately. | rule | P6 | V4: "the parent" used for Leaf or Coordinator | — | none |
| batch-execution-038 | L39 | Workers report each assignment result as soon as it is available. | rule | P7 | V1: third-person role statement | — | none |
| batch-execution-039 | L39-L41 | The parent applies [incremental reporting](../skills/batch/references/execution.md#incremental-reporting) to each result as it arrives. | rule | — | V4: "parent applies" used for Leaf or Coordinator | — | none |
| batch-execution-040 | L42 | Multiple selected items may be Doing or in Review concurrently. | definition | P1 | — | K2 | none |
| batch-execution-041 | L42-L44 | A deferred item keeps its truthful queue state and blocker but releases execution capacity after its writers stop and unfinished changes are safely isolated. | rule | P7 | — | — | none |
| batch-execution-042 | L44-L45 | Do not continue on a baseline contaminated by unfinished work; | rule | P5 | — | — | none |
| batch-execution-043 | L45 | stop if safe attribution or isolation cannot be established. | rule | P7 | — | — | none |
| batch-execution-044 | L45-L46 | New coupling stops affected work for reconciliation before rescheduling. | rule | P7 | — | — | none |
| batch-execution-045 | L47-L48 | Repairs and investigations obey the recorded per-item budget across assignments and resumptions; | rule | — | V8: same policy stated in duplicate group D59 | — | none |
| batch-execution-046 | L48 | changing agents or roles does not reset it. | rule | — | — | — | none |
| batch-execution-047 | L48 | Exhaustion defers affected work. | rule | P7 | — | — | none |
| batch-execution-048 | L49-L50 | The parent proceeds through authorized work without new role approvals and closes an item only when its completion conditions, required checks, and independent review pass. | rule | P5, P7 | V4: "parent proceeds" used for Leaf or Coordinator; V8: same policy stated in duplicate group D03 | — | none |
| batch-execution-049 | L50-L51 | Explicit human acceptance and delivery requirements remain binding. | rule | P5 | V8: same policy stated in duplicate group D02 | — | none |
| batch-execution-050 | L51-L52 | Report unavailable independent review rather than substituting a persona change. | rule | P5 | V8: same policy stated in duplicate group D21 | — | none |
| batch-execution-051 | L54 | Keep evidence in its owning change record, ADR, or existing separate plan; | rule | — | — | — | none |
| batch-execution-052 | L54 | batch coordination references those records. | definition | — | — | — | none |
| batch-execution-053 | L55-L56 | Existing commit authority and repository restrictions apply, with staging and commits owned by the parent after verified integration. | rule | P6 | V4: "the parent" used for Leaf or Coordinator; V8: same policy stated in duplicate group D43 | — | none |
| batch-execution-054 | L56-L57 | Batch authorization does not grant publication, deployment, or other external actions beyond the user's explicit scope. | rule | P6 | V8: same policy stated in duplicate group D40 | — | none |

## batch-use (`plugins/lusona/references/batch-use.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| batch-use-001 | L3 | Read when giving guidance about starting or resuming a batch. | rule | — | — | — | none |
| batch-use-002 | L5-L6 | Use [batch](../skills/batch/SKILL.md) to start or resume explicitly authorized unattended work on a fixed selection of current queue items. | rule | P6 | — | — | none |
| batch-use-003 | L6-L7 | Start with exact queue titles or IDs, authorized scope, and an explicit TDD policy or its existing source. | rule | P6 | — | — | none |
| batch-use-004 | L7 | For example: | not a rule | — | — | — | none |
| batch-use-005 | L9-L12 | Use Lusona's batch skill for only the current queue items "Invitation expiry" and "Expired invitation message". Authorize definition, necessary architecture, implementation, and independent review. Resolve routine details within existing project decisions; defer consequential gaps. Use targeted TDD for the expiry boundary and expired invitation behavior. Do not commit, push, or publish. | example | — | — | — | none |
| batch-use-006 | L14 | “All current queue items” selects the Active queue and excludes Icebox. | definition | — | V8: same policy stated in duplicate group D35 | K2 | none |
| batch-use-007 | L14-L15 | Explicitly reactivate parked outcomes before including them. | rule | P6 | — | — | none |
| batch-use-008 | L15 | Batch deferral alone does not park an item. | definition | — | V8: same policy stated in duplicate group D35 | K2 | none |
| batch-use-009 | L17 | To select the whole active queue and request five assignments: | not a rule | — | — | — | none |
| batch-use-010 | L19-L23 | Use Lusona's batch skill for all current queue items through implementation and independent review, using each item's recorded TDD and completion conditions. Resolve routine details within existing project decisions; defer consequential gaps or missing TDD. Request five concurrent assignments subject to host capacity. Do not commit, push, or publish. Exclude newly discovered work. | example | — | — | — | none |
| batch-use-011 | L25-L26 | The default requested ceiling is four assignments, or five when selected, reduced by host capacity including parent occupancy. | definition | — | V4: "parent occupancy" used for Leaf or Coordinator | — | none |
| batch-use-012 | L26-L27 | Assignments and nested grants share that ceiling under [Batch execution](batch-execution.md). | definition | — | — | — | none |
| batch-use-013 | L27-L28 | Available host tools determine concurrency and session continuity; | definition | — | — | — | none |
| batch-use-014 | L28 | the skill supplies no background execution guarantee. | definition | — | — | — | none |
| batch-use-015 | L30-L31 | The parent owns `docs/lusona/batches/<batch-slug>.md`, created from the [batch template](../templates/batch.md), and the queue and shared handoffs. | definition | — | V4: "parent owns" used for Leaf or Coordinator | K2 | none |
| batch-use-016 | L31 | Change records and ADRs retain their requirements and evidence; | definition | — | — | — | none |
| batch-use-017 | L31 | existing split records remain valid. | definition | — | V8: same policy stated in duplicate group D58 | — | none |
| batch-use-018 | L31 | Continue a recorded batch explicitly: | rule | — | — | — | none |
| batch-use-019 | L33-L35 | Use Lusona's batch skill to resume docs/lusona/batches/invitation-updates.md. Continue its remaining authorized scope, recorded TDD, and remaining repair allowance. Reconcile the current handoff and active ownership before dispatching work. | example | — | — | K2 | none |
| batch-use-020 | L37 | Use the actual batch path from the prior run. | rule | — | — | — | none |
| batch-use-021 | L37-L38 | In Claude Code, `/lusona:batch` selects the skill; | definition | — | V8: same policy stated in duplicate group D81 | K1 | none |
| batch-use-022 | L38 | in Codex, use its skill UI. | rule | — | — | — | none |
| batch-use-023 | L38-L39 | Resumption follows the skill's linked execution reference and preserves recorded authority; | rule | P6 | — | — | none |
| batch-use-024 | L39 | it does not expand selection or reset budgets. | rule | P6 | — | — | none |

## closeout (`plugins/lusona/references/closeout.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| closeout-001 | L3 | Coordinator-only: read when closing or reopening tracked work. | rule | — | V8: same policy stated in duplicate group D54 | — | none |
| closeout-002 | L3-L4 | Untracked work needs no history entry; | definition | — | — | — | none |
| closeout-003 | L4 | substantive outputs still follow [retention](retention.md). | rule | — | — | — | none |
| closeout-004 | L6-L7 | When the whole item meets its agreed completion condition, record a compact entry in `history/YYYY-MM-week-NN.md` using the [history template](../templates/history.md). | rule | P5 | — | K2 | none |
| closeout-005 | L8-L9 | Under Completed items, each dated item has its own heading, outcome, completion and evidence section, and optional related records. | definition | — | — | — | none |
| closeout-006 | L9-L10 | Preserve an existing project format when it retains those facts and stable links. | rule | — | — | — | none |
| closeout-007 | L10-L12 | Preserve any unique queue facts in their owning records, update links that targeted the removed row, and verify the history entry and links before removing the queue row. | rule | P5 | — | — | none |
| closeout-008 | L12-L13 | This closeout does not waive required checks, acceptance, delivery, or authorization. | rule | P5, P6 | — | — | none |
| closeout-009 | L13-L14 | History then owns archived state; | definition | — | — | — | none |
| closeout-010 | L14 | change records and notes do not duplicate it. | rule | — | V8: same policy stated in duplicate group D37 | — | none |
| closeout-011 | L14-L15 | Reopening an item restores its row and current state ownership to the queue with a backlink to its historical completion entry; | definition | P4 | — | — | none |
| closeout-012 | L16 | leave that entry as a historical fact. | rule | P4 | — | — | none |
| closeout-013 | L16 | Read history only when relevant to the selected work. | rule | — | — | — | none |
| closeout-014 | L18 | Use the bundled work-record helper for history names, dates, and initial structure. | rule | — | V8: same policy stated in duplicate group D15 | K3 | none |
| closeout-015 | L19 | Follow [shell selection, paths, and invocation](work-record.md). | rule | — | V8: same policy stated in duplicate group D16 | K3 | none |
| closeout-016 | L21-L22 | History uses month-local week numbers: 01 for days 1–7, 02 for 8–14, 03 for 15–21, 04 for 22–28, and 05 for 29–month end. | definition | — | V8: same policy stated in duplicate group D17 | K3 | none |
| closeout-017 | L22-L23 | September 10, 2026 belongs in `2026-09-week-02.md`. | example | — | — | K2 | none |
| closeout-018 | L23 | The date defaults to local today; | definition | — | V8: same policy stated in duplicate group D79 | K3 | none |
| closeout-019 | L23-L24 | pass the actual completion date for older work. | rule | — | — | K3 | none |
| closeout-020 | L24 | Pass an explicit project root for initialization; | rule | — | V8: same policy stated in duplicate group D13 | K3 | none |
| closeout-021 | L24 | existing files are preserved. | definition | — | V8: same policy stated in duplicate group D13 | K3 | none |
| closeout-022 | L25 | `init-history` loads the bundled history template and fills its period. | definition | — | — | K3 | none |
| closeout-023 | L25-L26 | Copy its commented item structure for each completed outcome in new history files; | rule | — | — | — | none |
| closeout-024 | L26-L27 | keep existing records and link targets intact. | rule | — | — | — | none |
| closeout-025 | L27 | The helper initializes records and returns paths; | definition | — | V8: same policy stated in duplicate group D14 | K3 | none |
| closeout-026 | L27-L28 | the coordinator records completion evidence and removes queue rows only after verifying preservation. | rule | P5 | V1: third-person role statement | — | none |
| closeout-027 | L29 | Do not initialize project data merely for orientation or installation. | rule | — | V8: same policy stated in duplicate group D12 | — | none |

## commits (`plugins/lusona/references/commits.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| commits-001 | L3-L4 | During authorized implementation, make local commits after coherent increments pass their required checks, unless the user opts out or repository instructions prohibit it. | rule | P5, P6 | V8: same policy stated in duplicate group D39 | — | none |
| commits-002 | L4-L5 | Group related implementation, tests, configuration, and documentation by purpose and dependency. | rule | — | — | — | none |
| commits-003 | L6 | An increment may span files or tasks; | definition | — | — | — | none |
| commits-004 | L6 | each commit must leave the project usable. | rule | — | V5: "usable" names no check | — | none |
| commits-005 | L6-L7 | Do not create one commit per file, task, skill stage, or workflow-state transition. | rule | — | — | — | none |
| commits-006 | L7-L8 | A small change can be one verified commit. | definition | — | V7: "small change" has no measurable bound | — | none |
| commits-007 | L9-L10 | Include related change records, verification evidence, queue updates, and any completion records already justified by the evidence in the implementation increment's commit. | rule | — | — | — | none |
| commits-008 | L11 | Saving a record or recovery checkpoint does not require committing it. | rule | — | — | — | none |
| commits-009 | L11-L12 | Do not create preparatory or follow-up documentation commits solely for workflow bookkeeping. | rule | — | — | — | none |
| commits-010 | L13-L15 | If required review, acceptance, or delivery occurs after the implementation commit, consolidate remaining record updates into one closeout commit when commit authorization covers it. | rule | — | — | — | none |
| commits-011 | L15 | Do not mark completion early to fit a commit boundary. | rule | P5 | — | — | none |
| commits-012 | L15-L16 | Documentation that is itself the requested deliverable can have its own commit when authorized. | rule | P6 | — | — | none |
| commits-013 | L17 | Complete the selected TDD sequence and required verification before committing. | rule | P5 | — | — | none |
| commits-014 | L17-L19 | Keep incomplete or failing work uncommitted unless the user explicitly requests a checkpoint commit. | rule | P5, P6 | — | — | none |
| commits-015 | L19 | Report any checks or commit operation that could not complete; | rule | P5 | — | — | none |
| commits-016 | L19 | do not claim success. | rule | P5 | — | — | none |
| commits-017 | L20 | The coordinator manages staging and commits after integrating delegated work; | rule | — | V1: third-person role statement; V8: same policy stated in duplicate group D43 | — | none |
| commits-018 | L20-L21 | subagents do not race on the shared index. | rule | — | V4: "subagents" used for Leaf or Coordinator | — | none |
| commits-019 | L21-L22 | Inspect working-tree and staged changes, stage only this increment's files or hunks, and inspect the resulting staged diff before committing. | rule | P5 | — | — | none |
| commits-020 | L23 | Preserve unrelated edits and staged changes; | rule | P6 | V8: same policy stated in duplicate group D86 | — | none |
| commits-021 | L23-L24 | never include them through a blanket add or commit. | rule | P6 | — | — | none |
| commits-022 | L24-L25 | Ensure the committed content is what passed verification, including when shared files require partial staging. | rule | P5 | — | — | none |
| commits-023 | L26 | Use the Conventional Commits format below | rule | — | V8: same policy stated in duplicate group D41 | — | none |
| commits-024 | L26 | and explain why in the body. | rule | — | — | — | none |
| commits-025 | L26-L27 | Choose the type for the increment's outcome; | rule | — | V8: same policy stated in duplicate group D42 | — | none |
| commits-026 | L27-L28 | accompanying workflow records do not make a fix or feature a documentation commit. | definition | — | — | — | none |
| commits-027 | L28 | Save verification evidence before committing | rule | P5 | — | — | none |
| commits-028 | L28-L29 | and report the resulting hash in the conversation. | rule | P5 | — | — | none |
| commits-029 | L29-L30 | Save a hash only when needed to identify reviewed or integrated content or when project rules require it; | rule | — | V5: banned term "when needed" | — | none |
| commits-030 | L30-L31 | include it in the next otherwise needed record update. | rule | — | V5: "otherwise needed" is not a checkable condition | — | none |
| commits-031 | L31 | Do not amend or create a commit solely to record another commit's hash. | rule | — | — | — | none |
| commits-032 | L32 | A successful commit records a verified increment. | definition | P5 | — | — | none |
| commits-033 | L32-L33 | Human acceptance and delivery remain separate completion conditions. | rule | P5 | V8: same policy stated in duplicate group D02 | — | none |
| commits-034 | L33-L34 | Pushing, publishing, amending commits, and rewriting shared or published history require separate authorization. | rule | P6 | V8: same policy stated in duplicate group D40 | — | none |
| commits-035 | L34-L35 | For integration, apply the rebase authority and linear-history rules below. | rule | — | — | — | none |
| commits-036 | L38-L39 | Use Conventional Commits: `type(scope): imperative summary`, with an optional useful scope and a body explaining why. | rule | — | V5: "optional useful scope" sets no condition; V8: same policy stated in duplicate group D41 | — | none |
| commits-037 | L39 | Choose the type for the change. | rule | — | V8: same policy stated in duplicate group D42 | — | none |
| commits-038 | L39-L40 | Mark breaking changes with `!` and a `BREAKING CHANGE:` footer explaining the impact. | rule | — | — | — | none |
| commits-039 | L44-L45 | Within authorized Git integration, prefer `git merge --ff-only` when the target can advance directly. | rule | — | — | — | none |
| commits-040 | L45-L46 | Check the incoming commits as well: a fast-forward can import existing merge commits, so fast-forward success alone does not establish linear history. | rule | P5 | V9: explanatory clause "a fast-forward can import" in the instruction | — | none |
| commits-041 | L46-L47 | Do not introduce merge commits into the target unless the user explicitly requests that topology. | rule | P6 | — | — | none |
| commits-042 | L48-L49 | If branches diverge, rebase agent-owned, unpublished commits onto the current target, then fast-forward. | rule | — | — | — | none |
| commits-043 | L49-L50 | This is included in authorized integration unless project instructions prohibit it; | rule | P6 | — | — | none |
| commits-044 | L50 | it does not authorize commits or integration where those actions are forbidden. | rule | P6 | — | — | none |
| commits-045 | L51-L52 | Do not rebase another contributor's work or shared/published commits without explicit authority, | rule | P6 | — | — | none |
| commits-046 | L52 | and do not force-push as an implicit part of rebasing. | rule | P6 | — | — | none |
| commits-047 | L53-L54 | The coordinator serializes rebasing and integration, stops affected writers, and preserves unrelated changes. | rule | — | V1: third-person role statement | — | none |
| commits-048 | L54-L55 | Inspect the resulting diff and rerun affected verification after a rebase or conflict resolution. | rule | P5 | — | — | none |
| commits-049 | L55-L56 | Refresh commit/content identities and review evidence when changed inputs invalidate it; | rule | P5 | — | — | none |
| commits-050 | L56 | confirm the target has not advanced before the final fast-forward. | rule | — | — | — | none |
| commits-051 | L57-L58 | Conflicts requiring a consequential behavior or scope decision follow the normal question or batch-deferral rules. | rule | P6 | — | — | none |
| commits-052 | L59-L60 | Squash integration is an alternative when explicitly selected or required by the project's established workflow. | rule | P6 | — | — | none |
| commits-053 | L60 | Verify the resulting content and record its new identity. | rule | P5 | — | — | none |
| commits-054 | L60-L61 | Do not silently discard meaningful commit boundaries merely to avoid resolving a divergence. | rule | — | — | — | none |
| commits-055 | L62 | Apply this policy to new integration; | rule | — | — | — | none |
| commits-056 | L62-L63 | do not rewrite existing target history to remove old merges. | rule | — | — | — | none |
| commits-057 | L63-L64 | If permitted operations cannot produce the requested linear result, report the exact blocker instead of falling back to a merge commit. | rule | P5 | — | — | none |
| commits-058 | L64-L65 | No Git operation is required for a no-commit workflow that integrates attributable file changes. | definition | — | — | — | none |

## corrections (`plugins/lusona/references/corrections.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| corrections-001 | L3 | Read before correcting or diagnostically probing an observed failing check or review finding. | rule | — | V8: same policy stated in duplicate group D19 | — | none |
| corrections-002 | L4 | Expected task-local TDD red before implementation does not trigger this procedure. | rule | — | V8: same policy stated in duplicate group D20 | — | none |
| corrections-003 | L6-L7 | Outside a batch, a correction round is one bounded correction or diagnostic experiment for an observed failing check or review finding, followed by its agreed verification. | definition | — | — | — | none |
| corrections-004 | L7-L8 | The initial attempt is not a correction round. | rule | — | — | — | none |
| corrections-005 | L8-L9 | Keep two counts for the same failure across workers, roles, and handoffs: consecutive rounds without material progress, and total rounds. | rule | P2 | V4: "workers" used for Leaf or Coordinator | — | none |
| corrections-006 | L9-L11 | Retain both counts and the evidence in the owning record under [retention](retention.md), with counts in the current handoff; | rule | — | — | — | none |
| corrections-007 | L11 | when saving is prevented, use the permitted channel. | rule | P5 | V8: same policy stated in duplicate group D31 | — | none |
| corrections-008 | L11-L13 | Material progress resolves part of the failure or establishes a new fact that changes the next justified action; | definition | P5 | — | — | none |
| corrections-009 | L13 | a rerun, changed wording, or worker change does not. | definition | P5 | V4: "worker" used for Leaf or Coordinator | — | none |
| corrections-010 | L14 | Expected task-local TDD red before implementation is not a failed attempt or correction round. | rule | — | V8: same policy stated in duplicate group D20 | — | none |
| corrections-011 | L16-L17 | After two consecutive rounds without material progress, stop repeating the affected corrections and report the evidence, ruled-out causes, and missing input or approach. | rule | P7 | — | — | none |
| corrections-012 | L17-L18 | Continue independent authorized work. | rule | P7 | V8: same policy stated in duplicate group D80 | — | none |
| corrections-013 | L18-L20 | While the total is below four, a materially different bounded approach supported by new evidence or a changed prerequisite may proceed within existing authority, with that change, its hypothesis, stopping condition, and expected evidence identified first; | rule | P6, P7 | V3: source sentence has 45 words, limit 40 | — | none |
| corrections-014 | L20-L21 | another round without material progress stops affected work again. | rule | P7 | V3: source sentence has 45 words, limit 40 | — | none |
| corrections-015 | L21-L22 | Relabeling an approach on unchanged inputs and evidence is not a different approach. | definition | — | — | — | none |
| corrections-016 | L22-L23 | Only demonstrated material progress resets the consecutive count; | definition | — | — | — | none |
| corrections-017 | L23 | nothing resets the total. | definition | — | — | — | none |
| corrections-018 | L23-L24 | After four total rounds, stop affected work and ask the user before any further round or approach on that failure. | rule | P6, P7 | — | — | none |
| corrections-019 | L24-L25 | Escalate missing decisions or authority rather than inventing a reset. | rule | P6 | — | — | none |
| corrections-020 | L25 | Inside a batch, the recorded repair budget applies instead. | rule | — | V8: same policy stated in duplicate group D59 | — | none |

## delegation (`plugins/lusona/references/delegation.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| delegation-001 | L3 | Leaves read Assigned leaves and Assignment results; | rule | — | V1: third-person role address; V8: same policy stated in duplicate group D77 | — | none |
| delegation-002 | L3 | coordinators read all sections. | rule | — | V1: third-person role address | — | none |
| delegation-003 | L3-L4 | Reuse current text under [core loading rules](../README.md#loading-rules). | rule | — | V8: same policy stated in duplicate group D71 | — | none |
| delegation-004 | L4-L7 | Coordinators also read [model routing](model-routing.md) before dispatch and [worker lifecycle](worker-lifecycle.md) when responsible for workers or their results, after results and before closing or handing off that responsibility. | rule | — | V1: third-person role address; V4: "workers" used for Leaf or Coordinator; V8: same policy stated in duplicate group D23 | — | none |
| delegation-005 | L7 | Leaves load these procedures only for granted responsibilities. | rule | — | V1: third-person role address; V8: same policy stated in duplicate group D24 | — | none |
| delegation-006 | L11 | Execute the bounded assignment; | rule | — | — | — | none |
| delegation-007 | L11 | return results before waiting/ending. | rule | P7 | — | — | none |
| delegation-008 | L11-L12 | Do not interview users or self-assign another workflow skill/phase. | rule | P6 | V8: same policy stated in duplicate group D25 | — | none |
| delegation-009 | L12 | Additional work requires a new assignment; | rule | P6 | — | — | none |
| delegation-010 | L12-L13 | children require an explicit grant. | rule | P6 | V4: "children" used for Leaf or Coordinator | — | none |
| delegation-011 | L13 | Domain skills supplement assigned scope without expanding responsibility or authority. | rule | P6 | V8: same policy stated in duplicate group D26 | — | none |
| delegation-012 | L14 | Route missing/contradictory context, questions, and recommended next actions to the coordinator; | rule | P6 | — | — | none |
| delegation-013 | L15-L16 | it reconciles findings, asks users through the permitted native tool, and alone writes shared queues, batch records, and their handoffs. | rule | P6 | V1: third-person statement of coordinator duties inside a leaf section; V8: same policy stated in duplicate group D08 | — | none |
| delegation-014 | L16 | Preserve the result and stop owned work before cooperating with shutdown; | rule | — | V8: same policy stated in duplicate group D61 | — | none |
| delegation-015 | L17 | report unfinished operations preventing safe shutdown. | rule | P5 | — | — | none |
| delegation-016 | L21 | Final reports contain these fields (`none` where applicable): | rule | — | — | — | none |
| delegation-017 | L23 | Status: `complete`, `blocked`, or `incomplete` as defined below. | definition | — | — | — | none |
| delegation-018 | L24 | Outcome: accomplished scope; changed paths/artifacts. | definition | — | — | — | none |
| delegation-019 | L25 | Verification: checks/results; required checks failing or unrun. | definition | P5 | — | — | none |
| delegation-020 | L26 | Remaining work and concerns: unfinished scope, findings, limits, blockers. | definition | — | — | — | none |
| delegation-021 | L27 | Recovery: retained work, active operations/children, next action/input. | definition | — | V4: "children" used for Leaf or Coordinator | — | none |
| delegation-022 | L28-L30 | Correction rounds: for correction/diagnostic work, each round, material progress, resulting consecutive/total counts for the failure under [correction limits](corrections.md), or the charged rounds under the batch repair budget inside a batch. | definition | — | — | — | none |
| delegation-023 | L32 | \| Status \| Meaning \| | not a rule | — | — | — | none |
| delegation-024 | L34 | \| `complete` \| Assigned scope and required checks satisfied \| | definition | P5 | — | — | none |
| delegation-025 | L35 | \| `blocked` \| Unavailable input, decision, permission, dependency, or capability prevents progress; report attempts and resumption prerequisite \| | definition | P7 | — | — | none |
| delegation-026 | L36 | \| `incomplete` \| Work/verification remains without a named blocking prerequisite \| | definition | — | — | — | none |
| delegation-027 | L38 | Statuses describe assignments, not queue state, coordinator acceptance, exit codes, or lifecycle. | definition | — | — | — | none |
| delegation-028 | L39 | A complete review may find defects; | definition | — | — | — | none |
| delegation-029 | L39 | unmet required checks prevent implementation `complete`. | rule | P5 | V8: same policy stated in duplicate group D01 | — | none |
| delegation-030 | L43 | Delegate the substantive specialist outcome, not merely inspection. | rule | — | V8: same policy stated in duplicate group D68 | — | none |
| delegation-031 | L43-L46 | Supply explicit workflow role and responsibilities, persona, bounded outcome, completion checks, write ownership, authority, explicit TDD/source, relevant workflow/domain skills, role-specific core sections, and Assignment results. | rule | P2, P6 | — | — | none |
| delegation-032 | L46-L47 | Supply accessible paths with explicit loading instructions or current text; | rule | — | V8: same policy stated in duplicate group D85 | — | none |
| delegation-033 | L47 | identify supplied/inherited sources and fill gaps under Loading rules. | rule | — | — | — | none |
| delegation-034 | L48 | Installation and anchor links do not prove context inheritance or section-only host loading. | rule | P5 | V8: same policy stated in duplicate group D67 | — | none |
| delegation-035 | L49-L50 | Prefer bounded context to full history: retain accepted intent, constraints, evidence, failure counts, and recovery inputs; | rule | P2 | V5: "Prefer" leaves the condition for full history unstated | — | none |
| delegation-036 | L50 | include only applicable procedures. | rule | — | V8: same policy stated in duplicate group D83 | — | none |
| delegation-037 | L50-L51 | Independent reviewers receive agreement, actual diff, and verification evidence without implementer conclusions. | rule | P5 | V1: third-person statement of a dispatch duty; V8: same policy stated in duplicate group D69 | — | none |
| delegation-038 | L55 | Coordinator acceptance is separate from worker completion or capacity release. | rule | P5 | V4: "worker" used for Leaf or Coordinator; V8: same policy stated in duplicate group D75 | — | none |
| delegation-039 | L55-L56 | Verify completed scope, resolve concerns, supply/defer blocked prerequisites, and schedule bounded incomplete continuation. | rule | P5, P7 | — | — | none |
| delegation-040 | L57 | Reconcile against acceptance and [verification rules](tdd.md); | rule | — | — | — | none |
| delegation-041 | L57 | serialize dependencies/mutable checks. | rule | — | — | — | none |
| delegation-042 | L58 | Reuse adequate checks on unchanged inputs; | rule | P2 | V8: same policy stated in duplicate group D44 | — | none |
| delegation-043 | L58-L59 | rerun for changed inputs, failures, missing/unreliable evidence, or concrete unresolved risks. | rule | P2, P5 | V8: same policy stated in duplicate group D44 | — | none |
| delegation-044 | L59 | Independently required checks/review still apply. | rule | P5 | — | — | none |
| delegation-045 | L61 | Missing/malformed reports, idle notifications, and crashes are not success. | rule | P5 | V8: same policy stated in duplicate group D60 | — | none |
| delegation-046 | L61-L62 | Ask reachable workers for missing information or reconcile artifacts/host evidence; | rule | P5 | V4: "workers" used for Leaf or Coordinator | — | none |
| delegation-047 | L62 | leave unresolved until established. | rule | P5 | — | — | none |
| delegation-048 | L63 | Map legacy `DONE` to `complete` only after evidence checks; | rule | P5 | — | — | none |
| delegation-049 | L63 | `NEEDS_CONTEXT`/`BLOCKED` to `blocked`; | rule | — | — | — | none |
| delegation-050 | L64 | assess `DONE_WITH_CONCERNS` against completion criteria without rewriting history. | rule | — | — | — | none |
| delegation-051 | L66-L67 | For blocked work, supply missing context, fix environment, select a stronger model when allowed and reasoning is insufficient, or split oversized separable outcomes. | rule | P7 | — | — | none |
| delegation-052 | L67-L68 | Ask users only for decisions/authority the coordinator cannot supply. | rule | P6 | V8: same policy stated in duplicate group D62 | — | none |
| delegation-053 | L68 | Do not retry unchanged blocked inputs/approach. | rule | P7 | — | — | none |
| delegation-054 | L68-L69 | Before transferring edits, stop the previous writer and explicitly transfer ownership; | rule | — | — | — | none |
| delegation-055 | L69 | avoid overlapping writers. | rule | — | V5: "avoid" states no condition or check | — | none |
| delegation-056 | L69-L70 | Preserve edits/evidence; | rule | — | — | — | none |
| delegation-057 | L70 | supply current state, remaining outcome, authority, and TDD to the successor. | rule | P2 | — | — | none |

## evidence (`plugins/lusona/references/evidence.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| evidence-001 | L3-L4 | Read before starting a measurement or experiment, and when producing or retaining material measurements, evaluations, or experiments. | rule | P5 | V8: same policy stated in duplicate group D27 | — | none |
| evidence-002 | L8-L9 | Optional [measurement](../skills/measure/SKILL.md) or [experimentation](../skills/experiment/SKILL.md) requires explicit or standing authority and a finite scope and resource budget; | rule | P6 | — | — | none |
| evidence-003 | L9-L10 | uncertainty alone does not launch studies or repeated offers. | definition | P6, P7 | — | — | none |
| evidence-004 | L10-L11 | Small self-contained empirical checks with available tools and inputs may stay with their owner without a separate study, delegate, stage, or evidence file; | rule | — | V5: "small self-contained" has no measurable bound | — | none |
| evidence-005 | L12 | diagnostic probes remain [investigation](../skills/investigate/SKILL.md). | definition | P1 | — | — | none |
| evidence-006 | L12-L13 | Keep routine evidence with its task; | rule | — | — | — | none |
| evidence-007 | L13 | retain material evidence and provenance under the rules below. | rule | P5 | — | — | none |
| evidence-008 | L13-L14 | Improvement claims need comparable support; | rule | P5 | — | — | none |
| evidence-009 | L14 | report unmet requirements and unsupported claims. | rule | P5 | — | — | none |
| evidence-010 | L14-L15 | Checks, TDD, empirical acceptance, and resource boundaries remain binding. | rule | P5, P6 | — | — | none |
| evidence-011 | L19-L20 | Save material decision evidence before handoff or completion without a separate save request under [retention](retention.md) and the core's write restrictions. | rule | P7 | V8: same policy stated in duplicate group D30 | — | none |
| evidence-012 | L20 | Disposable work needs no record. | definition | — | — | — | none |
| evidence-013 | L21 | Saving does not authorize new collection, implementation, or external actions. | rule | P6 | — | — | none |
| evidence-014 | L25 | Use relevant sections of the [evidence template](../templates/evidence.md). | rule | — | — | — | none |
| evidence-015 | L25-L26 | New material decision evidence lives in the consuming project's `docs/lusona/evidence/`: | definition | — | — | K2 | none |
| evidence-016 | L28 | A small one-off result can use `YYYY-MM-DD-<topic>.md`. | rule | — | — | K2 | none |
| evidence-017 | L29-L30 | Repeated runs or substantial artifacts can use `YYYY-MM-DD-<topic>/README.md` with `runs/001.md`, `runs/002.md`, or run directories such as `runs/001/README.md` as needed. | rule | — | V5: "as needed" vague condition | K2 | none |
| evidence-018 | L31 | The topic README states the question and links the runs; | definition | — | — | — | none |
| evidence-019 | L31 | it is not a copy of every result. | definition | — | — | — | none |
| evidence-020 | L33 | Reuse the topic owner when continuing the same question. | rule | P2 | — | — | none |
| evidence-021 | L33-L34 | Use unambiguous run identifiers within it. | rule | — | — | — | none |
| evidence-022 | L34 | A dated file is itself an exact run when no further split is useful. | definition | — | V5: "when no further split is useful" names no check | — | none |
| evidence-023 | L34-L35 | Do not create a directory tree or migrate existing notes solely to satisfy the new layout. | rule | — | V8: same policy stated in duplicate group D38 | — | none |
| evidence-024 | L39-L43 | Record enough method and provenance to interpret and reproduce the result: question and decision; declared design where applicable; metrics and units; population/workload and sample; reference; pinned revisions or artifact identifiers and local modifications; instrument and method versions; relevant inputs and environment; procedure; observations; uncertainty and limitations; conclusion. | rule | P5 | V5: "enough" sets no measurable bound; V3: source sentence has 47 words, limit 40 | — | none |
| evidence-025 | L43-L44 | Explain unavailable provenance and its effect rather than claiming reproducibility. | rule | P5 | — | — | none |
| evidence-026 | L44 | Separate observations, inference, and exploratory findings. | rule | P5 | — | — | none |
| evidence-027 | L46 | Preserve prior observations and the design that preceded them. | rule | P4 | — | — | none |
| evidence-028 | L46-L47 | Add a new run for new observations; | rule | P4, P5 | — | — | none |
| evidence-029 | L47 | do not overwrite an earlier result with a more favorable one. | rule | P5 | — | — | none |
| evidence-030 | L47-L49 | Correct transcription errors or refuted interpretations visibly beside the original claim, identifying the correction and reason. | rule | P4, P5 | V8: same policy stated in duplicate group D72 | — | none |
| evidence-031 | L49-L50 | Keep a topic's current conclusion and latest **comparable** result distinct from its chronologically latest run; | rule | P5 | — | — | none |
| evidence-032 | L50 | link the exact supporting runs and explain comparison limits. | rule | P5 | — | — | none |
| evidence-033 | L52-L53 | Retain methods, provenance, results, and material artifacts needed to support the decision, including unfavorable results that affect it. | rule | P5 | — | — | none |
| evidence-034 | L53-L54 | Large raw outputs may use a durable artifact reference with identifier, location, and access/reproduction information; | rule | — | V7: "large raw outputs" has no size threshold | — | none |
| evidence-035 | L54-L55 | avoid committing large disposable outputs. | rule | — | V7: "large disposable outputs" has no size threshold | — | none |
| evidence-036 | L55-L56 | Scratch prototypes, harnesses, and transient output belong under repo-local `tmp/` where practical. | rule | — | V5: "where practical" hedge | — | none |
| evidence-037 | L56 | Before cleanup, preserve the material evidence or a durable reference; | rule | P5 | — | — | none |
| evidence-038 | L57 | do not leave the only supporting evidence in disposable scratch storage. | rule | P5 | — | — | none |
| evidence-039 | L61 | Specs, notes, ADRs, and history link exact evidence files or runs for claims they rely on. | rule | P5 | V8: same policy stated in duplicate group D73 | — | none |
| evidence-040 | L62 | Notes discuss implications, alternatives, and open questions; | definition | — | — | — | none |
| evidence-041 | L62-L63 | the evidence record owns the observations and methods. | definition | — | — | — | none |
| evidence-042 | L63-L64 | A link to a changing topic summary alone does not identify the run supporting a claim. | definition | P5 | — | — | none |
| evidence-043 | L64 | Existing notes and other established records stay in place; | rule | — | V8: same policy stated in duplicate group D38 | — | none |
| evidence-044 | L64-L65 | link them instead of migrating or duplicating their evidence. | rule | — | V8: same policy stated in duplicate group D38 | — | none |
| evidence-045 | L67 | Routine test, build, and task verification logs stay with the task's existing evidence owner. | rule | — | — | — | none |
| evidence-046 | L68 | The dedicated home is for material decision evidence, not every command output. | definition | — | — | — | none |
| evidence-047 | L68-L69 | Saving a measurement does not require a spec, queue entry, plan, or a new approval. | rule | P7 | — | — | none |
| evidence-048 | L69-L70 | Retention and closeout preserve links needed to explain a decision or resume work; | rule | P4 | — | — | none |
| evidence-049 | L70-L71 | a concise conclusion must not replace its material method, provenance, and results. | rule | P5 | — | — | none |

## files (`plugins/lusona/references/files.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| files-001 | L3 | Read when locating project records or maintaining legacy ones. | rule | — | — | — | none |
| files-002 | L3-L4 | The consuming project owns its data; | definition | — | V8: same policy stated in duplicate group D10 | K2 | none |
| files-003 | L4 | paths are relative to that project. | definition | — | V8: same policy stated in duplicate group D10 | K2 | none |
| files-004 | L4 | Bundled links are relative to the loaded resource. | definition | — | V8: same policy stated in duplicate group D11 | — | none |
| files-005 | L8 | \| Path \| Purpose \| | not a rule | — | — | — | none |
| files-006 | L10 | \| `docs/lusona/README.md` \| Optional project-local contract, including a standing TDD preference \| | catalog | — | — | K2 | none |
| files-007 | L11 | \| `docs/lusona/product.md` \| Product brief, capability map, shared architecture context and ADR links \| | catalog | — | — | K2 | none |
| files-008 | L12 | \| `docs/lusona/work.md` \| Current queue; owns active state, priority, and concise completion conditions \| | catalog | — | — | K2 | none |
| files-009 | L13 | \| `docs/lusona/specs/<change-id>.md` \| Change agreement, optional execution steps, evidence, and one current handoff \| | catalog | — | — | K2 | none |
| files-010 | L14 | \| `docs/lusona/plans/<change-id>.md` \| Existing separate execution records remain valid; no new companion file by default \| | catalog | — | V8: same policy stated in duplicate group D57 | K2 | none |
| files-011 | L15 | \| `docs/lusona/batches/<batch-slug>.md` \| Parent-owned fixed selection, authority, assignments, recovery pointers, and current batch handoff \| | catalog | — | — | K2 | none |
| files-012 | L16 | \| `docs/lusona/notes/<change-slug>.md` \| Substantive findings, synthesis, or spec-free execution agreement and evidence without another owner \| | catalog | — | — | K2 | none |
| files-013 | L17 | \| `docs/lusona/visuals/<record-id>/` \| Chosen UI option's HTML and PNGs per state, or diagram Mermaid Markdown, with its `reference.md` binding list under [visuals](visuals.md); `<record-id>` is the owning spec or ADR basename or notes slug \| | catalog | — | — | K2 | none |
| files-014 | L18 | \| `docs/lusona/evidence/` \| Material measurement and experiment records, with exact-run references under [evidence](evidence.md) \| | catalog | — | — | K2 | none |
| files-015 | L19 | \| `docs/lusona/history/YYYY-MM-week-NN.md` \| Compact completed-item index; owns archived state and completion references under [closeout](closeout.md) \| | catalog | — | — | K2 | none |
| files-016 | L20 | \| `docs/lusona/adr/<YYYYMMDD>-<decision-slug>.md` \| Consequential architecture decision, shared or change-specific \| | catalog | — | — | K2 | none |
| files-017 | L21 | \| [Product template](../templates/product.md) \| Product context \| | catalog | — | — | — | none |
| files-018 | L22 | \| [Change template](../templates/spec.md) \| Agreement, optional execution, evidence, and current handoff \| | catalog | — | — | — | none |
| files-019 | L23 | \| [ADR template](../templates/adr.md) \| Architecture decision \| | catalog | — | — | — | none |
| files-020 | L24 | \| [Queue template](../templates/work.md) \| Work queue structure \| | catalog | — | — | — | none |
| files-021 | L25 | \| [Batch template](../templates/batch.md) \| Batch coordination record; links owning requirements and evidence \| | catalog | — | — | — | none |
| files-022 | L26 | \| [History template](../templates/history.md) \| Weekly sections and completed-item structure \| | catalog | — | — | — | none |
| files-023 | L27 | \| [Evidence template](../templates/evidence.md) \| Measurement or experiment design, run results, limitations, and interpretation \| | catalog | — | — | — | none |
| files-024 | L28 | \| [Notes template](../templates/notes.md) \| Durable questions, evidence, conclusions, and current handoff \| | catalog | — | — | — | none |
| files-025 | L29 | \| [Visual reference template](../templates/visual-reference.md) \| Chosen option, source, UI images, binding and illustrative items, fidelity, rejected options \| | catalog | — | — | — | none |
| files-026 | L30 | \| [Visual page template](../templates/visual-page.html) \| Page shell with notes and theme; UI mockup and index variants; device frames, flows, state and option switches; wireframe kit fallback \| | catalog | — | — | — | none |
| files-027 | L34 | Existing combined specs, separate specs and plans, feature documents, and `docs/agent/` records remain valid inputs. | definition | — | V8: same policy stated in duplicate group D58 | — | none |
| files-028 | L35 | Use an existing Feature map as the capability map; | rule | — | — | — | none |
| files-029 | L35-L36 | do not create a duplicate or rename consuming-project sections solely to adopt terminology. | rule | — | — | — | none |
| files-030 | L37 | Use their execution sections or linked plans and handoff in place; | rule | — | — | — | none |
| files-031 | L37-L38 | do not automatically migrate them or create another maintained copy. | rule | — | — | — | none |
| files-032 | L38-L40 | Split or move existing records only when requested, preserving criterion and task IDs, decisions, TDD, evidence, authorization, and references. | rule | P6 | — | — | none |
| files-033 | L40 | See [compatibility](https://github.com/lusona/ai-skills/blob/main/INSTALL.md#document-compatibility). | not a rule | — | — | — | none |
| files-034 | L42 | Create documents only as the authorized work needs them. | rule | P6 | — | — | none |
| files-035 | L42-L43 | Installing the plugin does not initialize project data. | definition | — | V8: same policy stated in duplicate group D12 | — | none |
| files-036 | L43 | Never write consuming-project data into installed plugin resources. | rule | — | V8: same policy stated in duplicate group D10 | — | none |

## handoff (`plugins/lusona/references/handoff.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| handoff-001 | L3 | Read before a checkpoint or handoff. | rule | — | V8: same policy stated in duplicate group D28 | — | none |
| handoff-002 | L3-L4 | The [core context budget](../README.md#context-budget) owns when to hand off; | definition | — | V8: README budget and this file point at each other | — | none |
| handoff-003 | L4 | this procedure owns what the handoff carries and how work resumes. | definition | — | — | — | none |
| handoff-004 | L6-L7 | In the owning current handoff preserve objective, decisions, authority, TDD reference, paths, evidence, correction counts, blockers, ownership, and next action; | rule | P2 | P2: handoff fields omit uncertainty | — | none |
| handoff-005 | L7-L8 | replace its predecessor under [retention](retention.md). | rule | P4 | — | — | none |
| handoff-006 | L8-L9 | If saving is prevented, return the handoff through the permitted channel and state the recovery limit. | rule | P5 | V8: same policy stated in duplicate group D31 | — | none |
| handoff-007 | L9 | Resume from surviving records and the working tree; | rule | P7 | — | — | none |
| handoff-008 | L10 | ask only for unrecoverable material facts or authority. | rule | P6, P7 | V8: same policy stated in duplicate group D62 | — | none |
| handoff-009 | L10-L11 | Do not claim checkpoints prevented by abrupt interruption. | rule | P5 | — | — | none |
| handoff-010 | L11 | Finish or safely pause bounded operations before transfer. | rule | P7 | — | — | none |
| handoff-011 | L11-L12 | Checkpointing ends neither authorization nor requires a new session. | definition | P6, P7 | — | — | none |

## interview-examples (`plugins/lusona/references/interview-examples.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| interview-examples-001 | L3 | Optional illustrations for a specific interviewing difficulty. | not a rule | — | V2: preamble describing the file | — | none |
| interview-examples-002 | L3-L4 | Read only the relevant section; | rule | — | — | — | none |
| interview-examples-003 | L4 | these are not required scripts or a question sequence. | definition | — | — | — | none |
| interview-examples-004 | L4-L6 | The [intent interview contract](interviews.md) governs questions, corrections, and user authority; | definition | — | — | — | none |
| interview-examples-005 | L6 | examples grant no permission to save documents or implement. | definition | P6 | — | — | none |
| interview-examples-006 | L8 | [Future experience](#explore-develop-the-future-experience): move beyond a proposed feature. | catalog | — | — | — | none |
| interview-examples-007 | L9 | [Ambition and initial scope](#product-preserve-ambition-while-defining-initial-scope): retain the product's long view. | catalog | — | — | — | none |
| interview-examples-008 | L10 | [Next delivery](#capabilities-connect-the-next-delivery-to-the-vision): connect priorities to the vision. | catalog | — | — | — | none |
| interview-examples-009 | L11 | [Context reuse](#reuse-context-avoid-restarting-discovery): build on settled answers. | catalog | — | — | — | none |
| interview-examples-010 | L12 | [Correction](#correction-revise-the-interpretation): revise an incorrect interpretation. | catalog | — | — | — | none |
| interview-examples-011 | L16-L32 | **User:** I want to add a dashboard for team managers. **Assistant:** What should managers be able to understand or decide that they struggle with today? **User:** They discover delays too late and spend meetings collecting updates. **Assistant:** Is the longer-term ambition to help managers detect delays sooner, or to let teams coordinate without managers collecting updates? Both could matter; which change is more important to you? **User:** Teams should coordinate themselves. Managers should handle exceptions. **Assistant:** That suggests the dashboard should make unresolved exceptions visible. It might eventually need fewer routine status details as teams gain better coordination tools. Can you describe a situation the team should handle independently, and one that should reach a manager? | example | — | — | — | none |
| interview-examples-012 | L34-L35 | *Why this works:* The interview moves from a proposed feature to a desired future, then uses a concrete scenario to clarify the distinction. | example | P2 | — | — | none |
| interview-examples-013 | L35 | The interpretation remains provisional. | example | P2 | — | — | none |
| interview-examples-014 | L39-L56 | **User:** We want to make it easier for independent tutors to run their businesses. Scheduling is the first problem. **Assistant:** When the product has matured, what should a tutor's working day look like? **User:** They should spend their time teaching. Scheduling, payments, and follow-ups should mostly happen automatically. **Assistant:** The intended future is a business that requires less routine administration. Scheduling is the initial scope; payments and follow-ups remain part of the ambition. What should tutors always control themselves, even if we could automate it? **User:** Prices and communication with parents. We can draft messages, but tutors should approve them. **Assistant:** Then tutor control over pricing and parent communication is a product principle. The scheduling scope should respect that principle, and future automation should preserve it. Have I captured the distinction correctly? | example | — | — | — | none |
| interview-examples-015 | L58 | *Why this works:* The first delivery does not become the entire product definition. | example | — | — | — | none |
| interview-examples-016 | L59-L60 | The interview establishes a principle that can guide later decisions and offers a correction opportunity without requiring repeated approval of established answers. | example | P7 | — | — | none |
| interview-examples-017 | L64-L81 | **User:** Let's build tutor booking first. Payments can wait. **Assistant:** Booking can deliver value before payments. For the longer-term experience, should a parent book individual lessons, or establish an ongoing arrangement with a tutor? **User:** Mostly ongoing weekly lessons, with occasional changes. **Assistant:** Recurring arrangements therefore belong in the capability map. A first delivery could support one-off bookings to test demand, or weekly bookings to test the main workflow. Weekly bookings would also require rules for cancellations and exceptions. Which uncertainty matters more right now? **User:** Whether tutors and parents can manage a weekly schedule without messaging back and forth. **Assistant:** Then I recommend weekly bookings with a simple cancellation and rescheduling flow as the first outcome. Payments remain deferred. The first delivery tests the coordination problem central to your vision. | example | — | — | — | none |
| interview-examples-018 | L83-L84 | *Why this works:* The recommendation follows the user's learning priority and long-term workflow, rather than implementation convenience. | example | — | — | — | none |
| interview-examples-019 | L84-L85 | A proposed first outcome is not a detailed specification or permission to execute it. | example | P6 | V8: same policy stated in duplicate group D05 | — | none |
| interview-examples-020 | L89-L99 | **User:** We already agreed on the tutor vision. Can we move payment reminders ahead of payment collection? **Assistant:** Yes. Reminders could use payment status entered by the tutor, with automated collection added later. That would reduce follow-up work but retain manual bookkeeping. Is that tradeoff acceptable for the next delivery? **User:** Yes, provided reminders are drafts the tutor approves. **Assistant:** That also preserves the established communication principle. The revised proposed order is payment tracking and reminder drafts, followed later by automated collection. | example | — | — | — | none |
| interview-examples-021 | L101-L102 | *Why this works:* The model answers the question, uses established intent, and asks only about the new tradeoff. | example | P7 | — | — | none |
| interview-examples-022 | L102 | Once the requested sequencing question is resolved, it stops. | example | P7 | — | — | none |
| interview-examples-023 | L106-L120 | **User:** I want tutors to spend less time on administration. **Assistant:** Should the mature product handle routine parent communication automatically? **User:** No. Personal contact is part of the service. I want tutors to prepare for those conversations faster, not send fewer messages. **Assistant:** I interpreted less administration as less direct communication. Your goal is to reduce preparation work while preserving personal contact. What does a tutor currently have to gather before speaking with a parent? **User:** Notes from previous lessons and whether the student did the practice work. **Assistant:** Then a useful capability to explore is preparing that information for the tutor before the conversation. Automatic messaging does not follow from the goal you described. | example | — | — | — | none |
| interview-examples-024 | L122 | *Why this works:* The correction changes both the next question and the proposed capability. | example | P2 | — | — | none |
| interview-examples-025 | L123 | The model does not retain its earlier interpretation as an accepted requirement. | example | P4 | — | — | none |

## interviews (`plugins/lusona/references/interviews.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| interviews-001 | L3-L4 | Read for explore, frame-product, map-capabilities, and architect when intent or acceptable tradeoffs are unclear. | rule | — | — | — | none |
| interviews-002 | L6-L7 | Explore, frame-product, and map-capabilities develop shared understanding before settling a direction, brief, or map. | definition | P2 | V1: third-person skill description, no imperative | — | none |
| interviews-003 | L7 | Architect interviews when intent or acceptable tradeoffs are unclear. | definition | — | V1: third-person skill description, no imperative | — | none |
| interviews-004 | L8 | The coordinator owns the conversation; | definition | P6 | — | — | none |
| interviews-005 | L8-L9 | specialists return focused questions and decision impact before dependent synthesis and use the supplied answers. | rule | P6 | V1: third-person role statement | — | none |
| interviews-006 | L9 | Independent evidence gathering can continue. | definition | P7 | — | — | none |
| interviews-007 | L11 | Start from supplied intent and established decisions. | rule | P3 | — | — | none |
| interviews-008 | L11-L12 | Investigate discoverable facts using available evidence; | rule | P5 | — | — | none |
| interviews-009 | L12 | ask the user about desired outcomes, priorities, experience, and tradeoffs. | rule | P6 | — | — | none |
| interviews-010 | L13 | Repository behavior does not establish what the user wants or understands. | rule | P5 | — | — | none |
| interviews-011 | L14 | Ask focused questions or a small related group, following dependencies and the answers. | rule | — | V7: "a small related group" has no count | — | none |
| interviews-012 | L15 | Explain choices with concrete scenarios at the user's level; | rule | — | — | — | none |
| interviews-013 | L15-L16 | invite reactions that develop understanding. | rule | — | — | — | none |
| interviews-014 | L16 | Do not use a fixed questionnaire or only fill artifact fields. | rule | — | — | — | none |
| interviews-015 | L17-L18 | Develop the intended long-term experience while distinguishing aspirations, initial scope, deferred capabilities, and commitments. | rule | P2 | — | — | none |
| interviews-016 | L18 | Reuse existing vision; | rule | P3 | P3: reuse of existing vision states no handling of contradicting input | — | none |
| interviews-017 | L18 | keep narrow questions scoped. | rule | — | — | — | none |
| interviews-018 | L19 | Reflect consequential interpretations and offer correction before settling output. | rule | P2 | — | — | none |
| interviews-019 | L19-L20 | Revise questions and proposals when corrected; | rule | P4 | — | — | none |
| interviews-020 | L20 | distinguish evidence, assumptions, proposals, and decisions. | rule | P2, P5 | — | — | none |
| interviews-021 | L21 | Reuse answers; | rule | P2 | V8: same policy stated in duplicate group D33 | — | none |
| interviews-022 | L21 | answer direct questions first. | rule | — | V8: same policy stated in duplicate group D32 | — | none |
| interviews-023 | L21-L22 | Stop when further answers would not change the outcome or the user asks to move on. | rule | P7 | V8: same policy stated in duplicate group D34 | — | none |
| interviews-024 | L22 | Label remaining assumptions; | rule | P5 | — | — | none |
| interviews-025 | L22-L23 | unresolved blocking decisions remain blocking. | definition | P7 | — | — | none |
| interviews-026 | L23 | An unanswered intent question is not answered by drafting a document. | definition | P6 | — | — | none |
| interviews-027 | L25-L26 | Consult [interview examples](interview-examples.md) only for a concrete uncertainty about interview technique. | rule | — | — | — | none |
| interviews-028 | L26 | Unattended batches reuse settled intent and defer consequential gaps. | rule | P3, P7 | P3: batches reuse settled intent with no revisit path | — | none |

## model-routing (`plugins/lusona/references/model-routing.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| model-routing-001 | L3 | Coordinators read before dispatching an assignment. | rule | — | V1: third-person role address; V8: same policy stated in duplicate group D23 | — | none |
| model-routing-002 | L5-L6 | Before every dispatch, select the least capable available model adequate for the assignment and a supported reasoning setting. | rule | — | — | — | none |
| model-routing-003 | L6-L7 | This is explicit routing guidance for model and reasoning overrides, subject to user choices and host restrictions. | definition | P6 | V9: describes the guidance's status instead of an action; V8: same policy stated in duplicate group D84 | — | none |
| model-routing-004 | L7-L8 | Consider uncertainty, coupling, failure consequences, and verification strength; | rule | — | V5: banned hedge "Consider" | — | none |
| model-routing-005 | L8 | file count alone does not establish complexity. | rule | — | — | — | none |
| model-routing-006 | L10 | \| Tier \| Choose when \| | not a rule | — | — | — | none |
| model-routing-007 | L12 | \| `fast` \| Instructions are clear, scope is isolated, and checks can establish correctness \| | catalog | — | — | — | none |
| model-routing-008 | L13 | \| `standard` \| Work requires implementation judgment within established boundaries \| | catalog | — | — | — | none |
| model-routing-009 | L14 | \| `deep` \| Work involves substantial uncertainty, interacting invariants, or consequential failure \| | catalog | — | — | — | none |
| model-routing-010 | L16 | Tiers describe the worker's model capability. | definition | — | V4: "worker" used for Leaf or Coordinator | — | none |
| model-routing-011 | L16-L17 | The `fast` tier is unrelated to a host's fast mode, which keeps the same model and changes output speed and cost. | definition | — | V9: explains an unrelated host feature | — | none |
| model-routing-012 | L19-L20 | Use the consuming project's instructions to map tiers to available models and supported reasoning settings. | rule | — | — | — | none |
| model-routing-013 | L20-L21 | Without a mapping, select from the host's exposed models and supported settings using their capability descriptions. | rule | — | — | — | none |
| model-routing-014 | L21-L22 | Pass the selected model and reasoning setting explicitly through the host's dispatch controls; | rule | — | — | — | none |
| model-routing-015 | L22-L23 | a tier label in the assignment does not select a model. | rule | — | — | — | none |
| model-routing-016 | L23 | Do not invent identifiers or assume unsupported controls. | rule | P5 | — | — | none |
| model-routing-017 | L23-L24 | Preserve explicit user model choices and host restrictions. | rule | P6 | V8: same policy stated in duplicate group D84 | — | none |
| model-routing-018 | L24-L25 | For each setting, inherit when those constraints require it or its selection control is unavailable; | rule | P6 | — | — | none |
| model-routing-019 | L25 | still select other independently supported settings. | rule | — | — | — | none |
| model-routing-020 | L26 | Report when this prevents the selected routing. | rule | P5 | — | — | none |
| model-routing-021 | L26-L27 | Selecting the current model remains valid when it is adequate and no less capable available model suffices. | definition | — | — | — | none |
| model-routing-022 | L28 | Routing selects the worker's model; | definition | — | V4: "worker" used for Leaf or Coordinator | — | none |
| model-routing-023 | L28 | it does not change the coordinator's model. | definition | — | — | — | none |
| model-routing-024 | L30 | Choose a context mode compatible with the selected model and reasoning setting. | rule | — | — | — | none |
| model-routing-025 | L30-L32 | When the host prohibits overrides with full-history forks, supply a bounded assignment with the needed instructions and inputs instead. | rule | — | — | — | none |
| model-routing-026 | L32-L33 | For hosts exposing `fork_turns` with that restriction, use `"none"` or a supported positive turn count; | rule | — | — | — | none |
| model-routing-027 | L33-L34 | omitted or `"all"` inherits the parent's model and reasoning settings. | definition | — | V4: "the parent" used for Leaf or Coordinator | — | none |
| model-routing-028 | L34 | Do not silently drop a selected override to retain full history. | rule | P5 | — | — | none |
| model-routing-029 | L36 | Record routing in the owning change or batch record only when it affects execution; | rule | — | — | — | none |
| model-routing-030 | L36-L37 | reassess at dispatch and escalation rather than requiring a tier and rationale for every planned task. | rule | — | — | — | none |
| model-routing-031 | L38 | Tiers never reduce required verification or expand scope. | definition | P5, P6 | — | — | none |
| model-routing-032 | L38-L39 | Keep useful parallel assignments independent and retain the coordinator's integration and verification responsibilities. | rule | — | V5: "useful parallel assignments" sets no condition | — | none |

## naming (`plugins/lusona/references/naming.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| naming-001 | L3 | Read before creating, updating, or renaming spec, plan, or ADR records. | rule | — | — | — | none |
| naming-002 | L5-L6 | New specs and ADRs use `YYYYMMDD-functional-name.md`, such as `specs/20260926-add-python-support.md` or `adr/20260926-python-runtime.md`. | rule | — | V8: same policy stated in duplicate group D50 | K2 | none |
| naming-003 | L7 | The complete basename is the record ID. | definition | — | — | K2 | none |
| naming-004 | L7-L8 | The prefix is the creation date in the local timezone, not a sequence or priority. | definition | — | — | K2 | none |
| naming-005 | L8 | Preserve the ID and filename on later edits. | rule | — | — | K2 | none |
| naming-006 | L9 | Existing spec/plan pairs retain their shared basename. | definition | — | — | — | none |
| naming-007 | L9-L10 | Do not create a companion plan for new changes by default. | rule | — | V5: "by default" leaves the exception unstated; V8: same policy stated in duplicate group D57 | — | none |
| naming-008 | L12-L13 | Use the bundled work-record helper to generate the name, check the destination, and create the record exclusively from its template: `init-change` for specs or `init-adr` for ADRs. | rule | — | V8: same policy stated in duplicate group D15 | K3 | none |
| naming-009 | L14 | Choose a descriptive functional slug; | rule | — | — | — | none |
| naming-010 | L14 | use `slug` to normalize a title when needed. | rule | — | V5: "when needed" vague condition | K3 | none |
| naming-011 | L15 | Follow [shell selection, paths, and invocation](work-record.md). | rule | — | V8: same policy stated in duplicate group D16 | K3 | none |
| naming-012 | L17 | Both creation commands accept an optional `YYYY-MM-DD` creation date; | definition | — | — | K3 | none |
| naming-013 | L17-L18 | otherwise they use local today. | definition | — | V8: same policy stated in duplicate group D79 | K3 | none |
| naming-014 | L18 | They return one JSON object on stdout with `status`, `path`, and `message`: | definition | — | V8: same policy stated in duplicate group D53 | K3 | none |
| naming-015 | L20 | \| Status \| Exit code \| Agent action \| | not a rule | — | — | K3 | none |
| naming-016 | L22 | \| `created` \| 0 \| Use the returned absolute path; fill the title and relevant template sections. \| | catalog | — | V8: same policy stated in duplicate group D53 | K3 | none |
| naming-017 | L23 | \| `conflict` \| 3 \| Inspect the existing path. Resume only if it is the intended existing record and ownership permits it; for distinct work choose a more specific functional slug and retry. \| | catalog | — | V8: same policy stated in duplicate group D53 | K3 | none |
| naming-018 | L24 | \| `error` \| 1 \| Correct the reported input or filesystem problem before retrying; `path` is empty if no destination was resolved. \| | catalog | — | V8: same policy stated in duplicate group D53 | K3 | none |
| naming-019 | L26-L27 | Creation never overwrites or silently resumes an existing path, including a symlink or directory. | definition | — | V8: same policy stated in duplicate group D74 | K3 | none |
| naming-020 | L27 | Identical inputs resolve to the same path; | definition | — | — | K3 | none |
| naming-021 | L27-L28 | there is no automatic numeric or random suffix. | definition | — | — | K3 | none |
| naming-022 | L28 | Independent records can be created concurrently without a shared allocator. | definition | — | — | — | none |
| naming-023 | L29 | Exclusive creation prevents two writers from claiming the same path in one filesystem; | definition | — | — | K3 | none |
| naming-024 | L30 | isolated branches can still create the same basename. | definition | — | — | — | none |
| naming-025 | L30-L31 | Reconcile record identity, ownership, and affected links before integration; | rule | — | — | — | none |
| naming-026 | L31 | do not combine unrelated records automatically. | rule | — | — | — | none |
| naming-027 | L32 | Queue updates, shared handoffs, and overlapping edits still require coordinated ownership. | rule | — | — | — | none |
| naming-028 | L34 | The helper fills the record ID and initial Created/Updated dates. | definition | — | — | K3 | none |
| naming-029 | L34-L35 | After substantive edits, use `stamp-header FILE [YYYY-MM-DD]`; | rule | — | — | K3 | none |
| naming-030 | L35 | Created remains immutable and only Updated changes. | definition | — | V8: same policy stated in duplicate group D52 | K3 | none |
| naming-031 | L36 | The command rejects invalid headers or dates that move backwards. | definition | — | — | K3 | none |
| naming-032 | L36 | Do not stamp on reads. | rule | — | — | K3 | none |
| naming-033 | L37 | Completion dates remain in history; | definition | — | — | — | none |
| naming-034 | L37 | spec and plan headers do not duplicate queue state. | definition | — | — | — | none |
| naming-035 | L38 | ADRs retain decision status, scope, authority, and supersession references. | definition | — | — | — | none |
| naming-036 | L40 | Legacy `next-change` and `next-adr` remain available for existing numbered workflows only. | definition | — | V8: same policy stated in duplicate group D51 | K3 | none |
| naming-037 | L41 | They ignore valid dated records and retain their existing sequence validation; | definition | — | V8: same policy stated in duplicate group D51 | K3 | none |
| naming-038 | L41-L42 | they do not reserve numbers and must not be used to name new records under this convention. | rule | — | V8: same policy stated in duplicate group D51 | K3 | none |
| naming-039 | L44 | Existing filenames and headers, including separate plans, remain valid. | definition | — | V8: same policy stated in duplicate group D58 | — | none |
| naming-040 | L44-L45 | Do not invent a number or creation date for an old document. | rule | P5 | — | — | none |
| naming-041 | L45-L46 | Renaming existing records or adopting the new headers requires an authorized migration that preserves dates, evidence, and links; | rule | P6 | — | — | none |
| naming-042 | L46-L47 | normal work does not trigger one. | definition | — | — | — | none |

## queue (`plugins/lusona/references/queue.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| queue-001 | L3 | Read when creating, updating, or using a spec, or maintaining or assessing tracked state, selection, or parking. | rule | — | — | — | none |
| queue-002 | L5 | The coordinator alone updates queue state and the queue and batch handoffs during authorized work. | rule | — | V1: third-person role statement; V8: same policy stated in duplicate group D08 | — | none |
| queue-003 | L5-L6 | The queue tracks whole outcomes, not individual coding tasks; | definition | — | — | — | none |
| queue-004 | L6 | Ready does not authorize execution. | rule | P6 | V8: same policy stated in duplicate group D04 | K4 | none |
| queue-005 | L7 | Prefer finishing active work before starting another item. | rule | — | V5: "Prefer" leaves the exception unstated | — | none |
| queue-006 | L7-L9 | A blocker or pending acceptance need not prevent independent work already authorized by the user, provided writers and unfinished changes remain safely separated. | definition | P7 | — | — | none |
| queue-007 | L9 | Blocked is a flag with its reason and next action. | definition | — | — | — | none |
| queue-008 | L10 | Use [batch execution](batch-execution.md) for unattended multi-item scheduling and recovery. | rule | — | — | — | none |
| queue-009 | L12 | Keep separate **Active queue** and **Icebox** sections. | rule | — | — | K2 | none |
| queue-010 | L12-L14 | Icebox holds deliberately parked outcomes with their lifecycle state, completion condition, evidence links, and a short parking reason or revisit condition. | definition | — | V8: same policy stated in duplicate group D64 | K2 | none |
| queue-011 | L14 | Move rows rather than copying them. | rule | — | — | — | none |
| queue-012 | L14-L15 | Park or reactivate work only within explicit user direction; | rule | P6 | — | — | none |
| queue-013 | L15 | a revisit condition prompts reconsideration, not automatic revival. | definition | P3 | — | — | none |
| queue-014 | L16-L17 | Icebox is excluded from active planning and default batch selection, including “all current queue items.” | definition | — | V8: same policy stated in duplicate group D35 | K2 | none |
| queue-015 | L17 | Explicitly selecting parked work for execution reactivates it; | definition | P6 | — | — | none |
| queue-016 | L17 | discussing it does not. | definition | P6 | — | — | none |
| queue-017 | L18 | Before parking started work, stop its writers and preserve isolated changes and a recovery handoff. | rule | — | — | — | none |
| queue-018 | L19 | Parking does not complete work, erase blockers, or reset batch repair counts. | definition | — | — | — | none |
| queue-019 | L19-L20 | A batch deferral alone does not move an item to Icebox. | definition | — | V8: same policy stated in duplicate group D35 | K2 | none |
| queue-020 | L20 | Existing queues without sections remain active queues; | definition | — | — | — | none |
| queue-021 | L21 | add sections when next updating them without silently parking existing rows. | rule | — | — | — | none |
| queue-022 | L23 | \| State \| Meaning \| Owning procedure \| | not a rule | — | — | K2 | none |
| queue-023 | L25 | \| Ideas \| Possible outcome \| [specify](../skills/specify/SKILL.md) \| | catalog | — | — | K2 | none |
| queue-024 | L26 | \| Ready \| Accepted definition and selected TDD \| [specify](../skills/specify/SKILL.md) \| | catalog | — | — | K2 | none |
| queue-025 | L27 | \| Doing \| Authorized implementation \| [implement](../skills/implement/SKILL.md) \| | catalog | — | — | K2 | none |
| queue-026 | L28 | \| Review \| Evidence ready for review or acceptance \| [implement](../skills/implement/SKILL.md), [review](../skills/review/SKILL.md) \| | catalog | — | — | K2 | none |
| queue-027 | L29 | \| Done \| Agreed completion condition met \| [implement](../skills/implement/SKILL.md) \| | catalog | — | — | K2 | none |
| queue-028 | L31 | Every new spec requires a row in `docs/lusona/work.md`, regardless of which skill creates it. | rule | — | V8: same policy stated in duplicate group D18 | K2 | none |
| queue-029 | L32 | A follow-up found during untracked work takes an Ideas row linking the notes that found it; | rule | — | — | K2 | none |
| queue-030 | L33 | a delegated worker returns the row to its coordinator. | rule | — | V4: "worker" used for Leaf or Coordinator; V8: same policy stated in duplicate group D09 | — | none |
| queue-031 | L34 | The coordinator creates a missing queue from [its template](../templates/work.md). | rule | — | V1: third-person role statement | — | none |
| queue-032 | L34-L35 | Reconcile the selected spec with its existing row or historical entry before adding anything; | rule | — | — | — | none |
| queue-033 | L35-L36 | updates reuse that item without duplication. | rule | — | — | — | none |
| queue-034 | L36 | New drafts start Ideas. | definition | — | — | K2 | none |
| queue-035 | L36-L37 | Ready requires accepted scope and criteria, an explicitly selected TDD policy, and no blocking definition questions. | definition | P6 | — | K2 | none |
| queue-036 | L37-L38 | Preserve existing lifecycle state, Icebox placement, and history; | rule | — | — | — | none |
| queue-037 | L38 | an ordinary spec edit does not reset or reopen work. | rule | — | — | — | none |
| queue-038 | L39-L40 | When planning, implementing, or refactoring from an existing spec, repair its missing row before planning handoff or execution, using supported current state. | rule | — | — | — | none |
| queue-039 | L40-L41 | Do not scan or backfill unrelated specs or restore archived completed items. | rule | — | — | — | none |
| queue-040 | L41 | Reopening requires explicit authority and [closeout](closeout.md). | rule | P6 | V8: same policy stated in duplicate group D54 | — | none |
| queue-041 | L43 | These requirements remain subject to the [core recording restrictions](../README.md#contract). | definition | — | V8: chain, links README contract, which links queue back | — | none |
| queue-042 | L44 | When saving is prevented, report the missing tracking through a permitted channel. | rule | P5 | V8: same policy stated in duplicate group D31 | — | none |
| queue-043 | L45 | Delegated workers return required queue changes to the coordinator; | rule | — | V4: "workers" used for Leaf or Coordinator; V8: same policy stated in duplicate group D09 | — | none |
| queue-044 | L45 | they do not write shared state. | rule | — | V8: same policy stated in duplicate group D08 | — | none |
| queue-045 | L46 | Read-only assessment reports gaps without repairing them. | rule | P6 | V8: same policy stated in duplicate group D49 | — | none |
| queue-046 | L48-L49 | The coordinator moves selected authorized implementation or refactoring to Doing when execution starts; | rule | P6 | V1: third-person role statement | K2 | none |
| queue-047 | L49 | planning-only work never enters Doing. | rule | P6 | V8: same policy stated in duplicate group D56 | K2 | none |
| queue-048 | L49-L50 | Queue membership does not authorize implementation or select TDD. | rule | P6 | V8: same policy stated in duplicate group D04 | K4 | none |
| queue-049 | L50 | Direct work without a spec may remain untracked; | definition | — | — | — | none |
| queue-050 | L50-L51 | [retention](retention.md) states what its notes retain and when a spec is required. | definition | — | — | — | none |
| queue-051 | L51 | Existing tracked work remains tracked. | definition | — | V8: same policy stated in duplicate group D36 | — | none |
| queue-052 | L52 | A recovery note alone does not require a queue, full spec, or history entry. | rule | — | — | — | none |
| queue-053 | L53 | Move work to Review when evidence is ready; | rule | P5 | — | K2 | none |
| queue-054 | L53 | list outstanding checks explicitly. | rule | P5 | — | — | none |
| queue-055 | L54-L55 | Done requires the whole item's completion condition, acceptance criteria, required checks, and any required acceptance or delivery. | rule | P5 | V8: same policy stated in duplicate group D03 | K2 | none |
| queue-056 | L55 | Failed or unrun required checks block completion; | rule | P5 | V8: same policy stated in duplicate group D01 | — | none |
| queue-057 | L55-L56 | passing tests do not establish human acceptance. | rule | P5 | V8: same policy stated in duplicate group D02 | — | none |
| queue-058 | L56-L57 | Return rejected work to Doing for authorized correction, or Ideas/Ready when scope needs reconsideration. | rule | P6 | — | K2 | none |
| queue-059 | L57 | A transition does not authorize fixes. | rule | P6 | — | — | none |
| queue-060 | L58 | Completed items stay Done unless explicitly reopened; | definition | P4 | — | K2 | none |
| queue-061 | L58-L59 | separately requested refactoring may use its own item. | definition | — | — | — | none |
| queue-062 | L59 | Reviews recommend a state without writing the queue. | rule | P6 | V1: third-person role statement | — | none |
| queue-063 | L61-L62 | Before removing a completed row or reopening archived work, the coordinator applies [closeout](closeout.md), preserving history and affected links. | rule | — | V1: third-person role statement; V8: same policy stated in duplicate group D54 | — | none |

## retention (`plugins/lusona/references/retention.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| retention-001 | L3 | Read when saving findings or evidence. | rule | — | — | — | none |
| retention-002 | L3-L4 | Closing or reopening tracked work is a separate [coordinator procedure](closeout.md). | definition | — | V8: same policy stated in duplicate group D54 | — | none |
| retention-003 | L6 | Apply the [core recording authority and restrictions](../README.md#contract). | rule | — | V8: chain, links README contract, which links back to retention | — | none |
| retention-004 | L6-L7 | Save substantive workflow outputs without waiting for the user to request a record. | rule | P7 | V8: same policy stated in duplicate group D30 | — | none |
| retention-005 | L7-L9 | In discussion, save when a synthesis captures reusable alternatives and tradeoffs, a supported preference, a meaningful change in understanding, or an open question and next step needed to resume. | rule | P2 | V5: "meaningful change" sets no checkable condition | — | none |
| retention-006 | L9-L10 | Do this once the synthesis is useful, and update it for material changes; | rule | P7 | V5: "once the synthesis is useful" is not a checkable trigger | — | none |
| retention-007 | L10-L11 | do not defer all recording until the conversation ends. | rule | P7 | V8: same policy stated in duplicate group D30 | — | none |
| retention-008 | L11-L12 | Ordinary explanations, greetings, acknowledgments, and disposable questions need no record. | definition | — | — | — | none |
| retention-009 | L12 | Use the existing owner or concise notes; | rule | — | — | — | none |
| retention-010 | L12-L13 | discussion alone requires no spec, queue item, plan, decision, or TDD selection. | definition | — | — | — | none |
| retention-011 | L13-L14 | Save other substantive outputs before handoff or completion. | rule | P7 | V8: same policy stated in duplicate group D30 | — | none |
| retention-012 | L14-L19 | A spec and its queue row are required whenever the workflow calls for a spec (Specify defines every change in one), the user requests a spec or tracking, a spec already exists, or the change requires independent review for security boundaries, persistent data, shared contracts, or coordinated multiple writers under [Review and communication](../README.md#review-and-communication), so the reviewer has acceptance criteria recorded before implementation starts; | rule | — | V9: rationale clause "so the reviewer has acceptance criteria" in instruction; V3: source sentence has 75 words, limit 40; V8: same policy stated in duplicate group D18; V8: same policy stated in duplicate group D22 | — | none |
| retention-013 | L19-L20 | a blanket repository review rule does not by itself require a spec. | definition | — | V3: source sentence has 75 words, limit 40 | — | none |
| retention-014 | L20 | Size and scope do not decide this. | definition | — | — | — | none |
| retention-015 | L20-L22 | Other direct implement or refactor work without a spec uses notes, which may hold its agreement, decisions, explicit TDD/source, checks/evidence, and handoff. | rule | — | — | — | none |
| retention-016 | L22-L23 | Any direct implement or refactor work can also create a spec directly without Specify, using only relevant template sections. | definition | — | — | — | none |
| retention-017 | L24-L25 | Investigations, measurements, and experiments use notes and evidence records. | rule | — | — | — | none |
| retention-018 | L25-L26 | Delegated assignments and handoffs within one session keep their handoff in notes or the owning record. | rule | — | — | — | none |
| retention-019 | L26 | Brief status needs no record. | definition | — | — | — | none |
| retention-020 | L27 | Reuse the existing owner; | rule | — | — | — | none |
| retention-021 | L27 | without one, use the smallest suitable notes or change record. | rule | — | V7: "smallest suitable" has no measurable bound | — | none |
| retention-022 | L28-L29 | Keep only the outcome, authority and TDD source when applicable, decisions, useful evidence, material open questions, ownership, correction counts when any, and next action needed to resume. | rule | P2 | — | — | none |
| retention-023 | L29 | Omit irrelevant fields. | rule | — | — | — | none |
| retention-024 | L30 | Notes do not require a full spec or execution plan. | rule | — | — | — | none |
| retention-025 | L32 | A spec's queue tracking follows the [queue rules](queue.md). | rule | — | V8: same policy stated in duplicate group D18 | — | none |
| retention-026 | L33-L34 | Notes alone do not require tracking: do not enroll spec-free work or restore deleted records merely to save recovery context; | rule | — | — | — | none |
| retention-027 | L34-L35 | an Ideas row for a distinct follow-up does not enroll the current work. | definition | — | — | K2 | none |
| retention-028 | L35 | Existing tracked work remains tracked. | definition | — | V8: same policy stated in duplicate group D36 | — | none |
| retention-029 | L36-L37 | Keep `work.md` as an index of open outcomes: one short row per item, linking its owning records, with a concise completion condition and current blocker or next action. | rule | — | — | K2 | none |
| retention-030 | L37-L38 | Keep task evidence, measurements, decisions, and activity narration out of the queue. | rule | — | — | — | none |
| retention-031 | L38-L39 | Icebox rows remain open and retain evidence under the [queue rules](queue.md); | definition | — | V8: same policy stated in duplicate group D64 | K2 | none |
| retention-032 | L39-L40 | parking is separate from completion and historical archival. | definition | — | — | — | none |
| retention-033 | L42-L45 | During authorized work beyond discussion, tracked or not, keep unresolved supported goal-relevant outcomes discoverable when the current assignment closes: link an existing open item or add a distinct proposal under the queue rules, creating the queue from its template when absent. | rule | P8 | V3: source sentence has 41 words, limit 40 | K2 | none |
| retention-034 | L45 | When saving is prevented, report the unowned follow-up through a permitted channel. | rule | P5 | V8: same policy stated in duplicate group D31 | — | none |
| retention-035 | L45 | Reference the owning evidence once; | rule | — | — | — | none |
| retention-036 | L45-L46 | do not leave the only next action buried in completed work. | rule | P8 | V6: metaphor "buried" | — | none |
| retention-037 | L46 | Retain evidence, uncertainty, and a next action; | rule | P2, P8 | — | — | none |
| retention-038 | L46-L47 | deferred proposals need a reason or revisit condition. | rule | — | — | — | none |
| retention-039 | L47 | A proposal does not authorize execution or join an active batch. | rule | P6 | V8: same policy stated in duplicate group D05 | — | none |
| retention-040 | L49 | Record each fact once. | rule | — | V8: same policy stated in duplicate group D37 | — | none |
| retention-041 | L49-L51 | New change records own accepted scope, acceptance criteria, explicit TDD, optional execution steps, verification evidence, and one current handoff replaced as work progresses. | definition | — | — | — | none |
| retention-042 | L51 | Preserve established ownership for existing separate specs and plans. | rule | — | — | — | none |
| retention-043 | L51-L52 | ADRs own consequential architecture decisions. | definition | — | V8: same policy stated in duplicate group D70 | — | none |
| retention-044 | L52-L53 | Add an execution section only when the [core task conditions](../README.md#work-loop) make it useful. | rule | — | V8: same policy stated in duplicate group D63 | — | none |
| retention-045 | L54 | Tasks reference acceptance criteria rather than restating them. | rule | — | — | — | none |
| retention-046 | L54-L55 | Save routine verification evidence directly in the change record whether or not it has tasks. | rule | P5 | — | — | none |
| retention-047 | L55-L57 | For material measurements and experiments, follow [evidence](evidence.md): new records live in `docs/lusona/evidence/`, and change records, notes, and history link the exact runs they rely on. | rule | P5 | V8: same policy stated in duplicate group D73 | K2 | none |
| retention-048 | L57 | Existing evidence stays in place; | rule | — | V8: same policy stated in duplicate group D38 | — | none |
| retention-049 | L57-L58 | do not migrate it merely to adopt the new layout. | rule | — | V8: same policy stated in duplicate group D38 | — | none |
| retention-050 | L58-L59 | Split a new record only for separate ownership, reuse, or readability, retaining links and one owner for each fact. | rule | — | — | — | none |
| retention-051 | L59-L61 | Use `notes/<change-slug>.md` for useful exploration decisions, open questions, investigations or findings without an existing owner; | rule | — | V5: "useful exploration decisions" sets no condition | K2 | none |
| retention-052 | L61 | an Ideas item needs no premature spec. | definition | — | — | K2 | none |
| retention-053 | L61-L62 | Link notes from the queue or owning record when available. | rule | — | — | — | none |
| retention-054 | L62-L63 | Retain facts needed to resume, explain a decision, reproduce a result, or avoid repeating investigation; | rule | P2, P4 | — | — | none |
| retention-055 | L64 | omit routine narration. | rule | — | — | — | none |
| retention-056 | L64-L65 | Correct refuted findings beside the original claim and revise the resulting recommendation. | rule | P4, P5 | V8: same policy stated in duplicate group D72 | — | none |
| retention-057 | L65-L66 | If a fact gains a change record or ADR owner, replace the notes copy with a link. | rule | P4 | — | — | none |
| retention-058 | L68-L69 | Consolidate ordinary evidence, queue, and handoff edits at meaningful boundaries and before an intentional handoff or completion, including when pausing work. | rule | — | V5: "meaningful boundaries" sets no checkable condition | — | none |
| retention-059 | L69-L70 | Missing directories or a queue do not waive saving: create the needed record directories within permitted writes. | rule | — | — | — | none |
| retention-060 | L70 | Write only changed facts; | rule | — | — | — | none |
| retention-061 | L71 | do not write every turn or refresh records solely because a skill stage ended. | rule | — | — | — | none |
| retention-062 | L71-L73 | Save authorization, blockers, ownership changes, and required batch recovery state when needed for safe continuation. | rule | P7 | V5: "when needed" vague condition | — | none |
| retention-063 | L73-L74 | These saves are working-tree edits, not commit boundaries; | definition | — | — | — | none |
| retention-064 | L74 | group them under the [commit procedure](commits.md). | rule | — | — | — | none |
| retention-065 | L76 | Use the bundled work-record helper for initial notes structure. | rule | — | V8: same policy stated in duplicate group D15 | K3 | none |
| retention-066 | L77 | Follow [shell selection, paths, and invocation](work-record.md). | rule | — | V8: same policy stated in duplicate group D16 | K3 | none |
| retention-067 | L79 | Reuse an existing item slug; | rule | — | V8: same policy stated in duplicate group D76 | — | none |
| retention-068 | L79 | use `slug` for new names. | rule | — | — | K3 | none |
| retention-069 | L79-L80 | Pass an explicit project root for initialization; | rule | — | V8: same policy stated in duplicate group D13 | K3 | none |
| retention-070 | L80 | existing files are preserved. | definition | — | V8: same policy stated in duplicate group D13 | K3 | none |
| retention-071 | L80-L81 | `init-notes` loads the bundled notes template and fills its slug. | definition | — | — | K3 | none |
| retention-072 | L81 | The helper initializes records and returns paths; | definition | — | V8: same policy stated in duplicate group D14 | K3 | none |
| retention-073 | L81-L82 | it does not record evidence or establish completion. | definition | P5 | — | K3 | none |
| retention-074 | L82 | Do not initialize project data merely for orientation or installation. | rule | — | V8: same policy stated in duplicate group D12 | — | none |
| retention-075 | L83 | For closing or reopening tracked work, the coordinator applies [closeout](closeout.md). | rule | — | V1: third-person role statement; V8: same policy stated in duplicate group D54 | — | none |

## tdd (`plugins/lusona/references/tdd.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tdd-001 | L3 | Read when selecting, recording, or applying a TDD policy. | rule | — | V8: same policy stated in duplicate group D78 | — | none |
| tdd-002 | L5 | Implementation requires explicit user selection or a standing preference, with no implicit default. | rule | P6 | V8: same policy stated in duplicate group D06 | K4 | none |
| tdd-003 | L6-L7 | A standing preference is recorded in the project's `docs/lusona/README.md` or its agent instructions (`CLAUDE.md` or `AGENTS.md`). | definition | — | — | K2 | none |
| tdd-004 | L7-L8 | Record selection and source in the owning change record under [retention](retention.md); | rule | — | — | — | none |
| tdd-005 | L8 | when saving is prevented, use conversation. | rule | P5 | V8: same policy stated in duplicate group D31 | — | none |
| tdd-006 | L9-L10 | Unset TDD permits definition and planning, not implementation; | rule | P6 | V8: same policy stated in duplicate group D07 | K4 | none |
| tdd-007 | L10 | no definition phase is required for a clear request. | definition | P1 | — | — | none |
| tdd-008 | L10-L11 | When unset, recommend a level and ask under [Questions and next actions](../README.md#questions-and-next-actions). | rule | P6 | — | — | none |
| tdd-009 | L13 | \| Level \| Requirement \| | not a rule | — | — | K4 | none |
| tdd-010 | L15 | \| `none` \| No test-first requirement; agreed verification and repository checks still apply \| | definition | — | — | K4 | none |
| tdd-011 | L16 | \| `targeted` \| Test first for named behaviors \| | definition | — | — | K4 | none |
| tdd-012 | L17 | \| `strict` \| Test first for every new or changed testable behavior \| | definition | — | — | K4 | none |
| tdd-013 | L19 | For targeted TDD, name the test-first behaviors. | rule | — | — | K4 | none |
| tdd-014 | L19-L20 | Required regression coverage is separate from test-first sequencing. | definition | — | — | — | none |
| tdd-015 | L21-L22 | For test-first behaviors, observe the intended failure before production changes, then verify passing behavior. | rule | P5 | — | — | none |
| tdd-016 | L22 | Record red/green evidence; | rule | P5 | — | — | none |
| tdd-017 | L22-L23 | setup failures and skipped failing runs are not red evidence. | rule | P5 | — | — | none |
| tdd-018 | L23-L24 | Under `none`, run agreed checks and add coverage when it usefully verifies the change or is required. | rule | P5 | V5: "usefully verifies" is not a checkable condition | K4 | none |
| tdd-019 | L25 | Test through observable interfaces. | rule | — | — | — | none |
| tdd-020 | L25 | Reuse adequate coverage; | rule | — | — | — | none |
| tdd-021 | L25-L26 | avoid tests that merely mirror the implementation, | rule | — | — | — | none |
| tdd-022 | L26 | and do not weaken assertions to fit a new structure. | rule | — | — | — | none |
| tdd-023 | L27 | Behavior-preserving restructuring starts green and stays green. | definition | P5 | — | — | none |
| tdd-024 | L27-L28 | Under targeted or strict TDD, first add missing coverage for the affected boundary; | rule | — | — | K4 | none |
| tdd-025 | L28-L29 | characterization tests pass on existing behavior and must exercise the relevant path. | rule | P5 | — | — | none |
| tdd-026 | L29-L30 | Do not manufacture a failing test or claim a red/green cycle. | rule | P5 | — | — | none |
| tdd-027 | L31-L32 | If the selected sequence is infeasible, obtain a revised policy before substituting another approach. | rule | P6 | — | — | none |
| tdd-028 | L32 | Do not silently change agreed TDD to fit an approach. | rule | P6 | — | — | none |
| tdd-029 | L34 | Implementation owns decomposition and evidence; | definition | — | — | — | none |
| tdd-030 | L34 | refactoring owns behavior-preserving checks. | definition | — | — | — | none |
| tdd-031 | L35 | Reuse valid checks when inputs are unchanged; | rule | P2 | V8: same policy stated in duplicate group D44 | — | none |
| tdd-032 | L35-L36 | broaden or repeat them only for changed inputs, failures, or concrete unresolved risks. | rule | P2, P5 | V8: same policy stated in duplicate group D44 | — | none |

## visuals (`plugins/lusona/references/visuals.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| visuals-001 | L3-L5 | Read for design, and for explore, specify, and architect when a choice is easier to judge visually or a diagram clarifies the decision, and for implement and review when the owning record links a visual reference. | rule | — | — | — | none |
| visuals-002 | L5 | Paths under `docs/lusona/` are in the consuming project. | definition | — | V8: same policy stated in duplicate group D10 | K2 | none |
| visuals-003 | L9-L10 | Offer 2-4 visual options when a concept, architecture, or UI choice is better judged by seeing it than by reading a description. | rule | — | V5: "better judged by seeing" is not a checkable condition | — | none |
| visuals-004 | L10-L11 | Do not offer options during implement when the agreement already settles the choice. | rule | P6 | — | — | none |
| visuals-005 | L12 | Include a diagram when it clarifies the decision. | rule | — | — | — | none |
| visuals-006 | L16 | Read the existing UI first. | rule | — | — | — | none |
| visuals-007 | L16 | Reuse its screen names, navigation, tab bars, and copy; | rule | — | — | — | none |
| visuals-008 | L16-L17 | label placeholders for content that does not exist yet. | rule | — | — | — | none |
| visuals-009 | L18-L19 | Style option content for the target platform or the project's theme in the page's `option-style` block. | rule | — | — | — | none |
| visuals-010 | L19-L20 | Show mobile UI in a plain, content-sized panel without phone bezels, hardware cutouts, or simulated system bars. | rule | — | — | — | none |
| visuals-011 | L20 | Use the wireframe kit when no platform look is known. | rule | — | — | — | none |
| visuals-012 | L21 | Scale fidelity to the question: wireframe for structure, closer styling for look and feel. | rule | — | — | — | none |
| visuals-013 | L22 | Use real content when it affects the judgment. | rule | — | — | — | none |
| visuals-014 | L23 | An option may be a flow of 2-5 screens; | definition | — | — | — | none |
| visuals-015 | L23 | number steps only for a sequence. | rule | — | — | — | none |
| visuals-016 | L24-L25 | Show states relevant to the choice, including failure when it affects the decision, using the state switch or separate screens. | rule | — | — | — | none |
| visuals-017 | L26-L27 | When options differ in one part of a flow, write one flow page with the in-place option switch, a one-line tradeoff per option, and the recommended option marked. | rule | — | V8: same policy stated in duplicate group D82 | — | none |
| visuals-018 | L28 | Explain the question on the page. | rule | — | — | — | none |
| visuals-019 | L28-L29 | In the notes, state what is approximate, such as system components drawn by hand, and list open questions and must-not-happen rules. | rule | P5 | — | — | none |
| visuals-020 | L33 | Present diagrams in fenced `mermaid` code blocks in the reply or a Markdown file. | rule | — | — | — | none |
| visuals-021 | L33-L34 | Use Mermaid Markdown for diagram options too; | rule | — | — | — | none |
| visuals-022 | L34 | do not create diagram HTML or PNGs. | rule | — | — | — | none |
| visuals-023 | L35-L36 | Start UI option, index, and flow pages from the [visual page template](../templates/visual-page.html) and follow its top comment. | rule | — | — | — | none |
| visuals-024 | L36 | Copy the file; | rule | — | — | — | none |
| visuals-025 | L37 | read only its top comment and body markup, not the shell CSS. | rule | — | — | — | none |
| visuals-026 | L37 | Pages are self-contained. | definition | — | — | — | none |
| visuals-027 | L38-L39 | Write one HTML file per UI option (`a.html`, `b.html`, ...) and an `index.html` that shows them side by side. | rule | — | — | — | none |
| visuals-028 | L39 | Use one in-place switch page instead only when options differ in one part of a flow. | rule | — | V8: same policy stated in duplicate group D82 | — | none |
| visuals-029 | L40 | Open the UI index or switch page in the browser for direct inspection; | rule | — | — | — | none |
| visuals-030 | L40-L41 | if the host cannot open it, report its absolute path. | rule | P5 | — | — | none |
| visuals-031 | L41 | Capture the chosen UI design only after the user agrees to it; | rule | P6 | — | — | none |
| visuals-032 | L42 | present drafts in the browser without capturing them. | rule | — | — | — | none |
| visuals-033 | L43-L44 | Write drafts outside tracked records: in a host-provided session scratch directory or the project's ignored temporary directory. | rule | — | — | — | none |
| visuals-034 | L48 | Label options A, B, C, D. | rule | — | — | — | none |
| visuals-035 | L48-L50 | Ask the user to choose by letter through the native question tool under [Questions and next actions](../README.md#questions-and-next-actions), otherwise in plain text. | rule | — | V8: same policy stated in duplicate group D55 | — | none |
| visuals-036 | L50 | There is no click-capture server. | definition | — | — | — | none |
| visuals-037 | L50-L51 | If the user rejects all options or asks for revision, retain no rejected draft assets and offer revised options; | rule | P2 | — | — | none |
| visuals-038 | L51-L52 | save consequential rejection reasons or new constraints under [retention](retention.md). | rule | — | — | — | none |
| visuals-039 | L56-L57 | After the user chooses, retain the reference before recording the decision, within the [core recording authority and restrictions](../README.md#contract); | rule | — | — | — | none |
| visuals-040 | L57-L58 | when saving is prevented, report the reference in the response. | rule | P5 | V8: same policy stated in duplicate group D31 | — | none |
| visuals-041 | L59 | Records never link draft pages. | rule | — | — | — | none |
| visuals-042 | L61-L62 | Directory: `docs/lusona/visuals/<record-id>/`, where `<record-id>` is the owning spec or ADR basename, or the notes slug when no spec exists yet. | definition | — | — | K2 | none |
| visuals-043 | L63 | UI mockup: retain `option-<letter>.html` with only its status changed to `Chosen reference`. | rule | — | — | — | none |
| visuals-044 | L64 | From a switch page, also delete the other options' elements and the option switch. | rule | — | — | — | none |
| visuals-045 | L64-L66 | Capture `option-<letter>.png`, or `option-<letter>-<state>.png` per shown state, in the light theme with an available screenshot tool. | rule | — | — | — | none |
| visuals-046 | L66-L67 | Include every screen without clipping and inspect each image. | rule | P5 | — | — | none |
| visuals-047 | L67 | If capture is unavailable, retain the HTML and report the missing images. | rule | P5 | — | — | none |
| visuals-048 | L68 | Diagram: retain `option-<letter>.md` containing fenced `mermaid` source, without HTML or PNGs. | rule | — | — | — | none |
| visuals-049 | L69-L71 | `reference.md` from the [visual reference template](../templates/visual-reference.md): chosen option, chooser and date, source, UI images when applicable, owner link, binding items, illustrative items, fidelity, and one line per rejected option with the reason. | rule | — | — | — | none |
| visuals-050 | L72-L73 | Binding items (V1, V2, ...) default to layout regions, element order, which controls exist, and information hierarchy, and may name a screen and state. | definition | — | — | — | none |
| visuals-051 | L73-L74 | Illustrative items default to colors, copy, and spacing unless the user marks them binding. | definition | P6 | — | — | none |
| visuals-052 | L75 | Do not retain the index or rejected option files. | rule | — | — | — | none |
| visuals-053 | L76 | Link `reference.md` from the owning spec, ADR, or notes. | rule | — | — | — | none |
| visuals-054 | L76-L77 | When page notes and `reference.md` disagree, `reference.md` governs. | definition | — | — | — | none |
| visuals-055 | L79 | A user-supplied reference keeps its existing capture in specify. | definition | — | — | — | none |
| visuals-056 | L79-L80 | Retain it this way only when the user asks. | rule | P6 | — | — | none |
| visuals-057 | L84-L85 | Implement and review read `reference.md` and its source: Mermaid Markdown for diagrams; HTML and available retained PNGs for UI mockups. | rule | — | V1: third-person skill statement | — | none |
| visuals-058 | L85 | Binding items are acceptance input; | definition | — | — | — | none |
| visuals-059 | L86 | illustrative items are not. | definition | — | — | — | none |
| visuals-060 | L86 | Implement reports each binding item's status. | rule | P5 | V1: third-person skill statement | — | none |
| visuals-061 | L87 | Review checks each binding item against the result and reports it as met, unmet, or unchecked; | rule | P5 | V1: third-person skill statement | — | none |
| visuals-062 | L88 | a partly met item is unmet, with what differs. | definition | P5 | — | — | none |
| visuals-063 | L88 | Check diagrams against their Mermaid source. | rule | P5 | — | — | none |
| visuals-064 | L89-L90 | For UI mockups with retained PNGs, compare a screenshot of the result when rendering and capture tools are available. | rule | P5 | — | — | none |
| visuals-065 | L90-L91 | Otherwise check code or markup, report the visual comparison as unrun, and identify what remains unverified. | rule | P5 | — | — | none |
| visuals-066 | L92 | A record without a visual reference leaves implement and review unchanged. | definition | — | — | — | none |

## work-record (`plugins/lusona/references/work-record.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| work-record-001 | L3-L4 | Use [Bash](../scripts/work-record.sh) in a Bash environment, or [PowerShell](../scripts/work-record.ps1) in a native Windows PowerShell environment. | rule | — | — | K3 | none |
| work-record-002 | L5-L6 | Choose from the agent's available shell, not just the operating system: a Windows WSL session uses Bash. | rule | — | — | K3 | none |
| work-record-003 | L6-L7 | Resolve the helper from the loaded plugin, never from the consuming project's current directory. | rule | — | — | K3 | none |
| work-record-004 | L7-L8 | From a skill, the paths are `../../scripts/work-record.sh` and `../../scripts/work-record.ps1`. | definition | — | — | K3 | none |
| work-record-005 | L10 | Both helpers use the same commands, arguments, statuses, and exit codes. | definition | — | — | K3 | none |
| work-record-006 | L10-L11 | Use the command reference below; | rule | — | — | K3 | none |
| work-record-007 | L11 | Bash `help` prints a short reminder, while PowerShell `help` prints usage. | definition | — | — | K3 | none |
| work-record-008 | L12 | Pass absolute project paths in the executing shell's filesystem; | rule | — | — | K3 | none |
| work-record-009 | L13 | PowerShell returns native absolute paths. | definition | — | — | K3 | none |
| work-record-010 | L13 | History paths are project-relative and use `/`. | definition | — | — | K3 | none |
| work-record-011 | L14 | PowerShell emits UTF-8 output, including JSON paths; | definition | — | — | K3 | none |
| work-record-012 | L14 | subprocess callers should decode it as UTF-8. | rule | — | — | K3 | none |
| work-record-013 | L15 | Do not pass a Windows drive path to a WSL helper or reinterpret returned paths in another shell. | rule | — | — | K3 | none |
| work-record-014 | L17-L19 | ```bash bash /resolved/plugin/scripts/work-record.sh slug 'Add invitation expiry' ``` | example | — | — | K3 | none |
| work-record-015 | L21-L23 | ```powershell powershell.exe -NoProfile -File "C:\resolved\plugin\scripts\work-record.ps1" slug 'Add invitation expiry' ``` | example | — | — | K3 | none |
| work-record-016 | L25 | The PowerShell helper targets Windows PowerShell 5.1 and PowerShell 7; | definition | — | — | K3 | none |
| work-record-017 | L25-L26 | use `pwsh` in place of `powershell.exe` for PowerShell 7. | rule | — | — | K3 | none |
| work-record-018 | L26 | Follow the host's script execution policy; | rule | P6 | — | — | none |
| work-record-019 | L27 | do not change policy automatically when execution is blocked. | rule | P6 | — | — | none |
| work-record-020 | L27-L28 | Report the blocked command and required environment instead. | rule | P5 | — | — | none |
| work-record-021 | L28 | The helpers use bundled templates and do not require Python. | definition | — | — | K3 | none |
| work-record-022 | L30 | For record identity and creation responses, apply [naming](naming.md); | rule | — | — | — | none |
| work-record-023 | L30-L31 | for notes and history, apply [retention](retention.md) and [closeout](closeout.md). | rule | — | — | — | none |
| work-record-024 | L31-L32 | After initialization, fill the relevant template sections within the existing work authorization. | rule | P6 | — | — | none |
| work-record-025 | L36 | Pass a command followed by its arguments to the resolved helper. | rule | — | — | K3 | none |
| work-record-026 | L36-L37 | Quote titles and paths containing spaces. | rule | — | — | K3 | none |
| work-record-027 | L37 | `DATE` is `YYYY-MM-DD` and defaults to today in the local timezone. | definition | — | V8: same policy stated in duplicate group D79 | K3 | none |
| work-record-028 | L39 | \| Command \| Arguments \| Result \| | not a rule | — | — | K3 | none |
| work-record-029 | L41 | \| `slug` \| `TITLE` \| Print a lowercase ASCII change slug \| | catalog | — | — | K3 | none |
| work-record-030 | L42 | \| `history-path` \| `[DATE]` \| Print the project-relative weekly history path \| | catalog | — | — | K3 | none |
| work-record-031 | L43 | \| `init-history` \| `PROJECT_ROOT [DATE]` \| Create a weekly history file if absent \| | catalog | — | — | K3 | none |
| work-record-032 | L44 | \| `init-notes` \| `PROJECT_ROOT SLUG` \| Create an item's notes file if absent \| | catalog | — | — | K3 | none |
| work-record-033 | L45 | \| `init-change` \| `PROJECT_ROOT SLUG [DATE]` \| Create a new `YYYYMMDD-slug` spec \| | catalog | — | — | K3 | none |
| work-record-034 | L46 | \| `init-adr` \| `PROJECT_ROOT SLUG [DATE]` \| Create a new `YYYYMMDD-slug` ADR \| | catalog | — | — | K3 | none |
| work-record-035 | L47 | \| `next-adr` \| `PROJECT_ROOT` \| Legacy: print the next four-digit ADR number \| | catalog | — | — | K3 | none |
| work-record-036 | L48 | \| `next-change` \| `PROJECT_ROOT` \| Legacy: print the next change number, including plans \| | catalog | — | — | K3 | none |
| work-record-037 | L49 | \| `stamp-header` \| `FILE [DATE]` \| Initialize Created and update Updated \| | catalog | — | — | K3 | none |
| work-record-038 | L50 | \| `help` \| None \| Show help; `-h` and `--help` are aliases \| | catalog | — | — | K3 | none |
| work-record-039 | L52 | Weeks are month-local: 01 covers days 1–7, 02 covers 8–14, through 05 for 29–end. | definition | — | V8: same policy stated in duplicate group D17 | K3 | none |
| work-record-040 | L53-L54 | `init-history` and `init-notes` print the absolute path and preserve existing regular files. | definition | — | V8: same policy stated in duplicate group D13 | K3 | none |
| work-record-041 | L54 | Reuse an item's existing slug; | rule | — | V8: same policy stated in duplicate group D76 | — | none |
| work-record-042 | L54 | initialization never overwrites or merges records. | definition | — | V8: same policy stated in duplicate group D13 | K3 | none |
| work-record-043 | L56-L57 | `init-change` and `init-adr` print JSON with `status`, `path`, and `message` fields: `created` (exit 0), `conflict` (exit 3), or `error` (exit 1). | definition | — | V8: same policy stated in duplicate group D53 | K3 | none |
| work-record-044 | L57-L58 | They reject existing paths, including symlinks. | definition | — | V8: same policy stated in duplicate group D74 | K3 | none |
| work-record-045 | L58 | New specs and ADRs use the creation date and a functional slug; | definition | — | V8: same policy stated in duplicate group D50 | K2 | none |
| work-record-046 | L59 | no counter is shared. | definition | — | — | K3 | none |
| work-record-047 | L59 | Diagnostic wording is descriptive; | definition | — | — | K3 | none |
| work-record-048 | L59 | branch on status and exit code. | rule | — | — | K3 | none |
| work-record-049 | L61 | Legacy sequence commands are read-only, ignore dated records, and reserve nothing. | definition | — | V8: same policy stated in duplicate group D51 | K3 | none |
| work-record-050 | L62 | Legacy numbered filenames use `NNNN-lowercase-slug.md`; | definition | — | — | K3 | none |
| work-record-051 | L62 | `README.md` is ignored. | definition | — | — | K3 | none |
| work-record-052 | L63 | Change scans ignore legacy filenames unless they begin with a digit. | definition | — | — | K3 | none |
| work-record-053 | L63-L64 | Matching legacy spec/plan basenames share a number; | definition | — | — | K3 | none |
| work-record-054 | L64 | conflicting slugs are rejected. | definition | — | — | K3 | none |
| work-record-055 | L66-L67 | Header stamping requires exactly one `Created:` and `Updated:` field, each containing a valid date or `<YYYY-MM-DD>`. | definition | — | — | K3 | none |
| work-record-056 | L67 | Existing Created dates never change. | definition | — | V8: same policy stated in duplicate group D52 | K3 | none |

## worker-lifecycle (`plugins/lusona/references/worker-lifecycle.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| worker-lifecycle-001 | L3-L4 | Agents responsible for workers or their results read after each result and before closing or handing off that responsibility. | rule | — | V1: third-person role address; V4: "workers" used for Leaf or Coordinator; V8: same policy stated in duplicate group D23 | — | none |
| worker-lifecycle-002 | L4-L5 | This includes inherited, reassigned, or earlier-session workers even when no new worker is dispatched. | definition | — | V4: "workers" used for Leaf or Coordinator | — | none |
| worker-lifecycle-003 | L5 | Leaves apply this procedure only for granted worker responsibilities. | rule | — | V1: third-person role address; V4: "worker" used for Leaf or Coordinator; V8: same policy stated in duplicate group D24 | — | none |
| worker-lifecycle-004 | L7-L8 | The responsible agent owns lifecycle decisions for those workers, including coordinating any granted children. | definition | — | V4: "workers" used for Leaf or Coordinator | — | none |
| worker-lifecycle-005 | L8 | After each result: | not a rule | — | — | — | none |
| worker-lifecycle-006 | L10-L11 | Preserve the result and recovery evidence, inspect it against the assignment, and decide acceptance separately from the worker's status. | rule | P5 | V4: "worker" used for Leaf or Coordinator; V8: same policy stated in duplicate group D75 | — | none |
| worker-lifecycle-007 | L11-L12 | Missing checks or material contradictions require follow-up; | rule | P5 | — | — | none |
| worker-lifecycle-008 | L12 | a status label alone is insufficient evidence. | rule | P5 | — | — | none |
| worker-lifecycle-009 | L13-L14 | Either assign concrete authorized follow-up work with explicit ownership, or release the worker through the host's supported shutdown/close mechanism. | rule | P7 | V4: "worker" used for Leaf or Coordinator | — | none |
| worker-lifecycle-010 | L14-L15 | Do not leave a persistent teammate idle merely in case more work appears. | rule | — | V4: "teammate" used for Leaf or Coordinator | — | none |
| worker-lifecycle-011 | L15 | Reuse must preserve required reviewer independence. | rule | P5 | — | — | none |
| worker-lifecycle-012 | L16 | Confirm termination or closure through host evidence. | rule | P5 | — | — | none |
| worker-lifecycle-013 | L16-L17 | An idle notification, final report, or sent shutdown request does not prove shutdown. | rule | P5 | V8: same policy stated in duplicate group D60 | — | none |
| worker-lifecycle-014 | L17-L18 | Track pending or rejected shutdown and resolve the stated reason; | rule | — | — | — | none |
| worker-lifecycle-015 | L18 | do not report capacity released before the host confirms it. | rule | P5 | — | — | none |
| worker-lifecycle-016 | L20 | Inspect the actual agent type and available controls. | rule | — | — | — | none |
| worker-lifecycle-017 | L20-L21 | For Claude Code teammates, request shutdown and wait for acknowledgment or host-confirmed termination. | rule | — | V4: "teammates" used for Leaf or Coordinator | — | none |
| worker-lifecycle-018 | L21-L22 | Ordinary subagents may end automatically; | definition | — | V4: "subagents" used for Leaf or Coordinator | — | none |
| worker-lifecycle-019 | L22 | observe the host result instead of inventing a team cleanup operation. | rule | P5 | — | — | none |
| worker-lifecycle-020 | L23 | For other hosts, use the exposed lifecycle controls. | rule | — | — | — | none |
| worker-lifecycle-021 | L23-L24 | If shutdown or confirmation is unavailable, report the limitation and surviving worker identity; | rule | P5 | V4: "worker" used for Leaf or Coordinator | — | none |
| worker-lifecycle-022 | L24-L25 | do not claim cleanup or delete transcripts, workspaces, or team directories as a substitute. | rule | P5 | — | — | none |
| worker-lifecycle-023 | L25 | Apply the host's actual capacity accounting. | rule | — | V8: same policy stated in duplicate group D65 | — | none |
| worker-lifecycle-024 | L27-L28 | At batch completion, deferral, interruption, or handoff, reconcile every worker within that responsibility and granted child. | rule | — | V4: "worker" used for Leaf or Coordinator | — | none |
| worker-lifecycle-025 | L28 | Preserve unfinished work before shutdown, | rule | — | V8: same policy stated in duplicate group D61 | — | none |
| worker-lifecycle-026 | L28-L29 | and record surviving workers, ownership, and pending lifecycle actions in the existing handoff when one is needed. | rule | — | V4: "workers" used for Leaf or Coordinator | — | none |
| worker-lifecycle-027 | L30 | Assignment completion, write-ownership release, and host-capacity release are separate facts. | definition | — | — | — | none |

## workflow-guide (`plugins/lusona/references/workflow-guide.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| workflow-guide-001 | L3 | Read the relevant section for skill selection, invocation, or terminology; | rule | P1 | — | — | none |
| workflow-guide-002 | L3 | this catalog and the routing table are not required for every assignment. | definition | P1 | V8: same policy stated in duplicate group D48 | — | none |
| workflow-guide-003 | L7 | \| Skill \| Persona and responsibility \| Output \| | not a rule | — | — | — | none |
| workflow-guide-004 | L9 | \| [explore](../skills/explore/SKILL.md) \| Discussion partner: selective questions, domain context, scenarios and tradeoffs \| [Discussion synthesis](../templates/brainstorm.md) in the owning record or notes for substantive outcomes \| | catalog | — | — | K1 | none |
| workflow-guide-005 | L10 | \| [status](../skills/status/SKILL.md) \| Workflow guide: current evidence, dependencies, next action, total known remainder \| Read-only [status assessment](../templates/status.md) \| | catalog | — | — | K1 | none |
| workflow-guide-006 | L11 | \| [batch](../skills/batch/SKILL.md) \| Batch coordinator: authorized selected outcomes, dependencies, and ownership \| Parent-owned [batch record](../templates/batch.md), linking owning evidence \| | catalog | — | — | K1 | none |
| workflow-guide-007 | L12 | \| [frame-product](../skills/frame-product/SKILL.md) \| Product strategist: long-term vision, users, problem, outcomes, boundaries \| [Product brief](../templates/product.md) \| | catalog | — | — | K1 | none |
| workflow-guide-008 | L13 | \| [map-capabilities](../skills/map-capabilities/SKILL.md) \| Product planner: long-term capability coverage, dependencies, useful delivery sequence \| Capability map in the [product template](../templates/product.md) \| | catalog | — | — | K1 | none |
| workflow-guide-009 | L14 | \| [specify](../skills/specify/SKILL.md) \| Change analyst: one change's observable behavior and acceptance \| [Change agreement and TDD policy](../templates/spec.md) \| | catalog | — | — | K1 | none |
| workflow-guide-010 | L15 | \| [design](../skills/design/SKILL.md) \| Visual designer: UI mockups, screen flows, and diagrams using existing context and references \| Inspectable drafts and chosen [visual references](../templates/visual-reference.md), linked from the owning record or notes \| | catalog | — | — | K1 | none |
| workflow-guide-011 | L16 | \| [architect](../skills/architect/SKILL.md) \| Architect: responsibilities, interfaces, data ownership, tradeoffs \| Shared or change-specific [ADRs](../templates/adr.md) \| | catalog | — | — | K1 | none |
| workflow-guide-012 | L17 | \| [implement](../skills/implement/SKILL.md) \| Engineer: planning, implementation, explicit TDD, and assigned verification \| Code and evidence in the owning record or [notes](../templates/notes.md) \| | catalog | — | — | K1 | none |
| workflow-guide-013 | L18 | \| [review](../skills/review/SKILL.md) \| Reviewer: defects and verification gaps in the actual diff \| [Review findings](../templates/review.md), without silent fixes \| | catalog | — | — | K1 | none |
| workflow-guide-014 | L19 | \| [refactor](../skills/refactor/SKILL.md) \| Maintainer: concrete structural improvement preserving behavior \| Code and regression evidence in the owning record or [notes](../templates/notes.md) \| | catalog | — | — | K1 | none |
| workflow-guide-015 | L20 | \| [investigate](../skills/investigate/SKILL.md) \| Investigator: bounded technical uncertainty \| [Investigation findings](../templates/notes.md) in the owning record or notes \| | catalog | — | — | K1 | none |
| workflow-guide-016 | L21 | \| [measure](../skills/measure/SKILL.md) \| Measurement analyst: decision-relevant magnitude, quality, cost, or change \| [Measurement evidence](../templates/evidence.md) with method and limitations \| | catalog | — | — | K1 | none |
| workflow-guide-017 | L22 | \| [experiment](../skills/experiment/SKILL.md) \| Experimenter: evaluate an intervention or alternatives \| [Experiment evidence](../templates/evidence.md) with design and exact runs \| | catalog | — | — | K1 | none |
| workflow-guide-018 | L26 | Consult this table when skill selection is unclear. | rule | P1 | V8: same policy stated in duplicate group D48 | — | none |
| workflow-guide-019 | L26-L27 | It maps an observed need to a skill or a direct action; | definition | P1 | — | — | none |
| workflow-guide-020 | L27 | it is a distinction of responsibilities, not a required sequence. | definition | P1 | V8: same policy stated in duplicate group D45 | — | none |
| workflow-guide-021 | L27-L28 | Routine design choices stay with implementation or refactoring. | definition | — | — | — | none |
| workflow-guide-022 | L28-L29 | Measurements and experiments within existing authorized work need no new command and enter under the [study entry rules](evidence.md#study-entry). | definition | P7 | — | — | none |
| workflow-guide-023 | L31 | \| Evidence or gap \| Action \| Inputs \| | not a rule | — | — | — | none |
| workflow-guide-024 | L33 | \| Start or resume unattended selected work \| [batch](../skills/batch/SKILL.md) \| Exact selection or batch record, and execution authority \| | catalog | P1 | — | — | none |
| workflow-guide-025 | L34 | \| Explore possibilities or tradeoffs \| [explore](../skills/explore/SKILL.md) \| The idea or decision \| | catalog | P1 | — | — | none |
| workflow-guide-026 | L35 | \| Product audience, outcome, or boundaries unclear \| [frame-product](../skills/frame-product/SKILL.md) \| The missing decision \| | catalog | P1 | — | — | none |
| workflow-guide-027 | L36 | \| Capabilities or delivery order unclear \| [map-capabilities](../skills/map-capabilities/SKILL.md) \| Product context \| | catalog | P1 | — | — | none |
| workflow-guide-028 | L37 | \| Change behavior or acceptance criteria unclear \| [specify](../skills/specify/SKILL.md) \| The selected outcome \| | catalog | P1 | — | — | none |
| workflow-guide-029 | L38 | \| UI mockup, screen flow, or diagram needed \| [design](../skills/design/SKILL.md) \| Existing UI, references, and the visual question \| | catalog | P1 | — | — | none |
| workflow-guide-030 | L39 | \| Consequential technical design, contract, or ownership decision unresolved \| [architect](../skills/architect/SKILL.md) \| That decision and accepted constraints \| | catalog | P1 | — | — | none |
| workflow-guide-031 | L40 | \| Cause or technical feasibility unknown \| [investigate](../skills/investigate/SKILL.md) \| One bounded question \| | catalog | P1 | — | — | none |
| workflow-guide-032 | L41 | \| Magnitude, quality, cost, or change to establish \| [measure](../skills/measure/SKILL.md) \| The decision the result informs and a reference \| | catalog | P1 | — | — | none |
| workflow-guide-033 | L42 | \| Proposed intervention or alternatives to test \| [experiment](../skills/experiment/SKILL.md) \| Declared criteria, budget, and stopping condition \| | catalog | P1 | — | — | none |
| workflow-guide-034 | L43 | \| Defined work needs decomposition or execution, or changed behavior or defect correction \| [implement](../skills/implement/SKILL.md) \| The selected outcome, explicit TDD, and authorization; a planning-only request stops before implementation \| | catalog | P1, P6 | V8: same policy stated in duplicate group D56 | — | none |
| workflow-guide-035 | L44 | \| Implementation needs review or verification \| [review](../skills/review/SKILL.md) when warranted, or name the missing check \| The actual diff, intended behavior, and evidence \| | catalog | P1 | V5: "when warranted" is not a checkable condition | — | none |
| workflow-guide-036 | L45 | \| Authorized structural improvement preserving observable behavior \| [refactor](../skills/refactor/SKILL.md) \| The behavior and interfaces to preserve \| | catalog | P1 | — | — | none |
| workflow-guide-037 | L46 | \| Required acceptance or delivery remains \| Name the exact action and owner \| The recorded completion condition \| | catalog | P1, P8 | — | — | none |
| workflow-guide-038 | L47 | \| Requested scope complete \| State completion; recommend a supported useful follow-up, or explicitly state none and why \| Established goals and observed findings; follow-up authority remains separate \| | catalog | P1, P8 | — | — | none |
| workflow-guide-039 | L49-L50 | Use the linked template for each skill's substantive output, applying relevant sections in conversation or in the existing owning document. | rule | — | — | — | none |
| workflow-guide-040 | L50-L51 | Format under the [shared presentation rules](../README.md#review-and-communication) and save under [retention](retention.md). | rule | — | — | — | none |
| workflow-guide-041 | L51 | Preserve project-local conventions. | rule | — | — | — | none |
| workflow-guide-042 | L53 | See [installation and compatibility](https://github.com/lusona/ai-skills/blob/main/INSTALL.md). | not a rule | — | — | — | none |
| workflow-guide-043 | L53-L54 | In Claude Code, invoke `/lusona:<skill>`; | rule | — | V8: same policy stated in duplicate group D81 | K1 | none |
| workflow-guide-044 | L54 | in other harnesses, use their exposed skill UI. | rule | — | — | — | none |
| workflow-guide-045 | L54-L55 | A useful prompt names the skill, selected outcome or input document, and authorized scope. | definition | — | — | — | none |
| workflow-guide-046 | L59 | \| Term \| Meaning \| | not a rule | — | — | — | none |
| workflow-guide-047 | L61 | \| Product \| The overall system and its intended outcomes \| | definition | — | — | — | none |
| workflow-guide-048 | L62 | \| Capability \| Something the product enables users to do \| | definition | — | — | — | none |
| workflow-guide-049 | L63 | \| Change \| A bounded feature, bug fix, refactor, or other deliverable \| | definition | — | V8: same policy stated in duplicate group D47 | — | none |
| workflow-guide-050 | L64 | \| Task \| A verifiable implementation step within a change \| | definition | — | V8: same policy stated in duplicate group D47 | — | none |
| workflow-guide-051 | L65 | \| Assignment \| Bounded work delegated to a subagent \| | definition | — | V4: "subagent" used for Leaf or Coordinator | — | none |
| workflow-guide-052 | L66 | \| Coordinator \| The parent agent responsible for delegation, integration, and verification \| | definition | — | — | — | none |
| workflow-guide-053 | L67 | \| Leaf \| An agent executing one assignment; also called worker or delegate \| | definition | — | V4: names two synonyms (worker, delegate) for Leaf | — | none |
| workflow-guide-054 | L69 | A change can contain one task. | definition | — | — | — | none |
| workflow-guide-055 | L69 | Use only the skills needed for its unresolved work; | rule | P1 | — | — | none |
| workflow-guide-056 | L70 | definition, planning, implementation, and review are responsibilities, not mandatory phases. | definition | P1 | V8: same policy stated in duplicate group D45 | — | none |
| workflow-guide-057 | L71 | Selecting one task for implementation does not authorize the rest of its change. | rule | P6 | V8: same policy stated in duplicate group D46 | — | none |

## execution (`plugins/lusona/skills/batch/references/execution.md`)

| ID | Lines | Rule | Kind | Principles | Conflicts | Contract | 20261110 row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| execution-001 | L3 | Use with [batch](../SKILL.md) and the [batch record](../../../templates/batch.md). | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-002 | L4 | The record owns coordination facts and evidence pointers, not a duplicate queue or task log. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-003 | L5-L6 | Keep requirements, implementation, review, and check evidence in each change record, linked ADRs, or existing separate execution records. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-004 | L6-L7 | Replace superseded transient state while retaining facts needed to recover ownership, authority, transfers, and consumed rounds. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-005 | L11-L12 | Before production edits, inspect actual repository and host capabilities and choose separate item workspaces, using worktrees or isolated copies as appropriate. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-006 | L12-L13 | Document-only assignments may share the project tree with disjoint ownership and helper-created date-prefixed records. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-007 | L13-L14 | Tasks within an item may share its workspace only with compatible behavior, disjoint writes, and safe check resources. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-008 | L16-L17 | Identify the required starting content: revision when present, staged and unstaged changes, untracked files, deletions, and binary content. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-009 | L17-L18 | Retain a content-identifiable baseline and distinguish user-owned starting content from batch-owned edits. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-010 | L18 | A clean checkout of HEAD alone may omit required inputs. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-011 | L19-L20 | Record workspace paths, ownership, baseline identity, dependencies, and the means of reconstructing the item delta. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-012 | L20-L21 | Check content identity using available repository tools or retained manifests/snapshots, including paths, bytes and relevant modes; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-013 | L21 | a branch name or plain status listing is insufficient. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-014 | L22 | Keep scratch material in the location permitted by project instructions. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-015 | L24 | Do not move, stash, overwrite, clean, or commit unrelated changes to obtain a baseline. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-016 | L24-L25 | Commit only when project authorization permits it. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-017 | L25-L26 | No-commit work retains uncommitted edits and transfers the attributable item delta relative to its baseline, including binaries and deletions. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-018 | L26-L27 | Never substitute a whole workspace copy that would overwrite destination changes. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-019 | L27-L28 | If required inputs or ownership cannot be established, defer affected work. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-020 | L28-L29 | Without isolation, proceed sequentially only where unfinished edits can remain safely separated; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-021 | L29 | otherwise stop the batch. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-022 | L31-L32 | Persist each assignment's dispatch intent, owner, responsibility, scope, dependencies, baseline, slot grant, and any charged round before starting it. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-023 | L32-L33 | Record the returned status and owning evidence references before releasing its write scope. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-024 | L33 | Stop old writers before reassignment, deferral, or integration; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-025 | L34 | a message requesting a stop is not proof of cessation. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-026 | L34-L35 | Only the parent grants nested assignments from the global pool. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-027 | L35 | No surviving worker may retain an unrecorded claim on a scope. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-028 | L36-L37 | Apply the shared [worker lifecycle](../../../references/worker-lifecycle.md) after each result and before batch closeout or handoff. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-029 | L37-L38 | Record result status, coordinator acceptance, and host lifecycle evidence separately; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-030 | L38-L39 | idle teammates still require a reuse or shutdown decision. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-031 | L39 | Reconcile granted children as well as direct workers. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-032 | L43-L44 | Include reporting timing in each assignment: return the shared assignment result to the parent as soon as the bounded assignment completes, blocks, or ends incomplete, before waiting or ending. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-033 | L45 | Use the host's completion notification or message mechanism; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-034 | L45-L46 | workers do not wait for sibling assignments or batch consolidation and do not edit the shared queue or batch handoff. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-035 | L48-L49 | The coordinator handles available results individually as they arrive, rather than waiting for all dispatched workers. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-036 | L49-L52 | Before further dispatch or waiting, and after any in-progress serialized operation reaches a safe boundary, inspect the result and its evidence, persist the assignment outcome and recovery references, and, when the item's state, blocker, or next action changed, update its row in `docs/lusona/work.md`. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-037 | L52 | Do not rewrite an unchanged row. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-038 | L52-L53 | Keep the row concise: truthful lifecycle state, current blocker or next action, and owning evidence link. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-039 | L54 | If evidence is missing, record the pending verification or missing report as the next action; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-040 | L55 | do not infer success from a completion notification. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-041 | L55-L56 | Refresh the current batch handoff's affected pointers so it remains resumable, without copying task evidence or adding an activity log. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-042 | L58 | A worker's `complete` describes its assignment, not the whole queue outcome. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-043 | L58-L59 | Keep remaining implementation, integration, checks, review, acceptance, or delivery visible in the row. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-044 | L59-L60 | Apply the normal state criteria and completion gates; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-045 | L60-L61 | close and archive an outcome once those gates pass, even while unrelated batch items continue. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-046 | L61-L62 | Reporting a result does not itself integrate changes or release write ownership or host capacity. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-047 | L62-L63 | Apply the existing integration and worker lifecycle procedures separately. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-048 | L63-L64 | On hosts without asynchronous notifications, collect available results at bounded assignment boundaries; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-049 | L64 | do not promise immediate background updates. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-050 | L68-L69 | When integration uses Git branches, apply the shared [linear integration procedure](../../../references/commits.md#linear-integration). | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-051 | L70-L71 | Rebasing changes identities: reconcile recorded baselines, candidate content, and affected verification/review evidence before resuming the steps below. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-052 | L73-L74 | Stop relevant writers and identify the source baseline, exact item delta, current destination baseline, and required dependencies. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-053 | L74 | Check destination drift and attribution before applying. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-054 | L75-L76 | Record integration intent, candidate location, expected content identities, and recovery method before mutation. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-055 | L76 | Preserve the source until acceptance and evidence recording are confirmed. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-056 | L77 | Materialize one attributable candidate at a time. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-057 | L77-L78 | Prefer holding a candidate outside the accepted destination until checks pass where supported. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-058 | L78-L79 | Record the phase as `candidate materialized` with its actual identity, including uncommitted content. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-059 | L79 | Keep intent and actual result distinguishable. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-060 | L80 | Run required verification and fresh independent review on the resulting candidate. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-061 | L80-L82 | Give reviewers the actual diff, governing definition/architecture, and check evidence without implementer conclusions. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-062 | L82-L83 | Record evidence in its owning document and link its candidate identity from the integration record; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-063 | L83 | then record `evidence collected`. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-064 | L83 | Unrun checks and unavailable review block Done. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-065 | L84-L86 | For an external candidate, record `promotion intent` with the accepted destination's pre-transfer identity, expected post-transfer identity matching the reviewed candidate, attributable delta, and recovery inputs. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-066 | L86 | Keep relevant writers stopped; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-067 | L86-L87 | immediately recheck destination drift before transferring that delta. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-068 | L87 | On drift, reconcile the candidate and affected evidence before proceeding. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-069 | L88-L89 | After transfer, record `promotion materialized` and compare the actual destination content identity with the reviewed candidate. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-070 | L89 | External candidate materialization alone is never destination promotion. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-071 | L90-L91 | Before recording `accepted`, require the actual destination to match the reviewed candidate and required evidence to cover final relevant content. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-072 | L91-L92 | For a candidate already materialized directly in the destination, compare that destination identity without a second transfer. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-073 | L92-L94 | A later integration requires assessing affected prior behavior: rerun affected checks and obtain review where reviewed behavior changed. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-074 | L94 | Do not repeat unrelated unchanged reviews. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-075 | L94 | Drift invalidates affected evidence; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-076 | L95 | reconcile it before acceptance. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-077 | L96 | For failure, retain candidate and evidence and use the item's repair budget. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-078 | L96-L98 | Hold the failed candidate outside the accepted destination, or restore only its attributable changes after proving that no other writer's changes will be lost. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-079 | L98-L99 | Record `deferred` when deferring and identify the accepted destination content. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-080 | L99 | If safe restoration cannot be established, stop the batch. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-081 | L99-L100 | Retain prior completion evidence when a later regression occurs; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-082 | L100-L101 | charge corrective attempts to the introducing item. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-083 | L101-L102 | If cause/ownership is uncertain, investigate within an identified responsible item's budget or defer affected work. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-084 | L104 | An intent is not evidence of transfer, and missing result metadata is not permission to apply again. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-085 | L105 | Recover candidate materialization and destination promotion separately. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-086 | L105-L106 | Compare each operation's actual target with its recorded pre-transfer and expected post-transfer identities. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-087 | L106-L107 | A retained external candidate proves nothing about promotion. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-088 | L107-L108 | If the destination matches the promotion's expected result, recover that phase and validate evidence without retransferring; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-089 | L108-L109 | if it still matches the pre-transfer identity, promote only after reconfirming ownership, candidate evidence, and drift. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-090 | L109-L110 | If content matches neither expected state, reconcile drift before transfer or restoration; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-091 | L110 | stop if attribution remains unsafe. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-092 | L110-L111 | Never blindly replay a patch. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-093 | L115-L116 | The initial bounded attempt is followed by at most two corrective rounds per item unless the user supplies another allowance. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-094 | L116 | The counter spans all responsibilities and owners. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-095 | L116-L118 | A failed implementation outcome, required check, review, integration, or unresolved bounded investigation needing another approach starts a round. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-096 | L118-L119 | Before dispatch, persist its charge, triggering finding reference, declared bounded correction/experiment set, owners, and expected checks/review. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-097 | L119-L120 | Increasing the allowance requires explicit new authority; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-098 | L120 | changing delegates, responsibilities, or labels does not reset it. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-099 | L122 | One round covers that declared set and its checks/review; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-100 | L122-L123 | independent fixes within it may run concurrently under the same global cap. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-101 | L123-L124 | A failed round needing a different correction/experiment, including a new actionable failure found during verification, consumes the next round. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-102 | L124-L125 | Do not append unbounded fixes to an open round. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-103 | L125-L126 | Diagnostic investigation of its declared failure belongs to that round. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-104 | L126 | Ordinary task-local TDD red/green steps are not failed batch attempts; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-105 | L126-L127 | an unsuccessful task outcome requiring a new approach is. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-106 | L129 | Initial investigation must have a bounded question, finite experiments, and a stopping condition. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-107 | L130 | If unresolved, another approach costs a round from the same item. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-108 | L130-L131 | Missing consequential decisions or authority cause immediate deferral, not speculative rounds. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-109 | L131 | Environment failures prevent completion; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-110 | L132 | a changed environment may justify a charged retry, never an unbounded loop. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-111 | L134-L135 | An interrupted round remains charged and resumes its declared correction set only where evidence supports safe continuation. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-112 | L135 | Cancel a reserved charge only with evidence that no work was dispatched; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-113 | L136 | retain that cancellation and evidence reference. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-114 | L136 | Uncertain progress remains charged. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-115 | L136-L137 | Exhaustion defers the item and unfinished dependents, retaining attempts, findings, and next action in owning records. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-116 | L138-L139 | On a requested suspension, stop dispatch, reconcile active writers, and checkpoint the reserved intent, charge, actual dispatch status, and retained candidate before handing off. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-117 | L139 | Suspension does not reset rounds. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-118 | L143-L145 | Before continuing past an unfinished item, stop/reconcile its writers, preserve source changes and baseline identities, reconcile candidate transfers, and record reason, dependent exclusions, repair consumption, and next action. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-119 | L145 | Release ownership only after safe isolation. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-120 | L145-L146 | Deferral is a scheduling flag, not Done and not a queue lifecycle reset. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-121 | L146-L147 | Unfinished content must not become an independent item's accidental input. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-122 | L147 | If isolation or restoration is unsafe, stop all affected continuation. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-123 | L149 | For an explicitly selected continuation: | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-124 | L151-L152 | Load fixed membership, authorization and constraints, TDD/completion references, dependency reconciliation, limits, assignments, open rounds, integration phases, and current handoff. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-125 | L153 | Recheck authority against current user instructions; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-126 | L153 | do not enlarge selection or reset budgets. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-127 | L154 | Inspect actual agents, workspace content, destination, and returned artifacts. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-128 | L154-L155 | Reattach to or stop surviving writers before redispatch. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-129 | L155 | Saved assignment state does not prove completion or cessation. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-130 | L156 | If the host cannot establish ownership safely, stop affected work and report the exact blocker. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-131 | L157 | Recover interrupted transfers as above. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-132 | L157 | Reuse completed checks and decisions only when their inputs match; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-133 | L158 | preserve valid evidence and link it. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-134 | L158-L159 | Refresh effective host capacity, retaining the requested cap and accounting for surviving workers and parent occupancy. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-135 | L159-L160 | Sequential fallback is allowed where safe but does not replace required independent review. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-136 | L161 | Update the one current handoff and dispatch the next eligible bounded assignment. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-137 | L161-L162 | Unresolved deferrals remain excluded until the recorded blocker is actually resolved within authority. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-138 | L164-L165 | At stop or completion, report completed history links, deferred/unfinished queue and evidence links, unresolved decisions, and concrete next actions. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-139 | L165-L166 | Distinguish completion of every selected outcome, selection exhausted with deferrals, interruption with resumable work, and inability to continue safely. | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-140 | L167 | Persist exact recovery inputs and ownership before handing off; | unreviewed | unreviewed | unreviewed | unreviewed | none |
| execution-141 | L167 | do not duplicate task evidence here. | unreviewed | unreviewed | unreviewed | unreviewed | none |

## Summary

### Rows per file and Kind

| File | rule | definition | example | catalog | not a rule | Total |
| --- | --- | --- | --- | --- | --- | --- |
| readme | 151 | 17 | 0 | 18 | 1 | 187 |
| batch-execution | 50 | 4 | 0 | 0 | 0 | 54 |
| batch-use | 9 | 10 | 3 | 0 | 2 | 24 |
| closeout | 17 | 9 | 1 | 0 | 0 | 27 |
| commits | 53 | 5 | 0 | 0 | 0 | 58 |
| corrections | 14 | 6 | 0 | 0 | 0 | 20 |
| delegation | 45 | 11 | 0 | 0 | 1 | 57 |
| evidence | 38 | 11 | 0 | 0 | 0 | 49 |
| files | 8 | 5 | 0 | 21 | 2 | 36 |
| handoff | 8 | 3 | 0 | 0 | 0 | 11 |
| interview-examples | 1 | 3 | 15 | 5 | 1 | 25 |
| interviews | 22 | 6 | 0 | 0 | 0 | 28 |
| model-routing | 20 | 8 | 0 | 3 | 1 | 32 |
| naming | 16 | 22 | 0 | 3 | 1 | 42 |
| queue | 38 | 19 | 0 | 5 | 1 | 63 |
| retention | 56 | 19 | 0 | 0 | 0 | 75 |
| tdd | 22 | 9 | 0 | 0 | 1 | 32 |
| visuals | 53 | 13 | 0 | 0 | 0 | 66 |
| work-record | 18 | 25 | 2 | 10 | 1 | 56 |
| worker-lifecycle | 22 | 4 | 0 | 0 | 1 | 27 |
| workflow-guide | 9 | 15 | 0 | 29 | 4 | 57 |
| Total | 670 | 224 | 21 | 94 | 17 | 1026 |

### Rows per principle

A row can implement more than one principle.

| Principle | Rows | Files |
| --- | --- | --- |
| P1 | 35 | readme, batch-execution, evidence, tdd, workflow-guide |
| P2 | 31 | readme, batch-execution, corrections, delegation, evidence, handoff, interview-examples, interviews, retention, tdd, visuals |
| P3 | 6 | readme, interviews, queue |
| P4 | 18 | readme, closeout, evidence, handoff, interview-examples, interviews, queue, retention |
| P5 | 135 | readme, batch-execution, closeout, commits, corrections, delegation, evidence, handoff, interviews, model-routing, naming, queue, retention, tdd, visuals, work-record, worker-lifecycle |
| P6 | 131 | readme, batch-execution, batch-use, closeout, commits, corrections, delegation, evidence, files, handoff, interview-examples, interviews, model-routing, naming, queue, retention, tdd, visuals, work-record, workflow-guide |
| P7 | 67 | readme, batch-execution, corrections, delegation, evidence, handoff, interview-examples, interviews, queue, retention, worker-lifecycle, workflow-guide |
| P8 | 18 | readme, retention, workflow-guide |

ID lists per principle:

- P1 (35): readme-019, readme-020, readme-021, readme-023, readme-069, readme-072, readme-186, batch-execution-007, batch-execution-008, batch-execution-009, batch-execution-040, evidence-005, tdd-007, workflow-guide-001, workflow-guide-002, workflow-guide-018, workflow-guide-019, workflow-guide-020, workflow-guide-024, workflow-guide-025, workflow-guide-026, workflow-guide-027, workflow-guide-028, workflow-guide-029, workflow-guide-030, workflow-guide-031, workflow-guide-032, workflow-guide-033, workflow-guide-034, workflow-guide-035, workflow-guide-036, workflow-guide-037, workflow-guide-038, workflow-guide-055, workflow-guide-056
- P2 (31): readme-022, readme-026, readme-028, readme-032, readme-033, readme-048, readme-056, batch-execution-007, corrections-005, delegation-031, delegation-035, delegation-042, delegation-043, delegation-057, evidence-020, handoff-004, interview-examples-012, interview-examples-013, interview-examples-024, interviews-002, interviews-015, interviews-018, interviews-020, interviews-021, retention-005, retention-022, retention-037, retention-054, tdd-031, tdd-032, visuals-037
- P3 (6): readme-041, readme-042, interviews-007, interviews-016, interviews-028, queue-013
- P4 (18): readme-043, readme-044, readme-045, readme-046, readme-047, closeout-011, closeout-012, evidence-027, evidence-028, evidence-030, evidence-048, handoff-005, interview-examples-025, interviews-019, queue-060, retention-054, retention-056, retention-057
- P5 (135): readme-010, readme-014, readme-025, readme-028, readme-053, readme-062, readme-086, readme-134, readme-135, readme-136, readme-137, readme-138, readme-139, readme-140, readme-141, readme-144, readme-149, readme-169, readme-178, readme-185, batch-execution-016, batch-execution-042, batch-execution-048, batch-execution-049, batch-execution-050, closeout-004, closeout-007, closeout-008, closeout-026, commits-001, commits-011, commits-013, commits-014, commits-015, commits-016, commits-019, commits-022, commits-027, commits-028, commits-032, commits-033, commits-040, commits-048, commits-049, commits-053, commits-057, corrections-007, corrections-008, corrections-009, delegation-015, delegation-019, delegation-024, delegation-029, delegation-034, delegation-037, delegation-038, delegation-039, delegation-043, delegation-044, delegation-045, delegation-046, delegation-047, delegation-048, evidence-001, evidence-007, evidence-008, evidence-009, evidence-010, evidence-024, evidence-025, evidence-026, evidence-028, evidence-029, evidence-030, evidence-031, evidence-032, evidence-033, evidence-037, evidence-038, evidence-039, evidence-042, evidence-049, handoff-006, handoff-009, interviews-008, interviews-010, interviews-020, interviews-024, model-routing-016, model-routing-020, model-routing-028, model-routing-031, naming-040, queue-042, queue-053, queue-054, queue-055, queue-056, queue-057, retention-034, retention-046, retention-047, retention-056, retention-073, tdd-005, tdd-015, tdd-016, tdd-017, tdd-018, tdd-023, tdd-025, tdd-026, tdd-032, visuals-019, visuals-030, visuals-040, visuals-046, visuals-047, visuals-060, visuals-061, visuals-062, visuals-063, visuals-064, visuals-065, work-record-020, worker-lifecycle-006, worker-lifecycle-007, worker-lifecycle-008, worker-lifecycle-011, worker-lifecycle-012, worker-lifecycle-013, worker-lifecycle-015, worker-lifecycle-019, worker-lifecycle-021, worker-lifecycle-022
- P6 (131): readme-015, readme-018, readme-023, readme-036, readme-042, readme-050, readme-051, readme-052, readme-054, readme-055, readme-064, readme-065, readme-066, readme-067, readme-068, readme-070, readme-071, readme-073, readme-074, readme-075, readme-085, readme-090, readme-116, readme-122, readme-125, readme-128, readme-129, readme-131, readme-132, readme-152, readme-164, readme-169, readme-170, readme-171, readme-177, batch-execution-002, batch-execution-003, batch-execution-004, batch-execution-006, batch-execution-010, batch-execution-011, batch-execution-012, batch-execution-017, batch-execution-021, batch-execution-024, batch-execution-026, batch-execution-027, batch-execution-028, batch-execution-031, batch-execution-032, batch-execution-036, batch-execution-037, batch-execution-053, batch-execution-054, batch-use-002, batch-use-003, batch-use-007, batch-use-023, batch-use-024, closeout-008, commits-001, commits-012, commits-014, commits-020, commits-021, commits-034, commits-041, commits-043, commits-044, commits-045, commits-046, commits-051, commits-052, corrections-013, corrections-018, corrections-019, delegation-008, delegation-009, delegation-010, delegation-011, delegation-012, delegation-013, delegation-031, delegation-052, evidence-002, evidence-003, evidence-010, evidence-013, files-032, files-034, handoff-008, handoff-011, interview-examples-005, interview-examples-019, interviews-004, interviews-005, interviews-009, interviews-026, model-routing-003, model-routing-017, model-routing-018, model-routing-031, naming-041, queue-004, queue-012, queue-015, queue-016, queue-035, queue-040, queue-045, queue-046, queue-047, queue-048, queue-058, queue-059, queue-062, retention-039, tdd-002, tdd-006, tdd-008, tdd-027, tdd-028, visuals-004, visuals-031, visuals-051, visuals-056, work-record-018, work-record-019, work-record-024, workflow-guide-034, workflow-guide-057
- P7 (67): readme-027, readme-029, readme-030, readme-031, readme-034, readme-035, readme-036, readme-037, readme-038, readme-054, readme-055, readme-068, readme-072, readme-082, readme-083, readme-084, readme-118, readme-119, readme-127, readme-142, readme-145, readme-146, readme-179, readme-184, batch-execution-015, batch-execution-020, batch-execution-022, batch-execution-023, batch-execution-025, batch-execution-038, batch-execution-041, batch-execution-043, batch-execution-044, batch-execution-047, batch-execution-048, corrections-011, corrections-012, corrections-013, corrections-014, corrections-018, delegation-007, delegation-025, delegation-039, delegation-051, delegation-053, evidence-003, evidence-011, evidence-047, handoff-007, handoff-008, handoff-010, handoff-011, interview-examples-016, interview-examples-021, interview-examples-022, interviews-006, interviews-023, interviews-025, interviews-028, queue-006, retention-004, retention-006, retention-007, retention-011, retention-062, worker-lifecycle-009, workflow-guide-022
- P8 (18): readme-117, readme-118, readme-120, readme-121, readme-144, readme-145, readme-149, readme-150, readme-151, readme-152, readme-153, readme-155, readme-165, retention-033, retention-036, retention-037, workflow-guide-037, workflow-guide-038

### Conflicts by P/V ID

Script findings come from the V3, V4, V5/V6 term and V8 group tests; hand findings from reading the row.

| ID | Rows | Findings (script) | Findings (hand) | Main reasons |
| --- | --- | --- | --- | --- |
| P2 | 1 | 0 | 1 | handoff fields omit uncertainty (1) |
| P3 | 4 | 0 | 4 | trigger limited to evidence, not requirement, spec or measurement (1); reopens within authority, omits revisiting the decision with user (1); reuse of existing vision states no handling of contradicting input (1) |
| P4 | 1 | 0 | 1 | keeps only useful rationale, no date and source marking (1) |
| P8 | 1 | 0 | 1 | None form omits the reason that readme-120 requires (1) |
| V1 | 37 | 0 | 37 | third-person role statement (17); third-person role address (8); third-person role address, not imperative (3) |
| V2 | 3 | 0 | 3 | "Coordinator catalog:" label restates section purpose (1); restates scope ("These exceptions apply") before the action (1); preamble describing the file (1) |
| V3 | 6 | 6 | 0 | source sentence has 45 words (2); source sentence has 75 words (2); source sentence has 47 words (1) |
| V4 | 55 | 54 | 1 | "worker" used for Leaf or Coordinator (12); "workers" used for Leaf or Coordinator (12); "the parent" used for Leaf or Coordinator (7) |
| V5 | 32 | 1 | 31 | "by default" leaves the exception unstated (2); "when needed" vague condition (2); "following role/section guidance" names no condition (1) |
| V6 | 4 | 0 | 4 | filler adjective "natural" (1); figurative statement that gives no action (1); attributes ownership of meaning to Lusona, gives no action (1) |
| V7 | 6 | 0 | 6 | "small clear work" has no measurable bound (1); "small change" has no measurable bound (1); "large raw outputs" has no size threshold (1) |
| V8 | 240 | 239 | 3 | same policy stated in duplicate group D30 (7); same policy stated in duplicate group D31 (7); same policy stated in duplicate group D10 (6) |
| V9 | 4 | 0 | 4 | explanatory clause "a fast-forward can import" in the instruction (1); describes the guidance's status instead of an action (1); explains an unrelated host feature (1) |

Principles with no conflict row were tested with the one-line tests in Conventions; zero means no row met the test.

- P2 (1):
  - handoff-004: handoff fields omit uncertainty
- P3 (4):
  - readme-041: trigger limited to evidence, not requirement, spec or measurement
  - readme-042: reopens within authority, omits revisiting the decision with user
  - interviews-016: reuse of existing vision states no handling of contradicting input
  - interviews-028: batches reuse settled intent with no revisit path
- P4 (1):
  - readme-044: keeps only useful rationale, no date and source marking
- P8 (1):
  - readme-155: None form omits the reason that readme-120 requires
- V1 (37):
  - readme-001: third-person role address, not imperative
  - readme-002: third-person role address, not imperative
  - readme-006: third-person role address, not imperative
  - readme-009: third-person statement of a coordinator duty
  - readme-080: third-person role statement, no trigger
  - readme-087: third-person role statement
  - readme-094: third-person role statement
  - readme-168: third-person role address
  - readme-183: third-person role statement
  - batch-execution-025: third-person role statement
  - batch-execution-030: third-person role statement
  - batch-execution-033: third-person role statement
  - batch-execution-038: third-person role statement
  - closeout-026: third-person role statement
  - commits-017: third-person role statement
  - commits-047: third-person role statement
  - delegation-001: third-person role address
  - delegation-002: third-person role address
  - delegation-004: third-person role address
  - delegation-005: third-person role address
  - delegation-013: third-person statement of coordinator duties inside a leaf section
  - delegation-037: third-person statement of a dispatch duty
  - interviews-002: third-person skill description, no imperative
  - interviews-003: third-person skill description, no imperative
  - interviews-005: third-person role statement
  - model-routing-001: third-person role address
  - queue-002: third-person role statement
  - queue-031: third-person role statement
  - queue-046: third-person role statement
  - queue-062: third-person role statement
  - queue-063: third-person role statement
  - retention-075: third-person role statement
  - visuals-057: third-person skill statement
  - visuals-060: third-person skill statement
  - visuals-061: third-person skill statement
  - worker-lifecycle-001: third-person role address
  - worker-lifecycle-003: third-person role address
- V2 (3):
  - readme-092: "Coordinator catalog:" label restates section purpose
  - batch-execution-002: restates scope ("These exceptions apply") before the action
  - interview-examples-001: preamble describing the file
- V3 (6 rows; 6 findings): corrections-013, corrections-014, evidence-024, retention-012, retention-013, retention-033
- V4 (55):
  - readme-002: "subagents" used for Leaf or Coordinator
  - readme-008: "children" used for Leaf or Coordinator
  - readme-014: "worker" used for Leaf or Coordinator
  - readme-038: "their parent" used for Leaf or Coordinator
  - readme-081: "the parent" used for Leaf or Coordinator
  - readme-087: "workers" used for Leaf or Coordinator
  - readme-109: "workers" used for Leaf or Coordinator
  - readme-170: "the parent" used for Leaf or Coordinator
  - readme-176: "worker" used for Leaf or Coordinator
  - readme-179: "workers" used for Leaf or Coordinator
  - readme-182: "workers" used for Leaf or Coordinator
  - batch-execution-001: "assigned delegate" used for Leaf or Coordinator
  - batch-execution-010: "parent coordinator" used for Leaf or Coordinator
  - batch-execution-017: "delegates return" used for Leaf or Coordinator
  - batch-execution-021: "the parent" used for Leaf or Coordinator
  - batch-execution-024: "Delegates do" used for Leaf or Coordinator
  - batch-execution-025: "parent reports" used for Leaf or Coordinator
  - batch-execution-029: "parent coordinator" used for Leaf or Coordinator
  - batch-execution-030: "the parent" used for Leaf or Coordinator
  - batch-execution-032: "a parent" used for Leaf or Coordinator
  - batch-execution-033: "parent alone" used for Leaf or Coordinator
  - batch-execution-036: "Review delegates" used for Leaf or Coordinator
  - batch-execution-037: "the parent" used for Leaf or Coordinator
  - batch-execution-039: "parent applies" used for Leaf or Coordinator
  - batch-execution-048: "parent proceeds" used for Leaf or Coordinator
  - batch-execution-053: "the parent" used for Leaf or Coordinator
  - batch-use-011: "parent occupancy" used for Leaf or Coordinator
  - batch-use-015: "parent owns" used for Leaf or Coordinator
  - commits-018: "subagents" used for Leaf or Coordinator
  - corrections-005: "workers" used for Leaf or Coordinator
  - corrections-009: "worker" used for Leaf or Coordinator
  - delegation-004: "workers" used for Leaf or Coordinator
  - delegation-010: "children" used for Leaf or Coordinator
  - delegation-021: "children" used for Leaf or Coordinator
  - delegation-038: "worker" used for Leaf or Coordinator
  - delegation-046: "workers" used for Leaf or Coordinator
  - model-routing-010: "worker" used for Leaf or Coordinator
  - model-routing-022: "worker" used for Leaf or Coordinator
  - model-routing-027: "the parent" used for Leaf or Coordinator
  - queue-030: "worker" used for Leaf or Coordinator
  - queue-043: "workers" used for Leaf or Coordinator
  - worker-lifecycle-001: "workers" used for Leaf or Coordinator
  - worker-lifecycle-002: "workers" used for Leaf or Coordinator
  - worker-lifecycle-003: "worker" used for Leaf or Coordinator
  - worker-lifecycle-004: "workers" used for Leaf or Coordinator
  - worker-lifecycle-006: "worker" used for Leaf or Coordinator
  - worker-lifecycle-009: "worker" used for Leaf or Coordinator
  - worker-lifecycle-010: "teammate" used for Leaf or Coordinator
  - worker-lifecycle-017: "teammates" used for Leaf or Coordinator
  - worker-lifecycle-018: "subagents" used for Leaf or Coordinator
  - worker-lifecycle-021: "worker" used for Leaf or Coordinator
  - worker-lifecycle-024: "worker" used for Leaf or Coordinator
  - worker-lifecycle-026: "workers" used for Leaf or Coordinator
  - workflow-guide-051: "subagent" used for Leaf or Coordinator
  - workflow-guide-053: names two synonyms (worker, delegate) for Leaf
- V5 (32):
  - readme-004: "following role/section guidance" names no condition
  - readme-051: "by default" leaves the exception unstated
  - readme-082: "proportionate to the work" sets no checkable condition
  - readme-083: "when it becomes useful" is not a checkable trigger
  - readme-126: "when useful" is not a checkable condition
  - readme-162: "useful" columns sets no condition
  - readme-184: "around 40%" is an approximate threshold
  - batch-execution-010: "conservative assumptions" sets no checkable condition
  - commits-004: "usable" names no check
  - commits-029: banned term "when needed"
  - commits-030: "otherwise needed" is not a checkable condition
  - commits-036: "optional useful scope" sets no condition
  - delegation-035: "Prefer" leaves the condition for full history unstated
  - delegation-055: "avoid" states no condition or check
  - evidence-004: "small self-contained" has no measurable bound
  - evidence-017: "as needed" vague condition
  - evidence-022: "when no further split is useful" names no check
  - evidence-024: "enough" sets no measurable bound
  - evidence-036: "where practical" hedge
  - model-routing-004: banned hedge "Consider"
  - model-routing-032: "useful parallel assignments" sets no condition
  - naming-007: "by default" leaves the exception unstated
  - naming-010: "when needed" vague condition
  - queue-005: "Prefer" leaves the exception unstated
  - retention-005: "meaningful change" sets no checkable condition
  - retention-006: "once the synthesis is useful" is not a checkable trigger
  - retention-051: "useful exploration decisions" sets no condition
  - retention-058: "meaningful boundaries" sets no checkable condition
  - retention-062: "when needed" vague condition
  - tdd-018: "usefully verifies" is not a checkable condition
  - visuals-003: "better judged by seeing" is not a checkable condition
  - workflow-guide-035: "when warranted" is not a checkable condition
- V6 (4):
  - readme-117: filler adjective "natural"
  - readme-159: figurative statement that gives no action
  - readme-166: attributes ownership of meaning to Lusona, gives no action
  - retention-036: metaphor "buried"
- V7 (6):
  - readme-059: "small clear work" has no measurable bound
  - commits-006: "small change" has no measurable bound
  - evidence-034: "large raw outputs" has no size threshold
  - evidence-035: "large disposable outputs" has no size threshold
  - interviews-011: "a small related group" has no count
  - retention-021: "smallest suitable" has no measurable bound
- V9 (4):
  - commits-040: explanatory clause "a fast-forward can import" in the instruction
  - model-routing-003: describes the guidance's status instead of an action
  - model-routing-011: explains an unrelated host feature
  - retention-012: rationale clause "so the reviewer has acceptance criteria" in instruction
- V8, pointer rows (3; duplicate-group rows are listed below):
  - handoff-002: README budget and this file point at each other
  - queue-041: chain, links README contract, which links queue back
  - retention-003: chain, links README contract, which links back to retention

### Duplicate groups (V8)

86 groups state the same policy in more than one place. Rows in a group are tagged V8 in the Conflicts column.

| Group | Policy | Rows | Files |
| --- | --- | --- | --- |
| D01 | Failed or unrun required checks block completion | readme-135, queue-056, delegation-029 | 3 |
| D02 | Passing tests or a commit are not human acceptance or delivery | readme-136, queue-057, commits-033, batch-execution-049 | 4 |
| D03 | Completion requires the whole outcome, criteria, checks and required acceptance | readme-134, queue-055, batch-execution-048 | 3 |
| D04 | Specs, plans, ADRs and queue states do not authorize implementation | readme-070, queue-004, queue-048 | 2 |
| D05 | A proposal or proposed step does not authorize execution | readme-122, retention-039, interview-examples-019 | 3 |
| D06 | Implementation requires explicit TDD selection | readme-131, tdd-002 | 2 |
| D07 | Unset TDD permits definition and planning only | readme-132, tdd-006, batch-execution-028 | 3 |
| D08 | Only the coordinator writes shared queues, batch records and their handoffs | readme-080, delegation-013, batch-execution-033, queue-002, queue-044 | 4 |
| D09 | Delegated workers return findings or queue changes to the coordinator | readme-087, queue-030, queue-043 | 2 |
| D10 | Project data belongs to the consuming project, never plugin resources | readme-077, readme-079, files-002, files-003, files-036, visuals-002 | 3 |
| D11 | Bundled links resolve relative to the loaded resource | readme-078, files-004 | 2 |
| D12 | Do not initialize project data for orientation or installation | closeout-027, retention-074, files-035 | 3 |
| D13 | Pass an explicit project root; existing files are preserved | closeout-020, closeout-021, retention-069, retention-070, work-record-040, work-record-042 | 3 |
| D14 | Helper initializes records and returns paths | closeout-025, retention-072 | 2 |
| D15 | Use the bundled work-record helper | closeout-014, naming-008, retention-065 | 3 |
| D16 | Follow work-record shell selection, paths and invocation | closeout-015, naming-011, retention-066 | 3 |
| D17 | History week numbers are month-local | closeout-016, work-record-039 | 2 |
| D18 | A spec requires a queue row | readme-088, queue-028, retention-012, retention-025 | 3 |
| D19 | Read correction limits before correcting a failed check or finding | readme-039, corrections-001 | 2 |
| D20 | Expected TDD red is not a correction round | readme-040, corrections-002, corrections-010 | 2 |
| D21 | Persona change is not independence; report unavailable review as unmet | readme-140, readme-141, batch-execution-050 | 2 |
| D22 | Conditions that require independent review | readme-138, retention-012 | 2 |
| D23 | Read model routing before dispatch and worker lifecycle after results | readme-181, readme-182, delegation-004, model-routing-001, worker-lifecycle-001 | 4 |
| D24 | Leaves load coordinator procedures only when granted those responsibilities | readme-183, delegation-005, worker-lifecycle-003 | 3 |
| D25 | Leaves do not interview users | readme-171, delegation-008, batch-execution-024 | 3 |
| D26 | Domain skills do not expand responsibility or authority | readme-171, delegation-011 | 2 |
| D27 | Read evidence rules before a measurement or experiment | readme-053, evidence-001 | 2 |
| D28 | Read handoff before a checkpoint or handoff | readme-187, handoff-001 | 2 |
| D29 | Silence or unanswered requests are not consent | readme-128, batch-execution-027 | 2 |
| D30 | Save substantive outputs without waiting for a request | readme-082, readme-084, readme-119, retention-004, retention-007, retention-011, evidence-011 | 3 |
| D31 | When saving is prevented, report through a permitted channel | readme-086, corrections-007, handoff-006, queue-042, retention-034, tdd-005, visuals-040 | 7 |
| D32 | Answer direct questions first | readme-024, interviews-022 | 2 |
| D33 | Reuse settled answers | readme-026, interviews-021 | 2 |
| D34 | Stop inquiry when more exchanges would not change the outcome | readme-029, interviews-023 | 2 |
| D35 | All current queue items excludes Icebox; batch deferral does not park | batch-use-006, batch-use-008, queue-014, queue-019 | 2 |
| D36 | Existing tracked work remains tracked | queue-051, retention-028 | 2 |
| D37 | Record each fact once; records do not duplicate history | retention-040, closeout-010 | 2 |
| D38 | Existing evidence and notes stay in place; no migration for the new layout | evidence-023, evidence-043, evidence-044, retention-048, retention-049 | 2 |
| D39 | Authorized implementation includes local verified commits | readme-073, commits-001 | 2 |
| D40 | Push, publication and history rewrite need separate authority | readme-075, commits-034, batch-execution-054 | 3 |
| D41 | Use Conventional Commits | commits-023, commits-036 | 1 |
| D42 | Choose the commit type for the outcome | commits-025, commits-037 | 1 |
| D43 | Coordinator owns staging and commits after integration | commits-017, batch-execution-053 | 2 |
| D44 | Reuse valid checks on unchanged inputs; rerun only for changes or risks | delegation-042, delegation-043, tdd-031, tdd-032 | 2 |
| D45 | Skills are responsibilities, not mandatory phases | readme-023, workflow-guide-020, workflow-guide-056 | 2 |
| D46 | Selecting a task does not authorize its whole change | readme-018, workflow-guide-057 | 2 |
| D47 | Change and task definitions | readme-016, readme-017, workflow-guide-049, workflow-guide-050 | 2 |
| D48 | Consult the routing table only when skill selection is unclear | readme-020, readme-021, workflow-guide-002, workflow-guide-018 | 2 |
| D49 | Read-only work reports without saving | readme-050, queue-045 | 2 |
| D50 | New specs and ADRs use YYYYMMDD-slug names | naming-002, work-record-045 | 2 |
| D51 | Legacy sequence commands: existing workflows only, reserve nothing | naming-036, naming-037, naming-038, work-record-049 | 2 |
| D52 | Created date is immutable | naming-030, work-record-056 | 2 |
| D53 | init-change and init-adr JSON statuses and exit codes | naming-014, naming-016, naming-017, naming-018, work-record-043 | 2 |
| D54 | Reopening and row removal go through closeout | queue-040, queue-063, retention-002, retention-075, closeout-001 | 3 |
| D55 | Use the native question tool, otherwise plain text | readme-123, visuals-035 | 2 |
| D56 | Planning-only work stops before execution | readme-071, queue-047, workflow-guide-034 | 3 |
| D57 | No companion plan file for new changes | naming-007, files-010 | 2 |
| D58 | Existing records and separate plans remain valid | files-027, naming-039, batch-use-017 | 3 |
| D59 | Inside a batch the repair budget replaces correction counts | corrections-020, batch-execution-045 | 2 |
| D60 | Idle notifications and reports do not prove success or shutdown | delegation-045, worker-lifecycle-013 | 2 |
| D61 | Preserve the result before shutdown | delegation-014, worker-lifecycle-025 | 2 |
| D62 | Ask only for missing consequential decisions or authority | readme-055, delegation-052, handoff-008 | 3 |
| D63 | Add an execution section only under the README task conditions | readme-058, retention-044 | 2 |
| D64 | Icebox rows retain evidence and stay open | queue-010, retention-031 | 2 |
| D65 | Apply host capacity accounting | readme-180, worker-lifecycle-023 | 2 |
| D66 | Host approval rules apply | readme-129, batch-execution-026 | 2 |
| D67 | Installation does not prove availability or context inheritance | readme-014, delegation-034 | 2 |
| D68 | Delegate the substantive outcome, not preliminary inspection | readme-174, delegation-030 | 2 |
| D69 | Independent reviewers receive actual diff, agreement and evidence | readme-139, delegation-037 | 2 |
| D70 | Consequential architecture decisions require or belong in ADRs | readme-089, retention-043 | 2 |
| D71 | Reuse current text under the Loading rules | readme-063, delegation-003 | 2 |
| D72 | Correct refuted claims visibly beside the original | evidence-030, retention-056 | 2 |
| D73 | Records link the exact evidence runs they rely on | evidence-039, retention-047 | 2 |
| D74 | Record creation never overwrites an existing path | naming-019, work-record-044 | 2 |
| D75 | Coordinator acceptance is separate from worker status | delegation-038, worker-lifecycle-006 | 2 |
| D76 | Reuse an existing item slug | retention-067, work-record-041 | 2 |
| D77 | Leaves read Assigned leaves and Assignment results | readme-168, delegation-001 | 2 |
| D78 | Read tdd when selecting or applying TDD policy | readme-133, tdd-001 | 2 |
| D79 | Dates default to local today | closeout-018, naming-013, work-record-027 | 3 |
| D80 | Continue independent authorized work | readme-036, batch-execution-023, corrections-012 | 3 |
| D81 | Invoke skills as /lusona:<skill> in Claude Code | batch-use-021, workflow-guide-043 | 2 |
| D82 | Switch page only when options differ in one part of a flow | visuals-017, visuals-028 | 1 |
| D83 | Load or include only applicable procedures | readme-093, delegation-036 | 2 |
| D84 | Preserve explicit user model choices and host restrictions | model-routing-003, model-routing-017 | 1 |
| D85 | Supply paths with loading instructions or current text | readme-094, delegation-032 | 2 |
| D86 | Preserve unrelated work and edits | readme-067, commits-020 | 2 |

### Rows with no principle tag

- rule (334): readme-001, readme-002, readme-003, readme-004, readme-005, readme-006, readme-008, readme-009, readme-012, readme-013, readme-024, readme-039, readme-040, readme-049, readme-058, readme-059, readme-060, readme-061, readme-063, readme-076, readme-077, readme-079, readme-080, readme-081, readme-087, readme-088, readme-089, readme-091, readme-092, readme-093, readme-094, readme-123, readme-124, readme-126, readme-130, readme-133, readme-143, readme-147, readme-148, readme-154, readme-156, readme-159, readme-160, readme-161, readme-162, readme-163, readme-167, readme-168, readme-172, readme-173, readme-174, readme-175, readme-180, readme-181, readme-182, readme-183, readme-187, batch-execution-001, batch-execution-005, batch-execution-013, batch-execution-014, batch-execution-018, batch-execution-019, batch-execution-030, batch-execution-033, batch-execution-034, batch-execution-035, batch-execution-039, batch-execution-045, batch-execution-046, batch-execution-051, batch-use-001, batch-use-018, batch-use-020, batch-use-022, closeout-001, closeout-003, closeout-006, closeout-010, closeout-013, closeout-014, closeout-015, closeout-019, closeout-020, closeout-023, closeout-024, closeout-027, commits-002, commits-004, commits-005, commits-007, commits-008, commits-009, commits-010, commits-017, commits-018, commits-023, commits-024, commits-025, commits-029, commits-030, commits-031, commits-035, commits-036, commits-037, commits-038, commits-039, commits-042, commits-047, commits-050, commits-054, commits-055, commits-056, corrections-001, corrections-002, corrections-004, corrections-006, corrections-010, corrections-020, delegation-001, delegation-002, delegation-003, delegation-004, delegation-005, delegation-006, delegation-014, delegation-016, delegation-030, delegation-032, delegation-033, delegation-036, delegation-040, delegation-041, delegation-049, delegation-050, delegation-054, delegation-055, delegation-056, evidence-004, evidence-006, evidence-014, evidence-016, evidence-017, evidence-021, evidence-023, evidence-034, evidence-035, evidence-036, evidence-043, evidence-044, evidence-045, files-001, files-028, files-029, files-030, files-031, files-036, handoff-001, interview-examples-002, interviews-001, interviews-011, interviews-012, interviews-013, interviews-014, interviews-017, interviews-022, interviews-027, model-routing-001, model-routing-002, model-routing-004, model-routing-005, model-routing-012, model-routing-013, model-routing-014, model-routing-015, model-routing-019, model-routing-024, model-routing-025, model-routing-026, model-routing-029, model-routing-030, model-routing-032, naming-001, naming-002, naming-005, naming-007, naming-008, naming-009, naming-010, naming-011, naming-025, naming-026, naming-027, naming-029, naming-032, naming-038, queue-001, queue-002, queue-005, queue-008, queue-009, queue-011, queue-017, queue-021, queue-028, queue-029, queue-030, queue-031, queue-032, queue-033, queue-036, queue-037, queue-038, queue-039, queue-043, queue-044, queue-052, queue-063, retention-001, retention-003, retention-009, retention-012, retention-015, retention-017, retention-018, retention-020, retention-021, retention-023, retention-024, retention-025, retention-026, retention-029, retention-030, retention-035, retention-038, retention-040, retention-042, retention-044, retention-045, retention-048, retention-049, retention-050, retention-051, retention-053, retention-055, retention-058, retention-059, retention-060, retention-061, retention-064, retention-065, retention-066, retention-067, retention-068, retention-069, retention-074, retention-075, tdd-001, tdd-004, tdd-013, tdd-019, tdd-020, tdd-021, tdd-022, tdd-024, visuals-001, visuals-003, visuals-005, visuals-006, visuals-007, visuals-008, visuals-009, visuals-010, visuals-011, visuals-012, visuals-013, visuals-015, visuals-016, visuals-017, visuals-018, visuals-020, visuals-021, visuals-022, visuals-023, visuals-024, visuals-025, visuals-027, visuals-028, visuals-029, visuals-032, visuals-033, visuals-034, visuals-035, visuals-038, visuals-039, visuals-041, visuals-043, visuals-044, visuals-045, visuals-048, visuals-049, visuals-052, visuals-053, visuals-057, work-record-001, work-record-002, work-record-003, work-record-006, work-record-008, work-record-012, work-record-013, work-record-017, work-record-022, work-record-023, work-record-025, work-record-026, work-record-041, work-record-048, worker-lifecycle-001, worker-lifecycle-003, worker-lifecycle-010, worker-lifecycle-014, worker-lifecycle-016, worker-lifecycle-017, worker-lifecycle-020, worker-lifecycle-023, worker-lifecycle-024, worker-lifecycle-025, worker-lifecycle-026, workflow-guide-039, workflow-guide-040, workflow-guide-041, workflow-guide-043, workflow-guide-044
- definition (182): readme-007, readme-011, readme-016, readme-017, readme-057, readme-078, readme-095, readme-115, readme-157, readme-158, readme-166, readme-176, batch-execution-029, batch-execution-052, batch-use-006, batch-use-008, batch-use-011, batch-use-012, batch-use-013, batch-use-014, batch-use-015, batch-use-016, batch-use-017, batch-use-021, closeout-002, closeout-005, closeout-009, closeout-016, closeout-018, closeout-021, closeout-022, closeout-025, commits-003, commits-006, commits-026, commits-058, corrections-003, corrections-015, corrections-016, corrections-017, delegation-017, delegation-018, delegation-020, delegation-021, delegation-022, delegation-026, delegation-027, delegation-028, evidence-012, evidence-015, evidence-018, evidence-019, evidence-022, evidence-040, evidence-041, evidence-046, files-002, files-003, files-004, files-027, files-035, handoff-002, handoff-003, interview-examples-003, interview-examples-004, interviews-003, model-routing-010, model-routing-011, model-routing-021, model-routing-022, model-routing-023, model-routing-027, naming-003, naming-004, naming-006, naming-012, naming-013, naming-014, naming-019, naming-020, naming-021, naming-022, naming-023, naming-024, naming-028, naming-030, naming-031, naming-033, naming-034, naming-035, naming-036, naming-037, naming-039, naming-042, queue-003, queue-007, queue-010, queue-014, queue-018, queue-019, queue-020, queue-034, queue-041, queue-049, queue-050, queue-051, queue-061, retention-002, retention-008, retention-010, retention-013, retention-014, retention-016, retention-019, retention-027, retention-028, retention-031, retention-032, retention-041, retention-043, retention-052, retention-063, retention-070, retention-071, retention-072, tdd-003, tdd-010, tdd-011, tdd-012, tdd-014, tdd-029, tdd-030, visuals-002, visuals-014, visuals-026, visuals-036, visuals-042, visuals-050, visuals-054, visuals-055, visuals-058, visuals-059, visuals-066, work-record-004, work-record-005, work-record-007, work-record-009, work-record-010, work-record-011, work-record-016, work-record-021, work-record-027, work-record-039, work-record-040, work-record-042, work-record-043, work-record-044, work-record-045, work-record-046, work-record-047, work-record-049, work-record-050, work-record-051, work-record-052, work-record-053, work-record-054, work-record-055, work-record-056, worker-lifecycle-002, worker-lifecycle-004, worker-lifecycle-018, worker-lifecycle-027, workflow-guide-021, workflow-guide-045, workflow-guide-047, workflow-guide-048, workflow-guide-049, workflow-guide-050, workflow-guide-051, workflow-guide-052, workflow-guide-053, workflow-guide-054
- example (13): batch-use-005, batch-use-010, batch-use-019, closeout-017, interview-examples-011, interview-examples-014, interview-examples-015, interview-examples-017, interview-examples-018, interview-examples-020, interview-examples-023, work-record-014, work-record-015
- catalog (79): readme-097, readme-098, readme-099, readme-100, readme-101, readme-102, readme-103, readme-104, readme-105, readme-106, readme-107, readme-108, readme-109, readme-110, readme-111, readme-112, readme-113, readme-114, files-006, files-007, files-008, files-009, files-010, files-011, files-012, files-013, files-014, files-015, files-016, files-017, files-018, files-019, files-020, files-021, files-022, files-023, files-024, files-025, files-026, interview-examples-006, interview-examples-007, interview-examples-008, interview-examples-009, interview-examples-010, model-routing-007, model-routing-008, model-routing-009, naming-016, naming-017, naming-018, queue-023, queue-024, queue-025, queue-026, queue-027, work-record-029, work-record-030, work-record-031, work-record-032, work-record-033, work-record-034, work-record-035, work-record-036, work-record-037, work-record-038, workflow-guide-004, workflow-guide-005, workflow-guide-006, workflow-guide-007, workflow-guide-008, workflow-guide-009, workflow-guide-010, workflow-guide-011, workflow-guide-012, workflow-guide-013, workflow-guide-014, workflow-guide-015, workflow-guide-016, workflow-guide-017
- not a rule (17): readme-096, batch-use-004, batch-use-009, delegation-023, files-005, files-033, interview-examples-001, model-routing-006, naming-015, queue-022, tdd-009, work-record-028, worker-lifecycle-005, workflow-guide-003, workflow-guide-023, workflow-guide-042, workflow-guide-046

### Contract rows

| K | Rows | Files |
| --- | --- | --- |
| K1 | 16 | batch-use, workflow-guide |
| K2 | 59 | readme, batch-execution, batch-use, closeout, evidence, files, naming, queue, retention, tdd, visuals, work-record |
| K3 | 87 | closeout, naming, retention, work-record |
| K4 | 17 | readme, batch-execution, queue, tdd |
| K5 | 0 | none |

K5 (plugin name in manifests and catalogs) has no source line in the README or references.

### Cross-check: principle anchors

The P table in spec 20261111 cites README line ranges as sources. Each README row in a cited range should carry that principle.

| Principle | README lines | Rows in range | Rows with the tag | Rows without |
| --- | --- | --- | --- | --- |
| P1 | L27-L27 | 2 | 1 | readme-022 |
| P2 | L26-L27 | 2 | 1 | readme-023 |
| P2 | L31-L32 | 3 | 1 | readme-027, readme-029 |
| P3 | L43-L43 | 2 | 2 | none |
| P4 | L44-L46 | 6 | 5 | readme-042 |
| P5 | L31-L31 | 2 | 1 | readme-027 |
| P6 | L68-L74 | 9 | 7 | readme-069, readme-072 |
| P7 | L31-L38 | 10 | 7 | readme-028, readme-032, readme-033 |

Rows without the tag share a cited line but state a different rule (for example readme-027, the next-action rule, is P7 on line 31, which the P2 and P5 rows also cite).

### Cross-check: 20261110 mapping rows

README rows map to 52 of the 54 mapping rows. Unmatched mapping rows: 53, 54.
Rows 53 and 54 describe uncommitted hooks and `completion.md` material that is not in `34186da`, so they have no source row.

| Mapping row | README rows |
| --- | --- |
| 1 | readme-001, readme-002, readme-003, readme-004, readme-005, readme-006 |
| 2 | readme-007, readme-008, readme-009 |
| 3 | readme-010, readme-011, readme-012, readme-013, readme-014 |
| 4 | readme-015 |
| 5 | readme-016, readme-017, readme-018 |
| 6 | readme-019, readme-020, readme-021 |
| 7 | readme-022, readme-023 |
| 8 | readme-024, readme-025, readme-026 |
| 9 | readme-027, readme-028, readme-029, readme-030, readme-031, readme-032, readme-033 |
| 10 | readme-034, readme-035, readme-036, readme-037, readme-038 |
| 11 | readme-039, readme-040 |
| 12 | readme-041, readme-042, readme-043, readme-044, readme-045, readme-046, readme-047 |
| 13 | readme-048, readme-049, readme-050, readme-051, readme-052 |
| 14 | readme-053 |
| 15 | readme-054, readme-055 |
| 16 | readme-056, readme-057, readme-058, readme-059, readme-060 |
| 17 | readme-061, readme-062, readme-063 |
| 18 | readme-064, readme-065, readme-066, readme-067, readme-068, readme-069 |
| 19 | readme-070, readme-071, readme-072 |
| 20 | readme-073, readme-074 |
| 21 | readme-075 |
| 22 | readme-076 |
| 23 | readme-077, readme-078, readme-079 |
| 24 | readme-080, readme-081 |
| 25 | readme-082, readme-083, readme-084, readme-085, readme-086 |
| 26 | readme-087 |
| 27 | readme-088 |
| 28 | readme-089 |
| 29 | readme-090, readme-091 |
| 30 | readme-092, readme-093, readme-094, readme-095, readme-096, readme-097, readme-098, readme-099, readme-100, readme-101, readme-102, readme-103, readme-104, readme-105, readme-106, readme-107, readme-108, readme-109, readme-110, readme-111, readme-112, readme-113, readme-114 |
| 31 | readme-115, readme-116 |
| 32 | readme-117, readme-120, readme-121 |
| 33 | readme-118, readme-119, readme-122 |
| 34 | readme-123, readme-124 |
| 35 | readme-125, readme-126, readme-127, readme-128, readme-129, readme-130 |
| 36 | readme-131, readme-132, readme-133 |
| 37 | readme-134, readme-135, readme-136, readme-137, readme-142 |
| 38 | readme-138, readme-139, readme-140, readme-141 |
| 39 | readme-143, readme-144 |
| 40 | readme-145 |
| 41 | readme-146, readme-147 |
| 42 | readme-148 |
| 43 | readme-149 |
| 44 | readme-150, readme-151, readme-152, readme-153, readme-154, readme-155 |
| 45 | readme-156, readme-157, readme-158, readme-159 |
| 46 | readme-160, readme-161, readme-162, readme-163, readme-164, readme-165, readme-166 |
| 47 | readme-167 |
| 48 | readme-168, readme-169, readme-170, readme-171 |
| 49 | readme-172, readme-173, readme-174, readme-175, readme-176, readme-177, readme-178 |
| 50 | readme-179, readme-180 |
| 51 | readme-181, readme-182, readme-183 |
| 52 | readme-184, readme-185, readme-186, readme-187 |
| 53 | none |
| 54 | none |

## Coverage check

Command, run from the repository root: `python3 scripts/check_rule_inventory.py docs/lusona/notes/rule-inventory-34186da.md 34186da`.
The script reads each source (the README, every `references/*.md` and every `skills/*/references/*.md`) with `git show 34186da:<path>` and parses this note. It checks that
(1) every non-blank source line other than headings and table separator rows, code-fence lines included, lies in at least one row's Lines range;
(2) each Rule cell occurs verbatim in the whitespace-joined source lines of its range (list and blockquote markers removed);
(3) IDs are unique and consecutive from 001 per file.
Negative test: a copy of this note with handoff-011 deleted and tdd-019's text and range altered made the script report `handoff: uncovered lines [12]` and `tdd: rule text not found verbatim in its line range: ['tdd-019']`, end with `FAIL`, and exit 1.

```text
readme: 211 lines, 163 content lines, 0 uncovered, 187 rows, 0 verbatim failures
batch-execution: 57 lines, 52 content lines, 0 uncovered, 54 rows, 0 verbatim failures
batch-use: 39 lines, 28 content lines, 0 uncovered, 24 rows, 0 verbatim failures
closeout: 29 lines, 24 content lines, 0 uncovered, 27 rows, 0 verbatim failures
commits: 65 lines, 58 content lines, 0 uncovered, 58 rows, 0 verbatim failures
corrections: 26 lines, 21 content lines, 0 uncovered, 20 rows, 0 verbatim failures
delegation: 70 lines, 50 content lines, 0 uncovered, 57 rows, 0 verbatim failures
evidence: 71 lines, 49 content lines, 0 uncovered, 49 rows, 0 verbatim failures
files: 43 lines, 33 content lines, 0 uncovered, 36 rows, 0 verbatim failures
handoff: 12 lines, 9 content lines, 0 uncovered, 11 rows, 0 verbatim failures
interview-examples: 123 lines, 77 content lines, 0 uncovered, 25 rows, 0 verbatim failures
interviews: 26 lines, 21 content lines, 0 uncovered, 28 rows, 0 verbatim failures
model-routing: 39 lines, 30 content lines, 0 uncovered, 32 rows, 0 verbatim failures
naming: 47 lines, 36 content lines, 0 uncovered, 42 rows, 0 verbatim failures
queue: 62 lines, 52 content lines, 0 uncovered, 63 rows, 0 verbatim failures
retention: 83 lines, 74 content lines, 0 uncovered, 75 rows, 0 verbatim failures
tdd: 36 lines, 29 content lines, 0 uncovered, 32 rows, 0 verbatim failures
visuals: 92 lines, 70 content lines, 0 uncovered, 66 rows, 0 verbatim failures
work-record: 67 lines, 51 content lines, 0 uncovered, 56 rows, 0 verbatim failures
worker-lifecycle: 30 lines, 24 content lines, 0 uncovered, 27 rows, 0 verbatim failures
workflow-guide: 71 lines, 53 content lines, 0 uncovered, 57 rows, 0 verbatim failures
execution: 167 lines, 137 content lines, 0 uncovered, 141 rows, 0 verbatim failures
TOTAL: 22 files, 1141 content lines, 1167 rows, PASS
```

