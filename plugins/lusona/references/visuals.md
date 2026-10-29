# Visual options and references

Read for explore, specify, and architect when a choice is easier to judge visually or a diagram
clarifies the decision, and for implement and review when the
owning record links a visual reference. Paths under `docs/lusona/` are in the consuming project.

## When

- Offer 2-4 visual options when a concept, architecture, or UI choice is better judged by
  seeing it than by reading a description. Do not offer options during implement when the
  agreement already settles the choice.
- Include a diagram when it clarifies the decision.

## Content

- Read the existing UI first. Reuse its screen names, navigation, tab bars, and copy; label
  placeholders for content that does not exist yet.
- Style option content for the target platform or the project's theme in the page's
  `option-style` block. Show mobile UI in a plain, content-sized panel without phone bezels,
  hardware cutouts, or simulated system bars. Use the wireframe kit when no platform look is known.
- Scale fidelity to the question: wireframe for structure, closer styling for look and feel.
  Use real content when it affects the judgment.
- An option may be a flow of 2-5 screens; number steps only for a sequence.
- Show states relevant to the choice, including failure when it affects the decision, using
  the state switch or separate screens.
- When options differ in one part of a flow, write one flow page with the in-place option switch,
  a one-line tradeoff per option, and the recommended option marked.
- Explain the question on the page. In the notes, state what is approximate, such as system
  components drawn by hand, and list open questions and must-not-happen rules.

## Presentation

- Show a simple diagram inline in the reply as Unicode or ASCII text. Write a larger diagram or a
  UI mockup as an HTML page.
- Start every option, index, flow, and diagram page from the
  [visual page template](../templates/visual-page.html) and follow its top comment. Copy the file;
  read only its top comment and body markup, not the shell CSS. Pages stay
  self-contained except the pinned Mermaid script; its source stays readable without the script.
- Write one file per option (`a.html`, `b.html`, ...) and an `index.html` that shows them side by
  side. Use one in-place switch page instead only when the options differ in one part of a flow.
- Open the index, switch, or diagram HTML file in the browser for direct inspection; if the host
  cannot open it, report its absolute path. Do not capture draft pages or present PNGs in place
  of the browser. Capture the chosen design only after the user agrees to it.
- Write draft pages outside tracked records: in a host-provided session scratch directory or the
  project's ignored temporary directory.

## Choice

Label options A, B, C, D. Ask the user to choose by letter through the native question tool
under [Questions and next actions](../README.md#questions-and-next-actions), otherwise in plain
text. There is no click-capture server. If the user rejects all options or asks for revision,
save nothing and offer revised options.

## Retention after a choice

After the user chooses, retain the reference before recording the decision, within the core
write authority and no-save restrictions; otherwise report the reference in the response.
Records never link draft pages.

- Directory: `docs/lusona/visuals/<record-id>/`, where `<record-id>` is the owning spec or ADR
  basename, or the notes slug when no spec exists yet.
- `option-<letter>.html`: the chosen option's source with only its status changed to
  `Chosen reference`. From a switch page, also delete the other options' elements and the option
  switch. Save a diagram as Mermaid in a Markdown file instead.
- `option-<letter>.png`, or `option-<letter>-<state>.png` per shown state: capture the whole
  page in the light theme with an available screenshot tool. Include every screen without
  clipping and inspect each image. If capture is unavailable, retain the HTML and report the
  missing images.
- `reference.md` from the [visual reference template](../templates/visual-reference.md): chosen
  option, chooser and date, images, HTML source, owner link, binding items, illustrative items,
  fidelity, and one line per rejected option with the reason.
- Binding items (V1, V2, ...) default to layout regions, element order, which controls exist, and
  information hierarchy, and may name a screen and state. Illustrative items default to colors,
  copy, and spacing unless the user marks them binding.
- Do not retain the index or rejected option files.
- Link `reference.md` from the owning spec, ADR, or notes. When page notes and `reference.md`
  disagree, `reference.md` governs.

A user-supplied reference keeps its existing capture in specify. Retain it this way only when
the user asks.

## Consumption

- Implement reads `reference.md`, the PNGs, and the HTML source, treats each binding item as
  acceptance input, and reports each item's status in its result. Illustrative items are not
  acceptance.
- Review reads `reference.md`, the PNGs, and the HTML source, checks each binding item against the
  result, and reports it as met, unmet, or unchecked; a partly met item is unmet, with what differs.
  When the result can be rendered and screenshotted with available tools, compare the screenshot
  with the retained PNGs. Otherwise check against code or markup, report the visual comparison as
  unrun, and identify what remains unverified.
- A record without a visual reference leaves implement and review unchanged.
