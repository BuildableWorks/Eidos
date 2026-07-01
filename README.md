# Eidos

_**εἶδος** (eidos), Greek — the form or essence of a thing: the look that makes it what it is. Plato's eternal Form; Aristotle's essence behind the matter._

> **[Eidos v4.1.0](EIDOS.md)** — the full standard.

A markdown registry for defining what a product _is_. One file completely defines one unit of the product — a **spec**, in the common case — true whether or not the thing has been built. The files live as plain `.md` next to your code. No SaaS. No lock-in. No hidden state.

A unit captures **state and intent, not work**. Tasks describe work and die when the work ships; a unit describes the product and stays accurate across its whole life: drafted, built, deprecated.

Eidos is **human-first**. A registry owner holds the intent, the scope, and the decisions. An agent — via the `eidos` skill — facilitates: it formats, supplements, asks clarifying questions, and presses on scope. It does **not** author items for you. An item no one thought through is worse than none.

## Why

Product knowledge rots in tickets, wikis, and people's heads. Eidos keeps the authoritative answer to "what is this thing" as version-controlled markdown, reviewed in PRs alongside the code it describes. Humans and coding agents read the same source of truth.

## How it works

A **registry** is one product's definition — a `Blueprint/` folder you drop into any repo. Everything Eidos defines is built from a few pieces:

```txt
Blueprint/                 # the registry — one product's definition
  README.md                # the human "start here"
  _eidos/                  # the form layer (hidden) — how this registry is shaped
    shapes/                #   collection body shapes, one per flavor (spec.*, frame.*)
    personas/              #   how the agent should talk to each role
    Registry.md            #   the index + config: version, naming, top-level docs, collections, and the property Schema
    user.md                #   who's in the seat (personal, gitignored)
  Roadmap.md               # a top-level doc — your own, free-form (optional)
  Frames/                  # a collection — the framing docs (Architecture, Audience, …)
    Architecture.md  Audience.md  Criteria.md  Market.md
  Specs/                   # a collection — units grouped into sub-folders
    index.md               #   generated index of the collection
    <Group>/<Title>.md     #   one unit per file
```

- **Registry** — the whole product definition, located by its hidden `_eidos/` folder. [`_eidos/Registry.md`](seed/Registry.md) is its **index and config**: the Eidos version, the naming convention, the list of top-level docs, and the collections. A visible `README.md` is the door into it.
- **Frames** — the framing docs that set what the whole product is judged against: Architecture, Audience, Criteria, Market. A **collection** (highly encouraged, not required), loose point-in-time prose, each following its flavor's shape.
- **Top-level docs** — one-of-a-kind documents you add at the root: a Roadmap, a Vision, the generated Registry Map. Free-form prose, no shape, no validation — the loose layer that annotates the whole.
- **Collections** — folders of repeated units (`Specs`, `Frames`, or your own). A registry can have several, and each can group its units one level deep in sub-folders. A unit is a small **frontmatter** contract (the firm part) plus a **body** (guidance).
- **Shapes & flavors** — a **shape** is the body template a *collection's* units follow (top-level docs have none); a collection can offer more than one — **flavors** — with one default (say a `full` shape and a lighter `micro`; `Frames` has one per kind of frame). Start in the flavor that fits and grow into a fuller one later.
- **Schema** — the frontmatter contract every unit carries: an Eidos-canonical baseline plus any custom properties you add. Frontmatter is generated from it, so every unit is born conforming.
- **Personas & the actor** — [`_eidos/personas/`](seed/personas) say how the agent should talk to each kind of person (a designer gets experience terms; a developer, full technical depth); the personal, gitignored `_eidos/user.md` says who _you_ are, so the same registry answers each reader differently.

The form layer is seeded with opinionated defaults — public and browsable in [`seed/`](seed) — that you extend without forking the standard, committed alongside the content (except `user.md`).

**`Specs` and `domains` are the default seed, not the essence.** Eidos starts you with a `Specs` collection grouped by `domain`, because most products begin there — but the machinery is collections, shapes, and flavors. A film team could define a `Scenes` collection grouped by `Act`, with `scene.full` and `scene.beat` flavors, and never write a "spec." Human-facing names follow a **naming convention you pick at init** (Title Case, TitleCase, or kebab-case); the kebab-case `id` inside each unit is its permanent reference.

The full rules are in **[EIDOS.md](EIDOS.md)**. See **[`example/`](example/)** for a filled-in registry (a small subset of YouTube) to pattern-match against.

## Quick start

Use Eidos on your own project:

1. **Get the skills. (optional)** Install `eidos` skills to help follow the spec, but it's easy enough to follow without it — see [Installing the skills](#installing-the-skills).
2. **Initialize.** Run `eidos-install`: it installs the `_eidos/` form layer and scaffolds a `Blueprint/`, following the current `EIDOS.md` — or copy the example and modify its contents.
3. **Fill the Frames.** Architecture, Audience, Criteria, Market — the `Frames` collection, prose, loose, point-in-time; fill what's known, leave the rest. Describe each Specs domain in the Registry's Collections section as specs accrue; each collection's `index.md` is generated by `eidos-index`.
4. **Author specs.** One file per unit under `Specs/<Domain>/`, named for its title in Title Case (`Magic Link Sign-In.md`). Each spec's frontmatter is generated from the registry's Schema; lead with Intent and Behaviors & Acceptance Criteria; press hard on **Out of Scope** — that's where scope is held. The `eidos` skill facilitates; it does not author for you.
5. **Commit it.** Specs are the product definition — `_eidos/` form layer and all (except the personal `_eidos/user.md`, which the seeded `.gitignore` keeps out). Review them in PRs alongside code. Eidos relies on git history (`created`/`modified` dates, the Decisions log, scope drift), so do **not** gitignore them.

Doing Eidos needs the skills and a seeded registry: `EIDOS.md` gives the method, but the form a registry uses lives in its `_eidos/`. See [`example/`](example/) for a filled-in registry to pattern-match against.

## Installing the skills

Eidos ships as a **Claude plugin** bundling nine skills:

- **`eidos`** — author + validate
- **`eidos-format`** — reshape a rough draft into Eidos shape (a collection item — a spec or a Frame — or a free-form top-level doc)
- **`eidos-install`** — scaffold a new registry (installs the `_eidos/` form layer)
- **`eidos-schema`** — add, rename, or retire a custom property and backfill every item
- **`eidos-registry`** — add a collection or a flavor, and keep the Registry's Top-Level index current
- **`eidos-index`** — regenerate each collection's `index.md` listing
- **`eidos-canvas`** — generate an Obsidian `.canvas` map of chosen collections, with `connects_to` links as edges
- **`eidos-whoami`** — set who you are: pick a persona and calibrate it (role, experience, technical capacity)
- **`eidos-migrate`** — move a registry to a new version

Most skills read from your registry at runtime and need nothing of the standard: `eidos-format`, `eidos-schema`, `eidos-registry`, `eidos-index`, `eidos-canvas`, and `eidos-whoami`. The other three carry a **committed copy** of just what they need — `eidos` (the `EIDOS.md` ruleset), `eidos-install` (the canonical [`seed/`](seed)), and `eidos-migrate` (the version history) — so each skill is self-contained wherever it's installed. `scripts/sync-skills.sh` keeps those copies in sync with the top-level sources.

### Why the skills carry copies of the standard

You'll notice the same files in two places — `EIDOS.md`, `seed/`, and `versions/` at the repo root, and again inside a few of the skill folders. That duplication is deliberate, not an oversight.

The top-level copies are the **source of truth** and the public review surface: one place to read, diff, and propose changes to what Eidos ships. But a skill often can't reach them once it's installed:

- **Claude Desktop sandboxes each skill to its own folder** — it can't read sibling files at the plugin root.
- **A git-marketplace install ships only what's committed** — anything gitignored never arrives.

So a skill that needs part of the standard has to _carry_ it, committed, to keep working after it's installed — and only the three that need it do (`eidos`, `eidos-install`, `eidos-migrate`). [`scripts/sync-skills.sh`](scripts/sync-skills.sh) regenerates those copies from the top-level sources, and `sync-skills.sh --check` fails if one has drifted, so a copy can never quietly fall out of step with the source. The trade was chosen on purpose: gitignoring the copies breaks Desktop installs, and dropping the top-level copies would cost the single, reviewable home for the standard — so we keep both, and let the script hold them together.

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

No build step: each skill carries the committed copies it needs and reads a registry's form from its own `_eidos/` — all committed, so it behaves the same wherever it's installed.

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

A skill is just a folder with a `SKILL.md`. Drop the folder at `<repo>/.claude/skills/<name>/` (one project) or `~/.claude/skills/<name>/` (everywhere); a project copy wins over a global one. Each folder is self-contained — the runtime skills read your registry's `_eidos/`, and `eidos`/`eidos-install`/`eidos-migrate` carry their committed copies of the standard — so the folder works as-is.

**Adding your own skill:** create `skills/<your-skill>/SKILL.md` — it ships with the plugin automatically.

## Canonical Seed

The **[`seed/`](seed)** folder is the public, browsable baseline that `eidos-install` installs into a registry's `_eidos/`. It's the standard's opinionated starting point — every piece of the form layer, laid out exactly as it lands in a fresh registry. Its contents:

- **`shapes/`** — the collection body shapes, one file per flavor (`spec.full.md`, `spec.micro.md`, `frame.architecture.md`, …). The body template each collection's items follow.
- **`personas/`** — the response contracts, one per role, that say how the agent talks to each kind of person.
- **`Registry.md`** — the registry's index and config: the Eidos version, the naming convention, the Top-Level documents, the Collections (with their flavors and grouping), and the property **Schema** (the frontmatter contract, in its `## Schema` section).
- **`user.md`** — the blank per-actor file; it installs gitignored, so no one's persona lands in anyone else's checkout.
- **`.gitignore`** — a real dotfile that keeps `user.md` out of version control.
- **`README.md`** — the `{{Product}}` front-door template that installs to the registry's root `README.md`, the human "start here."

It's a starting point, not a cage: a registry may reshape or override any of it — add a property, adjust a shape, add a flavor, retune a persona — without forking the standard. The default works out of the box; the parts you change are yours.

## Versioning

The standard is versioned with [Semantic Versioning](https://semver.org/). The current version is in [`EIDOS.md`](EIDOS.md); history and migrations are in [`CHANGELOG.md`](CHANGELOG.md). Each release is preserved in [`versions/`](versions/) under its full semver name — `EIDOS.md` copied in as-is when the version is tagged.

## License

Licensed under the [Apache License 2.0](LICENSE).

Copyright © 2026 Buildable
