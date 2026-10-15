# Perception — how the eye actually reads it

What the reader sees first, and what they read *as belonging together*, is
usually decided before they consciously look at anything. These effects are
automatic. You either use them or fight them.

## Pre-attentive attributes

Some properties are processed before conscious attention — in roughly 200 ms,
regardless of how many other elements are present:

**hue · intensity · size · orientation · curvature · added marks ·
enclosure · position · motion**

One item differing in one of these *pops out* instantly. This is the
mechanism behind every "draw attention to X" instruction.

Two rules:

- **One pop-out per view.** Two competing pop-outs cancel — the reader now
  has to search, which is the thing you were avoiding.
- **Pop-out fails on combinations.** "The large red one" among large blue and
  small red items requires a serial search. Differ in *one* attribute.

## Gestalt grouping

The reader groups elements automatically, by these rules, in roughly this
order of strength:

- **Proximity** — near things read as one group. The strongest and cheapest
  grouping tool you have. Adjust spacing before reaching for a border.
- **Common region** — a shared enclosure or background binds elements, even
  across distance. Beats proximity when they conflict.
- **Similarity** — same shape, size, or colour reads as same kind.
- **Continuity** — the eye follows lines and alignments through gaps.
  Misalignment reads as a new group whether you meant it or not.
- **Closure** — implied boundaries are perceived as complete. You rarely need
  a full box; three aligned edges imply the fourth.
- **Connection** — an explicit line binds more strongly than any of the
  above. Use for genuine relationships only.

**Practical consequence:** if two things must read as related, put them
close, align them, and give them a shared region. If two things must read as
separate, separating them in space beats drawing a divider — a divider is
another mark competing for attention.

**Whitespace does the work.** Most cluttered layouts are not too full; they
are evenly spaced. Uneven spacing is what creates structure.

## Figure and ground

Every element is read as either figure (object) or ground (field). Ambiguity
here is exhausting to look at.

- Keep the ground quiet. A busy background makes every foreground element
  compete.
- Contrast in *value* separates figure from ground more reliably than
  contrast in hue.
- Don't let decoration sit at the same visual weight as data.

## Scan paths

Where the eye starts and travels — for left-to-right readers:

- **Z-pattern** — sparse layouts, posters, landing pages. Top-left → top-right
  → diagonal → bottom-right. Put the destination at bottom-right.
- **F-pattern** — text-dense layouts. Strong horizontal at top, second
  shorter horizontal, then a vertical scan down the left. Front-load every
  line; the right end of a line is rarely read.
- **Gutenberg diagram** — evenly-weighted layouts. Primary optical area at
  top-left, terminal at bottom-right, and two weak fallow corners at
  top-right and bottom-left. Don't put anything essential in the fallow
  corners.
- **Charts** — the eye goes to the largest mark, the most isolated mark, and
  the extremes of a sorted sequence. Sorting puts the answer where the eye
  already lands.

**Entry point:** every artifact needs exactly one obvious place to begin. If
you can't say where it is, the reader can't either.

## Accessibility floor

Not optional, and mostly structural rather than stylistic:

- **Never colour alone.** Every distinction carried by colour must also be
  carried by position, shape, direct label, or pattern. Roughly 1 in 12 men
  cannot read red/green apart, and every artifact eventually gets printed in
  greyscale or photographed badly.
  → Direct-label lines at their ends instead of relying on a colour legend.
  → Vary marker shape as well as colour in scatter plots.
- **Legibility is a distance function.** Specify the viewing distance; the
  system supplies the size. See `composition.md` § Scale floors.
- **Interactive targets ≥ 44 px.**
- **Motion is optional.** Anything conveyed by animation must also exist in a
  static state. Respect `prefers-reduced-motion`.
- **Don't encode meaning in position alone for screen-readable output** —
  a static image still needs a text alternative stating what it shows.

## Legends

A legend forces the reader to look away, memorise a mapping, and look back —
every single time. It's a tax on every reading.

**Direct labelling beats a legend** in nearly every case. Label lines at
their right end, label bars in or beside the bar, label the two or three
points that matter in a scatter.

Keep a legend only when marks are too dense to label individually — and even
then, order the legend to match the visual order of the data, never
alphabetically.
