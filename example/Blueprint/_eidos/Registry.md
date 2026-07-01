---
# The Eidos version this registry targets; eidos-migrate reads and bumps it.
eidos_version: 4.2.0
# How files, folders, and links are named: Title Case | TitleCase | kebab-case. Absent = Title Case.
naming: Title Case
---

# Registry

This registry's index and config: the version and naming convention above, and below the Top-Level
documents and the Collections with their flavors and grouping. The root `README.md` is the friendly
door to it. Kept current with `eidos-registry`.

## Top-Level

<!-- eidos-registry: top-level index (regenerated) -->
- [Roadmap](../Roadmap.md) — where the subset is headed, in plain horizons (a custom top-level doc).

## Collections

### Specs

The product's units, one per spec, grouped by domain.

- **Leaf:** [Specs/index.md](../Specs/index.md)
- **Flavors:**
  - [full](shapes/spec.full.md) — the complete spec shape (default).
  - [micro](shapes/spec.micro.md) — Intent, Open Questions, ACs, Out of Scope; grow into full.
- **Domains:**
  - **Playback** — watching a video, and picking up where you left off.
  - **Channels** — publishing to a channel, and following one.

### Frames

The framing docs — one per frame — that set what every spec is judged against. Highly encouraged, not
required; each follows the flavor of its kind.

- **Leaf:** [Frames/index.md](../Frames/index.md)
- **Flavors:**
  - [architecture](shapes/frame.architecture.md) — the product as a built system (default).
  - [audience](shapes/frame.audience.md) — who it serves, and how each kind differs.
  - [criteria](shapes/frame.criteria.md) — budget, scope objectives, timeline.
  - [market](shapes/frame.market.md) — landscape, positioning, and how it earns.
