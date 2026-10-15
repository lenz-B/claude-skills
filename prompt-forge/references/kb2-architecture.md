# KB2 — Templates, Examples & Quality Standards

This document provides the 7-Component Prompt Architecture, universal fill-in templates, strong/weak examples with analysis, and quality benchmarks.

---

## THE 7-COMPONENT PROMPT ARCHITECTURE

Every high-performance prompt is built from these 7 components. Not every prompt needs all 7 — but every prompt should be evaluated against all 7.

### Component 1: ROLE
**What it does:** Sets the model's expertise lens, vocabulary, and depth of reasoning.
**Why it matters:** A "B2B SaaS growth strategist" produces fundamentally different output than a "marketing assistant." The role primes the model's entire knowledge retrieval and reasoning pattern.
**Rule:** Always make the role SPECIFIC to the domain. Never use generic roles.

### Component 2: CONTEXT
**What it does:** Provides the background the model needs to tailor its output to the specific situation.
**Why it matters:** Without context, the model defaults to generic advice. Context is the #1 differentiator between a useful prompt and a useless one.
**Rule:** Include only context that would CHANGE the output. Test by removing each line — if the output wouldn't change, delete it.

### Component 3: OUTCOME
**What it does:** Defines exactly what the deliverable is.
**Why it matters:** Vague outcomes produce vague outputs. "Help me with LinkedIn" vs "Produce a 30-day LinkedIn content calendar with post topics, hooks, and CTAs" will produce entirely different results.
**Rule:** The outcome must be concrete enough that you could objectively judge whether the model delivered it or not.

### Component 4: FORMAT
**What it does:** Controls the structure and presentation of the output.
**Why it matters:** Same content in different formats has wildly different usefulness. A comparison in paragraph form vs a table vs a decision matrix serves different purposes.
**Rule:** Specify format when it matters. Default to the most actionable format for the task.

### Component 5: CONSTRAINTS
**What it does:** Prevents the model from drifting into generic, obvious, or unwanted territory.
**Why it matters:** Without constraints, models default to safe, broad, "something-for-everyone" outputs. Constraints force specificity.
**Rule:** Every prompt for a non-trivial task should have at least one constraint. The most powerful constraint types are exclusion constraints ("Do NOT...").

### Component 6: QUALITY BAR
**What it does:** Sets the standard the output must meet.
**Why it matters:** Models calibrate effort to perceived expectations. Telling it "write like a McKinsey analyst" produces materially different output than leaving quality undefined.
**Rule:** Use a concrete reference point, not abstract words like "high quality."

### Component 7: SAFEGUARD
**What it does:** Tells the model what to do when it's uncertain.
**Why it matters:** Prevents hallucination and confident-sounding garbage. Forces the model to flag uncertainty rather than paper over it.
**Rule:** Include for any research, data, or factual prompt. Optional for creative tasks.

---

## UNIVERSAL TEMPLATES

### Template A: General-Purpose (Works for 80% of tasks)

```
You are a [SPECIFIC ROLE with domain expertise].

Context:
[2-4 sentences of relevant background. Include: the situation, who it's for, what matters most.]

Task:
[1-2 sentences stating the exact deliverable.]

Format:
[Specify structure: sections, bullet points, table, narrative, etc.]

Constraints:
- [Exclusion: what to avoid]
- [Specificity: what level of detail]
- [Scope: boundaries of the task]

Quality bar: [Concrete quality reference — e.g., "Write as if this will be presented to a board of directors."]

If any part of this is unclear, state your assumptions before proceeding.
```

### Template B: Research & Deep Dive

```
You are a [DOMAIN SPECIALIST] with deep expertise in [SPECIFIC AREA].

I need a comprehensive research brief on [TOPIC].

Cover the following:
1. [Specific question/dimension 1]
2. [Specific question/dimension 2]
3. [Specific question/dimension 3]
4. [Specific question/dimension 4]

For each section:
- Lead with the key insight
- Support with [evidence type: data, examples, case studies, mechanisms]
- Include practical implications

Constraints:
- Go beyond surface-level explanations. I need depth, not breadth.
- [Specific exclusions — what NOT to cover]
- If you're not confident about a specific claim, flag it explicitly.

Quality bar: This should read like an expert briefing document, not a Wikipedia article.
```

### Template C: Strategy & Planning

```
You are a [STRATEGY SPECIALIST] who has built/scaled [RELEVANT EXPERIENCE].

Context:
- Current situation: [Where things stand now]
- Goal: [Specific target outcome]
- Resources: [What's available — team, budget, time, tools]
- Constraints: [Limitations to work within]

Task: Create a [strategic plan / roadmap / framework] for [GOAL].

Structure:
1. Situation assessment (what's working, what's not)
2. Strategic options (at least [N] distinct approaches)
3. Recommended approach with reasoning
4. Implementation roadmap with phases and milestones
5. Key metrics to track

Constraints:
- Every recommendation must be executable with the stated resources.
- No generic advice. Every point must be specific to this situation.
- Prioritize by impact. Lead with highest-leverage moves.

Quality bar: [Concrete reference — e.g., "Like a growth strategy from a top-tier agency, not a blog post."]
```

### Template D: Content Creation

```
You are a [SPECIFIC WRITER TYPE] who writes for [AUDIENCE].

Context:
- Author/brand voice: [Describe the voice or reference a style]
- Audience: [Who reads this, what they care about]
- Goal: [What this content should accomplish]
- Platform: [Where this will be published]

Task: Write [CONTENT TYPE] about [TOPIC/ANGLE].

Structure:
- [Hook type / Opening approach]
- [Body structure — e.g., "3 key points with examples"]
- [Closing / CTA]

Tone: [Specific tone descriptors — e.g., "Confident, slightly provocative, uses short punchy sentences mixed with longer analytical ones."]

Constraints:
- Length: [Word count or range]
- Must include: [Non-negotiable elements]
- Must avoid: [Specific things to exclude]
- No AI-sounding phrases like "in today's world" or "it's important to note that"

Quality bar: [E.g., "This should sound like a human expert wrote it, not AI. It should pass an AI detection test."]
```

### Template E: Problem Solving

```
You are a [DOMAIN TROUBLESHOOTER / PROBLEM SOLVER].

Problem: [Clear problem statement]

Context:
- What's happening: [Symptoms]
- What's been tried: [Previous attempts and results]
- What success looks like: [Desired outcome]
- Constraints: [Time, budget, resources, technical limits]

Task: Diagnose the root cause and provide actionable solutions.

Format:
1. Most likely root causes (ranked by probability)
2. For each cause: specific solution, implementation steps, expected timeline
3. Quick wins: What can be done in the next 24 hours
4. Long-term fixes: What prevents this from recurring

Constraints:
- Prioritize practical solutions over theoretical ones.
- Account for the stated constraints.
- If multiple solutions exist, recommend the best one and explain why.
```

### Template F: Evaluation & Improvement

```
You are a [SENIOR EXPERT / REVIEWER] in [DOMAIN].

Here is what needs to be evaluated:
[Paste or describe the work]

Task: Provide a critical evaluation and actionable improvements.

Evaluate on:
1. [Criterion 1] — [What good looks like for this criterion]
2. [Criterion 2] — [What good looks like for this criterion]
3. [Criterion 3] — [What good looks like for this criterion]

Format for each criterion:
- Score: [1-10]
- What's working: [Brief]
- What's weak: [Specific issues]
- How to fix: [Concrete, implementable fix]

Overall assessment: [Summary + prioritized action items]

Constraints:
- Be direct. No fluff or unnecessary praise.
- Every criticism must come with a specific fix.
- Prioritize feedback by impact on [stated goal].
```

---

## STRONG vs WEAK EXAMPLES (WITH ANALYSIS)

### RESEARCH — Strong Example

```
You are a social media algorithm specialist who studies LinkedIn's content distribution mechanics.

Produce a technical breakdown of how LinkedIn's algorithm determines content reach in 2024.

Cover:
1. The initial distribution phase (first 60-90 minutes) — what signals does LinkedIn measure?
2. Content scoring factors — what specifically gets weighted and how?
3. The role of comments vs likes vs shares vs dwell time in amplifying reach
4. How LinkedIn treats different content formats (text-only, carousels, video, polls, newsletters)
5. Known algorithm penalties — what causes content to be suppressed?

For each section:
- Explain the mechanism, not just the tactic
- Include specific examples where possible
- Note any recent changes in 2024

Constraints:
- Go beyond generic advice like "post consistently" or "engage with your network."
- Focus on mechanics, not motivation.
- If something is speculation vs confirmed, label it clearly.

Quality bar: This should read like an internal platform strategy document, not a social media blog post.
```

**Why this works:**
- Specific role narrows the expertise
- Five explicit dimensions prevent the model from choosing what to cover
- "Mechanism, not tactic" constraint prevents generic output
- Quality bar sets a professional standard
- Safeguard against speculation prevents hallucination

### RESEARCH — Weak Example

```
Tell me everything about how LinkedIn works. I want to grow my account.
```

**Why this fails:**
- No role = model defaults to generic assistant
- "Everything" = no focus, model picks what's easiest to generate
- "Grow my account" mixes research with strategy — unclear deliverable
- No format = wall of text or random list
- No constraints = surface-level tips guaranteed
- No quality bar = model gives minimal effort

### RESEARCH — Weak Example 2

```
You are an expert. Research LinkedIn algorithm for me. Be thorough and comprehensive. Give me actionable insights.
```

**Why this fails:**
- "Expert" in what? Too vague
- "Be thorough and comprehensive" is noise — doesn't define dimensions of thoroughness
- "Actionable insights" without specifying what actions = model decides for you
- No structure = unpredictable output format
- No constraints = nothing preventing generic advice

---

### STRATEGY — Strong Example

```
You are a B2B service agency growth strategist who has scaled multiple agencies from $10K to $100K MRR.

Context:
- I run a LinkedIn personal branding agency with a team of 4 writers.
- Current MRR is around $8K. Clients are across US, UK, Dubai, India.
- Average client value is $1,500/month. We do ghostwriting + content strategy.
- Main acquisition channel is LinkedIn outreach and referrals.
- Biggest constraint: my time is split between client delivery and growth.

Task: Create a 90-day growth plan to double MRR from $8K to $16K.

Structure:
1. Quick audit of the current model — where are the bottlenecks?
2. 3 distinct growth levers I should focus on (ranked by impact)
3. For each lever: specific tactics, timeline, expected impact, resources needed
4. A weekly action framework I can follow
5. Key metrics to track weekly

Constraints:
- Don't suggest "raise your prices" without explaining the positioning change required to support it.
- No generic advice like "network more" or "create content." Specific tactics only.
- All recommendations must work with a team of 4 writers and limited owner bandwidth.

Quality bar: This should read like a strategic plan from a $500/hour consultant, not a LinkedIn post about "scaling tips."
```

**Why this works:**
- Hyper-specific role with scale context
- Rich situational context allows tailored advice
- Concrete goal ($8K to $16K in 90 days)
- Five structured sections ensure completeness
- Constraints prevent the most common generic outputs
- Quality bar forces depth

### STRATEGY — Weak Example

```
How do I grow my agency? I want to make more money.
```

**Why this fails:**
- No role = generic business advice
- No context = model doesn't know what kind of agency, current revenue, team size, or constraints
- "More money" = not measurable
- No format = unpredictable output
- No constraints = guaranteed to include "build your personal brand" and "increase prices"

---

### CONTENT CREATION — Strong Example

```
You are a LinkedIn ghostwriter who specializes in B2B founder content. You write in a style that's direct, slightly provocative, and uses personal stories to illustrate business lessons.

Context:
- Author: A founder who runs a DevOps consultancy, 15 years experience, audience is CTOs and VP Engineering.
- Goal: Build authority and generate inbound leads.
- Platform: LinkedIn text post (mobile-first reading experience).

Task: Write 3 LinkedIn post variations about "why most companies waste money on cloud infrastructure."

For each post:
- Use a different hook style (1: contrarian stat, 2: personal story, 3: direct challenge)
- Body: 1 core insight with a specific example
- CTA: Soft engagement CTA (question, not "DM me")
- Length: 800-1200 characters per post

Constraints:
- No corporate jargon. Write like talking to someone, not presenting to them.
- No AI-sounding phrases ("In today's rapidly evolving landscape...").
- No generic advice. Every point must come from genuine operational experience.
- Must feel like it was written by a human with strong opinions, not a content mill.

Quality bar: These should stop someone mid-scroll. If someone wouldn't pause to read this, it's not good enough.
```

**Why this works:**
- Specific writer persona with style definition
- Author context allows authentic voice matching
- Three variations with specified hook differences prevent sameness
- Character count prevents bloat
- Anti-AI constraint fights the most common content failure
- Quality bar is vivid and actionable

### CONTENT CREATION — Weak Example

```
Write me a LinkedIn post about cloud computing. Make it engaging.
```

**Why this fails:**
- No author context = generic voice
- No audience specified = writing for everyone (which means no one)
- "Cloud computing" = massive topic, no angle
- "Engaging" = meaningless without definition
- No structure, no length, no constraints
- Will produce something that reads like every other AI-generated LinkedIn post

---

### COMMUNICATION — Strong Example

```
You are a B2B sales outreach specialist who writes cold emails that sound like a human peer, not a salesperson.

Context:
- I run a LinkedIn ghostwriting agency for B2B founders.
- Target: VP Marketing at a Series B SaaS company (100-500 employees).
- They likely get 50+ cold emails per week.
- Goal: Get a 15-minute discovery call.

Task: Write a 3-email cold outreach sequence.

Email 1 (Initial): Hook with a specific observation about their LinkedIn presence. Max 80 words.
Email 2 (Follow-up, Day 3): Add value with a specific, relevant insight. Max 60 words.
Email 3 (Break-up, Day 7): Light, short, creates urgency without being pushy. Max 40 words.

Constraints:
- No "I hope this finds you well." No "I wanted to reach out."
- No pitch in Email 1. Lead with observation/value.
- Subject lines must be lowercase, casual, under 5 words.
- Each email must stand alone (don't reference "my last email").
- Must feel like it came from a peer, not a vendor.

Quality bar: A VP Marketing should read Email 1 and think "this person actually looked at my profile" not "this is a template."
```

### COMMUNICATION — Weak Example

```
Write a cold email for my agency. We do LinkedIn branding.
```

**Why this fails:**
- No recipient profile = generic messaging
- No sequence structure = single generic email
- No word limits = will be too long
- No constraints on tone = will sound like a sales pitch
- No quality bar = no scroll-stopping power

---

## PROMPT LENGTH CALIBRATION GUIDE

| Task Complexity | Prompt Length | Components Needed | Example Task |
|---|---|---|---|
| Simple/Clear | 3-8 lines | Outcome + Format | "Summarize this article in 3 bullet points" |
| Moderate | 8-20 lines | Role + Context + Outcome + Format + 1 Constraint | "Research X and present as a brief" |
| Complex | 20-40 lines | All 7 components | "Build a 90-day strategy for..." |
| Mission-Critical | 40-60+ lines | All 7 + multiple constraints + examples | "Design a complete system for..." |

**The golden rule:** A prompt should be exactly as long as needed to eliminate ambiguity. One extra line of useful constraint is better than one less line and a vague output.

---

## QUALITY BENCHMARK CHECKLIST

Before finalizing any generated prompt, evaluate it against:

1. **Specificity Test:** If you removed the topic, could this prompt be about anything? If yes → too generic.
2. **Deliverable Test:** Can you objectively judge if the model delivered what was asked? If not → outcome is too vague.
3. **Role Test:** Does the assigned role bring specific expertise that changes the output? If not → role is too generic.
4. **Constraint Test:** Is there at least one thing the model is told NOT to do? If not → output will drift generic.
5. **Format Test:** Will the output be structured in a useful way? If not → add format control.
6. **Quality Test:** Is there a concrete quality reference? If not → model will give minimum effort.
7. **Length Test:** Is the prompt the right length for the task? Too short = ambiguous. Too long = padded.
8. **Assumption Test:** For complex tasks, is there a safeguard against the model guessing wrong? If not → add one.
