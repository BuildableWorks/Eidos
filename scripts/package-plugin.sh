#!/usr/bin/env bash
#
# package-plugin.sh — build a self-contained plugin zip you can upload to Claude
# Desktop (Customize → Plugins → + → upload a custom plugin file) or hand to someone.
#
# It does the two things by hand are easy to get wrong:
#   1. vendors each skill's assets INTO its own folder (Desktop sandboxes a skill to
#      its folder — it can't read the plugin root), via scripts/sync-skills.sh; and
#   2. zips the plugin with the right things left out (.git, local-only dirs, build
#      output, OS noise).
#
# Output: dist/eidos-plugin.zip
#
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

out="dist/eidos-plugin.zip"

echo "1/2  vendoring assets into the skills (self-contained for Claude Desktop)…"
./scripts/sync-skills.sh

echo "2/2  zipping → $out …"
mkdir -p dist
rm -f "$out"
zip -rqX "$out" . \
  -x '.git/*' '.git' \
     '.claude/*' \
     '.obsidian/*' \
     '.eidos/*' \
     'dist/*' \
     '*.DS_Store' '*/.DS_Store'

size=$(du -h "$out" | cut -f1 | tr -d '[:space:]')
echo
echo "✓ built $out ($size)"
echo "  • Claude Desktop: Customize → Plugins → +  →  upload a custom plugin file  →  pick $out"
echo "  • Claude Code:    claude --plugin-dir $out"
