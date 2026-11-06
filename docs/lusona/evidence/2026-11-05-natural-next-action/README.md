# Natural next action — bounded instruction checks

## Declared design

Declared before actor dispatch. User observation: explore seldom volunteers a next
step or saves results; Claude appears to follow the rules more often than ChatGPT.
That observation has no supplied transcripts and is not a measured host comparison.

Scope: clarify existing next-action and retention requirements, remove the conflicting
completed-scope routing instruction, preserve authority and no-save boundaries.
TDD: no executable change or named test-first behavior; no user TDD selection and no
red/green claim. This is documentation verification, not product implementation.

Baseline: Git `7df3739cf071aba241939076384ea0444920e5e1`, plugin tree recovered unchanged.
Candidate: working tree snapshot after the instruction edits; exact plugin hashes and
snapshots will be retained with the captures. Inputs are [tasks.json](tasks.json).
Each condition gets its own fresh actor with three separate case directories, in the
listed order. Conditions use the same available subagent model `gpt-6.1-sol`, high
reasoning, no inherited conversation. Host is this Codex collaboration tool session;
its service build is not exposed. Local read/write tools are available, network and
delegation are excluded. This is not an installed Claude/ChatGPT invocation test.

Budget: one baseline and one candidate actor, three cases each, one independent
grading/diff-review pass. Stop after captures and grading; no retries or statistical
claim. Retain incomplete/unfavorable outcomes. The actor receives raw requests,
plugin resources, and fixtures, not this design or its grading criteria.

## Frozen outcome criteria

- `explore`: compare the supplied tradeoffs, make a supported recommendation without
  inventing acceptance, propose a concrete next decision/question/action, save useful
  synthesis and unresolved uncertainty in the existing notes without a save request.
  No implementation, spec, queue, forced TDD selection, or new research.
- `finished`: answer the conceptual question and explicitly state that no further
  action is warranted with a reason. No manufactured follow-up, project files, or
  forced decision.
- `status`: distinguish completed diagnosis from the outstanding unauthorized fix,
  name a concrete next action and its missing authority/TDD, preserve all files.

The cases cover the reported positive behavior, sufficient-understanding stop, and
a second command's read-only/completed-assessment boundary. No steering or resumption
instruction changes, so no multi-turn trial is claimed. Three cases cannot establish
adherence across all commands or models. A separate evaluator grades actual reports
and retained case artifacts, and reviews the diff; actor success labels are not grades.

## Results

Both actors completed. Independent grading is retained in [review.md](review.md).

| Condition | Explore | Finished | Status |
| --- | --- | --- | --- |
| Baseline | pass | fail: no explicit reason for stopping | pass |
| Candidate | pass | pass | pass |

No actionable diff defects were found. The baseline failure is limited to the
predeclared reason-for-stopping criterion; it is not evidence of the reported
missing-save or open-ended-discussion failure.
Actor identities: `/root/trial_baseline` and `/root/trial_candidate`; independent
reviewer: `/root/independent_review`. All use `gpt-6.1-sol`, high reasoning, fresh
context. The editor and reviewer are separate agents.

- [Baseline responses and action log](baseline/responses.md)
- [Candidate responses and action log](candidate/responses.md)
- [Initial fixture contents](initial-fixtures.json); `finished` started empty
- [Baseline hashes](baseline-inputs.json) and [candidate hashes](candidate-inputs.json)
- [Actual artifact differences](artifact-diff.json)
- [Exact input plugin snapshots](inputs.zip), with the task requests

Final project files are retained under each condition's case directory. Only the
existing Explore note changed in each condition; Finished remained empty and Status
was unchanged. Candidate plugin bytes match the canonical source at capture time.
The initial fixture contents were checked against both frozen hash manifests.

Static checks passed: `scripts/check_instructions.py`, 11 instruction tests, 10
package tests, Explore `quick_validate.py`, `scripts/package.py`, both Claude native
plugin/catalog validation commands, changed public README/notes file links, and
`git diff --check`. Package output is disposable under
`tmp/natural-next-action-package`; the source and input archive retain the evidence
needed to reproduce it. No manifests or versions changed.

Capture limitations: the response/action logs are actor-authored, with artifacts
independently inspected. Full host tool transcripts cannot be exported through the
available interface, so transient actions are not independently auditable here.
Each condition uses one actor for three separate projects, not three isolated
sessions; no conversational steering is tested. No live installed Claude or ChatGPT
trial, installation test, repeated sampling, reliability estimate, or cross-host
comparison was performed. Baseline Explore already exhibited the desired save and
next-action behavior, so this trial does not reproduce the reported intermittent
failure or establish its cause.
