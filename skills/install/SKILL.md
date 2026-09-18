---
name: install
description: >-
  Stand up a new root in a repo that doesn't have one yet. Use when someone wants to set up Eidos, initialize a product's blueprints, scaffold a framework, "start documenting our product", or says there's no Eidos here yet. It offers the seed frameworks Eidos ships (software, book, research), installs the chosen one into `.eidos/`, and scaffolds a `Blueprints/` around it, following the current `EIDOS.md` — no copying an example and deleting its contents. Trigger on "set up eidos", "init the blueprint", "scaffold our product docs", "we have no specs yet, get us started". For a root that already exists, use `eidos` (author/validate) or `migrate` (version upgrade) instead.
---

# Eidos Install

Create a fresh root: pick a seed framework, install it, scaffold that seed's collections around it. Start from well-formed structure, **not** by copying a worked example and editing over it. Companion to `eidos` — install makes the empty frame, `eidos` helps fill it.

## How you work: facilitate, don't author

Scaffold the structure and bring in the blank templates. Do **not** invent content — intent, scope, and decisions are the owner's. Ask for the few things you need (the seed, the root folder name, the first groups), create the files, hand off to `eidos`. A root full of AI-guessed prose is worse than an empty, honest one.

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
  templates/             # collection body templates, one file per variant (<unit>.<variant>.md)
  roles/              # response contracts, one per role (installs to .eidos/roles/)
  Framework.yaml      # version, naming, top_level, collections, properties, vocabulary (and the index, once blueprints exist)
  me.md               # blank me.md (installs to .eidos/me.md — personal, gitignored)
  .gitignore          # installs to .eidos/.gitignore (ignores me.md and plugins/*/local.yaml)
  README.md           # the {{Product}} template — installs to <root>/README.md, the visible "start here"
```

**Read the seeds at runtime, don't hardcode that table.** `eidos seeds` prints every seed's version, collections, variants, and grouping in one call, so a seed added after this file was written still gets offered. By hand, read only each `Framework.yaml`'s `collections` key: its variants and grouping are everything the offer needs. Take the version from the chosen seed's `Framework.yaml`; don't guess it. The templates wait until step 6, and are read from the installed copy.

## Run the CLI when you can

The `eidos` CLI (npm package `eidosmd`; `npx eidosmd` runs it with nothing installed) performs steps 5 and 6 from the four answers the owner gives you. **Prefer it whenever you have a shell** (Claude Code, the IDE):

```
eidos seeds                                   # every seed: version, collections, variants, grouping
eidos init <root> --seed <seed> --naming "<convention>" --group "<Group>" --product "<Name>"
```

It copies the seed into `<root>/.eidos/`, moves the seed README out to `<root>/README.md`, sets `naming`, renames each collection into the chosen convention (its entry, its folder, and the links that reach it), creates every collection folder, scaffolds one blank blueprint per framing variant (frontmatter from the Properties table, body from that variant's template with its guidance kept), writes an entry per starting group under the grouped collection's `grouping.groups`, and builds the index. `--group` is repeatable and optional; `--dry-run` prints every write and touches nothing.

It deliberately writes **no prose**. The README's one-liner, each group's description, and every scaffolded blueprint's `summary` and body remain the owner's, and its closing report names them as what is still open.

On a **sandboxed host** (Claude Desktop) where you can't run it, install by hand: steps 5 and 6 are exactly what it does.

## Procedure

1. **Confirm it's a fresh start.** Look for an `.eidos/` folder anywhere in the tree — that marker, not a folder name, is what makes a root. If one exists, stop: point the user to `eidos` to author, or `migrate` if it's on an older version.

2. **Choose the seed.** List `seeds/` and offer them with `AskUserQuestion`, describing each from its declared collections, their variants, and how they group. `eidos seeds` prints that for every seed at once; by hand, read only the `collections` key of each seed's `Framework.yaml`. Ask what the owner is actually defining, not which seed they want: "a product being built," "a book or course," "a research question" pick themselves.

   Say plainly that a seed is a **starting point, not a commitment**: everything in it is reshapeable later with `configure`, so one that is merely *close* is a fine choice. If none fit, take the nearest and name the parts they will likely rename. `software` is the default when the owner has no view and the repo is code — don't default silently on a repo that isn't.

3. **Name the root.** Default `Blueprints/`; offer to rename. Low-stakes — nothing points at it by path — so any name works. Several roots in one repo nest as `Blueprints/<name>/`, each with its own `.eidos/`.

4. **Choose the naming convention.** Offer the three with `AskUserQuestion` — **kebab-case** (default; lowercase and space-free, no `%20` in links), **TitleCase** (space-free and capitalized), **Title Case** (reads like prose, `%20` in every link) — and record it as `naming` in `Framework.yaml`. EIDOS.md has the worked table. It governs the whole folder and changing it later means renaming files, so settle it now; the default is the safe answer.

5. **Install the chosen framework.** Copy `seeds/<chosen>/` into the root as a hidden `.eidos/` — everything except `README.md`, which goes to the root:

   - `templates/`, `roles/`, `me.md`, `.gitignore` → straight into `<root>/.eidos/`.
   - `Framework.yaml` → `<root>/.eidos/Framework.yaml`, then set its `naming` to the convention from step 4 (seeds ship `kebab-case`). It carries the top-level docs, the collections, the Properties table (core and custom; no seed ships a tool's block), the Vocabulary, the Versions, and once blueprints exist the index — there is no separate Properties, glossary, or release file.
   - `README.md` → `<root>/README.md`, the visible "start here"; you fill its name and one-liner in step 6.

   Take every file from the **one** seed. Don't mix templates from one with roles from another — a seed's roles are written against its own collections.

   **The seed and the root may be on different machines.** The seed ships inside this skill; the root lives in the user's repo, which on some hosts is reachable only across a device bridge. One filesystem, and a copy (or the script) is the whole job. Across a bridge, **send the seed files with the file-delivery tool and write them to their final paths in a single commit call.** Never re-type a file's contents, base64, or a tarball through a shell heredoc: transcription is lossy, a failed checksum costs the entire round trip, and a staged archive is litter inside someone's repo that you then need permission to delete.

   This is the root's own framework — what every other skill reads from here on. Leave it as the baseline; the owner can extend it later (`configure` for a custom property, a collection, a variant, or a term), and a tool that keeps something in the framework makes its own `.eidos/plugins/<name>/` when first used. No seed ships one. The one personal file a tool may keep there, `local.yaml`, is already covered by the seeded `.gitignore`, so no tool adds a `.gitignore` of its own.

6. **Scaffold the seed's collections.** Read them from the `Framework.yaml` you just installed — never assume `Specs` and `Frames` — and create a folder for each, named in the chosen convention:

   - **the framing collection** (`Frames` in every seed Eidos ships) — the standard doesn't require one, but Eidos recommends it for every product, so it always gets scaffolded: its folder. Offer one blank blueprint per variant the seed declares, reading the variants off `Framework.yaml`, each with frontmatter from the Properties table and its body from that variant's template, italic prompts kept. A frame scaffolded but unfilled is fine; it's in progress.
   - **the grouped collection** — the one the owner will write many of: its folder and a sub-folder per starting group they name. Groups are optional; skipping them gives a flat collection.
   - **`README.md`** at the root: fill its name and a one-line "what this is." Keep it thin.
   - **the framework document** — `collections` already declares the seed's collections; add an entry per starting group under the grouped collection's `grouping.groups` (Domains, Parts, Strands: whatever that seed labels it), each a `name` and a `description` the owner supplies. Leave `top_level` at the README and `vocabulary` empty; top-level docs and terms are the owner's, added later. Then build the `index` (`eidos index`, or by hand as the `index` skill describes) so the scaffolded frames are listed.

   Don't write blueprint prose here — that's `eidos`. Don't invent top-level docs; if the owner wants one, point them at `format`. Install lays the frame.

7. **Set who you are.** Run [`whoami`](../whoami) to pick a role and calibrate it into `.eidos/me.md`. Blank is fine — a blank one means full facilitation, and they can run it later. Personal and gitignored, like a tool's `plugins/<name>/local.yaml`; everything else in `.eidos/` is committed.

8. **Hand off.** Report which seed was installed, what landed in `.eidos/`, the `README.md` front door, and the collections scaffolded — then point to `eidos` to start authoring. Don't fill anything in yourself.

## After init

The folder is plain markdown — commit it alongside the code, `.eidos/` and all, except the personal `me.md` and any tool's `plugins/<name>/local.yaml`, which the seeded `.gitignore` keeps out. From here: `eidos` authors and validates, `configure` adds a collection, variant, or property, `index` rebuilds the index, `whoami` sets who you are, `migrate` moves versions.
