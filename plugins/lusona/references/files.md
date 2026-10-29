# Record files and compatibility

Read when locating project records or maintaining legacy ones. The consuming project owns
its data; paths are relative to that project. Bundled links are relative to the loaded resource.

## Files

| Path | Purpose |
| --- | --- |
| `docs/lusona/README.md` | Optional project-local contract, including a standing TDD preference |
| `docs/lusona/product.md` | Product brief, capability map, shared architecture context and ADR links |
| `docs/lusona/work.md` | Current queue; owns active state, priority, and concise completion conditions |
| `docs/lusona/specs/<change-id>.md` | Change agreement, optional execution steps, evidence, and one current handoff |
| `docs/lusona/plans/<change-id>.md` | Existing separate execution records remain valid; no new companion file by default |
| `docs/lusona/batches/<batch-slug>.md` | Parent-owned fixed selection, authority, assignments, recovery pointers, and current batch handoff |
| `docs/lusona/notes/<change-slug>.md` | Optional durable findings without a change record or ADR owner |
| `docs/lusona/visuals/<record-id>/` | Chosen option's HTML source and PNGs per state, or diagram Markdown, with its `reference.md` binding list under [visuals](visuals.md); `<record-id>` is the owning spec or ADR basename or notes slug |
| `docs/lusona/evidence/` | Material measurement and experiment records, with exact-run references under [evidence](evidence.md) |
| `docs/lusona/history/YYYY-MM-week-NN.md` | Compact completed-item index; owns archived state and completion references under [closeout](closeout.md) |
| `docs/lusona/adr/<YYYYMMDD>-<decision-slug>.md` | Consequential architecture decision, shared or change-specific |
| [Product template](../templates/product.md) | Product context |
| [Change template](../templates/spec.md) | Agreement, optional execution, evidence, and current handoff |
| [ADR template](../templates/adr.md) | Architecture decision |
| [Queue template](../templates/work.md) | Work queue structure |
| [Batch template](../templates/batch.md) | Batch coordination record; links owning requirements and evidence |
| [History template](../templates/history.md) | Weekly sections and completed-item structure |
| [Evidence template](../templates/evidence.md) | Measurement or experiment design, run results, limitations, and interpretation |
| [Notes template](../templates/notes.md) | Durable questions, evidence, conclusions, and current handoff |
| [Visual reference template](../templates/visual-reference.md) | Chosen option, images, binding and illustrative items, fidelity, rejected options |
| [Visual page template](../templates/visual-page.html) | Page shell with notes and theme; mockup, diagram, and index variants; device frames, flows, state and option switches; wireframe kit fallback |

## Existing records

Existing combined specs, separate specs and plans, feature documents, and `docs/agent/` records remain valid inputs.
Use an existing Feature map as the capability map; do not create a duplicate or rename
consuming-project sections solely to adopt terminology.
Use their execution sections or linked plans and handoff in place; do not automatically
migrate them or create another maintained copy. Split or move existing records only when
requested, preserving criterion and task IDs, decisions, TDD, evidence, authorization, and
references. See [compatibility](https://github.com/lusona/ai-skills/blob/main/INSTALL.md#document-compatibility).

Create documents only as the authorized work needs them. Installing the plugin does not
initialize project data. Never write consuming-project data into installed plugin resources.
