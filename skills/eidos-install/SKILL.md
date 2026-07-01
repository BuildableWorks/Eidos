---
name: eidos-install
description: >-
  Stand up a new Eidos registry in a repo that doesn't have one yet. Use when someone wants to set up Eidos, initialize a product/Blueprint, scaffold a registry, "start documenting our product", or says there's no Eidos here yet. It installs the `_eidos/` form layer (the shapes and property Schema) and scaffolds a `Blueprint/`, following the current `EIDOS.md` — no copying the example and deleting its contents. Trigger on "set up eidos", "init the blueprint", "scaffold our product docs", "we have no specs yet, get us started". For a registry that already exists, use `eidos` (author/validate) or `eidos-migrate` (version upgrade) instead.
---

# Eidos Install

Create a fresh Eidos registry: install the form layer, then scaffold the starting collections (`Specs`, and the encouraged `Frames`) around it. The point is to start from well-formed structure — **not** by copying the worked example and editing over it.

This is the companion to `eidos` (which authors and validates items once the registry exists). Init makes the empty frame; `eidos` helps fill it.

## How you work: facilitate, don't author

Scaffold the structure and bring in the blank shapes. Do **not** invent the product's content — Intent, scope, audience, and decisions are the owner's. Ask for the few things you need (the root folder name, and the first domains for the default `Specs` collection), create the files, and hand off to `eidos` for authoring. A registry full of AI-guessed prose is worse than an empty, honest one.

## Where the seed lives

The canonical seed is the standard's — public and front-facing at the top level as **`seed/`**, and shipped as a committed copy inside this skill so it travels with it. It holds exactly what a new registry's form layer needs:

```
seed/
  shapes/             # collection body shapes (flavored, shared)
    spec.full.md      #   the Specs collection's default flavor
    spec.micro.md     #   a lighter flavor of the spec
    frame.architecture.md  # the Frames collection's flavors — one per framing doc
    frame.audience.md
    frame.criteria.md
    frame.market.md
  personas/           # response contracts, one per role (installs to _eidos/personas/)
  Registry.md         # version + naming (frontmatter); body indexes Top-Level, Collections, and the property Schema
  user.md             # blank actor frame (installs to _eidos/user.md — personal, gitignored)
  .gitignore          # installs to _eidos/.gitignore (ignores user.md beside it)
  README.md           # the {{Product}} template — installs to <root>/README.md, the visible "start here"
```

It ships as a committed `seed/` in this skill's own folder, kept in sync with the standard's top-level `seed/` (the source of truth and public review surface) by `scripts/sync-skills.sh` — so it's present whether you're in Claude Code or a sandboxed host. Read the version from the seed's `Registry.md`; don't guess it.

## Procedure

1. **Confirm it's a fresh start.** A registry's authoritative marker is an `_eidos/` folder anywhere in the tree (usually `Blueprint/_eidos/`). If one already exists, stop: point the user to `eidos` to author, or `eidos-migrate` if it's on an older version. Install is for empty ground — find a registry by that `_eidos/` marker, not by the default `Blueprint/` name or the presence of a `Specs/` folder.

2. **Name the root.** Default `Blueprint/`; offer to rename. The name is low-stakes — nothing points at it by path, and the skills locate the registry by its `_eidos/`, not its name — so `Abstract/`, `Product/`, or the product's own name all work. For several products in one repo, nest as `Blueprint/<name>/`, each with its own form layer.

3. **Choose the naming convention.** Ask the owner how human-facing names — item files, collection and sub-folders, top-level docs — should read, and record the choice as the `naming` key in `Registry.md`'s frontmatter. Offer the three with `AskUserQuestion`:

   - **Title Case** (default) — `Magic Link Sign-In.md`, `User Management/`. The most readable tree; links encode spaces as `%20`.
   - **TitleCase** — `MagicLinkSignIn.md`, `UserManagement/`. Readable but space-free, for shells and scripts; no `%20` in links.
   - **kebab-case** — `magic-link-signin.md`, `user-management/`. Fully lowercase and space-free; the filename _is_ the `id`.

   It governs the whole registry and is awkward to change later (it means renaming files), so settle it now. If the owner has no preference, take the default — it's the safe one.

4. **Install the form layer.** Copy the seed into the root as a hidden `_eidos/` — everything except `README.md`, which goes to the registry root:

   - `seed/shapes/` → `<root>/_eidos/shapes/` (the collection body shapes — the `spec.*` flavors and the `frame.*` flavors of the Frames collection)
   - `seed/personas/` → `<root>/_eidos/personas/` (the response contracts, committed and team-tunable)
   - `seed/Registry.md` → `<root>/_eidos/Registry.md`, then set its `naming` value to the convention from step 3 (the seed ships `Title Case`). This is the registry's index **and** its property Schema (the `## Schema` section) — no separate Schema file.
   - `seed/user.md` → `<root>/_eidos/user.md` (blank for now — set in step 6)
   - `seed/.gitignore` → `<root>/_eidos/.gitignore` (so the personal `user.md` beside it stays out of version control)
   - `seed/README.md` → `<root>/README.md` (the `{{Product}}` template — the visible "start here"; you fill its product name and one-liner in step 5)

   This is the registry's own copy of the form — the thing every other skill reads from here on. Leave it as the baseline; the owner can extend it later (`eidos-schema` for a custom property, `eidos-registry` for a collection or flavor).

5. **Scaffold the starting collections.** Into the root, name each folder and file in the chosen convention:

   - the default **`Specs` collection**: a `Specs/` folder with a sub-folder per starting domain the owner names (each folder in the chosen convention), and an empty `Specs/index.md` — the generated leaf `eidos-index` fills once items exist. `Specs` and its domains are the **default seed**, not a requirement: the owner can skip domains (a flat collection), rename `Specs`, or add other collections later with `eidos-registry`. Eidos is collections-and-shapes; specs and domains are just where it starts.
   - the **`Frames` collection** (highly encouraged, not required): a `Frames/` folder and an empty `Frames/index.md`. Offer to scaffold the four framing docs — `Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md` — as blank items, each with frontmatter generated from the Schema (`flavor: architecture|audience|criteria|market`, `owner`, `status`, the two dates) and its body from the matching `frame.*` flavor shape, guidance block kept for the owner to work against. A frame scaffolded but not yet filled is fine — it's **in progress**. If the owner would rather start empty, leave `Frames/` bare; frames can be authored later with `eidos`.
   - `README.md` at the registry root (installed in step 4): fill its product name and a one-line "what this is." It is the visible "start here"; keep it thin.
   - the Registry's index — in `<root>/_eidos/Registry.md`, the `## Collections` section already declares `Specs` (with `full`/`micro` flavors) and `Frames` (with its `frame.*` flavors); add a bullet per starting Specs domain under its **Domains**. Leave `## Top-Level` empty (a `<!-- TODO -->` is fine) — top-level docs are the owner's own, added later.

   Don't write items' prose here — `eidos` does that, generating each item's frontmatter from the Schema. And don't invent top-level docs of your own; if the owner wants one (a Roadmap, a Vision), it's free-form with no shape — point them to `eidos-format` to organize a draft. Init just lays the frame.

6. **Set the actor.** Run [`eidos-whoami`](../eidos-whoami) — it offers the installed personas (`_eidos/personas/`), calibrates the chosen one (role, experience with the scope, technical capacity), and writes `_eidos/user.md`. If the owner would rather not say now, leave it blank — an unset actor means full, registry-owner-style facilitation, and they can run `eidos-whoami` later. The file is personal and gitignored, so it is the one piece that isn't committed.

7. **Hand off.** Summarize what was created — the `_eidos/` form layer (shapes, personas, and the `Registry.md` that holds the index plus the property Schema, with the chosen naming convention), the `README.md` front door, and the starting collections (`Specs`, and `Frames` with any blank framing docs) — and point to `eidos` to start authoring. Don't fill them in yourself.

## After init

The registry is plain markdown — commit it alongside the code, `_eidos/` and all, except the personal `_eidos/user.md` that the seeded `.gitignore` keeps out. From here, `eidos` facilitates authoring and validation against the registry's Schema (in `_eidos/Registry.md`); `eidos-schema` adds or changes a custom property; `eidos-registry` adds a collection or flavor and keeps the Registry index current; `eidos-index` rebuilds each collection's `index.md` listing; `eidos-whoami` sets or updates who you are; and `eidos-migrate` moves everything forward when the standard's version changes.
