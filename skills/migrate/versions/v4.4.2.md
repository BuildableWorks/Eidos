# Eidos

**Version:** 4.4.2

A markdown standard for defining the essence of a thing — a product, a body of work, anything you set out to make. One file is the complete source of truth for one unit of it, independent of time or status: as true of something planned as of something long finished.

This file is the contract: the terms, the structures, and the rules. It names no collection, no shape, and no section — those belong to a framework, not to the standard. For worked frameworks see [`seeds/`](seeds). Doing the work takes a person, this contract, and the [skills](#for-an-agent).

## Vocabulary

Every term the standard uses, in the order they build on each other.

| Term | What it is |
| --- | --- |
| **root** | The one folder Eidos lives in, holding the framework, the collections, and any top-level docs. Found by the hidden `_eidos/` inside it, never by its name. |
| **framework** | The *form* a root is written in — its collections, shapes, flavors, roles, naming convention, and Schema. Lives in the root's hidden `_eidos/`. Portable: the same framework governs any number of roots. |
| **collection** | A top-level folder of repeated blueprints that share a body shape. A framework declares each one, and may group a collection's blueprints in one level of sub-folders. |
| **blueprint** | One markdown file in a collection, defining one unit completely. Frontmatter (a contract) plus a body (a shape). |
| **frame** | A blueprint describing the whole thing rather than one unit of it. Frames set what every other blueprint is judged against, and are revised whenever that judgment changes. Every framework declares a framing collection. |
| **shape** | One body template: the sections a blueprint carries, in order, under set names, each with its guidance. Body only; frontmatter is generated. One file per shape, in `_eidos/shapes/`. |
| **flavor** | A collection's shapes are variants of one family, and each variant is a flavor (`<kind>.<flavor>`). A collection declares one or more and marks one default — typically a light flavor a blueprint can grow out of, beside a fuller one. |
| **property** | One frontmatter field: a name, a type, which collections it applies to, and a meaning. |
| **Schema** | The framework's whole property contract: the core properties Eidos requires, plus whatever the framework adds. |
| **top-level doc** | A one-of-a-kind document at the root — a Roadmap, a Vision, the generated canvas. Free-form: no shape, no flavors, no validation. |
| **role** | A response contract for one kind of person, saying how an agent talks to them. |
| **actor** | Who is in the seat right now: their role, plus a personal calibration. |
| **seed** | A starting framework the standard ships. `install` copies one into a new root. |

A blueprint captures **state and intent, not work**. A task describes work and dies when the work ships; a blueprint describes the thing and stays accurate across its whole life — drafted, built, deprecated.

## Layout

The root is found by the hidden `_eidos/` inside it. It may be named anything; nothing points at it by path.

```txt
Blueprints/              # the root — `Blueprints` is only the default name
  README.md              # the visible "start here"
  _eidos/                # the framework (below)
  <Framing>/             # the framing collection — declared first
    index.md             #   generated leaf
    <Frame>.md           #   one per kind of frame, flat
  <Collection>/          # a collection of blueprints; declare as many as the work needs
    index.md             #   generated leaf
    <Group>/             #   one level of sub-folders, at most
      <Title>.md         #     one blueprint per file
  roadmap.md             # a top-level doc — optional, yours
```

Several roots in one repository nest as `Blueprints/<name>/…`, each with its own `_eidos/`.

## The framework (`_eidos/`)

Hidden the way `.git` and `.obsidian` are: present, manageable, out of the way once set. The root is plausibly an Obsidian vault, and `_eidos/` sits beside `.obsidian/`.

```txt
_eidos/
  shapes/                  # one file per flavor
    <kind>.<flavor-1>.md   #   a collection's default flavor
    <kind>.<flavor-2>.md   #   a second flavor of the same kind
    frame.<kind>.md        #   the framing collection's flavors, one per kind of frame
  roles/                   # response contracts, committed and team-tunable
    framework-owner.md     #   the one every seed carries
    <role>.md              #   the rest are the framework's own
  Framework.md             # index + config: version, naming, Top-Level, Collections, Schema
  me.md                    # the actor (personal, gitignored)
  .gitignore               # ignores me.md — the one file here not committed
```

The skills read the framework from the root they are working in, never from a copy of their own. A folder with no `_eidos/` is not a root.

### `Framework.md`

The one file describing the form rather than any single blueprint: frontmatter for the facts tooling parses, and a body indexing what it governs.

```markdown
---
eidos_version: 4.4.2
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
- **`- **Canvas:**`** — how `canvas` draws the collection: `file` (a full-file node, for prose read whole), `card` (a node embedding the blueprint), or `card from ## Section` (a node embedding that section). Absent means a plain card — the generator knows no collection by name and cannot guess which section is the summary.
- **`## Schema`** — `### Eidos Core` (the standard's, rewritten by `migrate`) and `### Custom Properties` (the framework's).

### Shapes and flavors

A shape is body-only: sections in their order, under set names, with their guidance. Every blueprint in a collection follows one of that collection's declared flavors, and a check validates against the flavor the blueprint names. Shape files are `<kind>.<flavor>.md`, lowercase and dotted. Top-level docs have no shape.

The default flavor is what gets scaffolded; a blueprint on another records it in `flavor`. A blueprint on a lighter flavor is never faulted for the sections only a fuller one carries.

### Schema

Each property is a row: **Name · Type · Applies To · Meaning**. A type comes from the set Obsidian uses — **Text, List, Number, Checkbox, Date, Date & time** — so frontmatter renders natively in a vault. Anything wanting more structure than one of those belongs in the body.

**Applies To** scopes a property to collections: `all`, or a list. Frontmatter is generated per blueprint from the properties that apply to its collection, so a scoped property never lands where it makes no sense.

**The core** — present on every blueprint, and the whole of what the standard requires:

| Name | Type | Meaning |
| --- | --- | --- |
| `id` | Text | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it. |
| `title` | Text | Human-readable name. Rename it freely; `id` is what holds still. |
| `summary` | Text | One plain line: what this blueprint is. The source for the collection's [`index.md`](#generated-leaves) listing; absent, the index flags it. |
| `flavor` | Text | Which flavor this blueprint follows. Absent = the collection's default. |
| `connects_to` | List | Blueprints this one connects to on the canvas, each a link, drawn as a directed edge. |

**Eidos defines no custom properties.** A lifecycle `status`, dates, a grouping, a dependency list — all are a framework's own choice. Each [seed](seeds) makes its own set. Add one with `configure`, which presses for all four of Name, Type, Applies To, and Meaning, then backfills the blueprints it applies to.

### Roles and the actor

Not everyone who works on the same root plays the same part — one holds the intent, another builds or drafts from it, another reviews it, another answers for it. The agent responds to each differently, from two files:

- **`_eidos/roles/<role>.md`** — one response contract per role: vocabulary and technical depth, what to surface versus fold away, and who holds which decisions. Which roles exist is the framework's call; each [seed](seeds) ships a set written against its own collections. Committed and team-tunable.
- **`_eidos/me.md`** — personal and gitignored, one per person. Names the actor's role and calibrates it on three axes: **ownership**, **experience with the scope**, and **technical capacity**. Set it with `whoami`. Blank is fine.

One role is common to every seed: the **Framework Owner**, who holds the intent, the scope, and the decisions. The rest of the cast depends on the work.

## Writing

### `README.md`

A visible front door at the root: what the thing is, and pointers into it — the top-level docs, the collections and their indexes, and `_eidos/Framework.md` for the full index. Thin, orientation and links, edited in place.

### Naming

Everything a human reads in the tree — top-level docs, collection and sub-folders, blueprint files — follows the framework's `naming` convention.

| Convention | A blueprint file | A grouping folder | For |
| --- | --- | --- | --- |
| **kebab-case** (default) | `blueprint-title-here.md` | `group-name/` | readable everywhere: no escaping, no `%20`, and the filename *is* the `id` |
| **TitleCase** | `BlueprintTitleHere.md` | `GroupName/` | space-free, capitalized |
| **Title Case** | `Blueprint Title Here.md` | `Group Name/` | a tree that reads like prose, at the cost of `%20` in every link |

An absent `naming` key means `kebab-case`.

One convention governs the whole folder, and changing it later means renaming files, so it is settled at init. Whichever you pick: `_eidos/` is always lowercase; `README.md` keeps the name every tool already looks for; the `id` is always kebab-case; a grouping property's value matches its folder exactly; and fields meant for tools are not names in the tree.

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

Two derived views. Both are regenerated wholesale, annotate rather than gate, and have nothing hand-written to preserve.

**The index.** Each collection carries a generated `index.md` in its folder, listing its blueprints — grouped under their sub-folders when it has them, flat when it doesn't. Each line is the blueprint's `summary`, verbatim; a blueprint with none is flagged, never invented. Links are relative to the collection folder. Rebuilt by `index`.

```markdown
# <Collection>

<!-- index: <Collection> (regenerated) -->

## <Group>
- [<Title>](<Group>/<Title>.md) — the blueprint's one-line `summary`, verbatim.
- [<Title>](<Group>/<Title>.md) — one bullet per blueprint, in file order.
```

**The canvas.** The spatial counterpart: an Obsidian `.canvas` map from `canvas`. Each collection draws the way it declares itself, is its own group, and nests a group per sub-folder; each blueprint's `connects_to` links become directed edges (with `depends_on` optionally overlaid in another color). The generated `.canvas` is itself a top-level doc — register it in `## Top-Level`.

## Rules

The load-bearing conventions.

1. **The frontmatter is the agreement; the body is guidance.** Properties are checked against the framework's Schema. Body sections are recommended structure, not requirements.
2. **The root owns its framework.** Shapes and properties live in the root's `_eidos/`. A skill reads the framework from the root it is working in, not from a copy of its own.
3. **Validation is framework-defined.** A check reads *that framework's* Schema and enforces it — the core properties plus the custom ones scoped to the blueprint's collection. The contract is the Schema, not a rule hardcoded in a tool.
4. **Portability over prescription.** A missing core property is surfaced and added with a note on why; a missing section is noted and offered. Never refuse the file.
5. **Write it like a human would read it.** The sections are a scaffold for a living blueprint, not a form to pour text into. If a blueprint reads like filled-in boilerplate, reshape it until it reads like someone wrote it.
6. **Reference other blueprints with links, not bare names** — in prose and in properties alike. Each blueprint's `id` is still its permanent identity, sitting behind the link.
7. **One shape family per collection, declared as flavors.** What flexes is *which* sections appear and *which* flavor a blueprint uses; never their order or names within a flavor. The shape is never forked per category.
8. **Properties carry a type and a meaning.** Every property declares its name, its type, which collections it applies to, and what it means. Frontmatter is generated from the Schema, so a new blueprint is born conforming.
9. **Soft labels are views, not structure.** A category label a framework adds drives views and filtering, never structure. An off-list value is valid. `flavor` carries the structural choice.
10. **A collection's grouping is the collection's own.** It may group its blueprints one level deep and may declare a property naming that grouping; the value then matches the folder, and an unknown value warns rather than blocks. The standard never names a grouping for it.
11. **A shape names its own stable part.** Every shape has a part that holds still and a part that moves, and says which is which. If the stable part changes substantially, ask whether this is a different blueprint.
12. **Non-goals carry the most weight.** Where a shape declares a section for what a blueprint deliberately will *not* do, that section is its strongest — it is where scope management actually happens. Still not a hard gate.
13. **A shape documents its own conventions.** Section names, their order and meaning, and any labeling a shape asks for live in the shape file. This standard governs collections, shapes, flavors, and properties; it never governs a section.
14. **No work-tracking fields.** No `sprint`, `estimate`, or `assignee` — the moment you add them, a blueprint becomes a task and rots. Bridge to a tracker with a link. The same holds in the body: a section describing how you mean to build a thing captures intent, never how far along it is.
15. **The Eidos version is a framework fact.** It lives in `Framework.md`, never as a per-blueprint property. Git holds the history; a framework that wants date properties declares them like any other.
16. **Loose prose is revised in place.** A top-level doc, and any collection a framework marks as loose prose, records what is true now and is expected to change. That is revision, not work status.
17. **The human authors; the agent facilitates.** Intent, scope, and decisions stay with the person. An agent formats, supplements, asks, and holds scope; it does not generate finished blueprints or set direction. A blueprint the owner did not think through is worse than none.
18. **Read the actor before acting.** Read `_eidos/me.md` and the matching contract in `_eidos/roles/`, and respond as that role defines. The human-first principle holds for every role; only the mode changes. A blank or absent file defaults to full facilitation.
19. **Every framework declares a framing collection.** Its name, its flavors, and how many it carries are the framework's own — a framework needs framing, not a particular set of frames. Required as a **declaration**: a framework that declares none is incomplete and a check says so. Never a gate: a declared frame left unwritten is a gap to surface, not a failure.

## Versioning

Semantic Versioning: major for breaking changes, minor for backward-compatible additions, patch for clarifications.

This file holds the version of **the standard** — right now, **4.4.2** — and it moves only when the text of this file moves. A framework records the version it targets as `eidos_version` in its `_eidos/Framework.md`; `migrate` reads and bumps it there. At tag time this file is copied as-is into `versions/` under its full semver name, so any two releases, even non-adjacent, can be diffed to migrate between them. Worked hops are in `versions/MIGRATIONS.md`. Tools may reject an unsupported version.

**The plugin that ships this standard versions separately.** The skills and seeds change far more often than the standard does, so a release that fixes a skill bumps the plugin and leaves this file — and every framework's `eidos_version` — untouched. When you need to know what a framework conforms to, read this version; the plugin's is in `.claude-plugin/plugin.json`, and `CHANGELOG.md` records which standard each plugin release carried.

## For an agent

_Operating detail. A human can stop above._

**Prefer the skills.** `eidos` authors and validates, `iterate` questions a rough idea into shape before any of that, `format` reshapes a draft already written, `install` scaffolds, `configure` adds a collection, flavor, or property and keeps the Framework current, `index` rebuilds a collection's leaf, `canvas` draws the map, `whoami` sets the actor, `migrate` upgrades versions.

**Find the framework in the root.** Locate the root by its `_eidos/` marker, not its name. Every operation reads that `_eidos/`. If a folder has none, offer `install`. Check the framework's `eidos_version` against the standard you carry once per session: a gap is worth one line and an offer of `migrate`, never a block, and the framework in front of you is the operative contract either way. Never fall back to a hardcoded contract, and never assume a collection or section name — read what the framework declares.

**Read the actor first.** `_eidos/me.md`, then the role file it names. Respond as that file defines the role — read it, don't infer from its filename. A framework defines its own cast.

**Navigate by the leaves.** `README.md` for orientation, `_eidos/Framework.md` for the full index, each collection's `index.md` for its blueprints. Read these instead of scraping the tree; regenerate them when stale.

**Authoring a blueprint:**

1. From `Framework.md`, take the Schema, the naming convention, and the target collection's flavors. Pick a flavor (the default unless the owner chooses another) and read its shape for the body. Name the file for its title in the convention; put a permanent kebab-case `id` inside.
2. Generate frontmatter from the properties that apply to that collection. Fill values from what the owner tells you; leave a property blank rather than guessing it.
3. Lead with the shape's opening sections and press hardest on its non-goals section. Read those names off the shape rather than assuming them, and follow whatever labeling it asks for. Omit a section that doesn't apply; keep the order and names of the ones that do.
4. Where the owner is vague, ask. Don't fill the gap with plausible prose.

**Validating a blueprint:** check frontmatter against the framework's Schema (`id` kebab-case, dates as `YYYY-MM-DD`, custom properties scoped to the collection). Report missing body sections against *the blueprint's flavor shape*, flagging an absent non-goals section first, and note anything skipping the labeling that shape asks for. Confirm no work-tracking fields crept in. Surface, don't block — the output is a review a human acts on.

**Facilitate, don't author.** Format and structure what the owner gives you, supplement, ask, and press on scope. Never invent a blueprint's purpose, decide direction, or hand back a finished blueprint to rubber-stamp. When unsure, ask.
