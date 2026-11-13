#!/usr/bin/env python3
"""
Quick validation script for skills - minimal version
"""

import sys
import os
import re
import yaml
from pathlib import Path

def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)

    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # Read and validate frontmatter
    content = skill_md.read_text()
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    # Parse YAML frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    # Define allowed properties
    ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility',
                          # Claude Code-only keys (claude.ai / API upload rejects these)
                          'disable-model-invocation', 'user-invocable', 'when_to_use', 'argument-hint',
                          'model', 'disallowed-tools', 'hooks'}

    # Check for unexpected properties (excluding nested keys under metadata)
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, (
            f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. "
            f"Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )

    # Check required fields
    if 'name' not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    # Extract name for validation
    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        # Check naming convention (kebab-case: lowercase with hyphens)
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"Name '{name}' should be kebab-case (lowercase letters, digits, and hyphens only)"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
        # Check name length (max 64 characters per spec)
        if len(name) > 64:
            return False, f"Name is too long ({len(name)} characters). Maximum is 64 characters."

    # Extract and validate description
    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        # Check for angle brackets
        if '<' in description or '>' in description:
            return False, "Description cannot contain angle brackets (< or >)"
        # Check description length (max 1024 characters per spec)
        if len(description) > 1024:
            return False, f"Description is too long ({len(description)} characters). Maximum is 1024 characters."

    # Validate compatibility field if present (optional)
    compatibility = frontmatter.get('compatibility', '')
    if compatibility:
        if not isinstance(compatibility, str):
            return False, f"Compatibility must be a string, got {type(compatibility).__name__}"
        if len(compatibility) > 500:
            return False, f"Compatibility is too long ({len(compatibility)} characters). Maximum is 500 characters."

    for w in lint_warnings(skill_path, content, description):
        print(f"WARN: {w}")
    return True, "Skill is valid!"


def lint_warnings(skill_path, content, description):
    """Quality lint: never fails validation, prints what to fix."""
    skill_path = Path(skill_path)
    warns = []
    body = content.split('---', 2)[2] if content.count('---') >= 2 else content
    lines = body.split('\n')
    if len(lines) > 500:
        warns.append(f"body is {len(lines)} lines (target <= 500); move detail into references/")
    if len(body) // 4 > 5000:
        warns.append(f"body is ~{len(body) // 4} tokens; compaction keeps only the first 5,000, so put load-bearing rules first")
    d = description.lower()
    if not re.search(r'\buse (this skill )?(when|whenever)|\btrigger', d):
        warns.append("description has no trigger phrase ('Use when ...')")
    if 'do not' not in d and 'not for' not in d and "don't" not in d:
        warns.append("description has no exclusion ('Do NOT use for ...')")
    if re.search(r'^description:\s*[^\'"\n>|][^\n]*:\s', content, re.M):
        warns.append("unquoted ': ' inside the description line can silently blank YAML metadata; quote it or use '>'")
    # referenced files exist, with exact case
    for ref in set(re.findall(r'`((?:references|scripts|agents|assets)/[^`\s]+)`', body)):
        target = skill_path / ref
        if not target.exists() or target.name not in {p.name for p in target.parent.glob('*')}:
            warns.append(f"referenced file missing or wrong case: {ref}")
    # hard rules without a reason
    bare = [l.strip() for l in lines if re.search(r'\b(NEVER|MUST|ALWAYS)\b', l)
            and not re.search(r'because|—|-- |\bso\b|\(|:', l)]
    if bare:
        warns.append(f"{len(bare)} NEVER/MUST/ALWAYS line(s) without a reason, e.g. '{bare[0][:70]}'")
    if not re.search(r'^#+ .*(verif|validat|check)', body, re.I | re.M):
        warns.append("no verification section heading (verify / validate / check)")
    if not re.search(r'^#+ .*cost', body, re.I | re.M):
        warns.append("no '## Cost & speed' block")
    if not re.search(r'^#+ .*runs on', body, re.I | re.M):
        warns.append("no '## Runs on' footer (see references/surfaces.md)")
    return warns

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)
    
    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)