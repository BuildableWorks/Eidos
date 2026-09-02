---
# The Eidos version this framework targets; migrate reads and bumps it.
eidos_version: 4.4.0
# How files, folders, and links are named: kebab-case | TitleCase | Title Case. Absent = kebab-case.
naming: kebab-case
---

# Framework

The framework's index and config, in one place: the version and naming convention above, and below the
Top-Level documents, the Collections (with their flavors and grouping), and the property Schema. The
visible `README.md` at the definition root is the friendly door to it; keep it current with the
`configure` skill.

## Top-Level

<!-- configure: top-level index (regenerated) -->
- [README](../README.md) — the definition's front door: what this book is, and pointers in.
<!-- One bullet per top-level document. README is the door and comes first; add your own below (an
     Outline, a Synopsis, the generated Framework Map canvas), each a link and a one-line description.
     The framing docs live in the Frames collection, not here. configure refreshes this list. -->

## Collections

A collection is a top-level folder of repeated items that share a body shape. `Frames` holds the
framing docs — the most primary thing the definition says about itself — and `Chapters` the book's
units. Add more with `configure`. Each lists its flavors (the default marked), how it draws on
the canvas, and its grouping, and points at its generated `index.md` leaf.

### Frames

The framing docs that set what every chapter is judged against — what the book argues, who it is for,
how it sounds, and where it sits. This framework's framing collection; each frame follows the flavor
of its kind, and one left unwritten is a gap to surface, not a failure.

- **Leaf:** [Frames/index.md](../Frames/index.md)
- **Flavors:**
  - [premise](shapes/frame.premise.md) — what the book says, and why it has to exist (default).
  - [reader](shapes/frame.reader.md) — who it is for, and what changes for them.
  - [voice](shapes/frame.voice.md) — person, tense, register, and the rules the prose keeps.
  - [market](shapes/frame.market.md) — shelf, comparables, and how it reaches readers.
- **Canvas:** file

### Chapters

The book's units, one per chapter, grouped by part.

- **Leaf:** [Chapters/index.md](../Chapters/index.md)
- **Flavors:**
  - [full](shapes/chapter.full.md) — the complete chapter shape (default).
  - [sketch](shapes/chapter.sketch.md) — Intent, Open Questions, What Happens, Out of Scope; grow into full.
- **Canvas:** card from `## Intent`
- **Parts:** _(add one bullet per part — a name and a short description — as parts accrue)_

## Schema

The property contract — what an item's frontmatter may carry, across every collection. Two parts: the
**core** properties Eidos's own machinery uses, and the **custom** ones you (or the seed) add. Every
custom property declares which collections it **applies to** — `all`, or a list — so a property never
lands where it makes no sense (`part` is Chapters-only). A property's type comes from the Obsidian set
(Text, List, Number, Checkbox, Date, Date & time), so frontmatter renders natively in an Obsidian
vault. The `configure` skill edits this section.

### Eidos Core

_Present on every item. Managed by the standard (Eidos 4.4.0); `migrate` rewrites this block on a version change — don't hand-edit it. (`flavor` absent = the collection's default; `connects_to` absent = no canvas edges; a missing `summary` is flagged by the index.)_

| Name        | Type | Meaning                                                                                        |
| ----------- | ---- | ---------------------------------------------------------------------------------------------- |
| id          | Text | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it.      |
| title       | Text | Human-readable name.                                                                           |
| summary     | Text | One plain line — what this item is, in a sentence, distilled from Intent. Source for the collection index.md listing; absent, the index flags it. |
| flavor      | Text | Which body flavor this item follows, from its collection's declared flavors. Absent = the collection's default flavor. |
| connects_to | List | Items this one connects to on the definition's canvas, each a markdown link; drawn as a directed edge (this → target). The intentional map, distinct from depends_on. |

### Custom Properties

_Yours to shape with the `configure` skill. The seed ships a few useful defaults below — keep, scope, or drop any of them; Eidos doesn't depend on them. Absence where a property applies is a soft gap the validator notes, never refuses._

| Name          | Type | Applies To | Meaning                                                                                    |
| ------------- | ---- | ---------- | ------------------------------------------------------------------------------------------ |
| status        | Text | all        | Lifecycle value: Draft / Outlined / Drafted / Revised / Final / Cut. An off-list value warns. |
| date_created  | Date | all        | YYYY-MM-DD. The day the item was first written. Set once.                                   |
| date_modified | Date | all        | YYYY-MM-DD. The day the item was last changed.                                              |
| tags          | List | all        | Free tags.                                                                                  |
| part          | Text | Chapters   | The grouping, matching the item's sub-folder under its collection in the naming convention. An unknown value warns, never fails. |
| depends_on    | List | Chapters   | Chapters a reader must have read first, each a markdown link. A reading dependency, not a canvas edge. |
