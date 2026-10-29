# Visual options and retained references — behavioral trials

Owner: [spec 20261028-visual-options-and-references](../../specs/20261028-visual-options-and-references.md).

## Declared design

Frozen on 2026-10-28 before canonical edits (`design.md`, `tasks/`, `fixture/`,
`evaluator/criteria.md` in [evidence.zip](evidence.zip); hashes in `frozen.sha256`).

- TDD: targeted (user, 2026-10-28). Test-first: TF-a = AC2 retention (C1); TF-b = AC6 binding
  acceptance in implement (C2). Regression, candidate-only: C3 explore diagrams (AC4, AC5),
  C4 review without screenshots (AC7), C5 rejection (AC3, AC1), C6 implement without reference (AC8).
- Baseline: canonical plugin at commit `6bcd4b0`, unchanged (`snapshots/baseline.sha256`).
  Candidate: canonical plugin after the first implementation pass (`snapshots/candidate.sha256`).
- Conditions: Claude Code subagents as actors, model Sonnet in both arms, host default reasoning;
  fresh fixture copy per trial; no delegation, no browser opening, no screenshot tool, no user
  mid-turn. C3 is two turns in one actor session.
- Budget: 8 trials, 9 turns, one attempt each, no retries. Grader: an independent Opus agent that
  did not write the changes or run the trials.

## Results

| Trial | Grade | Observation |
| --- | --- | --- |
| baseline-c1 | fail (expected red) | Layout B recorded in the spec as a link to the throwaway `tmp/options/b.html`; nothing retained under `docs/lusona`. |
| candidate-c1 | pass | `docs/lusona/visuals/20261028-account-settings/option-b.html` + `reference.md` with V1–V3 binding, colors illustrative, A/C rejection reasons; spec links it. |
| baseline-c2 | pass (red not observed) | Implemented B1–B4 and reported each; B1 and B2 share one bullet. |
| candidate-c2 | pass | B1–B4 reported individually; illustrative items stated as not acceptance. |
| candidate-c3 | pass | Turn 1 (TOML vs YAML): no diagram. Turn 2 (password reset): inline ASCII sequence diagram showing where the token is checked. No files written. |
| candidate-c4 | pass | B2 and B4 unmet with line references; B1, B3 met; visual comparison reported unrun; human visual acceptance required; no edits. |
| candidate-c5 | pass | Revised wizard options A–C written to `tmp/options/`; nothing saved under `docs/lusona`; asks for a letter. |
| candidate-c6 | pass | Implemented AC1–AC2; no visual files and no invented binding checklist. |

Full per-criterion grades and evidence: `evaluator/grades.md` in [evidence.zip](evidence.zip).

## Interpretation and limits

- TF-a has red/green evidence: baseline fail, candidate pass.
- TF-b has no red. The C2 fixture gives a labeled B1–B4 list, so the unchanged baseline already
  reported each item. That pass is characterization; no failure was manufactured. AC6 is supported
  only by candidate behavior, not by a demonstrated change.
- After grading, review findings R1–R4 were fixed: specify gained a separate diagram trigger (R1),
  `visuals.md` read trigger and draft location wording were widened or clarified (R1, R4), and the
  README paragraph was moved and reworded in five languages (R2, R3). These post-trial edits were
  not re-run in trials; AC4 in specify and architect has no trial coverage.
- One observation per case, one host and model. Replies for C4 and part of C3 turn 2 were
  condensed by the coordinator (`trials/REPLY-NOTES.txt`); trial files are unaltered. Actor
  isolation from evaluator files was by instruction only. Browser rendering, offline Mermaid
  behavior, native installation, and Codex, Cursor, and Xcode hosts are untested.

[implementation.patch](implementation.patch) is the source diff after R1–R4, before the template (see run 002).

## Run 002: standard HTML template

After the user withdrew acceptance for lack of a standard page template, AC9-AC12 were added and
tested in [run 002](runs/002/README.md): TF-c baseline fail, candidate pass; AC10 and AC11 pass in
run 2 after one source correction; AC12 pass. `implementation.patch` above predates the template.

## Run 003: platform-styled options and PNG retention

After the user reviewed an example iOS mockup, AC9 and AC11 were revised and AC13-AC19 added.
[Run 003](runs/003/README.md): TF-d and TF-e baseline fail, candidate pass; AC9, AC14-AC19 pass;
F1-F8 fixed after grading.
