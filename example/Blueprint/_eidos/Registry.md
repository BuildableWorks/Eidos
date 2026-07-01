---
# The Eidos version this registry targets; eidos-migrate reads and bumps it.
eidos_version: 4.1.0
# How files, folders, and links are named: Title Case | TitleCase | kebab-case. Absent = Title Case.
naming: Title Case
---

# Registry

This registry's index and config, in one place: the version and naming convention above, and below
the Top-Level documents, the Collections (with their flavors and grouping), and the property Schema.
The root `README.md` is the friendly door to it. Kept current with `eidos-registry` and `eidos-schema`.

## Top-Level

<!-- eidos-registry: top-level index (regenerated) -->
- [README](../README.md) — the front door: what this subset is, and pointers in.
- [Roadmap](../Roadmap.md) — where the subset is headed, in plain horizons (a custom top-level doc).

## Collections

### Frames

The framing docs — one per frame — that set what every other item is judged against. Highly encouraged,
not required; each follows the flavor of its kind.

- **Leaf:** [Frames/index.md](../Frames/index.md)
- **Flavors:**
  - [architecture](shapes/frame.architecture.md) — the product as a built system (default).
  - [audience](shapes/frame.audience.md) — who it serves, and how each kind differs.
  - [criteria](shapes/frame.criteria.md) — budget, scope objectives, timeline.
  - [market](shapes/frame.market.md) — landscape, positioning, and how it earns.

### Specs

The product's units, one per item, grouped by domain.

- **Leaf:** [Specs/index.md](../Specs/index.md)
- **Flavors:**
  - [full](shapes/spec.full.md) — the complete spec shape (default).
  - [micro](shapes/spec.micro.md) — Intent, Open Questions, ACs, Out of Scope; grow into full.
- **Domains:**
  - **Playback** — watching a video, and picking up where you left off.
  - **Channels** — publishing to a channel, and following one.

## Schema

The property contract — what an item's frontmatter may carry, across every collection. Two parts: the
**core** properties Eidos's own machinery uses, and the **custom** ones this registry (or the seed)
adds. Every custom property declares which collections it **applies to** — `all`, or a list — so a
property never lands where it makes no sense (`domain` and `beta` are Specs-only here). Types come
from the Obsidian set (Text, List, Number, Checkbox, Date, Date & time). The `eidos-schema` skill
edits this section.

### Eidos Core

_Present on every item. Managed by the standard (Eidos 4.1.0); `eidos-migrate` rewrites this block on a version change — don't hand-edit it. (`flavor` absent = the collection's default; `connects_to` absent = no canvas edges; a missing `summary` is flagged by the index.)_

| Name        | Type | Meaning                                                                                        |
| ----------- | ---- | ---------------------------------------------------------------------------------------------- |
| id          | Text | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it.      |
| title       | Text | Human-readable name.                                                                           |
| summary     | Text | One plain line — what this item is, in a sentence, distilled from Intent. Source for the collection index.md listing; absent, the index flags it. |
| flavor      | Text | Which body flavor this item follows, from its collection's declared flavors. Absent = the collection's default flavor. |
| owner       | Text | Who owns the document. Non-owners are warned before editing it (the registry owner aside).      |
| connects_to | List | Items this one connects to on the registry canvas, each a markdown link; drawn as a directed edge (this → target). The intentional map, distinct from depends_on. |

### Custom Properties

_Yours to shape with the `eidos-schema` skill. The seed ships a few useful defaults; keep, scope, or drop any of them — Eidos doesn't depend on them. Absence where a property applies is a soft gap the validator notes, never refuses._

| Name          | Type     | Applies To | Meaning                                                                                |
| ------------- | -------- | ---------- | -------------------------------------------------------------------------------------- |
| status        | Text     | all        | Lifecycle value: Draft / Intake / In Progress / Done / Archived / Deprecated. An off-list value warns. |
| date_created  | Date     | all        | YYYY-MM-DD. The day the item was first written. Set once.                               |
| date_modified | Date     | all        | YYYY-MM-DD. The day the item was last changed.                                          |
| tags          | List     | all        | Free tags.                                                                              |
| domain        | Text     | Specs      | The grouping, matching the item's sub-folder under its collection in the naming convention. An unknown value warns, never fails. |
| depends_on    | List     | Specs      | Items this one needs, each a markdown link. An implementation dependency, not a canvas edge. |
| type          | Text     | Specs      | Open, soft category label — drives views and filtering, never structure. e.g. feature, capability, integration. |
| beta          | Checkbox | Specs      | Whether this unit is in scope for the private beta.                                     |
