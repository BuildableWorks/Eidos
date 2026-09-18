# Eidos

***εἶδος** (eidos), Greek — the form or essence of a thing: the look that makes it what it is. Plato's eternal Form; Aristotle's essence behind the matter.*

> [!IMPORTANT]
>
> ## Documentation lives at [eidosmd.com](https://eidosmd.com)
>
> **This repository holds the standard** ([`EIDOS.md`](EIDOS.md)), the seeds, and a Claude plugin of base skills. It is the place to read and change what Eidos *is*; it is not the best way to *use* it.
>
> **Use the [`eidos` CLI](https://eidosmd.com/docs/cli) with your agent.** `npm install -g eidosmd`, then `eidos instructions`. The CLI does the mechanical part (scaffold, generate, check, index) deterministically and hands the agent only what it needs, so a session is faster and spends a fraction of the context that skills reading the standard every time do. Anything running on a host with a shell uses the CLI. The skills here are for hosts with no shell: Claude Desktop chat, the web, Cowork.

## **[Eidos v5.2.1](EIDOS.md)** — the full standard

Eidos is a system of organization for defining a product: an app, a book, a study, a workflow, anything work produces that has a shape. It puts a structure around the documentation that a tool can enforce, so ideation and development progress in one place and the definition keeps pace with both. One file is the complete source of truth for one unit of the product, independent of time or status: as true of something planned as of something long finished. The product is written in plain markdown beside your code; the structure it is written in is data, in a hidden `.eidos/` folder you seldom open. The result is a database of intent: what the product is meant to be, queryable and version-controlled, living in the repo. No SaaS. No lock-in. Nothing outside the repo.

A blueprint captures **a vision of the product as a source of truth**, not work. Tasks describe work and die when the work ships; a blueprint describes the product and stays accurate across its whole life: drafted, built, deprecated.

Eidos is **human-first**. A Framework Owner holds the intent, the scope, and the decisions. An agent — via the `eidos` skill — facilitates: it formats, supplements, asks clarifying questions, and presses on scope. It does **not** author blueprints for you. A blueprint no one thought through is worse than none.

## Why

Product knowledge rots in tickets, wikis, and people's heads. A tracker is a database of work, and work dies when it ships. Eidos is a database of intent, and intent outlives every ticket. It keeps the authoritative answer to "what is this product" as version-controlled markdown, reviewed in PRs alongside the code it describes. Humans and coding agents read the same source of truth.

It gives every role the same place to stand. A designer, a developer, a product owner, and a stakeholder each answer to the same blueprint in the same words, so working across roles stops being a run of misunderstandings to reconcile. And because the definition lives in the repository, the product's source and its source of truth are one thing in one place, not a codebase here and a document somewhere else that drifted.

## How it works

Eidos turns on three words. A **product** is what you are defining: an app, a book, a study, a workflow, anything work produces that has a shape. A **framework** is the *structure*: the collections, templates, roles, naming convention, Properties table, and Vocabulary that govern how you write about it. A **blueprint** is one *unit of the product*: one file defining it completely, a frontmatter contract plus a body. One framework governs any number of blueprints, and it is the portable piece — the part one team can hand to another.

It all lives in one folder — the **root** — that you drop into any repo:

```txt
Blueprints/                # the root — may be named anything
  README.md                # the human "start here" (optional; every seed ships one)
  .eidos/                  # the framework (hidden) — the structure everything here is written in
    templates/**             #   body templates, one file per variant
    roles/**                 #   how the agent should talk to each role
    Framework.yaml         #   the framework document: version, naming, collections, Properties, Vocabulary, index
    plugins/<name>/        #   a tool's own folder, like .obsidian/plugins/ (optional)
      local.yaml           #     the one personal file in it: one machine's settings (gitignored)
    me.md                  #   who's in the seat (personal, gitignored)
  <Doc>.md                 # a top-level doc — your own, free-form (optional)
  <Collection>/            # the blueprints, grouped one level deep
    index.md               #   generated index of the collection
    <Group>/<Title>.md     #   one blueprint per file
```

- **Framework** — the structure layer, found by its hidden `.eidos/` folder, and the piece you can publish or hand to another team. [`Framework.yaml`](seeds/software/Framework.yaml) is the framework document, config and index in one; a visible `README.md` is the door into it.
- **Collections** — folders of repeated blueprints, at least one per framework. A blueprint is a **frontmatter** contract plus a **body**. Every seed Eidos ships opens with a `Frames` collection, the loose docs saying what the whole product is: the standard doesn't require one, but it is the recommendation for every product.
- **Templates & variants** — a **template** is the body a collection's blueprints follow; a collection can offer more than one — **variants** — with one default. Start in the variant that fits and grow into a fuller one later.
- **Properties** — the frontmatter contract every blueprint carries: four core properties from Eidos (`id`, `title`, `summary`, `variant`), plus whatever the framework adds. Each says whether it is required, so only the fields a framework insists on land on every blueprint; the rest are there when they have a value. One whose value is one of a set declares its `options`, and a value off the list is surfaced, never refused.
- **Vocabulary** — the term contract: the words the root uses on purpose, each with what it means and what it is *not*, so a distinction made once (a team member is not staff) is not lost three blueprints later. Starts empty; Eidos declares none of them.
- **Top-level docs** — one-of-a-kind documents at the root: a Vision, a map a tool generates. Free-form, no template, no validation.
- **Roles** — [`roles/`](seeds) say how the agent talks to each kind of person; the personal, gitignored `me.md` says who *you* are, so the same blueprints answer each reader differently.
- **Plugins** — `.eidos/` is open the way `.obsidian/` is: a tool that keeps something in the framework takes `plugins/<name>/`, and a Properties row may carry the tool's own fields past the standard's six. Inside a file, a tool keeps what it needs in a **region**, a span between two HTML comments carrying its name, `<!-- <tool>:<region> <args> -->` to `<!-- /<tool>:<region> -->`, whose contents are the tool's own. The standard reads none of it and every skill leaves it alone.

**Nothing above is named by the standard.** `EIDOS.md` defines collections, templates, variants, and properties — never what any of them is called. That is the framework's, and the [seeds](seeds) show the same machinery answering to three different vocabularies:

|                    | [`software`](seeds/software)                        | [`book`](seeds/book)                      | [`research`](seeds/research)                    |
| ------------------ | --------------------------------------------------- | ----------------------------------------- | ----------------------------------------------- |
| **framing docs**   | `Frames` — architecture, audience, criteria, market | `Frames` — premise, reader, voice, market | `Frames` — question, prior work, method, ethics |
| **the blueprints** | `Specs`                                             | `Chapters`                                | `Investigations`                                |
| **grouped by**     | domain                                              | part                                      | strand                                          |
| **variants**       | `full` · `micro`                                    | `full` · `sketch`                         | `full` · `note`                                 |

Pick the nearest seed and reshape it; none of them is privileged, and a framework that ends up looking like none of them is working as intended.

## Quick start

1. **Get the tooling.** `npm install -g eidosmd` for the [CLI](#the-cli), which works with any agent that has a shell. On a host with no shell (Claude Desktop chat, the web, Cowork), the [skills](#installing-the-skills) stand in.
2. **Initialize.** Run `eidos init` (or the `install` skill, which asks what you're defining and offers the seeds). It scaffolds a root around the seed you pick. Everything in a seed is reshapeable later, so "close enough" is the right answer.
3. **Fill the framing docs first.** Every seed opens with a `Frames` collection; the standard doesn't require it, but Eidos recommends one for every product. Loose prose — fill what's known and leave the rest. They set what every other blueprint is judged against.
4. **Author the blueprints.** One file per blueprint, named for its title in the convention you chose (kebab-case by default). Frontmatter is generated from the Properties table; the body follows your collection's template. Lead with what the template opens on, and press hardest on its non-goals section — that's where scope is actually held. The `eidos` skill facilitates; it does not author for you.
5. **Commit it.** The folder is the source of truth, `.eidos/` and all (except the personal `me.md` and any tool's `local.yaml`, which the seeded `.gitignore` keeps out). Review it in PRs alongside the code. Eidos relies on git history, so don't gitignore any of it.

The full rules are in **[EIDOS.md](EIDOS.md)**.

## The CLI

The mechanical half of Eidos as one command, `eidos`, published on npm as **[`eidosmd`](https://www.npmjs.com/package/eidosmd)** and maintained by [The Virtual Panda](https://gitlab.com/the-virtual-panda/eidosmd) alongside [eidosmd.com](https://eidosmd.com). It scaffolds a root from a seed, generates blueprints that are born conforming, validates a root against its own framework, regenerates the indexes, opens the root in a local browser page, and prints the workflow an agent should follow, so any agent with a shell can work in a root without a plugin.

```bash
npm install -g eidosmd
eidos init --group Identity --product "Care Connect"
eidos new specs "Session Management" --group identity
eidos check
eidos index
eidos instructions overview      # the agent workflow; `eidos agents --write` puts a pointer in AGENTS.md
```

[eidosmd.com/docs/cli](https://eidosmd.com/docs/cli) documents every command. Prefer it over the skills wherever there is a shell: the CLI's output is deterministic, and an agent that reads `eidos instructions` and calls `eidos check` spends a fraction of the context of one that re-reads the standard and walks the tree itself. The CLI carries its own copy of `EIDOS.md` and the seeds, synced from this repository, and versions separately from both the plugin and the standard: `eidos --version` names the standard it ships.

## Installing the skills

**The skills are for hosts with no shell**: Claude Desktop chat, the web, Cowork. Eidos maintains this official set for them. Anywhere an agent has a shell, which is every local host, use the CLI instead: it modifies a root deterministically and hands the agent only what it needs, so an install that takes about ten minutes through the skills takes about one through the CLI with an agent asking the basic questions. The seeds that install into a root point at the CLI for the same reason; they no longer name a skill.

Eidos ships as a **Claude plugin** bundling eight skills:

- **`eidos`** — author + validate
- **`iterate`** — question one rough idea until it holds still: which shape it takes, what it's for, how it fits the rest. Writes nothing; hands the understanding to `eidos`
- **`format`** — reshape a rough draft into Eidos form (a collection blueprint, or a free-form top-level doc)
- **`install`** — scaffold a new root (pick a seed; installs it into `.eidos/`)
- **`configure`** — add a collection or a variant, add/rename/retire a custom property and backfill every blueprint, and keep the Framework's Top-Level index current
- **`index`** — regenerate each collection's `index.md` listing
- **`whoami`** — set who you are: pick a role and calibrate it (ownership, experience, technical capacity)
- **`migrate`** — move a root to a new version of the standard

Most skills read the framework at runtime and need nothing of the standard: `iterate`, `format`, `configure`, `index`, and `whoami`. The other three carry a **committed copy** of just what they need — `eidos` (the `EIDOS.md` ruleset), `install` (the canonical [`seeds/`](seeds)), and `migrate` (the version history) — so each skill is self-contained wherever it's installed. `scripts/sync-skills.sh` keeps those copies in sync with the top-level sources.

### Why the skills carry copies of the standard

You'll notice the same files in two places — `EIDOS.md`, `seeds/`, and `versions/` at the repo root, and again inside a few of the skill folders. That duplication is deliberate, not an oversight.

The top-level copies are the **source of truth** and the public review surface: one place to read, diff, and propose changes to what Eidos ships. But a skill often can't reach them once it's installed:

- **Claude Desktop sandboxes each skill to its own folder** — it can't read sibling files at the plugin root.
- **A git-marketplace install ships only what's committed** — anything gitignored never arrives.

So a skill that needs part of the standard has to *carry* it, committed, to keep working after it's installed — and only the three that need it do (`eidos`, `install`, `migrate`). [`scripts/sync-skills.sh`](scripts/sync-skills.sh) regenerates those copies from the top-level sources, and `sync-skills.sh --check` fails if one has drifted, so a copy can never quietly fall out of step with the source. The trade was chosen on purpose: gitignoring the copies breaks Desktop installs, and dropping the top-level copies would cost the single, reviewable home for the standard — so we keep both, and let the script hold them together.

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

No build step: each skill carries the committed copies it needs and reads the framework from the root's own `.eidos/` — all committed, so it behaves the same wherever it's installed.

### Claude Desktop / Web

On any paid plan (Pro, Max, Team, Enterprise), add the repository as a marketplace and install from it — that way `/plugin` updates reach you like any other release:

**Customize → Plugins → +** → *add marketplace from repository* → `https://github.com/BuildableWorks/Eidos` → install **eidos** ([docs](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)).

This works because each skill is **self-contained**: Desktop scopes a skill to its own folder and it can't reach sibling files at the plugin root, so the three skills that need the standard carry committed copies of it.

If you can't reach the repo — an air-gapped machine, or a private fork you'd rather not wire up — build a zip and upload that instead, accepting that it won't auto-update:

```
./scripts/package-plugin.sh        # → dist/eidos-plugin.zip
```

**Customize → Plugins → +** → *upload a custom plugin file* → pick `dist/eidos-plugin.zip`.

Either way the skills work in chat on Desktop, the web, and Cowork. (Eidos has no hooks or sub-agents, which would otherwise run only in Cowork.)

### Sharing it with someone else

Point them at the repo — it is a marketplace, so they get updates with it: `/plugin marketplace add BuildableWorks/Eidos` in Code, or *add marketplace from repository* in Desktop. A **private** fork works the same way for a team that isn't ready to publish.

When a repo isn't an option, hand them the self-contained zip instead:

```
./scripts/package-plugin.sh        # → dist/eidos-plugin.zip
```

They install it with **Customize → Plugins → +** → *upload a custom plugin file* (Desktop), or `claude --plugin-dir dist/eidos-plugin.zip` (Code). It's well under Desktop's 50 MB cap, but it's a snapshot: a zip install won't see later releases.

### Raw, in another Claude Code project

A skill is just a folder with a `SKILL.md`. Drop the folder at `<repo>/.claude/skills/<name>/` (one project) or `~/.claude/skills/<name>/` (everywhere); a project copy wins over a global one. Each folder is self-contained — the runtime skills read your root's `.eidos/`, and `eidos`/`install`/`migrate` carry their committed copies of the standard — so the folder works as-is.

**Adding your own skill:** create `skills/<your-skill>/SKILL.md` — it ships with the plugin automatically.

## Canonical Seeds

The **[`seeds/`](seeds)** folder holds the starting frameworks Eidos ships. `install` offers them and copies the chosen one into a root's `.eidos/`. What each covers:

- **[`software/`](seeds/software)** — a product, service, or system being built. The default, and the one most people start from.
- **[`book/`](seeds/book)** — a book, long-form argument, or course.
- **[`research/`](seeds/research)** — a question, a study, or a programme of inquiry.

Their collections and variants are compared [above](#how-it-works). Every seed carries the same pieces, laid out exactly as they land in a fresh folder:

- **`templates/`** — one file per variant: the body a collection's blueprints follow.
- **`roles/`** — the response contracts, one per role. Each seed's are written against its own collections: `software` has a Developer and a Designer, `book` an Editor and a Reader, `research` an adversarial Reviewer and a non-technical Sponsor.
- **`Framework.yaml`** — the framework document: version, naming convention, Top-Level documents, Collections (with variants and grouping), the **Properties**, and the **Vocabulary** (empty in every seed; the terms are the root's own), with guidance as comments.
- **`me.md`** and **`.gitignore`** — the blank per-person file, and the dotfile that keeps it out of version control.
- **`README.md`** — the `{{Product}}` front-door template that installs to the root.

A seed is a starting point, not a cage: a framework may reshape or override any of it — add a property, adjust a template, add a variant, retune a role — without forking the standard. And a seed is exactly the kind of artifact you'd hand to another team: structure, no content.

## Versioning

Three things version separately, all with [Semantic Versioning](https://semver.org/).

- **The standard** — the version in [`EIDOS.md`](EIDOS.md), and the one a root records as `eidos_version`. It moves only when the text of the standard moves. Each release is frozen in [`versions/`](versions/) under its full semver name, with the worked upgrade path in [`MIGRATIONS.md`](versions/MIGRATIONS.md).
- **The plugin** — the version in `.claude-plugin/plugin.json`, and what `/plugin install` and update checks see. It moves on every shipped release, including ones that only touch a skill or a seed.
- **The CLI** — versioned in [its own repository](https://gitlab.com/the-virtual-panda/eidosmd) and published to npm as `eidosmd`. Each release names the standard it ships.

Every shipped release is tagged `vX.Y.Z` on the **plugin** version; the standard's releases are files in [`versions/`](versions/) rather than tags. They started on the same number and will drift, because the tooling changes far more often than the standard does. [`CHANGELOG.md`](CHANGELOG.md) tracks plugin releases and records which standard each one ships — so a release note that says *Standard: unchanged* means your roots need nothing.

## License

Licensed under the [Apache License 2.0](LICENSE).

Copyright © 2026 Buildable
