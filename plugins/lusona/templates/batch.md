# Batch: <short title>

Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>

Coordinator: <sole writer of this record, queue, and shared handoffs>
Authorization: <user instruction/source, selected outcome scope, routine decision delegation, limits>
Repository restrictions: <references; commit/delivery/host permission limits>
Selection captured: <time/source of fixed active queue selection; Icebox excluded unless explicitly reactivated; new discoveries excluded>
Requested assignment cap: <4 by default; 5 if selected>
Host capacity and parent occupancy: <observed controls, parent reservation, surviving agents>
Effective capacity: <assignment ceiling and available delegate slots; sequential/model-control limitations>
Repair allowance: <2 corrective rounds per item unless explicitly authorized otherwise>

Only the parent edits this record. Membership, grants, deferral, and integration phases are
coordination facts, not queue states. Link requirements and evidence in their owning records.
Replace obsolete transient entries while retaining recovery identities and durable round charges.

## Fixed membership

| Local ID | Selected outcome and queue/history link | Authority limits/source | Change record and ADR owners (existing split records accepted) | TDD and completion-condition references |
| --- | --- | --- | --- | --- |
| B1 | <stable identity even before a spec exists> | <reference> | <links as created> | <explicit source or unset; conditions> |

## Dependencies and reconciliation

| Relevant items | Definition inputs and reconciliation | Architecture inputs and reconciliation | Dependencies/shared decision owner | Eligibility constraints |
| --- | --- | --- | --- | --- |
| <IDs> | <content/version references; compatible, unsettled, or question link> | <references or settled existing decision> | <required results, ownership, interfaces> | <write/check conflicts; reevaluate on changed inputs> |

## Workspaces and ownership

| Item | Workspace and owner | Required baseline identity and retained location | User-owned inputs versus item delta | Dependencies and transfer/recovery method |
| --- | --- | --- | --- | --- |
| <ID> | <path, active writer or stopped evidence> | <revision plus dirty/untracked/binary/deleted content identity> | <attribution manifest/snapshot pointers> | <inputs, accepted destination, no-commit method if applicable> |

## Assignment grants

Persist intent before dispatch and evidence pointers before releasing ownership. Include nested
and parent-executed assignments in the same pool; waiting agents still consume host capacity.
In the dispatch/result field, distinguish assignment status and coordinator acceptance from
observed worker lifecycle. Include concrete follow-up assignment or shutdown confirmation,
pending shutdown, or unavailable-control evidence. Ownership release alone does not prove
host capacity was released; identify surviving workers and granted children in the handoff.

| Assignment | Item/responsibility and bounded scope | Owner/agent, persona and model tier | Inputs, workspace/baseline, write/check ownership | Pool grant and parent grant for nested work | Dispatch/result and evidence | Ownership release |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | <ID, skill, outcome> | <identity; model override when relevant> | <references and exclusions> | <slot, grant source> | <intent/time; actual dispatch; status and owning evidence link> | <stopped/completed evidence or still owned> |

## Repair accounting

| Item | Allowance and source | Charged rounds | Open round | Remaining allowance |
| --- | --- | --- | --- | --- |
| <ID> | <number, authority> | <durable count> | <round ID or none> | <allowance minus charged rounds> |

| Item/round | Charge recorded before dispatch | Trigger evidence | Declared correction/experiment and check references | Assignments/owners | Outcome or interruption | Cancellation evidence, only if never dispatched |
| --- | --- | --- | --- | --- | --- | --- |
| <ID/R1> | <time and charge> | <owning record link> | <bounded set; associated review> | <grants> | <owning evidence; remains charged on uncertainty> | <none or proof> |

## Integration recovery

| Integration/item | Source baseline and attributable delta | Destination before transfer and required dependencies | Candidate intent/location/identity and separate promotion intent/recovery | Phase and actual resulting identity | Checks/review and affected prior evidence | Accepted/deferred result |
| --- | --- | --- | --- | --- | --- | --- |
| I1/<ID> | <retained source and identities including uncommitted content> | <content identity and inputs> | <record before each mutation; candidate recovery; promotion pre-destination and expected post identity, delta, recovery inputs, immediate drift check or direct-destination candidate> | <intent recorded / candidate materialized / evidence collected / promotion intent / promotion materialized / accepted / deferred; actual candidate and destination identities separately> | <owning links tied to candidate; impact assessment> | <destination identity matched to reviewed candidate, preserved candidate, remaining requirement> |

## Deferrals

| Item and unfinished dependents excluded | Reason/question and owning evidence | Writer cessation and isolated changes | Next action, owner, and required input |
| --- | --- | --- | --- |
| <IDs> | <decision, missing TDD/review/acceptance/delivery, exhaustion, or blocker> | <assignment/workspace/integration references proving safe separation> | <concrete action needed to resume> |

## Current handoff

Replace this section at bounded task boundaries; do not copy the queue or task evidence.

- Batch outcome: <running; all selected complete; selection exhausted with deferrals; interrupted; unsafe to continue>
- Remaining authorization: <source/limits; no silent selection or budget expansion>
- Completed outcomes: <history/evidence links; reusable candidate/input identities>
- Active ownership and recovery: <assignment, workspace, integration, and surviving writer references>
- Remaining work and blockers: <owning references; deferred dependencies and unmet completion conditions>
- Actual execution and limitations: <observed concurrency, independent review, unavailable capabilities>
- Next action: <owner, bounded assignment or exact blocker resolution, inputs, resume this record>
