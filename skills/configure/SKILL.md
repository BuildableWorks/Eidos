---
name: configure
description: >-
  Configure an Eidos definition's framework — the structure and contract in `_eidos/Framework.md`: its Collections (top-level content folders) and their Flavors (body shapes), its property Schema (the frontmatter contract every item carries), and its Top-Level document index. Use whenever someone wants to add a kind of content folder ("add a Decisions/ADR folder", "we need a Roles collection"), add or change a body flavor ("add a micro spec template", "make spec.full the default"), add, rename, or retire a custom property and backfill it across items ("add a `team` field to every spec", "every entry should have an owner team"), or refresh the Top-Level index ("update the framework index", "the Framework is out of date"). It scaffolds the folders and shape files and reconciles the items. It does not author items (use `eidos`), build a collection's per-item `index.md` (use `index`), or touch the Eidos core properties, which move with the standard's version (use `migrate`).
---

# Eidos Configure

Keep `_eidos/Framework.md` working as the framework's **index and contract** — the authoritative description of the form the definition is written in, with the visible root `README.md` as the friendly door to it. This skill owns the three indexed parts of the Framework body:

- **Top-Level** — the top-level documents, `README.md` first (the visible front door and the first listed entry), then the owner's own one-of-a-kind docs (a Roadmap, a Vision, the generated Framework Map), each a link and a one-line description. The framing docs are **not** here — they are a collection.
- **Collections** — each top-level content folder: its grouping (one level of sub-folders) and its **flavors** (body shapes, one marked default), plus a pointer to its generated `index.md` leaf.
- **Schema** — the property contract every item carries, in two blocks: `### Eidos Core` (the standard's, off-limits here) and `### Custom Properties` (the framework's — the seed's defaults plus your own, each scoped by Applies To).

It scaffolds collections and flavors, grows and reshapes the custom Schema and reconciles items to it, and refreshes the Top-Level index. For anything the rules decide — what a collection is, the flavor model, the `flavor` property — defer to **EIDOS.md**.

## How you work: press the owner to decide

A collection, flavor, or property nobody thought through reads as meaningful while no one knows what it holds. Don't invent them or guess their shape — facilitate; the owner decides. If they offer only a name, ask for the rest.

- **For a collection:** its **name** (the folder, in the framework's naming convention), a one-line **description**, how it **groups** its items (one level of sub-folders, or flat), at least one **flavor** with a **default**, and how it **draws** on the canvas (below).
- **For a flavor:** its **name** (lowercase, e.g. `full`, `micro`, `api`), a one-line **description**, and its **shape** — the sections the body carries.
- **For a property:** all four —
  - **name** — the frontmatter key. Lowercase, words joined by underscores, matching the core style (`summary`, `connects_to`). Short and stable.
  - **type** — from the Obsidian set: **Text, List, Number, Checkbox, Date, Date & time**. Anything richer — a structured object, an enum with behavior — belongs in the body, not a property. Say so.
  - **applies to** — `all`, or a list of collection names, so a field never lands where it makes no sense. Absence where it applies is a soft gap the validator notes, never refuses.
  - **meaning** — one line: what it holds and why. This is what stops it rotting into a mystery field.

## Boundaries

- **The Framework body only.** You edit its `## Top-Level`, `## Collections`, and `### Custom Properties` sections, and create shape files in `_eidos/shapes/`. Not per-item `index.md` files (`index`), not items (`eidos`).
- **Never touch `### Eidos Core`.** Those move with the standard's version (`migrate`). A core property change is a standards change; redirect.
- **Needs a framework.** Read `_eidos/Framework.md` from the definition root, found by its `_eidos/` marker. No `_eidos/` means no framework installed — offer `install` first.
- **Read the actor first.** `_eidos/me.md`, and tune how you facilitate to the role.
- **Shapes are the owner's.** A flavor's sections are a content decision. Scaffold a starting point — usually by trimming the collection's default flavor — but let the owner shape it.
- **Don't silently drop values.** Renaming or retiring a property touches real data in real items. Surface what's there before changing it.

## Adding a collection

1. **Decide** the name, description, grouping (sub-folders or flat), at least a default flavor, and the canvas style with the owner.

   The **canvas style** is a real question — ask it. Items read *whole* (loose prose: framing docs, decisions) want `file`; items scanned by their headline want `card from ## <Section>`, naming whichever section of the shape you just agreed carries the summary. Don't assume a section name. Declaring nothing gets a plain whole-item card, which is rarely what anyone wants.
2. **Create the folder** under the definition root, named in the framework's naming convention (read `naming` from `Framework.md`). Keep its organization to **one level of sub-folders** — deeper is discouraged.
3. **Create the default flavor's shape** in `_eidos/shapes/` as `<kind>.<flavor>.md` (e.g. `decision.full.md`), body-only, with the sections the owner wants and italic guidance prompts. Pattern it on the existing shapes.
4. **Register it** under `## Collections` in `Framework.md`: a `###` heading, the description, then bullets — **Leaf**, **Flavors** (default marked), **Canvas**, and the grouping (sub-folders each with a short description, or "ungrouped"). Bullets, never `·` separators, so someone adding a flavor can copy a line:

   ```markdown
   ### Decisions

   Architecture decision records — one per significant choice.

   - **Leaf:** [Decisions/index.md](../Decisions/index.md)
   - **Flavors:**
     - [decision.full.md](shapes/decision.full.md) — context, decision, consequences (default).
   - **Canvas:** card from `## Decision`
   - Ungrouped — a flat, dated list.
   ```

   The **Canvas** bullet is the only thing telling `canvas` how this collection draws — it knows no collection by name.
5. **A grouping property is optional and the collection's own.** Most collections group by sub-folder alone, recorded in the Framework. If the owner wants a property carrying the grouping, that's a Schema change — handle it as a property change below.
6. **Build the leaf and hand off.** Run `index` for the new `index.md`, point the owner to `eidos` for the first item, and report the folder, shape file, and Collections entry.

## Adding a flavor to a collection

1. **Decide** the flavor's name, description, and shape with the owner. A good second flavor is a deliberate variant — a lighter one to grow out of, or a genuine split in kind — never a fork per category label, which EIDOS.md forbids.
2. **Create the shape file** `_eidos/shapes/<kind>.<flavor>.md`. Start from the collection's default flavor and trim or extend it to what the owner wants; keep the section order and names of whatever it shares with the default.
3. **Register it** under the collection in `Framework.md`, in the **Flavors** line with its link. If this flavor should be the default, move the `(default)` marker to it (and only it).
4. **Existing items are untouched** — an absent `flavor` still means the collection's default. Authoring in the new flavor is `eidos`'s job.
5. **Report** the shape file added and the Collections entry updated, noting which flavor is now default.

## Adding a property

1. **Decide the four** (name, type, applies to, meaning — above) with the owner.
2. **Write the row** into `### Custom Properties` in the Framework's `## Schema`:

   ```markdown
   | Name | Type | Applies To | Meaning                     |
   | ---- | ---- | ---------- | --------------------------- |
   | team | Text | all        | Owning team, for filtering. |
   ```

   (Match the existing table's Title Case column headers.)
3. **Backfill the items** in the collections it applies to, with an empty or owner-supplied stub so each is conformant and fillable. Items elsewhere are left alone; new items are generated from the Schema, so only pre-existing ones need this.
4. **Report** the row added and the items touched, flagging which still need a value.

## Renaming a property

1. Confirm the new name (same naming rule). Custom properties only — never `### Eidos Core`.
2. Update the `Name` cell in the Framework's `## Schema`.
3. Rename the key in every item's frontmatter, **carrying the value across unchanged**.
4. Report the items touched. Only the key moved.

## Retiring a property

1. **Surface first.** Show the owner every value that would be lost, and ask whether to fold them somewhere or deliberately drop them.
2. Remove the row from `### Custom Properties`.
3. Remove the key from every item, once the owner has agreed to let the values go.
4. Report the items touched and anything carried over.

A seed's own defaults — a lifecycle, dates, tags, a grouping — are reshaped or retired the same way. Read the framework's `### Custom Properties` rather than assuming a set.

## Refreshing the Top-Level index

1. **Enumerate the top-level documents** at the definition root — `README.md` first, then the owner's own one-of-a-kind docs. Frames are collection items, not top-level.
2. **Rebuild the list** under `## Top-Level`, after the `<!-- configure: top-level index (regenerated) -->` marker: one bullet per doc, `- [Title](../Title.md) — one-line description`, `README` first. **Keep the owner's existing descriptions**; give a doc with none a `<!-- TODO: describe -->` and ask. Never invent one.
3. **Report** — the docs indexed and any still needing a description. A top-level doc that's still a stub is **in progress** — note it so the intention to complete it stays visible.

## After

The Framework is a current index and contract for the definition. From here, `eidos` reads it to know an item's collection and flavors when authoring, and validates each item against the updated Schema — a custom property now counts among the fields it checks for the collections it applies to, surfaced and added with a note where an applicable item is missing it, never failing the file. `index` rebuilds each collection's `index.md` (the per-item leaf) beneath it; and `README.md` is the visible door a human lands at first.
