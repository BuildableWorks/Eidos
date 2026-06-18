# Eidos

> **[Eidos v2.0.0](EIDOS.md)** — the full standard.

A markdown spec registry for defining what a product _is_. One file completely defines one unit of a product, true whether or not the thing has been built. Specs live as plain `.md` files next to your code. No SaaS. No lock-in. No hidden state.

A **spec** captures **state and intent, not work**. Tasks describe work and die when the work ships; a spec describes the product and stays accurate across its whole life: drafted, built, deprecated.

Eidos is **human-first**. A product owner holds the intent, the scope, and the decisions. An agent — via the `eidos` skill — facilitates: it formats, supplements, asks clarifying questions, and presses on scope. It does **not** author specs for you. A spec no one thought through is worse than none.

## Why

Product knowledge rots in tickets, wikis, and people's heads. Eidos keeps the authoritative answer to "what is this thing" as version-controlled markdown, reviewed in PRs alongside the code it describes. Humans and coding agents read the same source of truth.

## How it works

Drop a `Blueprint/` folder into any repo:

```txt
Blueprint/
  Architecture.md     # overarching system shape
  Audience.md         # who it serves and how each type interacts
  Criteria.md         # budget, scope objectives, timeline
  Market.md           # where it sits, how it differs, how it earns
  Domains.md          # the domains as descriptions; present by default
  Specs/
    <Domain>/
      <Title>.md      # one spec per unit, grouped by domain
```

- **Product docs** are four files — one of each — that frame the whole product.
- **Specs** are the many, one per unit, grouped into `<Domain>/` folders. Every spec shares one shape — Intent, Behaviors & Acceptance Criteria, Out of Scope, and the rest; the fields at the top are the firm part, the body is guidance.
- **Templates** ship with the standard — bundled in the plugin, and at the standard's own top-level `templates/`. The skills fill from them; you never keep a `templates/` folder in your product repo.
- Human-facing names are **Title Case** (the tree reads like a table of contents); the `id` inside each spec — lowercase words joined by hyphens — is its permanent reference.

The full rules are in **[EIDOS.md](EIDOS.md)**. See **[`example/`](example/)** for a filled-in product definition you can pattern-match against.

## Quick start

Use Eidos on your own project:

1. **Get the skills.** Install `eidos` (author + validate), `eidos-init` (scaffold a new registry), and `eidos-migrate` (move specs to a new version) — see [Installing the skills](#installing-the-skills). Or work by hand from [`EIDOS.md`](EIDOS.md) and the standard's [`templates/`](templates/) (from a clone — you don't keep them in your project).
2. **Initialize.** Run `eidos-init`: it scaffolds a `Blueprint/` from the standard's templates, following the current `EIDOS.md` — no copying the example and deleting its contents. (By hand: make a `Blueprint/` folder, copy the four product-doc templates and `Domains.md` from the standard's [`templates/`](templates/), and add a `Specs/` folder.)
3. **Fill the product docs.** Architecture, Audience, Criteria, Market — prose, loose, point-in-time; fill what's known, leave the rest. Describe each domain in `Domains.md` as specs accrue.
4. **Author specs.** One file per unit under `Specs/<Domain>/`, named for its title in Title Case (`Magic Link Sign-In.md`). Lead with Intent and Behaviors & Acceptance Criteria; press hard on **Out of Scope** — that's where scope is held. The `eidos` skill facilitates; it does not author for you.
5. **Commit it.** Specs are the product definition. Review them in PRs alongside code. Eidos relies on git history (`created`/`modified` dates, the Decisions log, scope drift), so do **not** gitignore them.

See [`example/`](example/) for a filled-in registry to pattern-match against.

## Installing the skills

Eidos ships as a **Claude plugin** bundling three skills:

- **`eidos`** — author + validate
- **`eidos-init`** — scaffold a new registry
- **`eidos-migrate`** — move specs to a new version

The plugin carries the standard with it — `EIDOS.md`, `templates/`, and the full version history — so the skills behave the same wherever it's installed: Claude Code, or the Chat tab in Claude Desktop, the web, and Cowork.

### In Claude Code

Not published yet, so install from your local clone (use an absolute path):

```
# try it for one session (ephemeral):
claude --plugin-dir /path/to/eidos

# …or install it persistently — add the clone as a local marketplace, then install
# (run these inside Claude Code):
/plugin marketplace add /path/to/eidos
/plugin install eidos@eidos
```

No build step: the plugin reads `EIDOS.md`, `templates/`, `versions/`, and `CHANGELOG.md` from its own root, and those are committed. Once the repo is public, the marketplace step becomes `/plugin marketplace add https://gitlab.com/the-virtual-panda/Eidos.git`.

### In Claude Desktop (and web / Cowork)

Desktop runs each skill **scoped to its own folder** — it can't reach sibling files at the plugin root, and there's no `${CLAUDE_PLUGIN_ROOT}` like in Claude Code. So `eidos-init` (needs `templates/`) and `eidos-migrate` (needs the version history) only work if those assets sit **inside their own folders**. One script handles that and builds the zip:

```
./scripts/package-plugin.sh        # → dist/eidos-plugin.zip
```

Then, on any paid plan (Pro, Max, Team, Enterprise): **Customize → Plugins → +** → _upload a custom plugin file_ → pick `dist/eidos-plugin.zip` ([docs](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)). The skills then work in chat on Desktop, the web, and Cowork. (Eidos has no hooks or sub-agents, which would otherwise run only in Cowork.)

The **Add marketplace → git URL** route also exists, but in Desktop it only works if those vendored copies are committed (they're gitignored by default) — the packaged zip is the reliable path.

### Sharing it with someone else

Hand a colleague the self-contained zip the package script builds — it works in both Claude Code and Desktop:

```
./scripts/package-plugin.sh        # → dist/eidos-plugin.zip
```

They install it with **Customize → Plugins → +** → _upload a custom plugin file_ (Desktop), or `claude --plugin-dir dist/eidos-plugin.zip` (Code). It's well under Desktop's 50 MB cap.

For ongoing iteration, push to a **private** git repo and share the URL — `/plugin marketplace add <url>` (Code). The URL route works cleanly in Code; for Desktop it needs the vendored copies committed.

### Raw, in another Claude Code project

A skill is just a folder with a `SKILL.md`. Run `./scripts/sync-skills.sh` to make it self-contained, then drop the folder at `<repo>/.claude/skills/<name>/` (one project) or `~/.claude/skills/<name>/` (everywhere). A project copy wins over a global one.

### When you need `sync-skills.sh`

`package-plugin.sh` already runs it when building a Desktop zip — you invoke it **directly** only for the **raw** route above (a skill folder dropped into another repo's `.claude/skills/`). Either way, it copies `templates/` and the version history into each skill so the folder stands alone. **Claude Code's plugin doesn't need it** — there, skills read the originals from the plugin root (`${CLAUDE_PLUGIN_ROOT}`). The copies are gitignored; re-run after the standard changes.

**Adding your own skill:** create `skills/<your-skill>/SKILL.md` — it ships with the plugin automatically.

## Versioning

The standard is versioned with [Semantic Versioning](https://semver.org/). The current version is in [`EIDOS.md`](EIDOS.md); history and migrations are in [`CHANGELOG.md`](CHANGELOG.md); prior versions are preserved in [`versions/`](versions/) under their full semver names.

## License

Licensed under the [Apache License 2.0](LICENSE).

Copyright © 2026 Brenton Unger II.
