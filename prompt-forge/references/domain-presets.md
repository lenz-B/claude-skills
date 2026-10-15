# Domain Presets

Pre-loaded context for domains the user works in frequently. When a user mentions one of these domains, inject the relevant preset into the prompt being built so they don't have to re-explain context every time.

---

## PRESET: Client Web Work (Clinics, Businesses, Personal Projects)

**Trigger keywords:** "landing page", "website", "web app", "clinic", "dental", "wellness", "booking", "client site", "build a site", "page for"

**What this covers:**
Client and personal web projects — primarily landing pages, full websites, and web apps for wellness clinics and dental clinics, plus the user's own projects. Deliverables range from single-page conversion sites to full multi-page websites to simple web apps.

**Client types:**
- **Wellness clinics** — massage, physio, chiro, yoga studios, health coaches. Audience: local, trust-driven, often booking a first appointment. Tone: warm, professional, reassuring.
- **Dental clinics** — general and cosmetic dentistry. Audience: locals searching for a dentist, often anxious. Tone: clean, clinical trust, friendly — not cold.
- **Personal projects** — user's own sites/tools. Tone: flexible, determined per project.

**Inject this context when building prompts for client web work:**
```
Project type: [Landing page / Full website / Web app]
Client type: [Wellness clinic / Dental clinic / Personal project]
Audience: Local consumers making a service decision — trust and clarity drive conversion more than clever copy.
Primary goal: [Bookings / Inquiries / Signups / Awareness]
Stack context: [Insert if known — e.g., Next.js, Webflow, plain HTML]
```

**Prompt angle by deliverable:**
- **Landing page** → Above fold: clear offer + trust signal. Middle: proof (photos, reviews, credentials). Bottom: frictionless CTA. Single goal per page.
- **Full website** → Information architecture first. Nav must answer "who are you / what do you do / how do I book" in 3 clicks or fewer.
- **Booking flow** → Friction removal at every step. Reassurance copy at decision moments (price reveal, personal info entry). Clear confirmation state.
- **Web app** → User clarity over feature density. Forgiving error states. Mobile-first for clinic use cases (patients book on phones).

**Common failure patterns for this domain:**
- Generic hero copy ("Welcome to [Clinic Name]") — always push for a specific value prop
- Missing trust signals (credentials, reviews, photos) above the fold
- CTAs that say "Learn More" instead of "Book Now" or "Get a Free Consult"
- No mobile-optimized layout on a service where 70%+ book on mobile

---

## PRESET: Deep Research

**Trigger keywords:** "research", "deep research", "look into", "find what works", "investigate", "analyze this niche", "what's working in"

**What this preset does:**
Research prompts need to produce validated, triangulated findings — not summaries of the first Google page. The deep-research skill's methodology applies: frame the question precisely, require multi-source triangulation, flag confidence levels, and output actionable patterns not just facts.

**Inject this framing when building research prompts:**
```
Research standard: Validated findings only. Require triangulation across 2+ independent source types.
Confidence labeling: Tag claims as Strong evidence / Moderate evidence / Limited evidence / Conflicting.
Output format: Key findings → supporting evidence → practical implications → confidence level.
Constraint: Do not present single-source claims as established facts. Flag uncertainty explicitly.
Safeguard: If specific data isn't available, provide directional insight and flag where to verify.
```

**Prompt angle by research type:**
- **"What works in X"** → Pattern extraction across practitioners + observable data + community consensus
- **"Research X vs Y"** → Structured comparison with clear evaluation criteria and a recommendation
- **"How does X work"** → Mechanism breakdown from first principles to practical application
- **"Find opportunities in X"** → Gap analysis: what exists, what's missing, who's underserved

---

## PRESET: Content Strategy / Meta-Level

**Trigger keywords:** "content strategy", "content plan", "content system", "what to post", "content calendar", "build an audience", "meta level", "strategy for my content"

**Context to inject:**
```
Deliverable: An actionable content system, not a list of topics.
Audience clarity required: Who specifically reads this, what they care about, what they'd share.
Platform-specific: Output must account for how the specific platform distributes content.
Anti-generic constraint: No "post consistently" or "provide value" advice — only specific mechanics.
Quality bar: A content director at a growth-stage brand should find this immediately executable.
```

---

## PRESET: Technical Breakdown

**Trigger keywords:** "technical breakdown", "how does X work", "explain the mechanics", "break down", "under the hood", "architecture", "deep dive technical"

**Context to inject:**
```
Audience: Assume technically literate reader — skip basic definitions, start at mechanism level.
Structure: Core mechanism first → components → how they interact → practical implications.
Depth: Go beyond surface explanations. If it's been covered in a blog post, go deeper.
Constraint: No filler. Every sentence must increase understanding. Cut anything that doesn't.
Format: Start with the key insight, then build the model. Not chronological history.
```

---

## Adding a New Preset

When the user describes a new recurring domain or project, extract:
1. What it is (1-2 sentences)
2. Who the audience is
3. What the tone/brand voice is
4. What the typical deliverables are
5. What the success criteria look like for that domain

Add it to this file under a new `## PRESET:` heading.
