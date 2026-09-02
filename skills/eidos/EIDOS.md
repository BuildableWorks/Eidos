# Eidos

**Version:** 4.4.0

A markdown standard for defining the essence of a thing — a product, a body of work, anything you set out to make. One file is the complete source of truth for one unit of it, independent of time or status: as true of something planned as of something long finished.

This file is the contract: the terms, the structures, and the rules. It names no collection, no shape, and no section — those belong to a framework, not to the standard. For worked frameworks see [`seeds/`](seeds); for filled-in definitions see [`examples/`](examples). Doing the work takes a person, this contract, and the [skills](#for-an-agent).

## Vocabulary

Every term the standard uses, in the order they build on each other.

| Term | What it is |
| --- | --- |
| **definition** | The whole thing being defined: one folder, holding collections of items and any top-level docs. What a team writes. |
| **framework** | The *form* a definition is written in — its collections, shapes, flavors, personas, naming convention, and Schema. Lives in the definition's hidden `_eidos/`. Portable: one framework, many definitions. |
| **collection** | A top-level folder of repeated items that share a body shape. A framework declares each one, and may group a collection's items in one level of sub-folders. |
| **item** | One markdown file in a collection, defining one unit completely. Frontmatter (a contract) plus a body (a shape). |
| **frame** | An item in the **framing collection** — the loose, point-in-time documents saying what the whole definition is, against which every other item is judged. Every framework declares a framing collection. |
| **shape** | The body template a collection's items follow: sections, in order, under set names, each with its guidance. Body only; frontmatter is generated. |
| **flavor** | One of a collection's shapes. A collection has one shape *family* with one or more flavors, one marked default — a light flavor an item can grow out of, or a deliberate variant. |
| **property** | One frontmatter field: a name, a type, which collections it applies to, and a meaning. |
| **Schema** | The framework's whole property contract: the core properties Eidos requires, plus whatever the framework adds. |
| **top-level doc** | A one-of-a-kind document at the definition root — a Roadmap, a Vision, the generated canvas. Free-form: no shape, no flavors, no validation. |
| **persona** | A response contract for one role, saying how an agent talks to that kind of person. |
| **actor** | Who is in the seat right now: their persona, plus a personal calibration. |
| **seed** | A starting framework the standard ships. `install` copies one into a new definition. |

An item captures **state and intent, not work**. A task describes work and dies when the work ships; an item describes the thing and stays accurate across its whole life — drafted, built, deprecated.

## Layout

A definition is one folder, found by the hidden `_eidos/` inside it. The root may be named anything; nothing points at it by path.

```txt
Blueprint/               # the definition root — `Blueprint` is only the default name
  README.md              # the visible "start here"
  _eidos/                # the framework (below)
  <Framing>/             # the framing collection — declared first
    index.md             #   generated leaf
    <Frame>.md           #   one per kind of frame, flat
  <Collection>/          # a collection of items; declare as many as the work needs
    index.md             #   generated leaf
    <Group>/             #   one level of sub-folders, at most
      <Title>.md         #     one item per file
  roadmap.md             # a top-level doc — optional, yours
```

Several definitions in one repository nest as `Blueprint/<name>/…`, each with its own `_eidos/`.

## The framework (`_eidos/`)

Hidden the way `.git` and `.obsidian` are: present, manageable, out of the way once set. A definition is plausibly an Obsidian vault, and `_eidos/` sits beside `.obsidian/`.

```txt
_eidos/
  shapes/                  # one file per flavor
    <kind>.<flavor-1>.md   #   a collection's default flavor
    <kind>.<flavor-2>.md   #   a second flavor of the same kind
    frame.<kind>.md        #   the framing collection's flavors, one per kind of frame
  personas/                # response contracts, committed and team-tunable
    framework-owner.md     #   the one every seed carries
    <role>.md              #   the rest are the framework's own
  Framework.md             # index + config: version, naming, Top-Level, Collections, Schema
  user.md                  # the actor (personal, gitignored)
  .gitignore               # ignores user.md — the one file here not committed
```

The skills read the framework from the definition, never from a copy of their own. A folder with no `_eidos/` is not an Eidos definition.

### `Framework.md`

The one file describing the form rather than any single item: frontmatter for the facts tooling parses, and a body indexing the definition.

```markdown
---
eidos_version: 4.4.0
naming: kebab-case
---

# Framework

## Top-Level
<!-- configure: top-level index (regenerated) -->
- [README](../README.md) — the definition's front door.

## Collections

### <Framing collection>

The framing docs — declared first.

- **Leaf:** [<Framing>/index.md](../<Framing>/index.md)
- **Flavors:**
  - [<kind>](shapes/frame.<kind>.md) — one flavor per kind of frame (mark one default).
- **Canvas:** file

### <Collection>

One line on what this collection holds.

- **Leaf:** [<Collection>/index.md](../<Collection>/index.md)
- **Flavors:**
  - [<flavor-1>](shapes/<kind>.<flavor-1>.md) — the fuller shape (default).
  - [<flavor-2>](shapes/<kind>.<flavor-2>.md) — a lighter one to grow out of.
- **Canvas:** card from `## <Section>`
- **<Grouping>:**
  - **<Group>** — one line on what falls under it.

## Schema

### Eidos Core
<!-- the standard's block: id, title, summary, flavor, connects_to -->

### Custom Properties
| Name   | Type | Applies To   | Meaning                        |
| ------ | ---- | ------------ | ------------------------------ |
| <name> | Text | all          | Whatever this framework needs. |
| <name> | Text | <Collection> | Scoped to one collection.      |
```

- **`eidos_version`** — the version this framework targets. `migrate` reads and bumps it.
- **`naming`** — `kebab-case` (default), `TitleCase`, or `Title Case`. See [Naming](#naming).
- **`## Top-Level`** — the top-level docs, `README` first. Framing docs are not here; they are a collection.
- **`## Collections`** — one `###` each: its **Leaf**, its **Flavors** (default marked), its **Canvas**, and its grouping.
- **`- **Canvas:**`** — how `canvas` draws the collection: `file` (a full-file node, for prose read whole), `card` (a node embedding the item), or `card from ## Section` (a node embedding that section). Absent means a plain card — the generator knows no collection by name and cannot guess which section is the summary.
- **`## Schema`** — `### Eidos Core` (the standard's, rewritten by `migrate`) and `### Custom Properties` (the framework's).

### Shapes and flavors

A shape is body-only: sections in their order, under set names, with their guidance. Every item in a collection follows one of that collection's declared flavors, and a check validates against the flavor the item names. Shape files are `<kind>.<flavor>.md`, lowercase and dotted. Top-level docs have no shape.

The default flavor is what gets scaffolded; an item on another records it in `flavor`. An item on a lighter flavor is never faulted for the sections only a fuller one carries.

### Schema

Each property is a row: **Name · Type · Applies To · Meaning**. A type comes from the set Obsidian uses — **Text, List, Number, Checkbox, Date, Date & time** — so frontmatter renders natively in a vault. Anything wanting more structure than one of those belongs in the body.

**Applies To** scopes a property to collections: `all`, or a list. Frontmatter is generated per item from the properties that apply to its collection, so a scoped property never lands where it makes no sense.

**The core** — present on every item, and the whole of what the standard requires:

| Name | Type | Meaning |
| --- | --- | --- |
| `id` | Text | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it. |
| `title` | Text | Human-readable name. |
| `summary` | Text | One plain line: what this item is. The source for the collection's [`index.md`](#generated-leaves) listing; absent, the index flags it. |
| `flavor` | Text | Which flavor this item follows. Absent = the collection's default. |
| `connects_to` | List | Items this one connects to on the canvas, each a link, drawn as a directed edge. |

**Eidos defines no custom properties.** A lifecycle `status`, dates, a grouping, a dependency list — all are a framework's own choice. Each [seed](seeds) makes its own set. Add one with `configure`, which presses for all four of Name, Type, Applies To, and Meaning, then backfills the items it applies to.

### Personas and the actor

Not every human on a definition plays the same part — one holds the intent, another builds or drafts from it, another reviews it, another answers for it. The agent responds to each differently, from two files:

- **`_eidos/personas/<role>.md`** — one response contract per role: vocabulary and technical depth, what to surface versus fold away, and who holds which decisions. Which roles exist is the framework's call; each [seed](seeds) ships a set written against its own collections. Committed and team-tunable.
- **`_eidos/user.md`** — personal and gitignored, one per person. Names the actor's persona and calibrates it on three axes: **role**, **experience with the scope**, and **technical capacity**. Set it with `whoami`. Blank is fine.

One persona is common to every seed: the **Framework Owner**, who holds the intent, the scope, and the decisions. The rest of the cast depends on the work.

## Writing a definition

### `README.md`

A visible front door at the definition root: what the thing is, and pointers into it — the top-level docs, the collections and their indexes, and `_eidos/Framework.md` for the full index. Thin, orientation and links, edited in place.

### Naming

Everything a human reads in the tree — top-level docs, collection and sub-folders, item files — follows the framework's `naming` convention.

| Convention | An item file | A grouping folder | For |
| --- | --- | --- | --- |
| **kebab-case** (default) | `item-title-here.md` | `group-name/` | readable everywhere: no escaping, no `%20`, and the filename *is* the `id` |
| **TitleCase** | `ItemTitleHere.md` | `GroupName/` | space-free, capitalized |
| **Title Case** | `Item Title Here.md` | `Group Name/` | a tree that reads like prose, at the cost of `%20` in every link |

An absent `naming` key means `kebab-case`.

One convention governs the whole definition, and changing it later means renaming files, so it is settled at init. Whichever you pick: `_eidos/` is always lowercase; `README.md` keeps the name every tool already looks for; the `id` is always kebab-case; a grouping property's value matches its folder exactly; and fields meant for tools are not names in the tree.

### Linking

Point at another item, doc, or section with a standard markdown link: the text is the human title, the path is the target's filename in the framework's convention (only a Title Case definition carries `%20`). Add a `#heading` anchor for a section. Properties that point outward hold links too, not bare ids — quote them in YAML, since a leading `[` starts a list:

```yaml
depends_on:
  - "[Some Item](../some-group/some-item.md)"
```

If a target has no item yet, name it plainly rather than fabricating a link.

### Item bodies

The body follows its flavor's shape. Keep the shape's order and names; leave a section out when it genuinely doesn't apply rather than leaving it empty. Within and beneath those sections, write it like a person would read it — sub-headings, tables, lists, small diagrams wherever they make the meaning clearer. Keep checkable statements short and observable, labeled the way the shape asks, with supporting detail pushed into a table or sub-section they point at.

The sections themselves are documented in the shape file, not here.

### Frames and top-level docs

Both are loose, point-in-time prose: record what is true now, revise when it changes. They differ in one way. A **frame** is a collection item — it follows a shape, carries the frontmatter contract, and is validated. A **top-level doc** is one-of-a-kind, filled in once and edited in place, so it needs no shared shape and gets none. A shape earns its keep by being stamped again; a document written once doesn't need a cookie-cutter.

For a top-level doc you've already drafted, `format` organizes it into the house style without adding anything of its own.

## Generated leaves

Two derived views. Both are regenerated wholesale, annotate rather than gate, and have nothing hand-written to preserve.

**The index.** Each collection carries a generated `index.md` in its folder, listing its items — grouped under their sub-folders when it has them, flat when it doesn't. Each line is the item's `summary`, verbatim; an item with none is flagged, never invented. Links are relative to the collection folder. Rebuilt by `index`.

```markdown
# <Collection>

<!-- index: <Collection> (regenerated) -->

## <Group>
- [<Title>](<Group>/<Title>.md) — the item's one-line `summary`, verbatim.
- [<Title>](<Group>/<Title>.md) — one bullet per item, in file order.
```

**The canvas.** The spatial counterpart: an Obsidian `.canvas` map from `canvas`. Each collection draws the way it declares itself, is its own group, and nests a group per sub-folder; each item's `connects_to` links become directed edges (with `depends_on` optionally overlaid in another color). The generated `.canvas` is itself a top-level doc — register it in `## Top-Level`.

## Rules

The load-bearing conventions.

1. **The frontmatter is the agreement; the body is guidance.** Properties are checked against the framework's Schema. Body sections are recommended structure, not requirements.
2. **The definition owns its framework.** Shapes and properties live in the definition's `_eidos/`. A skill reads the framework from the definition, not from a copy of its own.
3. **Validation is framework-defined.** A check reads *that framework's* Schema and enforces it — the core properties plus the custom ones scoped to the item's collection. The contract is the Schema, not a rule hardcoded in a tool.
4. **Portability over prescription.** A missing core property is surfaced and added with a note on why; a missing section is noted and offered. Never refuse the file.
5. **Write it like a human would read it.** The sections are a scaffold for a living item, not a form to pour text into. If an item reads like filled-in boilerplate, reshape it until it reads like someone wrote it.
6. **Reference other items with links, not bare names** — in prose and in properties alike. Each item's `id` is still its permanent identity, sitting behind the link.
7. **One shape family per collection, declared as flavors.** What flexes is *which* sections appear and *which* flavor an item uses; never their order or names within a flavor. The shape is never forked per category.
8. **Properties carry a type and a meaning.** Every property declares its name, its type, which collections it applies to, and what it means. Frontmatter is generated from the Schema, so a new item is born conforming.
9. **Soft labels are views, not structure.** A category label a framework adds drives views and filtering, never structure. An off-list value is valid. `flavor` carries the structural choice.
10. **A collection's grouping is the collection's own.** It may group its items one level deep and may declare a property naming that grouping; the value then matches the folder, and an unknown value warns rather than blocks. The standard never names a grouping for it.
11. **`id` is permanent.** Stable, unique, kebab-case, assigned once, never renamed. Rename `title` freely.
12. **A shape names its own stable part.** Every shape has a part that holds still and a part that moves, and says which is which. If the stable part changes substantially, ask whether this is a different item.
13. **Non-goals carry the most weight.** Where a shape declares a section for what an item deliberately will *not* do, that section is its strongest — it is where scope management actually happens. Still not a hard gate.
14. **A shape documents its own conventions.** Section names, their order and meaning, and any labeling a shape asks for live in the shape file. This standard governs collections, shapes, flavors, and properties; it never governs a section.
15. **No work-tracking fields.** No `sprint`, `estimate`, or `assignee` — the moment you add them, an item becomes a task and rots. Bridge to a tracker with a link. The same holds in the body: a section describing how you mean to build a thing captures intent, never how far along it is.
16. **`date_created` is set once; `date_modified` tracks the last change.** Git holds the full history. The Eidos version is a framework fact, in `Framework.md`, not a per-item property.
17. **Point-in-time documents evolve.** A top-level doc, and any collection a framework marks as loose prose, captures a snapshot of intent and is expected to change.
18. **The human authors; the agent facilitates.** Intent, scope, and decisions stay with the person. An agent formats, supplements, asks, and holds scope; it does not generate finished items or set direction. An item the owner did not think through is worse than none.
19. **Human-facing names follow the framework's naming convention** — `kebab-case` unless the framework says otherwise. The hidden `_eidos/` and the root `README.md` are the exceptions, keeping the names every tool already looks for. The kebab-case `id`, not the filename, is the permanent reference.
20. **`Framework.md` is the framework's index; `README.md` is its door.** `configure` keeps both current.
21. **Read the actor before acting.** Read `_eidos/user.md` and the matching contract in `_eidos/personas/`, and respond as that persona defines. The human-first principle holds for every persona; only the mode changes. A blank or absent file defaults to full facilitation.
22. **Every framework declares a framing collection.** Its name, its flavors, and how many it carries are the framework's own — a framework needs framing, not a particular set of frames. Required as a **declaration**: a framework that declares none is incomplete and a check says so. Never a gate: a declared frame left unwritten is a gap to surface, not a failure.
23. **Each collection has a generated index.** Rebuilt by `index`. Grouping more than one level deep is discouraged.
24. **Shapes are for collections; top-level docs have none.** A top-level doc is free-form prose: no shape, no flavors, not validated, edited in place.

## Versioning

Semantic Versioning: major for breaking changes, minor for backward-compatible additions, patch for clarifications.

This file holds the version of **the standard** — right now, **4.4.0** — and it moves only when the text of this file moves. A framework records the version it targets as `eidos_version` in its `_eidos/Framework.md`; `migrate` reads and bumps it there. At tag time this file is copied as-is into `versions/` under its full semver name, so any two releases, even non-adjacent, can be diffed to migrate between them. Worked hops are in `versions/MIGRATIONS.md`. Tools may reject an unsupported version.

**The plugin that ships this standard versions separately.** Skills, seeds, and examples change far more often than the standard does, so a release that fixes a skill bumps the plugin and leaves this file — and every definition's `eidos_version` — untouched. When you need to know what a definition conforms to, read this version; the plugin's is in `.claude-plugin/plugin.json`, and `CHANGELOG.md` records which standard each plugin release carried.

## For an agent

_Operating detail. A human can stop above._

**Prefer the skills.** `eidos` authors and validates, `iterate` questions a rough idea into shape before any of that, `install` scaffolds, `configure` adds a collection, flavor, or property and keeps the Framework current, `index` rebuilds a collection's leaf, `canvas` draws the map, `whoami` sets the actor, `migrate` upgrades versions.

**Find the framework in the definition.** Locate a definition by its `_eidos/` marker, not its folder name. Every operation reads that `_eidos/`. If a folder has none, offer `install`. Never fall back to a hardcoded contract, and never assume a collection or section name — read what the framework declares.

**Read the actor first.** `_eidos/user.md`, then the persona file it names. Respond as that file defines the role — read it, don't infer from its filename. A framework defines its own cast.

**Navigate by the leaves.** `README.md` for orientation, `_eidos/Framework.md` for the full index, each collection's `index.md` for its items. Read these instead of scraping the tree; regenerate them when stale.

**Authoring an item:**

1. From `Framework.md`, take the Schema, the naming convention, and the target collection's flavors. Pick a flavor (the default unless the owner chooses another) and read its shape for the body. Name the file for its title in the convention; put a permanent kebab-case `id` inside.
2. Generate frontmatter from the properties that apply to that collection. Fill values from what the owner tells you; leave a property blank rather than guessing it.
3. Lead with the shape's opening sections and press hardest on its non-goals section. Read those names off the shape rather than assuming them, and follow whatever labeling it asks for. Omit a section that doesn't apply; keep the order and names of the ones that do.
4. Where the owner is vague, ask. Don't fill the gap with plausible prose.

**Validating an item:** check frontmatter against the framework's Schema (`id` kebab-case, dates as `YYYY-MM-DD`, custom properties scoped to the collection). Report missing body sections against *the item's flavor shape*, flagging an absent non-goals section first, and note anything skipping the labeling that shape asks for. Confirm no work-tracking fields crept in. Surface, don't block — the output is a review a human acts on.

**Facilitate, don't author.** Format and structure what the owner gives you, supplement, ask, and press on scope. Never invent an item's purpose, decide direction, or hand back a finished item to rubber-stamp. When unsure, ask.
