# Skill Quality Evaluation Checklist

Use this checklist during Phase 5 (Quality Check) before presenting any skill.
Every criterion includes what to check and how to fix it if it fails.

---

## Tier 1: Structural Validity

These are hard requirements. A skill failing any of these is broken.

### 1.1 Valid YAML Frontmatter
- **Check:** File starts with `---`, contains `name` and `description` fields, ends with `---`
- **Fix:** Add missing fields. `name` must be kebab-case. `description` must be a quoted string.

### 1.2 Description Length
- **Check:** Description is 60–120 words
- **Fix:** Under 60 → add trigger inventory and hedged cases. Over 120 → merge redundant phrases, tighten the exclusion fence.

### 1.3 Trigger Inventory Present
- **Check:** Description contains specific keywords, file types, or user phrases that should activate the skill
- **Fix:** List 5–8 concrete trigger phrases. Include both formal ("generate a report") and casual ("make me a doc") variants.

### 1.4 Exclusion Fence Present
- **Check:** Description contains "Do NOT use for..." clause
- **Fix:** Identify 2–3 adjacent skills or task types that share keywords but need different handling. Add them explicitly.

### 1.5 Body Length
- **Check:** SKILL.md body (excluding frontmatter) is under 500 lines
- **Fix:** Extract domain branches to `references/`. Remove redundant explanations. Compress code examples to essential patterns only.

### 1.6 File References Resolve
- **Check:** Every file mentioned in the body (scripts, references, assets) exists in the directory structure
- **Fix:** Create the missing files or remove the dangling references.

---

## Tier 2: Instruction Quality

These determine whether the skill produces good outputs when triggered.

### 2.1 Domain Primer Exists
- **Check:** Body opens with 1–3 sentences of domain context (not a restatement of the description)
- **Fix:** Write a compact mental model — one insight that reframes how Claude should think about the domain. "A .docx file is a ZIP archive containing XML files" changes Claude's entire approach in one sentence.

### 2.2 Decision Router Exists
- **Check:** If the skill has 2+ task paths, a quick-reference table maps task types to approaches
- **Fix:** Add a `## Quick Reference` table with columns `| Task | Approach |`. Each row should point to a section in the body or a reference file.

### 2.3 Imperative Voice
- **Check:** Procedure steps use imperative form ("Set page size" not "You should set page size" or "The page size can be set")
- **Fix:** Rewrite passive/conditional phrasing to direct imperatives. "Consider validating" → "Validate the output."

### 2.4 Concrete Code Templates
- **Check:** Every code-generating procedure includes a copy-paste-ready template with real values, not a prose description of what code should look like
- **Fix:** Write a working code snippet that Claude can adapt. Include actual values (not `<placeholder>`), actual imports, actual configuration.

### 2.5 Constraints Have Explanations
- **Check:** Every MUST, NEVER, ALWAYS, or CRITICAL rule has a "because" or "this prevents" clause explaining the failure mode
- **Fix:** Append "— [failure mode]" to each constraint. "Never use `\n`" → "Never use `\n` — use separate Paragraph elements because newline characters produce invalid XML in this context."

### 2.6 No Naked Shouty Rules
- **Check:** No all-caps MUST/NEVER/ALWAYS exists without an accompanying rationale
- **Fix:** Reframe as an explanation. "ALWAYS SET PAGE SIZE" → "Set page size explicitly — docx-js defaults to A4, which produces unexpected formatting for US documents."

### 2.7 Input-Output Examples
- **Check:** Transformative skills (anything that takes input and produces structured output) include at least one concrete `Input → Output` example pair
- **Fix:** Write one realistic example showing exactly what goes in and what comes out.

---

## Tier 3: Robustness

These prevent failures in production use.

### 3.1 Validation Steps Exist
- **Check:** Every procedure block includes a step for verifying the output is correct
- **Fix:** Add a validation command (`python scripts/validate.py output`), a structural check ("open the file and verify..."), or assertion criteria.

### 3.2 Recovery Paths Exist
- **Check:** Every procedure that can fail includes a "if this fails, then..." clause
- **Fix:** For each failure point, add: what failure looks like, what caused it, and how to recover. "If validation fails, unpack, fix the XML, and repack."

### 3.3 Deterministic Ops Are Scripts
- **Check:** Any deterministic operation with >5 steps or involving structured data parsing is a bundled script, not prose instructions
- **Fix:** Write the script, place it in `scripts/`, and reference it from the body. "Run `python scripts/validate.py doc.docx`" is more reliable than 15 lines of validation instructions.

### 3.4 Constraint Catalog Exists
- **Check:** A dedicated "Critical Rules" or "Known Pitfalls" section exists near the end of the body (or relevant procedure blocks)
- **Fix:** Create the section. Populate with at least 3 named rules from domain knowledge. Each rule needs: name, instruction, and failure-mode explanation.

### 3.5 Anti-Patterns Are Explained
- **Check:** Anti-patterns include both the wrong way AND the right way, with an explanation of why the wrong way fails
- **Fix:** Use the pattern: `❌ WRONG: [bad code/approach]` / `✅ CORRECT: [good code/approach]` / `[Why the wrong way fails]`

---

## Tier 4: Trigger Reliability

These ensure the skill activates when it should and doesn't when it shouldn't.

### 4.1 Description Is Pushy
- **Check:** The description actively advocates for its own use rather than passively listing capabilities. It should feel like it's saying "use me for this!" not "I can do this."
- **Fix:** Add active language: "Use this skill whenever...", "Also trigger when...", "Make sure to use this skill even if..."

### 4.2 Hedged Cases Covered
- **Check:** Description covers cases where the user needs the skill but uses different terminology or doesn't name it explicitly
- **Fix:** Think of 3 ways a user might describe the task without using the skill's keywords. Add those phrasings.

### 4.3 Near-Miss Non-Triggers Tested
- **Check:** At least 2 should-not-trigger prompts exist that share keywords with the skill
- **Fix:** Identify adjacent tasks that use similar terms. Write prompts for them. Verify the exclusion fence would prevent triggering.

### 4.4 Test Prompts Are Substantive
- **Check:** Test prompts are complex enough that Claude would benefit from consulting a skill (simple queries like "read this file" won't trigger any skill)
- **Fix:** Add realistic detail: file names, personal context, multi-step requirements, casual phrasing.

### 4.5 Test Prompt Diversity
- **Check:** Test prompts cover at least 2 distinct task paths from the decision router
- **Fix:** Ensure each core task path has at least one test prompt targeting it.

---

## Tier 5: Maintainability

These determine whether the skill remains effective as it evolves.

### 5.1 No Section Exceeds 300 Lines
- **Check:** No single file in the skill exceeds 300 lines without progressive disclosure (reference files for sub-sections)
- **Fix:** Extract the longest section into a reference file. Add a pointer from the body: "For AWS-specific procedures, read `references/aws.md`."

### 5.2 Clear Pointers to Resources
- **Check:** Every reference file, script, and asset has a clear instruction in the body about WHEN to read/use it
- **Fix:** Add a "Reference Files" section at the bottom listing each resource with its purpose and trigger condition.

### 5.3 Scripts Are Independently Testable
- **Check:** Bundled scripts can be run standalone with test inputs (not dependent on Claude's runtime state)
- **Fix:** Add argument parsing and usage messages. Scripts should work from the command line without context.

### 5.4 Self-Contained Understanding
- **Check:** A different Claude instance could read the skill and execute it without needing the original conversation or context
- **Fix:** Remove references to "as we discussed" or assumptions about prior context. Every decision and pattern should be explained within the skill.

---

## Scoring

Count passing criteria per tier:

| Tier | Pass Rate | Assessment |
|------|-----------|------------|
| Tier 1 (6 criteria) | 6/6 required | Below 6/6 = broken, do not ship |
| Tier 2 (7 criteria) | 6/7+ = good | Below 5/7 = major quality issues |
| Tier 3 (5 criteria) | 4/5+ = good | Below 3/5 = fragile in production |
| Tier 4 (5 criteria) | 4/5+ = good | Below 3/5 = unreliable triggering |
| Tier 5 (4 criteria) | 3/4+ = good | Below 2/4 = maintenance burden |

**Ship threshold:** Tier 1 = 6/6 AND all other tiers ≥ "good" rating.
