# Medium — print

Anything physical: poster, flyer, handout, one-pager, notice on a wall.

**Chosen when:** it ends up on paper. Physical output has hard constraints
nothing on screen has — fixed size, fixed viewing distance, no zoom, no
scroll, no interaction, and one shot at being understood.

## Size and distance first

These two decide everything else. Establish both before designing.

| Piece | Size | Read at |
|---|---|---|
| wall poster | A2 / A1 | 2–3 m |
| notice, staff-area sign | A3 | 1–2 m |
| flyer, handout | A5 / A4 | 30–40 cm |
| one-pager, report page | A4 | 30–40 cm |

Scale floors follow from distance — `composition.md` § Scale floors. **A
poster read at 3 m needs a headline ≥ 100 pt.** This is the constraint people
get wrong most often, and it fails silently: it looks fine on the monitor and
is unreadable on the wall.

## Build

- Author in HTML/CSS, export to PDF. Set the page size explicitly:
  ```css
  @page { size: A3; margin: 0; }
  ```
  and set the body to exact physical dimensions in `mm`.
- **Work in mm and pt, not px.** Pixels have no meaning on paper.
- Bleed 3 mm on every edge if anything runs to the edge; keep all essential
  content ≥ 10 mm inside the trim.
- Fonts embedded in the PDF. Not referenced.
- Images ≥ 300 dpi at final print size. A 1000 px image printed at A3 width
  is roughly 85 dpi — visibly soft.
- Prefer vector for everything that can be vector.

## Composition

- **One message.** A poster is read in about three seconds by someone
  walking past. If it needs two messages, it's two posters.
- Strict hierarchy — headline, one supporting element, minimal detail.
  Three levels, hard steps between them (`composition.md`).
- Z-pattern for sparse layouts; put the takeaway or action at bottom-right
  (`perception.md`).
- Generous margins. Print tolerates far less density than screen — there's no
  scroll to relieve pressure, so crowding has nowhere to go.
- Fewer, larger elements. The instinct to shrink type to fit more is exactly
  backwards: cut content instead.
- **Assume greyscale.** Office printing is monochrome more often than not.
  Colour must never be the only carrier of meaning — this matters more here
  than anywhere else.

## Verify

- [ ] PDF page size is exactly right — no scaling on open
- [ ] Fonts embedded (check the PDF's font list, don't assume)
- [ ] Nothing essential inside 10 mm of the trim edge
- [ ] Headline clears the floor for the stated viewing distance
- [ ] Body text ≥ 12 pt; captions ≥ 9 pt
- [ ] Print one page at actual size and look at it from the real distance —
      or simulate it: view at 100 % zoom and step back
- [ ] Photocopy test — still fully readable in pure greyscale
- [ ] Images ≥ 300 dpi at final size
- [ ] Numbers match the source — spot-check at least two
