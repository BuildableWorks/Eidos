---
name: eidos-format
description: >-
  Reshape an existing rough draft — a brain-dump, rough notes, or half-formed prose — into Eidos shape, preserving the author's own words and adding nothing. Works on a collection item (a spec or a Frame) or a free-form top-level doc the owner added (a Roadmap, a Vision) — the latter has no shape to match, so it's organized into the house style rather than checked against a shape. Use when someone has already written something and wants it organized, formatted, tidied, cleaned up, or "made to conform" to the shape — e.g. "I brain-dumped a spec, format it", "organize these notes into the Eidos shape", "clean up this spec", "make this match the shape". This is a formatting and organizing pass within a single file, not authoring: it moves and shapes content that is already there. To develop new content with you, use `eidos`; to scaffold an empty registry, use `eidos-install`; to upgrade versions, use `eidos-migrate`.
---

# Eidos Format

Take a file someone has already written — a brain-dump, rough notes, half-formed prose — and reshape it into Eidos shape. You **organize and format**; you do not author. The thinking is already on the page; your job is to give it the registry's structure and make it read well, while keeping the author's words and meaning intact.

This is the companion to `eidos`, which develops content _with_ the user — asking, supplementing, pressing on scope. Reach for `eidos-format` when the content already exists and the user just wants it shaped; reach for `eidos` when there is thinking still to be done.

## The one rule: preserve, don't pad

The author's words carry their intent. Move them into the right place, fix the obvious formatting, and stop.

- **Keep their wording.** Relocate sentences into the section they belong in; tidy grammar and markdown; do not rewrite their voice or inflate three words into a paragraph.
- **Add nothing of substance.** No invented behaviors, intent, decisions, scope, or acceptance criteria. The product decisions that aren't on the page are not yours to make.
- **Surface gaps; don't fill them.** Omit sections that genuinely don't apply (no Open Questions heading when there are none) — the shape is a framework, not a checklist. For a section that clearly _should_ have content but doesn't — Out of Scope most often — keep the heading with a short `<!-- TODO: … -->` and call it out, rather than papering over it with plausible prose. An honest hole beats invented content.
- **Mark anything you inferred.** If you guess a `title`, or group a loose sentence under a heading you picked, flag it so the user can confirm or correct.

A formatting pass that quietly adds content is worse than none: the user stops trusting that the words on the page are theirs.

## Read like a human would read it

Shape the content; don't pour it into a form. The recommended sections are a scaffold — reshape within and beneath them so the result reads like a person wrote it:

- Break rich content out of a single line. A data model belongs in a **table**, a sequence in a **numbered list**, an enumeration in a **bulleted list**.
- Add your own `####` sub-headings inside a section when it has internal structure.
- Keep acceptance criteria short and checkable. When an AC has rich detail behind it, state the AC briefly and put the detail in a table or sub-section the AC points to — never cram `AC1: create X entity with a, b, c, d, e` onto one line.
- Turn references to other items into markdown links — `[Title](path)`, the path in the registry's naming convention (spaces become `%20` only in a Title Case registry), a `#heading` for a section — never bare `code-style` names. Converting a name into a link is formatting, not adding content, so it's squarely in scope.

## What you're reshaping

Two kinds of file land here, and they're reshaped differently:

- **A collection item** — a spec, or a Frame (Architecture, Audience, Criteria, Market) — reshape it toward its collection's flavor shape in `_eidos/shapes/` (the collection's default unless the draft's `flavor` says otherwise), with frontmatter from `_eidos/Registry.md`. The structured case: a spec follows its `spec.*` flavor, a frame its `frame.*` flavor.
- **A free-form top-level doc** the owner has added (a Roadmap, a Vision, a Glossary, the Registry Map) — there is **no shape and none is expected**. Organize the thoughts into the house style — readable headings, tables, lists, links over bare names — and maintain the light top-level-doc frontmatter (`title`, `tags`, `date_created`, `date_modified`). Same spirit as the rules, applied to a doc that is the owner's own structure.

The first shapes _toward_ a flavor; the second only _organizes_. In both you preserve the author's words and add nothing.

## Where the form lives

This skill reads the target shape from the **registry's own `_eidos/`** — it does not carry a template of its own. The file you're reshaping is in the user's project; so is the form you reshape it toward:

- **`_eidos/shapes/`** — collection body shapes, per flavor (`spec.full.md`, `spec.micro.md`, `frame.architecture.md`, …). A frame follows its `frame.*` flavor; a free-form top-level doc has no shape, and that's expected.
- **`_eidos/Registry.md`** — the property contract (its `## Schema` section) for an item's frontmatter; the naming convention (so any link you create uses the registry's filename style — `%20` only in a Title Case registry); and the collections with their flavors, so you know which shape an item follows.

Find `_eidos/` at the registry root in the working directory (by that marker, not the folder name — usually `Blueprint/_eidos/`). **If there is no `_eidos/`, the registry isn't set up — offer `eidos-install` before reshaping**, so you're shaping toward the registry's real form (which may include custom properties or an adjusted section set), not a guess.

## Procedure

1. **Read the whole file first, as-is.** Understand what the author means before moving anything.
2. **Get the form from the registry.** For a collection item (a spec or a frame), open its flavor shape in `_eidos/shapes/` — its collection's default unless its `flavor` says otherwise — and `_eidos/Registry.md` for the frontmatter contract. **A free-form top-level doc has no shape** — skip this and organize by the doc's own logic, keeping only the light frontmatter convention (`title`, `tags`, `date_created`, `date_modified`).
3. **Sort the existing content into sections, using their words.** For a collection item, follow its flavor's shape — for a spec that's Intent (with **Assumptions** nested under it); Open Questions; Behaviors & Acceptance Criteria; Out of Scope; Dependencies; Testing; Constraints & Decisions (a frame's flavor differs — Shape/Components, Audience/User types, and so on). A loose sentence about what it won't do goes to Out of Scope; something you're taking as given goes to Assumptions; something still unanswered goes to Open Questions; an observable outcome becomes an `AC{n}:`. For a free-form top-level doc there are no prescribed sections — group the content under the owner's own headings (or ones you draw from the draft and flag), in a sensible order, without forcing it into the spec sections.
4. **Format for readability, not shape-fidelity.** Tables for data models, lists for enumerations, `####` sub-headings where a section has internal structure. Keep ACs short and labeled; push rich detail into a table or sub-section the AC references.
5. **Fill only derivable frontmatter.** For a collection item, generate the frontmatter keys that apply to the item's collection (from `_eidos/Registry.md`); fill `title` from the document's heading and `date_created`/`date_modified` to today. Leave `id`, `owner`, `domain`, `status`, and any other value for the user where you can't derive them honestly — don't guess a `status`. For a free-form top-level doc there's no Schema to generate from — keep the light top-level-doc frontmatter (`title`, `tags`, `date_created`, `date_modified`), filling `title` and the dates and leaving the rest.
6. **List the gaps and your changes — don't act on them.** The recommended sections left empty (Out of Scope first), anything ambiguous, and any structure you inferred. These are questions for the user, not edits you make silently.
7. **Hand back the reshaped file plus that short list.** The user confirms, fills the gaps, and can take it to `eidos` for deeper work.

## Scope of this skill

- **In scope:** reorganizing and formatting content that already exists, within one file; light grammar and markdown cleanup; readability.
- **Out of scope:** inventing content (use `eidos` to develop it with the user), scaffolding a new registry (`eidos-install`), version migration (`eidos-migrate`).
- If a single dump clearly covers several units of the product, don't silently split it into multiple items — point it out and ask how the user wants it divided.
