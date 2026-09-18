---
name: configure
description: >-
  Configure a root's framework in `.eidos/Framework.yaml`: its folders (collections with their variants, assets, other), its Properties table, its Vocabulary, and its top-level index. Use to add a folder ("add a Decisions folder", "add an images folder"), add or change a variant ("add a micro spec template", "make spec.full the default"), add, rename, or retire a custom property and backfill it ("add a `team` field to every spec"), declare, rename, or retire a term ("a team member is not staff, write that down"), or refresh the root's declarations ("the Framework is out of date"). It does not author blueprints (`eidos`), build the index (`index`), or touch the Eidos core properties (`migrate`).
---

# Eidos Configure

You edit four keys of `.eidos/Framework.yaml` and nothing else: `top_level`, `folders`, `properties.custom`, and `vocabulary`. EIDOS.md defines what each key means; read it for anything the rules decide.

## Press the owner to decide

A folder, variant, property, or term nobody thought through reads as meaningful while no one knows what it holds. Never invent one; if the owner offers only a name, ask for the rest.

- **A folder:** `name` (in the framework's `naming`), `type` (`collection`, `assets`, or `other`), and a one-line `description`. A collection also needs how it groups (flat, or declared groups) and at least one variant marked default.
- **A variant:** `name` (lowercase: `full`, `micro`, `api`), a one-line `description`, and its template sections.
- **A property:** `name` (lowercase, underscores), `type` (Text, List, Number, Checkbox, Date, Date & time; anything richer belongs in the body), `applies_to` (`all` or collections), `required` (default to optional), one-line `meaning`, and `options` only when the value is one of a closed set the owner controls, in the order the values run. `variant` and a grouping property never carry `options`.
- **A term:** `term`, one-line `means`, and `not`: the near-misses, each with why it differs. Press here the way you press on non-goals; a term with nothing in `not` is not worth declaring yet.

## Boundaries

- **Never touch** `properties.core` (the standard's; `migrate`), any `properties.tools.<tool>` block or tool key on an entry (that tool's; carry them across unchanged), `.eidos/plugins/`, the `index` key (`index`), or blueprint bodies (`eidos`).
- **Needs a framework.** No `.eidos/` means offer `install`. A root on `Framework.md` (before 5.0.0) means offer `migrate`.
- **Read `me.md` first** and tune how you facilitate to the role.
- **Templates are the owner's.** Scaffold a starting point by trimming the collection's default variant; let the owner shape it.
- **Never silently drop values.** Renaming or retiring a property or narrowing its `options` touches real blueprints. Surface what is there first.

## Adding a folder

1. Decide name, type, and description with the owner; for a collection, its grouping and default variant too.
2. Create the folder under the root in the naming convention. For a grouped collection, create each declared group; a group holds blueprints and nothing deeper.
3. For a collection, create the default variant's template in `.eidos/templates/<unit>.<variant>.md`, body only, patterned on the existing templates.
4. Register it under `folders`:

   ```yaml
   - name: Decisions
     type: collection
     description: Architecture decision records, one per significant choice.
     variants:
       - { name: full, template: templates/decision.full.md, description: "context, decision, consequences", default: true }
   - { name: images, type: assets, description: Screenshots and diagrams the specs embed. }
   ```

5. A property carrying the grouping is a property change (below). For a collection, run `index`, then point the owner to `eidos` for the first blueprint.

## Adding a variant

1. Decide name, description, and template. A second variant is a lighter one to grow out of or a genuine split in kind, never a fork per category.
2. Create `.eidos/templates/<unit>.<variant>.md` from the default variant, keeping the order and names of shared sections.
3. Register it under the collection's `variants`. If it becomes the default, move `default: true` to it alone.
4. Existing blueprints are untouched; an absent `variant` still means the default.

## Properties

**Add:** decide the fields, write the entry under `properties.custom`, and backfill a required property into every existing blueprint it applies to with an empty or owner-supplied stub. An optional property backfills nothing.

```yaml
- { name: team, type: Text, applies_to: all, required: true, meaning: "Owning team, for filtering." }
- { name: tier, type: Text, applies_to: all, options: [Core, Extended, Experimental], meaning: "How central the unit is." }
```

**Rename:** update `name`, then rename the key in every blueprint's frontmatter, carrying values unchanged.

**Retire:** show the owner every value that would be lost and ask whether to fold or drop them, then remove the entry and the key.

**Options:** narrowing a list is retiring values (surface every blueprint carrying one first); widening touches nothing; adding `options` to an open property means surfacing every existing value off the new list.

Report the blueprints touched every time.

## Terms

**Declare:** most terms arrive as a collision (two words for one thing, or one word for two). Start there. Write the entry under `vocabulary`, with `see` pointing at the blueprint that defines it in full when one does. Then search the blueprints for each word in `not` and list where it appears with the declared term beside it; the owner decides which uses move, and the edit is `eidos`'s.

```yaml
- term: Team member
  means: A person with a login on a team, in any role.
  not: ["staff (payroll only)", "teammate (informal, never in a blueprint)"]
```

**Rename:** if the old word stays in use with another meaning, that is two entries, not a rename. Otherwise update `term`, usually moving the old word into `not`, and surface the blueprints using it.

**Retire:** surface where the term is used and ask whether the distinction or just the word is going. Remove the entry; the blueprints keep their text.

## Refreshing the root's declarations

1. List every file at the root (any extension) against `top_level`, and every folder against `folders`. Hidden entries (`.gitignore`, `.obsidian/`) are the host's and are not listed.
2. For a file with no entry, add one with an empty `description` and ask; never invent a description. For a folder with no entry, ask its type and description. For an entry whose file or folder is gone, tell the owner before dropping it; they may want the thing back rather than the entry.
3. Keep the owner's existing descriptions. Report what was added, what pointed at nothing, and what still needs a description.

## After

`eidos` reads the updated framework when authoring and validating; `index` rebuilds the `index` key. A custom property now counts among the fields checked for the collections it applies to, surfaced where missing and never failing the file.
