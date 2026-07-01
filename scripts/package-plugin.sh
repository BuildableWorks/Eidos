#!/usr/bin/env bash
#
# package-plugin.sh — build a self-contained plugin zip you can upload to Claude
# Desktop (Customize → Plugins → + → upload a custom plugin file) or hand to someone.
#
# The skills already carry committed copies of the canon they need (see scripts/sync-skills.sh),
# so they work installed from a git marketplace — on Claude Code and the sandboxed Claude Desktop
# alike. This script just refreshes those copies and zips the result for the upload-a-file path.
#
# Output: dist/eidos-plugin.zip
#
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

out="dist/eidos-plugin.zip"

# Claude Desktop rejects a plugin whose skill description exceeds 1024 characters, so
# catch it here — before zipping — rather than at upload. Also flags a missing name or
# description. python3 is already a plugin dependency (the eidos-index/eidos-canvas scripts).
echo "1/3  validating skill manifests…"
python3 - <<'PY'
import glob, re, sys

LIMIT = 1024
problems = []

def description_len(fm_lines):
    for i, line in enumerate(fm_lines):
        if not line.startswith("description:"):
            continue
        val = line[len("description:"):].strip()
        if val.startswith(">") or val.startswith("|") or val == "":
            # folded/literal block scalar: gather the indented continuation lines
            buf = []
            for nxt in fm_lines[i + 1:]:
                if nxt.strip() == "" or re.match(r"^\s+\S", nxt):
                    buf.append(nxt.strip())
                else:
                    break
            desc = " ".join(x for x in buf if x)
            return len(desc), True, desc
        desc = val.strip("\"'")
        return len(desc), True, desc
    return 0, False, ""

for path in sorted(glob.glob("skills/*/SKILL.md")):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        problems.append(f"{path}: no YAML frontmatter")
        continue
    fm = m.group(1).split("\n")
    if not any(l.startswith("name:") for l in fm):
        problems.append(f"{path}: missing 'name'")
    n, found, desc = description_len(fm)
    if not found:
        problems.append(f"{path}: missing 'description'")
        continue
    if n > LIMIT:
        problems.append(f"{path}: description is {n} chars (max {LIMIT}) — trim by {n - LIMIT}")
    tags = re.findall(r"<[^>]+>", desc)
    if tags:
        problems.append(f"{path}: description contains XML/angle-bracket tags {tags} — reword (e.g. `spec.full.md` not `<kind>.<flavor>.md`)")

if problems:
    print("  ✗ skill manifest check failed:", file=sys.stderr)
    for p in problems:
        print(f"    - {p}", file=sys.stderr)
    sys.exit(1)
print("  ✓ all skill descriptions valid (≤1024 chars, no XML tags)")
PY

echo "2/3  refreshing the skills' committed copies of the canon…"
./scripts/sync-skills.sh

echo "3/3  zipping → $out …"
mkdir -p dist
rm -f "$out"
zip -rqX "$out" . \
  -x '.git/*' '.git' \
     '.claude/*' \
     '.obsidian/*' \
     'dist/*' \
     '*.DS_Store' '*/.DS_Store'

size=$(du -h "$out" | cut -f1 | tr -d '[:space:]')
echo
echo "✓ built $out ($size)"
echo "  • Claude Desktop: Customize → Plugins → +  →  upload a custom plugin file  →  pick $out"
echo "  • Claude Code:    claude --plugin-dir $out"
