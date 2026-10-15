# Encoding — turning material into marks, honestly

The core question: *which visual property should carry this information?*
Not a matter of taste. Human accuracy at reading each property has been
measured, and the ranking is stable.

## The visual variables

Bertin's set — the properties a mark can vary in:

**position · length · angle · slope · area · volume · shape · texture ·
orientation · colour hue · colour value**

Colour is **one of eleven**. Most of this skill's work happens in the other
ten, which is why deferring colour to the design system costs almost nothing.

## Accuracy ranking

Cleveland & McGill, most accurately read first:

```
1. position on a common scale      ← use this whenever you can
2. position on identical, non-aligned scales
3. length
4. angle / slope
5. area
6. volume, curvature
7. shading, colour saturation      ← use only for what tolerates imprecision
```

**Rule: encode the most important quantity with the highest-ranked variable
available.** A bar chart beats a pie chart for comparison because position and
length beat angle and area — measured, not stylistic.

Push secondary information down the ranking. Colour and texture are for
category and grouping, not for quantities the reader must compare precisely.

## Shape → form

| Material shape | Default form | Use instead when |
|---|---|---|
| comparison across categories | horizontal bar, sorted by value | many categories (>12) → dot plot or table |
| trend over time | line | few points (<5) → bar; many series (>5) → small multiples |
| part-to-whole | stacked bar, or bar of the parts | ≤4 parts and precision not required → pie is allowed |
| part-to-whole over time | stacked area | parts matter individually → small multiples |
| distribution | histogram | comparing distributions → box plot, violin, or ridgeline |
| relationship / correlation | scatter | 3rd variable → size or colour; many points → binned heatmap |
| flow / sequence / process | flow diagram, left→right or top→bottom | quantities flow → Sankey |
| hierarchy / nesting | tree, indented list | leaf size matters → treemap |
| ranking | ordered bar, or slope chart for rank change | — |
| geographic | choropleth for rates, symbols for counts | area distorts → cartogram or plain bar |
| single value | one large figure with its context | trend matters → figure + sparkline |
| narrative / concept | diagram — boxes, arrows, zones | — |

**Sort by value, not alphabetically,** unless the category order is
meaningful (time, size buckets, an agreed sequence). Alphabetical order
destroys the pattern the reader came for.

**Horizontal bars over vertical** when labels are words. Labels stay
readable; no rotated text.

## Pies

Allowed only when **all three** hold:

1. part-to-whole, and the whole is meaningful
2. four slices or fewer
3. the reader does not need to compare slices precisely

Otherwise a bar. Never two pies side by side for comparison — angle
comparison across separate origins is close to the bottom of the accuracy
ranking.

Never a donut with a figure in the middle standing in for a single value —
that's a number wearing a costume. Use the number.

## Honesty — hard rules

These are not preferences. Violating them misrepresents the data.

- **Length encodings start at zero.** Bars, columns, areas. A truncated
  baseline multiplies apparent differences. No exceptions.
- **Line charts may truncate** — they encode slope and change, not magnitude
  — but the axis must be labelled clearly and the range chosen honestly.
- **Area scales by area, not radius.** Doubling a circle's radius quadruples
  its area and quadruples the apparent value.
- **No 3D on 2D data.** Perspective distorts every quantity in the chart.
- **No dual axes** unless the two series share a unit or the relationship is
  stated explicitly. Dual axes let you manufacture any correlation you want
  by choosing the scales.
- **Aspect ratio must not manufacture a slope.** Stretching a time axis
  flattens change; compressing it invents drama.
- **Consistent intervals.** Uneven time steps drawn evenly spaced is a lie
  about rate.
- **Show the denominator.** A count without its base, or a percentage
  without its n, is not interpretable.
- **Don't hide inconvenient data.** Excluded outliers, clipped ranges, and
  filtered rows get stated on the artifact, not in a footnote nobody reads.

*Tufte's lie factor:* size of the effect shown ÷ size of the effect in the
data. Target 1.0.

## Encoding requirements → the system

State what you need; the system supplies the values.

- *"needs 5 distinguishable categorical slots"*
- *"needs a sequential ramp, low→high, 4 steps"*
- *"needs a diverging ramp with a meaningful midpoint at zero"*
- *"needs one emphasis treatment against a neutral field"*

If the system can't meet it, the fix is usually a **different visual
variable** — group down, encode by position or shape, or use small multiples
— not a bigger palette. Offer that first at the plan gate.

## Consistency across an artifact

Within one deck, dashboard, or document: **the same variable always encodes
the same way.** If revenue is blue on slide 3, it is blue on slide 9. If
stores are ordered J1 → Upside → Holiday Inn once, they are ordered that way
everywhere.

Inconsistent encoding across panels forces the reader to re-learn the chart
each time, and quietly destroys any comparison between them.
