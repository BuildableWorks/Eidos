---
# The Eidos version this registry targets; eidos-migrate reads and bumps it.
eidos_version: 4.1.0
# How files, folders, and links are named: Title Case | TitleCase | kebab-case. Absent = Title Case.
naming: Title Case
---

# Registry

The registry's index and config: the version and naming convention above, and below the Top-Level
documents and the Collections with their flavors and grouping — the one place to read the whole
registry at a glance. The visible `README.md` at the registry root is the friendly door to it; keep
both current with the `eidos-registry` skill.

## Top-Level

<!-- eidos-registry: top-level index (regenerated) -->
<!-- One bullet per top-level document you create — a link and a one-line description. Top-level docs
     are your own (a Roadmap, a Vision, the generated Registry Map canvas); the framing docs live in
     the Frames collection below, not here. eidos-registry refreshes this list. For example:
- [Roadmap](../Roadmap.md) — where the product is headed, in plain horizons.
-->

## Collections

A collection is a top-level folder of repeated items that share a body shape. `Frames` holds the
framing docs — the most primary thing the registry says about itself — and `Specs` the product's
units. Add more with `eidos-registry`. Each lists its flavors (the default marked) and its grouping,
and points at its generated `index.md` leaf.

### Frames

The framing docs that set what every other item is judged against — the product's architecture,
audience, criteria, and market. Highly encouraged, not required; each frame follows the flavor of its
kind.

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
- **Domains:** _(add one bullet per domain — a name and a short description — as domains accrue)_
