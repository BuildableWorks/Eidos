# Seeds

The starting **frameworks** Eidos ships. A seed is a complete form layer — collections, body shapes and their flavors, roles, and a property Schema — that [`install`](../skills/install) copies into a new root's `_eidos/`. Pick the one nearest what you're defining; reshape it from there with `configure`.

| Seed | For | Collections |
| --- | --- | --- |
| [`software/`](software) | a product, service, or system being built | `Frames` (architecture, audience, criteria, market) · `Specs` by domain |
| [`book/`](book) | a book, long-form argument, or course | `Frames` (premise, reader, voice, market) · `Chapters` by part |
| [`research/`](research) | a question, a study, or a programme of inquiry | `Frames` (question, prior work, method, ethics) · `Investigations` by strand |

Every seed carries the same pieces, so the skills work identically across them:

```txt
<seed>/
  shapes/       # body shapes, one file per flavor (<kind>.<flavor>.md)
  roles/        # response contracts, one per role
  Framework.md  # version, naming, Top-Level, Collections, and the property Schema
  me.md         # blank actor frame (installs gitignored)
  .gitignore    # keeps me.md out of version control
  README.md     # the {{Product}} front-door template
```

**Three seeds, one standard.** `software` is the default and the one the standard teaches from, but nothing in Eidos knows a collection by name: `book` calls its units `Chapters` and groups them by `part`, `research` calls them `Investigations` and groups them by `strand`, and both work the same way the software seed does. A seed is a starting point, not a cage — and it's the same kind of artifact you'd publish for someone else to start from.

**None of these fit?** Start from the nearest and reshape it, or scaffold your own collections with `configure`.
