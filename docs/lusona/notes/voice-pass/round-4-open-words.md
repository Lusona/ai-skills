# Voice pass: drafted replacements for the open words (class O)

Status: APPLIED 2026-11-11 on the user's instruction (classes N, X, R and D, 32 rows). Class K is unchanged. 48 lines: 47 from a word sweep of the text after the class N rows were applied, plus 1 added in review (row 347).
The sweep used a fixed word list (safe, unsafe, clear, material, sufficient, insufficient, fresh, disposable, expensive, oversized, broader, ready, credible, ordinary, normal, when allowed). It is not a claim that no other untested word remains.
Row 347 was added in review. The last 8 uses that this listing leaves (rows 314 and 317, and six uses outside the sweep list) are decisions 19-21 in the [voice limits notes](../voice-limits-measurement.md).


## N. New criterion: no line states the test, or a second supported reading exists (named in the basis)

8 rows.

- [304] `skills/explore/SKILL.md`
  - Now: resolve a material uncertainty
  - Proposed: resolve an uncertainty that could change the direction
  - Basis: plugins/lusona/skills/explore/SKILL.md:70 (step 2) "When one missing preference could change the direction, ask the user for it." and plugins/lusona/templates/brainstorm.md.template:32 "Unknown: <question that could change the direction>". The competing wording is "an uncertainty that can change the next action" (plugins/lusona/skills/investigate/SKILL.md:58); ids 304 and 306 use the same test.
- [306] `skills/explore/SKILL.md`
  - Now: settle a material uncertainty
  - Proposed: settle an uncertainty that could change the direction
  - Basis: plugins/lusona/skills/explore/SKILL.md:70 (step 2) "When one missing preference could change the direction, ask the user for it." and plugins/lusona/templates/brainstorm.md.template:32 "Unknown: <question that could change the direction>". The competing wording is "An uncertainty that can change the next action" (plugins/lusona/skills/investigate/SKILL.md:102); ids 304 and 306 use the same test.
- [308] `skills/implement/SKILL.md`
  - Now: Verify each new step that is safe to repeat; name untested steps.
  - Proposed: Verify each new step that you can run again without a destructive action and within existing authority; name untested steps.
  - Basis: No line tests "safe to repeat". plugins/lusona/skills/implement/SKILL.md:11 "Ask the user before destructive actions" and :65 "Before an authorized persistent-data or deployment operation, establish verification and recovery" are the limits this file sets on running a step. The competing reading is a step that changes no state at all (plugins/lusona/skills/status/SKILL.md:52 "mutating checks").
- [312] `skills/specify/SKILL.md`
  - Now: Spec ready and implementation not authorized
  - Proposed: Spec meets the conditions of the Ready queue state and implementation not authorized
  - Basis: plugins/lusona/references/queue.md:36 "Ready requires accepted scope and criteria, an explicitly selected TDD level, and no blocking definition questions." plugins/lusona/references/queue.md:12 makes specify the owning skill of Ready, and plugins/lusona/skills/specify/SKILL.md:114-115 list the two unmet cases (a blocking question, TDD level unset).
- [313] `skills/specify/SKILL.md`
  - Now: Spec ready and implementation authorized
  - Proposed: Spec meets the conditions of the Ready queue state and implementation authorized
  - Basis: plugins/lusona/references/queue.md:36 "Ready requires accepted scope and criteria, an explicitly selected TDD level, and no blocking definition questions." Same test as id 312.
- [317] `references/delegation.md`
  - Now: select a more capable model when allowed and reasoning was insufficient
  - Proposed: select a more capable model when the reassessed routing selects a higher tier and no user model choice or host restriction prevents it
  - Basis: "when allowed": plugins/lusona/references/delegation.md:58 "Preserve explicit user model choices and host restrictions." "insufficient": plugins/lusona/references/delegation.md:67 "Reassess routing at dispatch and escalation." with the tier conditions at :50-52; the competing reading is the reasoning setting of :45. "oversized" is unchanged: no line states a size test, and its readings are the context limit (plugins/lusona/references/retention.md:112) and splitting off the part that the block does not affect (plugins/lusona/references/corrections.md:20 "Continue authorized work that the failure does not affect."). Coordinator note: "oversized" stays in the sentence; no line states a size test.
- [323] `references/evidence.md`
  - Now: Disposable work needs no record.
  - Proposed: Work whose result no decision relies on needs no evidence record.
  - Basis: Complement of plugins/lusona/references/evidence.md:11 "Evidence is material when a decision relies on it". "evidence record" keeps this rule apart from routine evidence, which the same line keeps "with its task". The competing reading is the scratch list of plugins/lusona/references/evidence.md:64, which id 326 uses for "disposable outputs".
- [336] `references/retention.md`
  - Now: Report the uncertainty and the next bounded action without implying broader completion.
  - Proposed: Report the uncertainty and the next bounded action, without implying that the action completes the goal.
  - Basis: No line tests "broader". plugins/lusona/references/retention.md:62 "Relate each concrete gap you find to an established goal." names the only thing larger than the bounded action. The competing reading is completion outside the inspected scope, from :64 "Do not audit the whole product unless the user asks."

## X. Existing test: the word is replaced by a test another line already states

16 rows.

- [300] `skills/design/SKILL.md`
  - Now: A draft is ready: the user inspects it at the named path or URL, owner user.
  - Proposed: A draft is open in the browser, or its path is reported: the user inspects it at the named path or URL, owner user.
  - Basis: plugins/lusona/skills/design/SKILL.md:64 states what makes a draft inspectable: "Open the draft, or the alternatives' index or switch page, in the browser before the user agrees. When the host cannot open it, report its absolute path."
- [302] `skills/explore/SKILL.md`
  - Now: Compare materially different options.
  - Proposed: Compare options that differ in more than wording.
  - Basis: plugins/lusona/skills/explore/SKILL.md:36 names the failure this rule prevents: "Options that differ only in wording."
- [305] `skills/explore/SKILL.md`
  - Now: Ordinary dialogue needs no record.
  - Proposed: Dialogue that meets no save condition needs no record.
  - Basis: plugins/lusona/templates/brainstorm.md.template:7 "Do not save discussion that meets no "When to save" condition." The same line of plugins/lusona/skills/explore/SKILL.md:75 already says "a save condition in retention".
- [310] `skills/map-capabilities/SKILL.md`
  - Now: An agreed increment is ready
  - Proposed: An agreed increment is already specified
  - Basis: The complement is plugins/lusona/skills/map-capabilities/SKILL.md:96 "The recommended outcome needs agreed behavior". plugins/lusona/skills/frame-product/SKILL.md:99 names the same condition: "already specified" (id 307).
- [316] `references/delegation.md`
  - Now: Report unfinished operations that prevent a safe shutdown.
  - Proposed: Report each operation that you cannot finish or pause in a recoverable state.
  - Basis: plugins/lusona/references/retention.md:100 "Before transfer, finish or pause each bounded operation in a recoverable state." plugins/lusona/references/delegation.md:99 names the same items in the Recovery field: "retained work, active operations and leaves".
- [326] `references/evidence.md`
  - Now: Do not commit disposable outputs.
  - Proposed: Do not commit scratch prototypes, harnesses or transient output.
  - Basis: plugins/lusona/references/evidence.md:64 lists the outputs and their location: "Put scratch prototypes, harnesses and transient output under the repository's `tmp/` unless the project names another ignored directory."
- [330] `references/evidence.md`
  - Now: Do not replace the material method, provenance and results with a conclusion.
  - Proposed: Do not replace the method, provenance and results that support a decision with a conclusion.
  - Basis: plugins/lusona/references/evidence.md:61 "Retain the methods, provenance, results and material artifacts that support the decision." Here "material" modifies a method and provenance, which the definition at :11 (evidence) does not cover.
- [333] `references/queue.md`
  - Now: Evidence ready for review or acceptance
  - Proposed: Verification evidence saved; review or acceptance remains
  - Basis: plugins/lusona/references/queue.md:47 "Move work to Review when its verification evidence is saved in the owning record and review or acceptance remains."
- [335] `references/retention.md`
  - Now: Ordinary explanations, greetings, acknowledgments, disposable questions and status updates need no record.
  - Proposed: Explanations, greetings, acknowledgments, questions and status updates that no later work or other session depends on need no record.
  - Basis: plugins/lusona/references/retention.md:7 "An output is substantive when later work or another session depends on it".
- [337] `references/retention.md`
  - Now: Ask the user only for material facts or authority that the records cannot supply.
  - Proposed: Ask the user only for authority, or for a fact that changes the next action, when the records cannot supply it.
  - Basis: plugins/lusona/skills/status/SKILL.md:55 "Ask only when an ambiguity changes the next action." and the Progress rule at plugins/lusona/skills/status/SKILL.md:19 "Stop inquiry that cannot change the next action."
- [338] `skills/batch/references/deferral-and-resumption.md`
  - Now: When isolation or restoration is unsafe, stop all affected work.
  - Proposed: When you cannot isolate the unfinished changes, or cannot prove that restoration loses no other writer's changes, stop all affected work.
  - Basis: plugins/lusona/skills/batch/references/deferral-and-resumption.md:9 "Release ownership only after the unfinished changes are isolated." and plugins/lusona/skills/batch/references/integration.md:40 "after proving that no other writer's changes will be lost".
- [339] `skills/batch/references/integration.md`
  - Now: When safe restoration cannot be established, stop the batch.
  - Proposed: When you cannot prove that restoring the destination loses no other writer's changes, stop the batch.
  - Basis: plugins/lusona/skills/batch/references/integration.md:40 "restore the destination by removing only the candidate's attributable changes, after proving that no other writer's changes will be lost."
- [340] `templates/batch.md.template`
  - Now: proving safe separation
  - Proposed: proving that writers stopped and unfinished changes are isolated
  - Basis: plugins/lusona/skills/batch/references/deferral-and-resumption.md:11 "once its writers stop and its unfinished changes are isolated", and the column heading at plugins/lusona/templates/batch.md.template:68 "Writer cessation and isolated changes".
- [345] `templates/review.md.template`
  - Now: any material verification limitation
  - Proposed: any unrun required check or verification gap
  - Basis: plugins/lusona/templates/review.md.template:36 "Not checked: <unrun required checks and remaining verification gaps>" and plugins/lusona/skills/review/SKILL.md:73 "Report verification gaps separately".
- [346] `templates/status.md.template`
  - Now: fresh checks
  - Proposed: verified results
  - Basis: plugins/lusona/skills/status/SKILL.md:59 "Separate recorded claims from verified results." and :33 "A recorded claim is not a verified result."
- [347] `skills/design/SKILL.md`
  - Now: Continue without another command.
  - Proposed: Continue without a new user request.
  - Basis: references/evidence.md and references/workflow-guide.md now say "need no new user request" for the same idea (rows 109 and 129, applied). This is the last use of "command" for a user instruction.

## R. Reworded: the word is removed or replaced and the rule is the same

7 rows.

- [301] `skills/experiment/SKILL.md`
  - Now: Revert only your own disposable edits and report anything left behind.
  - Proposed: Revert only your own temporary edits and report anything left behind.
  - Basis: The preceding sentence on the same line names the edits: "Keep temporary edits isolated." plugins/lusona/skills/investigate/SKILL.md:62 states the parallel rule without the word: "revert only your own diagnostic edits".
- [303] `skills/explore/SKILL.md`
  - Now: a material external claim
  - Proposed: an external claim
  - Basis: The same sentence already states the test: "affects the direction". plugins/lusona/skills/explore/SKILL.md:33 treats every unverified external claim alike: "An unverified external claim is an assumption".
- [307] `skills/frame-product/SKILL.md`
  - Now: An already specified outcome is ready
  - Proposed: An outcome is already specified
  - Basis: "already specified" states the condition; the complement is plugins/lusona/skills/frame-product/SKILL.md:98 "The first outcome needs agreed behavior". plugins/lusona/skills/implement/SKILL.md:55 routes back to specify "When intended behavior or scope is missing", so "ready" adds no second test.
- [318] `references/delegation.md`
  - Now: An ordinary Claude Code agent outside a team
  - Proposed: A Claude Code agent outside a team
  - Basis: "outside a team" already separates this case from plugins/lusona/references/delegation.md:139 "a persistent Claude Code agent team member", and :138 has the agent "Inspect the actual agent type".
- [328] `references/evidence.md`
  - Now: in disposable scratch storage
  - Proposed: in scratch storage
  - Basis: plugins/lusona/references/evidence.md:64 defines the storage as the repository's `tmp/` or "another ignored directory"; "disposable" adds no second condition to "scratch storage".
- [334] `references/queue.md`
  - Now: An ordinary spec edit does not reset or reopen work.
  - Proposed: A spec edit alone does not reset or reopen work.
  - Basis: plugins/lusona/references/queue.md:51 "Completed items stay Done unless explicitly reopened." and :52 "Reopening requires explicit authority." leave no kind of spec edit that resets or reopens work. "alone" follows :41 "A recovery note alone" and :64 "A batch deferral alone".
- [341] `templates/brainstorm.md.template`
  - Now: material cost or limitation
  - Proposed: cost or limitation
  - Basis: plugins/lusona/skills/explore/SKILL.md:71 states the same content without the qualifier: "When each option has a stated benefit and cost".

## D. Delete: the sentence repeats a rule stated completely elsewhere

1 rows.

- [332] `references/naming.md`
  - Now: Do not start one during normal work.
  - Proposed: (deleted)
  - Basis: The first sentence of plugins/lusona/references/naming.md:49 already limits a migration: "only in an authorized migration". plugins/lusona/references/files.md:47 "Read and update existing records in place, without migration." and :50 "Split or move existing records only when the user requests it." state the same limit, and no line tests "normal work".

## K. Keep: the word is defined, or the files do not support one reading

16 rows.

- [309] `skills/investigate/SKILL.md`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". plugins/lusona/skills/investigate/SKILL.md:52 has the agent read the Study entry rules, which hold that definition, before the first probe.
- [311] `skills/measure/SKILL.md`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". plugins/lusona/skills/measure/SKILL.md:44 has the agent read that reference before the measurement starts.
- [314] `skills/status/SKILL.md`
  - Basis: No line states a cost test. Three readings compete: (1) a check that needs a resource budget or authority beyond "available tools and inputs" (plugins/lusona/references/evidence.md:7 and :9); (2) a check whose recorded result is still valid, from plugins/lusona/references/delegation.md:121 "Reuse a valid check result when its inputs are unchanged", which tests validity and not cost; (3) delete "expensive or", which leaves the first sentence of plugins/lusona/skills/status/SKILL.md:52 ("only where the question depends on them") as the only limit on non-mutating checks.
- [315] `references/corrections.md`
  - Basis: This line is the definition of "material progress" that plugins/lusona/references/corrections.md:9, :14 and :19 and plugins/lusona/references/delegation.md:100 rely on.
- [319] `references/evidence.md`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". The definition is 8 lines below in the same file, and plugins/lusona/README.md:47 repeats this trigger word for word, so a change here would need the same change there.
- [320] `references/evidence.md`
  - Basis: This line is the definition of material evidence: "Evidence is material when a decision relies on it".
- [321] `references/evidence.md`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". The heading names the defined thing.
- [322] `references/evidence.md`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". The definition is 7 lines above in the same file.
- [324] `references/evidence.md`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". The definition is in the same file.
- [325] `references/evidence.md`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". The same sentence restates the test: "that support the decision".
- [327] `references/evidence.md`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". The definition is in the same file.
- [329] `references/evidence.md`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". The definition is in the same file.
- [331] `references/files.md`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". The cell describes the directory; the rule is plugins/lusona/references/evidence.md:75 "`docs/lusona/evidence/` holds material decision evidence, not every command output."
- [342] `templates/evidence.md.template`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". plugins/lusona/skills/measure/SKILL.md:68 and plugins/lusona/skills/experiment/SKILL.md:44 have the agent read that reference before this template is used.
- [343] `templates/evidence.md.template`
  - Basis: The line is a template `Label:` field name, which may not change. plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it".
- [344] `templates/notes.md.template`
  - Basis: plugins/lusona/references/evidence.md:11 defines the term: "Evidence is material when a decision relies on it". plugins/lusona/skills/investigate/SKILL.md:52 and plugins/lusona/skills/measure/SKILL.md:44 have the agent read that reference before notes for a measurement or experiment are written.
