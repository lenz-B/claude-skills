---
name: deep-research
description: "Deep multi-platform research with optional reverse engineering and playbook creation. Use this skill whenever the user wants to research any topic deeply — what works, what doesn't, why, and how to replicate it. Triggers include: 'research', 'find out what works', 'what's working in', 'reverse engineer', 'create a playbook', 'analyze this niche', 'find opportunities', 'what are the best examples of', 'break down why this works', 'how do the best people do X', 'look into X for me', 'I want to understand X', 'compare X vs Y', 'case study', 'update my research', or any request to investigate a topic across multiple sources and extract actionable patterns. Also trigger when the user asks to study a format, style, strategy, niche, market, or approach and wants to understand what separates winners from losers. Do NOT use for writing LinkedIn posts (use write-linkedin-post), creating SOPs (use sop-creator), one-off factual questions that need a single web search, or general conversation."
---

# Deep Research Engine

## Overview

Research that produces validated, actionable findings — not summaries of the first page of Google. Uses triangulation, structured source evaluation, strategic search, and pattern extraction adapted from formal research methodology for practical use.

## Mode Router

| User Says | Mode | Reference to Read |
|-----------|------|-------------------|
| "Research X" / "Look into X" | **Research** | `references/source-evaluation.md` + `references/search-strategies.md` |
| + "Reverse engineer" / "Break down why" | **+ Reverse Engineer** | Above + `references/reverse-engineering.md` |
| + "Playbook" / "Framework" / "Something I can use" | **+ Playbook** | Above + `references/playbook-creation.md` |
| "Compare X vs Y" / "X or Y" | **Comparison** | `references/research-modes.md` (Comparison section) |
| "Find opportunities in X" / "Any gaps in X" | **Opportunity Scanner** | `references/research-modes.md` (Opportunity Scanner section) |
| "Study how [company] did X" / "Case study" | **Case Study Analysis** | `references/research-modes.md` (Case Study Analysis section) |
| "Update my research on X" | **Research Update** | `references/research-modes.md` (Update Mode section) |

Default = Research only. Mention reverse engineering or playbook if strong replicable patterns emerge, but don't add them unless asked.

## Depth Levels

User specifies per request. If they don't, ask once at the start.

| Level | Sources | Validation | When to Use |
|-------|---------|------------|-------------|
| **Quick scan** | 3-5 | Light pattern check | "Just give me a feel for this" |
| **Standard** | 8-12 | Triangulated across 2-3 source types | Most research tasks |
| **Deep dive** | 15+ | Full triangulation + counter-evidence | High-stakes, need to really understand |

## Core Research Flow (all modes use this)

### Step 1: Frame
Before searching, state in 2-3 lines:
1. **The question** — one sentence, specific. Not "research hooks" but "What hook structures consistently drive high engagement on LinkedIn, and why?"
2. **What done looks like** — what would a complete answer contain?
3. **Source map** — where does the best info for THIS topic live? (Read `references/search-strategies.md` for platform mapping)

### Step 2: Evaluate Sources
Read `references/source-evaluation.md` for the two-layer evaluation framework (Quick SIFT + Deep Evaluation). Run every source through this before trusting it.

### Step 3: Search
Read `references/search-strategies.md` for the seed-and-map method, search angle templates, and platform-specific strategies. Use at least 3 search angles per task.

For each promising web_search result, use web_fetch for full content. Snippets are never enough.

### Step 4: Triangulate
Nothing is a finding until confirmed by 2+ independent source types (practitioners, observable data, community consensus, analytical breakdowns, counter-evidence absence).

| Status | Criteria | Label |
|--------|----------|-------|
| **Validated** | 3+ source types | "Strong evidence" |
| **Likely** | 2 source types | "Moderate evidence" |
| **Possible** | 1 source type, uncontradicted | "Limited evidence" |
| **Contested** | Sources disagree | "Conflicting evidence" |
| **Anecdote** | Single example | Do NOT call it a pattern |

When sources contradict, dig into WHY. Contradictions often contain the best insights.

### Step 5: Output
Save as markdown to `/mnt/user-data/outputs/research-[topic-slug]-[YYYY-MM-DD].md`. In chat, give a brief summary and present the file.

Read `references/output-templates.md` for the exact output structure for each mode.

## Confidence Decay

All research findings have a shelf life. When presenting findings, tag them:
- **Fresh** — less than 3 months old for fast-moving topics (social, tech, markets)
- **Current** — less than 12 months old
- **Aging** — 12-18 months old, may need re-validation
- **Stale** — 18+ months for fast-moving topics — flag prominently, recommend update

When running an Update (see `references/research-modes.md`), re-check aging/stale findings first.

## Skill Integration

This skill's output feeds directly into other skills when the user asks:
- Research → Reverse Engineer → Playbook → **write-linkedin-post** (use the playbook to write)
- Research → **sop-creator** (turn research process into a repeatable SOP)
- Research → **comment-writer** (use research insights to write better comments)

When the user chains skills, carry context forward. Don't make them repeat what was already found.

## Global Rules

- **Triangulate or flag.** No finding is "validated" without 2+ independent source types.
- **Always hunt counter-evidence.** At least one search angle per task dedicated to opposing views and failures.
- **Don't pad.** 3 strong findings > 7 padded ones. Thin research labeled honestly beats thick research that fakes confidence.
- **One example ≠ a pattern.** Minimum 3 examples before calling it a pattern.
- **Follow citation trails.** Trace claims to original sources. Secondary sources distort.
- **Separate observation from interpretation.** Label which is which.
- **Name your confidence.** Every finding gets an evidence-level tag.
- **Apply anti-ai-writing.** Output reads like a sharp analyst, not AI summarizing articles.
- **Save everything as markdown.** File goes to `/mnt/user-data/outputs/`. Brief summary in chat + present the file.

## Reference Files

- `references/source-evaluation.md` — SIFT + CRAAP evaluation framework, automatic disqualifiers, source hierarchy. Read when evaluating any source.
- `references/search-strategies.md` — Seed-and-map method, search angles, platform-specific strategies by topic type. Read when planning searches.
- `references/reverse-engineering.md` — Specimen selection, anomaly detection, mechanics breakdown (psychology → structure → context), failure mode analysis. Read when reverse engineering.
- `references/playbook-creation.md` — Framework building, variation creation, quality checklists. Read when creating playbooks.
- `references/research-modes.md` — Comparison mode, opportunity scanner, case study analysis, research update mode. Read when using any non-default mode.
- `references/output-templates.md` — Exact markdown templates for every output type. Read when compiling the final output file.
