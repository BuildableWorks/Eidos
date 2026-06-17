---
name: eidos-init
description: >-
  Stand up a new Eidos registry in a repo that doesn't have one yet. Use when someone wants to set up Eidos, initialize a product/Blueprint, scaffold a spec registry, "start documenting our product", or says there's no Eidos here yet. It scaffolds a `Blueprint/` from the standard's templates, following the current `EIDOS.md` — no copying the example and deleting its contents. Trigger on "set up eidos", "init the blueprint", "scaffold our product docs", "we have no specs yet, get us started". For a registry that already exists, use `eidos` (author/validate) or `eidos-migrate` (version upgrade) instead.
---

# Eidos Init

Create a fresh Eidos registry from the standard's templates, following the current `EIDOS.md`. The point is to start from blank, well-formed structure — **not** by copying the worked example and editing over it.

This is the companion to `eidos` (which authors and validates specs once the registry exists). Init makes the empty frame; `eidos` helps fill it.

## How you work: facilitate, don't author

Scaffold the structure and bring in the blank templates. Do **not** invent the product's content — Intent, scope, audience, and decisions are the owner's. Ask for the few things you need (the root folder name, the first domains), create the files, and hand off to `eidos` for authoring. A registry full of AI-guessed prose is worse than an empty, honest one.

## Where the standard lives

This skill reads two things from the standard — the templates and the contract. Find them in whichever location exists:

- **`${CLAUDE_PLUGIN_ROOT}/`** (installed as the plugin) — `${CLAUDE_PLUGIN_ROOT}/templates/` and `${CLAUDE_PLUGIN_ROOT}/EIDOS.md`.
- **This skill's own `templates/` and `EIDOS.md`** — present when the skill was made standalone by `scripts/sync-skills.sh`. These are gitignored, so run that script first if the folders are empty.
- **The repo's top-level `templates/` and `EIDOS.md`** — when working inside the standard's own repo.

`EIDOS.md` is the current contract: layout, frontmatter fields, body sections, and the version in its `**Version:**` header. `templates/` holds the blank fill-in templates. Never guess the contract — read it.

## Procedure

1. **Confirm it's a fresh start.** If a registry already exists (a `Blueprint/` or any `Specs/` folder), stop: point the user to `eidos` to author, or `eidos-migrate` if it's on an older version. Init is for empty ground.

2. **Read the standard.** Open `EIDOS.md` for the current layout, the frontmatter contract (including `eidos_version`), and the body sections. Note the version in its header — every doc you create will carry that as `eidos_version`.

3. **Name the root.** Default `Blueprint/`; offer to rename (the name is low-stakes — nothing points at it by path). For several products in one repo, nest as `Blueprint/<name>/`.

4. **Scaffold from the templates.** Into the root, place:

   - `Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md` — from their `templates/*.md`.
   - `Domains.md` — from `templates/Domains Template.md`.
   - a `Specs/` folder, with a sub-folder per starting domain the owner names. Keep each template's guidance block for the owner to work against (or strip it on request). Set `created`/`modified` to today and `eidos_version` to the version from `EIDOS.md`. Leave the prose for the human.

5. **Hand off.** Summarize what was created and point to `eidos` to start authoring the product docs and the first specs. Don't fill them in yourself.

## After init

The registry is plain markdown — commit it alongside the code. From here, `eidos` facilitates authoring and validation, and `eidos-migrate` moves everything forward when the standard's version changes.
