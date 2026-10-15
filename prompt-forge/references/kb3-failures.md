# KB3 — Prompt Optimization, Failure Patterns & Advanced Techniques

This document covers how to diagnose and fix weak prompts, the prompt scoring framework, and advanced techniques for maximum output control.

---

## PART 1: PROMPT FAILURE PATTERNS

### What is a "Prompt Bomb"?
A prompt bomb is any prompt that reliably produces generic, surface-level, or hallucinated output. It's not that the model "failed" — it's that the prompt didn't constrain the model enough to produce something useful.

### The 8 Most Common Failure Patterns

**FAILURE 1: The Naked Ask**
```
Tell me about content marketing.
```
Why it fails: No role, no context, no format, no constraints, no quality bar. The model has infinite freedom, so it defaults to the safest, most generic response.

Fixed version:
```
You are a B2B content marketing strategist who has built content engines for SaaS companies from 0 to 10K monthly organic visitors.

Produce a breakdown of the 5 highest-ROI content marketing tactics for a B2B SaaS company with a small team (2-3 people) and limited budget ($5K/month).

For each tactic:
- Why it works specifically for early-stage B2B SaaS
- Implementation steps (first 30 days)
- Expected timeline to results
- Resource requirements

Constraints:
- No generic advice like "create quality content" or "be consistent."
- Focus on tactics that compound over time.
- Exclude paid advertising and influencer marketing.

Quality bar: This should read like internal strategy notes from a growth agency, not a blog post about "content marketing tips."
```

---

**FAILURE 2: The Kitchen Sink**
```
I need you to research LinkedIn, create a content strategy, write 10 posts, analyze my competitors, build an outreach system, and give me tips for growing my following. Make it comprehensive.
```
Why it fails: 6 different tasks crammed into one prompt. The model will do all of them poorly instead of any of them well. Each task needs different role context, format, and constraints.

Fix: Split into 3-4 separate prompts, each with a single clear deliverable. Run sequentially, with each building on the previous output.

---

**FAILURE 3: The Vague Deliverable**
```
Give me some insights about email marketing.
```
Why it fails: "Some insights" could mean anything. The model doesn't know how many, what depth, what angle, or what format. It will give 5-7 bullet points of surface-level advice.

Fixed version:
```
You are an email marketing specialist who has managed campaigns for DTC e-commerce brands ($1M-$10M revenue).

Produce a breakdown of the 5 most impactful email marketing optimizations that most brands get wrong.

For each optimization:
- The common mistake
- Why it hurts performance (with approximate impact)
- The specific fix
- A before/after example

Constraints:
- Skip basics like "segment your list" and "write good subject lines."
- Focus on intermediate-to-advanced optimizations.
- Each must be implementable within one week.

Quality bar: An experienced email marketer should learn at least 2 new things from this.
```

---

**FAILURE 4: The False Constraint**
```
Be very detailed and thorough and comprehensive and make sure it's high quality and actionable and insightful.
```
Why it fails: These words add zero information. They're like telling a chef "make it taste good" — they already know that. The model ignores these because they don't define what "detailed" or "comprehensive" actually means for THIS task.

Fix: Replace with SPECIFIC constraints:
- Instead of "be detailed" → "Include specific metrics, timelines, and implementation steps"
- Instead of "be comprehensive" → "Cover these 5 specific dimensions: [list them]"
- Instead of "high quality" → "This should read like a McKinsey deliverable"
- Instead of "actionable" → "Every recommendation must include a specific first step someone can take tomorrow"

---

**FAILURE 5: The Missing Role**
```
How does LinkedIn's algorithm work? Give me a detailed breakdown.
```
Why it fails: Without a role, the model defaults to a general-purpose explainer. It doesn't know if you want technical mechanisms (engineer), growth tactics (marketer), content strategy (creator), or platform policy (LinkedIn employee perspective).

Fixed version with role (notice how the same question produces completely different outputs):
```
You are a social media growth engineer who reverse-engineers platform algorithms by analyzing distribution data across thousands of posts.

Break down how LinkedIn's content distribution algorithm works from a technical perspective...
```

---

**FAILURE 6: The Context Desert**
```
Create a marketing strategy for my business.
```
Why it fails: What business? What size? What industry? What budget? What's already been tried? What's the goal? Without context, the model can only give generic advice that applies to everyone and helps no one.

Fix: Always include situational context. Even 2-3 sentences dramatically improve output.

---

**FAILURE 7: The Format Vacuum**
```
Analyze these three marketing approaches and tell me which is best.
```
Why it fails: "Tell me which is best" could mean a one-word answer, a paragraph, or a 10-page report. The model will pick whatever is easiest — usually a few paragraphs with no clear structure.

Fix: Specify the format:
```
Analyze these three approaches using a comparison matrix:
- Rows: The 3 approaches
- Columns: Cost, time to implement, expected ROI, risk level, scalability
- Add a "Verdict" row with a clear recommendation and 2-sentence reasoning.
```

---

**FAILURE 8: The Hallucination Invitation**
```
Give me the exact statistics on LinkedIn engagement rates for each content format in 2024.
```
Why it fails: The model may not have exact current statistics. Without a safeguard, it will confidently generate plausible-sounding but potentially fabricated numbers.

Fix: Add an uncertainty safeguard:
```
...If specific statistics are not available or you're uncertain about exact numbers, provide directional insights (e.g., "significantly higher" or "roughly 2-3x") and flag where I should verify independently.
```

---

## PART 2: THE 4-STEP PROMPT OPTIMIZATION SYSTEM

When improving a weak prompt, apply these 4 steps in order:

### Step 1: CLARITY EXPANSION
**Goal:** Make the implicit explicit.

Method:
1. Read the prompt and ask: "If I gave this to 10 different experts, would they all produce the same type of output?" If no → clarify.
2. Identify every ambiguous word ("good," "detailed," "some," "effective," "insights") and replace with specifics.
3. Add a concrete deliverable statement: "The output should be [exact thing]."
4. Specify the audience: Who is this output FOR?

Before:
```
Give me tips for better LinkedIn engagement.
```

After clarity expansion:
```
Produce a list of 7 specific tactics to increase comment-to-impression ratio on LinkedIn text posts for B2B founders in the tech industry.
```

---

### Step 2: CONSTRAINT TIGHTENING
**Goal:** Eliminate the model's worst instincts.

Method:
1. Think about the most GENERIC, OBVIOUS response the model could give. Write a constraint to prevent it.
2. Think about the most LIKELY way the model could misinterpret the task. Write a constraint to prevent it.
3. Add at least one EXCLUSION constraint (what NOT to do).
4. Add at least one SPECIFICITY constraint (what level of detail).

Before:
```
...Produce a list of 7 tactics for LinkedIn engagement.
```

After constraint tightening:
```
...Produce a list of 7 tactics for LinkedIn engagement.

Constraints:
- Exclude generic advice like "post consistently," "engage with others," or "use hashtags."
- Every tactic must include a specific implementation example.
- Focus on tactics that work with fewer than 5,000 followers.
- No paid strategies.
```

---

### Step 3: OUTPUT STRUCTURING
**Goal:** Control the shape and usefulness of the response.

Method:
1. Define the output format explicitly (table, sections, numbered list, framework).
2. For each item/section, specify what it must contain.
3. If ordering matters, specify the ordering logic (by impact, by difficulty, chronologically).
4. Specify length bounds where relevant.

Before:
```
...7 tactics with constraints...
```

After output structuring:
```
...7 tactics. For each tactic, provide:
- Tactic name (5 words or fewer)
- How it works (2-3 sentences explaining the mechanism)
- Implementation example (a specific, real-world example of this tactic in action)
- Estimated impact: Low / Medium / High
- Difficulty: Easy / Medium / Hard

Order by impact (highest first).
```

---

### Step 4: QUALITY ELEVATION
**Goal:** Push the output from "fine" to "exceptional."

Method:
1. Add a role with specific expertise.
2. Add a quality bar with a concrete reference point.
3. Add a "differentiation" constraint — what should make this output DIFFERENT from what anyone else could produce.
4. Add a safeguard against the model's most common quality cop-out.

Before:
```
...7 tactics with format and constraints...
```

After quality elevation:
```
You are a LinkedIn growth strategist who has personally grown 3+ accounts from 0 to 50K followers using organic strategies only.

[task + format + constraints from previous steps]

Quality bar: These should be tactics a LinkedIn creator with 10K followers hasn't heard before. If it sounds like it could come from any "LinkedIn tips" thread, it's not good enough.

If you cannot identify 7 genuinely non-obvious tactics, provide fewer but higher quality. Do not pad with generic filler.
```

---

## PART 3: PROMPT SCORING FRAMEWORK

Score any prompt on these 8 dimensions, each on a 1-10 scale:

| Dimension | 1-3 (Weak) | 4-6 (Adequate) | 7-9 (Strong) | 10 (Elite) |
|---|---|---|---|---|
| **Role Precision** | No role or generic ("expert") | General domain role | Specific domain + experience | Domain + experience + perspective lens |
| **Context Richness** | No context | Basic situation mentioned | Situation + goals + constraints | Full picture: situation, goals, constraints, audience, history |
| **Outcome Clarity** | Vague ("help me with...") | General direction ("create a strategy") | Specific deliverable ("90-day plan with phases") | Deliverable + success criteria + measurability |
| **Format Control** | No format specified | Basic format ("use bullet points") | Structured format with sections | Detailed format with item-level specs |
| **Constraint Power** | No constraints | 1 generic constraint | 2-3 specific constraints | Multiple layered constraints targeting known failure modes |
| **Quality Calibration** | No quality bar | "Make it good" | Concrete quality reference | Quality reference + differentiation requirement |
| **Safeguard Presence** | None | Basic "if unclear, ask" | Uncertainty flagging | Uncertainty handling + assumption disclosure |
| **Length Calibration** | Way too short or too long | Reasonable but imperfect | Well-matched to task | Perfect match: every line earns its place |

**Scoring guide:**
- 10-30: Prompt bomb. Will produce generic garbage.
- 31-50: Functional but mediocre. Output will be "fine" but not impressive.
- 51-70: Solid prompt. Will produce good output with minor weaknesses.
- 71-80: Strong prompt. Will produce output that's ready to use with minimal editing.
- 81-90: Elite prompt. Will produce output that looks professionally crafted.
- 91-100: Master-class prompt. These are rare and represent prompt engineering at its peak.

---

## PART 4: ADVANCED TECHNIQUES

### Technique 1: Chain-of-Thought Steering (Without Overexposing Reasoning)

When you need the model to think deeply but present cleanly:

```
Think through this step-by-step internally, but present only your final conclusions in the following format: [format]. Do not show your working unless specifically asked.
```

For analytical tasks:
```
Before presenting your analysis, internally consider: [list of considerations]. Then present your final analysis structured as [format].
```

This gets the depth of chain-of-thought without the wall-of-text reasoning dump.

---

### Technique 2: Iterative Refinement Loops

Build prompts that self-improve:

```
[Main task instruction]

After completing your initial response, review it against these criteria:
1. [Criterion 1]
2. [Criterion 2]
3. [Criterion 3]

If any criterion scores below 8/10, revise that section before presenting the final version.

Present only the final, refined version.
```

---

### Technique 3: Self-Critique Prompting

Force the model to pressure-test its own output:

```
[Main task instruction]

After completing the output, add a section titled "Honest Assessment" where you:
1. Identify the weakest part of your response
2. Flag anything you're not fully confident about
3. Suggest one specific way this could be improved with additional context from me
```

---

### Technique 4: Adversarial Stress Testing

Test a prompt's robustness by adding:

```
[Main task instruction]

Stress test: After completing the task, identify the 3 most likely criticisms a domain expert would have with this output. Address each briefly.
```

Or for strategy/planning prompts:

```
[Main task instruction]

Pre-mortem: Before finalizing, assume this plan failed. What are the 3 most likely reasons it failed? Adjust your recommendations to address these failure modes.
```

---

### Technique 5: Prompt Compression

When a prompt is too long, compress without losing power:

**Before (verbose):**
```
I would like you to take on the role of someone who is an expert in the field of digital marketing, specifically someone who has extensive experience with search engine optimization and has worked with multiple large enterprise clients in the technology sector over the past decade.
```

**After (compressed):**
```
You are an enterprise SEO strategist with 10+ years of experience in tech sector clients.
```

**Compression rules:**
1. Remove every word that doesn't change the output.
2. Combine redundant instructions into one.
3. Use specific terms instead of explanatory phrases ("SEO strategist" instead of "someone who is an expert in search engine optimization").
4. If a constraint can be expressed as a phrase instead of a sentence, use the phrase.
5. BUT: Never compress context that's situation-specific. That's where the value lives.

---

### Technique 6: Persona Anchoring

For tasks that require maintaining a consistent voice or perspective:

```
Voice anchor: Throughout this entire output, maintain the perspective of [persona]. This means:
- Vocabulary: [type of words they'd use]
- Sentence structure: [short and punchy / long and analytical / mix]
- Attitude toward the topic: [skeptical / enthusiastic / practical / provocative]
- What they'd NEVER say: [specific phrases or approaches to avoid]
```

---

### Technique 7: Output Gating

Prevent the model from producing subpar work:

```
[Main task instruction]

Output gate: Before presenting your response, verify:
- [ ] Every recommendation is specific enough to implement tomorrow
- [ ] No point would be described as "obvious" by someone with 3+ years in this field
- [ ] Each section adds unique value (no repetition across sections)

If any check fails, revise before presenting.
```

---

### Technique 8: Context Windowing

For prompts that reference a lot of information, help the model focus:

```
Context provided below. When producing your output:
- PRIMARY focus: [specific parts of context that matter most]
- SECONDARY reference: [parts that provide background but aren't central]
- IGNORE: [parts that are included for completeness but shouldn't drive the output]

[Context block]
```

---

## PART 5: QUICK-REFERENCE DECISION TREES

### "How long should this prompt be?"
```
Is the task a single, clear action? → SHORT (3-8 lines)
Does the task need specific role context? → Add role. Now MEDIUM (8-15 lines).
Does the output need specific formatting? → Add format. Now MEDIUM-LONG (15-25 lines).
Are there known failure modes to prevent? → Add constraints. Now LONG (25-40 lines).
Is this high-stakes or multi-dimensional? → Add quality bar + safeguards. LONG+ (40-60 lines).
```

### "Should I ask the user a question or just generate?"
```
Can I determine the INTENT? 
  NO → Ask ONE question about intent.
  YES → Continue.

Can I determine the OUTPUT FORMAT?
  NO → Can I pick a sensible default? 
    YES → Generate with default, note assumption.
    NO → Ask ONE format question.
  YES → Continue.

Can I set MEANINGFUL CONSTRAINTS?
  NO → Generate with broad constraints, note that tightening is possible.
  YES → Generate. No questions needed.
```

### "Which category does this belong to?"
```
Is the user seeking INFORMATION? → Research & Analysis or Learning & Explanation
Is the user seeking a PLAN? → Strategy & Planning
Is the user seeking CONTENT? → Content Creation
Is the user seeking a SOLUTION? → Problem Solving
Is the user seeking a PROCESS? → System Design
Is the user seeking IDEAS? → Brainstorming & Ideation
Is the user seeking a MESSAGE? → Communication & Outreach
Is the user seeking DATA ORGANIZATION? → Data & Extraction
Is the user seeking FEEDBACK? → Evaluation & Critique
```
