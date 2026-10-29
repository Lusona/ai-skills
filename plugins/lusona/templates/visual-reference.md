# Visual reference: <record-id>

<!-- Apply the visual rules in ../references/visuals.md. Save only after the user chooses and
before recording the decision. Keep this file beside the chosen visual in
docs/lusona/visuals/<record-id>/. Omit unused fields. -->

- Chosen option: <letter and short name>, chosen by <user> on <YYYY-MM-DD>
- Source: <relative link to option-<letter>.html, or to the Mermaid Markdown file>
- Owner: <relative link to the owning spec, ADR, or notes>

## Images

<!-- Capture only after the user agrees to the design. One PNG per shown state of the whole page; each shows all screens. If screenshot capture was
unavailable, say so here and keep the HTML source alone. -->

- <link to option-<letter>-<state>.png>: <state>; screens <names>

## Binding

<!-- Acceptance input for implement and review. Defaults: layout regions, element order, which
controls exist, and information hierarchy. Add other aspects only when the user marks them binding.
An item may name a screen and state, e.g. "Shared list, failed: Retry appears below the title". -->

- V1: <screen and state, when specific>: <observable aspect that must match>

## Illustrative

<!-- Not acceptance. Defaults: colors, copy, and spacing unless the user marks them binding. -->

- <aspect shown for illustration only>

## Fidelity

<!-- What the images approximate, e.g. production uses system components. -->

- <approximate aspect>

## Rejected options

<!-- One line per rejected option. Do not save the index or rejected option files. -->

- <letter>: <short name>; <reason>
