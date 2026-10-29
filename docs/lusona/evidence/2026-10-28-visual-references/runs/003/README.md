# Run 003 — platform-styled options, flows, states, PNG retention (AC9, AC11, AC13-AC19)

Owner: [topic](../../README.md). Inputs, fixtures, trials, grades: [evidence.zip](evidence.zip)
(`design.md`, `evaluator/criteria.md`, `evaluator/grades.md`; scratch screenshots excluded).
Source delta from the pre-run working tree: [source.patch](source.patch) (includes F1-F8 fixes).

- Trigger: the user reviewed an example iOS mockup against Lusona's template and revised the
  criteria (see spec constraints 12-20, AC13-AC19).
- TDD targeted (user). Test-first TF-d (E1, AC13) and TF-e (E2, AC11). Baseline: working tree
  before run-003 edits. Fixture: a small SwiftUI app "Packlist". Actors: Claude Code subagents,
  Sonnet; grader: independent Opus agent. Headless Chrome available to actors; no Xcode.

| Trial | Grade | Observation |
| --- | --- | --- |
| baseline-e1 | TF-d fail (expected red) | Real names, but a generic grayscale wireframe; no iOS look. |
| candidate-e1 | TF-d pass; AC9, AC14, AC15, AC17, AC18 pass | iPhone frames, "Lisbon, 4 nights", tab bar, 3-screen flows with a save-failed state, fidelity and open questions. |
| baseline-e2 | TF-e fail (expected red) | Nothing retained; spec linked the draft `tmp/options/b.html`. |
| candidate-e2 | TF-e pass | `option-b.html` (status only changed), `option-b.png`, `reference.md` V1-V5; index and rejected files not kept. |
| candidate-e3 | AC16 pass | One page with in-place A/B/C switch, tradeoffs, A recommended, choice by letter. |
| candidate-e4 | AC19/AC7 pass (deviation) | V1, V2 unmet; V3 reported "partially met" with the cleared text raised as High; screenshot comparison reported unrun. |

- Baseline-e2 also shows that the 1.3.0 retention rule was not followed in that observation; the
  candidate's retention-before-recording trigger addressed it in candidate-e2.
- E4 used "partially met", outside the met/unmet/unchecked set; graded on meaning. The rule now
  says a partly met item is unmet with what differs.
- E4 fixture defect (setup): its reference HTML and PNGs were copied from a sample page with a
  different record ID, title, and tabs, and still contained option B. The trial still exercised
  binding-item checks from `reference.md`; a future review trial needs a correctly retained page.
- Correction round after grading: F1 (index captions reused one placeholder, medium), F2-F8 (low:
  switch-page condition, review reads PNGs, write-permission wording in triggers, PNG-per-state
  wording, mixed-case state names, malformed hash, light theme in capture command) fixed; F5 and
  F7 rechecked in headless Chrome; repository checks pass. Not re-run in trials.
- `evaluator/criteria.md` differs from `frozen.sha256` only by the E4 deviation list appended as
  declared in `design.md`.
- Limits: one observation per case; replies condensed by the coordinator (`trials/REPLY-NOTES.txt`);
  Safari, Firefox, offline Mermaid, Codex, Cursor, and Xcode untested; template is about 25 KB.
