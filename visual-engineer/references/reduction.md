# Reduction — what to remove

The discipline of subtraction. This is usually where competent output and
good output actually diverge — not in what was added.

## Data-ink ratio

Tufte: of all the ink on the page, what fraction encodes actual information?
Maximise it, within reason.

**Erase in this order, and check the reading after each:**

1. Backgrounds and fills behind plotting areas
2. Gridlines — remove entirely, or reduce to the faintest line that still
   guides. Never darker than the data.
3. Chart borders and panel frames
4. Redundant axis ticks — 3–5 labelled ticks is usually enough, not 12
5. Tick marks themselves, once labels are legible without them
6. Legends, replaced by direct labels (`perception.md` § Legends)
7. Axis lines, where the marks already imply the baseline
8. Data labels on every point — label the ones that matter, not all of them

**Stop when removing the next thing makes it harder to read.** Minimalism is
not the goal; clarity is. A stripped chart nobody can read is a failure with
better taste.

## Chartjunk

Remove entirely, always:

- 3D effects, extrusion, perspective on 2D data — these distort quantities,
  so they're an honesty problem, not just a taste one
- Drop shadows, bevels, glows on data marks
- Gradient fills that carry no meaning
- Decorative background images behind data
- Icons standing in for bars or points
- Moiré patterns — hatching, dense stripes, high-contrast textures that
  vibrate
- Heavy borders around everything
- Duplicated information: a value shown as bar length, printed on the bar,
  *and* listed in a legend

**The test:** does removing it lose any information? If no, it was junk.

## Small multiples

The strongest comparison tool available, and consistently underused.

Instead of one chart with eight overlapping series, draw eight small charts
in a grid — identical scale, identical axes, identical everything except the
data.

Use whenever:

- more than 4–5 series would overlap in one frame
- the same measure is being compared across categories, stores, regions, or
  periods
- the reader needs to compare *shapes* rather than read exact values

Requirements: identical axis ranges across every panel (otherwise the
comparison is a lie), a clear label per panel, a sensible panel order —
sorted by value, not alphabetically — and axis labels once at the edge
rather than repeated in every panel.

## Layering

When elements can't be removed, push them back. Establish a clear visual
stratification:

```
foreground  the data, the answer, the one thing that matters
mid         supporting marks, direct labels, reference lines
background  gridlines, axes, annotation, context
```

Separate layers by **weight and value contrast**, not by hue. Background
elements should be perceptible when looked for and invisible when not.

If everything is the same weight, everything competes, and the reader has to
do the prioritising you were supposed to do for them.

## Progressive disclosure

Not everything belongs in the first view.

- **Overview first, detail on demand.** The first read answers the main
  question; the detail answers follow-ups.
- Interactive → detail in tooltips, expansion, drill-down.
- Static → detail in a companion table or an appendix, not crammed in.
- Print → one idea per piece. If it needs two, it's two pieces.

## Annotation

The most valuable ink you can add — and the most commonly missing.

- **State the finding in words on the artifact.** "Upside is 40 % below the
  other two" beats making the reader derive it. A chart that requires
  interpretation will be interpreted wrong.
- Annotate the specific point that matters — the spike, the crossover, the
  outlier — directly, next to it.
- Note the caveat where it applies, not in a footnote: broken series,
  excluded rows, changed methodology, small n.
- Source and date, always, quietly, at the bottom.

Annotation adds ink and *increases* the data-ink ratio in effect, because it
increases delivered information. Reduction is about removing what doesn't
inform, not about saying less.

## The last pass

Before calling it done, one deliberate removal pass:

- What can be deleted without losing meaning?
- What is said twice?
- What did I add because the space looked empty? — Remove it. Empty space is
  a compositional tool, not a defect (`composition.md`).
- What would a reader with 5 seconds miss?

If nothing can be removed, you probably haven't looked properly.
