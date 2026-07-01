#!/usr/bin/env bash
#
# sync-skills.sh — copy the top-level canon into the skills that need it.
#
# The top-level files (EIDOS.md, seed/, versions/, CHANGELOG.md) are the source of
# truth and the public review surface. A distributed skill can't reach them: Claude Desktop
# sandboxes each skill to its own folder, and a git-marketplace install ("/plugin marketplace
# add …") ships only what is committed. So each skill carries a COMMITTED copy of what it needs,
# kept in sync by this script — duplication is the price of the sandbox.
#
# Run after changing EIDOS.md, seed/, versions/, or CHANGELOG.md, then commit the
# updated copies. Pass --check to verify the copies are current WITHOUT writing (for CI or a
# pre-commit hook); it exits non-zero if anything is stale.
#
# Skills that read the user's registry _eidos/ at runtime (eidos-format, eidos-schema,
# eidos-registry, eidos-index, eidos-canvas, eidos-whoami) carry nothing and are not touched.
#
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

check=0
[ "${1:-}" = "--check" ] && check=1
stale=0

# sync_one <src> <dest>
sync_one() {
  local src="$1" dest="$2"
  if [ "$check" -eq 1 ]; then
    if ! diff -rq "$src" "$dest" >/dev/null 2>&1; then
      echo "  ✗ stale: $dest"
      stale=1
    fi
  else
    rm -rf "$dest"
    cp -R "$src" "$dest"
    echo "  $src → $dest"
  fi
}

# eidos — the ruleset
sync_one "EIDOS.md"      "skills/eidos/EIDOS.md"

# eidos-install — the canonical seed it installs (personas live inside it now)
sync_one "seed"          "skills/eidos-install/seed"

# eidos-migrate — the seed plus the full version history, to diff and upgrade
sync_one "seed"          "skills/eidos-migrate/seed"
sync_one "versions"      "skills/eidos-migrate/versions"
sync_one "CHANGELOG.md"  "skills/eidos-migrate/CHANGELOG.md"
sync_one "EIDOS.md"      "skills/eidos-migrate/EIDOS.md"

# The seed's .gitignore ignores user.md; the shipped blank template must still travel with the
# committed skill copies, so keep those two tracked past the ignore.
if [ "$check" -eq 0 ]; then
  git add -f skills/eidos-install/seed/user.md skills/eidos-migrate/seed/user.md 2>/dev/null || true
fi

if [ "$check" -eq 1 ]; then
  if [ "$stale" -eq 0 ]; then
    echo "✓ skill copies are in sync with the top-level canon"
  else
    echo "✗ skill copies are stale — run: scripts/sync-skills.sh" >&2
    exit 1
  fi
else
  echo "✓ synced the canon into eidos, eidos-install, and eidos-migrate"
fi
