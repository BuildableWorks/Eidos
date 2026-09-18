---
name: configure
description: >-
  Configure a root's framework, the structure and contract in `.eidos/Framework.yaml`: its collections and their variants (body templates), its Properties table (the frontmatter contract), its Vocabulary (the terms the root uses on purpose), and its top-level index. Use to add a kind of content folder ("add a Decisions/ADR folder"), add or change a variant ("add a micro spec template", "make spec.full the default"), add, rename, or retire a custom property and backfill it ("add a `team` field to every spec"), declare, rename, or retire a term ("a team member is not staff, write that down", "add this to the vocabulary"), or refresh the top-level index ("the Framework is out of date"). It scaffolds folders and template files and reconciles the blueprints. It does not author blueprints (`eidos`), build the index (`index`), or touch the Eidos core properties (`migrate`).
---

# Eidos Configure

Keep `.eidos/Framework.yaml` working as the framework's **index and contract** — the authoritative description of the structure everything is written in, with the visible root `README.md` as the friendly door to it. This skill owns five of its keys:

- **`top_level`** — the top-level documents, `README.md` first (the visible front door and the first listed entry), then the owner's own one-of-a-kind docs (a Vision, the generated Blueprint Map), each a title, a path, and a one-line description. The framing docs are **not** here — they are a collection.
- **`collections`** — each top-level content folder: its description, its grouping (one level of sub-folders, each group described), and its **variants** (body templates, one marked default).
- **`properties`** — the property contract every blueprint carries, one block per owner: `core` (the standard's, off-limits here), `custom` (the framework's — the seed's defaults plus your own, each scoped by `applies_to`), and `tools.<tool>` for any tool that declares its own (that tool's, off-limits here too).
- **`vocabulary`** — the term contract: the words the root uses on purpose, one entry each (`term`, `means`, `not`, and `see` when a blueprint defines it in full). Every seed ships it empty; the terms are the root's own, and Eidos declares none of them.

It scaffolds collections and variants, grows and reshapes the custom Properties block and reconciles blueprints to it, grows the Vocabulary a term at a time, and refreshes the top-level index. For anything the rules decide — what a collection is, the variant model, the `variant` property, what a term is — defer to **EIDOS.md**.

## How you work: press the owner to decide

A collection, variant, or property nobody thought through reads as meaningful while no one knows what it holds. Don't invent them or guess their sections — facilitate; the owner decides. If they offer only a name, ask for the rest.

- **For a collection:** its **name** (the folder, in the framework's naming convention), a one-line **description**, how it **groups** its blueprints (one level of sub-folders, or flat), and at least one **variant** with a **default**.
- **For a variant:** its **name** (lowercase, e.g. `full`, `micro`, `api`), a one-line **description**, and its **template** — the sections the body carries.
- **For a property:** all five, and the sixth when it applies —
  - **name** — the frontmatter key. Lowercase, words joined by underscores, matching the core style (`summary`, `date_created`). Short and stable.
  - **type** — from the Obsidian set: **Text, List, Number, Checkbox, Date, Date & time**. Anything richer — a structured object, a value with behavior — belongs in the body, not a property. Say so.
  - **applies to** — `all`, or a list of collection names, so a field never lands where it makes no sense.
  - **required** — `true` or `false` (absent means `false`). Required: generated into every new blueprint it applies to, and a missing one is a soft gap the validator notes, never refuses. Optional: written when it has a value, absent otherwise, and never a gap. Default to optional; require only what the owner says every blueprint must answer.
  - **meaning** — one line: what it holds and why. This is what stops it rotting into a mystery field.
  - **options** — only when the value is one of a closed set (a lifecycle, a category the owner controls): the list, non-empty, on a Text or List property, in the order the values run (a lifecycle first stage to last; tools render and sort in that order). Exact match, case included. Off-list is surfaced, never refused. Without it any value is valid, so a label the owner wants open takes none; a `meaning` that lists values in prose is a set the entry should declare. No default rides with it: a required property with options is generated blank and the author picks. `variant` and a grouping property never carry it; their sets are the collection's.
- **For a term:** all three —
  - **term** — the word, as prose uses it. One word or a short phrase; if the owner offers two spellings, that is the first distinction to settle.
  - **means** — one line: what the word denotes in this root.
  - **not** — the near-misses, each with a clause on why it is a different thing. This is where the row earns its place, so press here the way you press on non-goals: "so a *teammate* is not a *team member*?" A term with nothing here is a dictionary entry, and usually not worth declaring yet.

## Boundaries

- **The framework document's declarations only.** You edit its `top_level`, `collections`, `properties.custom`, and `vocabulary` keys, documented in EIDOS.md, and create template files in `.eidos/templates/`. Never the generated `index` key (`index`), never blueprints (`eidos`). A framework on a version before 5.0.0 keeps a markdown `Framework.md`; offer `migrate` before editing it.
- **Never touch `properties.core` or a `properties.tools.<tool>` block.** Every property is owned by the block it sits in: the core is Eidos's and moves with the standard's version (`migrate`); a tool's block is written by that tool alone. A core property change is a standards change; a tool property change is that tool's; redirect either. The one exception is a tool that has left the root: then its block is retired like any property, values surfaced first, on the owner's say-so.
- **Never touch a tool's.** `.eidos/plugins/<name>/` is that tool's folder, and a key named for a tool on a property entry is that tool's fields on the entry. Carry them across unchanged when you edit an entry, never fill them in, and when retiring an entry that carries some, name the tool so the owner knows what else is affected.
- **Needs a framework.** Read `.eidos/Framework.yaml` from the root, found by its `.eidos/` marker. No `.eidos/` means no framework installed — offer `install` first.
- **Read `me.md` first.** `.eidos/me.md`, and tune how you facilitate to the role.
- **Templates are the owner's.** A variant's sections are a content decision. Scaffold a starting point — usually by trimming the collection's default variant — but let the owner shape it.
- **Don't silently drop values.** Renaming or retiring a property touches real data in real blueprints. Surface what's there before changing it.

## Adding a collection

1. **Decide** the name, description, grouping (sub-folders or flat), and at least a default variant with the owner.
2. **Create the folder** under the root, named in the framework's naming convention (read `naming` from `Framework.yaml`). Keep its organization to **one level of sub-folders** — deeper is discouraged.
3. **Create the default variant's template** in `.eidos/templates/` as `<unit>.<variant>.md` (e.g. `decision.full.md`), body-only, with the sections the owner wants and italic guidance prompts. Pattern it on the existing templates.
4. **Register it** under `collections` in `Framework.yaml`: an entry with its `name`, `description`, `variants` (default marked), and `grouping` (a label and a described group per sub-folder; none for a flat collection). One variant per line, so someone adding one can copy it:

   ```yaml
   - name: Decisions
     description: Architecture decision records, one per significant choice; a flat, dated list.
     variants:
       - { name: full, template: templates/decision.full.md, description: "context, decision, consequences", default: true }
   ```
5. **A grouping property is optional and the collection's own.** Most collections group by sub-folder alone, recorded in the Framework. If the owner wants a property carrying the grouping, that's a Properties change — handle it as a property change below.
6. **Build the index and hand off.** Run `index` so the new collection has its list, point the owner to `eidos` for the first blueprint, and report the folder, template file, and `collections` entry.

## Adding a variant to a collection

1. **Decide** the variant's name, description, and template with the owner. A good second variant is a deliberate one — a lighter one to grow out of, or a genuine split in kind — never a fork per category label, which EIDOS.md forbids.
2. **Create the template file** `.eidos/templates/<unit>.<variant>.md`, the collection's unit and then the variant. Start from the collection's default variant and trim or extend it to what the owner wants; keep the section order and names of whatever it shares with the default.
3. **Register it** under the collection's `variants` in `Framework.yaml`, with its `template` path. If this variant should be the default, move `default: true` to it (and only it).
4. **Existing blueprints are untouched** — an absent `variant` still means the collection's default. Authoring in the new variant is `eidos`'s job.
5. **Report** the template file added and the `collections` entry updated, noting which variant is now default.

## Adding a property

1. **Decide the five** (name, type, applies to, required, meaning — above) with the owner, and the options when the value is one of a set.
2. **Write the entry** under `properties.custom` in `Framework.yaml`:

   ```yaml
   - { name: team, type: Text, applies_to: all, required: true, meaning: "Owning team, for filtering." }
   - { name: tier, type: Text, applies_to: all, options: [Core, Extended, Experimental], meaning: "How central the unit is to the product." }
   ```
3. **Backfill the blueprints** in the collections it applies to, when it is required, with an empty or owner-supplied stub so each is conformant and fillable. An optional property backfills nothing. Blueprints elsewhere are left alone; new blueprints are generated from the Properties table, so only pre-existing ones need this.
4. **Report** the entry added and the blueprints touched, flagging which still need a value.

## Renaming a property

1. Confirm the new name (same naming rule). Custom properties only — never `properties.core`.
2. Update the entry's `name` under `properties.custom`.
3. Rename the key in every blueprint's frontmatter, **carrying the value across unchanged**.
4. Report the blueprints touched. Only the key moved.

## Retiring a property

1. **Surface first.** Show the owner every value that would be lost, and ask whether to fold them somewhere or deliberately drop them.
2. Remove the entry from `properties.custom`.
3. Remove the key from every blueprint, once the owner has agreed to let the values go.
4. Report the blueprints touched and anything carried over.

A seed's own defaults — a lifecycle, dates, tags, a grouping — are reshaped or retired the same way. Read the framework's `properties.custom` rather than assuming a set.

Narrowing a property's `options` is retiring values: before a value leaves the list, show the owner every blueprint carrying it and settle where each goes. Widening a list touches no blueprint. Adding `options` to a property that had none is a change to what conforms, so surface every existing value off the new list first.

## Declaring a term

1. **Decide the three** (term, means, not — above) with the owner. Most terms arrive as a collision: two words being used for one thing, or one word for two. Start from the collision, not from a blank definition. If the concept has a blueprint of its own, the entry's `see` points at it, and the blueprint's body carries the full account; the entry stays one line.
2. **Write the entry** under `vocabulary` in `Framework.yaml`: `term`, `means`, `not` as a list, and `see` for the path to the blueprint that defines it in full:

   ```yaml
   - term: Team member
     means: A person with a login on a team, in any role.
     not: ["staff (payroll only)", "teammate (informal, never in a blueprint)"]
   ```
3. **Surface the near-misses already written.** Search the blueprints for each word in the row's Not and list where it appears with the declared term beside it. Don't rewrite them: which uses were the near-miss and which meant something else is the owner's call, and the edit is `eidos`'s.
4. **Report** the entry added and the places that may want the declared term.

## Renaming a term

1. Confirm the new word. If the old one stays in circulation with a different meaning, that is two rows, not a rename.
2. Update `term`. The old word usually belongs in `not`, so the distinction that prompted the rename is kept.
3. Surface every blueprint using the old word, as in declaring; the owner decides which move.
4. Report the entry changed and the places surfaced.

## Retiring a term

1. **Surface first.** Show the owner where the term is used, and ask whether the distinction is being dropped or just the word.
2. Remove the entry. The blueprints keep their text; a word that is no longer declared is just a word.
3. Report the entry removed and the places that used it.

## Refreshing the top-level index

1. **Enumerate the top-level documents** at the root — `README.md` first, then the owner's own one-of-a-kind docs. Frames are collection blueprints, not top-level.
2. **Rebuild the list** under `top_level`: one entry per doc, a `title`, a `path` from `.eidos/` (`../Vision.md`), and a `description`, `README` first. **Keep the owner's existing descriptions**; give a doc with none an empty description and ask. Never invent one.
3. **Report** — the docs indexed and any still needing a description. A top-level doc that's still a stub is **in progress** — note it so the intention to complete it stays visible.

## After

The Framework is a current index and contract for the root. From here, `eidos` reads it to know a blueprint's collection and variants when authoring, and validates each blueprint against the updated Properties table — a custom property now counts among the fields it checks for the collections it applies to, surfaced and added with a note where an applicable blueprint is missing it, never failing the file. A declared term is the word `eidos` writes with, and a near-miss it finds is noted with the declared term beside it, never swapped in silently. `index` rebuilds the `index` key beneath it; and `README.md` is the visible door a human lands at first.
