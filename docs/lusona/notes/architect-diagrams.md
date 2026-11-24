# Diagrams in Architect discussions

## 2026-11-24 — When should Architect draw the first diagram?

The user wants Architect to try to diagram the work whenever possible. The [current skill](../../../plugins/lusona/skills/architect/SKILL.md) directs Architect to visual guidance when a description cannot show what the decision depends on. The [visual guidance](../../../plugins/lusona/references/visuals.md) already supports Mermaid in a reply.

Accepted direction: Proactively diagram the architecture whenever a visual helps someone understand, compare or verify a decision. Choose the diagram type, scope and level of detail to fit the question. Use multiple views when the decision spans distinct concerns. For a distributed job system, a component diagram can show ownership, a sequence diagram can trace retries, and a state diagram can show when a job reaches a terminal state.

On 2026-11-24 the user accepted the revised direction and authorized implementation and a version bump. Planned release: 3.1.2, a patch to the existing Architect workflow. The user selected TDD level `none` on 2026-11-24. Verification will cover the skill audit, a complex architectural decision, manifest alignment and packaging.

Behavior trial planned before execution: one candidate run with a Codex leaf acting as Architect. Ask about retry ownership across a queue, worker and external service, without requesting diagrams. Pass if the response proactively draws decision-relevant views covering ownership and failure sequence. The coordinator grades the output. Stop after one run.

Initial trial failed: two tables, no diagram. Correction round 1 ties diagram selection to presenting the proposal and names ownership and recovery as distinct concerns. Repeat the same scenario once with the corrected instruction supplied directly. Same grading criteria.

The correction trial passed. The actor drew an ownership flowchart and a sequence diagram tracing a crash after billing and before acknowledgment. The corrected instruction was supplied directly, so this checks its application. There was no installed-plugin discovery or interactive installation test. The voice checker subsequently rejected “consider”. Replacing it with “identify” passed the checker. Behavioral correction rounds: one total, zero consecutive without progress.

Verification against base 7a9a79a: 231 repository tests, 163 loop-conformance tests, Bash helper tests and 203 PowerShell assertions passed. Shared-region, skill-template, voice, instruction, contract, inventory, package and whitespace checks passed. Claude validated both the marketplace and plugin. Five native manifest copies and the five README source-version notices now report 3.1.2. The archive is in repo-local tmp/lusona-3.1.2-architect/. The user accepted the result and authorized local commits.

Both trials used read-only Codex leaves (gpt-6.2-sol, low reasoning) with no delegation or saving. The raw scenario was “Our queue delivers jobs at least once. A worker calls an external billing service which supports idempotency keys, and can crash before acknowledging the queue. Where should retry ownership sit and how should we reason about recovery?” It covers structural ownership and temporal recovery in one decision. Trial one loaded the working-tree candidate by path. Trial two received the revised trigger in its assignment. The coordinator graded both returned proposals. The scenario and grading conditions were chosen before execution. Exact dispatch metadata was documented afterward. These candidate-only trials establish neither an improvement rate nor installed discovery.

Independent audit by the Codex trial leaf (gpt-6.2-sol, low reasoning), which authored none of the diff. The reviewer checked the final skill instruction against docs/skill-audit.md and found no substantive wording defect. Its changelog fidelity observation was corrected and its requests for evidence are recorded above.
