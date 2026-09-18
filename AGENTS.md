# Agents

This repository is the home of the **Eidos** standard. `EIDOS.md` is the authoritative definition of the format; everything else supports it.

**Use the skills.** Eight live in the top-level [`skills/`](skills) and ship as a Claude plugin:

- **`eidos`** — author + validate
- **`iterate`** — question one rough idea into a shape, an intent, and its place; writes nothing
- **`format`** — reshape a rough draft into Eidos form (a collection blueprint, or a free-form top-level doc)
- **`install`** — scaffold a new folder
- **`configure`** — add a collection or variant, add/rename/retire a custom property or a Vocabulary term, snapshot the root as a version when asked, and keep the Framework index current
- **`index`** — rebuild the index in the framework document
- **`whoami`** — set who you are (role + calibration)
- **`migrate`** — move a root to a new version

Read the relevant skill (and `EIDOS.md`) before creating, scaffolding, migrating, or reviewing any blueprint or top-level doc.

**The `eidos` CLI is not in this repository.** It is The Virtual Panda's product (npm package `eidosmd`, source at [gitlab.com/the-virtual-panda/eidosmd](https://gitlab.com/the-virtual-panda/eidosmd) beside the eidosmd.com site) and implements the mechanical half of the standard: `init`, `new`, `check`, `index`, `list`, `show`, `framework`, `whoami`, `browser`, and `instructions`. It vendors `EIDOS.md` and `seeds/` from a checkout of this repository with its own sync script, so a release of the standard here is followed by a sync and a release there. This repository owns the standard, the seeds, and the plugin; a change to how the tool behaves belongs over there, and a change to what conforms belongs here.

**The framework lives in the folder.** A v4 folder owns its framework — templates, roles, and property contract — in a hidden `.eidos/` (`templates/` — collection body templates, one or more variants each, including the `Frames` collection's `frame.*` variants; `roles/` — the response contracts per role; `Framework.yaml` — the framework document: the index of top-level docs and collections, the Properties table under `properties`, the root's terms under `vocabulary`, the root's own versions, snapshots taken on purpose, as named commits under `versions`, **and** the generated `index`; `plugins/<name>/` — whatever a tool keeps in the framework, the standard's reading none of it, with `local.yaml` inside it the one file that is one person's on one machine; and the personal `me.md`). The framing docs (Architecture, Audience, Criteria, Market) are the `Frames` collection, a collection like any other whose variants are its templates; 5.0.0 reuses the word `templates/` that 4.0.0 had used for one-of-each top-level scaffolds, a concept retired in 4.1.0. The canonical defaults live, public and front-facing, at the top level in [`seeds/`](seeds) — `software`, `book`, and `research`, each a complete framework with its own templates and roles; `install` offers them and installs the chosen one into a root's `.eidos/`, and the other skills read the framework from the root they're working in, not from a copy of their own. A root's `.eidos/` is committed, never gitignored — except the personal `.eidos/me.md` and any tool's `plugins/<name>/local.yaml`, which the seeded `.gitignore` keeps out (`me.md` and the one pattern `plugins/*/local.yaml`, so no tool writes a `.gitignore` of its own). A framework also records its naming convention (`kebab-case` by default, or `TitleCase` or `Title Case`) in `Framework.yaml`, and the skills locate a root by its `.eidos/` marker — so the root folder may be named anything (`Blueprints` is just the default).

**Eidos is human-first: facilitate, don't author.** The Framework Owner holds the intent, the scope, and the decisions. Format, supplement, ask clarifying questions, and press on scope; do not generate finished blueprints or set direction.

**Two versions here, bumped separately.** Know which one a change touches before you bump anything. (The CLI has a third, in its own repository, and names the standard it carries.)

- **The plugin version** (`.claude-plugin/plugin.json` **and** `.claude-plugin/marketplace.json` — both, or updates no-op) moves on **every** shipped release, including skill-only and seed-only ones. Add a `CHANGELOG.md` entry naming the plugin version and, on its first line, which standard it ships.
- **The standard version** (`EIDOS.md`'s `**Version:**` header, its Versioning section, and the `eidos_version` in its sample Framework block) moves **only when the text of `EIDOS.md` moves**. When it does, also update: the badge at the top of `README.md`, and both version spots in **every** seed (`seeds/*/Framework.yaml` — its `eidos_version` **and** the version note in the comment on its `properties.core` block).

A skill fix bumps the plugin and nothing else — no snapshot, no seed edit, no `eidos_version` change in anyone's folder.

**Tag every shipped release `vX.Y.Z`, on the plugin version, lightweight, on the release's final commit.** Match the existing tags: `git tag v4.5.0 && git push origin v4.5.0`, no `-a`. When a release spans several commits, tag the finished state, not the first commit whose subject happens to say "Release" — the tag has to name a tree someone could actually install.

**Settled, don't re-litigate: the tags stay, and there is no second `standard/vX.Y.Z` namespace.** The two version lines already have two different release artifacts, and they are not interchangeable:

- **The standard's** artifact is a **file** — `versions/vX.Y.Z.md`. It answers "what did the contract say?", and you can read it without checking anything out. A tag would be strictly worse at this.
- **The plugin's** artifact is a **tree** — the `vX.Y.Z` tag. It answers "what did the skills and seeds look like when someone installed this?", which no snapshot carries. It is also what makes `git diff v4.4.0..v4.5.0` possible, what a GitHub Release attaches to, and what makes the `gitCommitSha` in a user's `installed_plugins.json` legible.

**Tags are not how an install detects an update**, so never reach for one to fix an update problem. Claude Code clones the repo as a marketplace, tracks its **default branch**, and compares the `version` in `.claude-plugin/marketplace.json` against the installed version in `~/.claude/plugins/installed_plugins.json`. A release that forgets that field is a silent no-op for every existing install, which is why the plugin version has to move in **both** manifests on every release.

**When the standard's version moves,** copy the current `EIDOS.md` into `versions/` under its full semver name (e.g. `versions/v3.0.0.md`) — snapshot at tag time, from the live file, so there's nothing historical to dig up. Add the hop to `versions/MIGRATIONS.md` (newest first): what moves, what stays, what needs a human decision. A plugin-only release does none of this. Worked hops live there, never in `migrate/SKILL.md`, so the skill stays a fixed size as the standard grows. `EIDOS.md` itself stays the current version. Migrate existing blueprints with the `migrate` skill. After changing `EIDOS.md`, `seeds/`, `versions/`, or `CHANGELOG.md`, run `scripts/sync-skills.sh` and commit the updated skill copies — they are committed (not gitignored), so a git-marketplace install works on sandboxed hosts like Claude Desktop. `scripts/sync-skills.sh --check` verifies they're current; `scripts/package-plugin.sh` refreshes them before zipping.
