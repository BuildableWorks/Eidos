# Agents

This repository is the home of the **Eidos** standard. `EIDOS.md` is the authoritative definition of the format; everything else supports it.

**Use the skills.** Nine live in the top-level [`skills/`](skills) and ship as a Claude plugin:

- **`eidos`** — author + validate
- **`iterate`** — question one rough idea into a shape, an intent, and its place; writes nothing
- **`format`** — reshape a rough draft into Eidos shape (a collection item, or a free-form top-level doc)
- **`install`** — scaffold a new definition
- **`configure`** — add a collection or flavor, add/rename/retire a custom property, and keep the Framework index current
- **`index`** — rebuild each collection's `index.md` listing
- **`canvas`** — generate an Obsidian `.canvas` map of chosen collections (`connects_to` links as edges)
- **`whoami`** — set who you are (persona + calibration)
- **`migrate`** — move a definition to a new version

Read the relevant skill (and `EIDOS.md`) before creating, scaffolding, migrating, or reviewing any item or top-level doc.

**The framework lives in the definition.** A v4 definition owns its framework — shapes, personas, and property contract — in a hidden `_eidos/` (`shapes/` — collection body shapes, one or more flavors each, including the `Frames` collection's `frame.*` flavors; `personas/` — the response contracts per role; `Framework.md` — the framework's index of top-level docs and collections **and** the property Schema, in a `## Schema` section; and the personal `user.md`). The framing docs (Architecture, Audience, Criteria, Market) are the `Frames` collection, not templates — Eidos v4.1 retired the `templates/` concept, promoting them to a collection whose flavors are their shapes. The canonical defaults live, public and front-facing, at the top level in [`seeds/`](seeds) — `software`, `book`, and `research`, each a complete framework with its own shapes and personas; `install` offers them and installs the chosen one into a definition's `_eidos/`, and the other skills read the framework from the definition they're working in, not from a copy of their own. A definition's `_eidos/` is committed, never gitignored — except the personal `_eidos/user.md`, which the seeded `.gitignore` keeps out. A framework also records its naming convention (`kebab-case` by default, or `TitleCase` or `Title Case`) in `Framework.md`, and the skills locate a definition by its `_eidos/` marker — so the root folder may be named anything (`Blueprint` is just the default).

**Eidos is human-first: facilitate, don't author.** The Framework Owner holds the intent, the scope, and the decisions. Format, supplement, ask clarifying questions, and press on scope; do not generate finished items or set direction.

**Two versions, bumped separately.** Know which one a change touches before you bump anything.

- **The plugin version** (`.claude-plugin/plugin.json` **and** `.claude-plugin/marketplace.json` — both, or updates no-op) moves on **every** shipped release, including skill-only, seed-only, and example-only ones. Add a `CHANGELOG.md` entry naming the plugin version and, on its first line, which standard it ships.
- **The standard version** (`EIDOS.md`'s `**Version:**` header, its Versioning section, and the `eidos_version` in its sample Framework block) moves **only when the text of `EIDOS.md` moves**. When it does, also update: the badge at the top of `README.md`; both version spots in **every** seed (`seeds/*/Framework.md` — the `eidos_version` frontmatter **and** the version note in its `## Schema` block) and both example definitions (`examples/*/_eidos/Framework.md`).

A skill fix bumps the plugin and nothing else — no snapshot, no seed edit, no `eidos_version` change in anyone's definition.

**When the standard's version moves,** copy the current `EIDOS.md` into `versions/` under its full semver name (e.g. `versions/v3.0.0.md`) — snapshot at tag time, from the live file, so there's nothing historical to dig up. Add the hop to `versions/MIGRATIONS.md` (newest first): what moves, what stays, what needs a human decision. A plugin-only release does none of this. Worked hops live there, never in `migrate/SKILL.md`, so the skill stays a fixed size as the standard grows. `EIDOS.md` itself stays the current version. Migrate existing items with the `migrate` skill. After changing `EIDOS.md`, `seeds/`, `versions/`, or `CHANGELOG.md`, run `scripts/sync-skills.sh` and commit the updated skill copies — they are committed (not gitignored), so a git-marketplace install works on sandboxed hosts like Claude Desktop. `scripts/sync-skills.sh --check` verifies they're current; `scripts/package-plugin.sh` refreshes them before zipping.
