---
name: eidos-schema
description: >-
  Add, rename, or retire a custom property in an Eidos registry's Schema, and backfill it across the items it applies to. Use whenever someone wants a new field on their items — "add a `team` field to every spec", "we need to track a review date", "I want a risk property", "every entry should have an owner team" — or wants to rename or remove a custom property they added before. This is the only correct way to extend a registry's frontmatter contract: it presses the owner to decide the property's type, meaning, and which collections it applies to (not just a name), writes it into the registry's Schema (the `## Schema` section of `_eidos/Registry.md`), and updates every item in those collections. It does not touch the Eidos core properties — those move with the standard's version (use `eidos-migrate`).
---

# Eidos Schema

Tend a registry's **property Schema** — the frontmatter contract every item carries. The Schema lives in the `## Schema` section of `_eidos/Registry.md`, in two blocks: `### Eidos Core` (the standard's, off-limits here) and `### Custom Properties` (the registry's — the seed's defaults plus your own). This skill grows and reshapes that custom block and reconciles every item to it.

A custom property is decided in full (name, type, **applies to**, meaning), added to `### Custom Properties`, and then **backfilled across the items it applies to** so the registry stays consistent. A property is scoped: its **applies to** lists the collections that carry it (`all`, or a list like `Specs`) — so `domain` can be Specs-only and never lands on a `Frames` item. Renaming and retiring a property are the same move in reverse.

The `eidos` skill authors and validates against the Schema; this skill _changes_ its custom block. `eidos-registry` tends the other parts of the Registry (Top-Level, Collections) — not the Schema.

## How you work: press the owner to decide

A property nobody thought through is like an item nobody thought through — it reads as meaningful while no one actually knows what it holds. So you do **not** invent properties or guess their shape. Before writing anything, get the owner to decide all four:

- **name** — the frontmatter key. Lowercase, words joined by underscores, matching the core style (`owner`, `depends_on`). Short and stable.
- **type** — from the set Obsidian uses: **Text, List, Number, Checkbox, Date, Date & time**. If the owner wants something richer than one of those — a structured object, an enum with behavior — that almost belongs in the body (a shape), not a property. Say so.
- **applies to** — which collections carry it: `all`, or a list (`Specs`, `Frames`). The property lands only on items in those collections — this is how you avoid a field that makes no sense on half the registry. Absence where it applies is a soft gap the validator notes, never refuses.
- **meaning** — one line: what it holds and why. This is what stops the property from rotting into a mystery field.

If the owner only offers a name, ask for the rest. Don't fill them in yourself.

## Boundaries

- **The custom block, not the core.** You edit `### Custom Properties` in the Registry's `## Schema` — including the seed's shipped defaults: `status`, the two dates, and `tags` (applies-to: all), plus `domain`, `depends_on`, and `type` (applies-to: `Specs`) — which are the registry's to keep, scope, or drop. Never touch `### Eidos Core` — those are the standard's, and they move with the version (`eidos-migrate`). If the owner wants to change a core property, that's a standards change, not a registry customization; redirect.
- **Needs a registry.** Read `_eidos/Registry.md` from the registry root (usually `Blueprint/_eidos/`). If there is no `_eidos/`, the registry isn't set up — offer `eidos-install` first.
- **Don't silently drop values.** Retiring or renaming a property touches real data in real items. Surface what's there before changing it.

## Adding a property

1. **Decide the four** (above) with the owner.
2. **Write the row** into `### Custom Properties` in the Registry's `## Schema`:

   ```markdown
   | Name | Type | Applies To | Meaning                     |
   | ---- | ---- | ---------- | --------------------------- |
   | team | Text | all        | Owning team, for filtering. |
   ```

   (Match the existing table's Title Case column headers.)
3. **Backfill the items.** Read the collections from `_eidos/Registry.md`, then walk every item **in the collections the property applies to** (all of them, or just the ones listed). Add the key to each with an empty or owner-supplied stub value, so each is conformant and the owner can fill it. Items in collections it doesn't apply to are left alone. Because new items are generated from the Schema, only the pre-existing ones need this.
4. **Report** — the row added, and the list of items touched (with which still need a value filled).

## Renaming a property

1. Confirm the new name with the owner (same naming rule).
2. Update the `Name` cell in the Registry's `## Schema`.
3. Rename the key in every item's frontmatter, **carrying the value across unchanged**.
4. Report the items touched. The property's meaning and data are unchanged — only the key moved.

## Retiring a property

1. **Surface first.** Find every item that carries the property and show the owner the values that would be lost. Ask whether to fold them somewhere (e.g. into the body) or deliberately drop them.
2. Remove the row from `### Custom Properties`.
3. Remove the key from every item's frontmatter, once the owner has agreed to let the values go.
4. Report the items touched and anything carried over.

## After

The registry's contract and its items are back in sync. From here, `eidos` validates against the updated Schema — a custom property now counts among the fields it checks for the collections it applies to, surfaced and added with a note where an applicable item is missing it, never failing the file.
