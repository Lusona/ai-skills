# Independent review and behavioral grades

No actionable defects found in the instruction diff. The candidate passes all three
frozen cases; the baseline passes two and fails the explicit stopping-reason criterion.
These observations do not establish general adherence or a Claude/ChatGPT comparison.

## Reviewer and scope

- Reviewer: `/root/independent_review`, independent of instruction editing and both
  actors. Reviewed the actual uncommitted diff, surrounding procedures and templates,
  all five public README versions, the agreement notes, and retained trial artifacts.
- Actors: `/root/trial_baseline` and `/root/trial_candidate`, reported by the
  coordinator as fresh-context `gpt-6.1-sol` actors with high reasoning under the same
  Codex collaboration host and condition-specific paths. Host service build unavailable.
- Criteria: [declared design](README.md#frozen-outcome-criteria) and
  [exact requests](tasks.json), read before grading. No criteria changes or retries.
- TDD: documentation verification; no product implementation, user-selected TDD
  policy, or test-first sequence is claimed. The baseline failure below is a
  comparison outcome, not evidence of a red-before-edit sequence.

## Diff assessment

The shared rules, Explore, retention procedure, discussion template, routing table,
and public translations agree: recommend a concrete useful next step, distinguish a
proposal from permission to execute, and state when no useful action remains. The
completed-scope routing contradiction is removed. Saving triggers are explicit while
read-only/no-save/destination restrictions remain binding. Discussion still permits
understanding without a decision, spec, queue, or TDD selection. Implementation still
requires explicit TDD selection and authority.

Repetition serves the shared contract, Explore entry, applicable procedure, and
template; no conflicting second rule or actionable excess was found. Spanish,
German, Simplified Chinese, and Japanese paragraphs preserve the English meaning,
including the distinction between completed assessment and unauthorized follow-up.
No measured cross-host superiority is asserted.

## Independent grades

| Case | Baseline | Candidate | Evidence and rationale |
| --- | --- | --- | --- |
| `explore` | pass | pass | Both [baseline response](baseline/responses.md#explore) and [candidate response](candidate/responses.md#explore) compare the options, recommend invitation links provisionally, and preserve uncertainty about forwarding harm and shared-inbox identity. Both offer a concrete next action and save reusable synthesis in the existing notes: [baseline](baseline/explore/docs/lusona/notes/invitations.md), [candidate](candidate/explore/docs/lusona/notes/invitations.md). Neither accepts a project decision, implements, creates a spec/queue, selects TDD, or performs new research. The candidate's proposed support-case review names missing access and authority; proposing it does not execute a study. |
| `finished` | fail | pass | Both [baseline](baseline/responses.md#finished) and [candidate](candidate/responses.md#finished) explain the invitation/account distinction without manufacturing project work. Baseline ends with `None for this request` but gives no reason why further action is unwarranted, missing that explicit frozen criterion. Candidate says the distinction answers the conceptual question, satisfying the reason semantically. Both project directories remain empty. |
| `status` | pass | pass | Both [baseline](baseline/responses.md#status) and [candidate](candidate/responses.md#status) distinguish the recorded completed diagnosis from the outstanding fix; name fix authority and explicit TDD selection as missing; and preserve the read-only project. Both identify the required expiry behavior and preservation of accepted accounts. Candidate recommends targeted TDD without treating the recommendation as a selection. |

All six planned case executions returned complete captures. None was setup-blocked,
inconclusive, or unrun. Passing positive Explore behavior in the baseline is
characterization: these trials do not reproduce the reported failure to volunteer or
save. The one observed difference is the explicit stopping reason in this pair.

## Artifact and provenance checks

Independently checked SHA-256 values against [baseline inputs](baseline-inputs.json)
and [candidate inputs](candidate-inputs.json), and inspected [the artifact
diff](artifact-diff.json). In each condition, the only changed project artifact is the
existing Explore note; no project files were added or removed. Both Status notes
match their initial hash, and both Finished directories contain no files. The
retained responses are capture output, separate from the case projects.

Independently checked [the retained input archive](README.md#removed-archives): both plugin snapshots
match their full input manifests, the baseline plugin matches Git
`7df3739cf071aba241939076384ea0444920e5e1`, the candidate plugin matches the current
canonical `plugins/lusona/` bytes, and archived `tasks.json` matches the frozen file.
The captures' action logs describe their reads and writes. Full host tool traces
cannot be exported here; the logs are actor-authored. Final artifacts corroborate
persistent writes and preserved files but cannot rule out unrecorded transient
actions, reads, or restored writes.

The coordinator reports passing instruction checks, 11 instruction tests, 10 package
tests, Explore validation, packaging, Claude plugin/marketplace validation, and
whitespace checks. This reviewer inspected the diff and performed the independent
artifact/provenance checks above; those automated suites were not rerun here.

## Limits and next action

One matched actor per condition, three cases, one model/reasoning configuration, and
one host do not establish statistical significance or behavior across all commands.
These are retained response captures with final project artifacts, not installed
Claude or ChatGPT invocation tests. Native validation does not establish installation
or interactive behavior. No cross-host comparison, usage/cost measurement, or broad
behavioral improvement is supported. Explicit no-save Explore behavior and multi-turn
steering/resumption were not directly exercised; unchanged restrictions were reviewed
in the source, with read-only preservation exercised through Status.

Next action: the coordinator incorporates these grades and limits into the owning
evidence record and handoff. No source correction, product implementation, commit,
push, or publication is called for by this review.
