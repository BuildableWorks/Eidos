# Example — Marginalia

A worked example of an Eidos product definition. **Marginalia** is a small, fictional SaaS: a shared reading library where teams save, annotate, and discuss articles. The [`Blueprint/`](Blueprint) folder beside this README is a filled-in registry, end to end — exactly what Marginalia would drop into its own repo. This README lives _outside_ the registry, just to narrate the example.

This is a reference to read and pattern-match against — **not** a starter to copy. To begin your own registry, run the `eidos-init` skill, or fill the standard's [`templates/`](../templates/) by hand following [`EIDOS.md`](../EIDOS.md). It is a filled-in product only; the blank templates are the standard's own, in the top-level [`templates/`](../templates/).

```
example/
  README.md          # this file — narrates the example, outside the registry
  Blueprint/         # the registry root (the standard's default name); drop one like it into a repo
    Architecture.md
    Audience.md
    Criteria.md
    Market.md
    Domains.md
    Specs/
      Identity/
        Magic Link Sign-In.md
        Session Management.md
      Library/
        Saved Articles.md
```

Human-facing names are Title Case so the tree reads like a table of contents. A spec's filename is its title; its permanent reference is the kebab-case `id` inside (`Magic Link Sign-In.md` carries `id: magic-link-signin`), so you can rename a title without breaking what points at it.
