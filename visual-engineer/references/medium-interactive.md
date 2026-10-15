# Medium — interactive

Live on screen: dashboards, explorable charts, filterable views, anything
where the reader acts on it.

**Chosen when:** the reader needs to filter, drill in, monitor over time, or
the data updates.

**Not chosen when:** it will be screenshotted, printed, or pasted into a doc
— that's `medium-static-image.md`. Interactive artifacts screenshot badly and
lose the thing that justified them.

## Build

- Single self-contained HTML file by default. Inline the CSS and JS; embed
  assets as data URIs. Portable beats modular at this size.
- Pull values from the project's system — CSS custom properties, imported
  tokens, or the bootstrapped `design-tokens.md`. Never hardcode a hex that
  isn't from the system.
- Responsive by default: relative units, flex/grid, `max-width: 100%` on
  media. Wide content — tables, dense charts — scrolls inside its own
  `overflow-x: auto` container. The page body never scrolls sideways.
- Theme-aware if the system defines both: `@media (prefers-color-scheme:
  dark)` plus an explicit override hook.
- Charts: hand-written SVG for anything simple. A library only when
  interaction genuinely demands it. Either way, the encoding rules in
  `encoding.md` override every library default — especially zero baselines,
  sort order, and direct labelling over legends.

## Interaction

- **The default view must answer the main question with no interaction at
  all.** Interaction is for follow-ups. If the first thing the reader must do
  is configure something, the default view failed.
- Hover for detail, click for change of state. Don't hide primary information
  behind hover — it doesn't exist on touch, and it doesn't survive a
  screenshot.
- Every control is labelled and its current state is visible without
  interacting.
- Empty, loading, and error states are part of the design, not an oversight.
  An empty state says what would appear and why it's empty.
- Targets ≥ 44 px. Motion respects `prefers-reduced-motion` and never carries
  information on its own.

## Layout

- Most important view top-left, at full width if it's the answer.
- Supporting panels below in a consistent grid — same gutter, same panel
  height where possible.
- Same variable, same encoding, same axis range across every panel
  (`composition.md` § Multi-visual coherence).
- Don't fill the viewport for its own sake. A dashboard with four honest
  panels beats one with nine, three of which are decorative.

## Verify

- [ ] Renders with a clean console — no 404s, no JS errors
- [ ] Body doesn't scroll horizontally at 375 px wide
- [ ] Works at 1280 px and at 1920 px
- [ ] Every interactive control does what its label says
- [ ] Default view answers the main question with zero clicks
- [ ] Reads correctly with colour removed (test in greyscale)
- [ ] Numbers match the source — spot-check at least two
