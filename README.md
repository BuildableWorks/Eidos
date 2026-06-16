# Eidos

> **[Eidos v1.0.0](EIDOS.md)** — the full standard.

A markdown spec registry for defining what a product *is*. One file completely
defines one unit of a product, true whether or not the thing has been built. Specs
live as plain `.md` files next to your code. No SaaS. No lock-in. No hidden state.

A **spec** captures **state and intent, not work**. Tasks describe work and die
when the work ships; a spec describes the product and stays accurate across its
whole life: proposed, built, deprecated.

## Why

Product knowledge rots in tickets, wikis, and people's heads. Eidos keeps the
authoritative answer to "what is this thing" as version-controlled markdown,
reviewed in PRs alongside the code it describes. Humans and coding agents read the
same source of truth.

## How it works

Drop a `product/` folder into any repo:

```txt
product/
  Architecture.md     # overarching system shape
  Audience.md         # who it serves and how each type interacts
  Criteria.md         # budget, objective + scope, timeline
  Market.md           # where it sits, how it differs, how it earns
  specs/
    <domain>/
      <id>.md         # one spec per unit, grouped by domain
  domains.md          # optional, describes each domain; derived from specs
```

- **Product docs** are four singletons that frame the whole product.
- **Specs** are the many, one per unit, grouped into `<domain>/` folders. Every
  spec shares one shape; the frontmatter is a hard contract, the body is guidance.

The full rules are in **[EIDOS.md](EIDOS.md)**. See **[`example/`](example/)** for a
filled-in product definition you can pattern-match against.

## Quick start

Use Eidos on your own project:

1. **Get the skill.** The `eidos` skill (in [`.claude/skills/eidos/`](.claude/skills/eidos))
   authors and validates specs to the standard. Install it in your agent, or work
   by hand from `EIDOS.md`.
2. **Create the registry.** Copy [`example/`](example/) into your repo as
   `product/` (rename freely — nothing points at it by path), or scaffold an empty
   `product/specs/` yourself.
3. **Fill the four product docs.** Architecture, Audience, Criteria, Market. Prose,
   loose, point-in-time. Fill what's known, leave the rest.
4. **Author specs.** One file per unit under `specs/<domain>/`. Lead with Intent
   and Behavior; press hard on **Out of Scope** — that's where scope is held.
5. **Commit it.** Specs are the product definition. Review them in PRs alongside
   code. Eidos relies on git history (`last_validated`, the Decisions log, scope
   drift), so do **not** gitignore them.

## Versioning

The standard is versioned with [Semantic Versioning](https://semver.org/). The
current version is in [`EIDOS.md`](EIDOS.md); history and migrations are in
[`CHANGELOG.md`](CHANGELOG.md); prior major versions are preserved in
[`versions/`](versions/). `manifest.json` mirrors the current version for tools.

## License

TBD.
