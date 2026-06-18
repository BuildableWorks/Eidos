#!/usr/bin/env bash
#
# sync-skills.sh — copy the standard's assets into the skills so each one is
# self-contained: it works installed as the plugin, or dropped on its own into a
# project's (or ~/) .claude/skills/.
#
# Dirty but simple: it COPIES, it does not symlink. The copies are gitignored — the
# canonical files live at the repo root and ship with the plugin (the skills read
# them from ${CLAUDE_PLUGIN_ROOT} when installed). Run this after cloning, or before
# packaging a skill for standalone use. Re-run whenever EIDOS.md, templates/,
# versions/, or CHANGELOG.md changes.
#
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# eidos authors specs and product docs from the templates, so it carries a copy
# to stay self-contained (e.g. Claude Desktop, which sandboxes each skill to its
# own folder). In Claude Code it reads ${CLAUDE_PLUGIN_ROOT}/templates instead.
rm -rf "skills/eidos/templates"
cp -R "templates" "skills/eidos/templates"

# eidos-init scaffolds a new registry from the templates, following the contract.
rm -rf "skills/eidos-init/templates"
cp -R "templates" "skills/eidos-init/templates"
cp "EIDOS.md" "skills/eidos-init/EIDOS.md"

# eidos-migrate diffs prior versions and reads the changelog's migration notes,
# so it carries the full version history to work when installed anywhere.
rm -rf "skills/eidos-migrate/versions"
cp -R "versions" "skills/eidos-migrate/versions"
cp "CHANGELOG.md" "skills/eidos-migrate/CHANGELOG.md"
cp "EIDOS.md" "skills/eidos-migrate/EIDOS.md"

echo "✓ copied templates -> eidos + eidos-init, versions + CHANGELOG -> eidos-migrate, EIDOS.md -> init + migrate"
