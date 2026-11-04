# Notes: next-action-table

Context: direct documentation change without a spec; the user requested a distinctive
"next step" output in substantive replies.

## 2026-11-03 — Next action presentation format

### Question and scope

- Question: how the next action should look in substantive replies so it stands apart
  from the Result and Evidence prose.
- Scope: the always-loaded presentation rule in `plugins/lusona/README.md`
  (Review and communication) and the illustrative handoff in the root `README.md`.
  Record templates under `plugins/lusona/templates/` and
  `references/delegation.md#assignment-results` are unchanged.

### Evidence

- Method: three layouts were offered through the native question tool with rendered
  previews: a one-row table, a vertical key/value table, and a one-line callout.
- Result: `python3 scripts/check_instructions.py` passes;
  `python3 -m unittest scripts.test_instructions` passes 11 tests. Rendering was observed
  once in the Claude Code terminal; other hosts were not tested.
- Limitations: GFM table cells cannot hold line breaks or blockquotes, so the
  continuation prompt sits below the table.

### Conclusion and decisions

- Decision, 2026-11-03 (user): when work remains, the next action is a one-row table
  `Next action | Owner | Needs | Authority`, followed by a continuation prompt in a
  blockquote when one is useful. When complete, the plain label
  **Next action:** `None for this request` is used without a table.
- Decision, 2026-11-03 (user): scope is chat replies only; record templates keep their
  `Next action` fields.
- Decision, 2026-11-03 (parent): where tables do not render, the label form carries the
  same fields in prose, consistent with the existing host-formatting override.

## Current handoff

- Authorized work: documentation edits only; no commit was requested.
- Next action: user reviews the two README diffs; commit requires a separate request.
