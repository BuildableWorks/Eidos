---
name: eidos-canvas
description: >-
  Generate an Obsidian-compatible visual map of an Eidos registry — a JSON Canvas 1.0 `.canvas` file. Each spec is a text node embedding its `## Intent`; each Frame (the framing docs) is a full-file node in its own group; directories (Specs by domain) become nested group nodes; and an item's `connects_to` links are drawn as directed edges — the intentional map of how pieces relate. Use when someone wants to "see the registry as a canvas", "map the specs visually", "make an Obsidian canvas of the product", "show how things connect", "visualize the blueprint", or open the registry in Obsidian's Canvas view. The user picks which collections to include; dependencies (`depends_on`) are off by default but can be added in a distinct color. Top-level documents are not mapped. The generated `.canvas` is itself a top-level document. Where a shell exists it runs `build-canvas.py`; on a sandboxed host it emits the JSON by hand. Regenerable and never gates.
---

# Eidos Canvas

Produce a **visual map** of a registry that opens in Obsidian's Canvas view — a [JSON Canvas 1.0](https://jsoncanvas.org) `.canvas` file. It is navigation, like an index but spatial: nothing is authored, everything is derived from the items already in the registry.

- **Specs → text nodes that embed the item's `## Intent`** — a wikilink title over an Obsidian embed (`**[[Specs/Playback/Watch a Video|Watch a Video]]**` then `![[Specs/Playback/Watch a Video#Intent]]`), so the Intent shows on the card and the title opens the note. Each collection gets its own color (its group box and its cards); you propose the schema up front — see the creation flow.
- **Frames → full-file nodes** (the whole framing doc), in the `Frames` group. A framing doc is context you want to read whole, not a one-line Intent, so it's mapped as a file node rather than an Intent embed.
- **Directories → nested group nodes.** A collection is a group; each sub-directory (Specs by domain) is a group nested inside it; a directory nested under that becomes another nested group. Groups wrap their cards spatially.
- **`connects_to` → directed edges** (this → target), in the default edge color — the primary map of how pieces relate. A connection to something not on the canvas is flagged, not drawn.
- **`depends_on` → edges only with `--include-dependencies`**, drawn in a distinct color (purple by default) so implementation dependencies read differently from the intentional `connects_to` map.
- **Top-level documents are not mapped** — they frame the product; the canvas maps the collections. The generated `.canvas` is itself a top-level document (see the last step).

## The creation flow

Creating a canvas is a short conversation, not a one-shot — pick what goes on it, agree the colors, then generate:

1. **Read the actor** (`_eidos/user.md`) and list what's available — `python3 <skill>/build-canvas.py <registry-root> --list` prints the declared collections (and notes that top-level docs aren't mapped).
2. **Ask what to map** with `AskUserQuestion` — offer the declared collections (multi-select), default to all. A canvas can be the **whole registry** or a focused slice (`Specs`, or `Specs` plus `Frames`). `Frames` is a collection like any other; include or omit it.
3. **Propose a color schema.** Each collection gets its own color. Look at the registry — its collections (and, for `Specs`, the `type` values in play) — and propose a sensible mapping of one Obsidian preset per collection (1 red, 2 orange, 3 yellow, 4 green, 5 cyan, 6 purple); show it to the owner ("Frames = purple, Specs = green — look good?") and adjust to taste. **Skip this when a canvas already exists** at the output path: regenerating reuses its colors, so the owner's earlier choice sticks — don't re-ask.
4. **Generate** — run the script with the chosen scope and `--color NAME:N` per collection.

## Run the script when you can

The skill ships **`build-canvas.py`** (beside this file) — stdlib-only Python 3, the same shape as `eidos-index/build-index.py`. **Prefer it whenever you have a shell** (Claude Code, the IDE):

```
python3 <skill>/build-canvas.py <registry-root>                         # map all collections
python3 <skill>/build-canvas.py <registry-root> --list                  # show mappable collections
python3 <skill>/build-canvas.py <registry-root> --collection Specs      # one collection (repeatable)
python3 <skill>/build-canvas.py <registry-root> --include-dependencies  # also draw depends_on edges (purple)
python3 <skill>/build-canvas.py <registry-root> --color Frames:6 --color Specs:4   # the agreed color schema
python3 <skill>/build-canvas.py <registry-root> --collection Specs --collection Frames --out "Registry Map.canvas"
```

- `<registry-root>` is the folder that contains `_eidos/` (often the registry root, e.g. `Blueprint/`).
- With **no** `--collection` flags it maps every declared collection; with flags it maps exactly what's named.
- `--color NAME:N` sets a collection's color (Obsidian preset `1`–`6`); pass one per collection with the schema you agreed in step 3. Without it, collections fall back to a distinct-per-collection palette — but a canvas that already exists keeps its colors, so a regenerate is consistent. The script prints the final `colors:` mapping it used.
- `--include-dependencies` adds `depends_on` edges; `--dependency-color N` sets their Obsidian preset color (default `6` = purple). `connects_to` edges always use the default edge color.
- `--vault` sets the root the embed/file paths are relative to (default: the registry root — an Eidos registry is plausibly the vault). `--out` sets the output path (default: `<vault>/Registry Map.canvas`).
- It prints any **unresolved `connects_to`/`depends_on`** to stderr — a link that isn't an item on the canvas (an external id, or an item in a collection you didn't include). Safe to ignore, or add the missing collection and regenerate.

## Register the map as a top-level document

The generated `.canvas` is a **top-level document** of the registry — the spatial view of the whole product. After writing it, add it to `_eidos/Registry.md` under `## Top-Level` (a link with a one-line description), the same as any top-level doc — the script prints a ready-made bullet. `eidos-registry` keeps that section current.

## On a sandboxed host

Where you can't run the script (Claude Desktop), emit the `.canvas` JSON by hand following the structure below — it's heavier than an index, so the script is strongly preferred.

```json
{
  "nodes": [
    { "id": "group:Specs", "type": "group", "x": 0, "y": 0, "width": 840, "height": 830, "label": "Specs" },
    { "id": "group:Specs/Playback", "type": "group", "x": 40, "y": 70, "width": 760, "height": 330, "label": "Playback" },
    { "id": "watch-a-video", "type": "text", "text": "**[[Specs/Playback/Watch a Video|Watch a Video]]**\n\n![[Specs/Playback/Watch a Video#Intent]]", "x": 80, "y": 140, "width": 320, "height": 220, "color": "4" },
    { "id": "architecture", "type": "file", "file": "Frames/Architecture.md", "x": 0, "y": 890, "width": 320, "height": 220, "color": "6" }
  ],
  "edges": [
    { "id": "conn:resume-playback->watch-a-video", "fromNode": "resume-playback", "toNode": "watch-a-video", "toEnd": "arrow" },
    { "id": "dep:resume-playback->watch-a-video", "fromNode": "resume-playback", "toNode": "watch-a-video", "toEnd": "arrow", "color": "6" }
  ]
}
```

- **Edges**: one `conn:` edge per `connects_to` (uncolored); one `dep:` edge per `depends_on` **only when `--include-dependencies` is requested** (dependency color). The example above shows both to illustrate the shape — omit the `dep:` edge unless dependencies were asked for.
- **Specs are `text` nodes** whose text is a wikilink title over `![[<vault-path-without-.md>#Intent]]` (or `![[<vault-path>]]` when the note has no `## Intent`). **Frames are `file` nodes** — `{ "type": "file", "file": "<vault-path.md>" }`. Paths are vault-relative with literal spaces.
- **Group membership is spatial and nests** — a node (card or sub-group) belongs to the group whose box contains it; there is no parent field. Lay each directory as a grid of its cards, then its sub-directories as nested group boxes below.
- **Colors** are the preset strings `"1"`–`"6"` (1 red, 2 orange, 3 yellow, 4 green, 5 cyan, 6 purple). Each collection's group box **and** its item cards take that collection's agreed color; `connects_to` edges are uncolored; `depends_on` edges (if included) take the dependency color.
- **Node ids** are the item `id` (so `connects_to`/`depends_on` resolve to them); group ids are `group:<path>`.

## Notes

- Regenerable: re-run after items change to refresh the map. It never gates — a canvas annotates and navigates, it doesn't validate. Hand-layout tweaks in Obsidian are overwritten on regeneration, so treat the file as generated.
- This is a sibling of `eidos-index` (the textual leaf listing) — same walk, different rendering. The property/shape form lives in `_eidos/` and is handled by the other skills.
