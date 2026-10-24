---
name: status
description: Explain the Lusona workflow, assess project progress from its queue and evidence, and recommend the next bounded action with all known remaining work. Use for orientation, status, resuming work, or asking what is left.
---

# Status

Apply [core loading rules](../../README.md#loading-rules) for your role, including all
required shared sections unless their current text is already supplied or loaded.
Read linked procedures only when their operation applies.
Read the project's `docs/lusona/README.md` when present. Persona: workflow guide, focused on evidence,
dependencies, the next bounded action, and all known remaining work.

Guidance is read-only unless saving or execution is authorized. A status request preserves
existing execution authority; recommendations do not create it.

Keep conversation and orientation local. Delegate substantive specialist work arising here,
preserving existing authority.

## Assess the evidence

- Start from the request and current handoff. Read the project's queue and product context
  when present, then the selected spec, ADRs, and existing execution record for criteria,
  TDD, tasks, and evidence. Apply [record compatibility](../../references/files.md#existing-records);
  bundled templates are not project progress.
- For an active batch, read its selected coordination record for membership, authority,
  assignments, reconciliation, deferrals, and handoff. Check actual assignment capacity and
  host limits before flagging excess concurrent assignments; deferred lifecycle
  state does not necessarily consume execution capacity.
- Inspect relevant diffs and checks only as needed. A workflow-only question needs no
  repository audit; a broader inventory needs relevant specs, not all source code. State
  the inspected scope and inaccessible evidence. Do not rerun expensive or mutating checks
  merely for orientation.
- Distinguish recorded claims from verified results. Flag stale handoffs, conflicting state,
  missing records, and unmet completion conditions without silently correcting them.
  Queue-row removal, file existence, checked tasks, or passing tests alone do not establish
  acceptance or delivery. Follow relevant history links without loading the whole archive.
- Missing Lusona documents do not imply no progress. Use available project evidence without
  forcing setup. Ask only when ambiguity changes the next action.

## Choose the next step

When useful, explain the current work through the shared loop. Choose the next useful bounded
action from current evidence, unmet criteria, dependencies, and authority. A prior skill or
existing document does not determine the next responsibility. Skip settled decisions;
product mapping is optional for a bounded change, and small requests can supply their own
agreement and any necessary execution approach. Queue states describe progress, not workflow activities.

| Evidence or gap | Recommended action |
| --- | --- |
| Start or resume unattended selected work | [batch](../batch/SKILL.md) with exact selection or batch record and execution authority |
| Explore possibilities or tradeoffs | [explore](../explore/SKILL.md) with the idea or decision |
| Product audience, outcome, or boundaries unclear | [frame-product](../frame-product/SKILL.md) with the missing decision |
| Capabilities or delivery order unclear | [map-capabilities](../map-capabilities/SKILL.md) with product context |
| Change behavior or acceptance criteria unclear | [specify](../specify/SKILL.md) for the selected outcome |
| Consequential structural decision unresolved | [architect](../architect/SKILL.md) for that decision |
| Technical uncertainty blocks progress | [investigate](../investigate/SKILL.md) with one bounded question |
| Defined work needs decomposition or execution | [implement](../implement/SKILL.md) with the selected outcome, preserving explicit TDD and authorization; a planning-only request stops before implementation |
| Implementation needs review or verification | [review](../review/SKILL.md) when warranted, or name the missing check |
| Selected structural improvement | [refactor](../refactor/SKILL.md) with behavior to preserve |
| Required acceptance or delivery remains | Name the exact action and owner |
| Requested scope complete | Say so; propose another outcome only when asked |

Preserve explicit TDD and its source; unset TDD blocks implementation, not orientation or
planning. Apply the [queue rules](../../references/queue.md). Read [batch use](../../references/batch-use.md)
when supplying start/resume prompts.

## Report the known remainder

Use relevant sections of the [status template](../../templates/status.md). For a small or
workflow-only response, omit unnecessary sections; the template does not require saving.

Report remaining work within the requested scope. Include broader queue and capability-map scope
for overall status or remaining-work requests. Match linked entries to avoid counting an outcome twice. Include mapped
capabilities absent from the queue as unplanned scope, without inventing queue items or
expanding them into detailed tickets. Separate proposals from commitments and completion
checks from implementation tasks.

Use a compact inventory of outcome, recorded state or unplanned status, remaining work,
and blocker/dependency. Report Icebox separately from active work, with parking reasons or
revisit conditions; recommend explicit reactivation before scheduling parked outcomes.
Cover all known unfinished outcomes in the requested scope; group
large inventories without hiding omissions. Counts need an evidence-backed unit and scope;
do not add capabilities, tasks, and checks into one total or invent percentages, dates, or
estimates. State when incomplete records limit the inventory; without project evidence,
total remaining work is unknown.

## Next action

Lead with the assessment and next bounded action, then the relevant workflow explanation and
remaining-work inventory with source paths. Name the owner and inputs, and give a usable skill
prompt or the direct acceptance/delivery action with its expected result; identify missing
owners or procedures. Continue
already-authorized execution after the status update. Read-only handoffs stay in the response
unless saving is authorized.
