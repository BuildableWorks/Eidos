---
# The Eidos version this framework targets; migrate reads and bumps it.
eidos_version: 4.4.3
# How files, folders, and links are named: kebab-case | TitleCase | Title Case. Absent = kebab-case.
naming: kebab-case
---

# Framework

The framework's index and config, in one place: the version and naming convention above, and below the
Top-Level documents, the Collections (with their flavors and grouping), and the property Schema. The
visible `README.md` at the root is the friendly door to it; keep it current with the
`configure` skill.

## Top-Level

<!-- configure: top-level index (regenerated) -->
- [README](../README.md) — the root's front door: what this programme asks, and pointers in.
<!-- One bullet per top-level document. README is the door and comes first; add your own below (a
     Protocol, a Data Statement, the generated Blueprint Map canvas), each a link and a one-line
     description. The framing docs live in the Frames collection, not here. configure refreshes
     this list. -->

## Collections

A collection is a top-level folder of repeated blueprints that share a body shape. `Frames` holds the
framing docs — the most primary thing the folder says about itself — and `Investigations` the
programme's units. Add more with `configure`. Each lists its flavors (the default marked), how
it draws on the canvas, and its grouping, and points at its generated `index.md` leaf.

### Frames

The framing docs that set what every investigation is judged against — what is being asked, what is
already known, what would count as knowing, and who is affected. This framework's framing collection;
each frame follows the flavor of its kind, and one left unwritten is a gap to surface, not a failure.

- **Leaf:** [Frames/index.md](../Frames/index.md)
- **Flavors:**
  - [question](shapes/frame.question.md) — what the programme asks, and why it matters (default).
  - [prior work](shapes/frame.prior-work.md) — what is already known, and where this sits.
  - [method](shapes/frame.method.md) — how anyone would know, and the standard of evidence.
  - [ethics](shapes/frame.ethics.md) — who is affected, what they consented to, what could go wrong.
- **Canvas:** file

### Investigations

The programme's units, one per line of inquiry, grouped by strand.

- **Leaf:** [Investigations/index.md](../Investigations/index.md)
- **Flavors:**
  - [full](shapes/investigation.full.md) — the complete investigation shape (default).
  - [note](shapes/investigation.note.md) — Intent, Open Questions, Claims, Out of Scope; grow into full.
- **Canvas:** card from `## Intent`
- **Strands:** _(add one bullet per strand — a name and a short description — as strands accrue)_

## Schema

The property contract — what a blueprint's frontmatter may carry, across every collection. Two parts: the
**core** properties Eidos's own machinery uses, and the **custom** ones you (or the seed) add. Every
custom property declares which collections it **applies to** — `all`, or a list — so a property never
lands where it makes no sense (`strand` is Investigations-only). A property's type comes from the
Obsidian set (Text, List, Number, Checkbox, Date, Date & time), so frontmatter renders natively in an
Obsidian vault. The `configure` skill edits this section.

### Eidos Core

_Present on every blueprint. Managed by the standard (Eidos 4.4.3); `migrate` rewrites this block on a version change — don't hand-edit it. (`flavor` absent = the collection's default; `connects_to` absent = no canvas edges; a missing `summary` is flagged by the index.)_

| Name        | Type | Meaning                                                                                        |
| ----------- | ---- | ---------------------------------------------------------------------------------------------- |
| id          | Text | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it.      |
| title       | Text | Human-readable name.                                                                           |
| summary     | Text | One plain line — what this blueprint is, in a sentence, distilled from Intent. Source for the collection index.md listing; absent, the index flags it. |
| flavor      | Text | Which body flavor this blueprint follows, from its collection's declared flavors. Absent = the collection's default flavor. |
| connects_to | List | Blueprints this one connects to on the canvas, each a markdown link; drawn as a directed edge (this → target). The intentional map, distinct from depends_on. |

### Custom Properties

_Yours to shape with the `configure` skill. The seed ships a few useful defaults below — keep, scope, or drop any of them; Eidos doesn't depend on them. Absence where a property applies is a soft gap the validator notes, never refuses._

| Name          | Type | Applies To     | Meaning                                                                                |
| ------------- | ---- | -------------- | -------------------------------------------------------------------------------------- |
| status        | Text | all            | Lifecycle value: Draft / Open / Running / Answered / Inconclusive / Abandoned. An off-list value warns. |
| date_created  | Date | all            | YYYY-MM-DD. The day the blueprint was first written. Set once.                               |
| date_modified | Date | all            | YYYY-MM-DD. The day the blueprint was last changed.                                          |
| tags          | List | all            | Free tags.                                                                              |
| strand        | Text | Investigations | The grouping — the line of inquiry this belongs to, matching the blueprint's sub-folder in the naming convention. An unknown value warns, never fails. |
| depends_on    | List | Investigations | Investigations, data, or approvals this one needs first, each a markdown link. A real dependency, not a canvas edge. |
