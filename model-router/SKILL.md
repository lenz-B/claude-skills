---
name: model-router
description: Recommends which Claude model tier and version to use for a task (Haiku/Sonnet/Opus/Fable, and which generation within each), and flags when a session's context is getting full enough that you should /compact or start a fresh chat. Use this whenever the user asks "which model should I use", "is this worth Opus", "should I use Sonnet or Opus for this", pastes a task and wants a model recommendation, mentions wanting to save on usage/costs/tokens, or asks whether to compact, /clear, or start a new chat. Also use proactively at the start of a substantial new task to suggest the right tier before work begins, and mid-session when context usage is climbing (visible in the statusline, /context, or a long chat with many large pastes) even if the user hasn't asked. Do NOT use this for actually performing the task itself, for general "which AI company/product should I use" comparisons, or for routine single-line questions where the current model is obviously fine.
---

Claude is shipped in tiers (Haiku, Sonnet, Opus, Fable) and each tier has generations (e.g. Opus 5, Opus 4.8, Opus 4.7). Picking a tier is a cost/capability tradeoff; picking a generation is almost never a tradeoff — newer is generally better at the same or lower price, so default to the newest generation available and only pin an older one deliberately. This skill covers both decisions, plus the separate question of when a session itself has run long enough that continuing to work in it is costing more than it's worth.

## Decision router

| Question | Go to |
|---|---|
| Recommending a model/effort for a task | [Step 1: classify the task](#step-1-classify-the-task) → [Step 2: pick a tier](#step-2-pick-a-tier) |
| Picking a specific generation within a tier | [Step 3: pick the generation](#step-3-pick-the-generation) |
| Tuning effort/thinking instead of (or in addition to) switching models | [Step 4: effort is a second lever](#step-4-effort-is-a-second-lever) |
| Session running long, asking about /compact or a new chat | [Context hygiene](#context-hygiene) |

## Step 1: Classify the task

Read the actual prompt, not just its topic. Score it on three independent axes — a task can be low on one and high on another (e.g. "rename this variable across 40 files" is mechanical *and* wide-scope):

- **Reasoning depth.** Lookup, formatting, extraction, classification, boilerplate ("mechanical") vs. weighing tradeoffs, diagnosing an ambiguous bug, designing an architecture, writing something that needs to persuade or hold up under scrutiny ("judgment").
- **Blast radius.** Cosmetic or easily-reverted (a draft, a local script, a UI tweak) vs. hard to reverse or high-stakes if wrong (a database migration, security code, financial/legal text, anything going to production or to a real audience).
- **Horizon.** A single exchange or short back-and-forth vs. a long autonomous run — many tool calls, many steps, expected to keep making sound decisions for a long stretch without a human checking each one (an overnight batch job, a large multi-phase agent workflow).

## Step 2: Pick a tier

Default to the cheaper tier that can plausibly do the job well; escalate only when the classification in Step 1 actually calls for it. Downgrading a routine task saves money every single time it doesn't need the bigger model — upgrading a task that needed it once saves you a redo. That asymmetry is why the default should lean cheap.

| Tier | Use for | Why |
|---|---|---|
| **Haiku** | Mechanical/lookup work: formatting, extraction, classification, short factual Q&A, high-volume repetitive subagent fan-out (e.g. "check if file X exists" across 50 files) | Near-frontier intelligence at roughly a fifth of Opus's per-token cost. Wasted on anything needing real judgment, but wastes money when used for tasks *below* its ceiling too — i.e. don't reach for Sonnet on a task Haiku already handles fine. |
| **Sonnet** | The default for real work — feature implementation, most debugging, refactors, everyday writing and analysis. This is where the majority of tasks should land. | The best speed/intelligence combination Anthropic ships, and currently the cheapest way to get frontier-adjacent coding quality. **Note:** Claude Sonnet 5 has introductory pricing ($2/$10 per MTok in/out) through 2026-08-31, undercutting even the prior Sonnet generation — an extra reason to lean here while it holds. If you're reading this after that date, assume standard Sonnet pricing ($3/$15) applies unless you've checked. |
| **Opus** | Escalate here when a task in Step 1 actually scored high on reasoning depth or blast radius within a *single sitting*: nontrivial architecture or design decisions, multi-file refactors with subtle invariants, a bug Sonnet already got wrong twice, anything hard-to-reverse or high-stakes (security-sensitive code, data migrations, production changes). | Meaningfully stronger reasoning than Sonnet at roughly double the price. Worth it exactly when being wrong is expensive — not as a default "just in case" tier. |
| **Fable** | Reserve for long-running autonomous agent work — a task expected to run many steps *unsupervised* where sustained coherence over a long horizon matters as much as peak reasoning on any single step (a large multi-phase Workflow, an overnight fix-everything batch run). Not simply "the hardest single question you have." | Positioned by Anthropic as "next-generation intelligence for long-running agents," with always-on adaptive thinking. Costs roughly double Opus and five times Sonnet per input token — the most expensive tier by a wide margin, so use it deliberately, not as a reflexive "give me the best one." |

If a task doesn't clearly need Opus or Fable, it doesn't — the failure mode to guard against is defaulting up "to be safe," which is exactly the pattern that runs usage budgets dry without a proportional quality gain. A good gut check: could Sonnet make one honest attempt at this and would a knowledgeable person be satisfied with the result? If yes, start there — you can always escalate the one time it stumbles, which costs far less than defaulting to Opus/Fable on the other twenty tasks that didn't need it.

## Step 3: Pick the generation

Once you know the tier, pick the newest generation available in it, unless there's a specific reason not to (reproducing a past result, an eval that needs a frozen model, a documented regression in the newest snapshot). Don't hardcode a specific version number as the "right" answer — the lineup changes every few months, and whatever list you're working from may already be stale.

Instead, check what's actually current:
- **Claude Code:** run `/model` — it lists every selectable model live, including generation and any context-window variants (e.g. a `[1m]` suffix for the 1M-token window). This is ground truth; trust it over anything memorized.
- **Claude.ai (chat/desktop):** the model picker in the composer shows the current lineup the same way.
- **API/build integrations:** the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) page or the Models API (`GET /v1/models`) is authoritative for IDs, context windows, and pricing.

As of this skill's last check (2026-07-27), the current generation is the "5" family (Fable 5, Opus 5, Sonnet 5) plus Haiku 4.5 — all with 1M-token context except Haiku 4.5 (200k). If `/model` or the model picker shows something newer than that, trust what you see, not this note.

## Step 4: Effort is a second lever

In Claude Code and the API, reasoning effort (`low`/`medium`/`high`/`xhigh`/`max`) is a separate dial from model choice — don't reach for a bigger model when turning this down would do, and don't leave it maxed out by habit. Opus 5 and Sonnet 5 already default to `high` effort in Claude Code and the API (Opus 4.8 defaults to `high` everywhere, including claude.ai) — that default is usually the sweet spot. Pushing to `xhigh` or `max` multiplies thinking-token spend for typically a small quality gain, so reserve it for the same genuinely-hard cases that would justify Opus/Fable in the first place. Conversely, drop to `low`/`medium` for mechanical work even on a capable model — you don't need deep deliberation to rename a variable.

This lever doesn't exist in Claude.ai's chat UI (no per-message effort control there) — in chat, model tier is the only dial available.

## Context hygiene

This is a distinct problem from model choice: a session that has been running a long time accumulates context, and a bloated context costs more per turn (everything gets re-sent) and degrades quality (the model has more to track and can lose earlier details) regardless of which model you're on. "88% of usage at >150k context" is a symptom of long sessions, not of picking the wrong model — the fix is managing session length, not switching tiers.

**In Claude Code**, this is directly measurable — don't guess:
- A statusline showing `context_window.used_percentage` (and ideally `rate_limits.five_hour.used_percentage`) is the fastest way to see this at a glance without asking. If the user doesn't have one, `/context` shows a live breakdown, and `/cost` shows session token/dollar totals.
- **Under ~50% used:** no action needed.
- **~50–75% used:** fine to continue, but if you're about to start a substantial new subtask, suggest `/compact` first so the new work gets full headroom instead of inheriting a half-full window.
- **Above ~75–80%, or `exceeds_200k_tokens: true` on a 200k-window model:** flag it. If the current thread of work still has meaningfully more to do, recommend `/compact`. If the current task is basically finished and the next ask is a new topic, recommend `/clear` instead — compaction lossily summarizes everything so far, which is worth it mid-task but pointless (and slower/costlier than a clean start) once the task is over.
- **Rate-limit percentage (5h/7d) climbing fast while context is still low:** that's a *budget* signal, not a context signal — it means the model tier or effort level is too high for the volume of work, not that the session needs compacting. Route back to Step 2/4.

**In Claude.ai (chat/desktop)**, there's no visible percentage — advise by heuristic instead. Suggest a fresh chat when several of these stack up: the conversation has had multiple large pastes (long documents, big code blocks, screenshots), the thread is many dozens of messages deep, the user is pivoting to an unrelated topic, or — the clearest tell — Claude starts re-asking or contradicting something already established earlier in the chat, which is a classic symptom of context pressure crowding out earlier detail. When several of these are present, say so plainly and suggest starting a new chat with a short recap of what matters, rather than letting quality degrade silently.

**Don't nag.** Mention context/compaction once when a threshold is genuinely crossed, not on every message — the goal is to catch the moment before quality degrades or cost balloons, not to interrupt a working session repeatedly.

## Worked example

> "Add a discount-code field to checkout, validate it against our promo table, and show the adjusted total."

- Reasoning depth: moderate — some judgment (validation edge cases, how to show the adjustment) but not an architecture decision.
- Blast radius: touches checkout, which affects real transactions — not purely cosmetic, but a well-scoped, reviewable change, not a schema migration.
- Horizon: a normal single-session implementation task, not a long unsupervised run.

→ **Sonnet** (current generation), default effort. Escalate to Opus only if the promo-table validation turns out to hinge on a subtle existing bug, or if this checkout path has a history of costly mistakes.
