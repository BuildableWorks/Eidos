---
name: eidos-index
description: >-
  Build or refresh a collection's `index.md` in an Eidos registry — the generated leaf that lists a collection's items so a human or agent can navigate without scraping the tree. Use when someone wants to "regenerate the index", "rebuild the specs index", "update Specs/index.md", "reindex the registry", "map the registry", says an index is stale, or after items have been added, renamed, moved, or removed. It reads the registry's declared collections, walks each collection's one-level sub-folders, and rewrites its `index.md` wholesale — each item a markdown link with its one-line `summary` property, grouped by sub-folder (Specs by domain) or flat. Ships a `build-index.py` that does the whole walk deterministically where a shell is available; falls back to doing it by hand on a sandboxed host. Regenerable and never gates.
---

# Eidos Index

Keep each collection's **`index.md`** current — the leaf a human or an agent reads to find an item without scraping the tree. An index lives inside its collection's folder (`Specs/index.md`), lists the collection's items grouped under their one-level sub-folders (Specs by domain) or flat, and is **fully generated**: a markdown link per item with the item's one-line `summary` property. Folder descriptions live in `_eidos/Registry.md`; this skill rebuilds only the listing.

This generalizes the former `eidos-domains` skill — every collection gets the same treatment, not just Specs.

## How you work: regenerate, don't author

Since 4.1.0 the one-line summary is a real frontmatter property (`summary`), authored once on the item and read here — so the index is **derived, not written**. Regenerating it is safe and mechanical. Two things stay the human's:

- **Descriptions.** A collection's description, and its sub-folder (e.g. domain) descriptions, live in `_eidos/Registry.md`, written once by the owner — the index does not carry them. If a sub-folder has no description in the Registry, note it and ask the owner; don't invent one.
- **The summaries themselves.** A summary is the item's own `summary` property; the index never adds meaning the item doesn't carry. An item with no `summary` yet is **flagged**, not invented — the owner (or `eidos` while authoring) writes it on the item, and the next regeneration picks it up.

## Run the script when you can

The skill ships **`build-index.py`** (beside this file) — stdlib-only Python 3 that does the entire walk deterministically. **Prefer it whenever you have a shell** (Claude Code, the IDE):

```
python3 <skill>/build-index.py <registry-root>            # rebuild every collection's index
python3 <skill>/build-index.py <registry-root> --check    # verify only; non-zero if any index is stale
python3 <skill>/build-index.py <registry-root> --collection Specs   # limit to one collection (repeatable)
```

`<registry-root>` is the folder that contains `_eidos/` (often the registry root, e.g. `Blueprint/`). The script reads the declared collections from `_eidos/Registry.md`, walks each, and rewrites each `index.md` from the items' `title` + `summary`. It prints any item missing a `summary` to stderr — **those are your only authoring task**: write a `summary` on each flagged item (distill its Intent to one plain line), then re-run the script. It does **not** touch the Registry, so still do the reconciliation in step 6 by reading `_eidos/Registry.md`.

On a **sandboxed host** (Claude Desktop) where you can't run the script, do the walk by hand — the procedure below is exactly what the script does.

## Where things are

- The collections are declared in `_eidos/Registry.md` (the `## Collections` section), each with its folder.
- Each collection's items live under `<Collection>/`, optionally in one level of sub-folders (`Specs/<Domain>/`).
- Each collection's index is `<Collection>/index.md`.
- This needs a set-up registry. If there's no `_eidos/`, it isn't an Eidos registry yet — offer `eidos-install`.

## Procedure (what the script does — and your fallback by hand)

1. **Read the actor** (`_eidos/user.md`) and the declared collections (`_eidos/Registry.md`).
2. **Decide which collections to re-index.** Default to all; if only some folders changed, the script's `--collection` filter (or your own scope by hand) limits the work. For a small registry, re-indexing everything is fine.
3. **For each chosen collection, walk its folder.** Read its one-level sub-folders (the grouping) and the items in each — or the items directly in the collection folder, if it's flat. For each item read its `title`, path, and `summary`.
4. **Take each item's `summary` verbatim.** It's one plain line already. If an item has **no** `summary`, flag it (the script writes a `⚠️ TODO` placeholder in the bullet and lists the file on stderr) — then write a `summary` on that item, distilling its Intent to one line, and regenerate. Never invent a summary into the index alone; it belongs on the item.
5. **Rewrite `<Collection>/index.md` wholesale.** It is fully generated — no hand-written prose to preserve — so rebuild the whole file:
   - An H1 of the collection name (`# Specs`) and the marker comment `<!-- eidos-index: <Collection> (regenerated) -->`.
   - **Grouped collection:** one `##` per sub-folder, then a bullet per item — `- [Title](<Sub-folder>/<File>.md) — summary`. Links are **relative to the collection folder** (`Identity/Magic%20Link%20Sign-In.md`, not `Specs/Identity/…`), built in the registry's naming convention (read `naming` from `_eidos/Registry.md`): encode spaces as `%20` in a Title Case registry; a TitleCase or kebab-case one has none.
   - **Flat collection:** no `##` groupings — just the bullet list of items under the marker.

   ```markdown
   # Specs

   <!-- eidos-index: Specs (regenerated) -->

   ## Identity
   - [Magic Link Sign-In](Identity/Magic%20Link%20Sign-In.md) — passwordless sign-in by an emailed single-use link.
   - [Session Management](Identity/Session%20Management.md) — keep a signed-in user across visits, and let them end access on a device.
   ```
6. **Reconcile against the Registry.**
   - A sub-folder (domain) with items but **no description in the Registry** — note it and ask the owner to add one to the Collections section; don't invent it.
   - A sub-folder described in the Registry but **with no items** — dangling; flag it.
7. **Report** — the collections and items indexed, any items still missing a `summary` (and where), and any sub-folder still needing a description in the Registry.

## Notes

- Regenerable and idempotent: running it again yields the same file (plus any new items). It never gates — an index annotates and navigates, it doesn't validate. The script's `--check` mode verifies an index is current without writing — useful in CI or a pre-commit hook.
- More than one level of sub-folders under a collection is discouraged (see EIDOS.md). If you find deeper nesting, index the first level and flag the rest for the owner.
- This is the leaf half of Eidos navigation; the top index is `_eidos/Registry.md` (Top-Level documents + Collections), kept by `eidos-registry`, with the visible root `README.md` as its door. The property/shape form lives in `_eidos/` and is handled by the other skills.
