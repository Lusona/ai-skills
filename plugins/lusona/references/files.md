# Project records and compatibility

Read before locating, creating or maintaining a project record under `docs/lusona/`, including a record from an earlier plugin version.

## Ownership

- The consuming project owns its data. Every `docs/lusona/` path is relative to that project.
- Links in bundled plugin files resolve relative to the file that contains them.
- Never write consuming-project data into installed plugin resources.
- Installing the plugin does not create project data. Create a record only when authorized work needs it. The one exception is the queue: [setup](../skills/setup/SKILL.md) creates it when the user asks for setup.

## Paths

| Path | Purpose |
| --- | --- |
| `docs/lusona/README.md` | Optional project-local contract, including a standing TDD preference |
| `docs/lusona/product.md` | Product brief, capability map, shared architecture context and ADR links |
| `docs/lusona/work.md` | Current queue; owns active state, priority and one-sentence completion conditions |
| `docs/lusona/specs/<change-id>.md` | Change agreement, optional execution steps, evidence and one current handoff |
| `docs/lusona/adr/<YYYYMMDD>-<decision-slug>.md` | Consequential architecture decision, shared or change-specific |
| `docs/lusona/notes/<change-slug>.md` | Findings, synthesis, or a spec-free execution agreement and evidence without another owner |
| `docs/lusona/evidence/` | Material measurement and experiment records with exact-run references |
| `docs/lusona/history/YYYY-MM-week-NN.md` | Completed-item index; owns archived state and completion references |
| `docs/lusona/plans/<change-id>.md` | Existing execution records; still valid; do not create one for a new change |
| `docs/lusona/batches/<batch-slug>.md` | Coordinator-owned batch selection, authority, assignments, recovery pointers and current batch handoff |
| `docs/lusona/visuals/<record-id>/` | Chosen UI option's HTML and PNGs per state, or a diagram's Mermaid Markdown, with its `reference.md` binding list; `<record-id>` is the owning spec or ADR basename or the notes slug |

## Templates

| Template | Use |
| --- | --- |
| [Product](../templates/product.md.template) | Product context |
| [Change](../templates/spec.md.template) | Agreement, optional execution, evidence and current handoff |
| [ADR](../templates/adr.md.template) | Architecture decision |
| [Queue](../templates/work.md.template) | Work queue structure |
| [Lusona section](../templates/agents-section.md.template) | Lusona section for a project's `AGENTS.md`, with the standing TDD preference and model tier mapping |
| [Batch](../templates/batch.md.template) | Batch coordination record; links owning requirements and evidence |
| [History](../templates/history.md.template) | Weekly sections and completed-item structure |
| [Evidence](../templates/evidence.md.template) | Measurement or experiment design, run results, limitations and interpretation |
| [Notes](../templates/notes.md.template) | Durable questions, evidence, conclusions and current handoff |
| [Visual reference](../templates/visual-reference.md.template) | Chosen option, source, UI images, binding and illustrative items, fidelity, rejected options |
| [Visual page](../templates/visual-page.html.template) | Page shell with notes and theme; UI mockup and index variants; device frames, flows, state and option switches; wireframe kit fallback |

Records created from earlier templates stay valid. New records may use the current templates.

## Existing records

- Read and update existing records in place, without migration. This includes combined specs, specs with execution records, feature documents, `docs/agent/` records and legacy `NNNN-slug` records.
- Use an existing Feature map as the capability map. Do not create a duplicate. Do not rename consuming-project sections only to adopt the plugin's terms.
- Use an existing record's execution section, linked execution record and handoff in place. Do not migrate them or create another maintained copy.
- Split or move existing records only when the user requests it. Preserve criterion and task IDs, decisions, the TDD level, evidence, authorization and references.
