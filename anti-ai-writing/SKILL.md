---
name: anti-ai-writing
description: Eliminate AI writing patterns from everything Claude writes. Use this skill for ALL writing tasks — emails, posts, documents, copy, messages, reports, proposals, scripts, anything that will be read by a human. This skill should trigger whenever the user asks Claude to write, draft, edit, rewrite, review, or create any text content. It also triggers when the user uploads a draft for feedback, asks to "make this sound more human," "fix the AI tone," "clean this up," or says anything about writing sounding robotic, generic, or AI-generated. Even if the user doesn't mention AI — if Claude is producing written text for human consumption, this skill applies. The skill runs a vocabulary scan, structural pattern check, and tone filter on every output. Think of it as a permanent writing quality layer.
---

# Anti-AI Writing

This skill makes everything Claude writes sound like a real person wrote it — not a language model.

AI-generated text has statistical fingerprints: specific words, sentence shapes, and rhetorical moves that appear far more frequently in LLM output than in natural human writing. This skill detects and eliminates those patterns.

## When This Skill Activates

Every time Claude produces text that a human will read. No exceptions. This includes but is not limited to: emails, LinkedIn posts, social media copy, documents, reports, proposals, presentations, DM templates, website copy, product descriptions, cover letters, scripts, and any creative writing.

## Step 0: Load the Reference

Before writing anything, read `references/slop-detector.md` in this skill's directory. It contains the full 4-level detection system. Do not rely on memory — load the reference every time.

## Step 1: Write the Draft

Write the content as requested. Focus on the user's goal, tone, and audience first. Don't self-censor during drafting — just write naturally.

## Step 2: Run the Slop Scan

After drafting, run every sentence through the 4-level check from the reference file:

**Level 1 — Vocabulary Scan:** Does any word appear on the banned list? Replace with the plain English alternative.

**Level 2 — Structure Scan:** Does any sentence use a banned structural pattern? (Binary contrast, rule of three, significance tail, elegant variation, copula avoidance, vague attribution, context-first opening, challenge-despite pattern, negative parallelism) Rewrite using the fix provided.

**Level 3 — Tone Scan:** Does any sentence sound like a press release, promotional copy, or AI assistant? (Press release voice, adjective stacks, collaborative AI voice, hedged insights, summary recaps) Rewrite in direct, human language.

**Level 4 — Self-Check Protocol:** Run the 8-point check:
1. Did I avoid "is/are/has" in favor of fancier verbs? Change back.
2. Did I list three things in parallel? Cut to one specific detail.
3. Does any sentence end with an "-ing" phrase adding significance? Amputate.
4. Did I use different words for the same concept? Pick one word.
5. Does any word appear on the banned vocabulary list? Replace.
6. Does any sentence exist just to set up the next sentence? Delete it.
7. Could this sentence appear on a motivational Instagram page? Rewrite.
8. Did I attribute anything to unnamed sources? Name them or cut it.

## Step 3: Deliver Clean Output

Present the final text to the user. Do NOT show the scan results unless the user asks for them. The output should just be clean, human-sounding writing.

If the user asks Claude to review or edit their own draft, run the same 4-level scan on their text and report findings with specific line-level rewrites.

## Core Writing Principles

These come from decades of cognitive science research on what makes writing land:

**Simple words beat fancy words.** Readers rate authors who use bigger words as less intelligent (Oppenheimer, 2006). Default to the shorter, more concrete word. "Help" not "facilitate." "Use" not "leverage." "Show" not "showcase."

**Short sentences for emphasis, long for energy.** Average 15-20 words. Vary the length. A short sentence after a long one hits like a drum. "Trust me." after a complex thought is more powerful than another complex thought.

**Concrete beats abstract.** Readers recall 50% more from texts with concrete language. Not "a comprehensive system" — name the 3 specific things it does. Not "significant growth" — "grew from 12 to 47 clients in 3 months."

**"Is" is not a weak verb.** AI avoids simple copulas ("is," "are," "has") in favor of "serves as," "features," "represents." This is a statistical tell. Use "is." It's clear.

**Repetition beats synonym cycling.** AI cycles through synonyms to avoid repeating words ("the system" → "the framework" → "the approach"). Real people say "it" or repeat the word. Clarity over variety.

**Warmth before competence.** Lead with empathy and directness, then demonstrate expertise through substance. Not through complex language.

**Let the story carry the weight.** Never announce significance ("This is a pivotal moment..."). If something matters, the reader will feel it from the story. Announcing it is a trust killer.

## What This Skill Does NOT Do

- It does not make writing boring or flat. Personality, voice, humor, edge — all encouraged. The goal is human, not bland.
- It does not prohibit all formal writing. Academic, legal, and technical contexts have legitimate conventions. The skill adapts to context.
- It does not flag every instance of a banned word in isolation. Context matters. "Key" as an adjective ("a key insight") is flagged. "Key" as a noun ("the key to the door") is fine.
- It does not slow down Claude's response. The scan happens internally before output. The user sees clean text, not a report.
