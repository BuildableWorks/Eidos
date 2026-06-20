# Example — Marginalia

A worked example of an Eidos product definition. **Marginalia** is a small, fictional SaaS: a shared reading library where teams save, annotate, and discuss articles. The [`Blueprint/`](Blueprint) folder beside this README is a filled-in registry, end to end — exactly what Marginalia would drop into its own repo, hidden `.eidos/` form layer and all. This README lives _outside_ the registry, just to narrate the example.

This is a reference to read and pattern-match against — **not** a starter to copy. To begin your own registry, run the `eidos-init` skill: it installs the `.eidos/` form layer and scaffolds the blank product docs, following [`EIDOS.md`](../EIDOS.md).

```
example/
  README.md          # this file — narrates the example, outside the registry
  Blueprint/         # the registry root (the standard's default name); drop one like it into a repo
    .eidos/          # the form layer: shapes, Schema, Registry (hidden machinery)
    Architecture.md
    Audience.md
    Criteria.md
    Market.md
    Domains.md
    Roadmap.md       # a custom top-level doc — free-form, no shape
    Specs/
      Identity/
        Magic Link Sign-In.md
        Session Management.md
      Library/
        Saved Articles.md
```

Human-facing names are Title Case so the tree reads like a table of contents. A spec's filename is its title; its permanent reference is the kebab-case `id` inside (`Magic Link Sign-In.md` carries `id: magic-link-signin`), so you can rename a title without breaking what points at it.

The `.eidos/Schema.md` here shows the form layer in use: alongside the canonical properties it adds one **custom property** — `beta`, a required Checkbox marking whether a unit is in scope for the private beta — which every spec then carries. That is a registry extending the opinionated baseline without forking the standard.

Marginalia also keeps a **custom top-level doc** of its own — `Roadmap.md` — beyond the canonical four. It has no shape and isn't validated: a registry writes the top-level docs its product needs and keeps them organized with `eidos-format`. The four are the baseline, not the whole set.
