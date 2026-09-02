# Agents

This repository is the home of the **Eidos** standard. `EIDOS.md` is the authoritative definition of the format; everything else supports it.

**Use the skills.** Nine live in the top-level [`skills/`](skills) and ship as a Claude plugin:

- **`eidos`** — author + validate
- **`iterate`** — question one rough idea into a shape, an intent, and its place; writes nothing
- **`format`** — reshape a rough draft into Eidos shape (a collection blueprint, or a free-form top-level doc)
- **`install`** — scaffold a new folder
- **`configure`** — add a collection or flavor, add/rename/retire a custom property, and keep the Framework index current
- **`index`** — rebuild each collection's `index.md` listing
- **`canvas`** — generate an Obsidian `.canvas` map of chosen collections (`connects_to` links as edges)
- **`whoami`** — set who you are (role + calibration)
- **`migrate`** — move an Eidos folder to a new version

Read the relevant skill (and `EIDOS.md`) before creating, scaffolding, migrating, or reviewing any blueprint or top-level doc.

**The framework lives in the folder.** A v4 folder owns its framework — shapes, roles, and property contract — in a hidden `_eidos/` (`shapes/` — collection body shapes, one or more flavors each, including the `Frames` collection's `frame.*` flavors; `roles/` — the response contracts per role; `Framework.md` — the framework's index of top-level docs and collections **and** the property Schema, in a `## Schema` section; and the personal `me.md`). The framing docs (Architecture, Audience, Criteria, Market) are the `Frames` collection, not templates — Eidos v4.1 retired the `templates/` concept, promoting them to a collection whose flavors are their shapes. The canonical defaults live, public and front-facing, at the top level in [`seeds/`](seeds) — `software`, `book`, and `research`, each a complete framework with its own shapes and roles; `install` offers them and installs the chosen one into a root's `_eidos/`, and the other skills read the framework from the folder they're working in, not from a copy of their own. A root's `_eidos/` is committed, never gitignored — except the personal `_eidos/me.md`, which the seeded `.gitignore` keeps out. A framework also records its naming convention (`kebab-case` by default, or `TitleCase` or `Title Case`) in `Framework.md`, and the skills locate an Eidos folder by its `_eidos/` marker — so the root folder may be named anything (`Blueprints` is just the default).

**Eidos is human-first: facilitate, don't author.** The Framework Owner holds the intent, the scope, and the decisions. Format, supplement, ask clarifying questions, and press on scope; do not generate finished blueprints or set direction.

**Two versions, bumped separately.** Know which one a change touches before you bump anything.

- **The plugin version** (`.claude-plugin/plugin.json` **and** `.claude-plugin/marketplace.json` — both, or updates no-op) moves on **every** shipped release, including skill-only and seed-only ones. Add a `CHANGELOG.md` entry naming the plugin version and, on its first line, which standard it ships.
- **The standard version** (`EIDOS.md`'s `**Version:**` header, its Versioning section, and the `eidos_version` in its sample Framework block) moves **only when the text of `EIDOS.md` moves**. When it does, also update: the badge at the top of `README.md`, and both version spots in **every** seed (`seeds/*/Framework.md` — the `eidos_version` frontmatter **and** the version note in its `## Schema` block).

A skill fix bumps the plugin and nothing else — no snapshot, no seed edit, no `eidos_version` change in anyone's folder.

**Tag every shipped release `vX.Y.Z`, on the plugin version, lightweight, on the release's final commit.** Match the existing tags: `git tag v4.5.0 && git push origin v4.5.0`, no `-a`. When a release spans several commits, tag the finished state, not the first commit whose subject happens to say "Release" — the tag has to name a tree someone could actually install.

**Settled, don't re-litigate: the tags stay, and there is no second `standard/vX.Y.Z` namespace.** The two version lines already have two different release artifacts, and they are not interchangeable:

- **The standard's** artifact is a **file** — `versions/vX.Y.Z.md`. It answers "what did the contract say?", and you can read it without checking anything out. A tag would be strictly worse at this.
- **The plugin's** artifact is a **tree** — the `vX.Y.Z` tag. It answers "what did the skills and seeds look like when someone installed this?", which no snapshot carries. It is also what makes `git diff v4.4.0..v4.5.0` possible, what a GitHub Release attaches to, and what makes the `gitCommitSha` in a user's `installed_plugins.json` legible.

**Tags are not how an install detects an update**, so never reach for one to fix an update problem. Claude Code clones the repo as a marketplace, tracks its **default branch**, and compares the `version` in `.claude-plugin/marketplace.json` against the installed version in `~/.claude/plugins/installed_plugins.json`. A release that forgets that field is a silent no-op for every existing install, which is why the plugin version has to move in **both** manifests on every release.

**When the standard's version moves,** copy the current `EIDOS.md` into `versions/` under its full semver name (e.g. `versions/v3.0.0.md`) — snapshot at tag time, from the live file, so there's nothing historical to dig up. Add the hop to `versions/MIGRATIONS.md` (newest first): what moves, what stays, what needs a human decision. A plugin-only release does none of this. Worked hops live there, never in `migrate/SKILL.md`, so the skill stays a fixed size as the standard grows. `EIDOS.md` itself stays the current version. Migrate existing blueprints with the `migrate` skill. After changing `EIDOS.md`, `seeds/`, `versions/`, or `CHANGELOG.md`, run `scripts/sync-skills.sh` and commit the updated skill copies — they are committed (not gitignored), so a git-marketplace install works on sandboxed hosts like Claude Desktop. `scripts/sync-skills.sh --check` verifies they're current; `scripts/package-plugin.sh` refreshes them before zipping.
