# Agents

This repository is the home of the **Eidos** standard. `EIDOS.md` is the authoritative definition of the format; everything else supports it.

**Use the skills.** Nine live in the top-level [`skills/`](skills) and ship as a Claude plugin:

- **`eidos`** — author + validate
- **`eidos-format`** — reshape a rough draft into Eidos shape (a spec or a Frame, or a free-form top-level doc)
- **`eidos-install`** — scaffold a new registry
- **`eidos-schema`** — add, rename, or retire a custom property
- **`eidos-registry`** — add a collection or flavor and keep the Registry index current
- **`eidos-index`** — rebuild each collection's `index.md` listing
- **`eidos-canvas`** — generate an Obsidian `.canvas` map of chosen collections (`connects_to` links as edges)
- **`eidos-whoami`** — set who you are (persona + calibration)
- **`eidos-migrate`** — move a registry to a new version

Read the relevant skill (and `EIDOS.md`) before creating, scaffolding, migrating, or reviewing any item or top-level doc.

**The form lives in the registry.** A v4 registry owns its shapes, personas, and property contract in a hidden `_eidos/` (`shapes/` — collection body shapes, one or more flavors each, including the `Frames` collection's `frame.*` flavors; `personas/` — the response contracts per role; `Registry.md` — the registry's index of top-level docs and collections **and** the property Schema, in a `## Schema` section; and the personal `user.md`). The framing docs (Architecture, Audience, Criteria, Market) are the `Frames` collection, not templates — Eidos v4.1 retired the `templates/` concept, promoting them to a collection whose flavors are their shapes. The canonical defaults live, public and front-facing, at the top level in [`seed/`](seed) (personas included); `eidos-install` installs it into a registry's `_eidos/`, and the other skills read the form from the registry they're working in, not from a copy of their own. A registry's `_eidos/` is committed, never gitignored — except the personal `_eidos/user.md`, which the seeded `.gitignore` keeps out. A registry also records its naming convention (Title Case, TitleCase, or kebab-case) in `Registry.md`, and the skills locate a registry by its `_eidos/` marker — so the root folder may be named anything (`Blueprint` is just the default).

**Eidos is human-first: facilitate, don't author.** The registry owner holds the intent, the scope, and the decisions. Format, supplement, ask clarifying questions, and press on scope; do not generate finished items or set direction.

**Keep the version in sync.** `EIDOS.md` always holds the current version (its `**Version:**` header and Versioning section). When it changes, update: the badge at the top of `README.md` (e.g. `[Eidos v3.0.0](EIDOS.md)`); the `version` in `.claude-plugin/plugin.json`; both version spots in the canonical seed (`seed/Registry.md` — the `eidos_version` frontmatter **and** the version note in its `## Schema` block) and the example registry (`example/Blueprint/_eidos/Registry.md`); and `CHANGELOG.md`.

**On each release (tag),** copy the current `EIDOS.md` into `versions/` under its full semver name (e.g. `versions/v3.0.0.md`) — snapshot at tag time, from the live file, so there's nothing historical to dig up. `EIDOS.md` itself stays the current version. Migrate existing items with the `eidos-migrate` skill. After changing `EIDOS.md`, `seed/`, `versions/`, or `CHANGELOG.md`, run `scripts/sync-skills.sh` and commit the updated skill copies — they are committed (not gitignored), so a git-marketplace install works on sandboxed hosts like Claude Desktop. `scripts/sync-skills.sh --check` verifies they're current; `scripts/package-plugin.sh` refreshes them before zipping.
