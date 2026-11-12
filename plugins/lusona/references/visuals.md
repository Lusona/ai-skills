# Visual options and references

Read before offering visual options or a diagram, and before implementing or reviewing work whose owning record links a visual reference.

## When to offer options

- Offer 2-4 visual options when a concept, architecture or UI choice depends on layout, structure, flow or appearance that a description does not show.
- Do not offer options during implementation when the agreement already settles the choice.
- Include a diagram when it shows a relationship, sequence or structure that the decision depends on.

## UI content

- Read the existing UI first. Reuse its screen names, navigation, tab bars and copy. Label placeholders for content that does not exist yet.
- Style option content for the target platform or the project's theme in the page's `option-style` block.
- Show mobile UI in a plain, content-sized panel without phone bezels, hardware cutouts or simulated system bars.
- Use the wireframe kit when no platform look is known.
- Match fidelity to the question: wireframe for a question about structure, target-platform or project-theme styling for a question about appearance.
- Use real content when it affects the judgment.
- An option may be a flow of 2-5 screens. Number the steps only for a sequence.
- Show the states the choice depends on, including failure when it affects the decision. Use the state switch or separate screens.
- When options differ in one part of a flow, write one flow page with the in-place option switch. Give a one-line tradeoff per option and mark the recommended option.
- Explain the question on the page.
- In the page notes, state what is approximate, such as system components drawn by hand. List open questions and must-not-happen rules.

## Presentation

- Present diagrams in fenced `mermaid` code blocks, in the reply or a Markdown file.
- Use Mermaid Markdown for diagram options too. Do not create diagram HTML or PNGs.
- Start UI option, index and flow pages from the [visual page template](../templates/visual-page.html.template). Follow its top comment.
- Copy the template file. Read only its top comment and body markup, not the shell CSS.
- Write each page as a self-contained file.
- Write one HTML file per UI option (`a.html`, `b.html`, ...) and an `index.html` that shows them side by side.
- Use one in-place switch page instead only when options differ in one part of a flow.
- Open the UI index or switch page in the browser for direct inspection. When the host cannot open it, report its absolute path.
- Write drafts outside tracked records: in a host-provided session scratch directory or the project's ignored temporary directory.
- Present drafts in the browser without capturing them. Capture the chosen UI design only after the user agrees to it.

## Choice

- Label options A, B, C, D. Ask the user to choose by letter in the conversation; the pages do not capture clicks.
- When the user rejects all options or asks for revision, do not retain the rejected draft pages, and offer revised options.
- Save in the owning record each new constraint and each rejection reason that later options depend on.

## Retention after a choice

After the user chooses, retain the reference before recording the decision. When saving is prevented, report the reference in the reply. Do not link draft pages from records.

- Directory: `docs/lusona/visuals/<record-id>/`. `<record-id>` is the owning spec or ADR basename, or the notes slug when no spec exists yet.
- UI mockup: retain `option-<letter>.html` with only its status changed to `Chosen reference`. From a switch page, also delete the other options' elements and the option switch.
- Capture `option-<letter>.png`, or `option-<letter>-<state>.png` per shown state, in the light theme with an available screenshot tool.
- Include every screen without clipping. Inspect each image.
- When capture is unavailable, retain the HTML and report the missing images.
- Diagram: retain `option-<letter>.md` with the fenced `mermaid` source, without HTML or PNGs.
- Write `reference.md` from the [visual reference template](../templates/visual-reference.md.template). Record the chosen option, chooser and date, source, UI images when present, owner link, binding items, illustrative items, fidelity, and one line per rejected option with its reason.
- Binding items (V1, V2, ...) default to layout regions, element order, which controls exist, and information hierarchy. Add another aspect only when the user marks it binding. A binding item may name a screen and state.
- Illustrative items default to colors, copy and spacing, unless the user marks them binding.
- Do not retain the index or rejected option files.
- Link `reference.md` from the owning spec, ADR or notes.
- When page notes and `reference.md` disagree, `reference.md` governs.
- During specification, keep a user-supplied reference as captured. Retain it in this directory only when the user asks.

## Implementing and reviewing against a reference

- Read `reference.md` and its source: Mermaid Markdown for diagrams; HTML and any retained PNGs for UI mockups.
- Binding items are acceptance input. Illustrative items are not.
- When implementing, report the status of each binding item.
- When reviewing, check each binding item against the result. Report it as met, unmet or unchecked. A partly met item is unmet; state what differs.
- Check diagrams against their Mermaid source.
- For a UI mockup with retained PNGs, compare a screenshot of the result when rendering and capture tools are available.
- Otherwise, check code or markup, report the visual comparison as unrun, and name what remains unverified.
- A record without a visual reference adds no visual check.
