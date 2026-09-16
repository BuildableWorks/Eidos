# Eidos

**Version:** 4.7.0

A markdown standard for defining a product: an app, a book, a study, a workflow, anything work produces that has a shape. One file is the complete source of truth for one unit of it, independent of time or status: as true of something planned as of something long finished.

This file is the contract: the terms, the layout, and the rules. It names no collection, no shape, and no section — those belong to a framework, not to the standard. For worked frameworks see [`seeds/`](seeds). Doing the work takes a person, this contract, and the [skills](#for-an-agent).

## Vocabulary

Every term the standard uses, in the order they build on each other.

| Term | What it is |
| --- | --- |
| **product** | What a root defines: an app, a book, a study, a workflow, anything work produces that has a shape. Every blueprint describes one unit of it; every frame describes it whole. |
| **root** | The one folder Eidos lives in, holding the framework, the collections, and any top-level docs. Found by the hidden `_eidos/` inside it, never by its name. |
| **framework** | The *structure* a root is written in — its collections, shapes, flavors, roles, naming convention, Schema, and Vocabulary. Lives in the root's hidden `_eidos/`. Portable: the same framework governs any number of roots. |
| **collection** | A top-level folder of repeated blueprints that share a body shape. A framework declares each one, and may group a collection's blueprints in one level of sub-folders. |
| **blueprint** | One markdown file in a collection, defining one unit completely. Frontmatter (a contract) plus a body (a shape). |
| **frame** | A blueprint describing the whole product rather than one unit of it. Frames set what every other blueprint is judged against, and are revised whenever that judgment changes. Every framework declares a framing collection. |
| **shape** | One body template: the sections a blueprint carries, in order, under set names, each with its guidance. Body only; frontmatter is generated. One file per shape, in `_eidos/shapes/`. |
| **flavor** | A collection's shapes are variants of one family, and each variant is a flavor (`<kind>.<flavor>`). A collection declares one or more and marks one default — typically a light flavor a blueprint can grow out of, beside a fuller one. |
| **property** | One frontmatter field: a name, a type, which collections it applies to, and a meaning. |
| **Schema** | The framework's whole property contract: the core properties Eidos requires, plus whatever the framework adds. |
| **term** | One word the root uses on purpose: what it means, and what it is not. Declared so a distinction made once is not lost later. |
| **Vocabulary** | The framework's whole term contract, beside its Schema. Eidos declares none of a framework's terms; this table is its own. |
| **top-level doc** | A one-of-a-kind document at the root — a Roadmap, a Vision, a map a tool generates. Free-form: no shape, no flavors, no validation. |
| **role** | A response contract for one kind of person, saying how an agent talks to them. |
| **actor** | Who is in the seat right now: their role, plus a personal calibration. |
| **seed** | A starting framework the standard ships. `install` copies one into a new root. |
| **version** | A snapshot of the root, taken on purpose: a named commit, and a tag if wanted, so a team can hold the definition against a fixed point later. Not the product's release version. Unused until the owner asks for one. |
| **plugin** | A tool's own folder inside the framework, `_eidos/plugins/<name>/`, holding whatever that tool keeps there. The standard reads none of it. |

A blueprint captures **state and intent, not work**. A task describes work and dies when the work ships; a blueprint describes the product and stays accurate across its whole life — drafted, built, deprecated.

## Layout

The root is found by the hidden `_eidos/` inside it. It may be named anything; nothing points at it by path.

```txt
Blueprints/              # the root — `Blueprints` is only the default name
  README.md              # the visible "start here"
  _eidos/                # the framework (below)
  <Framing>/             # the framing collection — declared first
    index.md             #   generated leaf (a markdown framework; a YAML one keeps it inside the document)
    <Frame>.md           #   one per kind of frame, flat
  <Collection>/          # a collection of blueprints; declare as many as the work needs
    index.md             #   generated leaf, likewise
    <Group>/             #   one level of sub-folders, at most
      <Title>.md         #     one blueprint per file
  roadmap.md             # a top-level doc — optional, yours
```

Several roots in one repository nest as `Blueprints/<name>/…`, each with its own `_eidos/`.

## The framework (`_eidos/`)

Hidden the way `.git` and `.obsidian` are: present, manageable, out of the way once set. The root is plausibly an Obsidian vault, and `_eidos/` sits beside `.obsidian/`. Open the way `.obsidian/` is, too: the standard names its own entries, and a tool that keeps something in the framework gets a folder of its own under `plugins/`.

```txt
_eidos/
  shapes/                  # one file per flavor
    <kind>.<flavor-1>.md   #   a collection's default flavor
    <kind>.<flavor-2>.md   #   a second flavor of the same kind
    frame.<kind>.md        #   the framing collection's flavors, one per kind of frame
  roles/                   # response contracts, committed and team-tunable
    framework-owner.md     #   the one every seed carries
    <role>.md              #   the rest are the framework's own
  Framework.md             # the framework document, for people: version, naming, Top-Level, Collections, Schema, Vocabulary, Versions
                           #   (or Framework.yaml, the same as data with the index inside it, for scripts and agents)
  plugins/                 # whatever tools keep in the framework, one folder each
    <name>/                #   a tool's own; the standard reads none of it
  me.md                    # the actor (personal, gitignored)
  .gitignore               # ignores me.md, and any personal file a plugin names
```

The skills read the framework from the root they are working in, never from a copy of their own. A folder with no `_eidos/` is not a root.

### Plugins

The top level of `_eidos/` is the standard's: the entries above, and whatever a later version adds. Everything else lives under `_eidos/plugins/`, one folder per tool, named for the tool: a CLI's cache, an editor extension's settings, a generator's templates, a script's state. What goes inside is the tool's own, and the standard neither reads nor validates it; a check never faults a folder there, `migrate` carries it across untouched, and `install` seeds none. A plugin folder is committed with the rest of the framework; a tool that keeps personal state names those files, and they go in `_eidos/.gitignore` beside `me.md`.

A tool touches only the folder it owns. The framework document, the shapes, and the roles are the owner's, edited through the skills or by hand; a plugin that needs the framework to know something declares it in its own folder, not in theirs.

### `Framework.md`

The framework document: the one file describing the structure rather than any single blueprint. It has two forms, the same fields in each, and a root keeps exactly one. This is the markdown form, for people: frontmatter for the facts tooling parses and a body indexing what it governs, readable in a vault and edited in place. The other is [`Framework.yaml`](#frameworkyaml), for scripts and agents.

```markdown
---
eidos_version: 4.7.0
naming: kebab-case
---

# Framework

## Top-Level
<!-- configure: top-level index (regenerated) -->
- [README](../README.md) — the front door.

## Collections

### <Framing collection>

The framing docs — declared first.

- **Leaf:** [<Framing>/index.md](../<Framing>/index.md)
- **Flavors:**
  - [<kind>](shapes/frame.<kind>.md) — one flavor per kind of frame (mark one default).

### <Collection>

One line on what this collection holds.

- **Leaf:** [<Collection>/index.md](../<Collection>/index.md)
- **Flavors:**
  - [<flavor-1>](shapes/<kind>.<flavor-1>.md) — the fuller shape (default).
  - [<flavor-2>](shapes/<kind>.<flavor-2>.md) — a lighter one to grow out of.
- **<Grouping>:**
  - **<Group>** — one line on what falls under it.

## Schema

### Eidos Core
<!-- the standard's block: id, title, summary, flavor -->

### Custom Properties
| Name   | Type | Applies To   | Meaning                        | <tool>           |
| ------ | ---- | ------------ | ------------------------------ | ---------------- |
| <name> | Text | all          | Whatever this framework needs. |                  |
| <name> | Text | <Collection> | Scoped to one collection.      | <field>: <value> |

### <tool> Properties
| Name   | Type | Applies To | Meaning                          |
| ------ | ---- | ---------- | -------------------------------- |
| <name> | Text | all        | A property the tool keeps itself. |

## Vocabulary

| Term   | Means                                  | Not                                          |
| ------ | -------------------------------------- | -------------------------------------------- |
| <Term> | One line: what the word denotes here.  | <near-miss>, and why it is a different thing. |
| [<Term>](../<Collection>/<Group>/<Title>.md) | A term its blueprint defines in full. | <near-miss> |

## Versions

| Version   | Commit | Tag   |
| --------- | ------ | ----- |
| <version> | <sha>  | <tag> |
```

- **`eidos_version`** — the version this framework targets. `migrate` reads and bumps it.
- **`naming`** — `kebab-case` (default), `TitleCase`, or `Title Case`. See [Naming](#naming).
- **`## Top-Level`** — the top-level docs, `README` first. Framing docs are not here; they are a collection.
- **`## Collections`** — one `###` each: its **Leaf**, its **Flavors** (default marked), and its grouping.
- **`## Schema`** — one block per owner: `### Eidos Core` (the standard's, rewritten by `migrate`), `### Custom Properties` (the framework's, edited by `configure`), and `### <tool> Properties` for each tool that declares properties of its own (that tool's, written by nobody else). The first four columns are the standard's; any column past them is a tool's, headed with the tool's name.
- **`## Vocabulary`** — the root's own terms, one row each: **Term · Means · Not**. Starts empty; absent means none declared.
- **`## Versions`** — snapshots of the root, taken on purpose, newest first, one row each: **Version · Commit · Tag**. A named commit, nothing copied. Starts empty and stays empty until the owner asks for one; absent means none recorded.

### `Framework.yaml`

The framework document may be data instead of markdown: `Framework.yaml` (or `.yml`) in place of `Framework.md`. It is the same framework, field for field, in the snake_case the frontmatter already uses, with comments wherever the owner wants them. Choose it when scripts and agents are the main readers: it parses without a markdown convention, and it carries the one thing the markdown form keeps elsewhere, the generated index, under `index` (see [Generated leaves](#generated-leaves)), so a YAML root is one document with everything in it. Choose markdown when people are: it renders in a vault and reads as prose. The markdown form's prose has no field to land in and stays behind when a root converts.

```yaml
eidos_version: 4.7.0
naming: kebab-case            # absent = kebab-case
top_level:                    # the top-level docs, README first
  - title: README
    path: ../README.md
    description: the front door.
collections:                  # the first is the framing collection
  - name: <Framing>
    description: The framing docs.
    flavors:
      - name: <kind>
        shape: shapes/frame.<kind>.md
        description: one flavor per kind of frame
        default: true
  - name: <Collection>
    description: One line on what this collection holds.
    flavors:
      - { name: <flavor-1>, shape: shapes/<kind>.<flavor-1>.md, description: the fuller shape, default: true }
      - { name: <flavor-2>, shape: shapes/<kind>.<flavor-2>.md, description: a lighter one to grow out of }
    grouping:
      label: <Grouping>
      property: <name>          # the custom property carrying the group, if one does
      groups:
        - { name: <Group>, description: one line on what falls under it }
schema:
  core: []                    # absent = the standard's core for this eidos_version
  custom:
    - { name: <name>, type: Text, applies_to: all, meaning: Whatever this framework needs. }
    - { name: <name>, type: Text, applies_to: [<Collection>], meaning: Scoped to one collection., <tool>: { <field>: <value> } }
  tools:                      # one block per tool that declares properties of its own; absent = none
    <tool>:
      - { name: <name>, type: Text, applies_to: all, meaning: A property the tool keeps itself. }
vocabulary:                   # the root's own terms; absent = none declared
  - { term: <Term>, means: One line on what the word denotes here., not: ["<near-miss>, and why it is a different thing"] }
  - { term: <Term>, means: A term its blueprint defines in full., not: [<near-miss>], see: ../<Collection>/<Group>/<Title>.md }
versions:                     # snapshots of the root, taken on purpose, newest first; absent = none recorded
  - { version: <version>, commit: <sha>, tag: <tag> }
index:                        # generated, regenerated wholesale by `index`; never hand-edited
  <Collection>:
    - { id: <id>, title: <Title>, summary: <the summary>, path: <Group>/<Title>.md, group: <Group> }
```

- Every path is relative to `_eidos/`, as the markdown form's links are. An index entry's `path` is relative to its collection folder, as an `index.md` link is.
- `default` marks a collection's default flavor; absent on all of them, the first is. `applies_to` is `all` or a list of collections. A key on a property entry that is not one of the standard's four is a tool's, named for the tool. `schema.tools.<tool>` is that tool's own block, the markdown form's `### <tool> Properties`. There is no **Leaf**: a structured root's index is inside the document.
- `vocabulary` is the markdown form's `## Vocabulary` table, one entry per term: `term`, `means`, and `not` as a list, each entry free to carry its clause. `see` is the path a markdown Term cell would link to, for a term its blueprint defines in full. Absent means no terms declared.
- `versions` is the markdown form's `## Versions` table, one entry per snapshot: `version`, `commit`, and `tag` when one was made. Absent means none recorded, which is the normal state.
- A tool reads whichever document is present and treats the framework the same. Converting a markdown root means writing the same fields as data, removing `Framework.md` and each collection's `index.md`, and regenerating the index.

### Shapes and flavors

A shape is body-only: sections in their order, under set names, with their guidance. Every blueprint in a collection follows one of that collection's declared flavors, and a check validates against the flavor the blueprint names. Shape files are `<kind>.<flavor>.md`, lowercase and dotted. Top-level docs have no shape.

The default flavor is what gets scaffolded; a blueprint on another records it in `flavor`. A blueprint on a lighter flavor is never faulted for the sections only a fuller one carries.

### Schema

Each property is a row: **Name · Type · Applies To · Meaning**. A type comes from the set Obsidian uses — **Text, List, Number, Checkbox, Date, Date & time** — so frontmatter renders natively in a vault. Anything wanting more structure than one of those belongs in the body.

**Applies To** scopes a property to collections: `all`, or a list. Frontmatter is generated per blueprint from the properties that apply to its collection, so a scoped property never lands where it makes no sense.

**Every property has an owner, and the owner is the block it sits in.** Eidos is the first tool: `### Eidos Core` is its block, and `migrate` rewrites it. `### Custom Properties` is the framework owner's, and `configure` edits it. A tool that needs properties of its own (the `eidos` CLI, an editor extension, a generator) declares them in a block of its own, `### <tool> Properties` (`schema.tools.<tool>` in YAML), and that tool alone writes it: not `configure`, not `migrate`, not another tool. A tool's properties are Schema properties like any other, generated into frontmatter where they apply, validated by a check, and bound by every rule here including the one against work-tracking; an unknown tool's block is never faulted. When a tool leaves, its block leaves with it, the values it held surfaced first the way any retired property's are.

**A row may also carry a tool's fields.** The four the standard names come first and mean what they mean here. Past them, a tool that needs something per property it does *not* own (how an editor renders `status`, what a checker allows, an option list) adds its own under its own name: a key named for the tool on the YAML entry, a column headed with the tool's name in the markdown table. The standard reads its four and ignores the rest; a check never faults them, and `configure` and `migrate` carry them across unchanged and never fill them in.

**The core** — present on every blueprint, and the whole of what the standard requires:

| Name | Type | Meaning |
| --- | --- | --- |
| `id` | Text | Stable, unique identity, in any form: a slug, a number, a GUID. Assigned once, never changed. References point at it. |
| `title` | Text | Human-readable name. Rename it freely; `id` is what holds still. |
| `summary` | Text | One plain line: what this blueprint is. The source for the collection's [`index.md`](#generated-leaves) listing; absent, the index flags it. |
| `flavor` | Text | Which flavor this blueprint follows. Absent = the collection's default. |

**Eidos defines no custom properties.** A lifecycle `status`, dates, a grouping, a dependency list, a relationship list — all are a framework's own choice, and how blueprints relate is better said in the body, as links in prose, than as a frontmatter field. Each [seed](seeds) makes its own set. Add one with `configure`, which presses for all four of Name, Type, Applies To, and Meaning, then backfills the blueprints it applies to.

### Vocabulary

The Schema's sibling: where the Schema is the contract for properties, the Vocabulary is the contract for words. Each term is a row: **Term · Means · Not**. **Term** is the word as prose uses it, or a link to the blueprint that defines the concept in full. **Means** is one line. **Not** is the near-misses, each with a clause on why it is a different thing, and it is where a row earns its place: a term with no Not is a dictionary entry, and a term that needs a body of its own is a blueprint, linked from its row.

Three layers of words meet in a root, and each is declared where it lives. The standard's terms are the table at the top of this file. A framework's structural names (its collections, flavors, groups) are declared where the structure is. The root's own terms, the words the product itself is described in, are the framework's Vocabulary. **Eidos declares none of the last.** A Vocabulary starts empty and grows a row when a word begins to carry a distinction worth keeping, with `configure`, which presses for all three of Term, Means, and Not.

A declared term is the word (Rule 20). An agent authoring or checking a blueprint uses it, and where a near-miss appears says which term the Vocabulary would have, as a suggestion. This is distinct from what a role sets: a role is register, how deep an agent goes and what it surfaces for one kind of reader; the Vocabulary is meaning, what a word denotes for every reader.

### Versions

The root can be versioned, separately from the product it defines. A version is a snapshot taken on purpose: a fixed point a team can hold the definition against later, when the product has gone a different direction, a stakeholder wants to iterate from what was agreed, or a freelancer hands over what was signed off. It is a tool for seeing shifts across people, and it is unused until someone asks for it: working alone, you will likely never take one, because git history is enough. No skill asks whether to version, no check faults a root that never has, and the section stays empty until the owner says otherwise.

`## Versions` is a table, newest first, one row per snapshot: **Version · Commit · Tag**. **Version** is the root's own number, in whatever scheme the owner keeps (semver reads well, since a change of direction is a major). It is not the product's release version, which has its own numbering and its own tags; the two move on separate lines. **Commit** is the sha of a commit in the repository the root lives in, full or abbreviated so long as it stays unique there. That commit is the snapshot: git already holds every blueprint as it was then, `git show <commit>:<path>` reads one, and nothing is copied into the root. **Tag** is optional. When one is wanted, name it **`blueprints/<version>`** (`blueprints/2.0.0`): its own namespace, so it never collides with the product's release tags (`v2.0.0`), and it names the blueprints rather than the tool.

A version is a fact about the whole root, never a property on a blueprint (Rule 15): a blueprint stays timeless, and a snapshot says which commit. It is not the Eidos version either, which is `eidos_version` in the same document and moves with the standard.

Taking one is two steps, in this order, the way a tag follows the commit it marks: the commit that is the snapshot exists first; then the row, and the tag if wanted, point at it, and the row's own commit comes after. `configure` does this when asked, and asks about the tag; it never asks about the version.

### Roles and the actor

Not everyone who works on the same root plays the same part — one holds the intent, another builds or drafts from it, another reviews it, another answers for it. The agent responds to each differently, from two files:

- **`_eidos/roles/<role>.md`** — one response contract per role: vocabulary and technical depth, what to surface versus fold away, and who holds which decisions. Which roles exist is the framework's call; each [seed](seeds) ships a set written against its own collections. Committed and team-tunable.
- **`_eidos/me.md`** — personal and gitignored, one per person. Names the actor's role and calibrates it on three axes: **ownership**, **experience with the scope**, and **technical capacity**. Set it with `whoami`. Blank is fine.

One role is common to every seed: the **Framework Owner**, who holds the intent, the scope, and the decisions. The rest of the cast depends on the work.

## Writing

### `README.md`

A visible front door at the root: what the product is, and pointers into it — the top-level docs, the collections and their indexes, and the framework document for the full index. Thin, orientation and links, edited in place.

### Naming

Everything a human reads in the tree — top-level docs, collection and sub-folders, blueprint files — follows the framework's `naming` convention.

| Convention | A blueprint file | A grouping folder | For |
| --- | --- | --- | --- |
| **kebab-case** (default) | `blueprint-title-here.md` | `group-name/` | readable everywhere: no escaping, no `%20` |
| **TitleCase** | `BlueprintTitleHere.md` | `GroupName/` | space-free, capitalized |
| **Title Case** | `Blueprint Title Here.md` | `Group Name/` | a tree that reads like prose, at the cost of `%20` in every link |

An absent `naming` key means `kebab-case`.

One convention governs the whole folder, and changing it later means renaming files, so it is settled at init. Whichever you pick: `_eidos/` is always lowercase; `README.md` keeps the name every tool already looks for; a grouping property's value matches its folder exactly; and fields meant for tools are not names in the tree.

### Linking

Point at another blueprint, doc, or section with a standard markdown link: the text is the human title, the path is the target's filename in the framework's convention (only a Title Case tree carries `%20`). Add a `#heading` anchor for a section. Properties that point outward hold links too, not bare ids — quote them in YAML, since a leading `[` starts a list:

```yaml
depends_on:
  - "[Some Blueprint](../some-group/some-blueprint.md)"
```

If a target has no blueprint yet, name it plainly rather than fabricating a link.

### Blueprint bodies

The body follows its flavor's shape. Keep the shape's order and names; leave a section out when it genuinely doesn't apply rather than leaving it empty. Within and beneath those sections, write it like a person would read it — sub-headings, tables, lists, small diagrams wherever they make the meaning clearer. Keep checkable statements short and observable, labeled the way the shape asks, with supporting detail pushed into a table or sub-section they point at.

The sections themselves are documented in the shape file, not here.

### Frames and top-level docs

Both are loose prose: record what is true now, revise when it changes. They differ in one way. A **frame** is a blueprint — it follows a shape, carries the frontmatter contract, and is validated. A **top-level doc** is one-of-a-kind, filled in once and edited in place, so it needs no shared shape and gets none. A shape earns its keep by being stamped again; a document written once doesn't need a cookie-cutter.

For a top-level doc you've already drafted, `format` organizes it into the house style without adding anything of its own.

## Generated leaves

One derived view the standard defines, regenerated wholesale, annotating rather than gating, with nothing hand-written to preserve.

**The index.** Each collection carries a generated `index.md` in its folder, listing its blueprints — grouped under their sub-folders when it has them, flat when it doesn't. Each line is the blueprint's `summary`, verbatim; a blueprint with none is flagged, never invented. Links are relative to the collection folder. Rebuilt by `index`.

In a root whose framework document is YAML there are no `index.md` files: every collection's index lives inside the framework document under `index`, one list per collection, each entry the blueprint's `id`, `title`, `summary` (null when absent, never invented), `path` relative to the collection folder, and `group` when it has one, in the order the markdown index would list them. The same `index` rebuilds it wholesale, rewriting that key and nothing else in the document.

```markdown
# <Collection>

<!-- index: <Collection> (regenerated) -->

## <Group>
- [<Title>](<Group>/<Title>.md) — the blueprint's one-line `summary`, verbatim.
- [<Title>](<Group>/<Title>.md) — one bullet per blueprint, in file order.
```

**Any other view is a tool's.** A map, a graph, a report: a tool that draws one reads the leaves and the links in the bodies, keeps whatever it needs in its own Schema block or its `plugins/` folder, and writes its output as a top-level doc, registered in `## Top-Level` like any other. The standard declares nothing for it.

## Rules

The load-bearing conventions.

1. **The frontmatter is the agreement; the body is guidance.** Properties are checked against the framework's Schema. Body sections are recommended structure, not requirements.
2. **The root owns its framework.** Shapes and properties live in the root's `_eidos/`. A skill reads the framework from the root it is working in, not from a copy of its own. Anything a tool keeps there lives under `_eidos/plugins/<name>/`, and a tool touches only the folder it owns.
3. **Validation is framework-defined.** A check reads *that framework's* Schema and enforces it — the core properties plus the custom ones scoped to the blueprint's collection. The contract is the Schema, not a rule hardcoded in a tool.
4. **Portability over prescription.** A missing core property is surfaced and added with a note on why; a missing section is noted and offered. Never refuse the file.
5. **Write it like a human would read it.** The sections are a scaffold for a living blueprint, not a form to pour text into. If a blueprint reads like filled-in boilerplate, reshape it until it reads like someone wrote it.
6. **Reference other blueprints with links, not bare names** — in prose and in properties alike. Each blueprint's `id` is still its permanent identity, sitting behind the link.
7. **One shape family per collection, declared as flavors.** What flexes is *which* sections appear and *which* flavor a blueprint uses; never their order or names within a flavor. The shape is never forked per category.
8. **Properties carry a type, a meaning, and an owner.** Every property declares its name, its type, which collections it applies to, and what it means; the block it sits in says who owns it (Eidos, the framework, or a tool), and only the owner writes there. Frontmatter is generated from the Schema, so a new blueprint is born conforming.
9. **Soft labels are views, not structure.** A category label a framework adds drives views and filtering, never structure. An off-list value is valid. `flavor` carries the structural choice.
10. **A collection's grouping is the collection's own.** It may group its blueprints one level deep and may declare a property naming that grouping; the value then matches the folder, and an unknown value warns rather than blocks. The standard never names a grouping for it.
11. **A shape names its own stable part.** Every shape has a part that holds still and a part that moves, and says which is which. If the stable part changes substantially, ask whether this is a different blueprint.
12. **Non-goals carry the most weight.** Where a shape declares a section for what a blueprint deliberately will *not* do, that section is its strongest — it is where scope management actually happens. Still not a hard gate.
13. **A shape documents its own conventions.** Section names, their order and meaning, and any labeling a shape asks for live in the shape file. This standard governs collections, shapes, flavors, and properties; it never governs a section.
14. **No work-tracking fields.** No `sprint`, `estimate`, or `assignee` — the moment you add them, a blueprint becomes a task and rots. Bridge to a tracker with a link. The same holds in the body: a section describing how you mean to build a product captures intent, never how far along it is.
15. **The Eidos version is a framework fact, and so is the root's.** The standard's version lives in the framework document as `eidos_version`; the root's own versions, snapshots taken on purpose, live there too under `## Versions`, each a named commit. Neither is ever a per-blueprint property. Git holds the history; a framework that wants date properties declares them like any other.
16. **Loose prose is revised in place.** A top-level doc, and any collection a framework marks as loose prose, records what is true now and is expected to change. That is revision, not work status.
17. **The human authors; the agent facilitates.** Intent, scope, and decisions stay with the person. An agent formats, supplements, asks, and holds scope; it does not generate finished blueprints or set direction. A blueprint the owner did not think through is worse than none.
18. **Read the actor before acting.** Read `_eidos/me.md` and the matching contract in `_eidos/roles/`, and respond as that role defines. The human-first principle holds for every role; only the mode changes. A blank or absent file defaults to full facilitation.
19. **Every framework declares a framing collection.** Its name, its flavors, and how many it carries are the framework's own — a framework needs framing, not a particular set of frames. Required as a **declaration**: a framework that declares none is incomplete and a check says so. Never a gate: a declared frame left unwritten is a gap to surface, not a failure.
20. **A declared term is the word.** Where the framework's Vocabulary declares a term, blueprints use it, and a near-miss it names is flagged with the declared term beside it, never refused and never swapped in silently. The standard declares no term of a framework's; a Vocabulary starts empty and grows a row at a time, each saying what the word means and what it is not.

## Versioning

Semantic Versioning: major for breaking changes, minor for backward-compatible additions, patch for clarifications.

This file holds the version of **the standard** — right now, **4.7.0** — and it moves only when the text of this file moves. A framework records the version it targets as `eidos_version` in its framework document; `migrate` reads and bumps it there. At tag time this file is copied as-is into `versions/` under its full semver name, so any two releases, even non-adjacent, can be diffed to migrate between them. Worked hops are in `versions/MIGRATIONS.md`. Tools may reject an unsupported version.

**The plugin that ships this standard versions separately.** The skills and seeds change far more often than the standard does, so a release that fixes a skill bumps the plugin and leaves this file — and every framework's `eidos_version` — untouched. When you need to know what a framework conforms to, read this version; the plugin's is in `.claude-plugin/plugin.json`, and `CHANGELOG.md` records which standard each plugin release carried.

## For an agent

_Operating detail. A human can stop above._

**Prefer the tooling.** The `eidos` command does the mechanical part: `init` scaffolds a root, `new` generates a conforming blueprint, `check` validates, `index` rebuilds the indexes, and `eidos instructions` prints the workflow. The skills carry the judgment: `eidos` authors and validates with the owner, `iterate` questions a rough idea into shape before any of that, `format` reshapes a draft already written, `install` scaffolds, `configure` adds a collection, flavor, property, or term, records a version, and keeps the framework current, `index` rebuilds a collection's leaf, `whoami` sets the actor, `migrate` upgrades versions.

**Find the framework in the root.** Locate the root by its `_eidos/` marker, not its name. Every operation reads that `_eidos/`. If a folder has none, offer `install`. Check the framework's `eidos_version` against the standard you carry once per session: a gap is worth one line and an offer of `migrate`, never a block, and the framework in front of you is the operative contract either way. Never fall back to a hardcoded contract, and never assume a collection or section name — read what the framework declares. Leave `_eidos/plugins/` alone unless you are the tool that owns a folder in it; a folder you don't recognize there is not a problem to report.

**Read the actor first.** `_eidos/me.md`, then the role file it names. Respond as that file defines the role — read it, don't infer from its filename. A framework defines its own cast.

**Speak the root's terms.** The framework's Vocabulary says which word is the word and what it is not. Use the declared term in what you write; where the owner's draft or speech uses a near-miss, say which term the Vocabulary declares and ask, rather than substituting silently. A word the owner keeps using that no row declares is worth naming as a candidate; declaring it is `configure`'s job, and the owner's call.

**Navigate by the leaves.** `README.md` for orientation, the framework document (`_eidos/Framework.md` or `.yaml`) for the full index, each collection's `index.md` for its blueprints (or the document's `index`, in a YAML root). Read these instead of scraping the tree; regenerate them when stale.

**Version only when asked.** `## Versions` is for a team snapshotting the root on purpose. Never propose one, never ask whether to take one, and never fault a root without any; an empty section is the normal state. When the owner asks, write the row from a commit that exists and ask whether to tag it `blueprints/<version>`; create the tag on a yes and not otherwise. To see the root as it was at a version, read the blueprint at that commit (`git show <commit>:<path>`), never a copy kept in the root.

**Authoring a blueprint:**

1. From the framework document, take the Schema, the Vocabulary, the naming convention, and the target collection's flavors. Pick a flavor (the default unless the owner chooses another) and read its shape for the body. Name the file for its title in the convention; put a permanent `id` inside, in whatever form the root uses.
2. Generate frontmatter from the properties that apply to that collection. Fill values from what the owner tells you; leave a property blank rather than guessing it.
3. Lead with the shape's opening sections and press hardest on its non-goals section. Read those names off the shape rather than assuming them, and follow whatever labeling it asks for. Omit a section that doesn't apply; keep the order and names of the ones that do.
4. Where the owner is vague, ask. Don't fill the gap with plausible prose.

**Validating a blueprint:** check frontmatter against the framework's Schema, every block of it (`id` present and unique, dates as `YYYY-MM-DD`, custom and tool properties scoped to the collection). Report missing body sections against *the blueprint's flavor shape*, flagging an absent non-goals section first, and note anything skipping the labeling that shape asks for. Note each near-miss the Vocabulary names, with the declared term beside it. Confirm no work-tracking fields crept in. Surface, don't block — the output is a review a human acts on.

**Facilitate, don't author.** Format and structure what the owner gives you, supplement, ask, and press on scope. Never invent a blueprint's purpose, decide direction, or hand back a finished blueprint to rubber-stamp. When unsure, ask.
