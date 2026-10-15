# Medium — deck

Paged content presented in sequence to an audience.

**Chosen when:** someone talks over it, or it advances one screen at a time
toward a conclusion.

**Not chosen when:** it's meant to be read alone at a desk — that's a
document. A deck built to be read alone becomes a dense document that works
as neither. If it will be sent rather than presented, say so and build a
document instead.

## Sequence first

The order *is* the argument. Decide it before designing a single slide.

- **One idea per slide.** If a slide needs two headlines, it's two slides.
- Write the headline of every slide first, in order, as sentences. Read them
  in sequence — that list alone should make the argument. If it doesn't, the
  structure is wrong and no amount of design will rescue it.
- **Headlines state the finding, not the topic.** "Upside runs 40 % below the
  other two stores" — not "Store Performance". A topic label makes the
  audience do the work, and they will do it wrong or not at all.
- Standard spine: situation → complication → evidence → implication → ask.
  Deviate deliberately, not by accident.

## Build

- Fixed canvas, 1920 × 1080 (16:9). Design at that exact size; scale to the
  viewport at display time. Never hand-roll scaling ad hoc — set the stage
  once and let every slide inherit it.
- One HTML file with each slide as a section, keyboard navigation (arrows,
  space), and slide numbers. Self-contained, inline everything.
- **Body text ≥ 24 px at 1920 × 1080. Ideally larger.** Assume the back row
  and a bad projector.
- Same grid, same margins, same header position on every slide. Inconsistent
  slide-to-slide placement makes elements appear to jump during transitions,
  which reads as sloppiness even to people who can't name it.

## Composition

- **Radically less content than a document.** A slide is glanced at while
  someone listens. Text competing with the speaker means neither is received.
- No bullet lists of full sentences. Either a short phrase or a visual.
- One chart per slide, large. A four-chart grid on a projected slide is four
  charts nobody can read.
- Same encoding for the same variable across the entire deck — colours,
  order, axis ranges (`composition.md` § Multi-visual coherence). The
  audience learns the visual language once; changing it mid-deck resets them.
- Annotate the finding directly on the chart. The audience has seconds, and
  half of them are looking at their phone when you say it out loud.
- Detail belongs in an appendix after the closing slide, not crammed into the
  body.

## Verify

- [ ] Every slide fits its canvas — nothing clipped, nothing overflowing
- [ ] Scales correctly on a small viewport; navigation stays reachable
- [ ] Keyboard navigation works both directions; slide numbers present
- [ ] All body text ≥ 24 px
- [ ] Headlines read in sequence make the argument on their own
- [ ] Header, margins, and grid identical across all slides
- [ ] Same variable encoded identically throughout
- [ ] Readable in greyscale, and from ~2 m off a 15" laptop screen
- [ ] Numbers match the source — spot-check at least two
