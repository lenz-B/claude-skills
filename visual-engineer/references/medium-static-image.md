# Medium — static image

A fixed image that travels: embedded in a document, README, issue, chat,
email, or slide built elsewhere.

**Chosen when:** it will be pasted somewhere you don't control, or it needs
to survive being forwarded.

**Not chosen when:** the reader needs to filter or explore
(`medium-interactive.md`), or it's going to physical paper
(`medium-print.md`).

## Format

**SVG** by default — sharp at any size, small, diffable in git, text stays
selectable and searchable. Use for charts, diagrams, anything vector.

**PNG** when the destination can't render SVG (many chat clients, some email,
some issue trackers) or when the image is genuinely raster. Export at 2× the
display size for sharp rendering on high-DPI screens.

Author in HTML/CSS and export, or write SVG directly. Both are fine; SVG
directly is usually cleaner for a single chart.

## Build

- **Design for one fixed size and commit to it.** No responsive behaviour
  exists here. Decide the display width first, then design for it.
- Common widths: 800 px for a README or issue, 1200 px for a document or blog,
  600 px for email.
- Embed fonts as paths, or use a system-safe stack from the design system.
  A referenced webfont will not load in most destinations — this is the most
  common way an exported image arrives broken.
- No external references of any kind. Everything inlined.
- Text at the final size must clear the floors in `composition.md`. There is
  no zooming in a README preview.

## Composition

- **One idea per image.** If it needs a paragraph of explanation to make
  sense, split it or annotate it directly.
- Title inside the image — captions get lost when the image is forwarded, and
  a chart with no title is unreadable out of context.
- Direct labels, never a legend (`perception.md` § Legends). Nothing to
  cross-reference off-image.
- Source and date inside the image, quietly, bottom edge. This image will
  outlive the context it was made in.
- Generous margin inside the canvas. Content touching the image edge looks
  cropped once it's placed against a page background.
- Assume it will be viewed against both white and dark backgrounds. A
  transparent PNG with dark text vanishes on a dark page — either give it an
  explicit background from the system, or verify both.

## Verify

- [ ] Opens standalone and renders identically outside the authoring context
- [ ] Fonts render — no fallback substitution, no missing glyphs
- [ ] Legible at the intended display width, not just zoomed in
- [ ] Nothing clipped at the canvas edge
- [ ] Readable against both light and dark page backgrounds
- [ ] Title, source, and date are inside the image
- [ ] Reads correctly in greyscale
- [ ] Numbers match the source — spot-check at least two
