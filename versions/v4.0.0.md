# Eidos

**Version:** 4.0.0

The Eidos standard — a markdown spec registry where one file completely defines one unit of a product, true whether or not the thing has been built. This file is the method: what a spec is, how a registry is shaped, and how the pieces fit. It gives the direction; the skills and a seeded registry are how you actually do the work (see [AI](#ai)).

## What a spec is

A **spec** is a living markdown document that defines one unit of a product completely: "this is what you're getting," with no ambiguity. A spec is true whether or not the thing it describes has been built. It captures **state and intent, not work**. Tasks describe work and die when the work ships; a spec describes the product and stays accurate across its whole life: drafted, built, deprecated.

A spec has two parts: a small **frontmatter** (the properties at the top, between the `---` lines) and a **body** (the prose below). The frontmatter is a contract; the body follows a shape. Both are defined by the registry itself, in its [form layer](#the-form-layer) — not hardcoded here.

A spec is the default unit Eidos defines, and the rest of this file teaches from it — but it isn't the whole of Eidos. A registry organizes its units into [collections](#collections) (`Specs` is the one Eidos seeds) and may define others, each with its own shape; "spec" and "domain" are the default seed, not the essence.

## A human-first standard

Eidos is a tool for a person — typically a product owner — to think clearly about what their product is. It is not a way to hand product definition to an AI. The human holds the intent, the scope, and the decisions; those are the parts of the job that cannot be delegated without the product owner losing the thread of their own product.

An agent's role is **facilitation, not authorship**. It formats, supplements, fills in shapes, asks clarifying questions, and pushes on scope (especially Out of Scope). It does not invent intent, decide direction, or generate a finished spec for a human to rubber-stamp. A spec the owner did not actually think through is worse than no spec: it reads as settled, but no one knows it. When in doubt, an agent asks rather than writes. The measure of a good Eidos session is that the human understands and stands behind every line — not that a lot of text appeared.

Eidos is opinionated but not rigid. It ships a strong default — the shapes and properties below — and then lets a registry supplement or change them. You adopt without forking, customize without leaving the standard, and still migrate, because the parts Eidos owns stay versioned while the parts you add are preserved.

## The actor

Eidos is human-first, and not every human in a registry plays the same part — a product owner decides, a developer builds, a stakeholder reviews, a designer shapes the experience. The agent must respond to each **differently**, so the actor is a core input it reads **before acting**, in two pieces:

- **Personas** (`.eidos/personas/`) — the response contracts, one per role. A persona sets the **vocabulary and technical depth**, **what to surface vs. fold away**, and **who holds which decisions**: the Designer persona keeps db relationships and indexes out of the reply and talks in experience terms; the Developer persona invites full technical depth; the Product Owner persona brings the decisions to the owner and never decides for them. They are committed and team-tunable, seeded from the standard's [`personas/`](personas), so a team can adjust how a role is treated for their product.
- **The actor file** (`.eidos/user.md`) — personal and **gitignored**, one per person. It names the actor's persona and **calibrates** it on three axes: their **role for this product**, their **experience with the scope** (how much orientation to give), and their **technical capacity** (how much mechanism and jargon to use). Persona sets the baseline; calibration tunes it for the person. Set it with the [`eidos-whoami`](#ai) skill; it ships blank, and `eidos-init` seeds a `.gitignore` so it never lands in anyone else's checkout.

The persona changes the mode, not the principle: whoever the actor, the human authors and decides and the agent facilitates. A blank or absent `user.md` is fine — the agent defaults to full, product-owner-style facilitation and offers to record who you are; it never gates. A persona is a baseline, not a cage — an actor may write a custom role, and a registry may add or reshape its personas. The five Eidos ships are **Product Owner**, **Developer**, **Stakeholder**, **Designer**, and **Project Manager**; their full contracts live in [`personas/`](personas).

## Two kinds of document

Eidos holds two kinds of document. They behave differently on purpose.

- **Top-level docs** — one of each, at the top of the product. Eidos ships four — `Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md` — and a registry adds its own (a Roadmap, a Vision). They are prose, deliberately loose, and point-in-time, and they set the frame every unit is judged against: who it serves, what it must respect, where it sits in the market, what it can afford (see [Top-level docs](#top-level-docs)).
- **Collections** are the many. A **collection** is a folder of repeated units that share a body shape; a registry can have several, and may group a collection's units one level deep. A unit is a small frontmatter contract plus a body in a [shape](#the-form-layer) — and a collection can offer more than one shape, a [flavor](#flavors). Eidos seeds one collection — `Specs`, grouped by `domain` — because most products start there, but the collections are the registry's to define (see [Collections](#collections)).

Top-level docs drive decisions and audit scope; the collections capture the units that result. When defining the _whole product_, reach for a top-level doc. When defining a _piece_ of it, reach for the right collection — a spec, by default.

## The form layer

A registry is two things: **content** and **form**.

- **Content** is what you write — the top-level docs and the collections' units. It is visible, Title Case, and reads like a table of contents.
- **Form** is what governs the content's shape — the body **shapes** for a collection's items, the **templates** for the top-level docs, the property contract, and the response contracts (personas). It is machinery. It lives in a hidden **`.eidos/`** folder at the registry root, named the way `.git` and `.obsidian` are: present, manageable, but out of the way once set. An Eidos registry is plausibly an Obsidian vault, and `.eidos/` sits beside `.obsidian/`.

```txt
.eidos/
  shapes/          # collection body shapes (flavored, shared, validated against)
    spec.full.md   # the Specs collection's default flavor
    spec.micro.md  # a lighter flavor of the same, to grow into full
  templates/       # one-of-each top-level-doc templates (no flavors; scaffold + intended-form record)
    Architecture.md
    Audience.md
    Criteria.md
    Market.md
  personas/        # response contracts — how the agent treats each role (committed, tunable)
    product-owner.md
    developer.md
    stakeholder.md
    designer.md
    project-manager.md
  Schema.md        # the property contract: canonical (Eidos's) + custom (yours)
  Registry.md      # the registry's index + config: version, naming, Top-Level, Collections
  user.md          # who is in the seat: persona + calibration (personal, gitignored)
  .gitignore       # ignores user.md — the one file in here not committed
```

The registry owns its form. Eidos seeds `.eidos/` with the opinionated baseline (`eidos-init`), and from there the owner may extend it — add a property, adjust a shape or template — without leaving the standard. This is what makes Eidos adoptable without a fork: the default works out of the box, and the parts you change are yours.

Because the form lives in the registry, the skills read it from there rather than carrying their own copy. A registry that calls itself Eidos has a `.eidos/`; a skill that finds none offers to install one (see [AI](#ai)).

### Shapes (`.eidos/shapes/`)

A **shape** is the body template a **collection's** items share — body only (the sections in their order, with their guidance), because an item's frontmatter is generated from the [Schema](#properties-eidosschemamd), not written by hand. A shape is the **shared, ongoing form of the many**: every item in the collection follows it, and a check validates against it. A collection may offer more than one shape of its body — a [flavor](#flavors) — each its own file named `<kind>.<flavor>.md` (`spec.full.md`, `spec.micro.md`).

### Templates (`.eidos/templates/`)

A **template** is the starting scaffold for a **top-level doc** — one per canonical doc, named for it (`Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md`), carrying that doc's own light frontmatter inline. Unlike a shape, a template is **not shared or validated**: a top-level doc is one-of-a-kind, scaffolded from its template once and then edited in place, and it has **no flavors**. The templates stay in `.eidos/templates/` as the **record of each doc's intended full form** — so a top-level doc that is still a stub or **in progress** can be filled out against its template, and the registry keeps the intention to complete it. (A custom top-level doc — a Roadmap, a Vision — gets no template; it is free-form, organized by `eidos-format`.)

The canonical shapes Eidos ships — the opinionated baseline — live, public and browsable, in [`standard-seed/shapes/`](standard-seed/shapes) at the top of the standard's repo; `eidos-init` installs them into a registry's `.eidos/`. A registry may then reshape its own, add flavors, and the skills consume whatever it holds. The shape files are where the specific sections are documented; [Spec body](#spec-body) below gives the rules for using them.

### Properties (`.eidos/Schema.md`)

`Schema.md` is the property contract — what a spec's frontmatter must and may carry. It is one markdown file in two parts:

- **`## Eidos Canonical`** — the properties Eidos defines for this version. Managed by the standard; `eidos-migrate` rewrites this block on a version change. Don't hand-edit it.
- **`## Custom Registry Properties`** — the properties this registry adds for its own use. Yours; preserved across migration.

Each property is a row: **name · type · required · meaning**. A property's `type` is drawn from the same small set Obsidian uses — **Text, List, Number, Checkbox, Date, Date & time** — so a registry's frontmatter renders natively in an Obsidian vault. Anything that wants more structure than one of those types almost belongs in the body (the shape), not in a property.

The canonical baseline (4.0.0 adds the optional `flavor`):

| Property     | Type | Required | Meaning                                                                                                        |
| ------------ | ---- | -------- | ------------------------------------------------------------------------------------------------------------- |
| `id`         | Text | yes      | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it.                     |
| `title`      | Text | yes      | Human-readable name. Rename freely.                                                                            |
| `type`       | Text | yes      | Open, soft label. Human-chosen. Drives views, never structure. Suggested: `feature`, `capability`, `domain`, `integration`. |
| `domain`     | Text | yes      | The grouping, matching its folder under `Specs/` in the registry's naming convention. An unknown domain is valid (warn only). |
| `flavor`     | Text | no       | Which body [flavor](#flavors) this item follows, from its collection's declared flavors. Absent = the collection's default flavor. |
| `status`     | Text | yes      | Current lifecycle value. Suggested baseline: `Draft` \| `Intake` \| `In Progress` \| `Done` \| `Archived` \| `Deprecated`. An off-list value warns, never fails. |
| `created`    | Date | yes      | `YYYY-MM-DD`. The day the spec was first written. Set once.                                                    |
| `modified`   | Date | yes      | `YYYY-MM-DD`. The day the spec was last changed. Git holds the full history.                                   |
| `owner`      | Text | no       | Who answers questions about this spec.                                                                         |
| `depends_on` | List | no       | Specs this one needs, each a link to that spec (same markdown form as prose).                                  |
| `tags`       | List | no       | Free tags.                                                                                                     |

**Custom properties** are added through the `eidos-property` skill, which presses the owner to decide all four of name, type, required, and meaning — never just a name — then writes the row and backfills the existing specs. A property nobody thought through is like a spec nobody thought through.

**Frontmatter is generated from the Schema.** When a spec is scaffolded, its frontmatter is emitted from the Schema's required properties (canonical plus any custom-required), so a new spec is born conforming. The shape never carries a frontmatter block of its own.

**Validation is registry-defined.** A skill validating a spec reads _that registry's_ `Schema.md` and checks against it — the canonical required properties plus whatever the registry marked required. A missing required property is a real gap within the registry, surfaced Eidos-style: the field is added with a note on why, never the file refused (see [Rules](#rules)).

### Registry (`.eidos/Registry.md`)

`Registry.md` is the registry's **index and config** — the one place that describes the whole registry rather than any single spec. It lives in `.eidos/` because it carries machinery (the version and naming convention), but it is also the authoritative index — so a thin, visible [`README.md`](#start-here-readmemd) at the registry root is the human "start here" that points into it. `Registry.md` has two parts: a small **frontmatter** for the facts tooling parses, and a **body** that indexes the registry.

```markdown
---
# The Eidos version this registry targets; eidos-migrate reads and bumps it.
eidos_version: 4.0.0
# How files, folders, and links are named: Title Case | TitleCase | kebab-case. Absent = Title Case.
naming: Title Case
---

# Registry

## Top-Level
<!-- eidos-registry: top-level index (regenerated) -->
- [Architecture](../Architecture.md) — the system as a built whole.
- [Audience](../Audience.md) — who it serves and how each kind of user differs.

## Collections

### Specs

The product's units.

- **Leaf:** [Specs/index.md](../Specs/index.md)
- **Flavors:**
  - [full](shapes/spec.full.md) — the complete spec shape (default).
  - [micro](shapes/spec.micro.md) — Intent, Open Questions, ACs, Out of Scope; grow into full.
- **Domains:**
  - **Identity** — who the user is and how they prove it.
  - **Library** — saving and reading the team's articles.
```

- **`eidos_version`** — the version this registry targets. `eidos-migrate` reads it, diffs to the target, and bumps it when done.
- **`naming`** — the convention for human-facing names: `Title Case` (the default), `TitleCase` (no spaces), or `kebab-case` (lowercase, hyphenated). Chosen at `eidos-init`; the skills read it to name and link files. An absent key means `Title Case`. See [Naming](#naming).
- **`## Top-Level`** — the [top-level documents](#top-level-docs) (the four Eidos ships and any the registry adds), each a link and a one-line description. The descriptions are the human's and the list is regenerable; the marker comment is where `eidos-registry` rewrites it.
- **`## Collections`** — one `###` per [collection](#collections): a pointer to its generated [`index.md`](#collection-indexes-indexmd) leaf, its [flavors](#flavors) (the default marked), and its grouping (the one-level sub-folders, each with a short description).

The two frontmatter facts are registry-level, not per-spec — every spec shares them, so stamping each file would only invite drift. The body is the index; `eidos-registry` keeps it current, and `README.md` is the friendly door to it.

## Directory layout

```txt
Blueprint/               # the registry root (found by its .eidos/); name is the default, renameable
  README.md              # the visible "start here" — what this is, and pointers into the registry
  .eidos/                # the form layer (hidden) — shapes, personas, Schema, Registry, user, .gitignore
  Architecture.md        # overarching system shape, one entry door
  Audience.md            # who it serves and how each type interacts
  Criteria.md            # budget, scope objectives, timeline
  Market.md              # where it sits, how it differs, how it earns
  Specs/                 # the default collection; declare more in the Registry
    index.md             # generated leaf — the collection's specs, grouped by domain
    <Domain>/
      <Title>.md         # one spec per unit, grouped by domain (one level of sub-folders)
  Arch/                  # optional, only when architecture detail outgrows one file
```

`Blueprint/` is the overarching root; `Blueprint` is only the default name. Nothing in a spec points at the root by path, and the skills locate a registry by its `.eidos/` marker rather than the folder name — so the root may be called anything (`Abstract/`, `Product/`, the product's own name). Domains are the Specs collection's sub-folders (one level); each collection carries a generated [`index.md`](#collection-indexes-indexmd) listing its items. Relationships between specs (`depends_on`) live in frontmatter so the folder choice stays low-stakes. One hierarchy on disk, many views from metadata.

If one repository holds several products, nest them as `Blueprint/<name>/...`, each with its own `.eidos/`, top-level docs, and collections.

### Start here (`README.md`)

A registry is read by people who didn't write it — a new teammate, a stakeholder, an agent. So the registry root carries a visible **`README.md`**: a short, friendly "start here" that says what the product is and points into the registry — the [top-level documents](#top-level-docs), the [collections](#collections) and their indexes, and `.eidos/Registry.md` for the full index. It is the front door; the hidden `Registry.md` is the index behind it. Keep it thin — orientation and links, not a second copy of the index — and edit it in place like a top-level doc. `eidos-init` seeds it; it is the one place a human reliably lands first.

### Naming

Everything a human reads in the file tree — top-level docs, collection and sub-folders, and item files — follows the registry's **naming convention**, chosen once at `eidos-init` and recorded as `naming` in [`Registry.md`](#registry-eidosregistrymd). The tree is a table of contents, and the convention decides how it reads:

| Convention | A spec file | A domain folder | For |
| --- | --- | --- | --- |
| **Title Case** (default) | `Magic Link Sign-In.md` | `User Management/` | the most readable tree; the original Eidos look |
| **TitleCase** | `MagicLinkSignIn.md` | `UserManagement/` | readable but space-free, for shells and scripts |
| **kebab-case** | `magic-link-signin.md` | `user-management/` | fully lowercase and space-free; the filename _is_ the `id` |

One convention governs the whole registry; pick the one your tooling wants and stay with it. The default is **Title Case** — the two space-free options are for registries that script over their files or would rather not see `%20` in their links.

A few things hold whichever you choose:

- **The `.eidos/` form layer is always lowercase** — hidden machinery named the way `.git` is, never following the content convention.
- **The `id` is always kebab-case** (`id: magic-link-signin`): the permanent reference, with the filename only a handle over it. In a kebab-case registry the filename and the `id` coincide; in the other two the filename renders the `title` and the `id` sits inside, so a title can be reworded without disturbing the `id`.
- **The `domain` value matches its folder** in whatever convention the registry uses, so the property and the folder are the same string and matching needs no normalization.
- **Fields meant for tools** (`status`, `type`, `tags`) are not names in the file tree, so they stay as written.

Changing the convention later means renaming the files and folders — a deliberate pass, not a flag you flip — so it is settled at init.

### Referencing other specs

Links to other specs and sections are encouraged — they read well and you can follow them, where a bare name is neither. Standard markdown links are the best format for compatibility across editors and tools. The link **text** is the human title; the link **path** is the target's filename in the registry's naming convention — so a space-free registry (TitleCase or kebab-case) carries no `%20` in its paths, and only a Title Case registry encodes spaces as `%20`. This extends to the properties that point at other specs: `depends_on` holds links too, not bare ids — each spec's `id` stays its permanent identity behind them.

## Collections

A **collection** is a top-level folder of repeated units that share a body shape — `Specs/` is the one Eidos ships, and the default. A registry **declares** its collections in the [Registry](#registry-eidosregistrymd), each with a one-line description, so the set is explicit rather than implied by whatever folders happen to exist.

- **`Specs` is the default.** Every registry has it. It holds the product's units.
- **A registry can add more.** A product often wants another kind of repeated unit — decisions (ADRs), personas, integrations, glossary entries. Declare it as a collection: a folder, a description, and at least one shape. The `eidos-registry` skill scaffolds it (see [AI](#ai)).
- **Each collection owns its shape(s).** This is where Eidos relaxes "one shape per registry": the shape is per-collection, and a collection may offer more than one [flavor](#flavors) of it. What does _not_ change — within a collection, every item follows one of the collection's declared flavors, in a predictable order under set names; `type` still drives views, never structure.
- **An item's collection is its top-level folder.** A spec under `Specs/` belongs to the Specs collection; an item under another collection's folder belongs to that one. That is how a check knows which shape to validate against.
- **A collection may group its items into one level of sub-folders.** `Specs/` groups by **domain** (`Specs/Identity/`, `Specs/Library/`); another collection might group by something else, or stay flat. **Going more than one level deep is discouraged** — the tree stops reading like a table of contents. `domain` is just the name the Specs collection gives its grouping (required, soft; an unknown value warns, never blocks); another collection's grouping is simply its sub-folders.
- **Each collection has a generated [`index.md`](#collection-indexes-indexmd)** inside its folder — the leaf listing of its items, grouped by sub-folder when it has them, flat when it doesn't. Descriptions live in the Registry, so the index is purely the listing and is rebuilt wholesale by [`eidos-index`](#ai).

## Flavors

A **flavor** is one of a collection's body shapes. A collection has one shape _family_ with one or more flavors, **one marked default**. Flavors let a unit start small and grow — a `micro` spec (Intent, Open Questions, a few acceptance criteria, Out of Scope) that matures into a `full` one — or let a collection carry deliberate variants of the same kind of document.

- **Shape files are named `<kind>.<flavor>.md`**, lowercase and dotted, in `.eidos/shapes/`: `spec.full.md` (the default), `spec.micro.md`. Top-level docs use [templates](#templates-eidostemplates), not shapes, so they have no flavors — they are one-of-each documents, not collection items.
- **The default flavor is what gets scaffolded.** Authoring a new item starts from the collection's default flavor unless the owner picks another; the choice is recorded in the item's [`flavor`](#properties-eidosschemamd) property. An absent `flavor` means the default.
- **Validation follows the item's flavor.** A check resolves the item's collection (its top-level folder), reads its `flavor` (or the collection default), finds that flavor's shape, and checks the body against _that_ shape — so a `micro` spec is never faulted for the sections only `full` carries.
- **Flavor is structural; `type` is a view.** A flavor is a deliberate, registry-declared choice of body shape. `type` is a soft label that drives views and never structure. Keeping the two apart is what stops flavors from collapsing back into the forbidden shape-per-`type`.

Flavors are declared in the [Registry](#registry-eidosregistrymd)'s Collections section — each a link to its shape file with a short description, the default marked. Add one with the `eidos-registry` skill.

## Top-level docs

A few files at the top of the product that frame the whole thing — one of each. Eidos ships **four** (Architecture, Audience, Criteria, Market), and a registry adds its own (see below). They are prose, deliberately loose, and point-in-time, and each carries a little light frontmatter (`type: system`, `title`, `tags`, `created`, `modified`). They are not bound by a collection's item Schema; they are the loose, special case. The four canonical ones have [templates](#templates-eidostemplates) that hold the full guidance for each; in short:

- **Architecture** — the shape of the product as a built system. When it outgrows one file, expand into an optional `Arch/` folder and keep this as the map.
- **Audience** — who it serves, and how each kind of user differs.
- **Criteria** — what decides and audits scope: budget, scope objectives, timeline.
- **Market** — where it sits, why it is not interchangeable, and how it earns.

Top-level docs are point-in-time snapshots of intent and are expected to evolve. Record what is true now; revise when it changes.

### Your own top-level docs

The four authored docs are the opinionated baseline, not a closed set. A product often wants a top-level doc of its own — a **Roadmap**, a **Vision**, a **Glossary**, a set of **Principles** — and a registry is free to add one. These are **free-form**: unlike the four canonical docs they get no template, and unlike a collection's items no shape and no validation. You write the doc the product needs; Eidos asks only that it carry the same light top-level-doc frontmatter (`type`, `title`, `tags`, `created`, `modified`) and read like the rest of the registry.

A **shape** earns its keep by being instantiated again and again — the Spec shape is a cookie-cutter, stamped once per item, so the whole collection conforms. A top-level doc is filled in **once** and edited in place for the life of the product, so it never needs a shared shape; the canonical four get a one-time **template** only because a blank scaffold helps the very first brain-dump. A doc you have already written doesn't need even that — so for a custom top-level doc Eidos helps the way that actually fits: not a template to fill, but [`eidos-format`](#ai) to **organize** what you wrote into the house style — readable headings, tables, lists, links over bare names — keeping the frontmatter in order and adding nothing of its own.

## Spec body

The body is the guided part of an item — a spec, in the common case — and the frontmatter above is the firm contract. It follows a **shape**: a set of sections, in a set order, under set names, so a reader always knows where to look. The shape is the registry's, held in `.eidos/shapes/` as one or more [flavors](#flavors); the canonical baseline — the sections Eidos ships, each with its guidance — lives in the default flavor [`standard-seed/shapes/spec.full.md`](standard-seed/shapes/spec.full.md), with a lighter [`spec.micro.md`](standard-seed/shapes/spec.micro.md) beside it. The specific sections are documented there, in the shape itself, so a registry can rework its shape without fighting the standard. What this file gives are the rules for using a body:

- **Keep the shape's order and names.** Leave a section out when it genuinely doesn't apply (no empty headings), but don't reorder them, rename them, or invent a parallel layout. A check may note a missing recommended section and offer to fill it; it never refuses the file.
- **One shape family per collection, never per `type`.** Every item in a collection follows one of its declared [flavors](#flavors); `type` drives views, not layout.
- **Write it like a human would read it.** Shape the content to fit — add your own `###`/`####` sub-headings, tables, lists, code blocks, or small diagrams wherever they make the meaning clearer, and never flatten rich content onto a single line. A data model reads better as a table than a sentence; a sequence reads better as a numbered list. The result should read like a person wrote it, not a filled-in form.
- **Keep acceptance criteria short and observable.** Label each `**AC1:**`, `**AC2:**`… — unique within the item for reference, not across the registry — and push supporting detail (a data model, a payload, a state table) into a table or sub-section the criterion points to, not onto the line.
- **Lead with intent and what you're getting; hold the line on non-goals.** The baseline shape opens with why the unit exists and its observable outcomes, and leans hardest on what it will _not_ do. Which sections carry each — and how to fill them — are documented in the shape file, not prescribed here.

## Rules

These are the load-bearing conventions.

1. **The frontmatter is the agreement; the body is guidance.** The properties at the top are checked against the registry's Schema. Body sections are recommended structure, not requirements.
2. **The registry owns its form.** Shapes and properties live in the registry's `.eidos/`, seeded from the opinionated baseline and free to be extended. A skill reads the form from the registry, not from a copy of its own.
3. **Validation is registry-defined.** A check reads _that registry's_ `Schema.md` and enforces it — canonical required properties plus whatever the registry marked required. The contract is the Schema, not a rule hardcoded in a tool.
4. **Portability over prescription.** Recommended sections may be omitted when a doc is in progress or genuinely does not apply. A missing required property is surfaced and added with a note on why; a missing section is noted and offered. Never refuse the file.
5. **Write it like a human would read it.** The recommended sections are a scaffold for a complete, living definition — not a form to pour text into. Reshape within and beneath them to fit the content: add your own `###`/`####` sub-headings, tables, lists, code blocks, or small diagrams wherever they make the meaning clearer, and never flatten rich content onto one line. Keep acceptance criteria short and observable; push supporting detail into a table or sub-section the criterion points to. If a spec reads like filled-in boilerplate, reshape it until it reads like someone wrote it.
6. **Reference other specs with links, not bare names — in prose and in properties.** Point at another spec, doc, or section with a markdown link. The same goes for frontmatter that points out, like `depends_on`. Each spec's `id` is still its permanent identity, sitting behind the link.
7. **One shape family per collection, declared as flavors.** Within a [collection](#collections) every item follows one of the collection's declared [flavors](#flavors) — a shape held in `.eidos/shapes/`, its sections in the same order under the same names, so a reader always knows where to look. What flexes is _which_ sections appear and _which_ flavor an item uses (recorded in `flavor`), never their order or names within a flavor. A flavor is a deliberate, registry-declared structural choice; `type` still drives views, never structure — the shape is never forked per `type`.
8. **Properties carry a type and a meaning.** Every property — canonical or custom — declares its name, its type (from the Obsidian set), whether it is required, and what it means. Frontmatter is generated from the Schema, so a new spec is born conforming.
9. **`type` is an open, soft label.** Humans choose it. It drives views and filtering, never structure. An off-list value is valid.
10. **`domain` is the Specs collection's grouping.** Required, soft, descriptive. Matches its sub-folder under `Specs/`. An unknown domain is valid — warn and offer to register it, don't block. Other collections group by their own one-level sub-folders.
11. **`id` is permanent.** Stable, unique, kebab-case, assigned once, never renamed. Rename `title` freely.
12. **Intent is stable; Behaviors & Acceptance Criteria evolve.** Editing behaviors is routine. If Intent changes substantially, ask whether this is a different spec.
13. **Out of Scope carries the most weight.** It is where scope management actually happens. The strongest recommended section, but still not a hard gate.
14. **Acceptance Criteria are labeled `AC{n}:`** — in bold, e.g. `**AC1:**`. Unique within a spec for reference, not across the whole set.
15. **No work-tracking fields.** No `sprint`, `estimate`, or `assignee`. The moment you add them, a spec becomes a task and rots. Bridge to a tracker with a link.
16. **Implementation Notes are intent, not status.** They capture how you mean to build a thing and why — never how far along it is.
17. **`created` is set once; `modified` tracks the last change.** Both `YYYY-MM-DD`. Git holds the full edit history. The Eidos version is a registry fact, in `Registry.md`, not a per-spec property.
18. **Top-level docs are point-in-time.** Criteria, Market, and Audience capture a snapshot of intent and are expected to evolve.
19. **The human authors; the agent facilitates.** Intent, scope, and decisions stay with the person. An agent formats, supplements, asks, and holds scope; it does not generate finished specs or set direction.
20. **Human-facing names follow the registry's naming convention.** Folders, top-level docs, and item files read like a table of contents, in the convention chosen at init — Title Case (default), TitleCase, or kebab-case — recorded as `naming` in `.eidos/Registry.md`. The hidden `.eidos/` form layer is always lowercase, the exception. The kebab-case `id`, not the filename, is the permanent reference.
21. **The Registry is the registry's index; `README.md` is its door.** `.eidos/Registry.md` holds the registry-level facts (version, naming) in frontmatter and, in its body, the Top-Level documents and the Collections with their flavors and grouping. A thin, visible `README.md` at the registry root is the human start-here that points into it. `eidos-registry` keeps both current.
22. **Read the actor before acting.** The agent reads `.eidos/user.md` — the actor's persona and calibration — and the matching contract in `.eidos/personas/`, and responds accordingly: the vocabulary, the technical depth, what it surfaces, and who it asks to decide all follow the persona (a Designer gets experience terms, not db indexes; a Developer gets full depth; the Product Owner is brought the decisions). The human-first principle holds for every persona; only the mode changes. A blank or absent file defaults to full facilitation. The file is personal and gitignored, never shared.
23. **Each collection has a generated index.** Content is organized into collections (`Specs` is the default); a collection may group its items one level deep (`Specs` by domain), and each carries a generated `index.md` leaf inside its folder, rebuilt by `eidos-index`. Going more than one level deep is discouraged.
24. **Shapes are for collections; top-level docs use templates.** A collection's items share a body **shape** (with flavors), in `.eidos/shapes/`, that every item follows and a check validates against. A top-level doc is scaffolded from a one-of-each **template** in `.eidos/templates/`, then edited in place — no flavors, not validated. The template stays as the record of the doc's intended full form, so a stub or in-progress top-level doc can be completed against it.

## Collection indexes (`index.md`)

Each collection carries a generated **`index.md`** inside its folder — the leaf a human or agent reads to find an item without scraping the tree. It lists the collection's items, grouped under their one-level sub-folders when the collection has them (`Specs` by domain), or as a flat list when it doesn't. Each item is a markdown link with a one-line summary distilled from its Intent.

```markdown
# Specs

<!-- eidos-index: Specs (regenerated) -->

## Identity
- [Magic Link Sign-In](Identity/Magic%20Link%20Sign-In.md) — passwordless sign-in by an emailed single-use link.
- [Session Management](Identity/Session%20Management.md) — keep a signed-in user across visits, and let them end access on a device.

## Library
- [Saved Articles](Library/Saved%20Articles.md) — save an article by URL; the team gets a readable, reliable copy.
```

- **Fully generated.** [`eidos-index`](#ai) crawls the collection, groups by sub-folder, and rebuilds the links and summaries. The descriptions live in the [Registry](#registry-eidosregistrymd), so the index is purely the listing — regenerated wholesale, with nothing hand-written to preserve. Re-run it whenever items are added, renamed, or moved.
- **Links are relative to the collection folder** (`Identity/…`, not `Specs/Identity/…`), since the index sits with its items.
- **Summaries distill each item's own Intent** — navigation, not the definition. The item stays the source of truth.
- Like everything in Eidos, an index annotates and navigates; it never gates.

## Versioning

- Semantic Versioning (`MAJOR.MINOR.PATCH`). Major bumps for breaking changes, minor for backward-compatible additions, patch for clarifications.
- This file always holds the current version — right now, 4.0.0. When a version is tagged, this file is copied as-is into `versions/` under its full semver name (e.g. `versions/v3.0.0.md`). Each release is frozen there, so any two — even non-adjacent — can be diffed to migrate specs between them (see the `eidos-migrate` skill).
- A registry records the version it targets in its `.eidos/Registry.md`; migration reads and bumps it there.
- See `CHANGELOG.md` for history and migrations.
- Tools may reject if the version in this file is unsupported.

## AI

_This section is for an AI assistant working in an Eidos registry. A human can stop above — the rest is operating detail._

Eidos gives the direction; **the skills and a seeded registry are how the work gets done.** Earlier versions promised that Eidos worked from this file alone — 3.0.0 retires that. The form a registry uses now lives in the registry itself (`.eidos/`), so doing Eidos means a human, the skills, and a `.eidos/` that has been set up. Prefer the skills: `eidos` to author and validate, `eidos-init` to scaffold, `eidos-property` to add or change a custom property, `eidos-registry` to add a collection or flavor and keep the Registry index current, `eidos-index` to rebuild a collection's `index.md`, `eidos-whoami` to set who you are, `eidos-migrate` to upgrade versions.

**Facilitate, don't author.** Eidos is human-first. Format and structure what the owner gives you, supplement, ask clarifying questions, and press on Out of Scope — but never invent Intent, decide direction, or hand back a finished spec to rubber-stamp. When unsure, ask. A spec the owner didn't think through is worse than none.

**Read the actor first.** Before acting, read `.eidos/user.md` — the actor's persona and calibration (role, experience with the scope, technical capacity) — and the matching contract in `.eidos/personas/`. Respond to _that_ actor: a Designer gets experience terms and no db/index jargon; a Developer gets full technical depth; the Product Owner is brought the decisions; a Stakeholder gets summary and risk; a Project Manager gets scope, status, and dependencies. Calibration tunes the baseline — less orientation for the experienced, less mechanism for the non-technical. A blank or absent file means full, product-owner-style facilitation; offer to set it with `eidos-whoami`. The human-first principle holds for every persona.

**Find the form in the registry.** Locate a registry by its `.eidos/` marker, not the folder name — the root may be called anything (`Blueprint` is just the default). Every operation reads that `.eidos/`: `Schema.md` for the property contract, `shapes/` for the collection body shapes (one or more flavors each), `templates/` for the top-level-doc templates, `personas/` for the response contracts, `Registry.md` for the version, the naming convention, and the Top-Level/Collections index, and `user.md` for the actor. If a registry has no `.eidos/`, it is not yet an Eidos registry — offer to install one with `eidos-init`. Do not fall back to a hardcoded contract; the registry's form is the source of truth.

**Start at `README.md`, then the Registry.** The root `README.md` is the visible front door — what the product is and where to go. `.eidos/Registry.md` is the full index: the Top-Level documents and the Collections with their flavors and grouping. Each collection's `index.md` is its leaf listing — items grouped by sub-folder, links with one-line summaries. Read these to navigate instead of scraping the tree; regenerate the Registry with `eidos-registry` and the collection indexes with `eidos-index` when they go stale.

**Authoring a spec:**

1. Read the registry's `.eidos/Schema.md` for the property contract and `.eidos/Registry.md` for the naming convention and the collection's flavors. Determine the target collection (its top-level folder) and pick a flavor — the collection's default unless the owner chooses another — then read that flavor's shape (`.eidos/shapes/<kind>.<flavor>.md`, e.g. `spec.full.md`) for the body. Name the file for its title in that convention (Title Case by default); put a permanent kebab-case `id` inside.
2. Generate the frontmatter from the Schema's required properties (canonical plus any custom-required); fill values from what the owner tells you; set `created`/`modified` to today, and set `flavor` when it isn't the collection's default. Don't guess a `status` or invent an `owner`.
3. Lead with **Intent** and **Behaviors & Acceptance Criteria** — short, observable criteria labeled `**AC1:**`, `**AC2:**`… Press hard on **Out of Scope**. Capture the rest as it surfaces; omit a section that doesn't apply, but keep the shape's order and names.
4. Where the owner is vague, ask — don't fill the gap with plausible prose. Push rich detail (a data model, a payload) into a table or sub-section rather than onto an AC line.

**Authoring a top-level doc:** for one of the four canonical docs (Architecture, Audience, Criteria, Market), start from its template in `.eidos/templates/`. Prose, loose, point-in-time — fill what's known, leave the rest. The template stays as the record of the doc's intended full form, so a stub can be completed against it later. For one the product needs beyond the four — a Roadmap, a Vision — there is no shape and none is required: write it free-form with the light top-level-doc frontmatter, and reach for `eidos-format` to organize a rough draft into the house style without checking it against a template.

**Validating a spec:** read the registry's `Schema.md` and check the frontmatter against it — required properties present and well-formed (`id` kebab-case, `created`/`modified` as `YYYY-MM-DD`; a `status` off the baseline warns, never fails), plus any custom-required property the Schema declares. Report missing body sections as suggestions **against the item's flavor shape** — resolve its collection (top-level folder) and its `flavor` (or the collection default), so a `micro` item isn't faulted for the sections only `full` carries — flagging an absent **Out of Scope** first, and note acceptance criteria that lack `**AC{n}:**` labels. Confirm no work-tracking fields crept in and that Implementation Notes read as intent, not progress. Surface, don't block — the output is a review the human acts on, and a missing required property is added with a note on why rather than failing the file.

**Linking other specs:** a relative markdown link whose path is the target's filename in the registry's naming convention — `[Session Management](../Identity/Session%20Management.md)` in a Title Case registry (spaces as `%20`), `[Session Management](../Identity/SessionManagement.md)` in a TitleCase one, `[Session Management](../Identity/session-management.md)` in a kebab-case one. The link text stays the human title. Add a `#heading` anchor for a section (GitLab/GitHub lowercase-and-hyphenate the heading; an Obsidian vault uses the literal heading text). Linking properties like `depends_on` use the same link, one markdown-link string per entry — quote it in YAML, since a leading `[` starts a list:

```yaml
depends_on:
  - "[Session Management](../Identity/Session%20Management.md)"
```

The linked spec's `id` is its permanent identity. If a dependency has no spec yet, name it plainly — a bare `id` in `depends_on`, no fabricated link.
