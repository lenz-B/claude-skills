# Composition — how it's arranged

Consistency comes from a system, not from restraint in the moment.

**Declare the structure before placing anything.** State — in a comment at
the top of the artifact, or out loud — the grid, the spacing unit, the type
steps you're using, and the section pattern. Deciding these element by
element is what produces output that looks assembled rather than designed.

## Grid

- Pick a column count and commit. 12 for flexible screen layouts, 6 for
  simpler ones, 3–4 for print and posters.
- **The gutter is part of the grid.** A consistent gutter does more for
  coherence than the column count does.
- Vertical rhythm matters as much as horizontal. Set a base unit (commonly
  4 or 8 px, or a mm value in print) and make every margin, gap, and padding
  a multiple of it. Arbitrary values are the single most common source of
  "something's off but I can't say what."
- Breaking the grid is legitimate — but deliberately, once, for the thing
  that matters most. Break it twice and there was no grid.

## Alignment

- Every element aligns to something. If you can't name what an edge aligns
  to, it's wrong.
- **Fewer alignment lines is stronger.** Three elements on one line reads
  better than three elements on three near-identical lines.
- **Optical over mathematical.** Round shapes need to overshoot their box
  slightly to look aligned with square ones. Text hangs punctuation outside
  the margin. Trust the eye over the number.
- Left-align text blocks. Centred text is for short display lines only —
  a centred paragraph gives the eye no reliable return edge.

## Hierarchy

Rank the content **before** styling it. Ask: if the reader takes only one
thing away, what is it? That's level 1. There is exactly one.

Tools for creating levels, roughly in order of strength:

**size · isolation (whitespace around it) · position (top-left, or
optical centre) · weight · contrast against ground · colour**

- **Isolation is underrated.** Whitespace around an element makes it dominant
  without making it bigger — and it costs nothing from the design system.
- **Three levels is usually enough.** Five is almost always too many; the
  reader stops perceiving them as ranked.
- **Skip steps.** Level 1 and level 2 must be *obviously* different. Adjacent
  sizes read as an accident rather than a decision.
- State the requirement to the system: *"three type levels, clearly stepped"*
  — the system supplies the sizes.

## Proportion

- Set a type scale with a stated ratio (1.2 minor third for dense
  information, 1.5 for display-heavy work). Every step comes from the ratio,
  not from taste.
- Useful compositional ratios: thirds, golden section (≈1.618), 2:3, 3:4.
  They're starting points that reliably avoid the dead-centre split, not
  laws.
- **Avoid near-symmetry.** Either genuinely centred or clearly off-centre.
  Almost-centred reads as a mistake.

## Balance

- Visual weight comes from size, density, contrast, and isolation — not area
  alone. A small dark element balances a large pale one.
- **Symmetric** = stable, formal, static. Right for certificates, title
  slides, formal notices.
- **Asymmetric** = dynamic, directional, modern. Right for most information
  work. Needs a counterweight — an empty area is a counterweight.
- Check by squinting until detail disappears: the blocks of weight should
  feel settled, not tipped.

## Rhythm and repetition

- Repeat the same treatment for the same kind of thing, every time. Section
  headers all identical. Captions all identical.
- Consistent intervals between repeated elements. Varying gaps implies
  grouping you didn't intend (see `perception.md` § Proximity).
- Introduce variation only to signal a real difference in kind.

## Density

- Density is a decision, not a leftover. Dense is correct for a monitoring
  dashboard; sparse is correct for a poster read at 3 m.
- Set it once for the whole artifact and hold it. Mixed density reads as
  unfinished.
- More content usually needs **more structure**, not smaller type.

## Framing

- Margins are the frame. Generous and equal on left/right; bottom margin
  slightly larger than top is the classical proportion and still reads well.
- **Nothing touches the edge** unless it deliberately bleeds off it. Half-cut
  elements at a boundary read as broken rendering.
- Nothing overlaps unintentionally. Overlap is a strong signal — use it to
  mean something or not at all.

## Scale floors

Minima, not starting points. Specify the requirement; the system supplies the
value.

| Context | Floor |
|---|---|
| slide body text (1920×1080) | ≥ 24 px |
| print body text | ≥ 12 pt |
| print caption / label | ≥ 9 pt |
| poster read at 3 m | headline ≥ 100 pt, body ≥ 24 pt |
| poster read at 1 m | headline ≥ 48 pt, body ≥ 14 pt |
| screen body text | ≥ 16 px |
| chart axis label | ≥ 11 px screen, ≥ 8 pt print |
| interactive target | ≥ 44 px |

If content doesn't fit above the floor, **the content is too much** — cut it
or split it. Never shrink below the floor to fit.

## Multi-visual coherence

For decks, dashboards, and multi-page documents — a set of visuals that
disagree with each other is worse than any one of them alone.

- Same grid across every panel or page.
- Same encoding for the same variable everywhere (`encoding.md`
  § Consistency).
- Same axis ranges when panels are meant to be compared. Different ranges
  make identical patterns look different, and different patterns look
  identical.
- Same density, same margins, same header pattern throughout.
- **Small multiples over one crowded composite** whenever the comparison is
  the point (`reduction.md`).
