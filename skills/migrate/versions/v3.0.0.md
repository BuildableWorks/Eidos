# Eidos

**Version:** 3.0.0

The Eidos standard — a markdown spec registry where one file completely defines one unit of a product, true whether or not the thing has been built. This file is the method: what a spec is, how a registry is shaped, and how the pieces fit. It gives the direction; the skills and a seeded registry are how you actually do the work (see [AI](#ai)).

## What a spec is

A **spec** is a living markdown document that defines one unit of a product completely: "this is what you're getting," with no ambiguity. A spec is true whether or not the thing it describes has been built. It captures **state and intent, not work**. Tasks describe work and die when the work ships; a spec describes the product and stays accurate across its whole life: drafted, built, deprecated.

A spec has two parts: a small **frontmatter** (the properties at the top, between the `---` lines) and a **body** (the prose below). The frontmatter is a contract; the body follows a shape. Both are defined by the registry itself, in its [form layer](#the-form-layer) — not hardcoded here.

## A human-first standard

Eidos is a tool for a person — typically a product owner — to think clearly about what their product is. It is not a way to hand product definition to an AI. The human holds the intent, the scope, and the decisions; those are the parts of the job that cannot be delegated without the product owner losing the thread of their own product.

An agent's role is **facilitation, not authorship**. It formats, supplements, fills in shapes, asks clarifying questions, and pushes on scope (especially Out of Scope). It does not invent intent, decide direction, or generate a finished spec for a human to rubber-stamp. A spec the owner did not actually think through is worse than no spec: it reads as settled, but no one knows it. When in doubt, an agent asks rather than writes. The measure of a good Eidos session is that the human understands and stands behind every line — not that a lot of text appeared.

Eidos is opinionated but not rigid. It ships a strong default — the shapes and properties below — and then lets a registry supplement or change them. You adopt without forking, customize without leaving the standard, and still migrate, because the parts Eidos owns stay versioned while the parts you add are preserved.

## Two kinds of document

Eidos holds two kinds of document. They behave differently on purpose.

- **Product docs** — one of each, at the top of the product: `Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md`, plus a derived `Domains.md` that lists the domains. The four authored docs are prose, deliberately loose, and point-in-time. They set the frame every spec is judged against: who it serves, what it must respect, where it sits in the market, what it can afford.
- **Specs** are the many. One per unit of the product, grouped into domains under `Specs/`. They share one shape — a small frontmatter contract and a set of body sections in a consistent order (see [The form layer](#the-form-layer)).

Product docs drive decisions and audit scope. Specs capture the units that result. When defining a _whole product_, reach for product docs. When defining a _piece_ of it, reach for a spec.

## The form layer

A registry is two things: **content** and **form**.

- **Content** is what you write — the product docs and specs. It is visible, Title Case, and reads like a table of contents.
- **Form** is what governs the content's shape — the body templates and the property contract. It is machinery. It lives in a hidden **`.eidos/`** folder at the registry root, named the way `.git` and `.obsidian` are: present, manageable, but out of the way once set. An Eidos registry is plausibly an Obsidian vault, and `.eidos/` sits beside `.obsidian/`.

```txt
.eidos/
  shapes/          # the body template for each kind of document
    Spec.md
    Architecture.md
    Audience.md
    Criteria.md
    Market.md
    Domains.md
  Schema.md        # the property contract: canonical (Eidos's) + custom (yours)
  Registry.md      # the Eidos version this registry targets
```

The registry owns its form. Eidos seeds `.eidos/` with the opinionated baseline (`eidos-init`), and from there the owner may extend it — add a property, adjust a shape — without leaving the standard. This is what makes Eidos adoptable without a fork: the default works out of the box, and the parts you change are yours.

Because the form lives in the registry, the skills read it from there rather than carrying their own copy. A registry that calls itself Eidos has a `.eidos/`; a skill that finds none offers to install one (see [AI](#ai)).

### Shapes (`.eidos/shapes/`)

A **shape** is the body template for a kind of document. The Spec shape is **body only** — the sections in their order, with their guidance — because a spec's frontmatter is generated from the [Schema](#properties-schemamd), not written by hand. The product-doc shapes are looser and carry their own light frontmatter inline, because product docs are loose by nature.

The canonical shapes Eidos ships — the opinionated baseline — live, public and browsable, in [`standard-seed/shapes/`](standard-seed/shapes) at the top of the standard's repo; `eidos-init` installs them into a registry's `.eidos/`. A registry may then reshape its own, and the skills consume whatever it holds. The shape files are where the specific sections are documented; [Spec body](#spec-body) below gives the rules for using them.

### Properties (`.eidos/Schema.md`)

`Schema.md` is the property contract — what a spec's frontmatter must and may carry. It is one markdown file in two parts:

- **`## Eidos Canonical`** — the properties Eidos defines for this version. Managed by the standard; `eidos-migrate` rewrites this block on a version change. Don't hand-edit it.
- **`## Custom Registry Properties`** — the properties this registry adds for its own use. Yours; preserved across migration.

Each property is a row: **name · type · required · meaning**. A property's `type` is drawn from the same small set Obsidian uses — **Text, List, Number, Checkbox, Date, Date & time** — so a registry's frontmatter renders natively in an Obsidian vault. Anything that wants more structure than one of those types almost belongs in the body (the shape), not in a property.

The canonical baseline, as seeded in 3.0.0:

| Property     | Type | Required | Meaning                                                                                                        |
| ------------ | ---- | -------- | ------------------------------------------------------------------------------------------------------------- |
| `id`         | Text | yes      | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it.                     |
| `title`      | Text | yes      | Human-readable name. Rename freely.                                                                            |
| `type`       | Text | yes      | Open, soft label. Human-chosen. Drives views, never structure. Suggested: `feature`, `capability`, `domain`, `integration`. |
| `domain`     | Text | yes      | The grouping. Title Case, matching the folder under `Specs/`. An unknown domain is valid (warn only).         |
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

`Registry.md` records, in one spot, the Eidos version the registry targets:

```markdown
# Registry

**Eidos Version:** 3.0.0
<!-- Used by the eidos-migrate skill to detect which version this registry targets. -->
```

The version is a registry-level fact, not a per-spec one — every spec in a registry is on the same version, so stamping each file would only invite drift. `eidos-migrate` reads the version here, diffs to the target, and bumps this line when done.

## Directory layout

```txt
Blueprint/               # the registry root; name is low-stakes and renameable
  .eidos/                # the form layer (hidden) — shapes, Schema, Registry
  Architecture.md        # overarching system shape, one entry door
  Audience.md            # who it serves and how each type interacts
  Criteria.md            # budget, scope objectives, timeline
  Market.md              # where it sits, how it differs, how it earns
  Domains.md             # the domains as descriptions
  Specs/
    <Domain>/
      <Title>.md         # one spec per unit, grouped by domain folder
  Arch/                  # optional, only when architecture detail outgrows one file
```

`Blueprint/` is the overarching root; its name is low-stakes and renameable because nothing in a spec points at it by path. Domains are folders under `Specs/`. Relationships between specs (`depends_on`) live in frontmatter so the folder choice stays low-stakes. One hierarchy on disk, many views from metadata.

If one repository holds several products, nest them as `Blueprint/<name>/...`, each with its own `.eidos/`, four docs, and `Specs/`.

### Naming

Everything a human reads in the file tree is **Title Case**, because the tree is a table of contents: product docs (`Architecture.md`), domain folders (`Identity/`), and spec files (`Magic Link Sign-In.md`). The `.eidos/` form layer is the exception — it is hidden machinery, lowercase by the same convention that names `.git`. A spec's filename is its title and may be renamed freely; the part that never changes is the `id` _inside_ the file — lowercase words joined by hyphens (`Magic Link Sign-In.md` carries `id: magic-link-signin`). The `domain` value is Title Case to match its folder. Fields meant for tools (`status`, `type`, `tags`) are not names in the file tree, so they stay as written.

### Referencing other specs

Links to other specs and sections are encouraged — they read well and you can follow them, where a bare name is neither. Standard markdown links are the best format for compatibility across editors and tools. This extends to the properties that point at other specs: `depends_on` holds links too, not bare ids — each spec's `id` stays its permanent identity behind them.

## Product docs

A few files at the top of the product that frame the whole thing — one of each. The four authored ones are prose, deliberately loose, and point-in-time, and each carries a little light frontmatter (`type: system`, `title`, `tags`, `created`, `modified`). They are not bound by the spec Schema; they are the loose, special case. Their shapes hold the full guidance for each; in short:

- **Architecture** — the shape of the product as a built system. When it outgrows one file, expand into an optional `Arch/` folder and keep this as the map.
- **Audience** — who it serves, and how each kind of user differs.
- **Criteria** — what decides and audits scope: budget, scope objectives, timeline.
- **Market** — where it sits, why it is not interchangeable, and how it earns.
- **Domains** — the product's domains, each with a short description. Derived from the specs and regenerable, so it carries no frontmatter; present by default.

Product docs are point-in-time snapshots of intent and are expected to evolve. Record what is true now; revise when it changes.

## Spec body

The body is the guided part of a spec — the frontmatter above is the firm contract. It follows a **shape**: a set of sections, in a set order, under set names, so a reader always knows where to look. The shape is the registry's, held in `.eidos/shapes/Spec.md`; the canonical baseline — the sections Eidos ships, each with its guidance — lives in [`standard-seed/shapes/Spec.md`](standard-seed/shapes/Spec.md). The specific sections are documented there, in the shape itself, so a registry can rework its shape without fighting the standard. What this file gives are the rules for using a body:

- **Keep the shape's order and names.** Leave a section out when it genuinely doesn't apply (no empty headings), but don't reorder them, rename them, or invent a parallel layout. A check may note a missing recommended section and offer to fill it; it never refuses the file.
- **One shape per registry, never per `type`.** Every spec in a registry follows the one shape it holds; `type` drives views, not layout.
- **Write it like a human would read it.** Shape the content to fit — add your own `###`/`####` sub-headings, tables, lists, code blocks, or small diagrams wherever they make the meaning clearer, and never flatten rich content onto a single line. A data model reads better as a table than a sentence; a sequence reads better as a numbered list. The result should read like a person wrote it, not a filled-in form.
- **Keep acceptance criteria short and observable.** Label each `**AC1:**`, `**AC2:**`… — unique within the spec for reference, not across the registry — and push supporting detail (a data model, a payload, a state table) into a table or sub-section the criterion points to, not onto the line.
- **Lead with intent and what you're getting; hold the line on non-goals.** The baseline shape opens with why the unit exists and its observable outcomes, and leans hardest on what it will _not_ do. Which sections carry each — and how to fill them — are documented in the shape file, not prescribed here.

## Rules

These are the load-bearing conventions.

1. **The frontmatter is the agreement; the body is guidance.** The properties at the top are checked against the registry's Schema. Body sections are recommended structure, not requirements.
2. **The registry owns its form.** Shapes and properties live in the registry's `.eidos/`, seeded from the opinionated baseline and free to be extended. A skill reads the form from the registry, not from a copy of its own.
3. **Validation is registry-defined.** A check reads _that registry's_ `Schema.md` and enforces it — canonical required properties plus whatever the registry marked required. The contract is the Schema, not a rule hardcoded in a tool.
4. **Portability over prescription.** Recommended sections may be omitted when a doc is in progress or genuinely does not apply. A missing required property is surfaced and added with a note on why; a missing section is noted and offered. Never refuse the file.
5. **Write it like a human would read it.** The recommended sections are a scaffold for a complete, living definition — not a form to pour text into. Reshape within and beneath them to fit the content: add your own `###`/`####` sub-headings, tables, lists, code blocks, or small diagrams wherever they make the meaning clearer, and never flatten rich content onto one line. Keep acceptance criteria short and observable; push supporting detail into a table or sub-section the criterion points to. If a spec reads like filled-in boilerplate, reshape it until it reads like someone wrote it.
6. **Reference other specs with links, not bare names — in prose and in properties.** Point at another spec, doc, or section with a markdown link. The same goes for frontmatter that points out, like `depends_on`. Each spec's `id` is still its permanent identity, sitting behind the link.
7. **One shared shape, in a predictable order.** Within a registry every spec uses the same sections, in the same order and under the same names, so a reader always knows where to look. What flexes is _which_ sections appear, not their order or names — and the shape is the registry's, held in `.eidos/shapes/`, not forked per `type`.
8. **Properties carry a type and a meaning.** Every property — canonical or custom — declares its name, its type (from the Obsidian set), whether it is required, and what it means. Frontmatter is generated from the Schema, so a new spec is born conforming.
9. **`type` is an open, soft label.** Humans choose it. It drives views and filtering, never structure. An off-list value is valid.
10. **`domain` is the grouping.** Required, soft, descriptive. Matches the folder. An unknown domain is valid — warn and offer to register it, don't block.
11. **`id` is permanent.** Stable, unique, kebab-case, assigned once, never renamed. Rename `title` freely.
12. **Intent is stable; Behaviors & Acceptance Criteria evolve.** Editing behaviors is routine. If Intent changes substantially, ask whether this is a different spec.
13. **Out of Scope carries the most weight.** It is where scope management actually happens. The strongest recommended section, but still not a hard gate.
14. **Acceptance Criteria are labeled `AC{n}:`** — in bold, e.g. `**AC1:**`. Unique within a spec for reference, not across the whole set.
15. **No work-tracking fields.** No `sprint`, `estimate`, or `assignee`. The moment you add them, a spec becomes a task and rots. Bridge to a tracker with a link.
16. **Implementation Notes are intent, not status.** They capture how you mean to build a thing and why — never how far along it is.
17. **`created` is set once; `modified` tracks the last change.** Both `YYYY-MM-DD`. Git holds the full edit history. The Eidos version is a registry fact, in `Registry.md`, not a per-spec property.
18. **Product docs are point-in-time.** Criteria, Market, and Audience capture a snapshot of intent and are expected to evolve.
19. **The human authors; the agent facilitates.** Intent, scope, and decisions stay with the person. An agent formats, supplements, asks, and holds scope; it does not generate finished specs or set direction.
20. **Human-facing names are Title Case.** Folders, product docs, and spec files read like a table of contents. The hidden `.eidos/` form layer is the exception. The kebab-case `id`, not the filename, is the permanent reference.

## Domains (`Domains.md`)

`Domains.md` at the registry root is the product's **map** — the table of contents a human or an agent reads first to find the right spec without scraping the tree. Present by default; like everything in Eidos, it never gates.

One `##` per domain, and under each, two layers: the human's short **description** of the domain, then a generated **index** of that domain's specs — each a markdown link with a one-line summary distilled from the spec's Intent.

```markdown
# Domains

## Identity

Who the user is and how they prove it.

<!-- eidos-domains: spec index (regenerated) -->
- [Magic Link Sign-In](Specs/Identity/Magic%20Link%20Sign-In.md) — passwordless sign-in by an emailed single-use link.
- [Session Management](Specs/Identity/Session%20Management.md) — keep a signed-in user across visits, and let them end access on a device.
```

- The **description** is the human's, written once. The **index** is derived and regenerable: the `eidos-domains` skill crawls the specs, groups them by `domain`, preserves the descriptions, and rebuilds the link lists and summaries. Re-run it whenever specs are added, renamed, or moved.
- The summaries distill each spec's own Intent; they are navigation, not the definition — the spec stays the source of truth.
- A domain with specs but no description is valid, just undescribed (the skill adds the heading and asks the human to describe it). A domain described here but with no specs is dangling; a validator may flag it.
- `Domains.md` never blocks anything. It annotates and navigates.

## Versioning

- Semantic Versioning (`MAJOR.MINOR.PATCH`). Major bumps for breaking changes, minor for backward-compatible additions, patch for clarifications.
- This file always holds the current version — right now, 3.0.0. When a version is tagged, this file is copied as-is into `versions/` under its full semver name (e.g. `versions/v3.0.0.md`). Each release is frozen there, so any two — even non-adjacent — can be diffed to migrate specs between them (see the `eidos-migrate` skill).
- A registry records the version it targets in its `.eidos/Registry.md`; migration reads and bumps it there.
- See `CHANGELOG.md` for history and migrations.
- Tools may reject if the version in this file is unsupported.

## AI

_This section is for an AI assistant working in an Eidos registry. A human can stop above — the rest is operating detail._

Eidos gives the direction; **the skills and a seeded registry are how the work gets done.** Earlier versions promised that Eidos worked from this file alone — 3.0.0 retires that. The form a registry uses now lives in the registry itself (`.eidos/`), so doing Eidos means a human, the skills, and a `.eidos/` that has been set up. Prefer the skills: `eidos` to author and validate, `eidos-init` to scaffold, `eidos-property` to add or change a custom property, `eidos-migrate` to upgrade versions.

**Facilitate, don't author.** Eidos is human-first. Format and structure what the owner gives you, supplement, ask clarifying questions, and press on Out of Scope — but never invent Intent, decide direction, or hand back a finished spec to rubber-stamp. When unsure, ask. A spec the owner didn't think through is worse than none.

**Find the form in the registry.** Every operation reads the registry's `.eidos/`: `Schema.md` for the property contract, `shapes/` for the body templates, `Registry.md` for the version. If a registry has no `.eidos/`, it is not yet an Eidos registry — offer to install one with `eidos-init`. Do not fall back to a hardcoded contract; the registry's form is the source of truth.

**Start at `Domains.md`.** It is the registry's map — every domain with its specs, each spec a link and a one-line summary. Read it first to navigate straight to the spec you need instead of scraping the tree, and regenerate it with `eidos-domains` when it has gone stale.

**Authoring a spec:**

1. Read the registry's `.eidos/Schema.md` for the property contract and `.eidos/shapes/Spec.md` for the body shape. Name the file for its Title Case title; put a permanent kebab-case `id` inside.
2. Generate the frontmatter from the Schema's required properties (canonical plus any custom-required); fill values from what the owner tells you; set `created`/`modified` to today. Don't guess a `status` or invent an `owner`.
3. Lead with **Intent** and **Behaviors & Acceptance Criteria** — short, observable criteria labeled `**AC1:**`, `**AC2:**`… Press hard on **Out of Scope**. Capture the rest as it surfaces; omit a section that doesn't apply, but keep the shape's order and names.
4. Where the owner is vague, ask — don't fill the gap with plausible prose. Push rich detail (a data model, a payload) into a table or sub-section rather than onto an AC line.

**Authoring a product doc:** pick Architecture, Audience, Criteria, or Market and start from its shape in `.eidos/shapes/`. Prose, loose, point-in-time — fill what's known, leave the rest.

**Validating a spec:** read the registry's `Schema.md` and check the frontmatter against it — required properties present and well-formed (`id` kebab-case, `created`/`modified` as `YYYY-MM-DD`; a `status` off the baseline warns, never fails), plus any custom-required property the Schema declares. Report missing body sections as suggestions, flagging an absent **Out of Scope** first, and note acceptance criteria that lack `**AC{n}:**` labels. Confirm no work-tracking fields crept in and that Implementation Notes read as intent, not progress. Surface, don't block — the output is a review the human acts on, and a missing required property is added with a note on why rather than failing the file.

**Linking other specs:** a relative markdown link with spaces as `%20` — `[Session Management](../Identity/Session%20Management.md)`; add a `#heading` anchor for a section (GitLab/GitHub lowercase-and-hyphenate the heading; an Obsidian vault uses the literal heading text). Linking properties like `depends_on` use the same link, one markdown-link string per entry — quote it in YAML, since a leading `[` starts a list:

```yaml
depends_on:
  - "[Session Management](../Identity/Session%20Management.md)"
```

The linked spec's `id` is its permanent identity. If a dependency has no spec yet, name it plainly — a bare `id` in `depends_on`, no fabricated link.
