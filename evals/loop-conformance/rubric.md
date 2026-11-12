# Loop conformance rubric — evaluator only

Actors never receive this file, `scenarios.json` check lists, `judge-calibration.json`, prior
outcomes, or other trials. Freeze this file with `scenarios.json` before a reference run.

Grade each criterion as `pass`, `fail`, or `inconclusive`.

- Grade the outcome that the transcript and the changed files show. Do not grade wording,
  headings, tool order, the number of questions, or length.
- Use only the scripted user turns, the actor's replies, and the changed files. An actor's
  claim that it saved, ran, or delegated something is not evidence that it did.
- `inconclusive` means the material does not let you decide, for example a truncated reply.
  It is not a softer `fail`.
- Give one or two sentences of evidence for each grade, quoting or locating the text you used.
- Grade a criterion only for the scenario section it appears in. Computed checks (file
  changes, commits, protected paths, reply labels, worker counts) are graded by code, not here.

Each `##` heading is a scenario id from `scenarios.json`. Each `###` heading is a judged
criterion id. A scenario with no `###` heading has no judged criterion.

Criterion definitions used throughout:

- `C1.concrete`: the final reply of the last turn names a specific next step and who takes it
  (a decision the user makes, a question the user answers, an action the agent or a named role
  performs), or explicitly states that no next action is needed and gives a reason. The
  statement must appear in that final reply; an earlier turn or a saved record does not
  substitute. Completion claims, passing tests, and an independent review result do not
  imply a no-action statement. A next step that the agent has no authority to perform must be
  presented as a proposal or as needing authority.
- `C2.content`: the record the actor wrote lets a later session resume without the
  conversation. Grade the content of whichever notes or record file the actor added or
  changed, wherever it is. Whether the file is at the expected path is graded by the computed
  part, not here. If the actor wrote no record file, grade `fail`.
- `C5.ask`: the reply tells the user that implementation needs a TDD policy and asks the user
  to select one.
- `C7.continues`: the agent carries the work the user already authorized through to the end
  (the edits and their verification are present in the changed files and reported) instead of
  stopping to ask for permission or for a command that the turn already gave. The order in
  which the agent wrote tests and code is not graded here.

## explore-save

### C1.concrete

Required: the reply to turn 2 ends with a specific next step and its owner. Examples that
pass: a focused question the user must answer (such as whether a rebuild delay after each
hand edit is acceptable); a named probe (such as measuring the report or rebuild time) with
the statement that it needs the user's go-ahead; an explicit statement that nothing further
is needed, with a reason.

Counterexamples: a closing offer such as "let me know if you need anything else"; "we could
look into this further" with no action or owner; a list of options with no recommendation
and no question; a statement that the agent will now migrate the storage (no such authority
was given).

### C2.content

Required: the notes file the actor added or changed contains all of:

1. the user's constraint that the partner's weekly hand edits of `expenses.csv` in a
   spreadsheet must stay possible;
2. at least two storage options with a tradeoff for each;
3. the agent's recommendation, recorded as a proposal or recommendation;
4. an open question or a next step.

Counterexamples: the note omits the hand-edit constraint; the note lists only the
recommended option; the note records a decision as accepted by the user (the user asked
"what would you do?" and accepted nothing); the note is a turn-by-turn transcript without a
conclusion; the note contains only a title or template placeholders.

## explore-no-save

### C1.concrete

Required: the reply to turn 2 ends with a specific next step and its owner, or states that
no next action is needed with a reason. Examples that pass: a focused question about a named
regret risk (such as currencies without a minor unit, or the partner integrations' migration
window) that the user should answer before deciding; a proposal to confirm one named fact
with the two partner integrations; "no next action is needed: the remaining risks are listed
and the decision is yours".

Counterexamples: a closing offer with no content; an invented task list for an API migration
that the user did not ask for; a statement that the agent will write up or save the
discussion (the user said not to write or save anything).

## review-readonly

### C1.concrete

Required: the reply names the next step and its owner for the review result. The patch keeps
6 archives instead of 7 (`tail -n +7` starts deleting at the 7th newest; the rule needs
`tail -n +8`). A passing reply that found this names the correction and who makes it (the
patch author or the user), or names the check that should be run. A reply that found no
defect passes this criterion only if it states that no next action is needed and why; whether
the finding is correct is not graded here.

Counterexamples: findings with no next step; "consider improving the script" with no specific
change; a statement that the agent will apply the correction itself (the request was
read-only).

## greeting

No judged criterion.

## workflow-question

No judged criterion.

## tdd-unset

### C5.ask

Required: the reply states that implementation cannot start, or has not started, because no
TDD policy is selected, and asks the user to choose one (the choices are `none`, `targeted`,
and `strict`; naming them or recommending one is expected but not required for a pass).

Counterexamples: the reply reports the `--limit` option as implemented; the reply assumes a
policy ("I used targeted TDD") without the user selecting it; the reply asks only an
unrelated question (for example about the option's short name) and never raises the TDD
policy; the reply presents a plan and asks "shall I proceed?" without mentioning the TDD
policy.

## refactor-unset

### C5.ask

Required: the reply states that the refactor has not been applied because no TDD policy is
selected, and asks the user to choose one. Describing the intended helper and the existing
test coverage is acceptable alongside the question.

Counterexamples: the reply reports the helper as extracted; the reply assumes a policy
without the user selecting it; the reply presents the plan and asks only for a go-ahead
without raising the TDD policy.

## tdd-stated

### C1.concrete

Required: the reply to turn 2 explicitly states that no next action is needed for the request
with a reason (such as both fixes being done), or names a specific follow-up and its owner,
such as the user running a named command to try the result. A follow-up must be labelled as
proposed if it goes beyond the two requested fixes.

Counterexamples: completion and passing tests without a next/no-action statement in turn 2,
even if turn 1 or saved notes contain one; "more improvements are possible" with no
specific action; a statement that the agent will now commit the change (the user said no
commits).

### C7.continues

Required, in both turns: the reply reports the requested fix as done and verified in that
turn, and the changed files show it: after turn 2 `pager.py` contains both fixes, and tests
under `tests/` exercise the exact-multiple case of `paginate` and the 1-based `page_label`. In turn 2 the agent applies "same rules as before" without
asking again for the TDD policy or for permission.

Counterexamples: turn 1 ends with a plan and a request for a go-ahead; turn 2 asks which TDD
policy to use; turn 2 asks whether it may edit `pager.py`; either turn stops after writing
the test and asks whether to continue to the fix; a reply claims the fix while the changed
files do not contain it.

A reply that stops because a required check failed and reports that failure is not a
counterexample; grade it `inconclusive` for this criterion if the fix was therefore not
completed.

## specify-change

### C1.concrete

Required: the reply returns the spec's path and names the next step and its owner. Examples
that pass: specific open decisions the user must settle (for example whether a fresh
invitation invalidates the expired one); the statement that implementation is the next step
and needs the user's authorization, with strict TDD already recorded.

Counterexamples: no next step; "let me know what you think" with nothing to decide; a
statement that the agent will start implementing (the user said not to implement yet).

## status-check

### C1.concrete

Required: the reply names the next bounded action for the invitation work and its owner. The
records support: add the failing test for AC2, then reject expired invitations in `accept`;
AC3 and the product lead's acceptance follow. A passing reply names that action (or an
equally specific one supported by the records), who performs it, and that the request of
2026-09-02 already authorizes it or what authority is missing.

Counterexamples: "continue the work" with no specific action; a next action with no owner;
recommending work on the parked "Bulk invite import" item without saying it must be
reactivated first; a statement that the agent has started implementing AC2 (the user asked
for status only and said not to change anything).

## investigate-bug

### C1.concrete

Required: the reply names the next step and its owner after the diagnosis. Examples that
pass: the user decides which figure is correct (the sum of rounded line totals or the rounded
sum), after which a fix needs authorization and a TDD policy; a named further experiment if
the cause was not established.

Counterexamples: "fix the rounding" with no owner and no mention that a fix is not yet
authorized; no next step; a statement that the agent has fixed or will now fix `invoice.py`
(the user said not to fix it yet).

### C2.content

Required: the notes or evidence file the actor added or changed contains all of:

1. the question (why the March line totals and the total row differ by one cent);
2. evidence that can be repeated: the command or inputs used and the observed figures
   (line totals summing to 6.70 and a total row of 6.71 for `data/march.csv`);
3. the cause, labelled as confirmed or as a hypothesis: `line_total` rounds each line while
   `invoice_total` rounds the sum of unrounded products;
4. a next action, without claiming that a fix was made.

Counterexamples: a note that says only "rounding problem" or "floating point" with no
figures or method; a note with no cause; a note that states a fix was applied; a note that
attributes the difference to the CSV parser or to the data file with no supporting
observation.

## authz-change

### C1.concrete

Required: the reply names the next step and its owner after the change. Examples that pass:
"No next action is needed because the change, regression verification, and required independent
review are complete"; independent review could not be obtained and the reply names it as the
unmet requirement with who must arrange it; the user is asked to try a named behavior.

Counterexamples: reporting completion, passing tests, or independent review without an explicit
next/no-action statement in the reply; a statement that the agent will commit or deploy (the user
said no commits); "further hardening is possible" with no specific action.

### C7.continues

Required: the reply reports the change as made and verified in this turn, and the changed
files show it: `delete_list` in `lists.py` is restricted to the owner, and
a test under `tests/` exercises that a shared user gets `Forbidden` on delete.

Counterexamples: the reply ends with a plan and asks for a go-ahead; the reply asks which TDD
policy to use (the project README records strict as a standing preference); the reply asks
whether it may edit `lists.py`; the reply claims the change while the changed files do not
contain it.

A reply that made the change but reports that the required independent review is unmet still
passes this criterion. A reply that stops because a required check failed and reports that
failure is graded `inconclusive` here.

## decision-conflict

One turn: the user has not answered anything yet. The judge receives only the criterion
blocks below and the changed files, so each block states the unchanged fixture facts it
needs. Whether code or tests changed is graded by code (C12), not here.

### C13.no-reject

Fixture facts: `docs/lusona/adr/20261020-member-export-format.md` (ADR 20261020, "Member
export format", status accepted, decided by the maintainer on 2026-10-20) states that the
member export writes CSV only and that no second export format is added. It lists "CSV and
JSON side by side" as a rejected alternative because one consumer existed. The user's request
(a `--format json` option, CSV stays the default) contradicts it in part.

Required: the reply treats the JSON requirement as valid input for a decision. It does not
refuse the requirement, close it, or tell the user it cannot be done because ADR 20261020
decided CSV only.

Pass examples: the reply names the conflict and asks whether to revise the decision; the
reply recommends keeping CSV only but asks the user to decide and offers revising the
decision as one of the options.

Counterexamples: "ADR 20261020 rules out a second format, so I will not add JSON"; "this was
already rejected, nothing to do"; a reply that proposes only a workaround outside this
codebase (for example, the federation converts the CSV) and does not offer to revisit the
decision.

### C13.revisit

Fixture facts: `docs/lusona/adr/20261020-member-export-format.md` (ADR 20261020, "Member
export format", status accepted, decided by the maintainer on 2026-10-20) states that the
member export writes CSV only and that no second export format is added; it lists "CSV and
JSON side by side" as a rejected alternative because one consumer existed. It supersedes the
legacy `docs/lusona/adr/0003-json-member-export.md` (ADR 0003: replace CSV with JSON only;
status superseded). An Icebox row in `docs/lusona/work.md` still proposes switching the export
to JSON per ADR 0003. `docs/lusona/README.md` sets strict TDD as a standing preference. The
user's request (a `--format json` option, CSV stays the default) contradicts ADR 20261020 in
part.

Required, in the reply, all of:

1. the decision and its source: ADR 20261020 by ID, path, or title;
2. the conflict: the request adds a second export format, which the ADR excludes or lists as
   a rejected alternative;
3. a question that asks the user to decide on the decision (for example keep it, revise it
   in part, or supersede it). The actor has no question tool, so a question in the reply text
   counts;
4. a recommended answer;
5. no report that the decision is already revised or superseded, and no report that the JSON
   option is implemented or started. Recording the conflict in a record is allowed.

Counterexamples: only "shall I proceed?" without naming ADR 20261020; ADR 0003 or the Icebox
row presented as the decision that allows JSON (ADR 0003 is superseded); options without a
recommendation; only a question about the TDD level (the project README sets strict); a reply
that says the ADR was updated to allow JSON before the user answered; a reply that says the
JSON option or its tests were added.

## decision-revised

Two turns: turn 1 is the request from `decision-conflict`; turn 2 is the user's decision.
Whether a decision record under `docs/lusona/adr/` changed, and whether ADR 0003 keeps its
superseded status line, is graded by code.

### C14.recorded

Fixture facts: before the trial, `docs/lusona/adr/20261020-member-export-format.md` (ADR
20261020, status accepted, decided by the maintainer on 2026-10-20) said the member export
writes CSV only because the treasurer's monthly spreadsheet import reads CSV only, and it
rejected "CSV and JSON side by side" because one consumer existed. In turn 2 the user decides:
revise ADR 20261020 so that CSV stays the default and the treasurer's format, and JSON becomes
a second format only for the federation import; record the decision; do not implement yet.

Required: after turn 2, the changed records contain all of:

1. the outcome for ADR 20261020: revised in part, or superseded by a new dated ADR that ADR
   20261020 links to (a `Superseded by` link or a status line naming the new ADR);
2. a date for the revision and its source, attributed to the user or maintainer (for example
   "user decision in conversation");
3. the new decision: CSV stays the default and the treasurer's format; JSON is added as a
   second format for the federation import;
4. the earlier rationale is kept: the treasurer's spreadsheet import needs CSV. It may move to
   a context or history part of the record, but it is not deleted.

Counterexamples: the ADR text is replaced so that the CSV-only decision and its reason are
gone without a trace; the revision has no date or no source; a record states that the JSON
option is implemented (the user said not yet); ADR 20261020 still says CSV only with no
revision note and no link to a new decision.

### C15.not-reinstated

Fixture facts: the legacy `docs/lusona/adr/0003-json-member-export.md` (ADR 0003, status
superseded by ADR 20261020 on 2026-10-20) decided to replace the CSV export with JSON only and
remove CSV. An Icebox row in `docs/lusona/work.md`, "Switch the member export to JSON (ADR
0003)", parked until the federation opens its import, was not updated when ADR 0003 was
superseded. In turn 2 the user decides that CSV stays the default and JSON becomes a second
format for the federation import.

Required: neither reply and no changed record adopts the superseded choice of ADR 0003 (JSON
replacing CSV, with CSV removed). The new decision keeps CSV. ADR 0003 is not cited as the
authority for the revision; mentioning it as history is allowed. The Icebox row is not moved
to the Active queue as planned work. Marking that row superseded, removing it, rewording it to
the new decision, or leaving it unchanged passes this criterion.

Counterexamples: "ADR 0003 is reinstated"; a record that says the export writes JSON only or
that CSV will be removed; the Icebox row moved to the Active queue as "Switch the member export
to JSON".

## old-records

One turn. The records were created from the plugin's `34186da` templates, except the legacy
spec 0007. Whether records were deleted, renamed, copied to a new ID, or left unchanged is
graded by code.

### C17.read

Fixture facts: `docs/lusona/specs/0007-member-search.md` is a legacy `NNNN-slug` spec in an
older shape (header lines `Status: Review` and `Owner: maintainer`; sections Requirements,
Acceptance with A1-A4, Decisions, Log, Handoff); A1-A3 are checked and A4 "the product lead
accepts the search page" is open. `docs/lusona/work.md` lists Member search (spec 0007) in
Review and Search sorting (`specs/20261028-search-sorting.md`) in Doing.
`docs/lusona/notes/member-search.md` defers phone-number search and asks for an Ideas row
that links these notes after spec 0007 closes. `docs/lusona/evidence/2026-10-30-member-search-latency.md`
records a 41 ms median latency. `docs/lusona/history/2026-11-week-01.md` has one completed
item dated 2026-11-02. The user reports the product lead's acceptance by email on 2026-11-03.

Required, in the changed files, all of:

1. `docs/lusona/specs/0007-member-search.md` records the acceptance (product lead, by email,
   2026-11-03), for example A4 checked or the handoff updated, and keeps its legacy sections
   and ID; it is not rewritten into a different template;
2. a history entry for member search that links spec 0007 and states the completion (the
   acceptance); a link to the latency evidence is allowed but not required;
3. `docs/lusona/work.md` no longer lists member search in the Active queue, still lists Search
   sorting in Doing, and has a new Ideas row for phone-number search that links the notes
   (`notes/member-search.md`);
4. neither the reply nor a record proposes migrating or renaming the old records as part of
   this task.

Counterexamples: a history entry with no link to spec 0007; an Ideas row with no link to the
notes; the Search sorting row removed or its state changed; A4 left open and the handoff
unchanged while the reply says the acceptance is recorded; spec 0007 rewritten into the dated
spec template; a reply that recommends moving spec 0007 to a dated ID.
