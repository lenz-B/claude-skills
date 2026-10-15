# Patterns Library — Concrete Examples for Every Skill Component

Read this file during Phase 4 (Write the Skill) for inspiration, templates, and anti-patterns.

---

## Description Patterns

### Pattern: The Full-Spectrum Description

The strongest descriptions have three zones: purpose, trigger inventory, and exclusion fence.

**Example (from the live `docx` skill):**
```yaml
description: "Use this skill whenever the user wants to create, read, edit,
  or manipulate Word documents (.docx files). Triggers include: any mention of
  'Word doc', 'word document', '.docx', or requests to produce professional
  documents with formatting like tables of contents, headings, page numbers,
  or letterheads. Also use when extracting or reorganizing content from .docx
  files, inserting or replacing images in documents, performing find-and-replace
  in Word files, working with tracked changes or comments, or converting content
  into a polished Word document. If the user asks for a 'report', 'memo',
  'letter', 'template', or similar deliverable as a Word or .docx file, use
  this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general
  coding tasks unrelated to document generation."
```

**Anatomy:**
- Zone 1 (Purpose): "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents"
- Zone 2 (Triggers): "Triggers include: any mention of 'Word doc'... Also use when extracting..."
- Zone 3 (Exclusion): "Do NOT use for PDFs, spreadsheets, Google Docs..."

### Pattern: The Hedged Trigger

For skills where users might need the capability without naming it:

```yaml
description: "...Make sure to use this skill whenever the user mentions
  dashboards, data visualization, internal metrics, or wants to display
  any kind of company data, even if they don't explicitly ask for a 'dashboard.'"
```

The phrase "even if they don't explicitly ask for" is a powerful trigger expander.

### Anti-Pattern: The Passive Description

```yaml
# BAD — passive, vague, no trigger surface
description: "Helps with document creation and formatting."

# BAD — too narrow, will miss casual phrasings
description: "Creates .docx files using the docx-js library."
```

---

## Domain Primer Patterns

### Pattern: The Reframing Primer

One sentence that changes how Claude thinks about the entire domain.

```markdown
## Overview
A .docx file is a ZIP archive containing XML files.
```

This transforms Claude's approach from "generate a docx somehow" to "construct a valid ZIP with well-formed XML" — a dramatically more tractable frame.

```markdown
## Overview
Effective code review operates on four layers: correctness, security,
architecture, and maintainability. Most automated linters cover only
the first.
```

This tells Claude exactly what gap this skill fills and establishes the review structure.

### Pattern: The Context-Setting Primer

```markdown
## Overview
Presentation files (.pptx) separate content from layout through a
slide-master hierarchy. Changes to the master propagate to all slides
that inherit from it, so editing the master is the most efficient way
to apply global style changes.
```

This prevents Claude from manually styling every slide.

### Anti-Pattern: The Restated Description

```markdown
# BAD — wastes tokens restating what the description already said
## Overview
This skill helps you create Word documents. When you need to make a
Word document, this skill will guide you through the process.
```

---

## Decision Router Patterns

### Pattern: The Task-Approach Table

```markdown
## Quick Reference

| Task | Approach |
|------|----------|
| Read/analyze content | `pandoc` or unpack for raw XML |
| Create new document | Use `docx-js` — see Creating New Documents below |
| Edit existing document | Unpack → edit XML → repack — see Editing below |
| Convert .doc to .docx | LibreOffice conversion — see Converting below |
```

### Pattern: The Conditional Router

For skills where the approach depends on context rather than task type:

```markdown
## Approach Selection

| Situation | Approach |
|-----------|----------|
| User provides raw data, wants a chart | Generate from scratch using Chart.js |
| User provides an existing dashboard URL | Fetch, analyze, and suggest improvements |
| User provides a screenshot | Analyze layout, then recreate in code |
```

### When NOT to Use a Router

If the skill has only one procedure (e.g., a style guide or brand guidelines), skip the router entirely. A router with one row is visual noise.

---

## Procedure Block Patterns

### Pattern: The Complete Block (Setup → Steps → Validate → Recover)

```markdown
## Creating New Documents

### Setup
```bash
npm install -g docx
```

### Procedure
Generate .docx files with JavaScript, then validate.

```javascript
const { Document, Packer, Paragraph, TextRun } = require('docx');
const doc = new Document({ sections: [{ children: [
  new Paragraph({ children: [new TextRun("Hello")] })
]}]});
Packer.toBuffer(doc).then(buffer =>
  fs.writeFileSync("doc.docx", buffer));
```

Set page size explicitly — docx-js defaults to A4, which produces
unexpected formatting for US documents:
```javascript
page: {
  size: { width: 12240, height: 15840 }, // US Letter in DXA
  margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
}
```

### Validation
After creating the file, validate it:
```bash
python scripts/office/validate.py doc.docx
```

### Recovery
If validation fails, unpack the file, fix the XML, and repack:
```bash
python scripts/office/unpack.py doc.docx unpacked/
# fix issues in unpacked/word/
python scripts/office/pack.py unpacked/ output.docx --original doc.docx
```
```

### Pattern: The Code Template with Anti-Pattern

Show both the wrong and right way when a common mistake exists:

```markdown
### Lists
```javascript
// ❌ WRONG — never manually insert bullet characters
new Paragraph({ children: [new TextRun("• Item")] })

// ✅ CORRECT — use numbering config with LevelFormat.BULLET
const doc = new Document({
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } }
      }]
    }]
  }
});
```
Why: Unicode bullets bypass the document's numbering engine, producing
items that can't be re-indented, restyled, or continued across pages.
```

### Pattern: The Layered Procedure

For complex multi-step reviews or analyses, define the layers explicitly:

```markdown
### Step 2: Layer 1 — Correctness
Check for:
- Off-by-one errors in loops and slices
- Unhandled exception paths (bare `except:` — catches KeyboardInterrupt
  and SystemExit, masking real bugs)
- Mutable default arguments (`def f(x=[])` — the list is shared across
  calls, a classic Python trap)

For each issue: state the LINE, the PROBLEM, the IMPACT, and a CONCRETE
FIX as a code snippet.
```

Each checklist item includes the failure mode in parentheses, not just the thing to check.

---

## Constraint Catalog Patterns

### Pattern: Named Rules with Failure Modes

```markdown
## Critical Rules for docx-js

- **Set page size explicitly** — docx-js defaults to A4; use US Letter
  (12240 x 15840 DXA) for US documents
- **Landscape: pass portrait dimensions** — docx-js swaps width/height
  internally; passing landscape dimensions double-swaps and breaks layout
- **Never use `\n`** — use separate Paragraph elements because newline
  characters produce invalid XML in this format
- **Never use tables as dividers** — cells have minimum height and render
  as empty boxes; use border on a Paragraph instead
- **Use `ShadingType.CLEAR`** — SOLID fills render as opaque black
  backgrounds in some viewers, hiding text
```

### Pattern: The Priority-Ordered Constraint

When some rules matter more than others, order them by severity:

```markdown
## Critical Rules

**Will break the output:**
- **Never use `pickle.loads` on untrusted data** — allows arbitrary code
  execution
- **Always parameterize SQL queries** — string formatting allows injection

**Will degrade quality:**
- **Functions over 30 lines need decomposition** — long functions resist
  testing and reuse
- **Document public interfaces** — undocumented APIs create implicit
  contracts that break silently
```

### Anti-Pattern: The Naked Rule List

```markdown
# BAD — no explanations, no failure modes, no structure
## Rules
- ALWAYS use DXA
- NEVER use percentages
- MUST validate after creation
- ALWAYS set page size
```

This produces rigid following without understanding. Claude can't generalize these rules to novel situations because it doesn't know why they exist.

---

## Test Prompt Patterns

### Pattern: The Realistic User Prompt

```
ok so my boss just sent me this xlsx file (its in my downloads, called
something like 'Q4 sales final FINAL v2.xlsx') and she wants me to add
a column that shows the profit margin as a percentage. The revenue is in
column C and costs are in column D i think
```

Why this is good: file path detail, casual speech, uncertainty ("i think"), realistic naming convention, specific columns, real business context.

### Pattern: The Edge-Case Prompt

```
I have a Word doc with tracked changes from 3 different reviewers and
I need to accept some changes, reject others, and add comments explaining
why. The doc is about 40 pages and has some images that keep breaking
when I edit. Can you help?
```

Why this is good: multi-author complexity, mixed operations, known failure mode (breaking images), substantial length.

### Anti-Pattern: The Toy Prompt

```
# BAD — too simple, won't trigger skills
"Format this data"
"Create a chart"
"Review my code"
```

These are so simple that Claude handles them without consulting any skill, regardless of how good the description is. Test prompts must be substantive enough that a skill would genuinely help.

---

## Resource Organization Patterns

### Pattern: Domain-Branched References

```
cloud-deploy/
├── SKILL.md           (80 lines — workflow + selection logic)
└── references/
    ├── aws.md         (300 lines — AWS-specific procedures)
    ├── gcp.md         (280 lines — GCP-specific procedures)
    └── azure.md       (310 lines — Azure-specific procedures)
```

SKILL.md contains: "For AWS deployments, read `references/aws.md`."
Claude loads only the relevant reference. Total context: ~380 lines instead of ~970.

### Pattern: The Bundled Script

When every test run produces Claude writing a similar validation script:

```
docx/
├── SKILL.md
└── scripts/
    ├── validate.py     (structural validation)
    ├── pack.py         (reassemble from XML)
    └── unpack.py       (decompose to XML)
```

The body says: `python scripts/validate.py doc.docx` — one line instead of 30 lines of validation instructions that Claude would write (slightly differently each time) from scratch.

### Pattern: The Agent Spec

For skills that delegate sub-tasks:

```
skill-creator/
├── SKILL.md
└── agents/
    ├── grader.md       (how to evaluate assertions against outputs)
    ├── comparator.md   (how to do blind A/B comparison)
    └── analyzer.md     (how to analyze why one version beat another)
```

Each agent spec is self-contained — a sub-agent can read `grader.md` and execute its task without needing the parent SKILL.md.
