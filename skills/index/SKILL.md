---
name: index
description: >-
  Rebuild the index in a root's framework document: the generated `index` key in `.eidos/Framework.yaml`, one list per collection, that lets a human or agent find a blueprint without scraping the tree. Use when someone wants to "regenerate the index", "rebuild the specs index", "reindex the blueprints", "map the blueprints", says the index is stale, or after blueprints have been added, renamed, moved, or removed. It reads the framework's declared collections, walks each collection's one-level sub-folders, and rewrites the `index` key wholesale, each blueprint an entry with its `id`, `title`, one-line `summary`, path, and group. Runs `eidos index` where a shell is available; falls back to doing it by hand on a sandboxed host. Regenerable and never gates.
---

# Eidos Index

Keep the **index** current: the generated `index` key in `.eidos/Framework.yaml`, one list per collection, each entry a blueprint's `id`, `title`, `summary`, `path` (relative to the collection folder), and `group` (its sub-folder, when it has one). It is **fully generated**. The framework's declarations, the owner's descriptions, and every other key in the document are left exactly as they are; this skill rewrites the `index` key and nothing else.

## How you work: regenerate, don't author

The one-line summary is a real frontmatter property, authored once on the blueprint and read here, so the index is **derived, not written**, and regenerating is safe and mechanical. Two things stay the human's:

- **Descriptions** live on the collections and their groups in `Framework.yaml`, written once by the owner. A sub-folder with no group entry gets noted and asked about, never invented.
- **Summaries** are the blueprint's own `summary`. The index never adds meaning the blueprint doesn't carry; a blueprint without one is listed with `summary: null` and **flagged**, and the next regeneration picks up whatever the owner writes.

## Run the CLI when you can

`eidos index` (the `eidos` CLI, npm package `eidosmd`; `npx eidosmd index` with nothing installed) does the whole walk deterministically. **Prefer it whenever you have a shell** (Claude Code, the IDE):

```
eidos index                 # rebuild every collection's index
eidos check                 # reports a stale index, among the rest
```

Run it from inside the root, or with `--root <path>`. It names any blueprint missing a `summary`; **those are your only authoring task**. Write a `summary` on each flagged blueprint (distill its Intent to one plain line), then run it again. It does not touch the declarations, so still do the reconciliation in step 5 by reading `Framework.yaml`.

On a **sandboxed host** (Claude Desktop) where you can't run it, do the walk by hand; the procedure below is exactly what it does.

## Where things are

- The collections are declared in `.eidos/Framework.yaml` under `collections`, each with its folder.
- Each collection's blueprints live under `<Collection>/`, optionally in one level of sub-folders (`<Collection>/<Group>/`).
- The index is the `index` key of the same document: `index.<Collection>` is that collection's list.
- This needs an installed framework. If there's no `.eidos/`, it isn't a root yet; offer `install`.

## Procedure (what the CLI does, and your fallback by hand)

1. **Read `me.md`** (`.eidos/me.md`) and the declared collections (`.eidos/Framework.yaml`).
2. **For each collection, walk its folder.** Read its one-level sub-folders (the grouping) and the blueprints in each, or the blueprints directly in the collection folder if it is flat. For each blueprint read its `id`, `title`, and `summary`.
3. **Take each blueprint's `summary` verbatim.** It is one plain line already. If a blueprint has **no** `summary`, list it with `summary: null` and flag it, then write a `summary` on that blueprint, distilling its Intent to one line, and regenerate. Never invent a summary into the index alone; it belongs on the blueprint.
4. **Rewrite the `index` key wholesale**, and nothing else in the document: one list per collection, in the order the collections are declared, entries in file order, a grouped collection's entries under their sub-folder in sub-folder order. `path` is relative to the collection folder, as the file is named on disk (`identity/magic-link-sign-in.md`, not `<Collection>/<Group>/…`); `group` is the sub-folder, absent in a flat collection.

   ```yaml
   index:
     specs:
       - { id: magic-link-sign-in, title: Magic Link Sign-In, summary: "passwordless sign-in by an emailed single-use link.", path: identity/magic-link-sign-in.md, group: identity }
       - { id: session-management, title: Session Management, summary: null, path: identity/session-management.md, group: identity }
   ```
5. **Reconcile against the declarations.**
   - A sub-folder with blueprints but **no group entry** under the collection's `grouping.groups`: note it and ask the owner to add one (`configure`); don't invent it.
   - A group entry **with no blueprints**: dangling; flag it.
6. **Report**: the collections and blueprints indexed, any blueprints still missing a `summary` (and where), and any sub-folder still needing a group entry.

## Notes

- Regenerable and idempotent: running it again yields the same key (plus any new blueprints). It never gates; an index annotates and navigates, it doesn't validate. `eidos check` reports a stale index without writing, useful in CI or a pre-commit hook.
- More than one level of sub-folders under a collection is discouraged (see EIDOS.md). If you find deeper nesting, index the first level and flag the rest for the owner.
- This is the leaf half of Eidos navigation; the declarations above it (`top_level`, `collections`) are kept by `configure`, with the visible root `README.md` as the door. The property and template structure lives in `.eidos/` and is handled by the other skills.
