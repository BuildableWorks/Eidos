---
name: index
description: >-
  Build or refresh a collection's `index.md` in an Eidos folder — the generated leaf that lists a collection's blueprints so a human or agent can navigate without scraping the tree. Use when someone wants to "regenerate the index", "rebuild the specs index", "update Specs/index.md", "reindex the blueprints", "map the blueprints", says an index is stale, or after blueprints have been added, renamed, moved, or removed. It reads the framework's declared collections, walks each collection's one-level sub-folders, and rewrites its `index.md` wholesale — each blueprint a markdown link with its one-line `summary` property, grouped by sub-folder (a grouped collection) or flat. Ships a `build-index.py` that does the whole walk deterministically where a shell is available; falls back to doing it by hand on a sandboxed host. Regenerable and never gates.
---

# Eidos Index

Keep each collection's **`index.md`** current — the leaf a human or agent reads to find a blueprint without scraping the tree. It lives inside its collection's folder, lists the blueprints grouped by sub-folder or flat, and is **fully generated**: one markdown link per blueprint carrying its `summary` property. Folder descriptions live in `_eidos/Framework.md`; this skill rebuilds only the listing, for every collection alike.

## How you work: regenerate, don't author

The one-line summary is a real frontmatter property, authored once on the blueprint and read here — so the index is **derived, not written**, and regenerating is safe and mechanical. Two things stay the human's:

- **Descriptions** live in `_eidos/Framework.md`, written once by the owner. A sub-folder without one gets noted and asked about, never invented.
- **Summaries** are the blueprint's own `summary`. The index never adds meaning the blueprint doesn't carry; a blueprint without one is **flagged**, and the next regeneration picks up whatever the owner writes.

## Run the script when you can

The skill ships **`build-index.py`** (beside this file) — stdlib-only Python 3 that does the entire walk deterministically. **Prefer it whenever you have a shell** (Claude Code, the IDE):

```
python3 <skill>/build-index.py <root>            # rebuild every collection's index
python3 <skill>/build-index.py <root> --check    # verify only; non-zero if any index is stale
python3 <skill>/build-index.py <root> --collection <Collection>   # limit to one collection (repeatable)
```

`<root>` is the folder that contains `_eidos/` (often the root, e.g. `Blueprints/`). The script reads the declared collections from `_eidos/Framework.md`, walks each, and rewrites each `index.md` from the blueprints' `title` + `summary`. It prints any blueprint missing a `summary` to stderr — **those are your only authoring task**: write a `summary` on each flagged blueprint (distill its Intent to one plain line), then re-run the script. It does **not** touch the Framework, so still do the reconciliation in step 6 by reading `_eidos/Framework.md`.

On a **sandboxed host** (Claude Desktop) where you can't run the script, do the walk by hand — the procedure below is exactly what the script does.

## Where things are

- The collections are declared in `_eidos/Framework.md` (the `## Collections` section), each with its folder.
- Each collection's blueprints live under `<Collection>/`, optionally in one level of sub-folders (`<Collection>/<Group>/`).
- Each collection's index is `<Collection>/index.md`.
- This needs an installed framework. If there's no `_eidos/`, it isn't an Eidos folder yet — offer `install`.

## Procedure (what the script does — and your fallback by hand)

1. **Read the actor** (`_eidos/me.md`) and the declared collections (`_eidos/Framework.md`).
2. **Decide which collections to re-index.** Default to all; if only some folders changed, the script's `--collection` filter (or your own scope by hand) limits the work. For a small folder, re-indexing everything is fine.
3. **For each chosen collection, walk its folder.** Read its one-level sub-folders (the grouping) and the blueprints in each — or the blueprints directly in the collection folder, if it's flat. For each blueprint read its `title`, path, and `summary`.
4. **Take each blueprint's `summary` verbatim.** It's one plain line already. If a blueprint has **no** `summary`, flag it (the script writes a `⚠️ TODO` placeholder in the bullet and lists the file on stderr) — then write a `summary` on that blueprint, distilling its Intent to one line, and regenerate. Never invent a summary into the index alone; it belongs on the blueprint.
5. **Rewrite `<Collection>/index.md` wholesale.** It is fully generated — no hand-written prose to preserve — so rebuild the whole file:
   - An H1 of the collection name and the marker comment `<!-- index: <Collection> (regenerated) -->`.
   - **Grouped collection:** one `##` per sub-folder, then a bullet per blueprint — `- [Title](<Sub-folder>/<File>.md) — summary`. Links are **relative to the collection folder** (`identity/magic-link-sign-in.md`, not `<Collection>/<Group>/…`), built in the framework's naming convention (read `naming` from `_eidos/Framework.md`, kebab-case by default): encode spaces as `%20` in a Title Case folder; a kebab-case or TitleCase one has none.
   - **Flat collection:** no `##` groupings — just the bullet list of blueprints under the marker.

   ```markdown
   # <Collection>

   <!-- index: <Collection> (regenerated) -->

   ## identity
   - [Magic Link Sign-In](identity/magic-link-sign-in.md) — passwordless sign-in by an emailed single-use link.
   - [Session Management](identity/session-management.md) — keep a signed-in user across visits, and let them end access on a device.
   ```
6. **Reconcile against the Framework.**
   - A sub-folder with blueprints but **no description in the Framework** — note it and ask the owner to add one to the Collections section; don't invent it.
   - A sub-folder described in the Framework but **with no blueprints** — dangling; flag it.
7. **Report** — the collections and blueprints indexed, any blueprints still missing a `summary` (and where), and any sub-folder still needing a description in the Framework.

## Notes

- Regenerable and idempotent: running it again yields the same file (plus any new blueprints). It never gates — an index annotates and navigates, it doesn't validate. The script's `--check` mode verifies an index is current without writing — useful in CI or a pre-commit hook.
- More than one level of sub-folders under a collection is discouraged (see EIDOS.md). If you find deeper nesting, index the first level and flag the rest for the owner.
- This is the leaf half of Eidos navigation; the top index is `_eidos/Framework.md` (Top-Level documents + Collections), kept by `configure`, with the visible root `README.md` as its door. The property/shape form lives in `_eidos/` and is handled by the other skills.
