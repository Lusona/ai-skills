# Decision evidence

Read when producing or retaining material measurements, evaluations, or experiments.
Apply [retention](retention.md) and the core's write restrictions. This procedure does not
require saving disposable work, override read-only or no-save instructions, or authorize
new collection, implementation, or external actions.

## Choose the smallest record

Use relevant sections of the [evidence template](../templates/evidence.md). New material
decision evidence lives in the consuming project's `docs/lusona/evidence/`:

- A small one-off result can use `YYYY-MM-DD-<topic>.md`.
- Repeated runs or substantial artifacts can use `YYYY-MM-DD-<topic>/README.md` with
  `runs/001.md`, `runs/002.md`, or run directories such as `runs/001/README.md` as needed.
  The topic README states the question and links the runs; it is not a copy of every result.

Reuse the topic owner when continuing the same question. Use unambiguous run identifiers
within it. A dated file is itself an exact run when no further split is useful. Do not create
a directory tree or migrate existing notes solely to satisfy the new layout.

## Preserve provenance and observations

Record enough method and provenance to interpret and reproduce the result: question and
decision; declared design where applicable; metrics and units; population/workload and sample;
reference; pinned revisions or artifact identifiers and local modifications; instrument and
method versions; relevant inputs and environment; procedure; observations; uncertainty and
limitations; conclusion. Explain unavailable provenance and its effect rather than claiming
reproducibility. Separate observations, inference, and exploratory findings.

Preserve prior observations and the design that preceded them. Add a new run for new
observations; do not overwrite an earlier result with a more favorable one. Correct transcription
errors or refuted interpretations visibly beside the original claim, identifying the correction
and reason. Keep a topic's current conclusion and latest **comparable** result distinct from its
chronologically latest run; link the exact supporting runs and explain comparison limits.

Retain methods, provenance, results, and material artifacts needed to support the decision,
including unfavorable results that affect it. Large raw outputs may use a durable artifact
reference with identifier, location, and access/reproduction information; avoid committing large
disposable outputs. Scratch prototypes, harnesses, and transient output belong under repo-local
`tmp/` where practical. Before cleanup, preserve the material evidence or a durable reference;
do not leave the only supporting evidence in disposable scratch storage.

## Link ownership without duplication

Specs, notes, ADRs, and history link exact evidence files or runs for claims they rely on.
Notes discuss implications, alternatives, and open questions; the evidence record owns the
observations and methods. A link to a changing topic summary alone does not identify the run
supporting a claim. Existing notes and other established records stay in place; link them
instead of migrating or duplicating their evidence.

Routine test, build, and task verification logs stay with the task's existing evidence owner.
The dedicated home is for material decision evidence, not every command output. Saving a
measurement does not require a spec, queue entry, plan, or a new approval. Retention and
closeout preserve links needed to explain a decision or resume work; a concise conclusion
must not replace its material method, provenance, and results.
