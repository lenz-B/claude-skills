# Example Skills — Annotated at Three Complexity Levels

These are complete, annotated example skills showing the design principles in action. Read this file for reference when building new skills.

---

## Example 1: Simple Skill (Flat SKILL.md, No Resources)

**Use case:** A brand style guide that ensures Claude applies consistent visual identity.

**Why it's simple:** One procedure, one domain, no branching, no scripts needed.

```markdown
---
name: brand-guidelines
description: "Applies Acme Corp's official brand colors and typography to any
  frontend artifact, document, or presentation. Use this skill whenever the user
  mentions brand colors, style guidelines, visual formatting, company design
  standards, or wants anything to look 'on-brand' or 'like our website'. Also
  trigger when creating customer-facing materials, pitch decks, or marketing
  assets for Acme Corp. Do NOT use for personal projects, non-Acme content, or
  when the user explicitly requests a different visual style."
---

# Acme Corp Brand Styling

## Overview

Acme Corp's visual identity uses a warm, confident palette with high contrast
and distinctive typography. The system has four hierarchy levels: primary dark
for text, accent orange for CTAs and emphasis, cool blue for informational
elements, and warm gray for backgrounds and dividers.

## Brand Tokens

### Colors
| Token | Hex | Usage |
|-------|-----|-------|
| Primary Dark | `#1A1A2E` | Body text, headings, dark backgrounds |
| Accent Orange | `#E94F37` | CTAs, links, emphasis, interactive elements |
| Info Blue | `#3A86A8` | Informational highlights, secondary actions |
| Warm Gray | `#F2F0EB` | Backgrounds, cards, dividers |
| White | `#FFFFFF` | Text on dark backgrounds, card surfaces |

### Typography
- **Headings:** DM Sans (fallback: Arial) — bold weight, tight tracking (-0.02em)
- **Body:** Source Serif Pro (fallback: Georgia) — regular weight, generous line-height (1.6)
- **Code/Data:** JetBrains Mono (fallback: Consolas)

### Spacing Scale
Base unit: 8px. Use multiples: 8, 16, 24, 32, 48, 64, 96.

## Application Rules

Apply these tokens consistently across all output formats:

**HTML/CSS:** Use CSS custom properties for all color and font values. Set
properties on `:root` so they cascade to all elements.

**Presentations (.pptx):** Apply DM Sans to all headings 24pt and larger.
Apply Source Serif Pro to body text. Use Accent Orange for shape fills and
slide accent elements. Cycle through Orange → Blue → Gray for charts.

**Documents (.docx):** Use DM Sans for Heading 1–3 styles. Use Source Serif
Pro for Normal style. Set heading color to Primary Dark (never use colored
headings — they reduce readability on print).

## Critical Rules

- **Never use colored headings in print documents** — screen colors don't
  reproduce reliably on all printers; always use Primary Dark for text
- **Minimum contrast ratio 4.5:1** — Accent Orange on white passes; Accent
  Orange on Warm Gray fails and needs Primary Dark instead
- **Don't mix brand fonts with system defaults** — if a brand font isn't
  available, use its designated fallback, not a random system font
```

**Annotations:**
- ✅ Description is 94 words with trigger inventory and exclusion fence
- ✅ Domain primer establishes the visual hierarchy model in 3 sentences
- ✅ No decision router needed (single procedure)
- ✅ Concrete token values, not vague descriptions
- ✅ Application rules cover three output formats with specific instructions
- ✅ Constraint catalog with failure modes
- ✅ No resources needed — everything fits in ~80 lines

---

## Example 2: Multi-Procedure Skill (Decision Router, No Resources)

**Use case:** A code review skill that handles multiple review types.

```markdown
---
name: code-review
description: "Use this skill whenever the user asks Claude to review, audit,
  critique, or analyze Python code for quality. Triggers include: 'code review',
  'review this code', 'review my PR', 'audit this file', 'what's wrong with
  this code', or any request to evaluate Python files for bugs, architecture,
  security, or maintainability. Also use when the user shares a Python file
  and asks for feedback, improvements, or 'what would you change'. Do NOT use
  for writing new code from scratch, debugging specific runtime errors, or
  reviewing non-Python languages."
---

# Python Code Review

## Overview

Effective code review operates on four layers: correctness (does it work),
security (can it be exploited), architecture (does it fit the system), and
maintainability (can someone else work on it in 6 months). Most automated
linters only cover correctness. This skill covers all four.

## Quick Reference

| Review Type | When to Use |
|------------|-------------|
| Full review | Default — use for any file or PR |
| Security-focused | User mentions security, auth, user input, APIs |
| Architecture-focused | User mentions design, refactoring, system structure |
| Quick scan | User says "quick look" or "anything obvious?" |

---

## Full Review Procedure

### Step 1: Read Completely First

Read the entire file before commenting. Understand the module's purpose,
public interface, and dependencies. Commenting on line 10 without knowing
what line 200 does produces contradictory advice.

### Step 2: Layer 1 — Correctness

Check for:
- Off-by-one errors in loops and slices
- Unhandled exception paths (bare `except:` catches KeyboardInterrupt and
  SystemExit, masking real bugs — always catch specific exceptions)
- Mutable default arguments (`def f(x=[])` — the list persists across calls)
- Type mismatches between function signatures and actual usage
- Race conditions in concurrent code (threading, asyncio)

### Step 3: Layer 2 — Security

Check for:
- SQL injection via string formatting (use parameterized queries — user
  input can escape string boundaries and execute arbitrary SQL)
- Path traversal via unsanitized `os.path.join` with user input
- Unsafe deserialization (`pickle.loads` on untrusted data allows arbitrary
  code execution — use JSON or a safe serializer)
- Hardcoded secrets in source (API keys, passwords, tokens)
- Missing input validation on any function accepting external data

### Step 4: Layer 3 — Architecture

Evaluate:
- Single Responsibility — does each class/function do one thing?
- Dependency direction — high-level modules should not import low-level ones
- Interface boundaries — are public methods well-defined and minimal?
- Coupling — would changing this module require changing 5 others?

### Step 5: Layer 4 — Maintainability

Check:
- Functions over 30 lines — likely need decomposition
- Single-letter variable names outside 3-line comprehensions — readability debt
- Public functions without docstrings — undocumented contracts break silently
- Untestable code — if you can't write a unit test for it, the coupling is wrong

### Step 6: Synthesize

Present findings in priority order:
1. **Critical** — bugs, security vulnerabilities, data loss risks
2. **Important** — architectural issues, significant maintainability problems
3. **Suggestions** — style, minor optimizations, nice-to-haves

For EVERY finding include: location (file:line), description (what + why),
and a concrete fix (actual code, not "add error handling").

End with: overall assessment (1–2 sentences), top 3 priorities, and
something done well. Exclusively negative reviews get ignored.

---

## Security-Focused Review

Follow Steps 1–2 from Full Review, then go deep on Step 3. For each
security finding, classify severity:
- **Critical** — exploitable now, no authentication required
- **High** — exploitable with some access or specific conditions
- **Medium** — defense-in-depth violation, not directly exploitable
- **Low** — best-practice deviation, theoretical risk

---

## Quick Scan

Read the file once. Report only Critical and Important findings. Skip
architecture and maintainability layers. Limit to 5 findings max. State
explicitly: "This is a quick scan — a full review would also cover
architecture and maintainability."

---

## Critical Rules

- **Never say 'add error handling' without specifics** — name the exception
  types, the recovery behavior, and the user-facing message
- **Always provide code fixes** — reviewees need to see what the fix looks
  like, not just that something is wrong
- **Read completely before commenting** — partial-file reviews produce
  contradictory advice
- **Don't flag style issues alongside bugs** — fix correctness first;
  style comments on broken code are noise that dilutes critical feedback
- **Acknowledge good patterns** — exclusively negative reviews are
  demoralizing and less likely to be acted on
```

**Annotations:**
- ✅ Four-layer domain primer creates the review structure
- ✅ Decision router maps four review types to procedures
- ✅ Each checklist item includes failure mode in parentheses
- ✅ Synthesis step has a specific output format (priority-ordered, always includes a fix)
- ✅ Quick scan explicitly states its limitations
- ✅ Constraint catalog addresses behavioral failures, not just technical ones

---

## Example 3: Multi-Domain Skill with Resources (Router + References + Scripts)

**Use case:** A data pipeline skill that handles multiple databases and file formats.

**Directory structure:**
```
data-pipeline/
├── SKILL.md                     (~120 lines — routing + shared patterns)
├── scripts/
│   └── validate_schema.py       (schema validation across all formats)
├── references/
│   ├── postgres.md              (PostgreSQL-specific procedures)
│   ├── bigquery.md              (BigQuery-specific procedures)
│   └── file-formats.md          (CSV/Parquet/JSON handling)
```

**SKILL.md (abbreviated to show structure):**

```markdown
---
name: data-pipeline
description: "Use this skill whenever the user needs to build, debug, or
  optimize data pipelines involving databases (PostgreSQL, BigQuery) or file
  transformations (CSV, Parquet, JSON). Triggers include: 'ETL', 'data pipeline',
  'load data into', 'extract from database', 'transform CSV', 'move data between',
  or any request to connect data sources, clean data, or build ingestion workflows.
  Also use when the user mentions dbt, Airflow, or data quality issues even without
  saying 'pipeline'. Do NOT use for one-off data analysis, visualization, or
  ML model training."
---

# Data Pipeline Builder

## Overview

Data pipelines have three phases: extract (get data from source), transform
(clean, reshape, validate), and load (write to destination). Most pipeline
failures occur at boundaries — where data crosses from one system to another
and format assumptions break. This skill focuses on making those boundaries
robust.

## Quick Reference

| Task | Approach |
|------|----------|
| PostgreSQL operations | Read `references/postgres.md` |
| BigQuery operations | Read `references/bigquery.md` |
| File format handling | Read `references/file-formats.md` |
| Schema validation | Run `python scripts/validate_schema.py` |
| Pipeline orchestration | See Orchestration Patterns below |

---

## Shared Patterns

### Schema Validation

Before loading data into any destination, validate the schema:

```bash
python scripts/validate_schema.py --source data.csv --schema expected.json
```

This catches type mismatches, missing columns, and unexpected nulls before
they corrupt the destination table.

If validation fails, the script outputs a diff showing exactly which columns
diverge and what values caused the failure.

### Orchestration Patterns

[... Airflow/dbt patterns shared across all databases ...]

---

## Critical Rules

- **Validate schemas at every boundary** — run validate_schema.py between
  every extract→transform and transform→load step, because type assumptions
  that hold in one system often break in another
- **Never use `SELECT *` in production pipelines** — schema changes upstream
  silently add columns that break downstream transforms
- **Always set explicit timeouts** — hanging connections from long queries
  block pipeline resources indefinitely without timeouts

## Reference Files

- `references/postgres.md` — Connection patterns, COPY vs INSERT performance,
  indexing strategies for pipeline tables. Read when the source or destination
  is PostgreSQL.
- `references/bigquery.md` — Authentication, streaming inserts vs batch loads,
  partitioning strategies. Read when using BigQuery.
- `references/file-formats.md` — CSV dialect handling, Parquet schema evolution,
  JSON nested-to-flat transforms. Read when working with file-based data.
```

**Annotations:**
- ✅ SKILL.md stays at ~120 lines by deferring domain detail to references
- ✅ Decision router explicitly says "Read `references/X.md`" — clear pointers
- ✅ Shared patterns (schema validation, orchestration) stay in the body because they apply across all domains
- ✅ Validation script is bundled because it's deterministic and used on every invocation
- ✅ Reference Files section at the bottom explains when to read each one
- ✅ Domain-specific references can grow independently without bloating the body
