# README opening draft

Status: README revisions and translations accepted for commit on 2026-11-03. The user
reverted the marketplace metadata changes in favor of the previous wording. The commit
includes documentation and these notes only. Original drafts and validation history are
retained below; the current decision supersedes earlier pending-review and authorization notes.

## Draft text

Lusona is a set of coding-agent skills organized around a shared work loop. Skills provide guidance for different kinds of work; they do not define a sequence of stages.

- **Choose the next action from the current state.** Assess the requested outcome, available evidence, and remaining work. Take a bounded action, check its result, and reassess. Repeat while useful authorized work remains.
- **There is no fixed skill sequence.** Exploration, investigation, design, implementation, and review can recur whenever needed. An implementation may require further investigation; an experiment may reopen a design question. Moving between these activities does not require a new command.
- **Decisions are revisable.** Recorded specs and plans represent the current agreement. When evidence challenges an accepted decision, identify the conflict and revisit it with the user. After agreeing on a revision, update affected records and work from the revised decision. Superseded instructions must not restore an earlier choice.
- **Plan execution as needed.** Use explicit plans when dependencies, coordination, or recovery require them. A separate planning document is not mandatory for every change. Adjust execution as evidence develops, preserving the agreed outcome and constraints.
- **Continue within the existing authorization.** Routine execution choices belong to the agent. Changes to agreed scope, consequential decisions, and additional authority require user input. Continue independent authorized work while a decision is pending.
- **Complete against the agreed criteria.** Completion requires the requested scope and required verification. Report failed or unrun checks, unresolved decisions, and remaining work explicitly.

## Validation against canonical instructions

Checked 2026-11-02 against the repository sources below. This validates what the instructions
require, not whether agents consistently follow them at runtime. Original draft preserved above.

| Claim | Assessment | Source and qualification |
| --- | --- | --- |
| Shared loop, with no mandatory stages | Supported | [Core: Work loop](../../../plugins/lusona/README.md#work-loop) explicitly says skills supply expertise, not mandatory phases. |
| Choose bounded action, check, reassess, continue | Supported with stopping conditions | Core Work loop requires this behavior, but also pauses for user requests, missing prerequisites, authority, and correction limits. “While useful authorized work remains” should not imply unlimited retries. |
| No fixed skill sequence; revisit activities without a command | Supported with ordering constraints | [Implement: Assess](../../../plugins/lusona/skills/implement/SKILL.md#assess-the-agreement-and-current-evidence) treats specialist responsibilities as nonmandatory stages; its increments section explicitly revisits design and investigation. [Core: Contract](../../../plugins/lusona/README.md#contract) still permits required sequencing for correctness, dependencies, explicit choices, and shared state. Selected TDD sequencing also remains binding. |
| Decisions are revisable; stale records cannot reinstate them | Supported | Core Work loop explicitly requires identifying conflicts, authorized revision, reconciliation, and resumption from the revision. [Architect: Decide and record](../../../plugins/lusona/skills/architect/SKILL.md#decide-and-record) requires linked superseding ADRs while retaining prior rationale. |
| Recorded specs and plans represent the current agreement | Too broad as written | Records can contain proposals and superseded history. Architect distinguishes proposed from accepted decisions; Core Contract says specs and plans do not grant implementation authority. Say “Accepted decisions remain in force until revised within authority.” |
| Every challenged decision is revisited with the user | Overstates required user involvement | Core Work loop says reopen within authority. Architect permits technical decisions within existing authority and asks when a consequential choice exceeds it. User involvement is necessary when existing authority does not cover the revision, not for every routine adjustment. |
| Plans are conditional; separate document not mandatory | Supported | Implement explicitly prohibits creating a companion plan by default and varies planning depth with dependencies, uncertainty, coordination, and recovery. An explicit planning request also requires a plan. |
| Routine choices belong to agent; scope and consequential choices need input | Supported with authority qualification | Core Contract and Implement preserve delegated authority. Replace blanket “consequential decisions ... require user input” with “Ask when a decision or change exceeds existing authority.” Independent authorized work continues while waiting. |
| Completion requires scope and verification | Supported but incomplete | [Core: Review and communication](../../../plugins/lusona/README.md#review-and-communication) additionally requires applicable independent review and required human acceptance/delivery. Failed or unrun required checks prevent completion; merely reporting them does not permit a completion claim. |

### Recommended wording adjustments

Keep the loop and revisable decisions as the main rules. Before applying the draft:

- Add to the sequence bullet: “Respect dependencies, required verification order, and the selected TDD policy.”
- Replace the decisions bullet with: “**Decisions are revisable.** Accepted decisions remain in force until revised within authority. When evidence challenges one, identify the conflict and affected assumptions. Ask the user when the revision exceeds existing authority. Reconcile affected records and assignments, preserve useful prior rationale, and continue from the revised decision. Stale records must not reinstate superseded choices.”
- Add uncertainty and explicit planning requests to the reasons for a plan.
- Replace the authorization bullet with: “**Continue within the existing authorization.** Resolve routine execution choices without repeated approval. Ask when a decision or change exceeds existing authority. Continue independent authorized work while input is pending; pause affected work when prerequisites are missing, correction limits are reached, or the user requests it.”
- Replace the completion bullet with: “**Complete against the agreed criteria.** Completion requires the whole authorized scope, required checks and review, and any required human acceptance or delivery. Failed or unrun required checks prevent a completion claim. Report remaining work and the prerequisites for continuing.”

### Next action

The user authorized applying this draft, then approved a shorter four-rule opening.
The English README now summarizes the loop, revisable decisions, authorization, and
completion. Detailed planning, TDD, and pause rules remain in the later README sections.
Canonical skills and translated READMEs were not changed.

Validation: inspected the README diff and ran `git diff --check`. No runtime tests apply
to this prose-only change. Next action: user reviews the English README opening.

## README consistency review and action groups

The user subsequently requested reviewing the rest of the README and replacing the
implementation-first introduction with natural starting points and groups of actions.

- Replaced “Start with an outcome” with “Where to start”: status for orientation or resumption;
  explore/frame-product for new direction; mapping, definition, and implementation as needs develop.
- Grouped all 13 skills by responsibility, replacing the flat catalog. Explicitly allows
  starting with any group, skipping settled questions, and returning as evidence changes.
- Retained invocation, request examples, explicit TDD, and authorization requirements.
- Clarified mandatory ordering where dependencies or TDD require it, and carried the
  revisable-decision rule into the detailed work-loop explanation.
- Reviewed the remaining sections for consistency. Moved misplaced Antigravity setup
  guidance from the Xcode subsection and linked correction rules directly to their source.
- Compared grouping and starting guidance with canonical status, frame-product,
  map-capabilities, and workflow-guide instructions, alongside the earlier core validation.
- Validation: all 58 local README links and anchors resolve; `git diff --check` passes.
  No installation or agent runtime behavior was tested. Translations remain unchanged.

### Later-section simplification

On the user's follow-up, reviewed the remaining README sections against the shared core,
interview, visual-reference, and retention rules. Simplified the four sections from
“How the work continues” through “Results and handoffs” from 1,209 to 817 whitespace-separated
words, excluding the unchanged Mermaid diagram.

- Connected every action group to the same loop and retained necessary dependency/TDD ordering.
- Restored a concise explanation of adaptive planning and planning-only authorization.
- Condensed continuation, pause, recovery, and reporting details while preserving their
  requirements and links to canonical procedures.
- Explained that evidence can inform any action group and queue states do not determine
  which skill runs next. Retained revisable decisions and authorization across resumption.
- Kept diagnosis completion distinct from completion of a production fix.
- Preserved concurrent user edits to the action-group table.
- Validation: all 59 local README links and anchors resolve; `git diff --check` passes.
  This was a source/document consistency check, not runtime or installation testing.

Next action: user reviews the English README changes. No commit or publication authorized.

### Mermaid graph validation

Checked the diagram against the shared work loop and correction rules. Added explicit
decision reconsideration and reconciliation, correction-limit pauses, and continued independent
work when another part is waiting or paused. Reassessment includes current decisions and evidence;
completion remains conditional on all completion requirements.

Combined asking/waiting and pausing in one node to keep the graph readable. The surrounding
text distinguishes missing input, user-requested pauses, resumption conditions, and authority.
The diagram describes control flow, not a sequence of skills.

Rendered the actual README diagram with Mermaid 11.4.1 in isolated headless Chromium and
visually inspected the final screenshot at a 1,000-pixel viewport. Parsing and SVG rendering
succeeded; `git diff --check` passes. Scratch HTML, renderer, rendered DOM, and screenshot are
under `tmp/mermaid-validation/`. GitHub's renderer was not tested.

### GitHub and marketplace descriptions

The user authorized updating GitHub and plugin/marketplace descriptions to match the README.
Updated the live `Lusona/ai-skills` GitHub description and verified it by reading it back.
Applied the same description to five native manifests (including the root Antigravity
reference) and the Claude/Cursor marketplace descriptions. Updated Codex's short and long
display summaries; the Codex marketplace index has no existing description field, so its
display copy remains owned by the plugin manifest.

The descriptions now lead with the shared work loop, no fixed skill sequence, and revisable
decisions. The longer summary includes status as a starting point, action selection from
evidence, existing authority, and completion requirements.

Validation: native Claude plugin and marketplace validation passed; packaging passed at
`tmp/readme-metadata-validation/`, including manifest identity/version and bundled links.
The native validator's advisory about adding installation text to the internal plugin README
was nonblocking. Installation and marketplace UI display were not tested.

GitHub's description was updated directly during this work. The user later reverted all
local manifest/catalog description edits, preferring the previous wording. Those metadata
edits are excluded from the accepted commit; versions remain 1.4.0.

### 2026-11-03 — Translation alignment

Updated README.es.md, README.de.md, README.zh-CN.md, and README.ja.md against the current
English README, including the user's action-table edits. Used language-specific technical
editing and a parent editorial pass rather than literal sentence-by-sentence translation.
The Spanish, German, and Japanese editors owned separate files; the parent owned Chinese.
The initial Japanese worker failed at model capacity without edits; a replacement completed
the assignment. All assignments are finished with no active child operations reported.

Preserved exact commands, inline code, paths, versions, navigation targets, and Mermaid
topology. Localized prose, headings, examples, and graph labels. Editorial corrections include
natural authorization/loop terminology, Chinese findings that cover all work rather than only
investigations, and Japanese references to production code. This was model-assisted editorial
review, not human native-speaker acceptance.

Validation: `tmp/readme-localization/check.py` confirms section hierarchy, link-target multisets,
anchor resolution, command/inline-code equality, and diagram topology/classes for all four
languages. All localized graphs rendered with Mermaid 11.4.1 and were visually inspected;
Chinese labels were adjusted for readable line breaks. Packaging passed at
`tmp/readme-localization/package/`; `git diff --check` passed. Installation, host interaction,
and GitHub's renderer were not retested.

The user accepted the documentation for commit, noting that the changes were based on user
feedback. Commit rationale: new users could not identify the reason to adopt Lusona from the
previous README; explain the actual loop, revisable decisions, and useful starting points
directly, with consistent localized documentation. Include the remaining installation host-order
cleanup. Commit is authorized; push is not authorized.
