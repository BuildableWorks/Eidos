# Eidos

**Version:** 4.2.1

The Eidos standard — a markdown method where one file completely defines one unit of a product, true whether or not the thing has been built. This file is the method: what an item is, how a definition is shaped, and how the pieces fit. It gives the direction; the skills and a seeded definition are how you actually do the work (see [AI](#ai)).

## Vocabulary

Two words carry the whole standard, and they are not interchangeable.

- A **framework** is the form: the collections, body shapes and flavors, personas, naming convention, and property Schema that govern how a definition is written. It lives in the hidden [`_eidos/`](#the-form-layer) folder, it is portable, and it is the piece one team can hand to another.
- A **definition** is the product: the frames, items, and top-level docs a team writes with a framework. It describes their product, it is theirs, and it is the thing Eidos exists to produce.

One framework, many definitions. Everything below uses the two words in exactly that sense.

## What an item is

An **item** is a living markdown document that defines one unit of a product completely: "this is what you're getting," with no ambiguity. An item is true whether or not the thing it describes has been built. It captures **state and intent, not work**. Tasks describe work and die when the work ships; an item describes the product and stays accurate across its whole life: drafted, built, deprecated.

An item has two parts: a small **frontmatter** (the properties at the top, between the `---` lines) and a **body** (the prose below). The frontmatter is a contract; the body follows a shape. Both are defined by the framework, which lives in the definition's [form layer](#the-form-layer) — not hardcoded here.

A spec is the default unit Eidos defines, and the rest of this file teaches from it — but it isn't the whole of Eidos. A framework declares the [collections](#collections) a definition organizes its units into (`Specs` is the one Eidos seeds) and may define others, each with its own shape; "spec" and "domain" are the default seed, not the essence.

## A human-first standard

Eidos is a tool for a person — typically a Framework Owner — to think clearly about what their product is. It is not a way to hand the job of defining a product to an AI. The human holds the intent, the scope, and the decisions; those are the parts of the job that cannot be delegated without the owner losing the thread of their own product.

An agent's role is **facilitation, not authorship**. It formats, supplements, fills in shapes, asks clarifying questions, and pushes on scope (especially Out of Scope). It does not invent intent, decide direction, or generate a finished item for a human to rubber-stamp. An item the owner did not actually think through is worse than no item: it reads as settled, but no one knows it. When in doubt, an agent asks rather than writes. The measure of a good Eidos session is that the human understands and stands behind every line — not that a lot of text appeared.

Eidos is opinionated but not rigid. It ships a strong default — the shapes and properties below — and then lets a framework supplement or change them. You adopt without forking, customize without leaving the standard, and still migrate, because the parts Eidos owns stay versioned while the parts you add are preserved.

## The actor

Eidos is human-first, and not every human working on a definition plays the same part — a Framework Owner decides, a developer builds, a stakeholder reviews, a designer shapes the experience. The agent must respond to each **differently**, so the actor is a core input it reads **before acting**, in two pieces:

- **Personas** (`_eidos/personas/`) — the response contracts, one per role. A persona sets the **vocabulary and technical depth**, **what to surface vs. fold away**, and **who holds which decisions**: the Designer persona keeps db relationships and indexes out of the reply and talks in experience terms; the Developer persona invites full technical depth; the Framework Owner persona brings the decisions to the owner and never decides for them. They are committed and team-tunable, seeded from the standard's [`personas/`](seed/personas), so a team can adjust how a role is treated for their product.
- **The actor file** (`_eidos/user.md`) — personal and **gitignored**, one per person. It names the actor's persona and **calibrates** it on three axes: their **role for this product**, their **experience with the scope** (how much orientation to give), and their **technical capacity** (how much mechanism and jargon to use). Persona sets the baseline; calibration tunes it for the person. Set it with the [`eidos-whoami`](#ai) skill; it ships blank, and `eidos-install` seeds a `.gitignore` so it never lands in anyone else's checkout.

The persona changes the mode, not the principle: whoever the actor, the human authors and decides and the agent facilitates. A blank or absent `user.md` is fine — the agent defaults to full, framework-owner-style facilitation and offers to record who you are; it never gates. A persona is a baseline, not a cage — an actor may write a custom role, and a framework may add or reshape its personas. The five Eidos ships are **Framework Owner**, **Developer**, **Stakeholder**, **Designer**, and **Project Manager**; their full contracts live in [`personas/`](seed/personas).

## Two kinds of document

Eidos holds two kinds of document. They behave differently on purpose.

- **Collections** are the many. A **collection** is a folder of repeated units that share a body shape; a framework can have several, and may group a collection's units one level deep. A unit is a small frontmatter contract plus a body in a [shape](#the-form-layer) — and a collection can offer more than one shape, a [flavor](#flavors). Eidos seeds two: `Specs` (grouped by `domain`, the product's units) and `Frames` (the framing docs — architecture, audience, criteria, market — that set what every unit is judged against). The collections are the framework's to define (see [Collections](#collections)).
- **Top-level docs** — one-of-a-kind documents at the definition root that you add yourself: a Roadmap, a Vision, the generated Framework Map. They are free-form prose, deliberately loose, and point-in-time — the layer that annotates the whole product with no shape behind it (see [Top-level docs](#top-level-docs)).

Frames drive decisions and audit scope; Specs capture the units that result; top-level docs hold whatever else the product needs said. When framing the _whole product_, reach for a Frame. When defining a _piece_ of it, reach for the right collection — a spec, by default.

## The form layer

A definition is two things: **content** and **form**. The form is its framework.

- **Content** is what you write — the collections' units and any top-level docs. It is visible, Title Case, and reads like a table of contents.
- **Form** is the **framework**: the body **shapes** for a collection's items (one or more [flavors](#flavors) each), the property contract, and the response contracts (personas). It is machinery. It lives in a hidden **`_eidos/`** folder at the definition root, named the way `.git` and `.obsidian` are: present, manageable, but out of the way once set. An Eidos definition is plausibly an Obsidian vault, and `_eidos/` sits beside `.obsidian/`.

```txt
_eidos/
  shapes/          # collection body shapes (flavored, shared, validated against)
    spec.full.md   # the Specs collection's default flavor
    spec.micro.md  # a lighter flavor of the same, to grow into full
    frame.architecture.md  # the Frames collection's flavors — one per framing doc
    frame.audience.md
    frame.criteria.md
    frame.market.md
  personas/        # response contracts — how the agent treats each role (committed, tunable)
    framework-owner.md
    developer.md
    stakeholder.md
    designer.md
    project-manager.md
  Framework.md      # the framework's index + config: version, naming, Top-Level, Collections, Schema
  user.md          # who is in the seat: persona + calibration (personal, gitignored)
  .gitignore       # ignores user.md — the one file in here not committed
```

A definition owns its framework. Eidos seeds `_eidos/` with the opinionated baseline (`eidos-install`), and from there the owner may extend it — add a property, adjust a shape, add a flavor — without leaving the standard. This is what makes Eidos adoptable without a fork: the default works out of the box, and the parts you change are yours. Because a framework is form and carries no product content, one that proves itself can be handed to another team and used to start a fresh definition.

Because the framework lives in the definition, the skills read it from there rather than carrying their own copy. A definition that calls itself Eidos has a `_eidos/`; a skill that finds none offers to install a framework (see [AI](#ai)).

### Shapes (`_eidos/shapes/`)

A **shape** is the body template a **collection's** items share — body only (the sections in their order, with their guidance), because an item's frontmatter is generated from the [Schema](#properties), not written by hand. A shape is the **shared, ongoing form of the many**: every item in the collection follows it, and a check validates against it. A collection may offer more than one shape of its body — a [flavor](#flavors) — each its own file named `<kind>.<flavor>.md` (`spec.full.md`, `spec.micro.md`, `frame.architecture.md`). The framing docs are a collection like any other: the `Frames` collection's flavors — `frame.architecture.md`, `frame.audience.md`, `frame.criteria.md`, `frame.market.md` — are ordinary shapes, one per kind of frame.

The canonical shapes Eidos ships — the opinionated baseline — live, public and browsable, in [`seed/shapes/`](seed/shapes) at the top of the standard's repo; `eidos-install` installs them into a definition's `_eidos/`. A framework may then reshape its own, add flavors, and the skills consume whatever it holds. The shape files are where the specific sections are documented; [Item body](#item-body) below gives the rules for using them.

### Properties

The property contract is a **`## Schema` section inside [`_eidos/Framework.md`](#framework)** — one file holds the whole framework: its index and its contract. The Schema has two parts:

- **`### Eidos Core`** — the properties Eidos's own machinery uses. Managed by the standard; `eidos-migrate` rewrites this block on a version change. Don't hand-edit it.
- **`### Custom Properties`** — everything else the framework carries. The seed pre-populates it with a few useful defaults (a lifecycle `status`, the two dates, `tags`, and — scoped to `Specs` — `domain`, `depends_on`, and `type`), but Eidos does not depend on them; keep, scope, or drop any. Yours, and preserved across migration.

Each property is a row: **Name · Type · Applies To · Meaning** (the core properties are universal, so they omit Applies To). A property's type is drawn from the same small set Obsidian uses — **Text, List, Number, Checkbox, Date, Date & time** — so a definition's frontmatter renders natively in an Obsidian vault. Anything that wants more structure than one of those types almost belongs in the body (the shape), not in a property.

**Applies To scopes a property to collections.** Every custom property declares which collections it belongs to — `all`, or a list (`Specs`). Frontmatter is generated per item from the properties that apply to its collection, so a `Specs`-only property like `domain` never lands on a `Frames` item. This is how a framework keeps a property from appearing where it makes no sense.

**The core — what Eidos itself needs** (present on every item; `flavor` absent means the collection's default, `connects_to` absent means no canvas edges, a missing `summary` is flagged by the index):

| Name          | Type | Meaning                                                                                                        |
| ------------- | ---- | ------------------------------------------------------------------------------------------------------------- |
| `id`          | Text | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it.                     |
| `title`       | Text | Human-readable name.                                                                                          |
| `summary`     | Text | One plain line — what this item is, in a sentence, distilled from Intent. The source for the collection [`index.md`](#collection-indexes-indexmd) listing; absent, the index flags it. |
| `flavor`      | Text | Which body [flavor](#flavors) this item follows, from its collection's declared flavors. Absent = the collection's default flavor. |
| `owner`       | Text | Who owns the document. Non-owners are warned before editing it (the framework owner aside).                     |
| `connects_to` | List | The items this one connects to on the definition's canvas — each a link, drawn as a directed edge (this → target). The intentional map, distinct from `depends_on`. |

**The seed's custom defaults** — opinionated, not part of what Eidos needs to function, so a framework may reshape, scope, or drop them:

| Name            | Type | Applies To | Meaning                                                                                                  |
| --------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------- |
| `status`        | Text | all        | Current lifecycle value. Baseline: `Draft` \| `Intake` \| `In Progress` \| `Done` \| `Archived` \| `Deprecated`. An off-list value warns, never fails. |
| `date_created`  | Date | all        | `YYYY-MM-DD`. The day the item was first written. Set once.                                              |
| `date_modified` | Date | all        | `YYYY-MM-DD`. The day the item was last changed. Git holds the full history.                             |
| `tags`          | List | all        | Free tags.                                                                                               |
| `domain`        | Text | Specs      | The grouping, matching the item's sub-folder under its collection in the naming convention. An unknown value warns, never fails. |
| `depends_on`    | List | Specs      | Items this one needs, each a link (same markdown form as prose). An implementation dependency, not a canvas edge. |
| `type`          | Text | Specs      | Open, soft category label — drives views and filtering, never structure (see Rule 9). e.g. `feature`, `capability`, `integration`. |

**Custom properties** are added through the `eidos-configure` skill, which presses the owner to decide all four of Name, Type, Applies To, and Meaning — never just a name — then writes the row and backfills the items it applies to. A property nobody thought through is like an item nobody thought through.

**Frontmatter is generated from the Schema.** When an item is scaffolded, its frontmatter is emitted from the properties that apply to its collection — the core, plus any custom property whose Applies To includes that collection — so a new item is born conforming. The shape never carries a frontmatter block of its own.

**Validation is framework-defined.** A skill validating an item reads _that framework's_ Schema (in `Framework.md`) and checks against it — the core properties, plus the custom properties scoped to the item's collection. A missing core property is a real gap in the definition, surfaced Eidos-style: the field is added with a note on why, never the file refused (see [Rules](#rules)).

### Framework

`Framework.md` is the framework's **index and config** — the one place that describes the form rather than any single item. It lives in `_eidos/` because it carries machinery (the version and naming convention), but it is also the authoritative index — so a thin, visible [`README.md`](#start-here-readmemd) at the definition root is the human "start here" that points into it. `Framework.md` has two parts: a small **frontmatter** for the facts tooling parses, and a **body** that indexes the definition — its Top-Level documents, its Collections, and the property [Schema](#properties).

```markdown
---
# The Eidos version this framework targets; eidos-migrate reads and bumps it.
eidos_version: 4.2.1
# How files, folders, and links are named: Title Case | TitleCase | kebab-case. Absent = Title Case.
naming: Title Case
---

# Framework

## Top-Level
<!-- eidos-configure: top-level index (regenerated) -->
- [README](../README.md) — the definition's front door.
- [Roadmap](../Roadmap.md) — where the product is headed, in plain horizons.

## Collections

### Frames

The framing docs — the most primary collection.

- **Leaf:** [Frames/index.md](../Frames/index.md)
- **Flavors:**
  - [architecture](shapes/frame.architecture.md) — the product as a built system (default).
  - [audience](shapes/frame.audience.md) — who it serves, and how each kind differs.
  - [criteria](shapes/frame.criteria.md) — budget, scope objectives, timeline.
  - [market](shapes/frame.market.md) — landscape, positioning, and how it earns.

### Specs

The product's units.

- **Leaf:** [Specs/index.md](../Specs/index.md)
- **Flavors:**
  - [full](shapes/spec.full.md) — the complete spec shape (default).
  - [micro](shapes/spec.micro.md) — Intent, Open Questions, ACs, Out of Scope; grow into full.
- **Domains:**
  - **Identity** — who the user is and how they prove it.
  - **Library** — saving and reading the team's articles.

## Schema

### Eidos Core
<!-- the standard's block: id, title, summary, flavor, owner, connects_to -->

### Custom Properties
| Name   | Type | Applies To | Meaning                        |
| ------ | ---- | ---------- | ------------------------------ |
| status | Text | all        | Lifecycle value.               |
| domain | Text | Specs      | The Specs collection grouping. |
```

- **`eidos_version`** — the version this framework targets. `eidos-migrate` reads it, diffs to the target, and bumps it when done.
- **`naming`** — the convention for human-facing names: `Title Case` (the default), `TitleCase` (no spaces), or `kebab-case` (lowercase, hyphenated). Chosen at `eidos-install`; the skills read it to name and link files. An absent key means `Title Case`. See [Naming](#naming).
- **`## Top-Level`** — the [top-level documents](#top-level-docs): `README` first (the door), then any you add (a Roadmap, a Vision, the generated Framework Map), each a link and a one-line description. The framing docs are not here — they live in the `Frames` collection. The descriptions are the human's and the list is regenerable; the marker comment is where `eidos-configure` rewrites it.
- **`## Collections`** — one `###` per [collection](#collections): a pointer to its generated [`index.md`](#collection-indexes-indexmd) leaf, its [flavors](#flavors) (the default marked), and its grouping (the one-level sub-folders, each with a short description).
- **`## Schema`** — the [property contract](#properties): an `### Eidos Core` block (the standard's, rewritten by `eidos-migrate`) and an `### Custom Properties` block (the framework's — seeded defaults plus your own, each scoped by Applies To). Kept by `eidos-configure`.

The two frontmatter facts are framework-level, not per-item — every item shares them, so stamping each file would only invite drift. The body is the index; `eidos-configure` keeps it current, and `README.md` is the friendly door to it.

## Directory layout

```txt
Blueprint/               # the definition root (found by its _eidos/); name is the default, renameable
  README.md              # the visible "start here" — what this is, and pointers into the definition
  _eidos/                # the framework (hidden) — shapes, personas, Schema, Framework, user, .gitignore
  Frames/                # the framing docs — the most primary collection; declared first in the Framework
    index.md             #   generated leaf listing the frames
    Architecture.md  Audience.md  Criteria.md  Market.md
  Specs/                 # the product's units; declare more collections in the Framework
    index.md             #   generated leaf — the collection's items, grouped by domain
    <Domain>/
      <Title>.md         #     one item per file, grouped by domain (one level of sub-folders)
  Roadmap.md             # a top-level doc — one-of-a-kind, free-form, yours (optional)
```

`Blueprint/` is the overarching root; `Blueprint` is only the default name. Nothing in an item points at the root by path, and the skills locate a definition by its `_eidos/` marker rather than the folder name — so the root may be called anything (`Abstract/`, `Product/`, the product's own name). Domains are the Specs collection's sub-folders (one level); each collection carries a generated [`index.md`](#collection-indexes-indexmd) listing its items. Relationships between items (`depends_on`) live in frontmatter so the folder choice stays low-stakes. One hierarchy on disk, many views from metadata.

If one repository holds several products, nest them as `Blueprint/<name>/...`, each with its own `_eidos/`, top-level docs, and collections.

### Start here (`README.md`)

A definition is read by people who didn't write it — a new teammate, a stakeholder, an agent. So the definition root carries a visible **`README.md`**: a short, friendly "start here" that says what the product is and points into the definition — the [top-level documents](#top-level-docs), the [collections](#collections) and their indexes, and `_eidos/Framework.md` for the full index. It is the front door; the hidden `Framework.md` is the index behind it. Keep it thin — orientation and links, not a second copy of the index — and edit it in place like a top-level doc. `eidos-install` seeds it; it is the one place a human reliably lands first.

### Naming

Everything a human reads in the file tree — top-level docs, collection and sub-folders, and item files — follows the framework's **naming convention**, chosen once at `eidos-install` and recorded as `naming` in [`Framework.md`](#framework). The tree is a table of contents, and the convention decides how it reads:

| Convention | An item file | A domain folder | For |
| --- | --- | --- | --- |
| **Title Case** (default) | `Magic Link Sign-In.md` | `User Management/` | the most readable tree; the original Eidos look |
| **TitleCase** | `MagicLinkSignIn.md` | `UserManagement/` | readable but space-free, for shells and scripts |
| **kebab-case** | `magic-link-signin.md` | `user-management/` | fully lowercase and space-free; the filename _is_ the `id` |

One convention governs the whole definition; pick the one your tooling wants and stay with it. The default is **Title Case** — the two space-free options are for definitions that script over their files or would rather not see `%20` in their links.

A few things hold whichever you choose:

- **The `_eidos/` framework folder is always lowercase** — hidden machinery named the way `.git` is, never following the content convention.
- **The `id` is always kebab-case** (`id: magic-link-signin`): the permanent reference, with the filename only a handle over it. In a kebab-case definition the filename and the `id` coincide; in the other two the filename renders the `title` and the `id` sits inside, so a title can be reworded without disturbing the `id`.
- **The `domain` value matches its folder** in whatever convention the definition uses, so the property and the folder are the same string and matching needs no normalization.
- **Fields meant for tools** (`status`, `type`, `tags`, `flavor`) are not names in the file tree, so they stay as written.

Changing the convention later means renaming the files and folders — a deliberate pass, not a flag you flip — so it is settled at init.

### Referencing other items

Links to other items and sections are encouraged — they read well and you can follow them, where a bare name is neither. Standard markdown links are the best format for compatibility across editors and tools. The link **text** is the human title; the link **path** is the target's filename in the framework's naming convention — so a space-free definition (TitleCase or kebab-case) carries no `%20` in its paths, and only a Title Case definition encodes spaces as `%20`. This extends to the properties that point at other items: `depends_on` holds links too, not bare ids — each item's `id` stays its permanent identity behind them.

## Collections

A **collection** is a top-level folder of repeated units that share a body shape — `Specs/` is the default, and `Frames/` the other Eidos seeds. A framework **declares** its collections in the [Framework](#framework), each with a one-line description, so the set is explicit rather than implied by whatever folders happen to exist.

- **`Specs` is the default.** Every framework has it. It holds the product's units, grouped by domain.
- **`Frames` holds the framing docs.** Architecture, Audience, Criteria, Market — the loose, point-in-time docs that set what every item is judged against. It is an ordinary collection (its flavors are one per kind of frame), **highly encouraged but not required**: a definition may carry none, some, or add its own frame. A flat collection — frames aren't grouped.
- **A framework can add more.** A product often wants another kind of repeated unit — decisions (ADRs), personas, integrations, glossary entries. Declare it as a collection: a folder, a description, and at least one shape. The `eidos-configure` skill scaffolds it (see [AI](#ai)).
- **Each collection owns its shape(s).** This is where Eidos relaxes "one shape per framework": the shape is per-collection, and a collection may offer more than one [flavor](#flavors) of it. What does _not_ change — within a collection, every item follows one of the collection's declared flavors, in a predictable order under set names; a soft category label (if a framework adds one) drives views, never structure.
- **An item's collection is its top-level folder.** A spec under `Specs/` belongs to the Specs collection; an item under another collection's folder belongs to that one. That is how a check knows which shape to validate against.
- **A collection may group its items into one level of sub-folders.** `Specs/` groups by **domain** (`Specs/Identity/`, `Specs/Library/`); another collection might group by something else, or stay flat. **Going more than one level deep is discouraged** — the tree stops reading like a table of contents. `domain` is just the name the Specs collection gives its grouping (required, soft; an unknown value warns, never blocks); another collection's grouping is simply its sub-folders.
- **Each collection has a generated [`index.md`](#collection-indexes-indexmd)** inside its folder — the leaf listing of its items, grouped by sub-folder when it has them, flat when it doesn't. Descriptions live in the Framework, so the index is purely the listing and is rebuilt wholesale by [`eidos-index`](#ai).

## Flavors

A **flavor** is one of a collection's body shapes. A collection has one shape _family_ with one or more flavors, **one marked default**. Flavors let a unit start small and grow — a `micro` spec (Intent, Open Questions, a few acceptance criteria, Out of Scope) that matures into a `full` one — or let a collection carry deliberate variants of the same kind of document.

- **Shape files are named `<kind>.<flavor>.md`**, lowercase and dotted, in `_eidos/shapes/`: `spec.full.md` (the default), `spec.micro.md`, `frame.architecture.md`. Top-level docs have no shape and no flavors — they are one-of-a-kind documents, not collection items.
- **The default flavor is what gets scaffolded.** Authoring a new item starts from the collection's default flavor unless the owner picks another; the choice is recorded in the item's [`flavor`](#properties) property. An absent `flavor` means the default.
- **Validation follows the item's flavor.** A check resolves the item's collection (its top-level folder), reads its `flavor` (or the collection default), finds that flavor's shape, and checks the body against _that_ shape — so a `micro` spec is never faulted for the sections only `full` carries.
- **Flavor is structural; a category label is a view.** A flavor is a deliberate, framework-declared choice of body shape. A soft label a framework might add (a `type`, a `category`) drives views and filtering, never structure. Keeping the two apart is what stops flavors from collapsing back into a forbidden shape-per-category.

Flavors are declared in the [Framework](#framework)'s Collections section — each a link to its shape file with a short description, the default marked. Add one with the `eidos-configure` skill.

## Top-level docs

A **top-level doc** is a one-of-a-kind document at the definition root that you add yourself — a **Roadmap**, a **Vision**, a **Glossary**, a set of **Principles**, or the generated **Framework Map** (the canvas). They are **free-form**: no shape, no flavors, no validation. Each carries only light frontmatter (`title`, `tags`, `date_created`, `date_modified`) and reads like the rest of the definition. They are the loose layer that annotates the whole product — listed in the Framework's `## Top-Level`, and regenerable there by `eidos-configure`.

Top-level docs are point-in-time snapshots of intent and are expected to evolve. Record what is true now; revise when it changes.

The **framing docs** that used to live here — Architecture, Audience, Criteria, Market — are now the [`Frames` collection](#collections): the same loose, point-in-time prose, but held as a collection so each follows a shared shape (its flavor) and carries the frontmatter contract. That is the one place Eidos asks for a little structure, because the framing docs are the frame everything else is judged against. A definition is encouraged to fill them, and a framework is free to add a frame of its own.

A **shape** earns its keep by being instantiated again — the Spec shape is a cookie-cutter, stamped once per item. A top-level doc is filled in **once** and edited in place, so it never needs a shared shape. There are no templates: for a Frame, author it as a collection item against its flavor; for a top-level doc you've already drafted, reach for [`eidos-format`](#ai) to **organize** what you wrote into the house style — readable headings, tables, lists, links over bare names — keeping the frontmatter in order and adding nothing of its own.

## Item body

The body is the guided part of an item — a spec, in the common case — and the frontmatter above is the firm contract. It follows a **shape**: a set of sections, in a set order, under set names, so a reader always knows where to look. The shape is the framework's, held in `_eidos/shapes/` as one or more [flavors](#flavors); the canonical baseline — the sections Eidos ships, each with its guidance — lives in the default flavor [`seed/shapes/spec.full.md`](seed/shapes/spec.full.md), with a lighter [`spec.micro.md`](seed/shapes/spec.micro.md) beside it. The specific sections are documented there, in the shape itself, so a framework can rework its shape without fighting the standard. What this file gives are the rules for using a body:

- **Keep the shape's order and names.** Leave a section out when it genuinely doesn't apply (no empty headings), but don't reorder them, rename them, or invent a parallel layout. A check may note a missing recommended section and offer to fill it; it never refuses the file.
- **One shape family per collection, never per category.** Every item in a collection follows one of its declared [flavors](#flavors); a soft label drives views, not layout.
- **Write it like a human would read it.** Shape the content to fit — add your own `###`/`####` sub-headings, tables, lists, code blocks, or small diagrams wherever they make the meaning clearer, and never flatten rich content onto a single line. A data model reads better as a table than a sentence; a sequence reads better as a numbered list. The result should read like a person wrote it, not a filled-in form.
- **Keep acceptance criteria short and observable.** Label each `**AC1:**`, `**AC2:**`… — unique within the item for reference, not across the definition — and push supporting detail (a data model, a payload, a state table) into a table or sub-section the criterion points to, not onto the line.
- **Lead with intent and what you're getting; hold the line on non-goals.** The baseline shape opens with why the unit exists and its observable outcomes, and leans hardest on what it will _not_ do. Which sections carry each — and how to fill them — are documented in the shape file, not prescribed here.

## Rules

These are the load-bearing conventions.

1. **The frontmatter is the agreement; the body is guidance.** The properties at the top are checked against the framework's Schema. Body sections are recommended structure, not requirements.
2. **The definition owns its framework.** Shapes and properties live in the definition's `_eidos/`, seeded from the opinionated baseline and free to be extended. A skill reads the framework from the definition, not from a copy of its own.
3. **Validation is framework-defined.** A check reads _that framework's_ Schema (the `## Schema` section of `Framework.md`) and enforces it — the core properties plus the custom properties scoped to the item's collection. The contract is the Schema, not a rule hardcoded in a tool.
4. **Portability over prescription.** Recommended sections may be omitted when a doc is in progress or genuinely does not apply. A missing core property is surfaced and added with a note on why; a missing section is noted and offered. Never refuse the file.
5. **Write it like a human would read it.** The recommended sections are a scaffold for a complete, living item — not a form to pour text into. Reshape within and beneath them to fit the content: add your own `###`/`####` sub-headings, tables, lists, code blocks, or small diagrams wherever they make the meaning clearer, and never flatten rich content onto one line. Keep acceptance criteria short and observable; push supporting detail into a table or sub-section the criterion points to. If an item reads like filled-in boilerplate, reshape it until it reads like someone wrote it.
6. **Reference other items with links, not bare names — in prose and in properties.** Point at another item, doc, or section with a markdown link. The same goes for frontmatter that points out, like `depends_on`. Each item's `id` is still its permanent identity, sitting behind the link.
7. **One shape family per collection, declared as flavors.** Within a [collection](#collections) every item follows one of the collection's declared [flavors](#flavors) — a shape held in `_eidos/shapes/`, its sections in the same order under the same names, so a reader always knows where to look. What flexes is _which_ sections appear and _which_ flavor an item uses (recorded in `flavor`), never their order or names within a flavor. A flavor is a deliberate, framework-declared structural choice; a soft category label drives views, never structure — the shape is never forked per category.
8. **Properties carry a type and a meaning.** Every property — core or custom — declares its name, its type (from the Obsidian set), which collections it applies to, and what it means. Frontmatter is generated from the Schema, so a new item is born conforming.
9. **Soft labels are views, not structure.** A category property like `type` is human-chosen; it drives views and filtering, never structure. An off-list value is valid. Eidos seeds `type` as a `Specs` default, but `flavor` — not `type` — carries the structural choice; the shape is never forked per category.
10. **`domain` is the Specs collection's grouping.** Required, soft, descriptive. Matches its sub-folder under `Specs/`. An unknown domain is valid — warn and offer to register it, don't block. Other collections group by their own one-level sub-folders.
11. **`id` is permanent.** Stable, unique, kebab-case, assigned once, never renamed. Rename `title` freely.
12. **Intent is stable; Behaviors & Acceptance Criteria evolve.** Editing behaviors is routine. If Intent changes substantially, ask whether this is a different item.
13. **Out of Scope carries the most weight.** It is where scope management actually happens. The strongest recommended section, but still not a hard gate.
14. **Acceptance Criteria are labeled `AC{n}:`** — in bold, e.g. `**AC1:**`. Unique within an item for reference, not across the whole set.
15. **No work-tracking fields.** No `sprint`, `estimate`, or `assignee`. The moment you add them, an item becomes a task and rots. Bridge to a tracker with a link.
16. **Implementation Notes are intent, not status.** They capture how you mean to build a thing and why — never how far along it is.
17. **`date_created` is set once; `date_modified` tracks the last change.** Both `YYYY-MM-DD`, recommended defaults the seed installs. Git holds the full edit history. The Eidos version is a framework fact, in `Framework.md`, not a per-item property.
18. **Frames and top-level docs are point-in-time.** The framing docs (Criteria, Market, Audience) and any top-level doc capture a snapshot of intent and are expected to evolve.
19. **The human authors; the agent facilitates.** Intent, scope, and decisions stay with the person. An agent formats, supplements, asks, and holds scope; it does not generate finished items or set direction.
20. **Human-facing names follow the framework's naming convention.** Folders, top-level docs, and item files read like a table of contents, in the convention chosen at init — Title Case (default), TitleCase, or kebab-case — recorded as `naming` in `_eidos/Framework.md`. The hidden `_eidos/` framework folder is always lowercase, the exception. The kebab-case `id`, not the filename, is the permanent reference.
21. **The Framework is the framework's index; `README.md` is its door.** `_eidos/Framework.md` holds the framework-level facts (version, naming) in frontmatter and, in its body, the Top-Level documents and the Collections with their flavors and grouping. A thin, visible `README.md` at the definition root is the human start-here that points into it. `eidos-configure` keeps both current.
22. **Read the actor before acting.** The agent reads `_eidos/user.md` — the actor's persona and calibration — and the matching contract in `_eidos/personas/`, and responds accordingly: the vocabulary, the technical depth, what it surfaces, and who it asks to decide all follow the persona (a Designer gets experience terms, not db indexes; a Developer gets full depth; the Framework Owner is brought the decisions). The human-first principle holds for every persona; only the mode changes. A blank or absent file defaults to full facilitation. The file is personal and gitignored, never shared.
23. **Each collection has a generated index.** Content is organized into collections (`Specs` is the default); a collection may group its items one level deep (`Specs` by domain), and each carries a generated `index.md` leaf inside its folder, rebuilt by `eidos-index`. Going more than one level deep is discouraged.
24. **Shapes are for collections; top-level docs have none.** A collection's items share a body **shape** (with flavors), in `_eidos/shapes/`, that every item follows and a check validates against — `Frames` included, its flavors one per kind of framing doc. A top-level doc is one-of-a-kind, free-form prose: no shape, no flavors, not validated, edited in place.

## Collection indexes (`index.md`)

Each collection carries a generated **`index.md`** inside its folder — the leaf a human or agent reads to find an item without scraping the tree. It lists the collection's items, grouped under their one-level sub-folders when the collection has them (`Specs` by domain), or as a flat list when it doesn't. Each item is a markdown link with its one-line `summary` property.

```markdown
# Specs

<!-- eidos-index: Specs (regenerated) -->

## Identity
- [Magic Link Sign-In](Identity/Magic%20Link%20Sign-In.md) — passwordless sign-in by an emailed single-use link.
- [Session Management](Identity/Session%20Management.md) — keep a signed-in user across visits, and let them end access on a device.

## Library
- [Saved Articles](Library/Saved%20Articles.md) — save an article by URL; the team gets a readable, reliable copy.
```

- **Fully generated and mechanical.** [`eidos-index`](#ai) crawls the collection, groups by sub-folder, and rebuilds the links — each item's listing is its `summary` property, so the index is derived, not authored. The folder descriptions live in the [Framework](#framework), so the index is purely the listing — regenerated wholesale, with nothing hand-written to preserve. Re-run it whenever items are added, renamed, or moved. The skill ships a `build-index.py` that regenerates every index deterministically wherever a shell is available.
- **Links are relative to the collection folder** (`Identity/…`, not `Specs/Identity/…`), since the index sits with its items.
- **Each line is the item's `summary`** — navigation, not the item itself. The item stays the source of truth; an item with no `summary` yet is flagged, not invented.
- Like everything in Eidos, an index annotates and navigates; it never gates.

The **canvas** is the spatial counterpart of the index — a generated Obsidian `.canvas` map produced by [`eidos-canvas`](#ai). Specs become cards embedding their Intent, `Frames` become full-file cards in their own group, sub-folders become nested groups, and each item's [`connects_to`](#properties) links are drawn as directed edges — the intentional map of how the product's pieces relate (with `depends_on` optionally overlaid in a distinct color). The generated `.canvas` is itself a [top-level doc](#top-level-docs); register it in the Framework's `## Top-Level`. Like the index, it is derived, regenerable, and never gates.

## Versioning

- Semantic Versioning (`MAJOR.MINOR.PATCH`). Major bumps for breaking changes, minor for backward-compatible additions, patch for clarifications.
- This file always holds the current version — right now, 4.2.1. When a version is tagged, this file is copied as-is into `versions/` under its full semver name (e.g. `versions/v3.0.0.md`). Each release is frozen there, so any two — even non-adjacent — can be diffed to migrate items between them (see the `eidos-migrate` skill).
- A framework records the version it targets in its `_eidos/Framework.md`; migration reads and bumps it there.
- See `CHANGELOG.md` for history and migrations.
- Tools may reject if the version in this file is unsupported.

## AI

_This section is for an AI assistant working in an Eidos definition. A human can stop above — the rest is operating detail._

Eidos gives the direction; **the skills and a seeded definition are how the work gets done.** Earlier versions promised that Eidos worked from this file alone — 3.0.0 retires that. The framework a definition uses now lives in the definition itself (`_eidos/`), so doing Eidos means a human, the skills, and a `_eidos/` that has been set up. Prefer the skills: `eidos` to author and validate, `eidos-install` to scaffold, `eidos-configure` to add a collection or flavor, add or change a custom property, and keep the Framework index current, `eidos-index` to rebuild a collection's `index.md`, `eidos-whoami` to set who you are, `eidos-migrate` to upgrade versions.

**Facilitate, don't author.** Eidos is human-first. Format and structure what the owner gives you, supplement, ask clarifying questions, and press on Out of Scope — but never invent Intent, decide direction, or hand back a finished item to rubber-stamp. When unsure, ask. An item the owner didn't think through is worse than none.

**Read the actor first.** Before acting, read `_eidos/user.md` — the actor's persona and calibration (role, experience with the scope, technical capacity) — and the matching contract in `_eidos/personas/`. Respond to _that_ actor: a Designer gets experience terms and no db/index jargon; a Developer gets full technical depth; the Framework Owner is brought the decisions; a Stakeholder gets summary and risk; a Project Manager gets scope, status, and dependencies. Calibration tunes the baseline — less orientation for the experienced, less mechanism for the non-technical. A blank or absent file means full, framework-owner-style facilitation; offer to set it with `eidos-whoami`. The human-first principle holds for every persona.

**Find the framework in the definition.** Locate a definition by its `_eidos/` marker, not the folder name — the root may be called anything (`Blueprint` is just the default). Every operation reads that `_eidos/`: `shapes/` for the collection body shapes (one or more flavors each, `Frames` included), `personas/` for the response contracts, `Framework.md` for the version, the naming convention, the Top-Level/Collections index, and the property Schema (its `## Schema` section), and `user.md` for the actor. If a folder has no `_eidos/`, it is not yet an Eidos definition — offer to install a framework with `eidos-install`. Do not fall back to a hardcoded contract; the definition's framework is the source of truth.

**Start at `README.md`, then the Framework.** The root `README.md` is the visible front door — what the product is and where to go. `_eidos/Framework.md` is the full index: the Top-Level documents and the Collections with their flavors and grouping. Each collection's `index.md` is its leaf listing — items grouped by sub-folder, links with one-line summaries. Read these to navigate instead of scraping the tree; regenerate the Framework with `eidos-configure` and the collection indexes with `eidos-index` when they go stale.

**Authoring an item:**

1. Read the definition's `_eidos/Framework.md` for the property Schema, the naming convention, and the collection's flavors. Determine the target collection (its top-level folder) and pick a flavor — the collection's default unless the owner chooses another — then read that flavor's shape (`_eidos/shapes/<kind>.<flavor>.md`, e.g. `spec.full.md`) for the body. Name the file for its title in that convention (Title Case by default); put a permanent kebab-case `id` inside.
2. Generate the frontmatter from the properties that apply to the item's collection — the core, plus any custom property scoped to it; fill values from what the owner tells you; set `date_created`/`date_modified` to today, and set `flavor` when it isn't the collection's default. Don't guess a `status` or invent an `owner`.
3. Lead with **Intent** and **Behaviors & Acceptance Criteria** — short, observable criteria labeled `**AC1:**`, `**AC2:**`… Press hard on **Out of Scope**. Capture the rest as it surfaces; omit a section that doesn't apply, but keep the shape's order and names.
4. Where the owner is vague, ask — don't fill the gap with plausible prose. Push rich detail (a data model, a payload) into a table or sub-section rather than onto an AC line.

**Authoring a Frame:** a framing doc (Architecture, Audience, Criteria, Market) is a `Frames` collection item — author it like any item: frontmatter from the Schema, body from the matching flavor shape (`frame.architecture.md`, …). Prose, loose, point-in-time — fill what's known, leave the rest. **Authoring a top-level doc:** a Roadmap, a Vision, or the generated Framework Map is one-of-a-kind and free-form — no shape and none required. Write it with the light top-level-doc frontmatter (`title`, `tags`, `date_created`, `date_modified`), and reach for `eidos-format` to organize a rough draft into the house style.

**Validating an item:** read the framework's Schema (in `Framework.md`) and check the frontmatter against it — the core properties present and well-formed (`id` kebab-case, the two dates as `YYYY-MM-DD`; a `status` off the baseline warns, never fails), plus the custom properties scoped to the item's collection. Report missing body sections as suggestions **against the item's flavor shape** — resolve its collection (top-level folder) and its `flavor` (or the collection default), so a `micro` item isn't faulted for the sections only `full` carries — flagging an absent **Out of Scope** first, and note acceptance criteria that lack `**AC{n}:**` labels. Confirm no work-tracking fields crept in and that Implementation Notes read as intent, not progress. Surface, don't block — the output is a review the human acts on, and a missing core property is added with a note on why rather than failing the file.

**Linking other items:** a relative markdown link whose path is the target's filename in the framework's naming convention — `[Session Management](../Identity/Session%20Management.md)` in a Title Case definition (spaces as `%20`), `[Session Management](../Identity/SessionManagement.md)` in a TitleCase one, `[Session Management](../Identity/session-management.md)` in a kebab-case one. The link text stays the human title. Add a `#heading` anchor for a section (GitLab/GitHub lowercase-and-hyphenate the heading; an Obsidian vault uses the literal heading text). Linking properties like `depends_on` use the same link, one markdown-link string per entry — quote it in YAML, since a leading `[` starts a list:

```yaml
depends_on:
  - "[Session Management](../Identity/Session%20Management.md)"
```

The linked item's `id` is its permanent identity. If a dependency has no item yet, name it plainly — a bare `id` in `depends_on`, no fabricated link.
