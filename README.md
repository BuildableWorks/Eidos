# Eidos

_**εἶδος** (eidos), Greek — the form or essence of a thing: the look that makes it what it is. Plato's eternal Form; Aristotle's essence behind the matter._

> **[Eidos v3.1.0](EIDOS.md)** — the full standard.

A markdown spec registry for defining what a product _is_. One file completely defines one unit of a product, true whether or not the thing has been built. Specs live as plain `.md` files next to your code. No SaaS. No lock-in. No hidden state.

A **spec** captures **state and intent, not work**. Tasks describe work and die when the work ships; a spec describes the product and stays accurate across its whole life: drafted, built, deprecated.

Eidos is **human-first**. A product owner holds the intent, the scope, and the decisions. An agent — via the `eidos` skill — facilitates: it formats, supplements, asks clarifying questions, and presses on scope. It does **not** author specs for you. A spec no one thought through is worse than none.

## Why

Product knowledge rots in tickets, wikis, and people's heads. Eidos keeps the authoritative answer to "what is this thing" as version-controlled markdown, reviewed in PRs alongside the code it describes. Humans and coding agents read the same source of truth.

## How it works

Drop a `Blueprint/` folder into any repo:

```txt
Blueprint/
  .eidos/             # the form layer: shapes, Schema, Registry (hidden)
  Architecture.md     # overarching system shape
  Audience.md         # who it serves and how each type interacts
  Criteria.md         # budget, scope objectives, timeline
  Market.md           # where it sits, how it differs, how it earns
  Domains.md          # the domains as a navigable map of the specs; present by default
  Specs/
    <Domain>/
      <Title>.md      # one spec per unit, grouped by domain
```

- **Product docs** are four files — one of each — that frame the whole product, plus any free-form top-level docs you add yourself (a Roadmap, a Vision).
- **Specs** are the many, one per unit, grouped into `<Domain>/` folders. Every spec shares one shape — Intent, Behaviors & Acceptance Criteria, Out of Scope, and the rest, used as they apply; the frontmatter is the firm part, the body is guidance you keep what you need of.
- **The form layer** — a hidden `.eidos/` holds the registry's shapes (the body template for each kind of doc) and its `Schema.md` (the property contract: an Eidos-canonical baseline plus any custom properties you add). It's seeded with an opinionated default — public and browsable in [`standard-seed/`](standard-seed) — that you can extend without forking the standard, and it's committed alongside the specs, not gitignored.
- Human-facing names follow a **naming convention you pick at init** — Title Case (default), TitleCase, or kebab-case — so the tree reads like a table of contents (and scripts cleanly if you want it to); the `id` inside each spec — lowercase words joined by hyphens — is its permanent reference.

The full rules are in **[EIDOS.md](EIDOS.md)**. See **[`example/`](example/)** for a filled-in product definition you can pattern-match against.

## Quick start

Use Eidos on your own project:

1. **Get the skills. (optional)** Install `eidos` skills to help follow the spec, but it's easy enough to follow without it — see [Installing the skills](#installing-the-skills).
2. **Initialize.** Run `eidos-init`: it installs the `.eidos/` form layer and scaffolds a `Blueprint/`, following the current `EIDOS.md` — or copy the example and modify its contents.
3. **Fill the product docs.** Architecture, Audience, Criteria, Market — prose, loose, point-in-time; fill what's known, leave the rest. Describe each domain in `Domains.md` as specs accrue.
4. **Author specs.** One file per unit under `Specs/<Domain>/`, named for its title in Title Case (`Magic Link Sign-In.md`). Each spec's frontmatter is generated from the registry's Schema; lead with Intent and Behaviors & Acceptance Criteria; press hard on **Out of Scope** — that's where scope is held. The `eidos` skill facilitates; it does not author for you.
5. **Commit it.** Specs are the product definition — `.eidos/` form layer and all. Review them in PRs alongside code. Eidos relies on git history (`created`/`modified` dates, the Decisions log, scope drift), so do **not** gitignore them.

Doing Eidos needs the skills and a seeded registry: `EIDOS.md` gives the method, but the form a registry uses lives in its `.eidos/`. See [`example/`](example/) for a filled-in registry to pattern-match against.

## Installing the skills

Eidos ships as a **Claude plugin** bundling six skills:

- **`eidos`** — author + validate
- **`eidos-format`** — reshape a rough draft into Eidos shape (a spec, a product doc, or a free-form top-level doc)
- **`eidos-init`** — scaffold a new registry (installs the `.eidos/` form layer)
- **`eidos-property`** — add, rename, or retire a custom property and backfill the specs
- **`eidos-domains`** — regenerate `Domains.md` as a navigation map of the specs
- **`eidos-migrate`** — move specs to a new version

Most skills read from your registry at runtime and need nothing of the standard: `eidos-format`, `eidos-property`, and `eidos-domains`. The other three carry a **committed copy** of just what they need — `eidos` (the `EIDOS.md` ruleset), `eidos-init` (the canonical [`standard-seed/`](standard-seed)), and `eidos-migrate` (the version history) — so each skill is self-contained wherever it's installed. `scripts/sync-skills.sh` keeps those copies in sync with the top-level sources.

### Why the skills carry copies of the standard

You'll notice the same files in two places — `EIDOS.md`, `standard-seed/`, and `versions/` at the repo root, and again inside a few of the skill folders. That duplication is deliberate, not an oversight.

The top-level copies are the **source of truth** and the public review surface: one place to read, diff, and propose changes to what Eidos ships. But a skill often can't reach them once it's installed:

- **Claude Desktop sandboxes each skill to its own folder** — it can't read sibling files at the plugin root.
- **A git-marketplace install ships only what's committed** — anything gitignored never arrives.

So a skill that needs part of the standard has to _carry_ it, committed, to keep working after it's installed — and only the three that need it do (`eidos`, `eidos-init`, `eidos-migrate`). [`scripts/sync-skills.sh`](scripts/sync-skills.sh) regenerates those copies from the top-level sources, and `sync-skills.sh --check` fails if one has drifted, so a copy can never quietly fall out of step with the source. The trade was chosen on purpose: gitignoring the copies breaks Desktop installs, and dropping the top-level copies would cost the single, reviewable home for the standard — so we keep both, and let the script hold them together.

### In Claude Code

The repo is a public plugin marketplace — add it and install:

```
# run these inside Claude Code:
/plugin marketplace add BuildableWorks/Eidos
/plugin install eidos@eidos
```

For development against a local clone, point Claude Code at it instead:

```
# try it for one session (ephemeral):
claude --plugin-dir /path/to/eidos

# …or add the clone as a local marketplace, then install:
/plugin marketplace add /path/to/eidos
/plugin install eidos@eidos
```

No build step: each skill carries the committed copies it needs and reads a registry's form from its own `.eidos/` — all committed, so it behaves the same wherever it's installed.

### In Claude Desktop (and web / Cowork)

Desktop runs each skill **scoped to its own folder** — it can't reach sibling files at the plugin root. That's fine: every skill is self-contained (the three that need the standard carry committed copies of it), so the same marketplace install above works here. If you'd rather upload a file than add a git marketplace, build the zip:

```
./scripts/package-plugin.sh        # → dist/eidos-plugin.zip
```

Then, on any paid plan (Pro, Max, Team, Enterprise): **Customize → Plugins → +** → _upload a custom plugin file_ → pick `dist/eidos-plugin.zip` ([docs](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)). The skills then work in chat on Desktop, the web, and Cowork. (Eidos has no hooks or sub-agents, which would otherwise run only in Cowork.)

### Sharing it with someone else

Hand a colleague the self-contained zip the package script builds — it works in both Claude Code and Desktop:

```
./scripts/package-plugin.sh        # → dist/eidos-plugin.zip
```

They install it with **Customize → Plugins → +** → _upload a custom plugin file_ (Desktop), or `claude --plugin-dir dist/eidos-plugin.zip` (Code). It's well under Desktop's 50 MB cap.

For ongoing iteration, push to a **private** git repo and share the URL — `/plugin marketplace add <url>` (Code).

### Raw, in another Claude Code project

A skill is just a folder with a `SKILL.md`. Drop the folder at `<repo>/.claude/skills/<name>/` (one project) or `~/.claude/skills/<name>/` (everywhere); a project copy wins over a global one. Each folder is self-contained — the runtime skills read your registry's `.eidos/`, and `eidos`/`eidos-init`/`eidos-migrate` carry their committed copies of the standard — so the folder works as-is.

**Adding your own skill:** create `skills/<your-skill>/SKILL.md` — it ships with the plugin automatically.

## Versioning

The standard is versioned with [Semantic Versioning](https://semver.org/). The current version is in [`EIDOS.md`](EIDOS.md); history and migrations are in [`CHANGELOG.md`](CHANGELOG.md). Each release is preserved in [`versions/`](versions/) under its full semver name — `EIDOS.md` copied in as-is when the version is tagged.

## License

Licensed under the [Apache License 2.0](LICENSE).

Copyright © 2026 Buildable
