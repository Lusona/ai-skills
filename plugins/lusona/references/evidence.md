# Decision evidence

Read before starting a measurement or experiment, and before producing or retaining a material measurement, evaluation or experiment.

## Study entry

- A [measurement](../skills/measure/SKILL.md) or [experiment](../skills/experiment/SKILL.md) that the request does not require needs explicit or standing authority. It also needs a finite scope and resource budget.
- Uncertainty alone does not start a study (a measurement or experiment). Do not repeat an offer of one.
- An empirical check inside the current task, using available tools and inputs, needs no separate study, stage or evidence file.
- Use [investigate](../skills/investigate/SKILL.md) for a diagnostic probe.
- Keep routine evidence (test, build and verification logs) with its task. Evidence is material when a decision relies on it; retain it and its provenance under the rules below.
- Support an improvement claim with a comparable result. Report unmet requirements and unsupported claims.
- Checks, the TDD level, empirical acceptance and resource limits still apply to a study.
- Measurements and experiments inside authorized work need no new user request.

## Retain material evidence

- Save material decision evidence before handoff or completion. Do not wait for a save request.
- Work whose result no decision relies on needs no evidence record.
- Saving does not authorize new collection, implementation or external actions.
- Saving a measurement does not require a spec, queue entry, plan or new approval.

## Choose the record

Use the sections of the [evidence template](../templates/evidence.md.template) that the work has content for. Save new material decision evidence in the consuming project's `docs/lusona/evidence/`:

- One result from one run: `YYYY-MM-DD-<topic>.md`.
- More than one run, or artifacts stored as separate files: `YYYY-MM-DD-<topic>/README.md`, with one file per run (`runs/001.md`, `runs/002.md`) or one directory per run (`runs/001/README.md`).
- The topic README states the question and links the runs. It does not copy every result.
- When continuing the same question, reuse its topic record.
- Give each run an identifier that is unique within the topic.
- A dated single file is itself an exact run.
- Do not create a directory tree or migrate existing notes only to match this layout.

## Provenance and observations

Record the method and provenance that a reader needs to interpret and reproduce the result:

- question and decision;
- declared design, when one exists;
- metrics and units;
- population or workload, and sample;
- reference;
- pinned revisions or artifact identifiers, and local modifications;
- instrument and method versions;
- inputs and environment;
- procedure and observations;
- uncertainty and limitations;
- conclusion.

- When provenance is unavailable, state what is missing and its effect. Do not claim reproducibility.
- Separate observations, inference and exploratory findings.
- Preserve earlier observations and the design that preceded them.
- Add a new run for new observations. Do not overwrite an earlier result with a more favorable one.
- Correct a transcription error or a refuted interpretation visibly beside the original claim. State the correction and its reason.
- Keep a topic's current conclusion and latest comparable result distinct from its chronologically latest run.
- Link the exact supporting runs and state the limits of each comparison.

## Artifacts and scratch

- Retain the methods, provenance, results and material artifacts that support the decision. Include unfavorable results that affect it.
- Raw outputs may be stored as a durable artifact reference with identifier, location, and access or reproduction steps.
- Do not commit scratch prototypes, harnesses or transient output.
- Put scratch prototypes, harnesses and transient output under the repository's `tmp/` unless the project names another ignored directory.
- Before cleanup, preserve the material evidence or a durable reference to it.
- Never leave the only supporting evidence in scratch storage.

## Links between records

- In specs, notes, ADRs and history, link each claim to the exact evidence files or runs it relies on.
- Notes discuss implications, alternatives and open questions. The evidence record owns observations and methods.
- Do not link a claim to a changing topic summary. Link the run that supports the claim.
- Leave existing notes and other established records in place. Link them; do not migrate or copy their evidence.
- Routine test, build and verification logs stay with the task's existing evidence owner.
- `docs/lusona/evidence/` holds material decision evidence, not every command output.
- When closing or handing off work, keep the links that explain a decision or resume work.
- Do not replace the method, provenance and results that support a decision with a conclusion.
