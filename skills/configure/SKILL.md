---
name: configure
description: >-
  Configure a root's framework — the structure and contract in `_eidos/Framework.md`: its Collections (top-level content folders) and their Flavors (body shapes), its property Schema (the frontmatter contract every blueprint carries), its Vocabulary (the terms the root uses on purpose, each with what it means and what it is not), and its Top-Level document index. Use whenever someone wants to add a kind of content folder ("add a Decisions/ADR folder", "we need a Roles collection"), add or change a body flavor ("add a micro spec template", "make spec.full the default"), add, rename, or retire a custom property and backfill it across blueprints ("add a `team` field to every spec", "every entry should have an owner team"), declare, rename, or retire a term ("a team member is not staff, write that down", "we keep mixing up these two words", "add this to the vocabulary"), snapshot the root as a version, only when asked ("version the specs", "snapshot the blueprints as 2.0", "tag this as a spec version so the client can sign off"), or refresh the Top-Level index ("update the framework index", "the Framework is out of date"). It scaffolds the folders and shape files and reconciles the blueprints. It does not author blueprints (use `eidos`), build a collection's per-blueprint `index.md` (use `index`), or touch the Eidos core properties, which move with the standard's version (use `migrate`).
---

# Eidos Configure

Keep `_eidos/Framework.md` working as the framework's **index and contract** — the authoritative description of the structure everything is written in, with the visible root `README.md` as the friendly door to it. This skill owns the five indexed parts of the Framework body:

- **Top-Level** — the top-level documents, `README.md` first (the visible front door and the first listed entry), then the owner's own one-of-a-kind docs (a Roadmap, a Vision, the generated Blueprint Map), each a link and a one-line description. The framing docs are **not** here — they are a collection.
- **Collections** — each top-level content folder: its grouping (one level of sub-folders) and its **flavors** (body shapes, one marked default), plus a pointer to its generated `index.md` leaf.
- **Schema** — the property contract every blueprint carries, in two blocks: `### Eidos Core` (the standard's, off-limits here) and `### Custom Properties` (the framework's — the seed's defaults plus your own, each scoped by Applies To).
- **Vocabulary** — the term contract: the words the root uses on purpose, one row each (**Term · Means · Not**). Every seed ships it empty; the terms are the root's own, and Eidos declares none of them.
- **Versions** — snapshots of the root, taken on purpose, newest first, one row each (**Version · Commit · Tag**): a named commit in the repository the root lives in, nothing copied. A team's tool for holding the definition against a fixed point; not the product's release version, and not `eidos_version`, which is the standard's and moves with `migrate`. Empty is the normal state.

It scaffolds collections and flavors, grows and reshapes the custom Schema and reconciles blueprints to it, grows the Vocabulary a term at a time, snapshots a version only when asked, and refreshes the Top-Level index. For anything the rules decide — what a collection is, the flavor model, the `flavor` property, what a term is — defer to **EIDOS.md**.

## How you work: press the owner to decide

A collection, flavor, or property nobody thought through reads as meaningful while no one knows what it holds. Don't invent them or guess their shape — facilitate; the owner decides. If they offer only a name, ask for the rest.

- **For a collection:** its **name** (the folder, in the framework's naming convention), a one-line **description**, how it **groups** its blueprints (one level of sub-folders, or flat), at least one **flavor** with a **default**, and how it **draws** on the canvas (below).
- **For a flavor:** its **name** (lowercase, e.g. `full`, `micro`, `api`), a one-line **description**, and its **shape** — the sections the body carries.
- **For a property:** all four —
  - **name** — the frontmatter key. Lowercase, words joined by underscores, matching the core style (`summary`, `connects_to`). Short and stable.
  - **type** — from the Obsidian set: **Text, List, Number, Checkbox, Date, Date & time**. Anything richer — a structured object, an enum with behavior — belongs in the body, not a property. Say so.
  - **applies to** — `all`, or a list of collection names, so a field never lands where it makes no sense. Absence where it applies is a soft gap the validator notes, never refuses.
  - **meaning** — one line: what it holds and why. This is what stops it rotting into a mystery field.
- **For a term:** all three —
  - **term** — the word, as prose uses it. One word or a short phrase; if the owner offers two spellings, that is the first distinction to settle.
  - **means** — one line: what the word denotes in this root.
  - **not** — the near-misses, each with a clause on why it is a different thing. This is where the row earns its place, so press here the way you press on non-goals: "so a *teammate* is not a *team member*?" A term with nothing here is a dictionary entry, and usually not worth declaring yet.

## Boundaries

- **The Framework body only.** You edit its `## Top-Level`, `## Collections`, `### Custom Properties`, `## Vocabulary`, and `## Versions` sections, and create shape files in `_eidos/shapes/`. Not per-blueprint `index.md` files (`index`), not blueprints (`eidos`). In a root whose framework document is `Framework.yaml` (Eidos 4.5.0+), the same declarations are the `top_level`, `collections`, `schema.custom`, `vocabulary`, and `versions` fields, documented in EIDOS.md; edit those, and never the generated `index` key. A framework on a version before 4.6.0 has no Vocabulary; offer `migrate` before adding one.
- **Never touch `### Eidos Core`.** Those move with the standard's version (`migrate`). A core property change is a standards change; redirect.
- **Never touch a tool's.** `_eidos/plugins/<name>/` is that tool's folder, and a column in the Schema table headed with a tool's name (a key named for it, in YAML) is that tool's fields on the row. Carry them across unchanged when you edit a row, never fill them in, and when retiring a row that carries some, name the tool so the owner knows what else is affected.
- **Needs a framework.** Read `_eidos/Framework.md` from the root, found by its `_eidos/` marker. No `_eidos/` means no framework installed — offer `install` first.
- **Read the actor first.** `_eidos/me.md`, and tune how you facilitate to the role.
- **Shapes are the owner's.** A flavor's sections are a content decision. Scaffold a starting point — usually by trimming the collection's default flavor — but let the owner shape it.
- **Don't silently drop values.** Renaming or retiring a property touches real data in real blueprints. Surface what's there before changing it.

## Adding a collection

1. **Decide** the name, description, grouping (sub-folders or flat), at least a default flavor, and the canvas style with the owner.

   The **canvas style** is a real question — ask it. Blueprints read *whole* (loose prose: framing docs, decisions) want `file`; blueprints scanned by their headline want `card from ## <Section>`, naming whichever section of the shape you just agreed carries the summary. Don't assume a section name. Declaring nothing gets a plain whole-blueprint card, which is rarely what anyone wants.
2. **Create the folder** under the root, named in the framework's naming convention (read `naming` from `Framework.md`). Keep its organization to **one level of sub-folders** — deeper is discouraged.
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

   The **Canvas** bullet is the only thing telling a canvas generator how this collection draws — it knows no collection by name.
5. **A grouping property is optional and the collection's own.** Most collections group by sub-folder alone, recorded in the Framework. If the owner wants a property carrying the grouping, that's a Schema change — handle it as a property change below.
6. **Build the leaf and hand off.** Run `index` for the new `index.md`, point the owner to `eidos` for the first blueprint, and report the folder, shape file, and Collections entry.

## Adding a flavor to a collection

1. **Decide** the flavor's name, description, and shape with the owner. A good second flavor is a deliberate variant — a lighter one to grow out of, or a genuine split in kind — never a fork per category label, which EIDOS.md forbids.
2. **Create the shape file** `_eidos/shapes/<kind>.<flavor>.md`. Start from the collection's default flavor and trim or extend it to what the owner wants; keep the section order and names of whatever it shares with the default.
3. **Register it** under the collection in `Framework.md`, in the **Flavors** line with its link. If this flavor should be the default, move the `(default)` marker to it (and only it).
4. **Existing blueprints are untouched** — an absent `flavor` still means the collection's default. Authoring in the new flavor is `eidos`'s job.
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
3. **Backfill the blueprints** in the collections it applies to, with an empty or owner-supplied stub so each is conformant and fillable. Blueprints elsewhere are left alone; new blueprints are generated from the Schema, so only pre-existing ones need this.
4. **Report** the row added and the blueprints touched, flagging which still need a value.

## Renaming a property

1. Confirm the new name (same naming rule). Custom properties only — never `### Eidos Core`.
2. Update the `Name` cell in the Framework's `## Schema`.
3. Rename the key in every blueprint's frontmatter, **carrying the value across unchanged**.
4. Report the blueprints touched. Only the key moved.

## Retiring a property

1. **Surface first.** Show the owner every value that would be lost, and ask whether to fold them somewhere or deliberately drop them.
2. Remove the row from `### Custom Properties`.
3. Remove the key from every blueprint, once the owner has agreed to let the values go.
4. Report the blueprints touched and anything carried over.

A seed's own defaults — a lifecycle, dates, tags, a grouping — are reshaped or retired the same way. Read the framework's `### Custom Properties` rather than assuming a set.

## Declaring a term

1. **Decide the three** (term, means, not — above) with the owner. Most terms arrive as a collision: two words being used for one thing, or one word for two. Start from the collision, not from a blank definition. If the concept has a blueprint of its own, the row's Term cell links to it, and the blueprint's body carries the full account; the row stays one line.
2. **Write the row** into `## Vocabulary`:

   ```markdown
   | Term        | Means                                              | Not                                                            |
   | ----------- | -------------------------------------------------- | -------------------------------------------------------------- |
   | Team member | A person with a login on a team, in any role.      | staff (payroll only), teammate (informal, never in a blueprint) |
   ```

   (Match the existing table's Title Case column headers. In a YAML document it is one `vocabulary` entry: `term`, `means`, `not` as a list, and `see` for the path a Term cell would link to.)
3. **Surface the near-misses already written.** Search the blueprints for each word in the row's Not and list where it appears with the declared term beside it. Don't rewrite them: which uses were the near-miss and which meant something else is the owner's call, and the edit is `eidos`'s.
4. **Report** the row added and the places that may want the declared term.

## Renaming a term

1. Confirm the new word. If the old one stays in circulation with a different meaning, that is two rows, not a rename.
2. Update the Term cell. The old word usually belongs in Not, so the distinction that prompted the rename is kept.
3. Surface every blueprint using the old word, as in declaring; the owner decides which move.
4. Report the row changed and the places surfaced.

## Retiring a term

1. **Surface first.** Show the owner where the term is used, and ask whether the distinction is being dropped or just the word.
2. Remove the row. The blueprints keep their text; a word that is no longer declared is just a word.
3. Report the row removed and the places that used it.

## Recording a version

Only when the owner asks. Never propose a version, never ask whether it is time for one, and never treat an empty `## Versions` as a gap: working alone, most roots never take one. It is for a team that needs a fixed point to hold the definition against later, and the owner knows when that is.

1. **Decide the two** with the owner: the **version**, the root's own number in whatever scheme they keep (semver reads well, since a change of direction is a major); and the **commit**, a sha that already exists in the repository the root lives in, the state being snapshotted. If nothing has been committed since the state they mean, that commit is `HEAD`: show it and have them confirm. Nothing is copied into the root; git holds every blueprint as it was at that commit.
2. **Write the row** at the top of `## Versions`, newest first:

   ```markdown
   | Version | Commit  | Tag              |
   | ------- | ------- | ---------------- |
   | 2.0.0   | 9f3c1e2 | blueprints/2.0.0 |
   ```

   (In a YAML document it is one `versions` entry: `version`, `commit`, and `tag` when there is one.)
3. **Ask about the tag.** One question: tag it? The name is `blueprints/<version>`, its own namespace so it never collides with the product's release tags and never names the tool. On a yes, `git tag blueprints/<version> <commit>` on the snapshot commit, and fill the Tag cell; on a no, leave the cell empty. Never create a tag on any other answer.
4. **Say what it means.** The commit that adds this row comes after the one it names, so the row is not in the snapshot it records; that is how a tag works too. The blueprints as they stand at that sha are the root at that version, and a blueprint never carries a version of its own.
5. **Report** the row added, and whether it was tagged.

## Refreshing the Top-Level index

1. **Enumerate the top-level documents** at the root — `README.md` first, then the owner's own one-of-a-kind docs. Frames are collection blueprints, not top-level.
2. **Rebuild the list** under `## Top-Level`, after the `<!-- configure: top-level index (regenerated) -->` marker: one bullet per doc, `- [Title](../Title.md) — one-line description`, `README` first. **Keep the owner's existing descriptions**; give a doc with none a `<!-- TODO: describe -->` and ask. Never invent one.
3. **Report** — the docs indexed and any still needing a description. A top-level doc that's still a stub is **in progress** — note it so the intention to complete it stays visible.

## After

The Framework is a current index and contract for the root. From here, `eidos` reads it to know a blueprint's collection and flavors when authoring, and validates each blueprint against the updated Schema — a custom property now counts among the fields it checks for the collections it applies to, surfaced and added with a note where an applicable blueprint is missing it, never failing the file. A declared term is the word `eidos` writes with, and a near-miss it finds is noted with the declared term beside it, never swapped in silently. `index` rebuilds each collection's `index.md` (the per-blueprint leaf) beneath it; and `README.md` is the visible door a human lands at first.
