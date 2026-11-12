# README rule destinations

Work item W5 of [spec 20261111](../docs/lusona/specs/20261111-loop-principles-and-skill-rewrite.md).
Rows: readme-001 to readme-187 of the [rule inventory](../docs/lusona/notes/rule-inventory-34186da.md); rule text is there.

Destination types: Block (every-task block line label; "Block (implied)" means the line implies the rule without stating it), Final reply (shared final-reply region),
Skill text (named skills), Reference (name; existing at `34186da` or new), README catalog (human documentation, W10), Removed (reason).
Block and Final reply text: `drafts/shared/every-task.md`, `drafts/shared/final-reply.md`.

## P-conflict rows

| Row | Conflict | Resolution |
| --- | --- | --- |
| readme-041 | P3: trigger limited to evidence | Block Decisions: "When new input contradicts an accepted decision"; input includes a requirement, specification, measurement or experiment |
| readme-042 | P3: "reopen within authority" omits the user | Block Decisions: "neither reject the input nor bypass the decision ... revisit it with the user" (decision 6) |
| readme-044 | P4: keeps only useful rationale, no date and source | Reference revisions (new): mark the superseded decision with date and source and keep its rationale; the block links it before recording the outcome |
| readme-155 | P8: None form omits the reason | Final reply: `**Next action:** None for this request` and a one-sentence reason |

## Rows

| ID | Lines | Kind | Destination |
| --- | --- | --- | --- |
| readme-001 | L5-L6 | rule | Removed: the read-once loading model is replaced by the block generated into each SKILL.md (S1) |
| readme-002 | L6-L7 | rule | Removed: the read-once loading model is replaced by the block generated into each SKILL.md (S1) |
| readme-003 | L7-L8 | rule | Removed: lookup through the README catalog is replaced by trigger links in skills (S2); the catalog stays in the README for humans (W10) |
| readme-004 | L8 | rule | Block: References ("Read each linked reference before its named action") |
| readme-005 | L8-L9 | rule | Reference: interviews (interview-examples merged in), workflow-guide (existing): each states that it may be read in part |
| readme-006 | L9 | rule | Reference: delegation (existing), Assignment contract |
| readme-007 | L11 | definition | Block: Role (role set only by an assignment naming a leaf); detail in reference delegation |
| readme-008 | L11-L12 | rule | Block: Role (role set only by an assignment naming a leaf); detail in reference delegation |
| readme-009 | L12 | rule | Reference: delegation (existing), Assignment contract |
| readme-010 | L14 | rule | Reference: delegation (existing), Assignment contract |
| readme-011 | L14 | definition | Reference: delegation (existing), Assignment contract |
| readme-012 | L15 | rule | Reference: delegation (existing), Assignment contract |
| readme-013 | L15-L16 | rule | Reference: delegation (existing), Assignment contract |
| readme-014 | L16 | rule | Reference: delegation (existing), Assignment contract |
| readme-015 | L17 | rule | Removed: host and project instructions bind the agent without plugin text; restating gives no action (open question Q2) |
| readme-016 | L17 | definition | Reference: workflow-guide (existing), Terminology |
| readme-017 | L17 | definition | Reference: workflow-guide (existing), Terminology |
| readme-018 | L18 | rule | Reference: queue (existing), selection |
| readme-019 | L20 | rule | Skill text: every skill, `## Establish <input>` (skills for unresolved needs) and `## Final reply` valid next actions (P1) |
| readme-020 | L20-L21 | rule | Skill text: status (unclear skill selection: read workflow-guide); reference: workflow-guide (existing), Routing |
| readme-021 | L21-L22 | rule | Removed: implied by the readme-020 trigger, which applies only when selection is unclear |
| readme-022 | L26-L27 | rule | Skill text: every skill, `## Establish <input>` reads carried state (template, P2); reference: retention, Handoff and checkpoint (handoff merged in) for handoff content |
| readme-023 | L27 | rule | Block: Authority (no authority from records); "skills are not phases": reference workflow-guide (existing), Terminology (P1) |
| readme-024 | L28 | rule | Block: Questions |
| readme-025 | L28-L29 | rule | Reference: interviews (existing) |
| readme-026 | L29 | rule | Skill text: every skill, `## Establish <input>` ("Reuse settled decisions"; implement has it) |
| readme-027 | L31 | rule | Block: Progress |
| readme-028 | L31-L32 | rule | Skill text: implement, Persona and judgment Decision criteria (judge against agreed behavior); Block (implied): Evidence |
| readme-029 | L32-L33 | rule | Block: Progress |
| readme-030 | L33 | rule | Block: Progress |
| readme-031 | L33-L34 | definition | Block (implied): Progress ("Take the next bounded authorized action unprompted"); not stated as a sentence |
| readme-032 | L34-L35 | rule | Reference: revisions (new): follow-up input is steering unless it cancels or replaces the objective; trigger in the `## Establish` section of architect, design, experiment, implement, investigate, measure, refactor and specify (W13 F3) |
| readme-033 | L35 | rule | Reference: revisions (new): follow-up input is steering unless it cancels or replaces the objective |
| readme-034 | L37 | rule | Block: Progress ("Pause only affected work; state what resumes it"); status Paused in Final reply |
| readme-035 | L38 | rule | Block: Progress ("Pause only affected work; state what resumes it"); status Paused in Final reply |
| readme-036 | L38-L39 | rule | Block: Questions and Block: Progress |
| readme-037 | L39 | rule | Final reply (status meanings: Paused and In progress are not Complete) |
| readme-038 | L39 | rule | Skill: batch (Repairs and deferral; per-skill reference deferral-and-resumption) |
| readme-039 | L39-L41 | rule | Skill text: implement (step 5), refactor, batch; reference: corrections (existing) |
| readme-040 | L41 | rule | Skill text: implement (step 5), refactor, batch; reference: corrections (existing) |
| readme-041 | L43 | rule | Block: Decisions. P3 resolved: trigger widened from evidence to any new input (requirement, specification, measurement, experiment) |
| readme-042 | L43-L44 | rule | Block: Decisions. P3 resolved (decision 6): "reopen within authority" replaced by "revisit it with the user" |
| readme-043 | L44-L45 | rule | Reference: revisions (new), P4 |
| readme-044 | L45 | rule | Reference: revisions (new), P4. Resolved: mark the superseded decision with date and source and keep its rationale (not only "useful" rationale) |
| readme-045 | L45 | rule | Reference: revisions (new), P4 |
| readme-046 | L46 | rule | Reference: revisions (new), P4 |
| readme-047 | L46 | definition | Reference: revisions (new), P4 |
| readme-048 | L48-L49 | rule | Reference: retention (existing) |
| readme-049 | L50 | rule | Block: Saving |
| readme-050 | L50-L51 | rule | Block: Saving |
| readme-051 | L51 | rule | Reference: retention (existing); "by default" removed (V5) |
| readme-052 | L51-L53 | rule | Reference: retention (existing); proposed follow-ups labelled in Final reply |
| readme-053 | L55 | rule | Skill text: measure, experiment, investigate; reference: evidence (existing) |
| readme-054 | L56 | rule | Block (implied): Authority (the ask list is closed, so routine choices need no approval); not stated as a sentence |
| readme-055 | L56-L57 | rule | Block: Questions ("State an assumption ... and continue") |
| readme-056 | L59 | rule | Skill text: implement, Planning practices ("Revise the approach as evidence changes, within authority") |
| readme-057 | L59-L60 | definition | Skill text: implement (description and Planning practices) |
| readme-058 | L60-L61 | rule | Skill text: implement, Planning practices (execution section triggers) |
| readme-059 | L62 | rule | Skill text: implement, Planning practices ("For clear work ... write no task list"); V7 resolved by the stated triggers for an execution section |
| readme-060 | L62 | rule | Block: Saving |
| readme-061 | L66 | rule | Skill text: every skill, `## Establish <input>` (template line; implement has it) |
| readme-062 | L67 | rule | Skill text: every skill, `## Establish <input>` (template line; implement has it) |
| readme-063 | L67 | rule | Removed: the read-once loading model no longer exists (S1) |
| readme-064 | L68 | definition | Block (implied): Authority (the user decides the listed changes); not stated as a sentence |
| readme-065 | L68-L70 | rule | Block: Authority |
| readme-066 | L70 | rule | Removed: host prompts are enforced by the host; restating gives no action (open question Q2) |
| readme-067 | L71 | rule | Skill text: implement (step 8), refactor; reference: commits (existing), staging |
| readme-068 | L71-L72 | rule | Block (implied): Authority (routine choices are outside the ask list); not stated as a sentence |
| readme-069 | L72 | rule | Skill text: template note for `## <Procedure> and record` ("in order only where order matters") |
| readme-070 | L73-L74 | rule | Block: Authority (K4 sentence); "including Ready": reference queue (existing); discussion and read-only review: reference workflow-guide (existing) |
| readme-071 | L74 | rule | Skill text: implement (description; Planning practices, planning-only stops before execution) |
| readme-072 | L74 | rule | Block (implied): Progress ("unprompted"); stated in reference workflow-guide (existing) |
| readme-073 | L75-L76 | rule | Skill text: implement (step 11), refactor; reference: commits (existing) |
| readme-074 | L76 | rule | Reference: commits (existing) |
| readme-075 | L76-L77 | rule | Skill text: implement (step 11), refactor; reference: commits (existing) |
| readme-076 | L77-L78 | rule | Skill text: implement (step 11), refactor; reference: commits (existing) |
| readme-077 | L79 | rule | Reference: files (existing) |
| readme-078 | L79-L80 | definition | Reference: files (existing) |
| readme-079 | L80 | rule | Reference: files (existing) |
| readme-080 | L80-L81 | rule | Reference: queue (existing), shared-state ownership |
| readme-081 | L81-L82 | rule | Reference: delegation, Assigned leaves (queue copy removed, V8, W13 F7) |
| readme-082 | L83-L85 | rule | Block: Saving; "proportionate to the work" removed (V5) |
| readme-083 | L85-L86 | rule | Block: Saving (trigger: before handoff or completion); V5 "when it becomes useful" replaced by that trigger; synthesis rule in reference retention (existing) |
| readme-084 | L86 | rule | Block: Saving |
| readme-085 | L86-L88 | rule | Block: Saving |
| readme-086 | L88 | rule | Block: Saving |
| readme-087 | L89 | rule | Block: Role (leaf returns results to the coordinator); reference: delegation (existing) |
| readme-088 | L90 | rule | Skill text: implement, specify (spec trigger); reference: queue (existing) |
| readme-089 | L91 | rule | Skill text: architect; reference: retention (existing) |
| readme-090 | L91-L92 | rule | Reference: retention (existing) |
| readme-091 | L92 | rule | Reference: retention (existing) |
| readme-092 | L96 | rule | Removed: catalog label; the README catalog is human documentation (W10, S3) |
| readme-093 | L96 | rule | Block: References |
| readme-094 | L97 | rule | Reference: delegation (existing), Assignment contract |
| readme-095 | L97 | definition | Removed: README path note; catalog stays in README for humans (W10) |
| readme-096 | L99 | not a rule | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-097 | L101 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-098 | L102 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-099 | L103 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-100 | L104 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-101 | L105 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-102 | L106 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-103 | L107 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-104 | L108 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-105 | L109 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-106 | L110 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-107 | L111 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-108 | L112 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-109 | L113 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-110 | L114 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-111 | L115 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-112 | L116 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-113 | L117 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-114 | L118 | catalog | README catalog (human documentation, W10); each reference trigger moves into the skill or block that links it (S2) |
| readme-115 | L120-L121 | definition | Skill: batch (description and per-skill references; batch-execution replaced, W8) |
| readme-116 | L121 | rule | Skill: batch (every-task block TDD, Authority and Evidence lines apply; W8) |
| readme-117 | L125 | rule | Final reply ("End every task reply with this form"); V6 "natural" removed |
| readme-118 | L126-L127 | rule | Block: Questions and Block: Progress |
| readme-119 | L127-L128 | rule | Block: Progress ("unprompted") and Block: Saving ("unasked") |
| readme-120 | L128-L129 | rule | Final reply (None form with a one-sentence reason) |
| readme-121 | L129-L130 | rule | Final reply (the form applies to task replies; greetings, acknowledgments and other non-task replies take no form and no invented follow-up; decision 16 Q5, W13 F13) |
| readme-122 | L130 | rule | Final reply (proposed follow-up labelled, missing authority stated) |
| readme-123 | L132-L133 | rule | Block: Questions ("native question tool"); host tool names move to reference interviews (existing) |
| readme-124 | L133 | rule | Reference: interviews (existing) |
| readme-125 | L133-L134 | rule | Block: Authority and Block: Questions |
| readme-126 | L134 | rule | Block: Questions ("recommending an answer"); V5 "when useful" removed: always recommend |
| readme-127 | L134-L135 | rule | Block: Questions |
| readme-128 | L135 | rule | Reference: interviews (existing) |
| readme-129 | L135-L136 | rule | Reference: interviews (existing) |
| readme-130 | L136 | rule | Block (implied): Questions ("Ask through the native question tool"); not stated as a separate sentence |
| readme-131 | L140 | rule | Block: TDD |
| readme-132 | L141 | rule | Block: TDD |
| readme-133 | L141 | rule | Block: TDD |
| readme-134 | L145-L146 | rule | Block: Evidence (completion definition) |
| readme-135 | L146 | rule | Block: Evidence (completion definition) |
| readme-136 | L147 | rule | Block: Evidence (completion definition) |
| readme-137 | L147 | rule | Skill text: implement step 8 (final diff inspection) and Failure modes; Block (implied): Evidence |
| readme-138 | L147-L149 | rule | Reference: delegation (existing), independent review conditions; trigger in implement `## Establish` (entry and scope growth) |
| readme-139 | L149 | rule | Reference: delegation (existing), independent review conditions; trigger in implement `## Establish` (entry and scope growth) |
| readme-140 | L149-L150 | rule | Reference: delegation (existing), independent review conditions; trigger in implement `## Establish` (entry and scope growth) |
| readme-141 | L150 | rule | Block: Role ("never satisfies independent review"); reference: delegation (existing) |
| readme-142 | L150 | rule | Skill text: implement (steps 4-5); reference: corrections (existing) |
| readme-143 | L152 | rule | Final reply ("Put a blocking decision or approval first") |
| readme-144 | L152-L154 | rule | Final reply (Result, Evidence, next-action table fields; `**Decisions:**` and `**Open issues:**` lines after Evidence, W13 F14) |
| readme-145 | L154-L155 | rule | Final reply (continuation directive); reference: retention, Handoff and checkpoint |
| readme-146 | L155-L156 | rule | Block: Questions ("Answer direct questions first") and Block: Progress |
| readme-147 | L156-L157 | rule | Skill text: implement valid next actions ("give concrete steps and expected results") |
| readme-148 | L157-L158 | rule | Reference: closeout (existing) |
| readme-149 | L160-L161 | rule | Final reply; resolved: "default to" removed, the form applies to every task reply (20261110 decision 3) |
| readme-150 | L162-L163 | rule | Final reply |
| readme-151 | L164 | rule | Final reply |
| readme-152 | L165 | rule | Final reply |
| readme-153 | L165-L166 | definition | Final reply (follow-up after complete scope) |
| readme-154 | L166-L167 | rule | Final reply (blockquote below the table) |
| readme-155 | L167-L168 | rule | Final reply. P8 resolved: `None for this request` requires a one-sentence reason (readme-120) |
| readme-156 | L169-L170 | rule | Final reply (K4 statuses); status glyphs kept with each status word (spec decision 16) |
| readme-157 | L170-L171 | definition | Final reply ("Status describes this reply, not the queue state") |
| readme-158 | L171-L172 | definition | Final reply ("Status describes this reply, not the queue state") |
| readme-159 | L172 | rule | Final reply: status glyphs kept (spec decision 16); each status word and its stated meaning carry the meaning, so the separate sentence is removed (V6) |
| readme-160 | L174 | rule | Final reply (lists and tables), per kept 20261110 decision 10: formatting in Final reply |
| readme-161 | L174-L176 | rule | Skill text: status, `## Final reply` after the region (status summary columns) |
| readme-162 | L176 | rule | Final reply (comparison columns; specialized tables kept) |
| readme-163 | L176-L177 | rule | Final reply (comparison columns; specialized tables kept) |
| readme-164 | L177 | rule | Final reply (user and host formatting override) |
| readme-165 | L177-L179 | rule | Final reply ("When tables do not render ...") |
| readme-166 | L179-L180 | definition | Removed: gives no action (V6); the Final reply form defines the reply |
| readme-167 | L180-L181 | rule | Final reply (leaf line); reference: delegation (existing), Assignment results |
| readme-168 | L185 | rule | Block: Role and Final reply (leaf line); reference: delegation (existing) |
| readme-169 | L186 | rule | Block (implied): the block is generated into every skill, so a leaf applies all of it; not stated as a sentence |
| readme-170 | L186-L187 | rule | Block: Role ("return questions, conflicts and next actions to the coordinator") |
| readme-171 | L187-L188 | rule | Reference: delegation (existing), Assigned leaves |
| readme-172 | L192-L193 | rule | Reference: delegation (existing), coordinator duties |
| readme-173 | L193-L196 | rule | Block: Role ("Delegate specialist work at every task size", 20261110 decision 4). Proposal: the task-local check exception is removed (from the discarded part of 20261110 decision 10); study entry stays in reference evidence (existing) |
| readme-174 | L196 | rule | Reference: delegation (existing), Assignment contract |
| readme-175 | L196-L197 | rule | Removed by 20261110 decision 4 (delegation at every task size); conversation with the user stays with the coordinator by the block Role line (open question Q3) |
| readme-176 | L197 | definition | Reference: delegation (existing) |
| readme-177 | L199 | rule | Block: Role |
| readme-178 | L199-L200 | rule | Block: Role |
| readme-179 | L200 | definition | Reference: delegation, Coordinator duties (worker-lifecycle merged in, Q1) |
| readme-180 | L201 | rule | Reference: delegation, Coordinator duties (worker-lifecycle merged in, Q1) |
| readme-181 | L201-L202 | rule | Block: Role (dispatch trigger to delegation); model routing: reference delegation, Model routing (model-routing merged in, Q1) |
| readme-182 | L203-L204 | rule | Reference: delegation, Leaf lifecycle (worker-lifecycle merged in, Q1) |
| readme-183 | L205 | rule | Block: Role ("As a leaf, delegate only when your assignment grants it"; decision 20, W13 F1) |
| readme-184 | L209 | rule | Reference: retention, Context budget; V5 "around 40%" replaced by "at 40%" |
| readme-185 | L209 | rule | Reference: retention, Context budget |
| readme-186 | L210 | rule | Reference: retention, Context budget |
| readme-187 | L210-L211 | rule | Reference: retention, Context budget and trigger line (handoff merged in, Q1), linked by the block Saving line |

Count: 187 rows. First destination type per row: Block 54, Final reply 24, README catalog 19, Reference 52, Removed 12, Skill text 26.
