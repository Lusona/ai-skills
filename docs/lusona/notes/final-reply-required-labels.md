# Notes: final-reply-required-labels

Context: direct change to the final-reply form without a spec. It addresses the queue item on
Codex replies that omit the `Result` and `Evidence` labels (check C9,
[run](../evidence/2026-11-11-rewrite-suite-run/README.md)).

## 2026-11-11 — Required labels and fields survive formatting preferences

### Question and scope

- Agreement (user, 2026-11-11, conversation: "let's make the copy authorative"): the sentence
  below, already in the working tree of `shared/final-reply.md`, is the accepted text of the
  final-reply form.
  - New: "Preserve the required labels and fields unless a user or host instruction explicitly
    requires an incompatible format. Brevity preferences do not remove required fields. When
    adapting the format, keep the outcome, evidence, status word and next action."
  - Replaced: "User and host formatting instructions override this form. Keep the outcome,
    evidence, status word and next action in the permitted format."
- Origin (user's report, 2026-11-11, conversation): GPT Astra suggested the sentence because
  Codex did not follow the final-reply and formatting requirements. The user reports that "it
  seem to work". The session that applied it left no record.
- Scope (user, 2026-11-11, native question tool, "All of them"): the sentence that restates
  the old rule in `plugins/lusona/templates/status.md.template`, in `README.md` and in the
  four README translations, and one line in `CHANGELOG.md`.
- TDD level: `none` (user, 2026-11-11, native question tool).
- Decision revised in part: recorded as
  [decision 29](../specs/20261111-loop-principles-and-skill-rewrite.md#decisions-and-uncertainty).

### Evidence

- Method: the coordinator applied seven exact-match replacements without a leaf and wrote the
  four translated sentences itself. `shared/final-reply.md` and the 14 generated regions were
  not edited in this pass; they already held the new sentence.
- Result (2026-11-11, working tree on `c9bd02a`), all exit 0:
  - `sync_shared.py --check`, `check_voice.py`, `check_skill_template.py`, `check_contract.py`,
    `check_instructions.py`.
  - Unit tests: `test_sync_shared` (18), `test_voice` (49), `test_skill_template` (64),
    `test_contract` (65), `test_instructions` (16), `test_package` (14),
    `test_rule_inventory` (3).
  - `python3 scripts/package.py --output tmp/final-reply-labels-pkg` built `lusona-3.0.0.zip`.
  - `python3 -I tmp/readme-rewrite/check_links.py .`: 69 relative links, 12 index entries.
  - `python3 -I tmp/final-reply-labels/check_translations.py`: each translation passes with 72
    links and 12 index entries. This is a copy of `tmp/readme-rewrite/check_translations.py`
    without its assertion on the SHA-256 of the earlier approved English text; the original
    fails on that assertion because `README.md` changed. New SHA-256 of `README.md`:
    `d7ab637b54bc6fbb9f3545c6b94e2ea23f2d34614a64eaa686a5e8d00867b36a`.
  - `python3 scripts/check_rule_inventory.py docs/lusona/notes/rule-inventory-34186da.md
    34186da`: exit 0, "TOTAL: 22 files, 1141 content lines, 1167 rows,
    PASS".
  - `git diff --check`: clean. A grep of `README*.md`, `plugins/` and `shared/` finds no
    remaining copy of the replaced sentence in any of the five languages.
- Limitations:
  - No agent run was observed in this pass. The effect on Codex is the user's report, not a
    measurement; the loop-conformance suite was not rerun, so the C9 marks of 3/5
    (`authz-change`) and 4/5 (`tdd-stated`) are not re-measured.
  - No check asserts the new sentence. `check_contract.py` passes with the new text; its pass
    with the old text is a recorded result at `70823d6`, not rerun here.
  - The four translated sentences have no independent or native-speaker review.
  - Rendered Markdown, installation and interactive behavior were not tested.
  - The suite spec still states "host formatting overrides are not failures of C9"
    ([suite spec](../specs/20261109-loop-conformance-suite.md)). An explicit incompatible host
    format still overrides the form, so the two agree; the grading was not changed.

### Conclusion and decisions

- Inspected and left unchanged: `plugins/lusona/templates/spec.md.template:16`, "Follow user
  and host formatting constraints." It concerns the format of the spec record, not the reply
  form.
- Deviation: implement-type work was done by the coordinator without a leaf, including the
  wording of the template, README and translated sentences. The Role exception of decision 28
  covers only `status` and `explore`.
- Decision: the new sentence is accepted and the six restating sentences now agree with it
  (user, 2026-11-11, sources above).
- Coordinator wording, within the accepted meaning: the status template says "Keep its required
  labels and fields unless a user or host instruction explicitly requires an incompatible
  format."; the README says "The reply keeps the required labels and fields unless you or the
  host explicitly require an incompatible format. A preference for brevity does not remove
  them. In an adapted format, the outcome, evidence, status and next action remain."

## Current handoff

- Authority: the accepted sentence, the seven edits above, TDD `none`. Commit, push,
  publication and a suite run are not authorized.
- State: closed on 2026-11-11 without a Codex rerun of C9 (user, conversation, "accept and
  close without a rerun") and recorded in
  [history](../history/2026-11-week-02.md#2026-11-11--final-reply-required-labels). The change
  is in the working tree, uncommitted.
- Next action: none for this item.
