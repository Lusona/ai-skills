# Skill audit: rules for additions to the Lusona plugin

Compiled: 2026-11-13, from the working tree on `main` after commit `6243701` (plugin 3.0.0,
15 skills; `setup` is uncommitted).

Use this document to audit a new or changed skill, reference, template, shared text or record
helper command under `plugins/lusona/` before it is accepted. It lists the principles and rules
that governed the 3.0.0 skill rewrite, each with its source and a check.

- Rule owner: [spec 20261111](lusona/specs/20261111-loop-principles-and-skill-rewrite.md) (the
  rewrite), [ADR 20261111](lusona/adr/20261111-skill-file-layout-and-shared-sources.md) (file
  layout), the [voice limits notes](lusona/notes/voice-limits-measurement.md) (voice decisions),
  `AGENTS.md` and `CONTRIBUTING.md`. This document restates them for audit use. An audit uses
  this document alone. When an auditor finds that an item disagrees with its source, the source
  governs: report the disagreement as a finding against this document and correct it.
- How this document was compiled where sources differ: it states the text now in `shared/` and
  the constants now in the check scripts, then the latest recorded user decision, then the
  original tables (P1-P8, V1-V9, S1-S6) in the spec. This order is not a rule. Section 13 lists
  the places where a script and a decision disagree; the user decides those.
- "Decision N" means user decision N in spec 20261111. "Voice decision N" means decision N in
  the voice limits notes. "W13" means the [independent review](lusona/notes/rewrite-independent-review.md)
  of the rewrite; its finding IDs (F1-F22, B1-B3, N1-N11) name defect classes the scripts missed.
- A rule marked **(inference)** has no recorded decision that states it in general form. It is
  derived from a practice the sources show, or from a criterion the user accepted for one
  addition (`setup`, spec 20261112). The user accepted every item that carried the mark on
  2026-11-13 (conversation: "accept"), including the severity definitions in section 1. Those
  items are rules. The mark stays because it shows the item's origin and because the severity
  definitions use it. An item that gets the mark after 2026-11-13 is a proposal until the user
  accepts it; record the acceptance here with its date and source.
- Revised on 2026-11-13 after the first audit of `setup` (user decision, native question tool,
  option "Change the document"): the pass conditions of P2, T6, V1, V4, E2 and VP7, and the
  severity of an item that carries the inference mark on one part only. Each changed sentence
  carries the mark **(revised 2026-11-13)**. Before the revision, `setup` and baseline skills
  failed these conditions for the same wording.
- Added on 2026-11-13: step 8 of section 1, the rule for the result of an audit (user decision,
  conversation: "approved, proceed"). Its test was extended to the records of the rewrite on the
  same day (user decision, native question tool, option "Extend to records"). Step 8 was then
  applied to the open readings of the `setup` audit. Reworded by the test: V8, E3, D2 and, to
  agree with D2, VP4, each marked **(revised 2026-11-13, step 8)**. P8 keeps its condition and
  gained a definition of "reaches" with the same mark; `review` and `batch` do not meet the
  condition (section 13). Reworded by a user decision where the test
  found no failing passage or record: V2, E4, T11 and VP6, each marked **(revised 2026-11-13,
  user decision)**. Step 6 gained the sentence on observations that no item covers (user decision,
  native question tool, option "Count as non-blocking").
- Other labels: "skeleton" is the skill skeleton accepted in decision 16
  ([drafting notes](lusona/notes/skill-rewrite-drafting/skill-template.md)). S1-S6 are the target
  structure items and AC1-AC19 the acceptance criteria of spec 20261111. A2-A8 are its
  architecture questions and W1-W15 its work items. "Voice pass" is the audit of the promoted
  text against V1-V9 in four rounds ([notes/voice-pass](lusona/notes/voice-pass/)).
- The owning record of an addition is the spec or notes file that holds its agreement, its
  decisions, its TDD level and its evidence.

## 1. Audit procedure

1. Name the base commit (the last commit without the addition) and the owning record. List the
   files of the addition with `git status --short` and `git diff --stat <base>`; `git diff` does
   not show untracked files. When no owning record exists, D1 fails, and E1, E2, E4, E5, D2, D3
   and T14 fail with it.
2. Name the addition types the change contains, using the table in section 3.
3. Run every script check in section 2. Each must exit 0. A non-zero exit is a finding. A check
   that cannot run in the audit environment (no agent host, no PowerShell) is reported under
   step 7, not counted as a pass.
4. Answer every review item that section 3 lists for those types. Record `pass`, `fail` or
   `not applicable` for each item. Give `path:line` for each `fail` and the reason for each
   `not applicable`.
5. List every sentence in the addition that changes, narrows or contradicts an existing rule
   (item D2). Each needs a recorded user decision.
6. Report findings in one table: `ID | Severity | Location | Defect | Violates`. Severity is
   `blocking` (a script check fails, a contract item K1-K7 changes without a recorded decision,
   or an item in sections 4-12 without the inference mark fails) or `non-blocking` (an item with
   the inference mark fails). When an item carries the mark on one part of its text only, the
   severity follows the part that failed **(revised 2026-11-13)**. A gap listed in section 13 does not lower the
   severity. W13 used
   both labels without defining them; this document wrote the definitions **(inference)**.
   An observation of an auditor or reviewer that no item covers is a `non-blocking` finding.
   Report it in the same table with "no item" in the `Violates` column
   **(added 2026-11-13, user decision)**.
7. Report each check that was not run, with the reason. An unrun required check is not a pass.
8. State one result for the addition.
   - `fail`: a blocking finding is open.
   - `pass`: all four conditions hold.
     1. No blocking finding is open.
     2. Each non-blocking finding is corrected, or the owning record holds a user decision that
        accepts it or moves it to a queue row.
     3. Each required check that was not run has a user decision in the owning record that
        accepts the gap.
     4. No result depends on the reading.
   - `undecided`: no blocking finding is open and one of conditions 2 to 4 does not hold. The
     report lists each open item.

   When a result depends on the reading, apply the reading that the 14 skills of 3.0.0 and
   the records of their rewrite (spec 20261111 and its notes) meet **(revised 2026-11-13)**.
   Name the skill passage or the record that fails the other reading. When the skills and the
   records meet both readings, the user decides. In both cases, reword the item's pass
   condition in the same change.

   The result applies to the audited text. After a correction, a reader who did not write the
   correction applies again the items that the changed passages touch. A second full audit is
   not required.

The auditor must not be the author of the addition when independent review is required
(item E5).

## 2. Script checks

Run from the repository root. Use `mise` for tools when it is available.

| Command | Rules it enforces | Documented limits |
| --- | --- | --- |
| `python3 scripts/sync_shared.py --source shared plugins/lusona --check` | B1, B2: each `SKILL.md` holds exactly one region per `shared/*.md` file, identical to its source; `shared/every-task.md` holds at most 300 words (`WORD_LIMITS`) | None recorded |
| `python3 scripts/check_skill_template.py` | T1-T5, T7 (`template`); L7 (`readme`); L1, L2, L5 (`reference`); L3 (`bare-path`); T10 (`size`) | Does not compare frontmatter `name` with the directory name. A sentence counts as a trigger sentence when it holds one word from `TRIGGER_WORDS` or `TRIGGER_CLAUSE_WORDS`; the check does not read whether the trigger matches the reference |
| `python3 scripts/check_voice.py` | VL1-VL4: banned terms (`TERMS`), file average at most 15 words per sentence, no sentence over 40 words | Does not check V1-V4, V6 idioms or V7-V9. Sentence splitting is a heuristic. Templates are scanned for terms only |
| `python3 scripts/check_instructions.py` | T12 in part (`PHRASES`); L12: catalog and routing tables exist once, in `references/workflow-guide.md` | A partial copy of the catalog that links fewer than half of the skills under another header is not detected |
| `python3 scripts/check_contract.py` | K1 for the 14 baseline skills, K2, K3 for the baseline commands, K4, K5, K6 | `SKILLS` and `COMMANDS` hold the inventory at commit `34186da`: `setup` and `init-queue` are not guarded. K4 does not detect an affirmative authority statement spread over several sentences, table cells, or a list without a `:` lead-in |
| `python3 scripts/package.py --output tmp/<new-directory>` | T8, K5 (names and versions aligned), L11 (every relative Markdown link in the package resolves), LICENSE files match, project data excluded | Does not read bare paths. Refuses an existing output directory |
| `python3 -m unittest discover scripts` | Tests of the checks above and of the package (231 tests on 2026-11-13) | None recorded |
| `bash scripts/test-work-record.sh` | K3 behavior of the Bash helper | None recorded |
| `pwsh -NoProfile -File scripts/test-work-record.ps1` | K3 behavior of the PowerShell helper | Native Windows and Windows PowerShell 5.1 are separate runs. Where `pwsh` is a `mise` shim without a set version, run `mise exec powershell@<installed version> -- pwsh -NoProfile -File scripts/test-work-record.ps1` |
| `(cd evals/loop-conformance && python3 -m unittest)` | Suite code (150 tests on 2026-11-13) | Runs no agent trial |
| `claude plugin validate plugins/lusona` and `claude plugin validate .claude-plugin/marketplace.json` | Native manifest and catalog validity | Does not establish installation or invocation |
| `git diff --check` | Whitespace errors in tracked files | Does not read untracked files |

`python3 scripts/check_rule_inventory.py` checks the rule inventory of baseline `34186da` only.
Run it when a change moves or deletes rules that the inventory covers (item D4).

## 3. Items by addition type

| Addition type | Sections to apply |
| --- | --- |
| New skill | 4, 5, 6, 7, 8 (B7, B8), 9, 11, 12 |
| New rule or changed text in an existing skill | 4 (the principles the text touches), 5 (T10-T13), 6 (when a link changes), 7, 11 (E1, E3-E6), 12 |
| New, moved or changed reference | 6, 7, 11 (E1, E3-E6), 12 |
| New or changed template | 6 (L13), 7 (VL1, VL4), 10, 12 |
| Change to `shared/every-task.md` or `shared/final-reply.md` | 8, 7, 9 (K4), 11, 12 |
| New or changed record helper command | 9 (K3), 10 (G5), 11 (E1, E2, E6), 12 |
| Changed listing, README, translation, asset or changelog | 11 (E7, E8), 12 (D5, D7) |

## 4. Loop principles (P1-P8)

Source: spec 20261111, "Loop principles (accepted)", decisions 6 and 7. The placement of each
principle comes from the skill skeleton accepted in decision 16
([drafting notes](lusona/notes/skill-rewrite-drafting/skill-template.md)).

| ID | Rule | Check |
| --- | --- | --- |
| P0 | Skill and reference text does not cite P1-P8 by ID. The principle table exists once, in `references/workflow-guide.md`. | Script-like: `grep -nE '\bP[1-8]\b' plugins/lusona/skills plugins/lusona/references -r` matches only `workflow-guide.md`. |
| P1 | Non-sequential. A skill is a responsibility, not a phase. Any skill may follow any other. | Review: the description names the unresolved need that selects the skill ("Use when") and the adjacent need it does not own ("Not for ...; use `<skill>`"). No sentence in any skill requires the new skill to run before or after another skill. Pass: `git status --short -- plugins/lusona/skills shared` and `git diff --stat <base> -- plugins/lusona/skills shared` show changes only in the new skill's directory, or each other changed line is covered by a recorded decision. |
| P2 | Refinement. Each pass reads the carried state and writes it back. | Review. Pass when both hold **(pass condition is an inference; the skeleton lists the six items without a pass rule)**: (a) `## Establish <input>` tells the agent to read the owning record or the request, or, in a skill that has no owning record, the project state it works on **(revised 2026-11-13)**, and names the carried items this skill's work depends on (from: outcome, accepted decisions, authority, TDD level and source, evidence, uncertainty); (b) `## <Procedure> and record` names what is recorded and the record that receives it, or states that the skill saves nothing. |
| P3 | Prior decisions are inputs. New input that contradicts an accepted decision is neither rejected because of the decision nor applied past it. | Review: no rule or failure mode in the addition forbids reopening an accepted choice without an exception for new input (W13 F4). An unattended context states what happens to such a conflict (W13 F6). Pass: every such sentence carries the exception, or links `revisions` in a trigger sentence. |
| P4 | Recorded invalidation. A superseded decision is marked with date and source and keeps its rationale. | Review: the addition defines no second procedure for superseding a decision. Pass: text about a superseded decision links [revisions](../plugins/lusona/references/revisions.md), or is absent. |
| P5 | Evidence over assertion. Behavior and completion are claimed only from observed checks. | Review: the Persona `Evidence` field states what counts as evidence for this skill's claims and what does not. No step tells the agent to report a result without a check that produced it. |
| P6 | Authority stays with the user. Specs, plans, ADRs and queue states do not authorize implementation. | Script: `check_contract.py` (K4) reports an affirmative authority sentence. Review: each step that writes outside the skill's own output, deletes, commits, pushes or publishes names the authority it needs. Each valid next action that needs authority says so. |
| P7 | Continue bounded work. | Review: each instruction to stop, pause or ask names its condition and what resumes the work. No instruction makes the agent wait for approval between two actions the same request authorizes. |
| P8 | Every task reply names the next action and its owner. | Script: `check_skill_template.py` requires text after the `final-reply` region. Review: that text is a list "Valid next actions for `<skill>`:" in which each item has the form `<condition>: <action>` and names an owner or a skill. The list has one item for each of these cases that the skill can reach **(inference from the 15 current lists)**: work remains and is authorized; an input or decision is missing; the scope is complete. A skill reaches a case when an instruction outside its generated regions tells it to ask the user, to stop or to finish in that case **(revised 2026-11-13, step 8)**. `review` and `batch` each lack an item for one case they reach (section 13). |

P3 and P6 together (decision 6): the agent states the decision, its source, the conflict and
the affected assumptions; revisits the decision with the user, with options and a recommended
answer; records the outcome before dependent work continues; and continues work the conflict
does not affect.

## 5. Skill structure (T)

Sources: spec 20261111 S1, S4, S5 and "Skill template"; spec 20261110 decision 2; decisions 16,
19 and 28; `scripts/check_skill_template.py`; `scripts/package.py`.

| ID | Rule | Source | Check |
| --- | --- | --- | --- |
| T1 | The skill directory name is lowercase and hyphenated. Frontmatter has `name` and `description`. `name` equals the directory name. | S5, K1 | Script: `template` checks that both fields exist. Review: `name` equals the directory name (the script compares them only for the 14 baseline skills, in `check_contract.py`). |
| T2 | The description has three parts in this order: action and output; "Use when ..."; "Not for ...; use `<skill>`" naming an existing other skill. | 20261110 decision 2, AC6 | Script: `template`. Review: the first part names the output the skill produces. |
| T3 | The body starts with an H1. The `every-task` region follows the H1 directly. | AC11, AC12 | Script: `template`. |
| T4 | The H2 sections are, in order: `## Persona and judgment`, `## Establish <input>`, optional `## <Domain> practices`, `## <Procedure> and record`, `## Final reply`. No other H2 is allowed, except in the skills named in `EXTRA_SECTIONS_ALLOWED_FOR` (`batch`, `status`). | 20261110 decision 2; decision 16 (A4) | Script: `template`. Review: a new name in `EXTRA_SECTIONS_ALLOWED_FOR` has a recorded user decision. |
| T5 | `## Persona and judgment` has the fields Persona, Responsibility, Decision criteria, Evidence, Failure modes. Responsibility states what the skill owns and what it does not own. Failure modes are concrete mistakes to check for before replying. | 20261110 AC2; skeleton | Script: `template` (field presence). Review: Responsibility names the outcome the skill owns and at least one thing it does not own, decide or do; each failure mode names an observable mistake, not a quality. |
| T6 | `## <Domain> practices` is omitted only when the skill has no domain checks (skeleton). It holds the checks and prohibitions of the skill's own discipline that apply during the whole procedure; each item is one instruction, and an item that applies only under a condition states the condition **(inference for this sentence)**. | Skeleton; V1 | Review: each conditional item names its condition **(revised 2026-11-13)**. A one-time action placed in practices is a finding only under T11, when a step uses its result before the text instructs it. |
| T7 | `## Final reply` is the last section. It holds the `final-reply` region first, then the skill's valid next actions. | 20261110 decision 2; decision 16 (A2) | Script: `template`. |
| T8 | The `SKILL.md` links at least one existing file in `plugins/lusona/templates/` for its output. | `package.py` `check_skill_templates` | Script: package build. |
| T9 | A skill that does technology-specific or domain-specific work holds this sentence in `## Establish`: "Before `<the skill's first action>`, read the domain skills available in the session that cover the task's technology or domain", followed by an instruction to report a missing required one. | 20261110 mapping row 17; voice decision 9 | Review: the sentence is present and names the skill's first action, or the audit records why the skill does no such work (`status` and `batch` omit it). |
| T10 | Line ceilings: `SKILL.md` 500, reference 200, Markdown template 100 (`SIZE_LIMITS`). The ceilings stop growth; they are not targets. Current skills hold 99 to 144 lines. | S4, decision 10 | Script: `size`. |
| T11 | Steps are ordered only where order matters for correctness or dependencies. Each step has an observable result. Each step uses only inputs that an earlier step or `## Establish` produced. The text states whether an output goes to a file or to the reply. | Skeleton; W13 F15, F16 | Review: for each step, name its result, the input it needs and the step that produces that input. Pass: no result and no input is missing. T11 does not compare the content of one step's output with the content of another's **(revised 2026-11-13, user decision)**. |
| T12 | The skill does not restate a rule of the every-task block. It adds only what it changes or adds. | Skeleton; V8 | Script: `check_instructions.py` reports the phrases in `PHRASES`. Review: no sentence outside the generated regions repeats a block line with the same trigger and action. |
| T13 | A skill that deviates from a block line states it as "Exception to the `<Name>` line", at the step where it applies. A deviation is an instruction that, under the same trigger, requires an action the block line forbids or forbids an action the block line requires **(definition is an inference)**. A skill that assigns work to the coordinator states which work the coordinator does itself; the Role line provides for this, so it is not an exception. | Decisions 19 and 28; W13 F5 | Review: compare each instruction with the nine block lines. Pass: every deviation carries the exception wording (examples: `status` for the Saving line, `batch` for the Decisions line), and coordinator work is stated in `## Establish` (examples: `status`, `explore`). |
| T14 | Each exception under T13 has a recorded user decision in the owning spec. **(inference)** | Practice in decisions 19 and 28, and in the `setup` spec | Review. |

## 6. References and file layout (L)

Sources: ADR 20261111 (decision 13), decision 14 (P-a, P-b), spec S2, S3, S6, AC10, AC14,
`AGENTS.md`.

| ID | Rule | Source | Check |
| --- | --- | --- | --- |
| L1 | A reference linked from 2 or more `SKILL.md` files lives in `plugins/lusona/references/`. A reference linked from exactly 1 lives in `plugins/lusona/skills/<skill>/references/`. | ADR decision 1-2 | Script: `reference`. |
| L2 | A skill uses a reference only when its own `SKILL.md` links it directly. No reference links another reference. The script reports only reference-to-reference links; current references link skills, templates and the helper scripts. | Decision 14 (P-a) | Script: `reference`. |
| L3 | A plugin-level file is named only by a Markdown link that resolves from the linking file: `[x](../../references/x.md)` from a `SKILL.md`, `[x](references/x.md)` for the skill's own reference. A bare path to a plugin-level file is rejected. | ADR decision 3 | Script: `bare-path`. |
| L4 | A change that moves a reference's use count across 1 and 2 moves the file and rewrites every relative link in it and to it, in the same change. | Decision 14 (P-b) | Script: `reference` and the package link check report the resulting state. |
| L5 | Every rule that does not apply to every task lives in a reference. Each `SKILL.md` that links a reference links it at least once in a trigger sentence: "Before `<action>`, read `[x](...)`" or "When `<condition>`, read `[x](...)`". | S2, AC14, V1 | Script: `reference` (trigger word present). Review: the trigger names the action the reference governs. |
| L6 | Each trigger a reference names for itself is named by at least one `SKILL.md` that links the reference, or by the every-task block. For a per-skill reference, that `SKILL.md` is its own skill's. | W13 F3, F8, F11, F22 | Review: list the triggers in the reference's opening line. For each, find a sentence in a `SKILL.md` or in `shared/every-task.md` that links the reference under that condition. Pass: none is missing. |
| L7 | No `SKILL.md`, reference or shared text links or names the plugin README as required reading. The plugin README is human documentation and a catalog. | S3, AC10, decisions 3 and 21 | Script: `readme`. |
| L8 | A reference opens with its H1 and one line that states when to read it ("Read before ...", "Read when ..."). **(inference)** | All 23 current references do; W13 F3 cites the line | Review. |
| L9 | A skill does not depend on a rule that exists only in another skill's `SKILL.md`. A rule 2 skills need lives in a shared reference or in the block. A reference is not named in prose without a link. | W13 F12; V8 | Review. |
| L10 | For each record operation in its steps, the skill links the reference that owns that operation in a trigger sentence: locating records or reading a record from an earlier plugin version, [files](../plugins/lusona/references/files.md); creating or naming a record or running the helper (the queue file included), [naming](../plugins/lusona/references/naming.md); creating or updating a spec or queue row, [queue](../plugins/lusona/references/queue.md); saving findings, evidence or a handoff, [retention](../plugins/lusona/references/retention.md). | W13 F9, F10; AC9 | Review. |
| L11 | Bundled resources resolve relative to the loaded skill. A `docs/lusona/` path in plugin text means the consuming project. No packaged file links to `shared/`, `docs/` or `scripts/` at the repository root. | `AGENTS.md`; S6; ADR decision 4 | Script: package build (links). Review: `docs/lusona/` paths. |
| L12 | The skill catalog table and the routing table exist once, in `references/workflow-guide.md`. A new skill has one row in the Skills table (persona and responsibility, output with its template link) and one row in the Routing table **(inference for the two rows)**. | `check_instructions.py`; `setup` spec AC1 | Script: duplication. Review: both rows exist for the new skill. |
| L13 | A new reference has one row in the References table of `plugins/lusona/README.md`. A new template has one entry in its Templates list. **(inference)** | The README lists all 23 references and 14 templates | Review. |

## 7. Voice (V)

Scope: text in `SKILL.md` files, references, shared blocks and templates. Sources: spec
20261111 "Skill voice (accepted)", decisions 7, 12 and 26; voice decisions 1-21;
`scripts/check_voice.py`.

| ID | Rule | Check |
| --- | --- | --- |
| V1 | Write instructions in the imperative, addressed to the agent, with the trigger stated: "When X, do Y"; "Before X, read Z". | Review: each instruction sentence (a sentence that tells the agent to do or not do something; this definition is an inference) starts with a verb or a trigger clause. A declarative sentence that states a requirement in the form the every-task block uses ("X requires Y", "X needs Y", "X does not authorize Y") passes **(revised 2026-11-13)**. A sentence with "can" or "may" grants a permission and states its condition; it is not used to give an instruction (W13 F19). |
| V2 | Lead with the action. No preamble. Do not restate the skill's purpose inside instruction text. | Review: outside the Persona fields, no sentence restates the skill's purpose or says what the skill adds. A sentence that sets the skill's scope or authority passes, whatever its verb: `explore/SKILL.md:48` "Exploration needs no earlier skill."; `setup/SKILL.md:47` "Setup is not implementation and needs no TDD level for itself." **(revised 2026-11-13, user decision)**. Voice pass round 3, class D, deleted one sentence of the failing kind from `batch` ("This skill adds coordination; ..."), with repetition as its stated basis. |
| V3 | One instruction per sentence where possible. | Script: no sentence over 40 words. Review: a sentence joined by semicolons holds one rule. |
| V4 | One term per concept. Use the terms in the [Terminology table](../plugins/lusona/references/workflow-guide.md#terminology). Do not introduce a synonym. A new concept gets a row in that table. | Review. Pass when all hold: for each concept that has a row in the table, the addition uses the table's term and no synonym; a term the addition defines for itself has one meaning throughout the addition; link text or a table label that names a bundled file is a label, not a term **(revised 2026-11-13)**; none of the replaced terms in VP5 occurs. A term that 2 or more files use gets a row in the table **(inference from voice decision 11)**. |
| V5 | State conditions instead of hedges: "when", "unless", "only when". | Script: `TERMS`. |
| V6 | Plain, literal language. No idioms, metaphors or analogies. Do not attribute intent to code. No filler adjectives or verbs. Precise technical terms are allowed. | Script: `TERMS` (filler words). Review: idioms, metaphors, intent attributed to code. |
| V7 | Numbers instead of vague intensifiers ("at most 2 correction rounds", not "a few"). | Review: every quantity word has a number or a stated limit. |
| V8 | Each shared policy has one authoritative definition. Other files link it. A short local repeat is allowed when it makes the skill easier to execute. No reference chain hides the action. | Review: search the plugin for each number, limit and defined term the addition states. Pass: one file defines it; other skills and references link that file (W13 F7). A template may repeat a short rule without naming the defining reference, and the repeat agrees with the definition: `work.md.template:31` repeats the Ready rule of `queue.md`, and `spec.md.template:38` lists the TDD levels of `tdd.md`. A template that names the reference names it in plain text, because G2 forbids the link **(revised 2026-11-13, step 8)**. Each example agrees with the rule it illustrates (W13 F17). |
| V9 | No rationale in instruction text unless it changes the action. Rationale belongs in specs and ADRs. | Review: no "because" or "so that" clause that could be deleted without changing what the agent does. |

Measurable limits (decision 12; voice decisions 1-4, 5, 14):

| ID | Limit | Check |
| --- | --- | --- |
| VL1 | No term from `TERMS` in `scripts/check_voice.py`. The list is kept in the script so that plugin text never names the banned words. Prose, headings, table cells, block quotes, HTML comments, link text and the frontmatter `description` are scanned. Fenced code, inline code and link targets are not. | Script. |
| VL2 | A file's average is at most 15 words per sentence (`DEFAULT_MAX_AVG_WORDS`). Sentences are counted in prose only: the frontmatter (the description included), fenced code, headings and table rows are excluded. | Script. |
| VL3 | No sentence has more than 40 words (`DEFAULT_MAX_SENTENCE_WORDS`), counted as in VL2. | Script. |
| VL4 | Templates are scanned for banned terms only. | Script. |
| VL5 | Not banned: `may` as a permission, `can`, and `should` or `might` inside example dialogue. Example dialogue stays as a person would say it. | Voice decision 1. |

Rules from the voice pass (decision 26; voice decisions 5-21; rounds listed in
[notes/voice-pass](lusona/notes/voice-pass/)):

| ID | Rule | Check |
| --- | --- | --- |
| VP1 | A qualifier needs a stated test. A word that asks the agent to judge without a criterion is replaced by the test, or deleted. Words the pass treated this way: substantive, applicable, adequate, sufficient, insufficient, meaningful, credible, safe, unsafe, disposable, ordinary, normal, expensive, oversized, broader, fresh, necessary, unnecessary, unneeded, clear (of work or a request), ready (as a condition), "when allowed", and the size words small, short, brief, concise, compact, minimal, large, several. | Review: for each use of a listed word in the addition, name the line that states its test. Pass: a line exists, or the word is one of the defined terms in VP2. The list is the audit scope; the pass did not claim it is complete (section 13). |
| VP2 | Defined qualifiers are used only in their defined sense: `substantive` (defined in `references/retention.md`, "When to save"), material evidence (`references/evidence.md`) and material progress (`references/corrections.md`). | Review. |
| VP3 | A size word is replaced by a limit the text states ("one-sentence", "one or two sentences") or deleted. | Review. |
| VP4 | An edit to existing text keeps the trigger, action and scope of the original. An edit that changes a condition or criterion, or that sets a criterion no line of the plugin states, needs the user's decision. | Round 1 (23 edits reverted); voice decisions 13 and 16. Review: item D2, which does not compare the time of the edit with the time of the decision **(revised 2026-11-13, step 8)**. |
| VP5 | Replaced terms are not reintroduced: "repair allowance" (now "repair budget"); "lifecycle state" of a queue item (now "queue state"); "separate plan", "companion plan", "split records" (now "execution record"); "TDD policy" (now "TDD level"). | Review: the VP5 command below returns only the "lifecycle states" line of `references/delegation.md`, which names leaf lifecycle. |
| VP6 | A sentence that repeats a rule stated completely elsewhere is deleted. A numbered step that names an action which a practice of the same file defines is not such a repeat **(revised 2026-11-13, user decision)**. | Review, with V8. |
| VP7 | The first sentence of a description states the action; the output is named in the first or the second sentence **(revised 2026-11-13)**. Description wording is literal. The pass split the 3 first sentences that held more than 30 words; no decision sets 30 words as a limit. | Voice pass round 2, class H. Review. |

VP5 command:

```bash
grep -rniE 'repair allowance|lifecycle state|separate plan|companion plan|split records|TDD policy' plugins/lusona
```

## 8. Shared text (B)

Sources: decisions 13, 15-17, 20, 26, 28, 29; `CONTRIBUTING.md` "Edit the text that every skill
shares"; `scripts/sync_shared.py`.

| ID | Rule | Check |
| --- | --- | --- |
| B1 | The every-task block and the final reply are edited only in `shared/every-task.md` and `shared/final-reply.md`. The regions in each `SKILL.md` are generated by `python3 scripts/sync_shared.py --source shared plugins/lusona`. The source and the regenerated files are committed together. | Script: sync `--check`. |
| B2 | `shared/every-task.md` holds at most 300 words by `wc -w` (293 on 2026-11-13). | Script: sync. |
| B3 | The block holds every rule that applies to every task, and a skill needs no other file to apply those rules (S1). The block links only references whose trigger can occur in every skill (now `delegation`, `revisions`, `tdd`, `retention`). | Decision 16 (A3). Review. |
| B4 | The two regions together name every TDD level in backticks (`none`, `targeted`, `strict`), the four reply statuses (Complete, In progress, Needs input, Paused) and the sentence that specs, plans, ADRs and queue states do not authorize implementation. | K4. Script: `check_contract.py`. |
| B5 | Links in shared sources are written as a `SKILL.md` needs them (`../../references/x.md`). `shared/` is not packaged. | ADR decision 4. Script: package build. |
| B6 | A change to shared text is a rule change for all 15 skills. It needs a user decision recorded in the owning spec, and each skill's stated exceptions (T13) are re-read against the new text. | Decisions 17, 20, 28 and 29 each record one. Review. |
| B7 | An addition that is not a shared-text change leaves `shared/` unchanged. | `setup` spec AC10 **(inference)**. Review: `git status --short -- shared` and `git diff --stat <base> -- shared` are empty. |
| B8 | A skill that adds content to its reply states where the content goes relative to the form. It does not remove Result, Evidence, the status word or the next action. | Decision 29. Review. |
| B9 | A new shared block has a source `shared/<name>.md` and its marker pair in every `SKILL.md`. | `CONTRIBUTING.md`. Script: sync. |

## 9. Public contract (K)

Source: spec 20261111, "Accepted constraints and invariants", decisions 2, 8, 9; baseline commit
`34186da`. An addition does not change a contract item. A change to one needs a user decision.

| ID | Contract item | Check |
| --- | --- | --- |
| K1 | The 14 baseline skill names and `/lusona:<skill>` invocation stay. No skill is removed or renamed. New skills may be added (decision 9). Descriptions and triggers may change. | Script: `check_contract.py` for the 14. Review: T1 for a new skill. |
| K2 | Project data layout: `docs/lusona/` paths `work.md`, `specs/`, `adr/`, `notes/`, `evidence/`, `history/`, `product.md`, `plans/`, `batches/`, `visuals/`, `README.md`; `YYYYMMDD-slug` record IDs; queue states Ideas, Ready, Doing, Review, Done, and Icebox. Each is defined in `files.md`, `naming.md` or `queue.md`. | Script: `check_contract.py`. Review: the addition writes no new path under `docs/lusona/` without a recorded decision. |
| K3 | Record helper: commands, arguments, JSON fields, statuses and exit codes of `work-record.sh` and `work-record.ps1`, including the legacy `next-adr` and `next-change`. Both helpers have the same commands, arguments, statuses and exit codes. No baseline line of the two test files is removed. The helpers need no Python. | Script: `check_contract.py`; both helper test files. Review for a new command: it exists in both helpers, has cases in both test files, and has a row in the Commands table of `references/naming.md`. |
| K4 | Behavior vocabulary: TDD levels `none`, `targeted`, `strict`; reply statuses Complete, In progress, Needs input, Paused; specs, plans, ADRs and queue states do not authorize implementation. | Script: `check_contract.py`. |
| K5 | Manifest identity: plugin name `lusona` in the native manifests and catalogs. Manifest versions are equal. The version changes only when the user requests it. | Script: `check_contract.py`, package build. Review: `git diff <base> -- '*plugin.json' '*marketplace.json'` shows no version change without a request. |
| K6 | No manifest declares hooks. The plugin has no runtime hooks and no runtime Python. | AC15; 20261110 decision 5. Script: `check_contract.py`. |
| K7 | Old records stay usable without migration: a record created from the `34186da` templates, and a legacy `NNNN-slug` record, is read and updated by every skill that reads records. | AC9. Review: L10 for `files`; a new skill does not require a field that only new templates have. |

## 10. Templates and helper (G)

| ID | Rule | Source | Check |
| --- | --- | --- | --- |
| G1 | A template is named `name.ext.template` (for example `spec.md.template`). | Decision 15 (A8) | Review; package build accepts both forms. |
| G2 | A template holds no relative Markdown link into the plugin. A record created from it lives in the consuming project, where the link does not resolve. | Decision 12; W5 results in spec 20261111 | Review: the G2 command below returns nothing. |
| G3 | A Markdown template holds at most 100 lines and no banned term. `.html` templates are exempt from the line ceiling. | S4; voice decision 4 | Script: `size`, `check_voice.py`. |
| G4 | A renamed template field label or heading is listed in the changelog entry. Records from earlier templates stay readable (K7). **(inference)** | CHANGELOG 3.0.0 lists each rename | Review. |
| G5 | A helper command creates a file only when it is absent and never overwrites or merges a record. Agents resolve the helper from the loaded plugin, by the linked script's absolute path. | `references/naming.md` | Script: helper tests. Review for a new command. |

G2 command:

```bash
grep -nP '\]\((?!https?://|#)' plugins/lusona/templates/*.template
```

## 11. Verification and evidence (E)

Sources: spec 20261111 "TDD policy" and AC16-AC19; `CONTRIBUTING.md` "Verify your change" and
"Behavioral evidence"; `AGENTS.md`; `references/delegation.md` "Independent review".

| ID | Rule | Check |
| --- | --- | --- |
| E1 | The change has an explicitly selected TDD level (`none`, `targeted` or `strict`) with its source (user or standing preference), recorded in the owning record. `none` still requires verification. | Review: the owning record states the level, who selected it and when. |
| E2 | Under `targeted` or `strict`, each named test-first behavior has a test observed failing before the implementation exists and passing after. A new or changed check script is also observed failing on a fixture that holds a deliberate break. A setup failure is not a red result. | Review: the record gives, for each named behavior, the failing result and the passing result, with the test or assertion count where the runner prints one and the exit code and last output line where it prints none **(revised 2026-11-13)**. |
| E3 | Wording and principles are not test-driven. They are verified by review against sections 4 and 7 and, when the text changes agent behavior, by behavior trials. | Spec "TDD policy". Review: the owning record names a review of the addition's wording (an independent review, or an audit with this document) and, when the text changes agent behavior, the trials. A recorded result for each of V1-V9 is not required **(revised 2026-11-13, step 8)**: the rewrite records script checks only for the text of decisions 28 and 29. |
| E4 | Behavior trials follow `CONTRIBUTING.md` "Behavioral evidence": cases, outcome criteria, pass marks, hosts, budget and stopping condition are declared before the trials; a baseline is pinned when a comparison is claimed; grading is independent of the actor; every outcome is reported, including failed and unrun trials. A pass mark is required when a case is repeated and the claim is a rate (decisions 19 and 23: "4 of 5 trials"); for trials that run once, the criteria declared for each check are sufficient **(revised 2026-11-13, user decision)**. Matched baseline and candidate evidence is required for a change to authority, TDD, completion, trust, persistent data or cross-worker ownership. A new skill without a baseline may use candidate-only trials **(inference from one decision, `setup` spec D12)**. | Decisions 19 and 23; `setup` spec D12. Review: the evidence record holds the declaration dated before the first trial. |
| E5 | Independent review is required when user or repository rules require it, or when the change affects security boundaries, persistent data or shared contracts, or has multiple coordinated writers. Shared text and the contract items K1-K7 count as shared contracts **(inference)**. The reviewer wrote none of the change and receives the spec, the diff and the check output, without the author's conclusions. Blocking findings are corrected and re-verified; in W13 a leaf that wrote none of the corrections re-verified them. | AC17; W13; `delegation.md`. Review: the record names the reviewer (the person, or the agent and its model), states that the reviewer wrote none of the change, and records the re-verification of each blocking finding. |
| E6 | The report names each check that was not run, and states when installation or interactive behavior was not tested. A package build does not establish host integration. | `AGENTS.md`; P5. Review. |
| E7 | Every current listing of the skills and every current skill count is updated: Skills and Routing tables in `workflow-guide.md`; `README.md` and its 4 translations; `INSTALL.md`; `CONTRIBUTING.md`; manifest and catalog descriptions; `plugins/lusona/assets/workflow-loop.svg`; the current `CHANGELOG.md` entry. Dated records and dated statements keep their counts. **(inference)** | `setup` spec AC1 and its review finding R7. Review: read the count and the skill list in each named file. The E7 commands below are a search aid for English counts; they do not match the translations. Pass: every count of the current plugin is the current number; a count of a subset ("the other 12 skills") equals the current number minus the skills the sentence names; a count in a sentence about an earlier step or a dated check stays. |
| E8 | The Spanish, German, Simplified Chinese and Japanese READMEs change together with `README.md`. | `CONTRIBUTING.md`. Review. |
| E9 | A new skill has a discovery test and a linked-resources test in `scripts/test_package.py`. **(inference)** | The two skills added after the first release, `design` and `setup`, each have both tests. Review. |

E7 commands (digit counts, then spelled-out counts):

```bash
grep -rniE '1[0-9] (skills|.SKILL)' README*.md INSTALL.md CONTRIBUTING.md CHANGELOG.md plugins/lusona .claude-plugin .agents .cursor-plugin .antigravity-plugin
grep -rniE 'thirteen|fourteen|fifteen|sixteen' README*.md INSTALL.md CONTRIBUTING.md CHANGELOG.md plugins/lusona .claude-plugin .agents .cursor-plugin .antigravity-plugin
```

## 12. Process and records (D)

| ID | Rule | Source | Check |
| --- | --- | --- | --- |
| D1 | The addition has an owning record. A spec and its queue row are required when the skill in use defines changes in a spec (`specify` does), when the change needs independent review because of what it affects (E5), when the user asks for one, or when a spec already exists. | `references/retention.md` | Review. |
| D2 | Every change of rule meaning is listed and has a user decision: a new criterion, a changed condition, a removed rule, an exception to a block line. A change without a decision is a finding until the user decides or the change is reverted. | Decisions 18 and 29; voice decisions 13 and 16 | Review: the owning record lists each one with the decision, its date and its source. The check does not compare the time of application with the time of the decision **(revised 2026-11-13, step 8)**: decision 29 accepted a sentence that was already in the working tree, and voice pass round 1 reverted 23 applied edits that had no decision. |
| D3 | When the addition contradicts an accepted decision, the decision is revisited with the user. The superseded or revised decision is marked in the record that owns it, with date and source, and keeps its rationale. | P3, P4; decisions 28 and 29 show the form | Review. |
| D4 | A change that moves or deletes existing rules gives each rule a destination or a removal reason. | AC13 | Review; `check_rule_inventory.py` for rules in the `34186da` inventory. |
| D5 | Edit canonical sources under `plugins/lusona/`. Do not edit generated packages. Keep scratch files and package output in repository-level `tmp/`. | `AGENTS.md`; `CONTRIBUTING.md` | Review: every file in `git status --short` is named in the scope of the owning record, or is a development record of the change under `docs/lusona/`. No scratch file lies outside `tmp/`. |
| D6 | No commit, push or publication without the user's request. Commits use Conventional Commits with a body that explains why. | `AGENTS.md` | Review. |
| D7 | The changelog describes the addition in the current version entry. | `setup` spec; CHANGELOG 3.0.0 | Review. |

## 13. Known gaps in enforcement

These are not rules. Each is a place where a script or a record does not cover a rule above.
An auditor checks the affected items by review.

- `check_contract.py` keeps `SKILLS` and `COMMANDS` at baseline `34186da`. `setup` and
  `init-queue` are not guarded (Ideas row in the [work queue](lusona/work.md)).
- No script compares a new skill's frontmatter `name` with its directory name (T1).
- `check_voice.py` covers V5, V6 filler words and the sentence limits only. V1-V4, V7-V9 and
  VP1-VP7 depend on review. The round 4 word sweep used a fixed word list and does not claim
  that no other word without a test remains.
- The trigger check (L5) accepts any sentence with a trigger word. L6 depends on review.
- The skeleton states that each practices item has a trigger and an action. Current skills hold
  unconditional items (for example `investigate`), so T6 requires a condition only for a
  conditional item.
- The Terminology table has 16 rows. Terms that every skill uses, such as "owning record" and
  "work queue", have no row.
- The skeleton asks for 2 to 5 failure modes. `architect` and `specify` hold 6 and `setup`
  holds 8. No decision or script sets a limit, so this document sets none.
- `check_contract.py` lists Icebox in `QUEUE_STATES`. `references/queue.md` and the Terminology
  table describe Icebox as a section of the queue, not a queue state (voice decision 15).
- No loop-conformance run and no independent review cover the text after the voice pass
  (decision 27). The AC18 run met 12 of 13 pass marks on each host; the 2 misses are Ideas rows in the
  work queue (decision 25).
- Loading from an installed Codex plugin, and a trigger reached late in a long task, were not
  tested in the layout experiment (ADR, "Verification implications").
- L6 does not say which references the auditor of an addition lists: the ones the addition
  adds or changes, or all of them. For `setup` both scopes give the same result, because the
  addition changes no opening line of a reference and no `SKILL.md` of the 14 skills.
- 19 results of the first audit of `setup` on 2026-11-13 carried a second reading. Step 8 of
  section 1 was applied to P8, V2, V8, E3, E4, D2, T11 and VP6 on 2026-11-13, and their pass
  conditions are reworded.
- No item covers an addition that fails one of its own acceptance criteria or a recorded
  decision. Step 6 makes such a result a `non-blocking` finding with "no item".
- T13 does not say whether an exception to a block line also covers a reference line that
  gives the same instruction. For `setup`, the user decided that `references/tdd.md:11`
  ("recommend a level") governs the level of a change and not a standing preference (`setup`
  spec, D33).
- Two of the 14 skills of 3.0.0 lack a next-action item for a case they reach (P8).
  `skills/review/SKILL.md:45` asks the user about an ambiguous scope, and its list has no item
  for a missing input. `skills/batch/SKILL.md:110` names the outcome "all selected complete",
  and its list has no item for a complete scope. An Ideas row in the
  [work queue](lusona/work.md) holds the correction.
- `references/interviews.md` says "ambition" where `skills/frame-product/SKILL.md` says
  "vision" (voice decision 16).

## 14. Sources and limits

Read for this compilation: spec 20261111 in full; ADR 20261111; the voice limits notes; the
drafting notes (`README.md`, `skill-template.md`); the W13 review notes; `AGENTS.md`;
`CONTRIBUTING.md`; `shared/`; the docstrings and constants of the six check scripts and
`package.py`; the acceptance criteria and template of spec 20261110; `references/retention.md`,
`naming.md`, `delegation.md`, `workflow-guide.md`. Two leaves extracted the facts of the `setup`
addition (spec 20261112, its evidence README and the working-tree diff) and the edit classes of
the four voice-pass rounds; the voice-pass rounds were read by headings and sampled rows, not
row by row.

Not read: the 1,819-line rule inventory; specs before 20261110; the evidence directories.

Checks run by the compiler on the working tree on 2026-11-13, all exit 0: `sync_shared.py --check`,
`check_voice.py`, `check_skill_template.py`, `check_instructions.py`, `check_contract.py`,
`check_rule_inventory.py`, `python3 -m unittest discover scripts` (231 tests), the
loop-conformance unit tests (150 tests), `package.py` (built `lusona-3.0.0.zip`). Reported by the
trial-audit leaf, not rerun by the compiler: `bash scripts/test-work-record.sh` exit 0 and the
PowerShell helper test exit 0 (203 assertions, PowerShell 7.6.10 through `mise exec`). Not run:
`claude plugin validate`, `agy plugin validate`, any agent trial.

Trial audit: a reviewer leaf that did not write this document used an earlier version of it to
audit the `setup` addition, and reported 26 defects in the document (commands that missed
files, items without a determinate result, pass conditions that current skills do not meet).
The corrections are in this text. A second leaf then ran the full audit of `setup` on the
corrected text on 2026-11-13: 10 findings, 19 results that depend on the reading, and 8 items
it could not apply as written. Six pass conditions and the severity rule were revised after
that audit (intro, "Revised on 2026-11-13"); a third leaf applied four of the revised
conditions (P2, T6, V1, VP7) to changed passages of `setup`. No full audit has run with the
revised conditions, so no check shows that every item gives two auditors the same result.
Step 8 of section 1, the rule for the result of an audit, was added on 2026-11-13. A fourth
leaf, which wrote neither this document nor the addition, searched the 14 skills and the
templates at `6243701` for passages that fail the stricter reading of P8, V2 and V8. It found
such passages for P8 and V8 and none for V2. For E3, E4 and D2 it collected what the records of
the rewrite show: they do not meet the stricter reading of E3 and D2, and they meet the stricter
reading of E4. The compiler read each cited passage and record before rewording P8, V8, E3 and
D2. The user decided V2 and E4, and later T11 and VP6. Two reads of changed `setup` passages
applied the conditions as they were worded at the time of each read. No full audit of an
addition has run with the reworded conditions, and no reader other than the compiler has
reviewed the reworded sentences.
