---
name: eidos-init
description: >-
  Stand up a new Eidos registry in a repo that doesn't have one yet. Use when someone wants to set up Eidos, initialize a product/Blueprint, scaffold a spec registry, "start documenting our product", or says there's no Eidos here yet. It installs the `.eidos/` form layer (the shapes and property Schema) and scaffolds a `Blueprint/`, following the current `EIDOS.md` — no copying the example and deleting its contents. Trigger on "set up eidos", "init the blueprint", "scaffold our product docs", "we have no specs yet, get us started". For a registry that already exists, use `eidos` (author/validate) or `eidos-migrate` (version upgrade) instead.
---

# Eidos Init

Create a fresh Eidos registry: install the form layer, then scaffold the blank product docs around it. The point is to start from well-formed structure — **not** by copying the worked example and editing over it.

This is the companion to `eidos` (which authors and validates specs once the registry exists). Init makes the empty frame; `eidos` helps fill it.

## How you work: facilitate, don't author

Scaffold the structure and bring in the blank shapes. Do **not** invent the product's content — Intent, scope, audience, and decisions are the owner's. Ask for the few things you need (the root folder name, the first domains), create the files, and hand off to `eidos` for authoring. A registry full of AI-guessed prose is worse than an empty, honest one.

## Where the seed lives

The canonical seed is the standard's — public and front-facing at the top level as **`standard-seed/`**, and shipped as a committed copy inside this skill so it travels with it. It holds exactly what a new registry's form layer needs:

```
standard-seed/
  shapes/          # the body template for each kind of document
    Spec.md
    Architecture.md
    Audience.md
    Criteria.md
    Market.md
    Domains.md
  Schema.md        # the canonical property contract (Eidos 3.0.0) + an empty custom block
  Registry.md      # the Eidos version + naming convention this registry will target
```

It ships as a committed `standard-seed/` in this skill's own folder, kept in sync with the standard's top-level `standard-seed/` (the source of truth and public review surface) by `scripts/sync-skills.sh` — so it's present whether you're in Claude Code or a sandboxed host. Read the version from its `Registry.md`; don't guess it.

## Procedure

1. **Confirm it's a fresh start.** If a registry already exists (a `.eidos/` anywhere, a `Blueprint/`, or any `Specs/` folder), stop: point the user to `eidos` to author, or `eidos-migrate` if it's on an older version. Init is for empty ground. (The skills find a registry by its `.eidos/` marker, so look for that, not only the default name.)

2. **Name the root.** Default `Blueprint/`; offer to rename. The name is low-stakes — nothing points at it by path, and the skills locate the registry by its `.eidos/`, not its name — so `Abstract/`, `Product/`, or the product's own name all work. For several products in one repo, nest as `Blueprint/<name>/`, each with its own form layer.

3. **Choose the naming convention.** Ask the owner how human-facing names — spec files, domain folders, product docs — should read, and record the choice as the `naming` key in `Registry.md`'s frontmatter. Offer the three with `AskUserQuestion`:

   - **Title Case** (default) — `Magic Link Sign-In.md`, `User Management/`. The most readable tree; links encode spaces as `%20`.
   - **TitleCase** — `MagicLinkSignIn.md`, `UserManagement/`. Readable but space-free, for shells and scripts; no `%20` in links.
   - **kebab-case** — `magic-link-signin.md`, `user-management/`. Fully lowercase and space-free; the filename _is_ the `id`.

   It governs the whole registry and is awkward to change later (it means renaming files), so settle it now. If the owner has no preference, take the default — it's the safe one.

4. **Install the form layer.** Copy the seed into the root as a hidden `.eidos/`:

   - `standard-seed/shapes/` → `<root>/.eidos/shapes/`
   - `standard-seed/Schema.md` → `<root>/.eidos/Schema.md`
   - `standard-seed/Registry.md` → `<root>/.eidos/Registry.md`, then set its `naming` value to the convention from step 3 (the seed ships `Title Case`).

   This is the registry's own copy of the shapes and the property contract — the thing every other skill reads from here on. Leave it as the baseline; the owner can extend it later (`eidos-property` for a custom property).

5. **Scaffold the product docs from the installed shapes.** Into the root, create from `<root>/.eidos/shapes/`, naming each file in the chosen convention:

   - `Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md` — from their matching shape, keeping the guidance block for the owner to work against (or stripping it on request). Set `created`/`modified` to today; leave the prose for the human.
   - `Domains.md` — from the `Domains.md` shape.
   - a `Specs/` folder, with a sub-folder per starting domain the owner names (each folder in the chosen convention).

   Don't write specs here — `eidos` does that, generating each spec's frontmatter from the Schema. And don't invent top-level docs of your own; if the owner wants one (a Roadmap, a Vision), it's free-form with no shape — point them to `eidos-format` to organize a draft. Init just lays the frame.

6. **Hand off.** Summarize what was created — the `.eidos/` form layer (with the chosen naming convention) and the blank product docs — and point to `eidos` to start authoring. Don't fill them in yourself.

## After init

The registry is plain markdown — commit it alongside the code, `.eidos/` and all. From here, `eidos` facilitates authoring and validation against `.eidos/Schema.md`; `eidos-property` adds or changes a custom property; `eidos-domains` keeps `Domains.md` a live map of the specs; and `eidos-migrate` moves everything forward when the standard's version changes.
