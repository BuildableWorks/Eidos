---
# The Eidos version this framework targets; migrate reads and bumps it.
eidos_version: 4.4.0
# How files, folders, and links are named: kebab-case | TitleCase | Title Case. Absent = kebab-case.
naming: kebab-case
---

# Framework

This framework's index and config, in one place: the version and naming convention above, and below
the Top-Level documents, the Collections (with their flavors and grouping), and the property Schema.
The root `README.md` is the friendly door to it. Kept current with `configure`.

## Top-Level

<!-- configure: top-level index (regenerated) -->
- [README](../README.md) — the front door: what this subset is, and pointers in.
- [Roadmap](../roadmap.md) — where the subset is headed, in plain horizons (a custom top-level doc).

## Collections

### frames

The framing docs — one per frame — that set what every other item is judged against. This framework's
framing collection; each follows the flavor of its kind, and one left unwritten is a gap to surface,
not a failure.

- **Leaf:** [frames/index.md](../frames/index.md)
- **Flavors:**
  - [architecture](shapes/frame.architecture.md) — the product as a built system (default).
  - [audience](shapes/frame.audience.md) — who it serves, and how each kind differs.
  - [criteria](shapes/frame.criteria.md) — budget, scope objectives, timeline.
  - [market](shapes/frame.market.md) — landscape, positioning, and how it earns.
- **Canvas:** file

### specs

The product's units, one per item, grouped by domain.

- **Leaf:** [specs/index.md](../specs/index.md)
- **Flavors:**
  - [full](shapes/spec.full.md) — the complete spec shape (default).
  - [micro](shapes/spec.micro.md) — Intent, Open Questions, ACs, Out of Scope; grow into full.
- **Canvas:** card from `## Intent`
- **Domains:**
  - **playback** — watching a video, and picking up where you left off.
  - **channels** — publishing to a channel, and following one.

## Schema

The property contract — what an item's frontmatter may carry, across every collection. Two parts: the
**core** properties Eidos's own machinery uses, and the **custom** ones this framework (or the seed)
adds. Every custom property declares which collections it **applies to** — `all`, or a list — so a
property never lands where it makes no sense (`domain` and `beta` are specs-only here). Types come
from the Obsidian set (Text, List, Number, Checkbox, Date, Date & time). The `configure` skill
edits this section.

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

_Yours to shape with the `configure` skill. The seed ships a few useful defaults; keep, scope, or drop any of them — Eidos doesn't depend on them. Absence where a property applies is a soft gap the validator notes, never refuses._

| Name          | Type     | Applies To | Meaning                                                                                |
| ------------- | -------- | ---------- | -------------------------------------------------------------------------------------- |
| status        | Text     | all        | Lifecycle value: Draft / Intake / In Progress / Done / Archived / Deprecated. An off-list value warns. |
| date_created  | Date     | all        | YYYY-MM-DD. The day the item was first written. Set once.                               |
| date_modified | Date     | all        | YYYY-MM-DD. The day the item was last changed.                                          |
| tags          | List     | all        | Free tags.                                                                              |
| domain        | Text     | specs      | The grouping, matching the item's sub-folder under its collection in the naming convention. An unknown value warns, never fails. |
| depends_on    | List     | specs      | Items this one needs, each a markdown link. An implementation dependency, not a canvas edge. |
| type          | Text     | specs      | Open, soft category label — drives views and filtering, never structure. e.g. feature, capability, integration. |
| beta          | Checkbox | specs      | Whether this unit is in scope for the private beta.                                     |
