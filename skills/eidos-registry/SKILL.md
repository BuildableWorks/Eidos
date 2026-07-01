---
name: eidos-registry
description: >-
  Tend an Eidos registry's index — its Collections (top-level content folders) and their Flavors (body shapes), and the Top-Level documents — all held in the body of `_eidos/Registry.md`, with the visible root `README.md` as its door. Use whenever someone wants to add a new kind of content folder ("add a Decisions/ADR folder", "we need a Personas collection"), add or change a body flavor for a collection ("add a micro spec template", "give specs a full and a micro version", "make spec.full the default"), or refresh the registry's Top-Level index ("update the registry index", "the Registry is out of date"). It presses the owner to decide each collection's name/description/grouping/flavors and each flavor's shape, scaffolds the folder and the `{kind}.{flavor}.md` shape files, and keeps the Registry's Top-Level and Collections sections current. It does not author items (use `eidos`), build a collection's per-item `index.md` (use `eidos-index`), or change the property Schema (use `eidos-schema`).
---

# Eidos Registry

Keep `_eidos/Registry.md` working as the registry's **index** — the authoritative description of the whole registry, with the visible root `README.md` as the friendly door to it. The Registry body has two indexed parts:

- **Top-Level** — the top-level documents, `README.md` first (the visible front door and the first listed entry), then the owner's own one-of-a-kind docs (a Roadmap, a Vision, the generated Registry Map), each a link and a one-line description. The framing docs (Architecture, Audience, Criteria, Market) are **not** here — they live in the `Frames` collection.
- **Collections** — each top-level content folder: its grouping (one level of sub-folders) and its **flavors** (body shapes, one marked default), plus a pointer to its generated `index.md` leaf.

`Registry.md` also carries a `## Schema` section (the property contract) — but that belongs to `eidos-schema`, not this skill. You manage **Top-Level** and **Collections**; you never touch **Schema**.

This skill adds collections and flavors and refreshes the Top-Level index. It does **not** author items (that's `eidos`), build a collection's per-item `index.md` (that's `eidos-index`), or change the frontmatter contract — the `## Schema` section (that's `eidos-schema`). For anything the rules decide — what a collection is, the flavor model, the `flavor` property — defer to **EIDOS.md**.

## How you work: press the owner to decide

A collection or flavor nobody thought through is like an item nobody thought through — it reads as meaningful while no one knows what it holds. So you do **not** invent collections or flavors or guess their shape. Facilitate; the owner decides.

- **For a collection:** its **name** (the folder, in the registry's naming convention), a one-line **description**, how it **groups** its items (one level of sub-folders, or flat), and at least one **flavor** with a **default**.
- **For a flavor:** its **name** (lowercase, e.g. `full`, `micro`, `api`), a one-line **description**, and its **shape** — the sections the body carries.

If the owner offers only a name, ask for the rest. Don't fill them in yourself.

## Boundaries

- **Registry body only.** You edit the `## Top-Level` and `## Collections` sections of `_eidos/Registry.md`, and create shape files in `_eidos/shapes/`. You do not touch the frontmatter contract (the `## Schema` section of `Registry.md` — that's `eidos-schema`), build the per-collection `index.md` (that's `eidos-index`), or author items (`eidos`).
- **Needs a registry.** Read `_eidos/Registry.md` from the registry root (found by its `_eidos/` marker, usually `Blueprint/_eidos/`). If there is no `_eidos/`, the registry isn't set up — offer `eidos-install` first.
- **Read the actor first.** As with every Eidos operation, read `_eidos/user.md` and tune how you facilitate to the persona (see EIDOS.md).
- **Shapes are the owner's.** A flavor's sections are a content decision. Scaffold a starting point — usually by trimming the collection's default flavor — but let the owner shape it.

## Adding a collection

1. **Decide** the name, description, grouping (sub-folders or flat), and at least a default flavor with the owner.
2. **Create the folder** under the registry root, named in the registry's naming convention (read `naming` from `Registry.md`). Keep its organization to **one level of sub-folders** — deeper is discouraged.
3. **Create the default flavor's shape** in `_eidos/shapes/` as `<kind>.<flavor>.md` (e.g. `decision.full.md`), body-only, with the sections the owner wants and italic guidance prompts. Pattern it on the existing shapes.
4. **Register it** under `## Collections` in `Registry.md`: a `###` heading (the collection name), the description, then plain bullets — a **Leaf** pointer to its `index.md`, the **Flavors** (one bullet each, the default marked), and the grouping (its sub-folders as bullets, each with a short description; or "ungrouped" if flat). Use bullets, never separators like `·` — someone adding a flavor should be able to copy a line:

   ```markdown
   ### Decisions

   Architecture decision records — one per significant choice.

   - **Leaf:** [Decisions/index.md](../Decisions/index.md)
   - **Flavors:**
     - [decision.full.md](shapes/decision.full.md) — context, decision, consequences (default).
   - Ungrouped — a flat, dated list.
   ```
5. **`domain` is the Specs grouping property.** It's a custom property scoped (applies-to) to `Specs`; other collections group by their sub-folders, recorded in the Registry, not by a property. If the owner wants `domain` on another collection, or off Specs, that's a Schema question — redirect to `eidos-schema`; don't change core properties here.
6. **Build the leaf and hand off.** Run `eidos-index` to create the new collection's `index.md`, and point the owner to `eidos` to author the first item. Report the folder created, the shape file added, and the Collections entry written.

## Adding a flavor to a collection

1. **Decide** the flavor's name, description, and shape with the owner. A good second flavor is a deliberate variant — a lighter `micro` to grow into `full`, or an `api` vs `ui` split — not a per-`type` fork (EIDOS.md forbids that).
2. **Create the shape file** `_eidos/shapes/<kind>.<flavor>.md`. Start from the collection's default flavor and trim or extend it to what the owner wants; keep the section order and names of whatever it shares with the default.
3. **Register it** under the collection in `Registry.md`, in the **Flavors** line with its link. If this flavor should be the default, move the `(default)` marker to it (and only it).
4. **Existing items are untouched.** An item's flavor is recorded in its `flavor` property (absent = the collection's default); adding a flavor doesn't change any existing item. Authoring a new item in this flavor is `eidos`'s job.
5. **Report** — the shape file added and the Collections entry updated, noting which flavor is now default.

## Refreshing the Top-Level index

1. **Enumerate the top-level documents** at the registry root — `README.md` is the **first** top-level document (the visible front door and a listed entry), then the owner's own one-of-a-kind docs (a Roadmap, a Vision, the generated Registry Map). The framing docs are collection items under `Frames/`, not top-level.
2. **Rebuild the list** under `## Top-Level`, between the `<!-- eidos-registry: top-level index (regenerated) -->` marker and the next heading: one bullet per doc, `- [Title](../Title.md) — one-line description`. Lead with `README` first (`- [README](../README.md) — …`), then the owner's docs. **Keep the owner's existing descriptions**; only add a bullet (with a `<!-- TODO: describe -->`) for a doc that has none, and ask the owner to describe it. Don't invent descriptions.
3. **Report** — the docs indexed and any still needing a description. A top-level doc that's still a stub is **in progress** — note it so the intention to complete it stays visible.

## After

The Registry is a current index of the registry. From here, `eidos` reads it to know an item's collection and flavors when authoring and validating; `eidos-index` rebuilds each collection's `index.md` (the per-item leaf) beneath it; and `README.md` is the visible door a human lands at first.
