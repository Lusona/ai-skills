# Spec 20261112-add-setup-skill: Add a setup skill

Created: 2026-11-12
Updated: 2026-11-13

Kind: feature
Work item: [Historical completion](../history/2026-11-week-02.md#2026-11-12--add-setup-skill)
Context: none; no issue or ticket was supplied

## Agreement

- User and problem: a person who installs Lusona in a project. Today no step creates the
  record directory and the queue, and the project's agent instructions do not say that the
  project uses Lusona. Reported, not reproduced: an agent handles a task without invoking a
  Lusona skill ("It's rare, but GPT doesn't invoke lusona skills"). Each session asks again
  for the TDD level and the model tier mapping.
- Desired behavior:
  - A `setup` skill creates `docs/lusona/` and `docs/lusona/work.md` in the consuming project.
  - Setup proposes one Lusona section for the project's `AGENTS.md` and, where needed, a
    one-line reference to `AGENTS.md` in `CLAUDE.md`. It writes them after the user confirms.
  - The section says that the project uses Lusona skills, how to invoke them, where the
    records are, and the standing TDD preference and model tier mapping the user gave.
  - Setup's reply suggests next steps.
  - Setup is optional. No other skill asks for it, requires it or stops for it; a skill
    creates the records its work needs (D9).
- Scope:
  - The new `setup` skill.
  - An exception for setup in the rule text of `files.md` line 10 (D9).
  - The workflow guide Skills and Routing tables, the plugin README catalog and `INSTALL.md`.
  - The English, Spanish, German, Simplified Chinese and Japanese READMEs.
  - Manifest and catalog descriptions, and skill counts where a file states one.
  - `CHANGELOG.md`, and the repository tests and checks.
- Exclusions:
  - Startup hooks or any automatic run at installation.
  - Migration of legacy records.
  - `docs/lusona/README.md`, `product.md` or any record other than `work.md` (A4).
  - `GEMINI.md`, `.cursor` rules and other host-specific instruction files.
  - A plugin version bump. Source: standing user preference, version bumps only on request.
  - Commits made by setup.
  - Measuring whether the section changes how often Codex invokes Lusona skills (A7).
- Accepted constraints and invariants:
  - Repository `AGENTS.md`: canonical sources live in `plugins/lusona/`. The every-task block
    and the final reply are edited only in `shared/` and regenerated with
    `python3 scripts/sync_shared.py --source shared plugins/lusona`. Each shared policy has one
    authoritative definition. Resource paths resolve relative to the loaded skill. Manifest
    identity and version stay aligned. Packages exclude project data.
  - `CONTRIBUTING.md`: the five READMEs stay in sync. Instructions that change skill behavior
    need behavioral evidence. Consequential shared boundaries, including persistent data and
    authority, need matched baseline and candidate evidence.
  - [ADR 20261111-skill-file-layout-and-shared-sources](../adr/20261111-skill-file-layout-and-shared-sources.md).
  - [files](../../../plugins/lusona/references/files.md), Ownership: setup never writes
    consuming-project data into installed plugin resources.
  - `scripts/check_contract.py` checks that no manifest declares hooks.
  - Setup selects no TDD level for any change and authorizes no implementation.
- Completion condition: AC1–AC10, AC12 and AC13 are met, the repository checks pass,
  behavioral evidence is recorded as `CONTRIBUTING.md` requires, and independent review is
  done. Independent review is required by
  [delegation](../../../plugins/lusona/references/delegation.md): the new skill writes
  persistent project data and agent instructions. The evidence names the host and interactive
  checks that were not run. No human acceptance or delivery step is required beyond these
  unless the user adds one.

### Acceptance criteria

- [x] AC1: `setup` is available through native skill discovery and in the portable package,
  and its linked resources resolve. The workflow guide Skills and Routing tables, the plugin
  README catalog, `INSTALL.md`, the five READMEs and the manifest and catalog descriptions list
  it accurately, including each skill count stated as current. Dated verification records, such
  as the "thirteen skills" observations in `INSTALL.md`, keep their observed counts. Manifest identity and version alignment
  and project-data exclusion are preserved. The plugin version is unchanged.
- [x] AC2: In a project without `docs/lusona/`, setup creates `docs/lusona/` and a
  `docs/lusona/work.md` whose content equals the bundled queue template. It creates no other
  file under `docs/lusona/` (A4, A6).
- [x] AC3: When `docs/lusona/work.md` or other files under `docs/lusona/` exist before setup
  runs, each stays byte-identical, and setup reports them as existing.
- [x] AC4: Before it writes `AGENTS.md` or `CLAUDE.md`, setup shows the exact text and the
  target paths and waits for the user's confirmation. When the user declines, setup writes
  neither file and reports that. The AC2 result is the same in both cases (A6).
- [x] AC5: Revised 2026-11-12 by D11. After confirmation, `AGENTS.md` holds exactly one Lusona
  section; setup creates the file when it is missing. The section states:
  - that the project uses Lusona skills;
  - that the agent invokes the appropriate skill with the host's syntax: `/lusona:<skill>`
    in Claude Code, `$lusona:<skill>` in Codex CLI, and either form in the Codex desktop app
    (D13);
  - that records are under `docs/lusona/` and the queue is `docs/lusona/work.md`, except when
    the user declined creating `docs/lusona/` in a project with legacy records; the section
    then has no such line;
  - the standing TDD preference, when the user gave one;
  - the model tier mapping, when the user gave one.

  All text outside the section is byte-identical to the text before setup ran, apart from one
  newline byte when the file did not end with one.

  Text before the revision: the third item read "that records are under `docs/lusona/` and the
  queue is `docs/lusona/work.md`;", the second "`/lusona:<skill>`, and `$lusona:<skill>`
  subject to Q1;", and the last sentence had no newline exception.
- [x] AC6: Revised 2026-11-12 by D11 and 2026-11-13 by D25. Setup asks for the standing TDD
  preference and for the model tier mapping, except for a value that is already recorded in
  `docs/lusona/README.md` or in agent-instruction text outside the section: setup shows that
  value and its location, does not ask for it and writes no second copy. When the section and
  at least one other location hold a value, setup shows each value with its location, the
  user chooses which location keeps it, and setup removes the section's line only on that
  choice. The section holds only the values the user gave; a declined item is absent (A5).
  The user gave a value when the user stated it or chose it from the values the question
  named (D24). In a later session in the same project, a skill that needs the TDD level uses
  the recorded level, names `AGENTS.md` as its source and does not ask for it.

  Text before the revision of 2026-11-12: "Setup asks for the standing TDD preference and for
  the model tier mapping." without the exception. Text before the revision of 2026-11-13: the
  criterion without the sentence "When the section and at least one other location ..." and
  without the sentence "The user gave a value ...".
- [x] AC7: Revised 2026-11-12 by D10. When `CLAUDE.md` is missing, or holds no `@` import of
  `AGENTS.md` and is not the same file through a symbolic link, setup proposes the one line
  `@AGENTS.md` under the AC4 confirmation. A `CLAUDE.md` that already imports `AGENTS.md`
  stays byte-identical. A prose mention of `AGENTS.md` is not an import.

  Text before the revision: "When `CLAUDE.md` is missing or does not reference `AGENTS.md`,
  setup proposes a one-line reference to `AGENTS.md` under the AC4 confirmation. A `CLAUDE.md`
  that already references `AGENTS.md` stays byte-identical."
- [x] AC8: A second setup run in the same project adds no second Lusona section and no second
  reference. A preference value the user changed replaces the old value inside the section.
  `docs/lusona/work.md` stays byte-identical.
- [x] AC9: Setup's final reply lists the created, changed, unchanged and declined files. It
  names at least one next action from the workflow guide Routing, with its skill prompt in the
  host's invocation syntax. The reply authorizes no work, and setup makes no commit.
- [x] AC10: Revised 2026-11-12 by D9. No existing skill asks about setup, requires it or stops
  for it. In a project without `docs/lusona/`, a skill continues the requested work and creates
  the records that work needs, as before this change. `shared/every-task.md` and the 14
  existing `SKILL.md` files are unchanged by this change.
- AC11: withdrawn 2026-11-12 by D9. Earlier text: "When the user declines the AC10 permission,
  the skill continues the requested work, creates only the records that work needs, and does
  not ask again in the same session (A1). As a leaf, a skill neither asks the user nor runs
  setup; its result reports the missing setup to the coordinator (A3)."
- [x] AC12: Revised 2026-11-12 by D9. In a project that has legacy records such as
  `docs/agent/` and no `docs/lusona/`, a setup that the user invokes reports the legacy
  records, asks before it creates `docs/lusona/` and leaves the legacy records byte-identical
  (A8).
- [x] AC13: Revised 2026-11-12 by D9. `files.md` names setup as the case in which the queue is
  created before work needs it. `retention.md` line 92 and `status/SKILL.md` line 54 keep their
  statements. The plugin text, `INSTALL.md` and the five READMEs state that installation
  creates no project documents, that setup is optional and that no skill requires it.

### Decisions and uncertainty

Accepted decisions. Source for each, unless stated: user, 2026-11-12, native question tool.

- D1, revised in part 2026-11-12 by D9; the text below is the decision as first recorded:
  Setup is the expected first step in a consuming project. This supersedes parts of three
  rule texts and revises one statement. The statement that installing the plugin creates no
  project data is kept.
  - Conflict: the request asks for a setup that creates `docs/lusona/` and `work.md` before
    any work needs them. The rule texts below say that records are created only when
    authorized work needs them and that no setup is required.
  - Superseded, 2026-11-12, by this decision; the texts remain in the plugin until
    implementation replaces them (AC13):
    - [files](../../../plugins/lusona/references/files.md) line 10, second sentence: "Create a
      record only when authorized work needs it." The first sentence, "Installing the plugin
      does not create project data.", is kept.
    - [retention](../../../plugins/lusona/references/retention.md) line 92: "Do not create
      project data only for orientation or installation." The orientation part is superseded:
      a skill that finds `docs/lusona/` missing asks to run setup (D4). The installation part
      is kept. This is duplicate group D12 in the
      [rule inventory](../notes/rule-inventory-34186da.md).
    - [status](../../../plugins/lusona/skills/status/SKILL.md) line 54, the clause "do not
      require setup". The clause "assess progress from the available project evidence" is kept.
  - Revised: `INSTALL.md` lines 235–238 ("Installation does not create or migrate project
    documents. ... No startup hooks are required.") gain a statement that names setup.
  - Rationale of the superseded texts: none is recorded. A search of `docs/lusona/specs`,
    `docs/lusona/adr`, the rule inventory, `docs/lusona/history` and `CHANGELOG.md` found only
    the rule texts and their inventory rows.
  - Not superseded: AC4 of [spec 20261031-add-antigravity-support](20261031-add-antigravity-support.md),
    "Installation does not create consuming-project records". Installing the plugin still
    creates nothing. Only a setup that the user invokes or approves creates records.
  - The option the user selected read "A skill that finds docs/lusona/ missing directs the
    user to run setup". D4 replaces that wording with the inline behavior.
- D2: The surface is a new skill named `setup`, the 15th skill; `/lusona:setup` in Claude Code.
- D3: The agent-instruction text has two purposes.
  - The agent stops asking again for the standing TDD preference and the model tier mapping.
    [TDD](../../../plugins/lusona/references/tdd.md) and
    [delegation](../../../plugins/lusona/references/delegation.md) already read both from
    agent instructions.
  - The agent is told that the project uses Lusona skills and that it invokes the appropriate
    skill with `/lusona:` or `$lusona:` commands. Source: the user's free-text answer.
  - The user also selected "No observed problem". Its proposed minimal text was: the project
    uses Lusona, records are under `docs/lusona/`, and the standing TDD preference when the
    user chooses one.
- D4, superseded 2026-11-12 by D9; text as first recorded: A skill that finds `docs/lusona/`
  missing asks the user for permission, performs setup itself in the same session, then
  continues the requested work.
- D5: Setup writes one Lusona section in `AGENTS.md`, created when missing. When `CLAUDE.md`
  is missing or does not reference `AGENTS.md`, setup proposes a one-line reference to
  `AGENTS.md`. Setup shows the exact text and the target files and writes after the user
  confirms.
- D6: TDD level `targeted`; see TDD level below.
- D7: The user accepted AC1–AC13 and A1–A9 and authorized implementation of this spec. Source:
  user, 2026-11-12, chat ("accepted, /lusona:implement 20261112-add-setup-skill").
- D8: Implementation decisions by the coordinator, within routine design authority; they close
  Q2.
  - The missing-setup rule (D4) is defined once in `shared/every-task.md` and synced into
    every `SKILL.md`. Reason: the ADR places every-task rules in each `SKILL.md` from the
    shared source, and the rule applies to every skill.
  - A work-record helper command `init-queue PROJECT_ROOT` creates `docs/lusona/` and
    `work.md` in Bash and PowerShell. Reason: AC2 requires content equal to the bundled
    template, and AC3 requires existing files to stay byte-identical.
  - The `AGENTS.md` section text comes from a bundled template.
  - The first bullet of D8 is withdrawn by D9: no missing-setup rule exists.
- D9: Setup is optional. No skill stops work because a project is not set up, and no skill
  stops work to set it up. Work that requires a record creates the files and directories it
  needs. Source: user, 2026-11-12, chat: "I don't think we should stop work if project isn't
  'setup', and we shouldn't stop work to make sure that it is; most work that requires
  recording should create the appropriate files/directories."
  - Conflict stated: D1 made setup the expected first step and D4 made every skill ask for it.
  - D1 is revised in part. Kept: a `setup` skill exists and creates `docs/lusona/` and the
    queue when the user invokes it. Replaced: "expected first step" becomes "optional". The
    three rule texts D1 listed as superseded are kept: `retention.md` line 92 and
    `status/SKILL.md` line 54 unchanged, and `files.md` line 10 with an exception that names
    setup.
  - D4 is superseded. AC11 and assumptions A1, A2, A3 and A9 are withdrawn. AC10, AC12 and
    AC13 are revised. The D4 trigger part of A8 is withdrawn.
  - Consequence: the every-task block and the 14 existing skills do not change, so the loop
    conformance suite and its stored references are not affected.
- D10: In D5 and AC7, a reference to `AGENTS.md` is an `@AGENTS.md` import, or a `CLAUDE.md`
  that is the same file through a symbolic link; a prose mention is not one. Setup proposes
  the import line otherwise. This confirms A10. Source: user, 2026-11-12, native question
  tool, option "Import only (Recommended)".
- D11: The user accepts both narrowings that the review repairs R2 and R4 made: AC6 (no
  question for a preference already recorded outside the section) and AC5 (no records line
  when `docs/lusona/` was declined in a legacy project). AC5 and AC6 are revised in place.
  Source: user, 2026-11-12, native question tool, option "Accept both (Recommended)".
- D12: Candidate-only behavioral evidence is accepted for this change: the recorded trials
  plus short confirming trials on the final text. The plugin before the change has no setup
  skill to run, and the 14 existing skills are byte-identical. Source: user, 2026-11-12,
  native question tool, option "Accept (Recommended)".
- D13: The section template, the READMEs and the workflow guide keep stating both forms for
  the Codex desktop app as written. Source: user, 2026-11-12, native question tool, option
  "Keep as written". The statement rests on the user's report; no check verified it.
- D14: Five corrections from the skill audit of 2026-11-13 (Evidence, "Skill audit") are
  applied. In `skills/setup/SKILL.md`: the instruction to delete the `- Project records are
  under` list item moves from step 1 to the compose-the-section practice, with the condition
  "the user declined in step 1" and without the clause "because it names `docs/lusona/`"; the
  practice "Both answers are optional. Do not assume a value. Record only what the user
  gave. ..." becomes "Exception to the Questions line: both answers are optional, and setup
  assumes no value for either. Do not invent a level, a model identifier or a mapping." In
  `CHANGELOG.md` and in `README.md` with its 4 translations: `setup` is named as a third
  skill that assigns its work to the coordinator. The exception to the Questions line is the
  wording for A5; its content does not change. TDD level `targeted` stays; wording is outside
  the named test-first behaviors. Source: user, 2026-11-13, native question tool, option
  "Apply all 5 (Recommended)".
- D15: The record helper command `init-queue` (D8, a coordinator decision) is accepted as an
  addition to the helper contract. Source: user, 2026-11-13, native question tool, option
  "`init-queue` helper command". In the same question the user did not select the option that
  confirms the exception to the Saving line (`skills/setup/SKILL.md`, step 8); it stays
  covered by A4 under one reading and has no explicit confirmation.
- D16: The five audit results that depend on pass conditions of `docs/skill-audit.md` (P2,
  T6, V1, V4, E2) and the wording of VP7 are settled by changing the audit document, not the
  addition. Source: user, 2026-11-13, native question tool, option "Change the document
  (Recommended)".
- D17: Decision 28 of spec 20261111 ("the other 12 skills ... assign no work to the
  coordinator") and the sentence in `CHANGELOG.md` and the five READMEs stay as written, and
  `skills/batch/SKILL.md` stays unchanged. Reason: the two rows that `batch` labels
  "(coordinator)" are reconciliation, which
  [delegation](../../../plugins/lusona/references/delegation.md) lists under Coordinator
  duties ("reconcile results"); they are not specialist work that a skill assigns to the
  coordinator. This settles finding 1 of the review of the corrected passages. Source: user,
  2026-11-13, chat, "Conflict with an accepted decision: apply recommendation".
- D18: The exception to the Saving line in `skills/setup/SKILL.md`, step 8, is confirmed. This
  replaces the last sentence of D15. Source: user, 2026-11-13, chat, "Saving exception:
  confirmed".
- D19: The audit document states one result for an addition: `pass`, `fail` or `undecided`
  (`docs/skill-audit.md`, section 1, step 8). A result that depends on the reading takes the
  reading that the 14 skills of 3.0.0 and the records of their rewrite meet; when they meet
  both, the user decides. Source: user, 2026-11-13, chat, "approved, proceed", and native
  question tool, option "Extend to records (Recommended)". Consequence for this item: D2
  (repairs R2 and R4 were applied before D11) and E3 (no result for each of V1-V9 is recorded)
  take the lenient reading and pass, because the rewrite's records do not meet the strict one.
- D20: E4 requires a pass mark when a case is repeated and the claim is a rate. For trials
  that run once, the criteria declared for each check are sufficient. This item's trials pass
  E4. Source: user, 2026-11-13, native question tool, option "Marks for repeated trials
  (Recommended)".
- D21: V2 fails a sentence that restates the skill's purpose or says what the skill adds. A
  sentence that sets the skill's scope or authority passes. `skills/setup/SKILL.md:47` stays.
  Source: user, 2026-11-13, native question tool, option "Only purpose statements fail
  (Recommended)".
- D22: The two P8 misses of the baseline (`review`, `batch`) get one Ideas row in the work
  queue; P8 stays as written. Source: user, 2026-11-13, native question tool, option "Queue
  row to correct both (Recommended)".
- D23: Setup recommends no answer to the two preference questions. This is a second exception
  to the Questions line, stated in the same practice as the first. New text of that practice
  in `skills/setup/SKILL.md`, which replaces the text of D14: "Exception to the Questions
  line: recommend no answer to a preference question. When the user declines it or gives no
  answer, assume no value and record no new one. Do not invent a level, a model identifier or
  a mapping." followed by the sentence of D24. Source: user, 2026-11-13, native question
  tool, option "Recommend nothing (Recommended)". This settles finding 2 of the review of the
  corrected passages, V1 at that line, and the second half of F5.
- D24: "The user gave a value when the user stated it or chose it from the values the
  question named." The sentence ends the practice of D23 and defines "gave" for A5 and AC6.
  The sentence "Record a model only when the user chose it" is deleted. Source: user,
  2026-11-13, native question tool, option "Stated or chosen (Recommended)". This settles F5
  and F7.
- D25: AC6 is revised: when the section and at least one other location hold a value, the
  user chooses which location keeps it. Source: user, 2026-11-13, native question tool,
  option "User chooses the location (Recommended)". This settles the AC6 reading.
- D26: Exact text for three passages of `skills/setup/SKILL.md`. Source: user, 2026-11-13,
  native question tool, option "Approve (Recommended)". The approval is the user decision
  for v3 edits 2 and 3, which had none (F4).
  - The tier-question practice ends: "When the host lists its models, the question may name
    them." (F6).
  - The two-locations practice: "When the section and at least one other location hold a
    value, show each value with its location and ask which location keeps the value. This
    question is the preference question for that value. Remove the section's line only when
    the user chooses another location. When the user gives a new value, replace the section's
    value with it. Leave the text of every other location unchanged. Tell the user each
    location that still holds a value, and that setup changes a value only in the section."
    (F1, F2, F3, P8 for that practice).
  - Step 5: "Compose the section as the practices above describe. Show its text and the
    target paths, and wait for the user's confirmation." (T11, finding 4).
- D27: The Terminology table of the workflow guide gains the rows "Lusona section" and "Model
  tier mapping", and the label in `references/files.md` changes from "Agent-instruction
  section" to "Lusona section" (V4). Source: user, 2026-11-13, native question tool, option
  "Two rows and one label (Recommended)".
- D28: "Legacy records" stays without a test in `skills/setup/SKILL.md` (finding 3). Reason:
  setup reads `references/files.md` before locating them, and a wrong judgment costs one
  extra question. Source: user, 2026-11-13, native question tool, option "Accept as is
  (Recommended)".
- D29: Behavior trials run again after this correction round: 5 trials on Claude Code,
  criteria declared before the first trial, at most 5 USD inside the 25 USD ceiling. Cases:
  two values that differ and the section kept; a new value given to the location question;
  the question names models and the user declines; the user chooses a named model; legacy
  records declined. Source: user, 2026-11-13, native question tool, option "Reduced rerun
  (Recommended)".
- D30: An observation of a reviewer that no audit item covers counts as a non-blocking
  finding of the audit (`docs/skill-audit.md`, section 1, step 6). Source: user, 2026-11-13,
  native question tool, option "Count as non-blocking (Recommended)".
- D31: Rule for further reads of this item: the reader applies the audit items to the changed
  sentences only. Anything else it reports is listed in this spec as accepted, unless it is
  a contradiction between two instructions or a blocking item failure. The rule holds for
  this item and does not change the audit document. Source: user, 2026-11-13, native question
  tool, option "Items on changed text only (Recommended)".
- D32: Two corrections. In the two-locations practice of `skills/setup/SKILL.md`, "When the
  user gives a new value, replace the section's value with it." becomes "When the user gives
  a new value and chooses no other location, replace the section's value with it." (R2-F2).
  In `references/workflow-guide.md:24`, the link label "agent-instruction section" becomes
  "Lusona section", which completes D27 (R2-O6). Source: user, 2026-11-13, native question
  tool, option "Approve both (Recommended)".
- D33: D23 also applies when the user asks which value setup would pick: setup answers that
  it recommends none and explains the levels or the tier criteria. `references/tdd.md:11`
  ("recommend a level") governs the level of a change, not a standing preference. No text
  change. Source: user, 2026-11-13, native question tool, option "D23 applies, no text change
  (Recommended)". This settles R2-F3.
- D34: The other 11 results of the re-read are accepted without a text change: R2-F1, R2-F4,
  R2-F5, R2-O1 to R2-O5 and R2-O7 to R2-O10. The trial rerun of D29 gains a sixth case inside
  the same 5 USD cap: a repeated run on a section with a user's line, which checks that the
  shown text is the written text (R2-F1). Source: user, 2026-11-13, native question tool,
  option "Accept all, add one trial (Recommended)".
- D35: A format example that names a level, such as "for example `targeted` for input
  parsing", is not a recommendation under D23. The two `D23-norec` cells of Amendment 4
  (C14-t1, C15-t1) stay `fail` in the evidence as graded under the locked definition, and the
  behavior is accepted. No text change. Source: user, 2026-11-13, native question tool,
  option "No, accept (Recommended)".
- D36: The two observations of Amendment 4 are accepted without a text change: no
  confirmation is asked when the composed section equals the existing one and nothing is
  written (C12-t1), and the agent's phrase "I recommend no answer for either one" (C15-t1).
  Source: user, 2026-11-13, native question tool, option "Accept both (Recommended)".
- D37: Audit item T11 checks that a step's result and inputs exist; it does not compare one
  step's output with another's. R2-F1 is therefore not a T11 failure and stays accepted
  (D34). Source: user, 2026-11-13, native question tool, option "T11 does not cover it
  (Recommended)".
- D38: Audit item VP6: a numbered step may name an action that a practice of the same file
  defines; a rule repeated in two lines that are not steps, or in another file, fails. Step 5
  of `skills/setup/SKILL.md` passes VP6 (R2-F4). Source: user, 2026-11-13, native question
  tool, option "A step may name a practice's action (Recommended)".
- D39: The two sentences of `skills/setup/SKILL.md:72` on how Claude Code loads `AGENTS.md`
  stay. V9 passes for that line by this decision; the first auditor had put them in the
  class of the rationale clause that D14 deleted. Source: user, 2026-11-13, native question
  tool, option "Keep both sentences (Recommended)".
- D40: The plugin version changes from 3.0.0 to 3.1.0 for this addition. Tag `3.0.0` is on
  origin at the diff base `6243701`, so the changelog gets a 3.1.0 entry that holds the setup
  changes, the 3.0.0 entry returns to its tagged text with the tag date, and the intro names
  3.1.0 as the only untagged version. Source: user, 2026-11-13, chat ("bump version to
  3.1"), and native question tool, option "3.0.0 and the intro (Recommended)".
- D41: `README.md`, its four translations and `INSTALL.md` name `setup` as the optional first
  step in a new project: the section "Start and choose a skill" opens with it, its table row
  is first, and "First use" in `INSTALL.md` opens with it. D9 is unchanged: setup stays
  optional, and no skill requires or asks for it. No file under `plugins/lusona/` changes for
  this decision. Source: user, 2026-11-13, native question tool, options "Setup first,
  optional (Recommended)" and "INSTALL.md First use (Recommended)".
- D42: Clean-up before the commit: this session's scratch under `tmp/` is deleted; the
  withdrawn spec 20261113-capture-project-working-context-during-setup and its exploration
  notes are deleted without a commit; non-essential files of the evidence directory are
  discarded. Source: user, 2026-11-13, native question tool, selections "This session's
  scratch", "Withdrawn spec and its notes" and the typed answer "setup skills evidance
  directory -- discard non-essential files".

Assumptions. The user accepted A1–A9 on 2026-11-12 (D7). D9 withdrew A1, A2, A3 and A9 and
the D4 trigger part of A8 on the same day.

- A1, withdrawn by D9: When the user declines the D4 permission, the skill continues the requested work,
  creates only the records that work needs, and does not ask again in the same session. The
  on-demand creation is the current behavior in
  [retention](../../../plugins/lusona/references/retention.md) and
  [queue](../../../plugins/lusona/references/queue.md). Consequence: when the declined
  session creates no record, `docs/lusona/` stays missing and a skill in a later session asks
  again.
- A2, withdrawn by D9: The D4 trigger is exactly "the `docs/lusona/` directory is missing". A project that has
  `docs/lusona/` but no Lusona section in `AGENTS.md` is not asked.
- A3, withdrawn by D9: D4 applies to all 14 existing skills when the agent is the coordinator, including
  `status`, whose assessment is otherwise read-only. As a leaf, a skill neither asks the user
  nor runs setup; it returns the missing setup to the coordinator. Source: the every-task Role
  rule.
- A4: Setup creates only `docs/lusona/` and `docs/lusona/work.md` from the bundled queue
  template. It creates no `README.md`, `product.md`, `specs/` or other record. Standing
  preferences go in the `AGENTS.md` section only.
- A5: Setup asks for the standing TDD preference and the model tier mapping. Each is optional.
  A declined item is left out of the section. Setup records no value the user did not give.
- A6: Invoking setup authorizes the creation of `docs/lusona/` and `work.md`. The D5
  confirmation covers only `AGENTS.md` and `CLAUDE.md`.
- A7: Measuring whether the section changes how often Codex invokes Lusona skills is not part
  of the completion condition. It can be proposed later as a `measure` follow-up.
- A8: A project that has no `docs/lusona/` but has legacy records such as `docs/agent/`
  ([files](../../../plugins/lusona/references/files.md), Existing records) counts as set up for
  the D4 trigger: no skill asks. A setup that the user invokes there reports the legacy records
  and asks before it creates `docs/lusona/`. Setup does not move, copy or edit legacy records.
- A9, withdrawn by D9: Behavioral trials for AC10–AC12 use a representative set of the 14 skills, justified in
  the evidence as `CONTRIBUTING.md` allows, not one trial set per skill. Proposed set:
  `specify`, `implement` and `status` as coordinator, and one skill as a leaf.
- A10, confirmed by the user on 2026-11-12 (D10): in AC7 and D5, "references
  `AGENTS.md`" means an `@AGENTS.md` import line or a `CLAUDE.md` that is a symlink to
  `AGENTS.md`, and the proposed one-line reference is the import `@AGENTS.md`. Evidence:
  Claude Code memory documentation, https://code.claude.com/docs/en/memory.md, fetched
  2026-11-12: "A `CLAUDE.md` that tells Claude in words to read `AGENTS.md`: Claude sees
  `AGENTS.md` only if it decides to open the file", and "By default, Claude reads `AGENTS.md`
  only when you have no `CLAUDE.md` in your working directory or above it" (version 2.1.277
  or later). A prose mention would leave AC6 unmet on Claude Code. Every write to `CLAUDE.md`
  stays behind the AC4 confirmation.

Questions.

- Q1, answered: Codex CLI uses `$lusona:<skill>`; the Codex desktop app accepts both
  `$lusona:<skill>` and `/lusona:<skill>`. Source: user, 2026-11-12, chat. User-reported; no
  check in this change verified it. `INSTALL.md` documents no Codex command syntax.
- Q2, closed by D8.

- Architecture: [ADR 20261111-skill-file-layout-and-shared-sources](../adr/20261111-skill-file-layout-and-shared-sources.md)
  applies. No new ADR exists for this change.

### TDD level

- Level: `targeted`
- Selected by user: 2026-11-12, native question tool, option "targeted (Recommended)".
- Test-first behaviors, as named in the selected option:
  - the setup skill appears in skill discovery, in the catalogs and in the portable package,
    checked by the repository test scripts;
  - any new helper-script behavior.
- Skill wording is verified by behavioral trials after it is written.
- Required regression coverage: the checks in `CONTRIBUTING.md` "Verify your change" and the
  `scripts/check_*.py` and `scripts/test_*.py` scripts continue to pass. No existing skill text
  changes (AC10).

## Execution

- Approach: D8 as amended by D9.
- Questions put to the user on 2026-11-12 through the native question tool; the user stopped
  the dialog and then gave D9:
  - Skipping the missing-setup question: moot after D9.
  - The loop conformance suite: not affected after D9.
  - Trial budget and hosts: the user's selection in the dialog was "Claude Code + Codex, up to
    $40". After D9 the planned trials cover only the setup skill and stay under that ceiling.
    A Codex trial adds one trust entry per workspace to `~/.codex/config.toml`; back the file
    up before the run and remove the entries after it.

### T1: Helper command `init-queue`, test first

- Acceptance criteria: AC2, AC3.
- Scope: `plugins/lusona/scripts/work-record.sh`, `work-record.ps1`,
  `scripts/test-work-record.sh`, `scripts/test-work-record.ps1`,
  `plugins/lusona/references/naming.md`.
- Verification: `bash scripts/test-work-record.sh`;
  `mise exec powershell@7.6.10 -- pwsh -NoProfile -File scripts/test-work-record.ps1`. Red
  before the helper code, green after.
- Ownership: one leaf, implementation engineer.
- [x] Complete — evidence: T1 under Evidence.

### T2: Setup skill and section template, test first for discovery and package

- Acceptance criteria: AC1, AC4–AC10, AC12, AC13.
- Dependencies: the T1 command contract.
- Scope: `plugins/lusona/skills/setup/SKILL.md` (new), a section template under
  `plugins/lusona/templates/` (new), `plugins/lusona/references/files.md` and
  `workflow-guide.md`, `plugins/lusona/README.md`, `scripts/check_contract.py`,
  `scripts/test_contract.py`, `scripts/test_package.py`. `shared/every-task.md` and the
  existing `SKILL.md` files are not edited.
- Ownership: one leaf, implementation engineer.
- [x] Complete — evidence: T2 under Evidence.

### T3: Public documentation

- Acceptance criteria: AC1, AC13.
- Dependencies: T2 wording.
- Scope: `INSTALL.md`, the five READMEs, `CHANGELOG.md`, `CONTRIBUTING.md` line 49, manifest
  and catalog descriptions.
- Ownership: one leaf, technical writer.
- [x] Complete — evidence: T3 under Evidence. The link to `skills/setup/SKILL.md` resolves
  only after T2.

### T4: Behavioral trials

- Acceptance criteria: AC2–AC9 and AC12, candidate only; the skill is new, so no baseline
  exists. AC10 is checked by the diff, not by trials.
- Dependencies: T1–T3.
- [x] Complete — evidence: T4 under Evidence and the evidence record it links.

### T5: Independent review and integrated checks

- Dependencies: T1–T4. A reviewer that wrote none of the change and has not received the
  implementers' conclusions. The coordinator runs the integrated repository checks.
- [x] Complete — evidence: Review, the repairs of R1–R7 and the integrated checks under
  Evidence.

- Verification: the repository commands below ran and passed (see Evidence); the behavioral
  trials are in T4.
  - Repository commands, from the repository root, confirmed in `CONTRIBUTING.md` and `scripts/`:
    - `git diff --check`
    - `claude plugin validate plugins/lusona`
    - `claude plugin validate .claude-plugin/marketplace.json`
    - `python3 scripts/sync_shared.py --source shared plugins/lusona --check`
    - `python3 scripts/package.py --output tmp/<fresh-directory>`
    - `python3 scripts/test_package.py`, `test_contract.py`, `test_instructions.py`,
      `test_rule_inventory.py`, `test_skill_template.py`, `test_sync_shared.py` and
      `test_voice.py`, each run as `python3 scripts/<name>`
    - `python3 scripts/check_contract.py`, `check_skill_template.py` and `check_voice.py`
      (each defaults to `plugins/lusona`), and `check_instructions.py`
    - `agy plugin validate plugins/lusona --strict`, when the Antigravity CLI is available
    - `bash scripts/test-work-record.sh` and `scripts/test-work-record.ps1`, only when the
      change touches the work-record helper
  - Behavioral trials to design under `CONTRIBUTING.md` "Behavioral evidence", with cases and
    criteria declared before the trials:
    - setup in a project without `docs/lusona/`, `AGENTS.md` or `CLAUDE.md` (AC2, AC4, AC5,
      AC7, AC9);
    - setup in a project with existing records and agent instructions, and a second run (AC3,
      AC5, AC7, AC8);
    - confirmation declined (AC4);
    - preferences given, declined and changed, and a later session that needs the TDD level
      (AC6, AC8);
    - setup in a project with legacy records and no `docs/lusona/` (AC12).
  - AC10: `git diff --stat 6243701 -- shared plugins/lusona/skills` lists only
    `plugins/lusona/skills/setup/`.

## Evidence

- T1, helper command `init-queue` (leaf on the `sonnet` model, standard tier; coordinator
  inspected the diff and reran both suites on 2026-11-12):
  - Red, before the helper code: `bash scripts/test-work-record.sh` exited 1 with
    `work-record: Unknown command: init-queue`. The PowerShell suite exited 1 with
    `Command [init-queue, .../queue project] expected exit 0, got 1`.
  - Green: `bash scripts/test-work-record.sh` printed `Work-record behavioral checks passed.`
    and exited 0. `mise exec powershell@7.6.10 -- pwsh -NoProfile -File
    scripts/test-work-record.ps1` printed `PowerShell work-record behavioral checks passed
    (203 assertions).` and exited 0; the count before the change was 187.
  - The tests cover: content equal to the template, `docs/lusona/` created when absent, an
    existing `work.md` byte-identical, no other entry under `docs/`, wrong argument counts,
    a missing root, a file as root, a symlink and a directory at the destination, and a
    relocated helper.
  - One correction round, in the leaf's new PowerShell test only.
  - Limits: native Windows and Windows PowerShell 5.1 were not tested. Both helpers normalize
    trailing newlines to one, so equality with the template depends on the template ending
    in one newline, which it does.
- T3, public documentation (leaf on the `sonnet` model, standard tier; coordinator inspected
  the diffs on 2026-11-12):
  - The five READMEs each received the same five changes: count 14 to 15, a `setup` row after
    `status`, the Codex invocation forms, one sentence in the TDD paragraph, and one paragraph
    before the records table. `INSTALL.md` gained the Codex forms and a setup paragraph;
    `CHANGELOG.md` two entries in the 3.0.0 section; `CONTRIBUTING.md` the count.
  - No manifest, catalog or issue template changed: none enumerates the skills or states a
    count. The dated "thirteen skills" records in `INSTALL.md` are unchanged.
  - Coordinator corrections: the `INSTALL.md` paragraph said that the directory and queue wait
    for confirmation; it now says that only `AGENTS.md` and `CLAUDE.md` do. The added
    paragraphs in the English, Spanish and German READMEs were rewrapped to 100 columns.
  - `git diff --check` reported nothing. No `"version"` line changed.
  - Limits: no native reader checked the four translations.
- T2, setup skill and section template (forked leaf; a fork inherits the coordinator's model,
  so no tier routing applied; coordinator read the skill, template and reference diffs on
  2026-11-12):
  - Red: the new `test_package.py` assertions run against a `git archive 6243701` copy gave
    `Ran 16 tests`, `FAILED (failures=9)`, each `'setup' not found in {...}` for the four
    native manifests or `The portable package must include setup.`
  - Green: `python3 scripts/test_package.py` gave `Ran 16 tests`, `OK` (14 tests before).
  - The frontmatter description differs from the planned text in one place: "by creating"
    replaces a colon, because a colon followed by a space is invalid in an unquoted YAML value.
  - Decisions inside the skill that the criteria do not state: a preference already recorded
    in `docs/lusona/README.md` or other agent-instruction text is shown, left in place and not
    copied into the section; a new `CLAUDE.md` import goes on the first line; a new section is
    appended to an existing `AGENTS.md`; setup creates no notes, spec or queue row for itself.
  - `check_contract.py` keeps its baseline inventory at `34186da`; `setup` and `init-queue`
    are not added to it.
- Integrated repository checks, run by the coordinator on 2026-11-12 on the combined change
  (output in `tmp/setup-skill-integrated/checks-1.txt`, a scratch copy):
  - `git diff --check`: no output.
  - `python3 scripts/sync_shared.py --source shared plugins/lusona --check`: `Shared regions
    in sync.`
  - `check_contract.py`, `check_skill_template.py`, `check_voice.py`, `check_instructions.py`:
    exit 0.
  - `test_package.py` 16, `test_contract.py` 65, `test_instructions.py` 16,
    `test_rule_inventory.py` 3, `test_skill_template.py` 64, `test_sync_shared.py` 18,
    `test_voice.py` 49: all `OK`.
  - `python3 scripts/package.py --output tmp/setup-skill-integrated/package-1`: exit 0; the
    package holds 15 skill directories including `setup`, and `agents-section.md.template`.
  - `claude plugin validate plugins/lusona` and `claude plugin validate
    .claude-plugin/marketplace.json`: `Validation passed`. The first prints one advice line
    about an install line in the plugin README, which this change did not introduce.
  - `agy plugin validate plugins/lusona --strict`, and the same on the packaged plugin:
    `skills 15`, `Validation passed`.
  - `bash scripts/test-work-record.sh`: passed. The PowerShell suite: 203 assertions passed.
  - `evals/loop-conformance/test_checks.py`, `test_compare.py`, `test_run.py`: `OK`.
  - AC10: `git diff --stat 6243701 -- shared plugins/lusona/skills` prints nothing, and
    `git status --short plugins/lusona/skills shared` lists only `plugins/lusona/skills/setup/`.
  - Coordinator edit: the docstring count in `scripts/check_instructions.py` ("5 of 14
    skills") now says 15.
- Review: independent review on 2026-11-12 by a fresh leaf on the `opus` model that wrote none
  of the change and received the spec, the patch against `6243701` and the check outputs. It
  reran the helper suites, the four `check_*.py` scripts and the seven `test_*.py` scripts;
  all passed. No blocking defect. Findings, each in correction round 1 (consecutive 0, total
  1 once repaired and verified):
  - R1, should fix (AC5, AC7): `AGENTS.md` as a symbolic link to `CLAUDE.md` leads to a
    self-import and a change outside the section.
  - R2, should fix (AC5, AC6): a preference recorded outside the section plus a different new
    answer is either dropped or recorded twice. Repair decision: setup shows the recorded
    value, does not ask that question, and names where to change it. This narrows "setup asks"
    in AC6 to the case where no value is recorded outside the section.
  - R3, should fix (AC8): a rerun without a new answer removes a recorded preference.
  - R4, should fix (AC12): the legacy question is missing from the numbered steps, and a
    declined creation leaves a false records line in the section. Repair decision: on decline
    setup creates nothing under `docs/lusona/` and leaves the records line out.
  - R5, minor (AC7, AC8): other import forms such as `@./AGENTS.md` are not recognized.
  - R6, minor (AC5, AC8): section matching by literal text; user text below the section can
    be replaced on a rerun.
  - R7, should fix (AC1): `plugins/lusona/assets/workflow-loop.svg`, embedded in the five
    READMEs, says "14 skills" and does not show setup. The T3 evidence above missed this file.
  - Not repaired: the READMEs, the workflow guide and the section template state the Codex
    desktop syntax as fact, while `INSTALL.md` marks it as maintainer-reported. The user's
    words were "desktop seems to support both". Left for the user to decide.
  - Verification gaps the reviewer named: only trials can establish AC4–AC9, AC12 and the
    skill-dependent parts of AC2 and AC3. `tmp/setup-skill-t2/red-test_package.txt` (working
    tree) is not red evidence, because a README link from T3 broke the run; the red evidence
    is the run against the `6243701` copy, recorded under T2 above.
  - Trials are candidate only. Reason: the plugin at `6243701` has no `setup` skill, so a
    baseline session cannot start it, and the existing skills are byte-identical (AC10), so
    no behavior of an existing skill differs between baseline and candidate.
- Repairs of R1–R7 (the T2 leaf, resumed; coordinator read the repaired skill sections and
  viewed the rendered diagram on 2026-11-12):
  - R1–R6 are in `skills/setup/SKILL.md`: link inspection and the one-file rule; no question
    for a value recorded outside the section; kept values on a rerun; the legacy question as
    step 1 with the decline outcome; import recognition by resolution; section matching by a
    level-2 heading outside code fences, in-place update that keeps the user's lines, and the
    one allowed newline byte.
  - R7: the diagram says "15 skills" and lists `setup` in the coordination group; the SVG is
    well-formed and `rsvg-convert` renders it at 1100 x 852 without overlap.
  - Integrated checks rerun after the repairs, all exit 0 (scratch copy in
    `tmp/setup-skill-integrated/checks-2.txt`): the same commands as above, with
    `package.py --output tmp/setup-skill-integrated/package-2`. A search for "14 skills" and
    "fourteen" outside `docs/` finds only the historical `CHANGELOG.md` entry.
  - The reviewer has not re-reviewed the repairs. Trials on the repaired text are the
    verification of R1–R6.
- T4, behavioral trials (leaf on the `opus` model, deep tier): design, criteria, driver and
  per-trial data are in
  [evidence 2026-11-12-setup-skill](../evidence/2026-11-12-setup-skill/README.md). The
  criteria were written and locked before the first trial. First round, 9 trials:
  - Claude Code 2.1.323, `claude-opus-5-5`, effort high, 7 trials (C1 twice, C2 to C6 once):
    every check passed for AC2, AC3, AC4, AC5, AC6, AC7, AC8, AC9, AC12 and the repairs R1,
    R3 and R4. Total Claude-reported cost 3.5774 USD of a 25 USD ceiling.
  - The scope check passes on Claude Code only with one exclusion: the host creates an empty
    directory `.claude/.cc-writes` in every workspace. No tool call creates it. The
    coordinator accepted the exclusion; the frozen wording would grade it as a failure.
  - Codex CLI 0.167.2, X1 (new project): every check passed.
  - Codex CLI, X2 (later session through `specify`): 3 checks failed. The session used the
    level `targeted` without asking, but implemented the change instead of writing a spec
    ("The skill routes this fully specified request to implementation."), changed `greet.py`
    and `test_greet.py`, and did not name `AGENTS.md` as the source of the level. The request
    text began "Change greet.py so that ...". The `specify` skill is unchanged by this change.
  - Coordinator inspection: the files written in C1, C2, C5 and C6 match the reported
    outcomes.
  - Limits: one trial per case (C1 two), one grader, headless sessions without a native
    question tool. `memory_paths` did not show which instruction files Claude Code loaded, so
    the C4 result cannot be attributed to the `@AGENTS.md` import alone.
  - Amendment 1 (3 trials, criteria locked before they ran; Claude cost 0.9247 USD, record
    total 4.5021 USD):
    - X2-t2, Codex, the later session with a request worded as a definition: every check
      passed. The created spec records "Level: targeted." with `AGENTS.md` as its source, and
      `greet.py` and `test_greet.py` are byte-identical. Together with X2-t1 this indicates
      that the X2-t1 failures followed the request wording. X2-t1 keeps its 3 failed checks.
    - C8-t1, Claude Code, repairs R5 and R6: every check passed. `CLAUDE.md` with an inline
      `@./AGENTS.md` stayed byte-identical, the heading inside a code fence was not treated as
      a section, and the user's line stayed in the section.
    - C7-t1, Claude Code, repair R2: the R2 checks passed (no TDD question, the value and its
      location shown, no `TDD:` line written, `docs/lusona/README.md` byte-identical). The
      check for AC4 failed: the agent wrote `AGENTS.md` and `CLAUDE.md` after the reply "No
      model tier mapping. Continue." and before the confirming turn. Its words: "I read your
      \"Continue\" as confirming both files as shown." The written text equals the shown text.
  - Failure F1 (AC4, from C7-t1), correction round 1: the skill did not define a
    confirmation and allowed the proposal before the preference answers. Repair: the text is
    shown after the preference answers; a confirmation approves the shown text for a named
    file; an answer to a preference question or a request to continue is not one. The edit
    was made by a leaf on the `sonnet` model with the exact text supplied by the coordinator.
    The integrated checks were rerun on it and all exit 0 (scratch copy in
    `tmp/setup-skill-integrated/checks-3.txt`).
  - Amendment 2 (2 trials on candidate v2, which differs from v1 only in that paragraph;
    Claude cost 0.8987 USD; record total 5.4008 USD of 25 USD):
    - C7-t2, the same turn texts as C7-t1: every check passed. `AGENTS.md` and `CLAUDE.md` are
      absent after turn 2 and exist only after turn 3. The reply to "Continue" reads: "Your
      \"Continue\" answered the model tier question but does not approve the file text, so
      neither file has been written."
    - C1-t3, the new-project case: every check passed.
    - F1: round 1, material progress (repaired and verified by C7-t2). Consecutive without
      progress 0, total 1.
  - Totals: 14 trials (11 on Claude Code, 3 on Codex CLI). Failed checks: 3 in X2-t1 and 1 in
    C7-t1; both are explained above and both later trials passed. The working tree equals
    candidate v2 (`diff -r` prints nothing).
  - Observed and not repaired: in 5 trials the tier question listed example model identifiers
    of the host; none was recorded. The skill does not say whether such examples are allowed.
  - Residue outside the repository: counted under "Trial totals" below.
- `~/.codex/config.toml`: backed up before the Codex trials; the two added trust entries were
  removed and the file equals its backup.
- Second review pass, 2026-11-12, the same independent reviewer, on the final patch, the
  repairs and the trial record:
  - R1–R7 are resolved; the reviewer quoted the resolving sentence for each and inspected the
    rendered diagram. The repairs and the confirmation rule introduced no defect in the
    skill's logic and no contradiction with the synced regions or the references.
  - The reviewer recomputed the three design locks; each predates the first trial it covers.
    It agreed with every grade it spot-checked (C2-t1, C5-t1, C7-t1, C7-t2, X2-t2), and
    confirmed that all failures are kept in the record and that the working tree equals
    candidate v2 in all 62 files.
  - Finding A, should fix: the R2 and R4 repair decisions narrow AC6 and AC5, which the user
    accepted in D7, without the user's approval. Open; put to the user with A10.
  - Finding B, minor: "The request to run setup permits creating `docs/lusona/` ..." has no
    qualifier for the legacy question in step 1. Open; not edited, so that the trialed text
    stays the text in the working tree.
  - Finding C, minor: a value held both in the section and outside it gets two instructions
    ("leave the value's line out" and "Remove a recorded value only when the user asks").
    Open; no trial covers it.
  - The reviewer's assessment per criterion: established AC1, AC2, AC3, AC8, AC9, AC10 and
    AC13; partly AC4 (the confirmation repair verified by one trial for one wording; a
    decline of one file only is untested), AC5 (C5 passes only under the R4 narrowing), AC6
    (C7 passes only under the R2 narrowing; X2-t1 failed on other wording), AC7 (rests on
    A10) and AC12 (only the decline path ran).
  - Marks above: the seven criteria the reviewer rated established are marked. AC4 and AC12
    stay unmarked: the both-file decline (C3) ran only on candidate v1, whose confirmation
    paragraph v2 replaced, and no trial created `docs/lusona/` beside legacy records. AC5,
    AC6 and AC7 stay unmarked until the user decides the narrowings and A10.
  - Candidate-only trials remain a stated gap against the literal wording of `CONTRIBUTING.md`
    "Behavioral evidence" item 1 for persistent data; the record gives the reason.
- Candidate v3, 2026-11-12, after the user's decisions D10–D13: three edits to
  `skills/setup/SKILL.md` by a leaf on the `sonnet` model with text supplied by the
  coordinator: the permission sentence names the legacy exception (finding B); a value held
  both in the section and elsewhere is shown with both locations and the user chooses
  (finding C); the tier question may name the host's models and a model is recorded only when
  the user chose it. `diff` against candidate v2 shows only these bullets, and `diff -rq`
  shows no other file differs. Findings B and C: correction round 1 each.
  - Integrated checks on v3, all exit 0 (scratch copy in
    `tmp/setup-skill-integrated/checks-4.txt`): `git diff --check`, the sync check, the four
    `check_*.py` scripts, the seven `test_*.py` scripts, `package.py --output
    tmp/setup-skill-integrated/package-4`, `claude plugin validate` on the plugin and the
    marketplace, `agy plugin validate --strict`, the Bash helper suite and the PowerShell
    helper suite (203 assertions). AC10 diff: empty.
  - The reviewer has not seen the v3 edits. Edits B and C follow its own correction notes.
- T4, Amendment 3: five Claude Code trials on candidate v3, criteria locked before they ran,
  one trial each, no rerun; every check passed. Cost 2.1347 USD; record total 7.5355 USD of
  the 25 USD ceiling. The working tree equals candidate v3 (`diff -rq` prints nothing).
  - C3-t2, both files declined: neither file exists at the end and both are reported as
    declined (AC4).
  - C10-t1, `AGENTS.md` confirmed and `CLAUDE.md` declined: `AGENTS.md` holds the shown
    section, `CLAUDE.md` does not exist in any snapshot, and the reply says "`CLAUDE.md`:
    declined, not created" (AC4, AC5, AC6).
  - C5-t2, legacy records with `docs/lusona/` declined: no `docs/lusona/`, legacy files
    byte-identical, no records line in the section (AC12, AC5 as revised).
  - C11-t1, legacy records with `docs/lusona/` accepted: the first reply says "Nothing has
    been created yet, because this project has legacy records and no `docs/lusona/`";
    `docs/lusona/` appears only after the user's yes, `work.md` equals the template, and the
    legacy files are byte-identical (AC12, AC2).
  - C9-t1, a TDD value in both the section and `docs/lusona/README.md`: the first reply shows
    both values with their locations and asks which location keeps it; after the user chose
    the README, the section has no `TDD:` line and the README is byte-identical (finding C,
    AC3, AC7, AC8).
  - Observation: all five tier questions named host models; two recommended a full mapping.
    No model was recorded without the user choosing it.
- Trial totals: 19 trials (16 on Claude Code, 3 on Codex CLI) on three frozen candidates.
  Failed checks: 3 in X2-t1 and 1 in C7-t1, both explained above and followed by passing
  trials. Residue outside the repository, counted on 2026-11-12 and not deleted: 19 trial
  workspaces under `~/.cache/lusona-evals/`, 16 Claude Code project directories under
  `~/.claude/projects/` and 3 Codex session rollouts. Scratch inside the repository:
  `tmp/setup-skill-*` (git-ignored).
- Criteria: AC1–AC10, AC12 and AC13 are marked met on the evidence above. AC11 is withdrawn.
- Limits and checks not run: one trial per case on each candidate, apart from the
  new-project case (three trials); one grader; headless sessions without a native question
  tool; no Codex trial on v2 or v3; no installation on Codex, Cursor, Xcode or the
  Antigravity App; no native Windows or Windows PowerShell 5.1 run; the four translations
  have no native reader's review; the reviewer has not seen the three v3 edits; the Codex
  desktop syntax rests on the user's report (D13).
- Changes: uncommitted on `main`, diff base `6243701`. A commit needs the user's request
  (repository `AGENTS.md`).
- Skill audit, 2026-11-13, with [docs/skill-audit.md](../../skill-audit.md) (user request:
  "make sure that the newly added setup skills passes skills audit"). No file of the addition
  was changed by the audit.
  - Script checks, run by the coordinator on the working tree, all exit 0:
    `sync_shared.py --check`, `check_skill_template.py`, `check_voice.py`,
    `check_instructions.py`, `check_contract.py`, `unittest discover scripts` (231 tests), the
    loop-conformance unit tests (150), `package.py`, `test-work-record.sh`,
    `test-work-record.ps1` (203 assertions, PowerShell 7.6.10 through `mise exec`),
    `git diff --check`, `claude plugin validate` for the plugin and the marketplace.
    Not run: `agy plugin validate`, any agent trial.
  - Review items: one independent auditor leaf (`opus`; it wrote neither the audit document
    nor the addition) applied the document as written. Its result: 10 findings, 4 blocking
    (T11, V9, VP6, E2) and 6 non-blocking (P2, T6, T13, V1, V4, E7). 19 of its results depend
    on how an item is read. The addition does not pass the audit as the document stands.
  - The coordinator read each cited line. The coordinator wrote the audit document, so the
    three lists below are its reading, not a second independent result.
  - List A, findings the coordinator agrees are defects of the addition:
    1. T11 (blocking; the auditor marks the result as reading-dependent):
       `skills/setup/SKILL.md:79` (step 1) deletes a list item "from the section" before any
       step composes the section; the composition instruction is the practices item at
       line 67.
    2. V9 (blocking): `skills/setup/SKILL.md:79` holds the clause "because it names
       `docs/lusona/`", which can be deleted without changing the action. The auditor names
       line 72 (two sentences on how Claude Code loads `AGENTS.md`) as the same class; the
       coordinator reads those as changing the action, because they exclude a plain name and
       a Markdown link from counting as an import (D10).
    3. VP6 (blocking when "elsewhere" covers the same file): `skills/setup/SKILL.md:63`
       "Record only what the user gave." repeats line 32 "Record only values the user gave."
    4. T13 (non-blocking): `skills/setup/SKILL.md:63` "Do not assume a value." forbids what
       the Questions line requires for optional preferences and lacks the wording "Exception
       to the Questions line". The content is covered by A5 (D7).
    5. E7 (non-blocking): `CHANGELOG.md:29` says "The other 12 skills assign no work to the
       coordinator" and names `status` and `explore` only. `README.md:157` and the same
       sentence in the 4 translations say that two skills assign work to the coordinator.
       `setup` is a third (`skills/setup/SKILL.md:46`). The auditor reported the changelog
       line; the coordinator found the README sentences.
  - List B, fails the coordinator attributes to pass conditions of the audit document. The
    user decides whether the pass condition or the addition changes (audit items D2, VP4):
    P2 (no instruction to read the owning record or the request; setup has no owning record
    and reads the project state), T6 (line 67 is a one-time action placed in practices; no
    test separates a practice from a step), V1 (line 48 "needs the confirmation"; the
    every-task block uses the same declarative form), V4 ("Agent-instruction section" is the
    template's label in `files.md:36` and the workflow guide), E2 (the Bash suite prints no
    assertion count; the red and green results and the PowerShell counts 187 and 203 are
    recorded). VP7 passes only because the auditor read past its wording: "the first
    sentence states the action and the output" is not met by the descriptions the voice pass
    split, which name the output in the second sentence.
  - List C, passes whose other reading is a fail: K3 (`init-queue` is a new helper command
    decided by the coordinator in D8, with no user decision), E5 (the reviewer has not seen
    the v3 edits), E3 (no review of the wording against V1-V9 is recorded), E4 (per-check
    criteria are declared, no pass mark), D2 (R2 and R4 were applied before D11 accepted
    them), V8 (the section template repeats the invocation syntax of the workflow guide),
    D1 (the handoff below names a row in `work.md` that does not exist), P8, T14 and V2.
  - The Saving exception (`skills/setup/SKILL.md:92`) is covered by A4, accepted in D7; the
    line "decisions inside the skill that the criteria do not state" above lists it as well.
  - Limits: one auditor. A first trial audit on an earlier version of the document produced
    a different list. No correction is applied; each correction changes text that the
    behavior trials and the review covered.
- Corrections after the skill audit, 2026-11-13 (D14-D16):
  - Applied by a leaf (`sonnet`) with the exact text of D14: `skills/setup/SKILL.md` (step 1,
    the compose-the-section practice, the optional-answers practice), `CHANGELOG.md`,
    `README.md` and its 4 translations. The coordinator inspected each changed line and
    re-wrapped one line in `README.md`. The 4 translated sentences have no native reader's
    review.
  - `docs/skill-audit.md`: the pass conditions of P2, T6, V1, V4, E2 and VP7 and the severity
    rule for an item marked in part are reworded and marked "(revised 2026-11-13)" (D16).
  - Checks on the final text, run by the coordinator, all exit 0: `sync_shared.py --check`,
    `check_voice.py`, `check_skill_template.py`, `check_instructions.py`, `check_contract.py`,
    `unittest discover scripts` (231 tests), the loop-conformance unit tests (150),
    `package.py` (built `lusona-3.0.0.zip`), `test-work-record.sh`, `test-work-record.ps1`
    (203 assertions), `git diff --check`, `claude plugin validate` for the plugin and the
    marketplace. Not run: `agy plugin validate`.
  - Review of the corrected passages by a fresh leaf (`opus`; it wrote none of the text and
    saw no earlier review): no blocking finding. Its passages were the two changed practices,
    steps 1 to 6, the Establish section, the description, the changelog bullet and the README
    paragraphs. Of the three v3 edits it reviewed the permission sentence in full (Establish)
    and touched the two-locations practice and the tier-question practice only through items
    T6 and P3. E5 for the v3 edits stays open. It followed the legacy-records path for a declined and a
    non-declined project: every instruction has its input when it is reached, and the list
    item is deleted exactly when the project has legacy records and no `docs/lusona/` and the
    user declined. Five non-blocking findings, none corrected:
    1. `CHANGELOG.md` and the 5 READMEs say three skills assign work to the coordinator and
       the other 12 assign none; `skills/batch/SKILL.md:72,74` assigns definition and
       architecture reconciliation to the coordinator. The sentence comes from decision 28
       of spec 20261111 ("the other 12 skills ... assign no work to the coordinator") and
       predates this addition.
    2. The preference practices neither require nor exclude a recommended answer, which the
       Questions line asks for.
    3. "Legacy records" has no test beyond "such as `docs/agent/`"; it controls step 1.
    4. No numbered step composes the section; the practice composes it and the confirmation
       practice times it "after the preference answers" (T11, reading-dependent).
    5. "both answers are optional, and setup assumes no value for either" is declarative
       (V1, reading-dependent).
  - Audit result by count. The audit document defines severity and no overall pass rule.
    Script checks: all exit 0. The first audit's 4 blocking findings: T11, V9 and VP6 are
    corrected in the text (D14); the reviewer found no blocking defect in those passages and
    marked T11 and VP6 as passing under one reading. E2, applied by the coordinator to the
    revised condition, not by an independent reader: the T1 evidence gives the failing and
    passing results with exit code and output line for the Bash suite and the counts 187 and
    203 for PowerShell, which meets the revised condition; the docstring-only change to
    `scripts/check_instructions.py` ("5 of 14" to "5 of 15") had no fixture-break run, which
    fails E2 when a docstring edit counts as a changed check script. The first audit's 6
    non-blocking findings: T13 and E7 corrected (D14); P2, T6 and V1 re-applied by the
    reviewer under the revised conditions (P2 and T6 pass; V1 fails under one reading, finding
    5 above); V4 not re-applied by a reviewer, and open: "Lusona section" is used in
    `skills/setup/SKILL.md`, `references/files.md:36` and the plugin README without a row in
    the Terminology table, which the accepted inference part of V4 asks for. K3 is settled by
    D15. Not settled: the list C readings other than K3, the five non-blocking findings above,
    V4, the second part of E2, and the Saving exception without explicit confirmation. No full
    audit was run on the final text or with the revised pass conditions.
  - Limits: the behavior trials were not rerun, so no trial covers the text of D14; one
    reviewer; headless review of text, no agent run of the skill.
  - Settled after this entry, 2026-11-13: finding 1 above by D17 and the Saving exception by
    D18. No file under `plugins/lusona/` changed for either decision, and no check was rerun.
- Result rule applied, 2026-11-13 (D19-D22). No file under `plugins/lusona/` changed.
  - Baseline test by a leaf (`opus`; it wrote neither the audit document nor the addition),
    read-only, baseline `6243701`. The coordinator read each passage and record cited below.
    - P8: `setup` has no instruction that ends a reply while authorized work remains, so it
      passes under both readings. Baseline misses: `skills/review/SKILL.md:45` (no list item
      for a missing input) and `skills/batch/SKILL.md:110` (none for a complete scope); D22.
    - V8: the baseline repeats a rule in a template without naming its reference
      (`templates/work.md.template:31`, `templates/spec.md.template:38`), so the lenient
      reading applies and `setup` passes.
    - V2: no sentence of the form "<skill> is" outside the Persona fields in the 14 skills;
      settled by D21.
    - E3: the rewrite records script checks only for the text of decisions 28 and 29
      (`notes/selective-delegation-for-status-and-explore.md:56-60`,
      `notes/final-reply-required-labels.md:35-38`); lenient reading, pass (D19).
    - E4: the rewrite declared pass marks before its repeated trials (spec 20261111,
      decisions 19 and 23); this item declared a criterion for each check and ran each trial
      once; settled by D20.
    - D2: decision 29 accepted a sentence "already in the working tree"
      (`notes/final-reply-required-labels.md:11-13`), and voice pass round 1 applied and then
      reverted 23 edits (`notes/voice-pass/round-1-wording-edits.md:780-782`); lenient
      reading, pass (D19).
  - `docs/skill-audit.md`: step 8 added; the pass conditions of P8, V8, E3 and D2 are reworded
    by the test and those of V2 and E4 by D20 and D21. `docs/lusona/work.md`: one Ideas row
    (D22).
  - E5, review of the two v3 edits that no reviewer had read in full
    (`skills/setup/SKILL.md:62`, last two sentences, and `:65`), by a second leaf (`opus`; it
    wrote none of the text). With it, a reader who wrote none of the text has read each of
    the three v3 edits. Both passages do what the "Candidate v3" entry states. Its findings,
    none corrected:
    - F1 (non-blocking, no audit item): at `:65`, no line decides the case where the user
      answers with a new value instead of a location.
    - F2 (non-blocking, no audit item): at `:65`, when the two values differ and the user
      keeps the section, two values remain and the user is not told.
    - AC6, reading-dependent: when the section and another location both hold a value and
      the user keeps the section, the section still holds a copy of a value that is recorded
      elsewhere. AC6 says setup "writes no second copy". Read as "adds no new copy", AC6 is
      met. Read as "the section ends with no copy", it is not. Trial C9-t1 covered only the
      path where the user chose the other location.
    - P8, reading-dependent for `:65`: the next-action item "A preference question is open"
      covers an unanswered location question only when that question counts as a preference
      question; the text does not say.
    - F3 (non-blocking, no audit item): `:65` assumes exactly one location outside the
      section.
    - F4 (VP4, reading-dependent, blocking under one reading): the v3 edit at `:65` sets a
      new action without a recorded user decision. No user decision covers v3 edits 2 and 3.
    - F5 (non-blocking, no audit item): `:62` does not say whether accepting a mapping that
      the agent recommended counts as "the user chose it".
    - F6 (V1, reading-dependent, blocking under one reading): "The question may name the
      models the host offers" has no trigger clause. The 14 skills hold no permission
      sentence with "may", so the test does not decide.
    - F7 (VP6 and V8, reading-dependent, blocking under one reading): the last sentence of
      `:62` restates `:32` for models.
  - Audit result under step 8: `undecided`. No open finding is blocking under every reading.
    Open, 17 items. Results that depend on the reading (8): AC6 and P8 for `:65` (both
    above), the second part of E2 (the docstring-only edit to
    `scripts/check_instructions.py`), T11 (finding 4 above), V1 at `:63` (finding 5 above),
    F4, F6, F7. A user decision that accepts v3 edits 2 and 3 settles F4 under both readings. Non-blocking findings without a decision (7):
    findings 2 and 3 above, V4, F1, F2, F3, F5. Checks not run without a decision that
    accepts the gap (2): `agy plugin validate`; behavior trials on the text of D14.
  - List C of the first audit after these steps: K3 by D15, T14 by D18, V8, P8, E3, D2 by the
    test, V2 by D21, E4 by D20, E5 by the review above. D1: the handoff no longer names a queue
    row ("The queue holds no row for this item").
  - Not independently applied: E2, first part, and V4 rest on the coordinator's application.
    The reworded conditions of P8, V8, E3, D2 and VP4 are the coordinator's wording, and no
    reader has reviewed them.
  - Checks after these edits, run by the coordinator: `git diff --check` exit 0;
    `python3 -m unittest discover scripts` 231 tests OK; `check_instructions.py` exit 0. The
    other script checks were not rerun.
  - Two of the 17 open items closed afterwards by checks, both run by the coordinator on the
    current text, which leaves 15:
    - `agy plugin validate plugins/lusona --strict`: "Validation passed", 15 skills, exit 0.
      It runs again after any further correction.
    - E2, second part: `scripts/check_instructions.py` on an unchanged copy of the plugin
      exits 0. With the sentence "A queue state does not authorize implementation." appended
      to `skills/setup/SKILL.md` in a copy, it exits 1 ("restated: ... does not authorize").
      With the Skills table of the workflow guide copied into `references/files.md` in a
      second copy, it exits 1 ("tables: catalog table duplicated in references/files.md").
      The strict reading of E2 is met, so the result no longer depends on the reading. The
      copies are in `tmp/e2-fixture/` (scratch).

- Correction round 2, 2026-11-13 (D23-D30):
  - Applied by a leaf (`sonnet`) with the exact text of D23, D24, D26 and D27:
    `skills/setup/SKILL.md` lines 62, 63, 65 and step 5 (line 83);
    `references/workflow-guide.md` lines 90-91; `references/files.md:36`. Each old string
    matched once. The coordinator inspected each changed line. AC6 is revised in this spec
    (D25). `docs/skill-audit.md`, step 6, holds the sentence of D30.
  - Checks on the corrected text, run by the coordinator, all exit 0: `sync_shared.py
    --check`, `check_voice.py`, `check_skill_template.py`, `check_instructions.py`,
    `check_contract.py`, `check_rule_inventory.py`, `unittest discover scripts` (231 tests),
    `package.py` (built `lusona-3.0.0.zip` in `tmp/setup-round2-package`), `claude plugin
    validate` for the plugin and the marketplace, `agy plugin validate plugins/lusona
    --strict`, `test-work-record.sh`, `git diff --check`. Not rerun: `test-work-record.ps1`
    (the helper did not change).
  - Re-read of the six changed passages by a leaf (`opus`; it wrote none of the text). The
    passages match D23-D27 word for word. It walked 16 cases and reported 5 item findings and
    10 other observations, none corrected:
    - R2-F1 (the reader's label: T11 and AC4, blocking): on a repeated run, step 5 shows the
      composed template section, and step 6 writes it merged with the user's lines; the shown
      text is not the text written. The gap predates this round. The coordinator's reading:
      the T11 check asks whether a step's result or input is missing, and neither is; the
      finding concerns AC4 ("shows the exact text"), and no audit item covers a failed
      acceptance criterion, so step 6 as amended by D30 makes it non-blocking. The result
      depends on the reading. It is a prediction, not an observation: in trial C8-t1
      (candidate v2, a repeated run on a section with a user's line) the agent showed the
      merged section with the user's line before the confirmation
      (`raw.zip`, `raw/C8-t1/s1-turn-2.stdout.jsonl`). No trial ran on the current step 5.
    - R2-F2 (AC6 with AC8; no audit item covers a failed acceptance criterion, so
      non-blocking by step 6): the user gives a new value and chooses a location outside the
      section; "replace the section's value" and "remove the section's line" both apply.
    - R2-F3 (T13, reading-dependent, non-blocking): the user asks which value the agent
      suggests; "Answer direct questions first", `references/tdd.md:11` ("recommend a level")
      and "recommend no answer" meet, and the exception names only the Questions line.
    - R2-F4 (VP6, reading-dependent): step 5 repeats line 74 of the same file.
    - R2-F5 (V4, non-blocking): "standing preference" is used in 4 files without a
      Terminology row.
    - R2-O1: a mapping for one or two tiers, or a model without a reasoning setting, is not
      decided. R2-O2: no instruction to ask again after an unclear preference answer. R2-O3:
      when the user keeps the section and another location holds a different value, no line
      of the plugin says which standing preference governs. R2-O4: "assume no value" with
      "Delete a line that has no value" can be read as deleting an existing section value.
      R2-O5: "new value" is undefined. R2-O6: `references/workflow-guide.md:24` keeps the link
      label "agent-instruction section". The first audit's V4 finding named this line as
      well; D27 as applied is incomplete, because the coordinator's search for the label was
      case-sensitive. R2-O7: the Terminology row says "that setup writes",
      and the skill also counts a section written by hand. R2-O8: `README.md:151` says the
      agent recommends an answer, without the setup exception. R2-O9: when the composed
      section equals the existing one, step 5 still asks for confirmation. R2-O10: when both
      locations hold the same value, the location question is still asked.
  - Settled by this round, by text or decision: findings 2 to 5 of the review of the
    corrected passages, V4 as first reported, F1 to F7 of the review of the v3 edits, the AC6
    reading, P8 for line 65, and `agy plugin validate`. Open: the 15 results of the re-read
    above, and the trials of D29, which have not run.
  - Audit result under step 8: `undecided`. No open finding is blocking under every reading;
    R2-F1 is blocking under the reader's reading of T11.
  - Counts of the three reads by readers who wrote none of the text: 5 results (review of
    the D14 passages), 9 (review of the two v3 edits), 15 (this re-read). At least 6 of the
    15 concern sentences that this round added.

- Correction round 3, 2026-11-13 (D31-D34):
  - Applied by a leaf (`sonnet`) with the exact text of D32: `skills/setup/SKILL.md:65` and
    `references/workflow-guide.md:24`. Each old string matched once; `grep -rni
    "agent-instruction section" plugins/lusona` finds no match. The coordinator inspected
    both lines.
  - Checks on the corrected text, run by the coordinator, all exit 0: `sync_shared.py
    --check`, `check_voice.py`, `check_skill_template.py`, `check_instructions.py`,
    `check_contract.py`, `check_rule_inventory.py`, `unittest discover scripts` (231 tests),
    `package.py` (built in `tmp/setup-round3-package`), `claude plugin validate` for the
    plugin and the marketplace, `agy plugin validate plugins/lusona --strict`,
    `test-work-record.sh`, `test-work-record.ps1` (203 assertions), `git diff --check`.
  - Settled by decision: R2-F2 and R2-O6 by D32, R2-F3 by D33, the other 11 results of the
    re-read by D34.
  - Read under D31 by a leaf (`opus`; it wrote none of the text): the audit items T6, T11,
    T13, L5, L12, V1-V9, VL5 and VP1-VP7 applied to the two changed sentences. No item fails,
    and no result depends on the reading. Within line 65, each reply of the user (another
    location; the section; a new value with no location; a new value with another location;
    no answer) triggers at most one of "remove" and "replace". Neither sentence contradicts
    another instruction of its file. Two remarks, listed as accepted under D31: a new value
    given together with another location is written nowhere by setup, and the user is told
    that setup changes a value only in the section; "Remove the section's line only when"
    states a necessary condition and is read as the instruction to remove.

- T4, Amendment 4, 2026-11-13 (D29, D34): six Claude Code trials on candidate v4, the text
  after correction round 3, each run once by a leaf (`opus`) that wrote none of the skill
  text. Record:
  [evidence](../evidence/2026-11-12-setup-skill/README.md#amendment-4). The design was
  locked at 2026-11-13T23:54:01Z and the first trial started at 23:55:27Z; the coordinator
  ran the driver's lock check after the trials and it reported no difference. Cost
  2.5745 USD of the 5 USD cap; record total 10.1100 USD of 25 USD. Claude Code 2.1.325 (the
  declared condition names 2.1.323; disclosed in the design before the lock). `diff -r` of
  the frozen candidate against `plugins/lusona` printed nothing before and after the trials.
  - C12-t1, two values that differ and the section kept: every check passed. The first reply
    shows both values with their locations and asks which location keeps the value; the
    section keeps its line, `docs/lusona/README.md` is byte-identical, and the reply names
    both locations that still hold a value.
  - C13-t1, a new value given to the location question: every check passed. The section
    holds the new value, the README is byte-identical, and the user is told that it still
    holds a value.
  - C14-t1, both preferences declined: `AC5` and `AC4-order` passed (no `TDD:` line, no
    `Model tiers:` line). `D23-norec` failed under the locked definition: turn 1 says "You
    can also attach a scope to a level, for example \"`targeted` for input parsing\"."
  - C15-t1, the user chooses among the models the question named: the section holds only the
    chosen models; no `TDD:` line. `D23-norec` failed under the locked definition: turn 1
    says "You can give a level and its scope, for example \"targeted for argument
    parsing\", or decline."
  - C5-t3, legacy records with `docs/lusona/` declined: every check passed.
  - C8-t2, a repeated run on a section with a user's line: every check passed, including
    `AC4-shown`: the section shown before the confirming turn contains the user's line and
    equals the written section line for line. This is one observation against the
    prediction R2-F1.
  - The grader recorded its disagreement with its own locked definition for the two
    `D23-norec` failures (it reads both sentences as examples of the answer format) and did
    not apply it. The coordinator read both quotes in `trials/C14-t1/trial.json` and
    `trials/C15-t1/trial.json`. Whether a format example that names a level is a
    recommendation under D23 is the user's decision.
  - Observations outside the criteria: in C12-t1 the composed section equalled the existing
    one, and the agent wrote nothing and asked for no confirmation ("Since writing it would
    change nothing, I didn't ask you to confirm it."), so `AC4-order` passed there without
    testing the confirmation. In C15-t1 the agent told the user "I recommend no answer for
    either one", which a user can read as advice to decline both. The tier question named
    host models in five of six trials; only C15 recorded models, and only the chosen ones.
  - Planned and unrun: C15-t2 (the form of C15 for a tier question that names no model); its
    condition did not occur.
  - Limits: one trial per case, one host, one model (`claude-opus-5-5`, effort high),
    headless mode without the native question tool; no Codex trial on this text.

- Audit result, 2026-11-13 (D35-D39), stated by the coordinator, who wrote the audit
  document and its result rule; no other reader applied step 8:
  - Checks behind the last three decisions. VP6: a search of the 14 skills for a numbered
    step that restates a sentence of a practices or Establish item of the same file (string
    similarity above 0.62, 25 pairs) found only link sentences with different triggers, so
    the baseline does not decide and the user decided (D38). V9 at line 72: no decision and
    no read by a non-author covered it before D39. E2, first part: the failing PowerShell run
    is recorded with its exit code and message (`scripts/test-work-record.ps1:31` throws at
    the first failed assertion, and the count is printed only on success, line 264); the
    passing run with 203 assertions; the Bash runner prints no count; the T2 red result is
    "Ran 16 tests, FAILED (failures=9)" and the green result "Ran 16 tests, OK". This meets
    the E2 condition as revised by D16, by the coordinator's application.
  - Step 8, condition 1 (no blocking finding open): the first audit's T11, V9 and VP6
    findings are corrected (D14) and its E2 finding is met (above, and the deliberate-break
    run). R2-F1 and R2-F4 are not failures of T11 and VP6 (D37, D38). V9 at line 72 passes
    (D39).
  - Condition 2 (each non-blocking finding corrected or decided): corrected by text: T13 and
    E7 of the first audit, V4 (D27, D32), findings 2, 4 and 5 of the review of the D14
    passages (D23, D26), F1 to F7 of the review of the v3 edits (D24, D26), R2-F2 and R2-O6
    (D32). Accepted by decision without a text change, 21 results: finding 1 (D17), finding 3
    (D28), R2-F3 (D33), 11 results of the re-read (D34), 2 remarks of the read under D31, 2
    failed trial cells (D35), 2 trial observations (D36), V9 at line 72 (D39).
  - Condition 3 (unrun required checks): every script check of section 2 of the audit
    document ran on the final text and exits 0. The trials ran in the scope the user set
    (D29, D34). Not run, reported as limits: a Codex trial on the final text, C15-t2, an
    installation test on any host, a native reader's review of the translated sentences.
  - Condition 4 (no result depends on the reading): the 19 reading-dependent results of the
    first audit are settled by D15, D16, D18-D22 and the corrections; the later ones by D33
    and D37-D39. 15 pass conditions of the audit document were reworded on the way (P2, T6,
    V1, V4, E2, VP7, P8, V8, E3, D2, VP4, V2, E4, T11, VP6). Three further points:
    - L6: the first auditor applied it to the references the addition links or changes and
      noted that the item does not state the scope. Both scopes give the same result here:
      `git diff 6243701` shows that the first changed line is line 7 in `files.md`, line 86
      in `naming.md` and line 21 in `workflow-guide.md`, so no opening line changed, and
      `git status` shows no changed `SKILL.md` among the 14 skills.
    - T11 (D37): the two findings that T11 cites, W13 F15 ("Report file vs reply content
      unclear") and F16 (a directory written "before the record supplying the ID exists"),
      concern where an output goes and a missing input. Neither records two steps whose
      outputs disagree, so the records of the rewrite do not contradict D37.
    - `skills/setup/SKILL.md:47` against the TDD line: the first auditor marked its cover by
      the constraint "Setup selects no TDD level for any change and authorizes no
      implementation" (Agreement, accepted in D7) as reading-dependent. D21 names the
      sentence and keeps it.
  - Limit of this statement: section 1 of the audit document says that the auditor must not
    be the author when independent review is required. The coordinator supplied the text of
    every correction, wrote the result rule, and applied step 8, the first part of E2 and
    the judgment of which unrun checks are required. The item results come from readers who
    wrote none of the text; the result word does not.
  - Result: `pass`.

- Version, documentation and clean-up before the commit, 2026-11-13 (D40-D42):
  - Version 3.1.0 in the five native manifests and in the version label of the five READMEs.
    `CHANGELOG.md`: a 3.1.0 entry holds the setup changes; the 3.0.0 entry has the text of
    tag `3.0.0` with the heading date 2026-11-12, so its sentence "The other 12 skills assign
    no work to the coordinator" again names `status` and `explore` only, which is correct for
    the 14 skills of 3.0.0 (D17); the 3.1.0 entry states that `setup` does its work as
    coordinator. Found and not changed: the headings of 2.0.0 to 2.0.5 say "Untagged source
    snapshot" although tags exist; the intro now says so.
  - README and INSTALL (D41), applied by a leaf (`opus`): the English text was supplied by
    the coordinator; the leaf translated it for the four translations. No native reader
    reviewed the translations. The leaf noted alternatives for "Set up Lusona" in Spanish
    ("Prepara") and Chinese ("配置").
  - Clean-up (D42): deleted from `tmp/`: the audit and setup package directories of this
    session, `audit-trial`, `e2-fixture`, `raw-look` and the draft file. Earlier entries of
    this spec that name those paths describe scratch that no longer exists. Kept:
    `tmp/setup-skill-t4`, which holds the frozen candidates that the driver's lock check
    reads. Deleted without a commit: the withdrawn spec
    20261113-capture-project-working-context-during-setup and
    `notes/setup-user-outcomes.md`. Evidence directory: 82 files under
    `trials/<trial>/final/` removed, each of which duplicated text in its `trial.json`; the
    evidence README has a "Removed files" section; the lock check passes after the removal.
    Not deleted: `raw.zip` (git-ignored) and the trial workspaces under
    `~/.cache/lusona-evals/`.
  - Checks on the state that is committed, run by the coordinator, all exit 0:
    `sync_shared.py --check`, `check_voice.py`, `check_skill_template.py`,
    `check_instructions.py`, `check_contract.py`, `check_rule_inventory.py`, `unittest
    discover scripts` (231 tests), the loop-conformance unit tests (150), `package.py` (built
    `lusona-3.1.0.zip`), `claude plugin validate` for the plugin and the marketplace, `agy
    plugin validate plugins/lusona --strict`, `test-work-record.sh`, `test-work-record.ps1`
    (203 assertions), `git diff --check`. Under `plugins/lusona/`, only the `"version"` line
    of the four manifests differs from the trial candidate v4.
  - Audit item K5 (the version changes only on the user's request): met by D40.

## Current handoff

- Authorized work: implementation of this spec (D7) and the five corrections of D14. Source:
  user, 2026-11-12, chat, and 2026-11-13, native question tool. Commits are not authorized:
  repository `AGENTS.md` allows a commit only on request.
- Completed and remaining work: AC1–AC10, AC12 and AC13 are met on the paths the trials
  covered. The skill audit result is `pass`, stated by the coordinator (Evidence, "Audit
  result"); 21 results are accepted by decision without a text change. The plugin version is
  3.1.0 (D40). No work remains on this item.
- Human acceptance and delivery: committed on `main` on 2026-11-13 at the user's request
  ("clean-up, group and commit"), in three commits: the setup skill with version 3.1.0, the
  skill audit document, and these records. Not pushed, not tagged, not published.
- Correction rounds: R1–R7, X2 and F1, round 1 each, all with material progress; the audit
  corrections of D14, round 1, with material progress; consecutive without progress 0.
- Resume context: diff base `6243701`. This spec; its completion entry is in
  [history](../history/2026-11-week-02.md#2026-11-12--add-setup-skill). The queue holds no row
  for this item. Audit rules: [docs/skill-audit.md](../../skill-audit.md).
- Try it: in a project without `docs/lusona/`, run `/lusona:setup` (Claude Code, after
  `/reload-plugins` or a new session) or `$lusona:setup` (Codex CLI). Expected: the queue
  appears at `docs/lusona/work.md`, the agent asks for the two preferences, shows the section
  text and writes `AGENTS.md` and `CLAUDE.md` only after you confirm.
- Next action: owner user. Decide the open items above; request a commit when wanted; decide
  whether to delete the trial residue listed under Evidence.
