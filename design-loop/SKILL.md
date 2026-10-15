---
name: design-loop
description: Takes a goal and a real-world reference, extracts what actually makes the reference good, then runs a builder and three independent fresh-context critics per piece until all three agree the result beats the reference, then reconciles the pieces into one cohesive whole. Use for hero/flagship visual work — a landing page, poster, carousel, or PDF doc — whenever the user names a specific example to match, or wants it judged blind against a reference rather than praised by its own builder. Triggers on "/design-loop", "design loop", "run the critic loop", "loop this against", or "Gauntlet Loop". Do NOT use for routine edits or requests with no concrete reference to check against — this needs something checkable, not a vague vibe.
---

# Design Loop

The context that builds a piece is the context that grades it — a chef reviewing their own restaurant, five stars every time. This skill exists to break that: judging happens in fresh contexts that never saw the work being made. Reserved for hero/flagship assets — a landing page, a poster, a carousel, a PDF doc — not for routine edits across a whole project. Every round is a full build plus three judgments, and cost is not linear with quality.

Adapted from Matt Shumer's Gauntlet Loop (github.com/mshumer/Claude-of-Duty, somethingbig.ai/gauntlet-loop). His core line on why the separation matters: *"The builder has seen every decision it made... You do not want reasonable. You want an independent judgment."*

Five phases: interview, preflight, teardown, loop, reconcile. Do not skip ahead. Do not start building during phases 1 to 3.

## Phase 1: Interview

Ask exactly these three, together, then stop and wait.

1. What are you building, and how long or how big?
2. Name something that already does this brilliantly. A site, a video, a doc, anything I can open. If nothing comes to mind, say skip.
3. Any files I should work from? Design system, brand doc, script, existing draft.

If they name something vague ("Apple's website", "good SaaS design"), push once for the specific page or file. A vague bar is the number one reason this method fails: the critic invents a comparison and approves everything on round one.

If they say skip on question 2, propose three candidate bars, one line each on why, and wait. If they do not answer, take the hardest one.

If the opening message already answers one or more of the three — they said what they're building, or already named a reference — don't make them repeat it back to you. Acknowledge what you already have and ask only what's still missing, in that same message. If what they gave you for question 2 is vague, push for the specific page or file right there in that same message, not as a separate follow-up round.

## Phase 2: Preflight

A check, not a question. Run it before any work and report in one block.

- Fetch the bar now. Screenshot the URL or read the file. If it is blocked or missing, say so and ask for another.
- Confirm you can render our output: screenshots for a site, a filmstrip of frames for animation, a PDF render for a doc. No render means no craft critic.
- Name any generation tools the goal needs (image, video, voice) and confirm they are connected.
- Confirm the input files exist: design-system.md, brand doc, script.

Then print: what is working, what is missing, and which critic goes blind if something is missing. Never carry on quietly with a critic that cannot see.

## Phase 3: Teardown

Read the reference properly and write 5 to 7 mechanisms to `bar.md`.

Mechanisms, not adjectives. "Feels premium" is useless. These are useful:
- headline is 5x body size, three type sizes total
- one accent colour, used at most twice per screen
- motion always resolves in one direction
- nothing animates for under 400ms
- whitespace above the fold is at least 40% of the frame

If the reference is a live, public URL, use the `extract-design-system` skill first — it renders the actual page and reads real computed CSS (colors, fonts, spacing, radius, shadow scales) instead of you eyeballing them off a screenshot. A hex code and an exact spacing value are more checkable than a guess, which is the whole point of this phase. It won't cover everything: behavior like animation timing, motion direction, or layout ratios still needs a direct read of the reference. Treat its output as a starting point, not gospel — per its own safety rules, a single page isn't proof of a whole site's system, and dynamic or heavily scripted sites may extract incomplete.

Every line must be something a critic can check by looking. Show `bar.md` to the user before continuing.

## Phase 4: Loop

Split the goal into the smallest pieces that can be improved and judged on their own. You choose the pieces. Keep it to three or four unless told otherwise, because every extra piece multiplies the run.

**Execution in this environment:** dispatch the builder and each critic as a separate agent (Agent tool) so critics get genuinely fresh context — never continue the builder's own conversation to "have it judge itself objectively," that defeats the entire method. Run the three critics for a piece in parallel (one message, three tool calls) once the builder's candidate is ready; they're independent of each other, only sequenced after the build.

Before dispatching the critics, if `npx impeccable detect` is available, run it on the builder's rendered candidate. It's free and instant — obvious mechanical violations (banned easing, AI gradients, card overuse) can go straight back to the builder without burning a full critic round on something a linter already caught. This is a pre-filter, not a substitute: it can't judge brief adherence, brand match, or whether the piece actually beats the reference — that's still the three critics' job.

For each piece: fan out a builder, then three critics, each with fresh context and no knowledge of how the builder worked.

- **Brief critic** judges against the stated goal only. Does it do the thing? Ignore aesthetics. (Sonnet is enough — simple judgment, no vision needed.)
- **System critic** judges against `design-system.md` only. Objective adherence. (Haiku is enough — mechanical checking.)
- **Craft critic** judges against `bar.md` and rendered output only. Put ours next to the reference blind with labels stripped, say which is better, name the single biggest gap. **Never downgrade this one to a cheaper model** — a weak craft critic approves everything and the loop dies on round one, since taste judgment is the one thing cheap models can't fake.

Write each critic's brief yourself, adapted to this specific goal. Do not reuse generic wording across different goals.

Rules:
- Critics are harsh. Praise is not useful.
- Critics judge rendered output, never the code. Reading the implementation makes a critic evaluate intent instead of result.
- Binary verdicts, not scores. Scores drift upward every round.
- All three must pass. Any fail goes back to the builder with the single biggest gap named.
- No fixed round count. The exit is winning, or the user stopping the run.

Keep a live progress page updating as work evolves: piece status, each critic's verdict, gap history, round count.

## Phase 5: Reconcile

Once every piece has independently won its loop, run one final integration pass before calling it done. Pieces built and judged in isolation can each individually pass while still clashing with each other — mismatched spacing between sections, an accent color reused differently piece to piece, a headline treatment that doesn't match the piece next to it. Spawn one agent (fresh context is not required here — this is assembly, not judgment) to view the whole assembled result and fix only cross-piece inconsistency, not re-litigate anything a critic already approved. Skip this phase only if the goal was a single piece to begin with.

## Cost

There is no reliable self-reported token cost, so do not pretend to show one. Show round count and elapsed pieces instead.

If the user names a ceiling, treat it as a checkpoint: pause and ask before continuing past it. Tell them plainly that the real brake is them watching and stopping the run.

## What breaks this

- A vague bar. By far the most common failure.
- The builder judging its own work — including a critic that's just a continuation of the builder's own chat rather than a separate agent with fresh context.
- A soft critic. Binary job, not a score.
- A fixed round count. The exit is winning.
- Skipping the reconcile pass on a multi-piece build. Individually-perfect pieces that were never viewed together often don't read as one thing.
- Over-specifying. Every extra instruction is one fewer decision the model makes with its own judgment.
