---
# The Eidos version this framework targets; migrate reads and bumps it.
eidos_version: 4.4.2
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
- [README](../README.md) — the root's front door: what this is, and pointers in.
<!-- One bullet per top-level document. README is the door and comes first; add your own below (a
     Roadmap, a Vision, the generated Blueprint Map canvas), each a link and a one-line description.
     The framing docs live in the Frames collection, not here. configure refreshes this list. -->

## Collections

A collection is a top-level folder of repeated blueprints that share a body shape. `Frames` holds the
framing docs — the most primary thing the folder says about itself — and `Specs` the product's
units. Add more with `configure`. Each lists its flavors (the default marked) and its grouping,
and points at its generated `index.md` leaf.

### Frames

The framing docs that set what every other blueprint is judged against — the product's architecture,
audience, criteria, and market. This framework's framing collection; each frame follows the flavor of
its kind, and one left unwritten is a gap to surface, not a failure.

- **Leaf:** [Frames/index.md](../Frames/index.md)
- **Flavors:**
  - [architecture](shapes/frame.architecture.md) — the product as a built system (default).
  - [audience](shapes/frame.audience.md) — who it serves, and how each kind differs.
  - [criteria](shapes/frame.criteria.md) — budget, scope objectives, timeline.
  - [market](shapes/frame.market.md) — landscape, positioning, and how it earns.
- **Canvas:** file

### Specs

The product's units, one per blueprint, grouped by domain.

- **Leaf:** [Specs/index.md](../Specs/index.md)
- **Flavors:**
  - [full](shapes/spec.full.md) — the complete spec shape (default).
  - [micro](shapes/spec.micro.md) — Intent, Open Questions, ACs, Out of Scope; grow into full.
- **Canvas:** card from `## Intent`
- **Domains:** _(add one bullet per domain — a name and a short description — as domains accrue)_

## Schema

The property contract — what a blueprint's frontmatter may carry, across every collection. Two parts: the
**core** properties Eidos's own machinery uses, and the **custom** ones you (or the seed) add. Every
custom property declares which collections it **applies to** — `all`, or a list — so a property never
lands where it makes no sense (`domain` is Specs-only). A property's type comes from the Obsidian set
(Text, List, Number, Checkbox, Date, Date & time), so frontmatter renders natively in an Obsidian
vault. The `configure` skill edits this section.

### Eidos Core

_Present on every blueprint. Managed by the standard (Eidos 4.4.2); `migrate` rewrites this block on a version change — don't hand-edit it. (`flavor` absent = the collection's default; `connects_to` absent = no canvas edges; a missing `summary` is flagged by the index.)_

| Name        | Type | Meaning                                                                                        |
| ----------- | ---- | ---------------------------------------------------------------------------------------------- |
| id          | Text | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it.      |
| title       | Text | Human-readable name.                                                                           |
| summary     | Text | One plain line — what this blueprint is, in a sentence, distilled from Intent. Source for the collection index.md listing; absent, the index flags it. |
| flavor      | Text | Which body flavor this blueprint follows, from its collection's declared flavors. Absent = the collection's default flavor. |
| connects_to | List | Blueprints this one connects to on the canvas, each a markdown link; drawn as a directed edge (this → target). The intentional map, distinct from depends_on. |

### Custom Properties

_Yours to shape with the `configure` skill. The seed ships a few useful defaults below — keep, scope, or drop any of them; Eidos doesn't depend on them. Absence where a property applies is a soft gap the validator notes, never refuses._

| Name          | Type | Applies To | Meaning                                                                                    |
| ------------- | ---- | ---------- | ------------------------------------------------------------------------------------------ |
| status        | Text | all        | Lifecycle value: Draft / Intake / In Progress / Done / Archived / Deprecated. An off-list value warns. |
| date_created  | Date | all        | YYYY-MM-DD. The day the blueprint was first written. Set once.                                   |
| date_modified | Date | all        | YYYY-MM-DD. The day the blueprint was last changed.                                              |
| tags          | List | all        | Free tags.                                                                                  |
| domain        | Text | Specs      | The grouping, matching the blueprint's sub-folder under its collection in the naming convention. An unknown value warns, never fails. |
| depends_on    | List | Specs      | Blueprints this one needs, each a markdown link. An implementation dependency, not a canvas edge. |
| type          | Text | Specs      | Open, soft category label — drives views and filtering, never structure. e.g. feature, capability, integration. |
