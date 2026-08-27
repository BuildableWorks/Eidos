---
name: eidos-configure
description: >-
  Configure an Eidos definition's framework — the structure and contract held in the body of `_eidos/Framework.md`: its Collections (top-level content folders) and their Flavors (body shapes), its property Schema (the frontmatter contract every item carries), and its Top-Level document index — with the visible root `README.md` as the door to it. Use whenever someone wants to add a kind of content folder ("add a Decisions/ADR folder", "we need a Personas collection"), add or change a body flavor ("add a micro spec template", "give specs a full and a micro version", "make spec.full the default"), add, rename, or retire a custom property and backfill it across items ("add a `team` field to every spec", "we need to track a review date", "every entry should have an owner team"), or refresh the framework's Top-Level index ("update the framework index", "the Framework is out of date"). It presses the owner to decide each thing in full — a collection's name/grouping/flavors, a flavor's shape, a property's type/applies-to/meaning — never just a name, then scaffolds folders and `{kind}.{flavor}.md` shape files, writes the Framework, and reconciles the items. It does not author items (use `eidos`), build a collection's per-item `index.md` (use `eidos-index`), or touch the Eidos core properties, which move with the standard's version (use `eidos-migrate`).
---

# Eidos Configure

Keep `_eidos/Framework.md` working as the framework's **index and contract** — the authoritative description of the form the definition is written in, with the visible root `README.md` as the friendly door to it. This skill owns the three indexed parts of the Framework body:

- **Top-Level** — the top-level documents, `README.md` first (the visible front door and the first listed entry), then the owner's own one-of-a-kind docs (a Roadmap, a Vision, the generated Framework Map), each a link and a one-line description. The framing docs (Architecture, Audience, Criteria, Market) are **not** here — they live in the `Frames` collection.
- **Collections** — each top-level content folder: its grouping (one level of sub-folders) and its **flavors** (body shapes, one marked default), plus a pointer to its generated `index.md` leaf.
- **Schema** — the property contract every item carries, in two blocks: `### Eidos Core` (the standard's, off-limits here) and `### Custom Properties` (the framework's — the seed's defaults plus your own, each scoped by Applies To).

This skill scaffolds collections and flavors, grows and reshapes the custom Schema and reconciles items to it, and refreshes the Top-Level index. It does **not** author items (that's `eidos`), build a collection's per-item `index.md` (that's `eidos-index`), or touch `### Eidos Core` — those core properties move with the standard's version (`eidos-migrate`). For anything the rules decide — what a collection is, the flavor model, the `flavor` property — defer to **EIDOS.md**.

## How you work: press the owner to decide

A collection, flavor, or property nobody thought through is like an item nobody thought through — it reads as meaningful while no one actually knows what it holds. So you do **not** invent collections, flavors, or properties, or guess their shape. Facilitate; the owner decides.

- **For a collection:** its **name** (the folder, in the framework's naming convention), a one-line **description**, how it **groups** its items (one level of sub-folders, or flat), at least one **flavor** with a **default**, and how it **draws** on the canvas (below).
- **For a flavor:** its **name** (lowercase, e.g. `full`, `micro`, `api`), a one-line **description**, and its **shape** — the sections the body carries.
- **For a property:** all four —
  - **name** — the frontmatter key. Lowercase, words joined by underscores, matching the core style (`summary`, `connects_to`). Short and stable.
  - **type** — from the set Obsidian uses: **Text, List, Number, Checkbox, Date, Date & time**. If the owner wants something richer than one of those — a structured object, an enum with behavior — that almost belongs in the body (a shape), not a property. Say so.
  - **applies to** — which collections carry it: `all`, or a list of collection names. The property lands only on items in those collections — this is how you avoid a field that makes no sense on half the definition. Absence where it applies is a soft gap the validator notes, never refuses.
  - **meaning** — one line: what it holds and why. This is what stops the property from rotting into a mystery field.

If the owner offers only a name, ask for the rest. Don't fill them in yourself.

## Boundaries

- **The Framework body only.** You edit the `## Top-Level`, `## Collections`, and `### Custom Properties` (under `## Schema`) sections of `_eidos/Framework.md`, and create shape files in `_eidos/shapes/`. You do **not** build a collection's per-item `index.md` (that's `eidos-index`) or author items (`eidos`).
- **Never touch `### Eidos Core`.** Those are the standard's properties, and they move with the version (`eidos-migrate`). If the owner wants to change a core property, that's a standards change, not a framework customization; redirect.
- **Needs a framework.** Read `_eidos/Framework.md` from the definition root (found by its `_eidos/` marker, usually `Blueprint/_eidos/`). If there is no `_eidos/`, no framework is installed — offer `eidos-install` first.
- **Read the actor first.** As with every Eidos operation, read `_eidos/user.md` and tune how you facilitate to the persona (see EIDOS.md).
- **Shapes are the owner's.** A flavor's sections are a content decision. Scaffold a starting point — usually by trimming the collection's default flavor — but let the owner shape it.
- **Don't silently drop values.** Renaming or retiring a property touches real data in real items. Surface what's there before changing it.

## Adding a collection

1. **Decide** the name, description, grouping (sub-folders or flat), at least a default flavor, and the canvas style with the owner.

   The **canvas style** is a real question, not a formality — ask it rather than defaulting. Items people read *whole* (loose prose: framing docs, decisions, personas) want `file`. Items people scan by their headline want `card from ## <Section>`, naming whichever section of the shape carries the one-paragraph summary. Pick the section off the shape you just agreed; don't assume a name. A collection that declares nothing gets a plain card embedding the whole item, which is rarely what anyone wants.
2. **Create the folder** under the definition root, named in the framework's naming convention (read `naming` from `Framework.md`). Keep its organization to **one level of sub-folders** — deeper is discouraged.
3. **Create the default flavor's shape** in `_eidos/shapes/` as `<kind>.<flavor>.md` (e.g. `decision.full.md`), body-only, with the sections the owner wants and italic guidance prompts. Pattern it on the existing shapes.
4. **Register it** under `## Collections` in `Framework.md`: a `###` heading (the collection name), the description, then plain bullets — a **Leaf** pointer to its `index.md`, the **Flavors** (one bullet each, the default marked), and the grouping (its sub-folders as bullets, each with a short description; or "ungrouped" if flat). Use bullets, never separators like `·` — someone adding a flavor should be able to copy a line:

   ```markdown
   ### Decisions

   Architecture decision records — one per significant choice.

   - **Leaf:** [Decisions/index.md](../Decisions/index.md)
   - **Flavors:**
     - [decision.full.md](shapes/decision.full.md) — context, decision, consequences (default).
   - **Canvas:** card from `## Decision`
   - Ungrouped — a flat, dated list.
   ```

   The **Canvas** bullet takes `file`, `card`, or `card from ## <Section>`. It is the only thing telling `eidos-canvas` how this collection draws — the generator reads the declaration and knows no collection by name, so an undeclared collection falls back to a plain whole-item card.
5. **A grouping property is optional and the collection's own.** The software seed scopes `domain` (applies-to) to `Specs`; other collections group by their sub-folders, recorded in the Framework, not by a property. If the owner wants a grouping property on a new collection, or `domain` somewhere else, that's a Schema change — handle it as a property change below; don't touch core properties.
6. **Build the leaf and hand off.** Run `eidos-index` to create the new collection's `index.md`, and point the owner to `eidos` to author the first item. Report the folder created, the shape file added, and the Collections entry written.

## Adding a flavor to a collection

1. **Decide** the flavor's name, description, and shape with the owner. A good second flavor is a deliberate variant — a lighter `micro` to grow into `full`, or an `api` vs `ui` split — not a per-`type` fork (EIDOS.md forbids that).
2. **Create the shape file** `_eidos/shapes/<kind>.<flavor>.md`. Start from the collection's default flavor and trim or extend it to what the owner wants; keep the section order and names of whatever it shares with the default.
3. **Register it** under the collection in `Framework.md`, in the **Flavors** line with its link. If this flavor should be the default, move the `(default)` marker to it (and only it).
4. **Existing items are untouched.** An item's flavor is recorded in its `flavor` property (absent = the collection's default); adding a flavor doesn't change any existing item. Authoring a new item in this flavor is `eidos`'s job.
5. **Report** — the shape file added and the Collections entry updated, noting which flavor is now default.

## Adding a property

1. **Decide the four** (name, type, applies to, meaning — above) with the owner.
2. **Write the row** into `### Custom Properties` in the Framework's `## Schema`:

   ```markdown
   | Name | Type | Applies To | Meaning                     |
   | ---- | ---- | ---------- | --------------------------- |
   | team | Text | all        | Owning team, for filtering. |
   ```

   (Match the existing table's Title Case column headers.)
3. **Backfill the items.** Read the collections from `_eidos/Framework.md`, then walk every item **in the collections the property applies to** (all of them, or just the ones listed). Add the key to each with an empty or owner-supplied stub value, so each is conformant and the owner can fill it. Items in collections it doesn't apply to are left alone. Because new items are generated from the Schema, only the pre-existing ones need this.
4. **Report** — the row added, and the list of items touched (with which still need a value filled).

## Renaming a property

1. Confirm the new name with the owner (same naming rule). This is for the framework's own custom properties — not `### Eidos Core`.
2. Update the `Name` cell in the Framework's `## Schema`.
3. Rename the key in every item's frontmatter, **carrying the value across unchanged**.
4. Report the items touched. The property's meaning and data are unchanged — only the key moved.

## Retiring a property

1. **Surface first.** Find every item that carries the property and show the owner the values that would be lost. Ask whether to fold them somewhere (e.g. into the body) or deliberately drop them.
2. Remove the row from `### Custom Properties`.
3. Remove the key from every item's frontmatter, once the owner has agreed to let the values go.
4. Report the items touched and anything carried over.

Each seed ships a few custom defaults that are the framework's to keep, scope, or drop — a lifecycle, the two dates, tags, a grouping, a dependency list. Read the framework's own `### Custom Properties` rather than assuming a set, and reshape or retire any of them the same way — they live in `### Custom Properties`, not `### Eidos Core`.

## Refreshing the Top-Level index

1. **Enumerate the top-level documents** at the definition root — `README.md` is the **first** top-level document (the visible front door and a listed entry), then the owner's own one-of-a-kind docs (a Roadmap, a Vision, the generated Framework Map). The framing docs are collection items under `Frames/`, not top-level.
2. **Rebuild the list** under `## Top-Level`, between the `<!-- eidos-configure: top-level index (regenerated) -->` marker and the next heading: one bullet per doc, `- [Title](../Title.md) — one-line description`. Lead with `README` first (`- [README](../README.md) — …`), then the owner's docs. **Keep the owner's existing descriptions**; only add a bullet (with a `<!-- TODO: describe -->`) for a doc that has none, and ask the owner to describe it. Don't invent descriptions.
3. **Report** — the docs indexed and any still needing a description. A top-level doc that's still a stub is **in progress** — note it so the intention to complete it stays visible.

## After

The Framework is a current index and contract for the definition. From here, `eidos` reads it to know an item's collection and flavors when authoring, and validates each item against the updated Schema — a custom property now counts among the fields it checks for the collections it applies to, surfaced and added with a note where an applicable item is missing it, never failing the file. `eidos-index` rebuilds each collection's `index.md` (the per-item leaf) beneath it; and `README.md` is the visible door a human lands at first.
