"""Skill listing budget check.

Claude Code lists every model-invocable skill's description in a shared budget of
1% of the context window (each entry capped at 1,536 chars). Over budget, it silently
drops descriptions of the least-used skills. This script estimates where you stand.

Usage: python scripts/budget_check.py [--context 1000000] [--project PATH]
Counts ~/.claude/skills, ~/.claude/plugins and PATH/.claude/skills (default: cwd).
Skills with disable-model-invocation: true, or set to name-only / user-invocable-only /
off in skillOverrides (user or project settings.json), are excluded.
"""
import argparse, glob, json, os, re

CAP = 1536


def overrides(paths):
    out = {}
    for p in paths:
        try:
            out.update(json.load(open(p, encoding="utf-8")).get("skillOverrides", {}))
        except Exception:
            pass
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--context", type=int, default=1_000_000, help="context window in tokens")
    ap.add_argument("--project", default=os.getcwd())
    a = ap.parse_args()
    home = os.path.expanduser("~/.claude")
    ov = overrides([os.path.join(home, "settings.json"),
                    os.path.join(a.project, ".claude", "settings.json"),
                    os.path.join(a.project, ".claude", "settings.local.json")])
    # plugins/marketplaces holds catalog checkouts, not installed plugins: skip it.
    # plugins/cache holds installed plugins: count only those enabled in settings.
    try:
        enabled = [k.split("@")[0] for k, v in json.load(open(os.path.join(home, "settings.json"),
                   encoding="utf-8")).get("enabledPlugins", {}).items() if v]
    except Exception:
        enabled = []
    plug = [f for f in glob.glob(home + "/plugins/**/SKILL.md", recursive=True)
            if "marketplaces" not in f.replace("\\", "/").split("/")
            and ("/cache/" not in f.replace("\\", "/") or any(f"/{e}/" in f.replace("\\", "/") for e in enabled))]
    files = (glob.glob(home + "/skills/*/SKILL.md") + plug
             + glob.glob(os.path.join(a.project, ".claude", "skills", "*", "SKILL.md")))
    seen, rows = set(), []
    for f in files:
        t = open(f, encoding="utf-8", errors="replace").read()
        m = re.search(r"^---(.*?)\n---", t, re.S)
        if not m:
            continue
        fm = m.group(1)
        nm = re.search(r"^name:\s*(.+)$", fm, re.M)
        name = nm.group(1).strip().strip("'\"") if nm else os.path.basename(os.path.dirname(f))
        if "disable-model-invocation: true" in fm or ov.get(name, "on") != "on":
            continue
        d = re.search(r"description:\s*(.*?)(\n[a-z_-]+:|\Z)", fm, re.S)
        w = re.search(r"when_to_use:\s*(.*?)(\n[a-z_-]+:|\Z)", fm, re.S)
        n = len(d.group(1).strip()) if d else 0
        n += len(w.group(1).strip()) if w else 0
        key = (name, f.split("plugins")[0])
        if key in seen:
            continue
        seen.add(key)
        rows.append((min(n, CAP) + len(name) + 4, name))
    used = sum(r[0] for r in rows)
    budget = a.context // 100 * 4  # 1% of context, in chars (~4 chars/token)
    print(f"model-invocable skills: {len(rows)}")
    print(f"listing chars: {used:,}  (~{used // 4:,} tokens)")
    print(f"budget at {a.context:,}-token context: {budget:,} chars (~{a.context // 100:,} tokens)")
    if used > budget:
        print(f"OVER BUDGET by {used - budget:,} chars: least-used skill descriptions are being dropped.")
        print("Fix: skillOverrides 'name-only' for rarely used skills, or disable-model-invocation: true for user-invoked ones.")
    else:
        print(f"OK: {budget - used:,} chars headroom.")
    print("Largest descriptions:")
    for n, name in sorted(rows, reverse=True)[:8]:
        print(f"  {n:5}  {name}")


if __name__ == "__main__":
    main()
