---
name: format
description: >-
  Reshape an existing rough draft — a brain-dump, rough notes, or half-formed prose — into Eidos shape, preserving the author's own words and adding nothing. Works on a collection blueprint, or a free-form top-level doc the owner added (a Roadmap, a Vision) — the latter has no shape to match, so it's organized into the house style rather than checked against a shape. Use when someone has already written something and wants it organized, formatted, tidied, cleaned up, or "made to conform" to the shape — e.g. "I brain-dumped a spec, format it", "organize these notes into the Eidos shape", "clean up this doc", "make this match the shape". This is a formatting and organizing pass within a single file, not authoring: it moves and shapes content that is already there. To develop new content with you, use `eidos`; to scaffold an empty folder, use `install`; to upgrade versions, use `migrate`.
---

# Eidos Format

Take a file someone has already written — a brain-dump, rough notes, half-formed prose — and reshape it into Eidos shape. You **organize and format**; you do not author. The thinking is already on the page; give it the framework's structure and make it read well, keeping the author's words intact.

Companion to `eidos`, which develops content _with_ the user. Reach for this one when the content exists and just needs shaping; reach for `eidos` when there is thinking still to do, or `iterate` when the idea itself is not settled yet.

## The one rule: preserve, don't pad

The author's words carry their intent. Move them into the right place, fix the obvious formatting, and stop.

- **Keep their wording.** Relocate sentences into the section they belong in; tidy grammar and markdown; do not rewrite their voice or inflate three words into a paragraph.
- **Add nothing of substance.** No invented behaviors, intent, decisions, scope, or acceptance criteria. The product decisions that aren't on the page are not yours to make.
- **Surface gaps; don't fill them.** Omit a section with nothing under it — the shape is a scaffold, not a checklist. For one that clearly _should_ have content, most often the shape's non-goals section, keep the heading with a short `<!-- TODO: … -->` and call it out. An honest hole beats invented content.
- **Mark anything you inferred.** If you guess a `title`, or group a loose sentence under a heading you picked, flag it so the user can confirm or correct.

A formatting pass that quietly adds content is worse than none: the user stops trusting that the words on the page are theirs.

## Read like a human would read it

Shape the content; don't pour it into a form. The recommended sections are a scaffold — reshape within and beneath them so the result reads like a person wrote it:

- Break rich content out of a single line. A data model belongs in a **table**, a sequence in a **numbered list**, an enumeration in a **bulleted list**.
- Add your own `####` sub-headings inside a section when it has internal structure.
- Keep checkable statements short. When one has rich detail behind it, state it briefly and point at a table or sub-section — never cram the whole thing onto one line.
- Turn references to other blueprints into markdown links — `[Title](path)`, the path in the framework's naming convention (kebab-case by default; spaces become `%20` only in a Title Case tree), a `#heading` for a section — never bare `code-style` names. Converting a name into a link is formatting, not adding content, so it's squarely in scope.

## What you're reshaping

Two kinds of file land here, and they're reshaped differently:

- **A collection blueprint** — reshape it *toward* its flavor's shape in `_eidos/shapes/` (the collection's default unless the draft's `flavor` says otherwise), with frontmatter from `_eidos/Framework.md`.
- **A free-form top-level doc** (a Roadmap, a Vision, a Glossary) — **no shape, and none expected.** Only *organize*: readable headings, tables, lists, links over bare names, plus the light frontmatter (`title`, `tags`, `date_created`, `date_modified`).

In both you preserve the author's words and add nothing.

This skill carries no template of its own — it reads the shape, the Schema, and the naming convention from the root's own `_eidos/`, found by that marker rather than a folder name. **No `_eidos/` means no framework is installed — offer `install` before reshaping**, so you shape toward the framework's real form rather than a guess.

## Procedure

1. **Read the whole file first, as-is.** Understand what the author means before moving anything.
2. **Get the form from the framework.** For a collection blueprint, open its flavor shape in `_eidos/shapes/` — its collection's default unless its `flavor` says otherwise — and `_eidos/Framework.md` for the frontmatter contract. **A free-form top-level doc has no shape** — skip this and organize by the doc's own logic, keeping only the light frontmatter convention (`title`, `tags`, `date_created`, `date_modified`).
3. **Sort the existing content into sections, using their words.** For a collection blueprint, **read the section names off its flavor's shape, never from memory** — a shape you have seen before tells you nothing about this one. Then route by meaning: a sentence about what it won't do belongs in the shape's non-goals section, something taken as given in its assumptions section, something unanswered in its open-questions section, an observable outcome among its checkable statements. Where the shape has no home for a passage, say so rather than inventing a heading. For a free-form top-level doc there are no prescribed sections — group under the owner's own headings, or ones you draw from the draft and flag.
4. **Format for readability, not shape-fidelity.** Tables for structured data, lists for enumerations, `####` sub-headings where a section has internal structure. Keep checkable statements short and labeled the way the shape asks; push detail into something they point at.
5. **Fill only derivable frontmatter.** For a collection blueprint, generate the frontmatter keys that apply to the blueprint's collection (from `_eidos/Framework.md`); fill `title` from the document's heading and `date_created`/`date_modified` to today. Leave `id` and any value you can't derive honestly for the user — never guess a lifecycle or a grouping. For a free-form top-level doc there's no Schema to generate from — keep the light top-level-doc frontmatter (`title`, `tags`, `date_created`, `date_modified`), filling `title` and the dates and leaving the rest.
6. **List the gaps and your changes — don't act on them.** The shape's sections left empty (its non-goals section first), anything ambiguous, and any structure you inferred. These are questions for the user, not edits you make silently.
7. **Hand back the reshaped file plus that short list.** The user confirms, fills the gaps, and can take it to `eidos` for deeper work.

## Scope of this skill

- **In scope:** reorganizing and formatting content that already exists, within one file; light grammar and markdown cleanup; readability.
- **Out of scope:** inventing content (use `eidos` to develop it with the user), scaffolding a new folder (`install`), version migration (`migrate`).
- If a single dump clearly covers several units of the product, don't silently split it into multiple blueprints — point it out and ask how the user wants it divided.
