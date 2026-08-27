# Eidos

_**εἶδος** (eidos), Greek — the form or essence of a thing: the look that makes it what it is. Plato's eternal Form; Aristotle's essence behind the matter._

> **[Eidos v4.3.2](EIDOS.md)** — the full standard.

A markdown standard for defining the essence of a thing — a product, a body of work, anything you set out to make. One file is the complete source of truth for one unit of it, independent of time or status: as true of something planned as of something long finished. The files live as plain `.md` next to your code. No SaaS. No lock-in. No hidden state.

A unit captures **state and intent, not work**. Tasks describe work and die when the work ships; a unit describes the product and stays accurate across its whole life: drafted, built, deprecated.

Eidos is **human-first**. A Framework Owner holds the intent, the scope, and the decisions. An agent — via the `eidos` skill — facilitates: it formats, supplements, asks clarifying questions, and presses on scope. It does **not** author items for you. An item no one thought through is worse than none.

## Why

Product knowledge rots in tickets, wikis, and people's heads. Eidos keeps the authoritative answer to "what is this thing" as version-controlled markdown, reviewed in PRs alongside the code it describes. Humans and coding agents read the same source of truth.

## How it works

Eidos turns on two words. A **framework** is the *form*: the collections, shapes, personas, naming convention, and property Schema that govern how you write. A **definition** is the *thing*: the frames, items, and docs a team writes with a framework. One framework, many definitions — the framework is the portable piece, the part one team can hand to another.

A definition is one folder you drop into any repo:

```txt
Blueprint/                 # the definition — the root may be named anything
  README.md                # the human "start here"
  _eidos/                  # the framework (hidden) — the form this definition is written in
    shapes/                #   body shapes, one file per flavor
    personas/              #   how the agent should talk to each role
    Framework.md           #   the index + config: version, naming, collections, Schema
    user.md                #   who's in the seat (personal, gitignored)
  Roadmap.md               # a top-level doc — your own, free-form (optional)
  <Framing>/               # the framing collection — every framework declares one
  <Collection>/            # the units, grouped one level deep
    index.md               #   generated index of the collection
    <Group>/<Title>.md     #   one unit per file
```

- **Framework** — the form layer, found by its hidden `_eidos/` folder, and the piece you can publish or hand to another team. [`Framework.md`](seeds/software/Framework.md) is its index and config; a visible `README.md` is the door into it.
- **Collections** — folders of repeated units. Every framework declares a **framing collection** first (the loose docs saying what the whole thing is), then at least one collection of units. A unit is a **frontmatter** contract plus a **body**.
- **Shapes & flavors** — a **shape** is the body template a collection's units follow; a collection can offer more than one — **flavors** — with one default. Start in the flavor that fits and grow into a fuller one later.
- **Schema** — the frontmatter contract every unit carries: six core properties Eidos requires, plus whatever the framework adds.
- **Top-level docs** — one-of-a-kind documents at the root: a Roadmap, a Vision, the generated Framework Map. Free-form, no shape, no validation.
- **Personas & the actor** — [`personas/`](seeds) say how the agent talks to each kind of person; the personal, gitignored `user.md` says who _you_ are, so the same definition answers each reader differently.

**Nothing above is named by the standard.** `EIDOS.md` defines collections, shapes, flavors, and properties — never what any of them is called. That is the framework's, and the [seeds](seeds) show the same machinery answering to three different vocabularies:

|  | [`software`](seeds/software) | [`book`](seeds/book) | [`research`](seeds/research) |
| --- | --- | --- | --- |
| **framing collection** | `Frames` — architecture, audience, criteria, market | `Frames` — premise, reader, voice, market | `Frames` — question, prior work, method, ethics |
| **the units** | `Specs` | `Chapters` | `Investigations` |
| **grouped by** | domain | part | strand |
| **flavors** | `full` · `micro` | `full` · `sketch` | `full` · `note` |

Pick the nearest seed and reshape it; none of them is privileged, and a framework that ends up looking like none of them is working as intended.

## Quick start

1. **Get the skills.** Optional but recommended — see [Installing the skills](#installing-the-skills).
2. **Initialize.** Run `eidos-install`. It asks what you're defining, offers the seeds, and scaffolds a definition around the one you pick. Everything in a seed is reshapeable later, so "close enough" is the right answer.
3. **Fill the frames first.** Loose, point-in-time prose — fill what's known and leave the rest. They set what every other item is judged against, which is why every framework has to declare them.
4. **Author the units.** One file per unit, named for its title in the convention you chose. Frontmatter is generated from the Schema; the body follows your collection's shape. Lead with what the shape opens on, and press hardest on its non-goals section — that's where scope is actually held. The `eidos` skill facilitates; it does not author for you.
5. **Commit it.** The definition is the source of truth, `_eidos/` and all (except the personal `user.md`, which the seeded `.gitignore` keeps out). Review it in PRs alongside the code. Eidos relies on git history, so don't gitignore any of it.

The full rules are in **[EIDOS.md](EIDOS.md)**. See **[`examples/`](examples/)** for two filled-in definitions — a subset of YouTube, and a short film — to pattern-match against.

## Installing the skills

Eidos ships as a **Claude plugin** bundling eight skills:

- **`eidos`** — author + validate
- **`eidos-format`** — reshape a rough draft into Eidos shape (a collection item, or a free-form top-level doc)
- **`eidos-install`** — scaffold a new definition (pick a seed; installs it into `_eidos/`)
- **`eidos-configure`** — add a collection or a flavor, add/rename/retire a custom property and backfill every item, and keep the Framework's Top-Level index current
- **`eidos-index`** — regenerate each collection's `index.md` listing
- **`eidos-canvas`** — generate an Obsidian `.canvas` map of chosen collections, with `connects_to` links as edges
- **`eidos-whoami`** — set who you are: pick a persona and calibrate it (role, experience, technical capacity)
- **`eidos-migrate`** — move a definition to a new version of the standard

Most skills read your definition's framework at runtime and need nothing of the standard: `eidos-format`, `eidos-configure`, `eidos-index`, `eidos-canvas`, and `eidos-whoami`. The other three carry a **committed copy** of just what they need — `eidos` (the `EIDOS.md` ruleset), `eidos-install` (the canonical [`seeds/`](seeds)), and `eidos-migrate` (the version history) — so each skill is self-contained wherever it's installed. `scripts/sync-skills.sh` keeps those copies in sync with the top-level sources.

### Why the skills carry copies of the standard

You'll notice the same files in two places — `EIDOS.md`, `seeds/`, and `versions/` at the repo root, and again inside a few of the skill folders. That duplication is deliberate, not an oversight.

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

No build step: each skill carries the committed copies it needs and reads a definition's framework from its own `_eidos/` — all committed, so it behaves the same wherever it's installed.

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

A skill is just a folder with a `SKILL.md`. Drop the folder at `<repo>/.claude/skills/<name>/` (one project) or `~/.claude/skills/<name>/` (everywhere); a project copy wins over a global one. Each folder is self-contained — the runtime skills read your definition's `_eidos/`, and `eidos`/`eidos-install`/`eidos-migrate` carry their committed copies of the standard — so the folder works as-is.

**Adding your own skill:** create `skills/<your-skill>/SKILL.md` — it ships with the plugin automatically.

## Canonical Seeds

The **[`seeds/`](seeds)** folder holds the starting frameworks Eidos ships. `eidos-install` offers them and copies the chosen one into a definition's `_eidos/`. What each covers:

- **[`software/`](seeds/software)** — a product, service, or system being built. The default, and the one most people start from.
- **[`book/`](seeds/book)** — a book, long-form argument, or course.
- **[`research/`](seeds/research)** — a question, a study, or a programme of inquiry.

Their collections and flavors are compared [above](#how-it-works). Every seed carries the same pieces, laid out exactly as they land in a fresh definition:

- **`shapes/`** — one file per flavor: the body template a collection's items follow.
- **`personas/`** — the response contracts, one per role. Each seed's are written against its own collections: `software` has a Developer and a Designer, `book` an Editor and a Reader, `research` an adversarial Reviewer and a non-technical Sponsor.
- **`Framework.md`** — the index and config: version, naming convention, Top-Level documents, Collections (with flavors, canvas style, and grouping), and the property **Schema**.
- **`user.md`** and **`.gitignore`** — the blank per-actor file, and the dotfile that keeps it out of version control.
- **`README.md`** — the `{{Product}}` front-door template that installs to the definition's root.

A seed is a starting point, not a cage: a framework may reshape or override any of it — add a property, adjust a shape, add a flavor, retune a persona — without forking the standard. And a seed is exactly the kind of artifact you'd hand to another team: form, no content.

## Versioning

Two things version separately, both with [Semantic Versioning](https://semver.org/).

- **The standard** — the version in [`EIDOS.md`](EIDOS.md), and the one a definition records as `eidos_version`. It moves only when the text of the standard moves. Each release is frozen in [`versions/`](versions/) under its full semver name, with the worked upgrade path in [`MIGRATIONS.md`](versions/MIGRATIONS.md).
- **The plugin** — the version in `.claude-plugin/plugin.json`, and what `/plugin install` and update checks see. It moves on every shipped release, including ones that only touch a skill, a seed, or an example.

They started on the same number and will drift, because the tooling changes far more often than the standard does. [`CHANGELOG.md`](CHANGELOG.md) tracks plugin releases and records which standard each one ships — so a release note that says *Standard: unchanged* means your definitions need nothing.

## License

Licensed under the [Apache License 2.0](LICENSE).

Copyright © 2026 Buildable
