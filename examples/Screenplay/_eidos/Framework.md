---
# The Eidos version this framework targets; migrate reads and bumps it.
eidos_version: 4.4.0
# How files, folders, and links are named: kebab-case | TitleCase | Title Case. Absent = kebab-case.
naming: kebab-case
---

# Framework

This framework started from the **book** seed and was reshaped: `chapters` became `scenes`, `part`
became `act`, the chapter shapes became scene shapes, and a `pov` property was added. Nothing was
forked — the standard is untouched, and every skill reads this file the same way it reads the
software seed's.

## Top-Level

<!-- configure: top-level index (regenerated) -->
- [README](../README.md) — the definition's front door: what this film is, and pointers in.
- [Framework Map](../framework-map.canvas) — the generated canvas: every scene, and what it sets up.

## Collections

### frames

What the film argues, who watches it, how it sounds, and where it sits. Loose, point-in-time prose.

- **Leaf:** [frames/index.md](../frames/index.md)
- **Flavors:**
  - [premise](shapes/frame.premise.md) — what the film is about, and why it has to exist (default).
  - [audience](shapes/frame.audience.md) — who watches, and what changes for them.
  - [voice](shapes/frame.voice.md) — tone, camera, and the rules the film keeps.
  - [market](shapes/frame.market.md) — festival, format, comparables, and how it reaches people.
- **Canvas:** file

### scenes

The film's units, one per scene, grouped by act.

- **Leaf:** [scenes/index.md](../scenes/index.md)
- **Flavors:**
  - [full](shapes/scene.full.md) — the complete scene shape (default).
  - [beat](shapes/scene.beat.md) — Logline, Intent, Out of Scope; grow into full.
- **Canvas:** card from `## Logline`
- **Acts:**
  - **act-i** — the commission, and the last accurate map.
  - **act-ii** — the crossing, and what the map leaves out.

## Schema

The property contract. Two parts: the **core** properties Eidos's machinery uses, and the **custom**
ones this framework adds. `act` and `pov` are scenes-only; the seed's `depends_on` was kept and
`tags` dropped.

### Eidos Core

_Present on every item. Managed by the standard (Eidos 4.4.0); `migrate` rewrites this block on a version change — don't hand-edit it._

| Name        | Type | Meaning                                                                                        |
| ----------- | ---- | ---------------------------------------------------------------------------------------------- |
| id          | Text | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it.      |
| title       | Text | Human-readable name.                                                                           |
| summary     | Text | One plain line — what this item is, in a sentence, distilled from Intent. Source for the collection index.md listing; absent, the index flags it. |
| flavor      | Text | Which body flavor this item follows, from its collection's declared flavors. Absent = the collection's default flavor. |
| connects_to | List | Items this one connects to on the definition's canvas, each a markdown link; drawn as a directed edge (this → target). |

### Custom Properties

| Name          | Type | Applies To | Meaning                                                                                    |
| ------------- | ---- | ---------- | ------------------------------------------------------------------------------------------ |
| status        | Text | all        | Lifecycle value: Draft / Outlined / Drafted / Revised / Final / Cut. An off-list value warns. |
| date_created  | Date | all        | YYYY-MM-DD. The day the item was first written. Set once.                                   |
| date_modified | Date | all        | YYYY-MM-DD. The day the item was last changed.                                              |
| act           | Text | scenes     | The grouping, matching the item's sub-folder under `scenes/`.                                |
| pov           | Text | scenes     | Whose eyes the scene is shot from. Blank means the camera is nobody's.                       |
| depends_on    | List | scenes     | Scenes a viewer must have seen first for this one to land, each a markdown link.             |
