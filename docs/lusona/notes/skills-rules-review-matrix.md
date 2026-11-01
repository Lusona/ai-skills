# Lusona skills and rules — review matrix

Snapshot: 2026-10-31, canonical working tree targeting 1.4.0, including uncommitted changes.
Purpose: a source-linked inventory for comparing, replacing, or simplifying rules. This is a
review aid, not a second normative contract. Source files govern; proposed swaps below are
unaccepted. IDs identify rows in this document only. “Swap” is interpreted as comparing current
wording with proposed replacement wording; no rules are changed by this inventory.

## 1. Structure and ownership

| Layer | Owns | Source | Review question |
| --- | --- | --- | --- |
| Host, user, repository | Permissions, explicit scope, local restrictions | Host instructions, user request, repository AGENTS.md | Does a local restriction override a plugin default? |
| Shared contract | Authority, work loop, saving, TDD gate, completion, roles, communication | [Core](../../../plugins/lusona/README.md) | Is this invariant needed across skills? |
| Shared procedures | Operational detail loaded when applicable | Procedure catalog below | Is there one owner for the rule? |
| Skills | Trigger, specialist judgment, bounded outcome, next action | Skill matrix below | Does this skill add distinct expertise? |
| Templates | Record structure and relevant prompts | [Templates](../../../plugins/lusona/templates) | Does saved output remain usable outside the plugin? |
| Helpers and packaging | Record initialization, metadata and resource distribution | [Helpers](../../../plugins/lusona/scripts), [Packager](../../../scripts/package.py) | Does tooling preserve the written contract? |
| Consuming-project records | Actual agreements, decisions, state, evidence, handoffs | [File ownership](../../../plugins/lusona/references/files.md) | Is each fact retained once, with a clear owner? |

Skills are selectable responsibilities, not mandatory sequential stages. Every skill inherits
the shared contract. The skill table lists distinctive rules, not every inherited rule.

## 2. Skill matrix

All substantive saving below is subject to explicit read-only/no-save restrictions and write
permissions. The coordinator owns shared queue and saved handoff updates; assigned leaves return
those changes. Implementation always needs scope authorization and an explicit TDD policy.

| ID | Skill / source | Use when / responsibility | Distinctive rules and boundaries | Durable output |
| --- | --- | --- | --- | --- |
| S01 | [explore](../../../plugins/lusona/skills/explore/SKILL.md) | Develop understanding, alternatives, long-term possibilities | Answer first; compare meaningful alternatives; decision optional; ordinary conversation may stay local; no implementation authority | Substantive synthesis in existing owner or notes; no forced spec/queue |
| S02 | [frame-product](../../../plugins/lusona/skills/frame-product/SKILL.md) | Establish audience, problem, vision, outcomes, exclusions | Preserve mature ambition separately from first delivery; coordinator interviews, specialist synthesizes; preserve existing map/architecture | Requested brief in product.md |
| S03 | [map-capabilities](../../../plugins/lusona/skills/map-capabilities/SKILL.md) | Establish coverage, dependencies, delivery order | Evidence for dependencies; horizons are not commitments; no automatic detailed backlog, specs, or queue entries | Capability map in product.md |
| S04 | [specify](../../../plugins/lusona/skills/specify/SKILL.md) | Define one bounded observable outcome | Stable acceptance IDs; retain technical constraints and sources; unknown causes remain hypotheses; save even small specs; reconcile queue; Ready requires accepted scope/criteria and selected TDD | Spec plus coordinator-maintained queue row |
| S05 | [architect](../../../plugins/lusona/skills/architect/SKILL.md) | Resolve consequential boundaries, contracts, ownership | Compare consequential tradeoffs; preserve constraints; save every consequential decision; supersede with linked ADR; no production edits or implied implementation authority | ADR and links from relevant product/spec; routine choices stay in owner |
| S06 | [investigate](../../../plugins/lusona/skills/investigate/SKILL.md) | Reproduce failure, establish cause or feasibility | Distinguishing hypotheses/experiments; observed vs inferred; isolate temporary edits; no speculative production fixes; stop when evidence/input limits apply | Findings in owner or notes; material evidence linked |
| S07 | [measure](../../../plugins/lusona/skills/measure/SKILL.md) | Establish magnitude, quality, cost, or change | Define metric/reference; validate instrument; pin inputs/revision; comparable observations; report variation and limits; candidate vs verified gains | Material measurements in evidence; routine checks stay with task |
| S08 | [experiment](../../../plugins/lusona/skills/experiment/SKILL.md) | Evaluate an intervention or alternatives | Declare criteria, controls, budget, stopping condition before results; retain unfavorable results; label post-hoc changes; adopt/reject/refine/inconclusive does not authorize production adoption | Trial design and exact-run evidence, linked from owner |
| S09 | [implement](../../../plugins/lusona/skills/implement/SKILL.md) | Plan or execute authorized behavior changes/fixes | Planning-only stops before edits; explicit TDD; plan proportional to dependencies/recovery; verify actual outcome; no Specify prerequisite for clear work | Existing spec/plan or notes; queue required when spec-linked/already tracked |
| S10 | [refactor](../../../plugins/lusona/skills/refactor/SKILL.md) | Resolve a concrete structural problem while preserving behavior | Existing implementation; passing baseline; reversible increments; preserve public contracts/data formats; behavior changes route to implement; no speculative cleanup | Existing owner or notes, baseline/final evidence; same tracking condition as implement |
| S11 | [review](../../../plugins/lusona/skills/review/SKILL.md) | Assess a specified actual diff | Concrete failure/consequence and severity; inspect callers/tests; distinguish defects/questions/suggestions; fresh reviewer for independence; do not fix/commit/deploy | Coordinator saves findings and limits in owner or notes; state recommendation only |
| S12 | [status](../../../plugins/lusona/skills/status/SKILL.md) | Orient, resume, explain remaining work | Recorded claims vs verified facts; preserve broader requested scope; report Icebox separately; read-only assessment does not repair tracking; no audit for simple orientation | Brief status need not be saved; requested inventory can be a deliverable |
| S13 | [batch](../../../plugins/lusona/skills/batch/SKILL.md) | Coordinate explicitly selected unattended work | Freeze membership; exclude Icebox unless reactivated; reconcile dependencies/ownership; one bounded assignment pool; default two corrective rounds/item; independent integration review; deferral preserves state | Batch coordination record; linked per-item owners; parent queue/handoffs |

## 3. Shared rule matrix

| ID | Rule family | Current requirement | Applies / exception | Canonical owner |
| --- | --- | --- | --- | --- |
| R01 | Loading | Read required core sections once per context; reuse current inherited text; load applicable procedures | All roles; coordinators have additional sections | [Loading](../../../plugins/lusona/README.md#loading-rules) |
| R02 | Authority | Skills, records, Ready state, and recommendations do not authorize execution; preserve accepted scope; ask for missing consequential decisions | All; routine choices within authority need no repeated permission | [Contract](../../../plugins/lusona/README.md#contract) |
| R03 | Continuation | Continue useful bounded authorized work; follow-ups steer unless replacing/cancelling; pause only affected work | All; unavailable prerequisite, user pause, correction limit | [Work loop](../../../plugins/lusona/README.md#work-loop) |
| R04 | Questions | Use permitted native question UI; no mode switch solely to ask; silence/preselection is not consent | Coordinator owns user conversation; leaves return questions | [Questions](../../../plugins/lusona/README.md#questions-and-next-actions), [Interviews](../../../plugins/lusona/references/interviews.md) |
| R05 | TDD | Explicit none/targeted/strict and source; unset blocks implementation; record genuine red/green where selected | Refactoring characterizes existing behavior and stays green; none still requires verification | [TDD](../../../plugins/lusona/references/tdd.md) |
| R06 | Saving | Save substantive outputs before handoff/completion, including small work; reuse owner; no separate save request | Explicit restrictions prevail; ordinary dialogue/brief status need no file | [Retention](../../../plugins/lusona/references/retention.md) |
| R07 | Tracking | Every new spec requires a row; reconcile selected existing specs; preserve state, Icebox, history | Spec-free work may remain untracked in notes; existing tracked work remains tracked | [Queue](../../../plugins/lusona/references/queue.md) |
| R08 | Planning | Execution sections/tasks only when useful for dependencies, uncertainty, coordination, recovery, long context, or requested planning | Clear work can proceed without Specify; planning-only stops before execution | [Work loop](../../../plugins/lusona/README.md#work-loop), [Implement](../../../plugins/lusona/skills/implement/SKILL.md) |
| R09 | Decisions | Consequential architecture decisions require ADRs; preserve rationale and supersession links | Routine local choices do not need ADRs | [Architect](../../../plugins/lusona/skills/architect/SKILL.md#decide-and-record) |
| R10 | Evidence | Actual results, provenance, uncertainty, exact-run links; no unsupported improvement claims | Routine checks stay with owner; material measurements/experiments use evidence records | [Evidence](../../../plugins/lusona/references/evidence.md), [Retention](../../../plugins/lusona/references/retention.md) |
| R11 | Completion/review | Whole outcome, criteria, required checks, acceptance/delivery; self-inspection required | Independent review required by user/repo or security, persistent data, shared contracts, coordinated writers; batch also requires independent review | [Review/completion](../../../plugins/lusona/README.md#review-and-communication), [Batch](../../../plugins/lusona/skills/batch/SKILL.md) |
| R12 | Delegation | Coordinator delegates substantive specialist work; owns questions, reconciliation and shared state; bounded assignments | Explore/status orientation and task-local empirical checks may stay local; prohibited/unavailable delegation permits local fallback, not independent-review substitution | [Roles](../../../plugins/lusona/README.md#personas-and-subagents), [Delegation](../../../plugins/lusona/references/delegation.md) |
| R13 | Model/lifecycle | Select least capable adequate available model and supported reasoning; inspect results; follow up or release via actual host controls | Honor explicit choices/host limits; never claim unavailable shutdown or released capacity | [Routing](../../../plugins/lusona/references/model-routing.md), [Lifecycle](../../../plugins/lusona/references/worker-lifecycle.md) |
| R14 | Corrections | Track consecutive no-progress and total rounds for same failure; stop after 2 without progress; 4 total needs user decision | Expected task-local TDD red excluded; batch uses recorded repair budget | [Corrections](../../../plugins/lusona/references/corrections.md) |
| R15 | Commits/delivery | Plugin allows local verified implementation commits unless user/repo prohibits; push/publication/PRs etc. need separate authority | This repository prohibits commits unless requested; current inventory grants no commit authority | [Contract](../../../plugins/lusona/README.md#contract), [Commits](../../../plugins/lusona/references/commits.md) |
| R16 | Record closeout | Preserve completion/evidence/history links before removing Done row; explicit authority to reopen | Untracked work needs no history entry | [Closeout](../../../plugins/lusona/references/closeout.md) |
| R17 | Context | Preserve one current recovery handoff at boundaries; measured target before 50%; no invented usage | Without telemetry checkpoint at task boundaries; context transfer does not end authorization | [Context](../../../plugins/lusona/README.md#context-budget) |
| R18 | Communication | Outcome, evidence/limits, next owner/action/input; provisional Result/Evidence/Next action and status-label trial | User/host formatting overrides; ordinary dialogue remains natural | [Communication](../../../plugins/lusona/README.md#review-and-communication) |
| R19 | Visuals | Compare useful options; retain chosen reference with binding vs illustrative items; implement/review check binding items | Only when applicable; no visual reference leaves implementation/review unchanged | [Visuals](../../../plugins/lusona/references/visuals.md) |
| R20 | Resource paths | Plugin resources resolve relative to loaded resource; project data belongs in consuming project; preserve legacy ownership | Installation does not initialize project records | [Files](../../../plugins/lusona/references/files.md), [Helper invocation](../../../plugins/lusona/references/work-record.md) |

## 4. Record ownership

Paths below are relative to the consuming project, not the plugin installation.

| Record | Owns | Creation/update trigger | Does not imply |
| --- | --- | --- | --- |
| docs/lusona/README.md | Optional local contract/standing TDD | Project-local policy is needed | Mandatory setup |
| product.md | Brief, capability map, shared ADR links | Requested definition/map/documentation | Detailed backlog or execution state |
| specs/<change-id>.md | Agreement, criteria, TDD, optional execution, evidence, current handoff | Every specified definition; optional direct implementation owner | Implementation authority |
| work.md | Active/Icebox state, priority, concise completion condition, owner links | Spec created/used/updated; already tracked work | Task diary, authority, or TDD selection |
| adr/<date>-<slug>.md | Consequential decision/rationale/status | Consequential architecture decision | Production edit authority |
| notes/<slug>.md | Substantive synthesis/findings or spec-free work without another owner | Durable output needs an owner | Queue enrollment or full spec |
| evidence/ | Material measurement/experiment design, runs, provenance | Material empirical support for a decision | Routine test log duplication |
| visuals/<record-id>/ | Chosen visual reference and binding items | Applicable chosen option retained | Acceptance of illustrative details |
| batches/<slug>.md | Fixed selection, authority, assignments, recovery, batch handoff | Authorized batch | Duplicate per-item requirements/evidence |
| history/YYYY-MM-week-NN.md | Archived completion state and links | Tracked closeout before queue removal | Erasure of original evidence |
| plans/<change-id>.md | Existing separate execution ownership | Maintain existing legacy record | New companion plan requirement |

## 5. Swap/review worksheet

Copy a row for each proposed change. Use S/R IDs plus the exact source section to identify the
target. Review shared rules before skill-specific wording so the same decision is not made
13 times. A source move, deletion, or replacement must account for linked procedures,
templates, helpers, and existing record compatibility.

| Target ID / exact source | Current wording | Proposed replacement / destination | Reason / intended behavior change | Affected skills and resources | Behavior to preserve / verification | Decision / authority |
| --- | --- | --- | --- | --- | --- | --- |
| <Sxx or Rxx + section> | <quote exact clause> | <new clause, move, or delete> | <concrete problem and outcome> | <consumers and links> | <scenario and expected result> | Proposed / accepted / rejected; source |

Suggested review order (questions, not confirmed defects):

| Order | Review unit | Comparison to make |
| --- | --- | --- |
| 1 | R02–R05: authority, continuation, questions, TDD | Required decisions versus routine autonomy; ask/continue/pause boundaries |
| 2 | R06–R10, R16, R20: records | Mandatory saving versus smallest suitable record; spec tracking versus direct notes; ownership and valid links |
| 3 | R11–R14: agents and checks | Mandatory delegation versus local work; independent review; capacity, release, correction budgets |
| 4 | S01–S05: definition | Distinct output of exploration, product framing, mapping, specification, architecture |
| 5 | S06–S08: empirical work | Cause/feasibility versus magnitude versus intervention evaluation; shared evidence requirements |
| 6 | S09–S13: execution and coordination | Implementation versus refactor; reviewer authority; status breadth; batch exceptions |
| 7 | R15, R17–R19: delivery and presentation | Commit defaults, context recovery, response-format trial, visual-reference obligations |

## Consistency review — 2026-10-31

Requested follow-up: identify inconsistencies, without changing directives. Parent inspected
current sources and reconciled an independent read-only review by `/root/directive_consistency`.
This broader review supplements the earlier cohesion review; it does not reopen the repaired
template-link defect. Static source review only; no agent-behavior trials were run.

| Finding | Classification / impact | Source pair | Proposed correction (not authorized or applied) |
| --- | --- | --- | --- |
| F1: diagram retention and consumption disagree | P2 contract mismatch. A properly retained Mermaid diagram has Markdown instead of HTML, but downstream implement/review still require HTML. The no-screenshot retention fallback likewise permits missing PNGs without making consumption conditional. Valid records can appear incomplete. | [Visual retention](../../../plugins/lusona/references/visuals.md#retention-after-a-choice), [Consumption](../../../plugins/lusona/references/visuals.md#consumption), [Allowed record forms](../../../plugins/lusona/references/files.md#files) | Define consumption by reference type: HTML/UI versus Mermaid/diagram; inspect available captures and explicitly report missing visual verification. Align reference template fields. |
| F2: discussion restrictions have unclear scope | Ambiguity. Frame-product and map-capabilities say discussion alone does not authorize edits; core requires retaining substantive synthesis without a save request. Reading “edits” as all files loses useful synthesis; reading it as product.md permits notes. | [Frame brief](../../../plugins/lusona/skills/frame-product/SKILL.md#record-the-brief), [Map](../../../plugins/lusona/skills/map-capabilities/SKILL.md#record-the-map), [Retention](../../../plugins/lusona/references/retention.md) | Limit the prohibition to accepting/changing the product brief or map; explicitly retain substantive discussion in notes under normal retention. |
| F3: rejected visuals say “save nothing” | Ambiguity. The phrase can suppress recording consequential rejection reasons or new constraints, although retention requires substantive decisions/open questions. Draft artifact exclusion is reasonable; losing decision facts is not. | [Choice](../../../plugins/lusona/references/visuals.md#choice), [Retention](../../../plugins/lusona/references/retention.md) | Say not to retain rejected draft artifacts as chosen references; save material reasons/constraints in the owning record. |
| F4: contribution exclusion does not distinguish this repository's own records | Local-policy scope ambiguity, not an unresolved precedence conflict. CONTRIBUTING excludes consuming-project records from contributions, while the plugin commit procedure includes related change records/evidence. Repository restrictions win, but it is unclear whether the exclusion covers this repository's own development records or only external consumer data. | [Contribution instructions](../../../CONTRIBUTING.md#make-a-change), [Commit records](../../../plugins/lusona/references/commits.md) | State which project records belong in contributions and distinguish that from excluding project data from distributable packages. |

Explicitly resolved differences, not findings: repository no-commit rules override plugin commit
defaults; batch repair budgets override ordinary correction limits; leaves route questions and
handoff changes through the coordinator; review leaves remain read-only while the coordinator
retains results; spec-free work may use notes while spec-linked work requires queue tracking.

## Approved wording revisions — 2026-10-31

User accepted F2 and F3, preferring concise rewrites over additional instructions. Implemented:

- Frame-product and map-capabilities now restrict discussion-only changes to the brief/map,
  while routing substantive discussion to its existing owner or notes under retention.
- Visual choice now excludes rejected draft assets while retaining consequential rejection
  reasons and new constraints under retention.

These resolve the ambiguous clauses by restating the existing shared retention contract;
they add no new workflow stage or saving requirement. The earlier findings above describe the
pre-revision text. Editor: `/root/rewrite_retention_clauses`; parent inspected the exact three-file
diff. Standing targeted TDD remains unchanged; no new test-first behavior is introduced by this
editorial clarification. Both changed skills passed `quick_validate.py`; the package builder's
resource/link checks passed with output in `tmp/retention-wording-verification`; `git diff --check`
passed. No interactive agent-behavior trials were run, and static checks do not prove behavior.

F1 was initially discussion only; the user decision below supersedes that status. Recommended format policy: Mermaid Markdown for structural
diagrams, HTML plus captures for UI appearance, and consumers matched to the retained format.
Mermaid explicitly represents nodes and connections in text; the expected LLM reading advantage
is an engineering judgment, not a measured comparison. Reference: [Mermaid syntax](https://mermaid.js.org/syntax/flowchart.html).
For F4, this repository already tracks its own development records, while package.py explicitly
selects distributable resources and excludes project records. User accepted the clarification: retain
Lusona development records in this repository, exclude unrelated consuming-project data from
contributions, and exclude project records from distributable packages. Applied as a replacement
of the existing CONTRIBUTING.md bullet; packaging behavior is unchanged.
Verification: all eight package tests pass, including project-record exclusion; whitespace
checks pass. No installation or interactive behavior was tested for this documentation edit.

## Mermaid-only diagram decision — 2026-10-31

User selected: “We should use mermaid for diagram -- no html or png.” This authorizes the
F1 correction: diagrams use fenced Mermaid in conversation and Mermaid Markdown when retained;
neither HTML nor PNG is required or produced for diagrams. UI mockups retain their HTML and
chosen-image workflow. Preserve existing historical records rather than migrating them.

Acceptance: presentation, retention, reference template, resource catalog and implementation/
review consumption agree on the diagram format; obsolete HTML diagram generation is removed;
UI-only template behavior and earlier retention fixes remain intact.

TDD: existing user-selected targeted policy remains; this format change is outside its named
packaging/metadata test-first behaviors. Verification covers the final instruction contract,
resource links/package integrity and independent content review. No model-accuracy improvement
claim or new architecture decision is implied.

Verification completed: `python3 scripts/package.py --output tmp/mermaid-only-verification`
built the portable catalog/ZIP with link validation; all eight package tests passed; canonical
resource links and whitespace checks passed. Removed the HTML diagram variant, its exclusive
styles and CDN/rendering code; shared UI styling and theme storage remain. Independent reviewer
`/root/review_mermaid_policy` inspected the final diff and consumers and reported no actionable
findings. Editor: `/root/mermaid_only_diagrams`. No browser or interactive model trials were run;
these checks establish source consistency and packaging, not measured model behavior. F1 is
resolved. No historical diagrams were migrated and no commits were made.

## Current handoff

- Authorized work: inventory/review, approved F2/F3/F4 rewrites, and the Mermaid-only F1 correction.
- Evidence: read canonical core and all 13 skill files; inspected applicable shared procedures;
  source catalog below enumerates every shared procedure and the batch-local procedure.
- Limits: this is a summarized source map, not an exhaustive clause-by-clause audit or behavioral
  validation. Current working-tree content is the baseline; later edits can stale this snapshot.
- Next action: none for the approved diagram correction; F1–F4 are addressed. Separate
  Antigravity root-manifest installation verification and primary-command documentation remain
  outside this correction. Nothing committed.

## Source catalog

All shared procedures plus the batch-local procedure. Titles are read from the source files.

| Source | Topic |
| --- | --- |
| [references/batch-execution.md](../../../plugins/lusona/references/batch-execution.md) | Batch execution |
| [references/batch-use.md](../../../plugins/lusona/references/batch-use.md) | Batch use |
| [references/closeout.md](../../../plugins/lusona/references/closeout.md) | Closeout and reopening |
| [references/commits.md](../../../plugins/lusona/references/commits.md) | Commit verified increments |
| [references/corrections.md](../../../plugins/lusona/references/corrections.md) | Correction limits |
| [references/delegation.md](../../../plugins/lusona/references/delegation.md) | Delegation |
| [references/evidence.md](../../../plugins/lusona/references/evidence.md) | Decision evidence |
| [references/files.md](../../../plugins/lusona/references/files.md) | Record files and compatibility |
| [references/interview-examples.md](../../../plugins/lusona/references/interview-examples.md) | Interview examples |
| [references/interviews.md](../../../plugins/lusona/references/interviews.md) | Intent interviews |
| [references/model-routing.md](../../../plugins/lusona/references/model-routing.md) | Model routing |
| [references/naming.md](../../../plugins/lusona/references/naming.md) | Document names and headers |
| [references/queue.md](../../../plugins/lusona/references/queue.md) | Work queue |
| [references/retention.md](../../../plugins/lusona/references/retention.md) | Work records and retention |
| [references/tdd.md](../../../plugins/lusona/references/tdd.md) | TDD and verification |
| [references/visuals.md](../../../plugins/lusona/references/visuals.md) | Visual options and references |
| [references/work-record.md](../../../plugins/lusona/references/work-record.md) | Work-record helpers |
| [references/worker-lifecycle.md](../../../plugins/lusona/references/worker-lifecycle.md) | Worker lifecycle |
| [references/workflow-guide.md](../../../plugins/lusona/references/workflow-guide.md) | Workflow guide |
| [skills/batch/references/execution.md](../../../plugins/lusona/skills/batch/references/execution.md) | Execution and recovery |

Template inventory: [adr.md](../../../plugins/lusona/templates/adr.md), [batch.md](../../../plugins/lusona/templates/batch.md), [brainstorm.md](../../../plugins/lusona/templates/brainstorm.md), [evidence.md](../../../plugins/lusona/templates/evidence.md), [history.md](../../../plugins/lusona/templates/history.md), [notes.md](../../../plugins/lusona/templates/notes.md), [product.md](../../../plugins/lusona/templates/product.md), [review.md](../../../plugins/lusona/templates/review.md), [spec.md](../../../plugins/lusona/templates/spec.md), [status.md](../../../plugins/lusona/templates/status.md), [visual-page.html](../../../plugins/lusona/templates/visual-page.html), [visual-reference.md](../../../plugins/lusona/templates/visual-reference.md), [work.md](../../../plugins/lusona/templates/work.md).
