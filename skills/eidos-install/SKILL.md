---
name: eidos-install
description: >-
  Stand up a new Eidos definition in a repo that doesn't have one yet. Use when someone wants to set up Eidos, initialize a product/Blueprint, scaffold a framework, "start documenting our product", or says there's no Eidos here yet. It offers the seed frameworks Eidos ships (software, book, research), installs the chosen one into `_eidos/`, and scaffolds a `Blueprint/` around it, following the current `EIDOS.md` — no copying an example and deleting its contents. Trigger on "set up eidos", "init the blueprint", "scaffold our product docs", "we have no specs yet, get us started". For a definition that already exists, use `eidos` (author/validate) or `eidos-migrate` (version upgrade) instead.
---

# Eidos Install

Create a fresh Eidos definition: pick a seed framework, install it, scaffold that seed's collections around it. Start from well-formed structure, **not** by copying a worked example and editing over it. Companion to `eidos` — install makes the empty frame, `eidos` helps fill it.

## How you work: facilitate, don't author

Scaffold the structure and bring in the blank shapes. Do **not** invent content — intent, scope, and decisions are the owner's. Ask for the few things you need (the seed, the root folder name, the first groups), create the files, hand off to `eidos`. A definition full of AI-guessed prose is worse than an empty, honest one.

## Where the seeds live

A committed copy of the standard's **`seeds/`** ships inside this skill, synced by `scripts/sync-skills.sh`, so they are present on a sandboxed host too. Each is a complete framework, and every skill treats them interchangeably:

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

**Read the seeds at runtime, don't hardcode that table.** List `seeds/` and read each `Framework.md`'s `## Collections`, so a seed added after this file was written still gets offered. Take the version from the chosen seed's `Framework.md`; don't guess it.

## Procedure

1. **Confirm it's a fresh start.** Look for an `_eidos/` folder anywhere in the tree — that marker, not a folder name, is what makes a definition. If one exists, stop: point the user to `eidos` to author, or `eidos-migrate` if it's on an older version.

2. **Choose the seed.** List `seeds/` and offer them with `AskUserQuestion`, describing each from its own `Framework.md` — its collections, their flavors, and how they group. Ask what the owner is actually defining, not which seed they want: "a product being built," "a book or course," "a research question" pick themselves.

   Say plainly that a seed is a **starting point, not a commitment**: everything in it is reshapeable later with `eidos-configure`, so one that is merely *close* is a fine choice. If none fit, take the nearest and name the parts they will likely rename. `software` is the default when the owner has no view and the repo is code — don't default silently on a repo that isn't.

3. **Name the root.** Default `Blueprint/`; offer to rename. Low-stakes — nothing points at it by path — so any name works. Several definitions in one repo nest as `Blueprint/<name>/`, each with its own `_eidos/`.

4. **Choose the naming convention.** Offer the three with `AskUserQuestion` — **Title Case** (default, most readable, `%20` in links), **TitleCase** (space-free, for shells and scripts), **kebab-case** (lowercase and space-free; the filename *is* the `id`) — and record it as `naming` in `Framework.md`'s frontmatter. EIDOS.md has the worked table. It governs the whole definition and changing it later means renaming files, so settle it now; the default is the safe answer.

5. **Install the chosen framework.** Copy `seeds/<chosen>/` into the root as a hidden `_eidos/` — everything except `README.md`, which goes to the definition root:

   - `shapes/`, `personas/`, `user.md`, `.gitignore` → straight into `<root>/_eidos/`.
   - `Framework.md` → `<root>/_eidos/Framework.md`, then set its `naming` to the convention from step 4 (seeds ship `Title Case`). It carries the index **and** the property Schema — there is no separate Schema file.
   - `README.md` → `<root>/README.md`, the visible "start here"; you fill its name and one-liner in step 6.

   Take every file from the **one** seed. Don't mix shapes from one with personas from another — a seed's personas are written against its own collections.

   This is the definition's own framework — the thing every other skill reads from here on. Leave it as the baseline; the owner can extend it later (`eidos-configure` for a custom property, a collection, or a flavor).

6. **Scaffold the seed's collections.** Read them from the `Framework.md` you just installed — never assume `Specs` and `Frames` — and create a folder for each, named in the chosen convention:

   - **the framing collection** (`Frames` in every seed Eidos ships) — every framework declares one, so it always gets scaffolded: its folder and an empty `index.md`. Offer one blank item per flavor the seed declares, reading the flavors off `Framework.md`, each with frontmatter from the Schema and its body from that flavor's shape, guidance block kept. A frame scaffolded but unfilled is fine; it's in progress.
   - **the grouped collection** — the one the owner will write many of: its folder, a sub-folder per starting group they name, and an empty `index.md`. Groups are optional; skipping them gives a flat collection.
   - **`README.md`** at the definition root: fill its name and a one-line "what this is." Keep it thin.
   - **the Framework's index** — `## Collections` already declares the seed's collections; add a bullet per starting group under the grouped collection's grouping line (**Domains**, **Parts**, **Strands** — whatever that seed calls it). Leave `## Top-Level` empty; top-level docs are the owner's, added later.

   Don't write item prose here — that's `eidos`. Don't invent top-level docs; if the owner wants one, point them at `eidos-format`. Install lays the frame.

7. **Set the actor.** Run [`eidos-whoami`](../eidos-whoami) to pick a persona and calibrate it into `_eidos/user.md`. Blank is fine — an unset actor means full facilitation, and they can run it later. Personal and gitignored, the one piece not committed.

8. **Hand off.** Report which seed was installed, what landed in `_eidos/`, the `README.md` front door, and the collections scaffolded — then point to `eidos` to start authoring. Don't fill anything in yourself.

## After init

The definition is plain markdown — commit it alongside the code, `_eidos/` and all, except the personal `user.md` the seeded `.gitignore` keeps out. From here: `eidos` authors and validates, `eidos-configure` adds a collection, flavor, or property, `eidos-index` rebuilds the leaves, `eidos-whoami` sets the actor, `eidos-migrate` moves versions.
