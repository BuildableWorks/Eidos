---
name: eidos-install
description: >-
  Stand up a new Eidos definition in a repo that doesn't have one yet. Use when someone wants to set up Eidos, initialize a product/Blueprint, scaffold a framework, "start documenting our product", or says there's no Eidos here yet. It offers the seed frameworks Eidos ships (software, book, research), installs the chosen one into `_eidos/`, and scaffolds a `Blueprint/` around it, following the current `EIDOS.md` — no copying an example and deleting its contents. Trigger on "set up eidos", "init the blueprint", "scaffold our product docs", "we have no specs yet, get us started". For a definition that already exists, use `eidos` (author/validate) or `eidos-migrate` (version upgrade) instead.
---

# Eidos Install

Create a fresh Eidos definition: pick a seed framework, install it, then scaffold that seed's collections around it. The point is to start from well-formed structure — **not** by copying the worked example and editing over it.

This is the companion to `eidos` (which authors and validates items once the definition exists). Init makes the empty frame; `eidos` helps fill it.

## How you work: facilitate, don't author

Scaffold the structure and bring in the blank shapes. Do **not** invent the product's content — Intent, scope, audience, and decisions are the owner's. Ask for the few things you need (the seed, the root folder name, and the first groups for its grouped collection), create the files, and hand off to `eidos` for authoring. A definition full of AI-guessed prose is worse than an empty, honest one.

## Where the seeds live

The canonical seeds are the standard's — public and front-facing at the top level as **`seeds/`**, and shipped as a committed copy inside this skill so they travel with it. Each seed is a complete framework, and they are interchangeable as far as every skill is concerned:

| Seed | For | Collections |
| --- | --- | --- |
| `software` | a product, service, or system being built | `Frames` (architecture, audience, criteria, market) · `Specs` by domain |
| `book` | a book, long-form argument, or course | `Frames` (premise, reader, voice, market) · `Chapters` by part |
| `research` | a question, a study, or a programme of inquiry | `Frames` (question, prior work, method, ethics) · `Investigations` by strand |

Every seed carries the same pieces, in the same layout:

```
seeds/<seed>/
  shapes/             # collection body shapes, one file per flavor (<kind>.<flavor>.md)
  personas/           # response contracts, one per role (installs to _eidos/personas/)
  Framework.md        # version + naming (frontmatter); body indexes Top-Level, Collections, and the property Schema
  user.md             # blank actor frame (installs to _eidos/user.md — personal, gitignored)
  .gitignore          # installs to _eidos/.gitignore (ignores user.md beside it)
  README.md           # the {{Product}} template — installs to <root>/README.md, the visible "start here"
```

They ship as a committed `seeds/` in this skill's own folder, kept in sync with the standard's top-level `seeds/` (the source of truth and public review surface) by `scripts/sync-skills.sh` — so they're present whether you're in Claude Code or a sandboxed host. Read the version from the chosen seed's `Framework.md`; don't guess it.

**Read the seeds at runtime, don't hardcode this table.** List `seeds/` and read each `Framework.md`'s `## Collections`, so a seed added after this file was written still gets offered.

## Procedure

1. **Confirm it's a fresh start.** A definition's authoritative marker is an `_eidos/` folder anywhere in the tree (usually `Blueprint/_eidos/`). If one already exists, stop: point the user to `eidos` to author, or `eidos-migrate` if it's on an older version. Install is for empty ground — find a definition by that `_eidos/` marker, not by the default `Blueprint/` name or by any folder that looks like a collection.

2. **Choose the seed.** List `seeds/` and offer them with `AskUserQuestion`, describing each from its own `Framework.md` — its collections, their flavors, and how they group. Ask what the owner is actually defining, not which seed they want: "a product being built," "a book or course," "a research question" pick themselves.

   A seed is a **starting point, not a commitment** — say so. Every collection, flavor, property, and persona can be reshaped later with `eidos-configure`, and nothing in Eidos knows a collection by name, so a seed that is *close* is a fine choice. If none of them fit, take the nearest and tell the owner which parts they will likely rename.

   `software` is the default when the owner has no view and the repo is code. Don't default silently on a repo that isn't.

3. **Name the root.** Default `Blueprint/`; offer to rename. The name is low-stakes — nothing points at it by path, and the skills locate the definition by its `_eidos/`, not its name — so `Abstract/`, `Product/`, or the product's own name all work. For several products in one repo, nest as `Blueprint/<name>/`, each with its own form layer.

4. **Choose the naming convention.** Ask the owner how human-facing names — item files, collection and sub-folders, top-level docs — should read, and record the choice as the `naming` key in `Framework.md`'s frontmatter. Offer the three with `AskUserQuestion`:

   - **Title Case** (default) — `Magic Link Sign-In.md`, `User Management/`. The most readable tree; links encode spaces as `%20`.
   - **TitleCase** — `MagicLinkSignIn.md`, `UserManagement/`. Readable but space-free, for shells and scripts; no `%20` in links.
   - **kebab-case** — `magic-link-signin.md`, `user-management/`. Fully lowercase and space-free; the filename _is_ the `id`.

   It governs the whole definition and is awkward to change later (it means renaming files), so settle it now. If the owner has no preference, take the default — it's the safe one.

5. **Install the chosen framework.** Copy `seeds/<chosen>/` into the root as a hidden `_eidos/` — everything except `README.md`, which goes to the definition root:

   - `seeds/<chosen>/shapes/` → `<root>/_eidos/shapes/` (the collection body shapes, one file per flavor)
   - `seeds/<chosen>/personas/` → `<root>/_eidos/personas/` (the response contracts, committed and team-tunable)
   - `seeds/<chosen>/Framework.md` → `<root>/_eidos/Framework.md`, then set its `naming` value to the convention from step 4 (every seed ships `Title Case`). This is the framework's index **and** its property Schema (the `## Schema` section) — no separate Schema file.
   - `seeds/<chosen>/user.md` → `<root>/_eidos/user.md` (blank for now — set in step 7)
   - `seeds/<chosen>/.gitignore` → `<root>/_eidos/.gitignore` (so the personal `user.md` beside it stays out of version control)
   - `seeds/<chosen>/README.md` → `<root>/README.md` (the `{{Product}}` template — the visible "start here"; you fill its product name and one-liner in step 6)

   Take every file from the **one** seed. Don't mix shapes from one with personas from another — a seed's personas are written against its own collections and frames.

   This is the definition's own framework — the thing every other skill reads from here on. Leave it as the baseline; the owner can extend it later (`eidos-configure` for a custom property, a collection, or a flavor).

6. **Scaffold the seed's collections.** Read them from the `Framework.md` you just installed — never assume `Specs` and `Frames` — and create a folder for each, named in the chosen convention:

   - **the grouped collection** — the one whose items the owner will write many of (`Specs` in software, `Chapters` in book, `Investigations` in research): its folder, a sub-folder per starting group the owner names (each in the chosen convention), and an empty `index.md` — the generated leaf `eidos-index` fills once items exist. The owner can skip the groups entirely for a flat collection.
   - **the framing collection** (`Frames` in every seed Eidos ships; highly encouraged, not required): its folder and an empty `index.md`. Offer to scaffold one blank item per flavor the seed declares — read the flavors off `Framework.md` rather than assuming a set — each with frontmatter generated from the Schema (`flavor:` its kind, plus whatever else applies) and its body from that flavor's shape, guidance block kept for the owner to work against. A frame scaffolded but not yet filled is fine — it's **in progress**. If the owner would rather start empty, leave the folder bare.
   - `README.md` at the definition root (installed in step 5): fill its product name and a one-line "what this is." It is the visible "start here"; keep it thin.
   - the Framework's index — in `<root>/_eidos/Framework.md`, the `## Collections` section already declares the seed's collections, their flavors, and how each draws on the canvas; add a bullet per starting group under the grouped collection's grouping line (**Domains**, **Parts**, **Strands** — whatever that seed calls it). Leave `## Top-Level` empty (a `<!-- TODO -->` is fine) — top-level docs are the owner's own, added later.

   Don't write items' prose here — `eidos` does that, generating each item's frontmatter from the Schema. And don't invent top-level docs of your own; if the owner wants one (a Roadmap, a Vision), it's free-form with no shape — point them to `eidos-format` to organize a draft. Init just lays the frame.

7. **Set the actor.** Run [`eidos-whoami`](../eidos-whoami) — it offers the installed personas (`_eidos/personas/`), calibrates the chosen one (role, experience with the scope, technical capacity), and writes `_eidos/user.md`. If the owner would rather not say now, leave it blank — an unset actor means full, framework-owner-style facilitation, and they can run `eidos-whoami` later. The file is personal and gitignored, so it is the one piece that isn't committed.

8. **Hand off.** Summarize what was created — which seed was installed, the `_eidos/` framework (shapes, personas, and the `Framework.md` that holds the index plus the property Schema, with the chosen naming convention), the `README.md` front door, and the starting collections with any blank framing docs — and point to `eidos` to start authoring. Don't fill them in yourself.

## After init

The definition is plain markdown — commit it alongside the code, `_eidos/` and all, except the personal `_eidos/user.md` that the seeded `.gitignore` keeps out. From here, `eidos` facilitates authoring and validation against the framework's Schema (in `_eidos/Framework.md`); `eidos-configure` adds or changes a custom property, adds a collection or flavor, and keeps the Framework index current; `eidos-index` rebuilds each collection's `index.md` listing; `eidos-whoami` sets or updates who you are; and `eidos-migrate` moves everything forward when the standard's version changes.
