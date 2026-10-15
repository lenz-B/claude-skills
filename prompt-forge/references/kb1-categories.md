# KB1 — Prompt Category Framework & Decision Logic

This is the reference document for classifying raw user input into the correct prompt category. Each category has specific structural patterns that produce the highest-quality outputs.

---

## THE 10 PROMPT CATEGORIES

---

### CATEGORY 1: RESEARCH & ANALYSIS

**When to classify here:** The user wants to find, understand, compare, or synthesize information about a topic. Keywords: "how does X work," "research," "what's the best," "compare," "analyze," "break down," "what are the options."

**Best structural patterns:**

**Pattern A — Deep Dive Research**
```
Role: [Domain specialist]
Task: Produce a comprehensive research brief on [topic].
Structure: Break into [specific sections].
Depth: Go beyond surface-level. Include [mechanisms/data/examples].
Constraints: [What to exclude]. [What to prioritize].
Quality: Write as if briefing a senior executive who will make decisions based on this.
```

**Pattern B — Comparative Analysis**
```
Role: [Analyst type]
Task: Compare [X] vs [Y] across [specific dimensions].
Format: Use a structured comparison with clear winners per dimension.
Criteria: Evaluate on [criteria 1], [criteria 2], [criteria 3].
Constraints: Base analysis on [evidence type]. Flag uncertainty.
Output: End with a clear recommendation with reasoning.
```

**Pattern C — Mechanism Breakdown**
```
Role: [Technical expert]
Task: Explain exactly how [system/process] works.
Depth: Go from first principles to practical implications.
Structure: Start with the core mechanism, then explain each component, then show how they interact.
Audience: [Specify knowledge level].
Constraints: No filler. Every sentence must increase understanding.
```

---

### CATEGORY 2: STRATEGY & PLANNING

**When to classify here:** The user needs a plan, roadmap, framework, or strategic recommendation. Keywords: "strategy," "plan," "roadmap," "how should I," "framework," "approach," "next steps."

**Best structural patterns:**

**Pattern A — Strategic Framework**
```
Role: [Strategy specialist in specific domain]
Context: [Situation, goals, constraints, resources]
Task: Develop a strategic framework for [goal].
Structure: Include situational analysis, strategic options, recommended approach, implementation phases, success metrics.
Constraints: [Budget/time/resource limits]. Must be executable by [team size/type].
Quality: This should read like a top-tier consulting deliverable, not a blog post.
```

**Pattern B — Decision Framework**
```
Role: [Decision-making specialist]
Context: [The decision to be made, stakes, constraints]
Task: Build a decision framework for [choice].
Include: Key criteria, weighted scoring, risk analysis for each option, clear recommendation.
Constraints: Prioritize [speed/quality/cost]. Account for [specific risks].
Format: Decision matrix with reasoning.
```

**Pattern C — Action Roadmap**
```
Role: [Execution-focused strategist]
Context: [Current state, desired state, available resources]
Task: Create a phased action roadmap to achieve [goal] in [timeframe].
Structure: Phase 1/2/3 with specific milestones, tasks, owners, and deadlines.
Constraints: Must be realistic for [team size]. Start with highest-impact actions.
Quality: Someone should be able to start executing Phase 1 immediately after reading this.
```

---

### CATEGORY 3: CONTENT CREATION

**When to classify here:** The user wants to create written content — posts, articles, emails, scripts, copy. Keywords: "write," "draft," "create," "content," "post," "article," "copy."

**Best structural patterns:**

**Pattern A — Targeted Content Piece**
```
Role: [Specific writer type — e.g., "B2B LinkedIn ghostwriter who specializes in founder storytelling"]
Context: [Who is the author? Who is the audience? What's the goal?]
Task: Write [content type] about [topic].
Tone: [Specific tone markers — e.g., "conversational but authoritative, like talking to a smart friend at a conference"]
Structure: [Hook type, body structure, CTA type]
Constraints: [Word count]. [What to avoid]. [What must be included].
Quality: This should feel like it was written by someone with 10+ years in [industry], not AI.
```

**Pattern B — Multi-Variant Generation**
```
Role: [Writer type]
Context: [Brief, audience, goal]
Task: Generate [N] variations of [content type].
Variation parameters: Vary [hook style / angle / tone / format] across versions.
Format: Label each version clearly. Include a 1-line note on what makes each version different.
Constraints: No two versions should share the same opening structure or core angle.
```

**Pattern C — Content Expansion/Transformation**
```
Role: [Writer type]
Source material: [Paste or describe the source]
Task: Transform this into [target format].
Preserve: [Core message, key data, specific points]
Change: [Tone, length, structure, audience level]
Constraints: Do not add information not present in the source. Maintain factual accuracy.
```

---

### CATEGORY 4: PROBLEM SOLVING

**When to classify here:** The user has a specific problem, blocker, or challenge and needs solutions. Keywords: "stuck," "not working," "how do I fix," "problem," "challenge," "struggling with."

**Best structural patterns:**

**Pattern A — Diagnostic Problem Solving**
```
Role: [Domain troubleshooter]
Problem: [Specific problem statement]
Context: [What's been tried, what the current state is, what success looks like]
Task: Diagnose the root cause and provide solutions.
Structure: 1) Most likely root causes ranked by probability. 2) Solution for each cause. 3) Recommended first action.
Constraints: Focus on actionable fixes, not theory. Prioritize speed of resolution.
```

**Pattern B — Obstacle Navigation**
```
Role: [Strategic advisor in domain]
Situation: [The obstacle and its impact]
Goal: [What the user is trying to achieve despite the obstacle]
Task: Provide [N] distinct approaches to overcome this obstacle.
For each approach: Explain the method, required resources, timeline, risk level, and likelihood of success.
Constraints: At least one approach must be executable within [timeframe] with [resource level].
```

**Pattern C — Root Cause Analysis**
```
Role: [Systems thinker / analyst]
Symptom: [What's going wrong]
Context: [System/process description, when it started, what changed]
Task: Perform a root cause analysis.
Method: Use [5 Whys / Fishbone / First Principles] approach.
Output: Root cause identification, contributing factors, and prevention strategy.
```

---

### CATEGORY 5: SYSTEM DESIGN

**When to classify here:** The user wants to build a process, workflow, SOP, automation, or operational system. Keywords: "system," "process," "workflow," "SOP," "automate," "build a system for."

**Best structural patterns:**

**Pattern A — Process Design**
```
Role: [Operations/systems architect in domain]
Context: [Current pain points, scale, team structure]
Task: Design a complete [process/workflow] for [function].
Include: Step-by-step process, roles/responsibilities, tools needed, handoff points, quality checkpoints.
Constraints: Must work for a team of [size]. Must be implementable without [excluded tools/resources].
Quality: Detailed enough that someone new could follow it on day one.
```

**Pattern B — SOP Creation**
```
Role: [Operations manager]
Function: [What this SOP covers]
Task: Create a detailed SOP for [process].
Format: Numbered steps with decision points, exceptions handling, and quality checks.
Include: Trigger (when to start), inputs needed, step-by-step procedure, expected outputs, common errors and fixes.
Constraints: Write for someone with [experience level]. No assumed knowledge beyond [baseline].
```

**Pattern C — Automation Blueprint**
```
Role: [Automation architect]
Current manual process: [Describe what's being done manually]
Goal: Design an automation blueprint.
Include: What to automate vs keep manual, tool recommendations, data flow, trigger conditions, error handling.
Constraints: Budget [X]. Existing tools: [list]. Technical skill level of implementer: [level].
```

---

### CATEGORY 6: LEARNING & EXPLANATION

**When to classify here:** The user wants to understand something, learn a concept, or build a mental model. Keywords: "explain," "teach me," "how does," "what is," "help me understand," "break down for me."

**Best structural patterns:**

**Pattern A — Concept Explanation**
```
Role: [Expert teacher in domain]
Task: Explain [concept] to someone who [knowledge level description].
Structure: Start with a one-sentence definition. Then explain the core mechanism. Then give a real-world analogy. Then show practical application.
Depth: [Surface overview / Working understanding / Deep technical grasp]
Constraints: No jargon unless defined. Prioritize clarity over completeness.
```

**Pattern B — Skill Building Guide**
```
Role: [Experienced practitioner and teacher]
Task: Create a learning roadmap for [skill].
Learner profile: [Current level, available time, goals]
Structure: Phase-based progression from [current state] to [target state].
For each phase: Core concepts to master, practice exercises, resources, milestones to hit before moving on.
Constraints: Practical over theoretical. Include specific exercises, not just "practice more."
```

**Pattern C — Mental Model Construction**
```
Role: [Systems thinker / domain expert]
Task: Build a mental model for understanding [complex topic].
Approach: Identify the 3-5 core principles that govern [topic]. Explain each with an analogy. Show how they interact. Provide a framework for applying this mental model to real situations.
Constraints: Prioritize usefulness over completeness. The model should help make better decisions, not just sound smart.
```

---

### CATEGORY 7: DATA & EXTRACTION

**When to classify here:** The user wants to pull structured information from unstructured sources, organize data, or create structured outputs from messy inputs. Keywords: "extract," "organize," "structure," "list all," "pull out," "categorize."

**Best structural patterns:**

**Pattern A — Structured Extraction**
```
Role: [Data analyst / researcher]
Source: [Describe or paste source material]
Task: Extract [specific data points] and organize into [format].
Format: [Table with columns X, Y, Z / Categorized list / Database-ready format]
Rules: [How to handle ambiguity, missing data, duplicates]
Constraints: Only extract explicitly stated information. Flag inferences separately.
```

**Pattern B — Classification & Categorization**
```
Role: [Domain specialist]
Input: [Data/list to categorize]
Task: Categorize each item into [category system].
Categories: [Define each category with clear criteria]
Format: [Grouped list / Table with category column / Nested structure]
Rules: [How to handle items that fit multiple categories, edge cases]
```

**Pattern C — Data Transformation**
```
Role: [Data specialist]
Input format: [What you have]
Desired output format: [What you need]
Task: Transform the input data into the output format.
Rules: [Mapping logic, handling of special cases, validation criteria]
Output: [Exact format specification]
```

---

### CATEGORY 8: EVALUATION & CRITIQUE

**When to classify here:** The user wants to review, audit, score, or improve existing work. Keywords: "review," "feedback," "improve," "what's wrong with," "audit," "score," "evaluate."

**Best structural patterns:**

**Pattern A — Structured Critique**
```
Role: [Senior expert / reviewer in domain]
Material to review: [Paste or describe]
Task: Provide a detailed critique.
Evaluate on: [Criterion 1], [Criterion 2], [Criterion 3].
Format: For each criterion — current state, specific problems, specific fix.
Constraints: Be direct. No compliment sandwiches. Prioritize fixes by impact.
Quality: Review as if this will ship to [high-stakes audience] tomorrow.
```

**Pattern B — Scoring & Benchmarking**
```
Role: [Evaluator with domain expertise]
Items to evaluate: [List/describe]
Task: Score each item on [scale] across [dimensions].
Scoring criteria: [Define what each score level means]
Format: Scorecard with scores, brief justification per score, and overall ranking.
Constraints: Justify every score. No arbitrary ratings.
```

**Pattern C — Gap Analysis**
```
Role: [Domain strategist]
Current state: [Describe what exists]
Desired state: [Describe the target]
Task: Identify gaps between current and desired state.
Format: Gap identification, severity ranking, recommended fixes, priority order.
Constraints: Focus on gaps that are fixable within [timeframe/budget]. Distinguish quick wins from long-term fixes.
```

---

### CATEGORY 9: COMMUNICATION & OUTREACH

**When to classify here:** The user needs to compose a message to another person — emails, DMs, pitches, scripts, follow-ups. Keywords: "email," "message," "reach out," "pitch," "follow up," "reply," "cold outreach."

**Best structural patterns:**

**Pattern A — Persuasive Outreach**
```
Role: [Communication specialist — e.g., "cold outreach strategist for B2B services"]
Context: [Who's sending, who's receiving, relationship status, goal of message]
Task: Write a [message type] to [recipient].
Goal: [Specific desired action from recipient]
Tone: [Match to relationship and context]
Structure: [Hook → Value prop → Proof → CTA]
Constraints: Max [word count]. No generic flattery. Lead with value.
```

**Pattern B — Response Crafting**
```
Role: [Communication strategist]
Original message: [Paste what you're responding to]
Context: [Relationship, stakes, your goal in responding]
Task: Draft a response that [achieves specific goal].
Tone: [Specified based on situation]
Constraints: Address all points raised. Keep it [concise/detailed based on context].
```

**Pattern C — Script/Talk Track**
```
Role: [Sales/communication coach]
Scenario: [Meeting type, call type, presentation]
Audience: [Who you're talking to]
Goal: [What outcome you want]
Task: Create a talk track / script.
Structure: Opening, key points, objection handling, close.
Constraints: Natural conversational flow, not robotic. Include transition phrases.
```

---

### CATEGORY 10: BRAINSTORMING & IDEATION

**When to classify here:** The user wants to generate ideas, explore possibilities, or think creatively. Keywords: "ideas," "brainstorm," "what if," "options," "possibilities," "creative," "angles."

**Best structural patterns:**

**Pattern A — Structured Brainstorm**
```
Role: [Creative strategist in domain]
Context: [Problem/opportunity to brainstorm around]
Task: Generate [N] distinct ideas for [goal].
Diversity rule: Ideas must span [different approaches/categories/risk levels].
Format: For each idea — name, 2-sentence description, why it could work, biggest risk.
Constraints: No obvious/generic ideas. Push past the first 5 "safe" ideas into unexpected territory.
```

**Pattern B — Angle Mining**
```
Role: [Content strategist / creative director]
Topic: [The base topic]
Task: Find [N] unique angles to approach [topic].
Angle types: Include at least one contrarian angle, one data-driven angle, one story-driven angle, and one practical angle.
Format: Angle name, 1-sentence description, why it would resonate with [audience].
Constraints: No angles that have been overdone. Prioritize freshness.
```

**Pattern C — Idea Expansion**
```
Role: [Innovation strategist]
Seed idea: [The starting concept]
Task: Expand this idea into [N] concrete variations.
Expand along: [Audience, format, scale, application, industry]
Format: Each variation described in 3-4 sentences with a clear differentiator.
Constraints: Each variation must be different enough to stand alone. No slight rewordings.
```

---

## CATEGORY DECISION LOGIC

When the user's input could fit multiple categories, use this priority logic:

1. **What is the PRIMARY deliverable?** — A research brief? A plan? A piece of content? A solution? Classify based on the end output, not the topic.

2. **Is the user trying to LEARN or DO?** — "How does LinkedIn algorithm work" = Research/Learning. "Create a LinkedIn strategy" = Strategy. "Write me a LinkedIn post" = Content Creation.

3. **Is there a PROBLEM to solve?** — If yes and the core ask is fixing something, it's Problem Solving. If the core ask is building something new, it's System Design or Strategy.

4. **Is the user generating or evaluating?** — Generating new ideas = Brainstorming. Evaluating existing work = Evaluation & Critique.

5. **When still ambiguous:** Default to the category that requires MORE structure. Over-structuring produces better outputs than under-structuring.

---

## CROSS-CATEGORY COMBINATIONS

Some tasks legitimately span categories. In these cases, the prompt should use the PRIMARY category's structure as the backbone, then inject elements from the secondary category.

Examples:
- "Research LinkedIn algorithm AND create a content strategy" → Primary: Strategy. Secondary: Research (used as context-building section within the strategy prompt).
- "Brainstorm email subject lines AND evaluate which are strongest" → Primary: Brainstorming. Secondary: Evaluation (add evaluation criteria at the end of the brainstorm prompt).
- "Explain how sales funnels work AND build one for my business" → Split into two separate prompts. Recommend the user run them sequentially.
