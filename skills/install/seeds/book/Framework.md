---
# The Eidos version this framework targets; migrate reads and bumps it.
eidos_version: 4.7.0
# How files, folders, and links are named: kebab-case | TitleCase | Title Case. Absent = kebab-case.
naming: kebab-case
---

# Framework

The framework's index and config, in one place: the version and naming convention above, and below the
Top-Level documents, the Collections (with their flavors and grouping), the property Schema, the
Vocabulary, and the Versions. The visible `README.md` at the root is the friendly door to it; keep
it current with the `configure` skill.

## Top-Level

<!-- configure: top-level index (regenerated) -->
- [README](../README.md) — the root's front door: what this book is, and pointers in.
<!-- One bullet per top-level document. README is the door and comes first; add your own below (an
     Outline, a Synopsis, a map a tool generates), each a link and a one-line description.
     The framing docs live in the Frames collection, not here. configure refreshes this list. -->

## Collections

A collection is a top-level folder of repeated blueprints that share a body shape. `Frames` holds the
framing docs — what the root says first about the product — and `Chapters` the book's
units. Add more with `configure`. Each lists its flavors (the default marked) and its grouping, and points at its generated `index.md` leaf.

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

### Chapters

The book's units, one per chapter, grouped by part.

- **Leaf:** [Chapters/index.md](../Chapters/index.md)
- **Flavors:**
  - [full](shapes/chapter.full.md) — the complete chapter shape (default).
  - [sketch](shapes/chapter.sketch.md) — Intent, Open Questions, What Happens, Out of Scope; grow into full.
- **Parts:** _(add one bullet per part — a name and a short description — as parts accrue)_

## Schema

The property contract — what a blueprint's frontmatter may carry, across every collection. One block per
owner: the **core** properties Eidos's own machinery uses, the **custom** ones you (or the seed) add, and a
`### <tool> Properties` block for any tool that declares properties of its own (none ship with a seed). Every
custom property declares which collections it **applies to** — `all`, or a list — so a property never
lands where it makes no sense (`part` is Chapters-only). A property's type comes from the Obsidian set
(Text, List, Number, Checkbox, Date, Date & time), so frontmatter renders natively in an Obsidian
vault. The `configure` skill edits this section.

### Eidos Core

_Present on every blueprint. Managed by the standard (Eidos 4.7.0); `migrate` rewrites this block on a version change — don't hand-edit it. (`flavor` absent = the collection's default; a missing `summary` is flagged by the index.)_

| Name        | Type | Meaning                                                                                        |
| ----------- | ---- | ---------------------------------------------------------------------------------------------- |
| id          | Text | Stable, unique identity, in any form: a slug, a number, a GUID. Assigned once, never changed. References point at it. |
| title       | Text | Human-readable name.                                                                           |
| summary     | Text | One plain line — what this blueprint is, in a sentence, distilled from Intent. Source for the collection index.md listing; absent, the index flags it. |
| flavor      | Text | Which body flavor this blueprint follows, from its collection's declared flavors. Absent = the collection's default flavor. |

### Custom Properties

_Yours to shape with the `configure` skill. The seed ships a few useful defaults below — keep, scope, or drop any of them; Eidos doesn't depend on them. Absence where a property applies is a soft gap the validator notes, never refuses._

| Name          | Type | Applies To | Meaning                                                                                    |
| ------------- | ---- | ---------- | ------------------------------------------------------------------------------------------ |
| status        | Text | all        | Lifecycle value: Draft / Outlined / Drafted / Revised / Final / Cut. An off-list value warns. |
| date_created  | Date | all        | YYYY-MM-DD. The day the blueprint was first written. Set once.                                   |
| date_modified | Date | all        | YYYY-MM-DD. The day the blueprint was last changed.                                              |
| tags          | List | all        | Free tags.                                                                                  |
| part          | Text | Chapters   | The grouping, matching the blueprint's sub-folder under its collection in the naming convention. An unknown value warns, never fails. |
| depends_on    | List | Chapters   | Chapters a reader must have read first, each a markdown link. A reading dependency. |

## Vocabulary

The term contract — the words this root uses on purpose, so a distinction made once is not lost later.
One row per term: what it **means**, and what it is **not** (the near-misses, each with why it is a
different thing). A term whose blueprint defines it in full links to that blueprint from its Term cell.
Eidos declares none of these; the table starts empty and grows a row when a word begins to carry a
distinction worth keeping. The `configure` skill edits this section and presses for all three of Term,
Means, and Not.

| Term | Means | Not |
| ---- | ----- | --- |

_(no terms yet — add a row when a word starts to carry a distinction worth keeping)_

## Versions

Snapshots of this root, taken on purpose. Not the product's release version, and not Eidos's (that is
`eidos_version` above): a fixed point a team can hold the definition against later, when the product
has gone a different direction, a stakeholder wants to iterate from what was agreed, or a handover
needs a signed-off state. Working alone you will likely never take one; git history is enough. One row
per snapshot, newest first: the root's own number, the commit that *is* the snapshot (nothing is copied;
`git show <commit>:<path>` reads a blueprint as it was then), and the tag if one was made, named
`blueprints/<version>` so it never collides with the product's own tags. No skill asks whether to
version; the `configure` skill records one when you ask, and asks whether to tag it.

| Version | Commit | Tag |
| ------- | ------ | --- |

_(none — and that is the normal state; add a row only when a team needs a fixed point to hold the definition against)_
