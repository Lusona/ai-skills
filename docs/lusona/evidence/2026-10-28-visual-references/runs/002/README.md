# Run 002 — standard HTML template (AC9-AC12)

Owner: [topic](../../README.md). Inputs, fixtures, trials, grades: [evidence.zip](evidence.zip)
(`design.md` with run-2 addendum, `evaluator/criteria.md`, `evaluator/grades.md`).
Source delta from the 1.3.0 working tree: [template.patch](template.patch) (includes the N1 line).

- TDD targeted (user). Test-first TF-c (AC9, AC11 option files + index). Baseline: 1.3.0 working
  tree before template edits. Actors: Claude Code subagents, Sonnet; grader: independent Opus agent.

| Trial | Grade | Observation |
| --- | --- | --- |
| baseline-d1 | fail (expected red) | One combined free-form file; no frame, no index, own classes and colors. |
| candidate-d1 (run 1) | TF-c pass; AC10 fail | Templated a/b/c + index; `b.html` used inline `style` for sidebar widths. |
| candidate-d2 (run 1) | AC11 fail | Retained file also changed the footer binding summary, which `visuals.md` then permitted. |
| candidate-d3 (run 1) | pass | Templated diagram page with Mermaid variant, pinned script, path reported, both failure paths. |
| candidate2-d1 (run 2) | TF-c pass; AC10 pass | Kit classes only; sidebar via `wf-col is-narrow`; `Option index` status. |
| candidate2-d2 (run 2) | AC11 pass | Retained `option-b.html` differs from the draft only in status. |

- Correction round 1 between runs: grader findings F1 (footer change permitted, contradicting AC11),
  F2 (no column width in kit), F3-F5 (title, instruction comment, index status) fixed. Run-1 results
  are preserved. N1 (footer vs `reference.md` precedence) fixed after run 2 with one line; not re-run.
- `design.md` hash differs from `frozen.sha256` only by the appended, pre-run-2 addendum.
- Limits: one observation per case; D3 not re-run after the template comment/title change; browser
  rendering at phone width, dark mode, and Mermaid offline not verified in a browser in run 2;
  Codex, Cursor, Xcode untested. Several replies condensed by the coordinator (`trials/REPLY-NOTES.txt`).
