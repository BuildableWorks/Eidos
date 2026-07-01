# Changelog

All notable changes to the Eidos standard are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). The current version of the standard always lives in `EIDOS.md`; when a version is tagged, that `EIDOS.md` is copied into `versions/` under its full semver name.

## [Unreleased]

## [4.1.0] - 2026-07-01

The release that makes Eidos's navigation mechanical and generalizes the framing docs. Every item gains two optional properties — `summary` (the one-line index/reference blurb) and `connects_to` (canvas edges); the framing docs (Architecture, Audience, Criteria, Market) become an official **`Frames` collection** (the retired `templates/` become its flavor shapes); "top-level documents" become a purely user-created loose layer; two generators ship — `eidos-index` (`build-index.py`) and the new **`eidos-canvas`** skill; and the hidden form directory is renamed **`.eidos/` → `_eidos/`** so Obsidian shows it. Additive over 4.0.0: existing items are untouched and both new properties are optional.

### Added

- **`summary` canonical property (optional).** One plain line — what the item is, in a sentence, distilled from Intent. The source for the collection `index.md` listing (and reference hovers), authored once on the item and read everywhere. Optional; an item missing it is flagged by the index, never refused.
- **`connects_to` canonical property (optional).** A List of links to the items this one connects to on the registry canvas — drawn as directed edges (this → target). The intentional map of how the product's pieces relate, decoupled from `depends_on` (an implementation dependency). Optional; absent means no canvas edges.
- **`Frames` collection.** The framing docs are promoted from one-off top-level docs to a real collection (`Frames/`), highly encouraged but not required. Its flavors — `frame.architecture`, `frame.audience`, `frame.criteria`, `frame.market` — are the old templates, now ordinary body shapes. Frames follow the same frontmatter contract as any collection item (`type: frame`, a `flavor`, a `status`, dates). A flat collection — frames aren't grouped by domain.
- **`build-index.py` in the `eidos-index` skill.** A stdlib-only Python 3 script that reads `_eidos/Registry.md` for the declared collections, walks each collection's folder, and rebuilds its `index.md` from the items' `title` + `summary` — grouped by sub-folder or flat, links URL-encoded for the registry's naming convention. Deterministic and idempotent, with a `--check` mode for CI and a `--collection` filter. Runs wherever a shell is available; on a sandboxed host the skill falls back to doing the walk by hand.
- **`eidos-canvas` skill.** Generate an Obsidian-compatible [JSON Canvas 1.0](https://jsoncanvas.org) `.canvas` map of the registry via `build-canvas.py`: items are text nodes embedding their `## Intent`; **Frames are full-file nodes** in their own group; directories nest into **nested groups** (a sub-directory under a domain becomes another group); each item's `connects_to` links are drawn as edges, with `--include-dependencies` overlaying `depends_on` in a distinct color (purple by default). **Each collection gets its own color** — the skill proposes a schema from the registry, confirms it, and a regenerated canvas keeps its colors so the choice sticks. Top-level documents are not mapped; the generated `.canvas` is itself a top-level document — register it in the Registry's `## Top-Level`.

### Changed

- **Form-layer directory renamed `.eidos/` → `_eidos/`.** The dot is dropped so Obsidian no longer hides the directory — users can open and edit `Registry.md`, the shapes, and the personas straight from the vault. It also sorts to the top of the tree and has no shell/tooling/wikilink edge cases. Same "machinery, out of the way" intent — only the leading character changes.
- **`eidos-init` skill renamed to `eidos-install`.** "Install" reads more plainly than "initialize" for what it does — stand up the form layer and starting collections in a repo.
- **Property model reworked into Core + Custom, scoped by Applies To.** Eidos's own machinery uses six **core** properties (`id`, `title`, `summary`, `flavor`, `owner`, `connects_to`); everything else — `status`, `date_created`, `date_modified`, `tags`, `domain`, `depends_on`, `type` — is a **custom** property the seed ships as a default, useful but not depended on, each scoped by an **Applies To** column (a list of collections, or `all`) so a property never lands where it makes no sense (`domain`, `depends_on`, and `type` are Specs-only). This replaces the old flat "canonical + required" table: the previously-required `domain`, `status`, dates, and `type` were opinionated, not things Eidos needs. `created`/`modified` become `date_created`/`date_modified`; `type` stays as a `Specs`-scoped soft category label (feature, capability, integration), no longer a core/required property. `owner` now means who owns the document (non-owners are warned before editing). Schema table headers are Title Case (`Name`, `Type`, `Applies To`, `Meaning`) for readability.
- **The Schema moved into `Registry.md` as a `## Schema` section**, and the property skill `eidos-property` → **`eidos-schema`**. There is no separate `_eidos/Schema.md` — one file (`Registry.md`) now holds the whole registry index and its frontmatter contract (`### Eidos Core` + `### Custom Properties`).
- **Seed folder `standard-seed/` → `seed/`, personas moved into it.** Dropping the "standard-" theming leaves room for non-canonical seeds later; the personas now live at `seed/personas/` (installed to `_eidos/personas/`) rather than a top-level folder. The seed self-documentation moved into this README's **Canonical Seed** section, `README.template.md` became the seed's `README.md` (it installs directly, no rename gymnastics), and the seed's `.gitignore` is now a real dotfile.
- **Persona `product-owner` → `registry-owner`.** The owner holds true ownership of the registry — which may define a product, a body of research, a methodology, or any other form of thought, not necessarily a product.
- **README is a top-level document.** It's listed first under the Registry's `## Top-Level` — the front door and a first-class entry, not a special case.
- **Spec shape splits "Open Questions & Assumptions" in two.** Assumptions (what you're taking as given) become an `### Assumptions` subsection under `## Intent`, where they frame it; `## Open Questions` (what you don't yet know) stands on its own. Mixing the two made a reader stop to ask "is this an active question or a settled assumption?" — the split removes that. Both `spec.full` and `spec.micro` flavors updated.
- **Collection indexes and the canvas are derived, not authored.** `eidos-index` emits each item's `summary` rather than distilling one at generation time; the canvas is built from `connects_to`. Both regenerate wholesale.
- **"Top-level documents" are now 100% user creations.** Eidos no longer ships canonical top-level docs; the framing four moved into `Frames`. A top-level doc (a Roadmap, a Vision, the generated Registry Map) is one-of-a-kind, free-form prose — no shape, no flavors, no validation — listed in the Registry's `## Top-Level`.

### Removed

- **The `templates/` concept.** The one-off top-level-doc templates are gone, replaced by the `Frames` collection's flavor shapes in `_eidos/shapes/`. `eidos-install` scaffolds a `Frames/` collection (optionally with the four blank framing docs) instead of scaffolding top-level docs from templates.

**Migration from 4.0.0:** run `eidos-migrate` — it renames `.eidos/` → `_eidos/`, adds the optional `summary` and `connects_to` rows to the canonical Schema, moves `.eidos/templates/*` → `_eidos/shapes/frame.*`, moves the root framing docs into `Frames/` as collection items, declares the `Frames` collection, and trims `## Top-Level`. Existing items are untouched; both new properties are optional. Bumps `eidos_version` to `4.1.0`.

## [4.0.0] - 2026-06-23

A breaking release that makes `.eidos/Registry.md` the registry's **index**, generalizes `Specs/` into declared **collections** with multiple body **flavors**, moves each collection's listing into a generated **`index.md`** inside its folder (retiring the top-level `Domains.md`), and adds a visible **`README.md`** "start here" plus a personal **`user.md`** actor file. A 3.x registry migrates with `eidos-migrate`; the per-spec contract is essentially unchanged, but the layout moves.

### Added

- **Collections.** A registry declares its top-level content folders in the Registry body, each with a description. `Specs` is the default; add more — decisions, personas, integrations — with `eidos-registry`. An item's collection is its top-level folder. A collection may group its items one level deep in sub-folders (Specs by domain); deeper nesting is discouraged.
- **Flavors.** A collection can offer more than one body shape — a default `full` and a lighter `micro` — each a file named `<kind>.<flavor>.md` in `.eidos/shapes/`. A new optional canonical property, `flavor`, records which an item follows (absent = the collection's default); validation checks the body against that flavor's shape, so a `micro` spec isn't faulted for `full`-only sections. The canonical default flavor renames `Spec.md` → `spec.full.md`, with `spec.micro.md` beside it. Shapes are **collection-only** and live in `.eidos/shapes/`; the one-of-each top-level-doc scaffolds are now **templates** in `.eidos/templates/` (no flavors, not validated, kept as the record of each doc's intended full form).
- **The Registry as index.** `.eidos/Registry.md` keeps its frontmatter (`eidos_version`, `naming`) and gains a body: a `## Top-Level` list of the top-level documents and a `## Collections` section with each collection's flavors and grouping. It is the authoritative index of the whole registry.
- **`README.md` start-here.** A thin, visible `README.md` at the registry root is the human front door — what the product is, with pointers into the registry — pointing into the hidden `Registry.md`. `eidos-init` seeds it from `standard-seed/README.template.md`.
- **Per-collection `index.md`.** Each collection carries a generated `index.md` leaf inside its folder — the item listing, grouped by sub-folder when present, flat otherwise. Fully generated (descriptions live in the Registry), so it rebuilds wholesale.
- **Personas.** Default response contracts — `personas/`, installed into `.eidos/personas/` (committed, team-tunable) — one per role (Product Owner, Developer, Stakeholder, Designer, Project Manager). A persona sets the agent's vocabulary, technical depth, what it surfaces, and who decides: a Designer gets experience terms (no db indexes), a Developer full depth, the Product Owner the decisions. The agent reads the actor's persona before responding.
- **The actor (`.eidos/user.md`) + `eidos-whoami` skill.** A personal, gitignored file that names the actor's persona and **calibrates** it — role for this product, experience with the scope, technical capacity. Set it with the new `eidos-whoami` skill (a guided who-are-you that `eidos-init` runs); unset or absent defaults to full, product-owner-style facilitation. It is the one `.eidos/` file not committed.
- **`eidos-registry` skill** — add a collection or flavor and keep the Registry's Top-Level/Collections index current.

### Changed

- **Rule 7 reframed** — from "one shape per registry" to "one shape family per collection, declared as flavors." A flavor is a deliberate, registry-declared structural choice; `type` still drives views, never structure. New rules: the Registry is the index and `README.md` its door (21), read the actor before acting (22), each collection has a generated index (23). New **The actor**, **Collections**, **Flavors**, and **Collection indexes** sections in `EIDOS.md`; `## Overview` in the Registry body is now `## Top-Level`.
- **`eidos-domains` → `eidos-index`.** The domain re-indexer generalizes to regenerate any collection's `index.md`, prompting which collections to re-index. `eidos`, `eidos-init`, `eidos-format`, and `eidos-registry` are updated for collections, flavors, the actor, and the new layout; the example registry gains a `micro`-flavored spec, a `Specs/index.md`, a `README.md`, and a committed `user.md`.

### Removed

- **The top-level `Domains.md`** and its shape. Its per-spec listing moves into `Specs/index.md` (one `index.md` per collection); the domain descriptions move up into the Registry's Collections section. This is the breaking change.

**Migration from 3.x:** run `eidos-migrate`. Net per registry: add the optional `flavor` to the canonical Schema; rename `.eidos/shapes/Spec.md` → `spec.full.md` (optionally add `spec.micro.md`); move `Domains.md` → `Specs/index.md` (its descriptions lifted into the Registry); add the Registry body (Top-Level + Collections), a root `README.md`, `.eidos/personas/`, and `.eidos/user.md` with a `.eidos/.gitignore` (then `eidos-whoami` to set personas); bump `eidos_version` to `4.0.0`. The per-spec body and most frontmatter are unchanged.

## [3.1.0] - 2026-06-19

An additive release. A registry now chooses how its files are named, the root folder is officially any name, and a registry can carry its own free-form top-level docs. Nothing here breaks an existing 3.0.0 registry — an unset naming convention defaults to today's Title Case.

### Added

- **Configurable naming convention.** A registry picks how human-facing names — spec files, domain folders, product docs — read, recorded as a `naming` key in `.eidos/Registry.md`'s YAML frontmatter: `Title Case` (the default; spaces, as before), `TitleCase` (no spaces), or `kebab-case` (lowercase, hyphenated — the filename then equals the `id`). The link format follows from it: only a Title Case registry encodes spaces as `%20`, so the two space-free options give clean, scriptable paths. `eidos-init` asks for the convention at setup; `eidos`, `eidos-format`, and `eidos-domains` read it when naming or linking.
- **Free-form top-level docs.** Beyond the canonical four product docs (Architecture, Audience, Criteria, Market), a registry may add its own top-level docs — a Roadmap, a Vision, a Glossary. These are free-form: no shape, no validation. They carry the light product-doc frontmatter and are supported by `eidos-format`, which organizes a draft into the house style rather than checking it against a template — because a top-level doc is filled in once and edited in place, not stamped out like a spec. The example registry gains a `Roadmap.md` to show the pattern.

### Changed

- **The registry root is officially any name.** It was always renameable, but the skills now locate a registry by its `.eidos/` marker rather than the folder name, so `Abstract/`, `Product/`, or the product's own name work as well as the default `Blueprint/`. The root is simply wherever `.eidos/` lives.
- **`Registry.md` is the registry's small config card, now YAML frontmatter.** It records the Eidos version (`eidos_version`) and the naming convention (`naming`) as frontmatter — the two registry-level facts the skills read, in the same metadata format the specs use and ready for `yq`/tooling.
- **`eidos-format` reshapes any registry doc**, not only specs: a spec toward the Spec shape, a product doc toward its shape, and a free-form top-level doc into the house style with no shape at all.

**Migration from 3.0.0:** nothing required — a 3.0.0 registry keeps working, defaulting to Title Case. To adopt the new format, convert `.eidos/Registry.md` to YAML frontmatter with `eidos_version` and `naming` (or run `eidos-migrate`, which does it and bumps the version). The canonical property set is unchanged.

## [3.0.0] - 2026-06-19

A breaking release that moves a registry's **form** — its body shapes and its property contract — out of the standard and into the registry itself, as a hidden `.eidos/` folder. Eidos becomes an opinionated baseline you can extend without forking: adopt as-is, add your own properties, still migrate.

### Added

- **The `.eidos/` form layer.** Every registry now owns its form in a hidden `.eidos/` at its root: `shapes/` (the body template for each kind of document), `Schema.md` (the property contract), and `Registry.md` (the Eidos version). Seeded by `eidos-init` from an opinionated baseline; the skills read it from there.
- **`Schema.md` — a registry-defined property contract.** Two blocks: `## Eidos Canonical` (the standard's properties, managed by `eidos-migrate`) and `## Custom Registry Properties` (yours, preserved across migration). Each property declares name, type, required, and meaning. Property types are drawn from the Obsidian set — Text, List, Number, Checkbox, Date, Date & time — so frontmatter renders natively in an Obsidian vault.
- **Generated frontmatter.** A spec's frontmatter is emitted from the Schema's required properties, so every new spec is born conforming.
- **Registry-defined validation.** A check reads _that registry's_ Schema — canonical required plus any custom-required — and surfaces a missing field by adding it with a note on why, never refusing the file.
- **`eidos-property` skill** — add, rename, or retire a custom property: it presses the owner to decide type, meaning, and whether it's required, writes the row into `Schema.md`, and backfills every existing spec.
- **`eidos-domains` skill** — regenerate `Domains.md` as a navigation index: each domain's hand-written description plus a generated list of its specs (links + a one-line summary distilled from each spec's Intent). Makes `Domains.md` the map humans and agents read first instead of scraping the tree.
- **`Registry.md`** — records the Eidos version in one spot, read and bumped by `eidos-migrate`.

### Changed

- **Skills consume the registry's form instead of vendoring templates.** The canonical baseline lives, public and front-facing, in the top-level `standard-seed/`; `eidos-init` installs it, and `eidos`, `eidos-format`, and `eidos-property` read the live `.eidos/` from the registry in the working directory. The old template triplication is gone; the three skills that need the standard (`eidos`, `eidos-init`, `eidos-migrate`) carry committed copies of just what they need, kept in sync by `scripts/sync-skills.sh`, so a git-marketplace install works on Claude Code and sandboxed Claude Desktop alike.
- **"Works from `EIDOS.md` alone" is retired.** `EIDOS.md` gives the method; doing Eidos now needs the skills and a seeded registry. The `## AI` section and the "templates ship with the standard" guidance were rewritten accordingly.
- **Body shapes** moved from the top-level `templates/` into `.eidos/shapes/`. The Spec shape is body-only (frontmatter is generated); the product-doc shapes keep their own light frontmatter. The baseline section set is unchanged from 2.1.
- **The canonical baseline is a public, top-level `standard-seed/`.** The seed (shapes + `Schema.md` + `Registry.md`) is browsable at the repo root, not tucked inside a skill; `eidos-init` installs it, and `eidos-migrate` reads it.
- **The `eidos` skill is lean and defers to `EIDOS.md`.** It holds the facilitation flow and reads the registry's `.eidos/`, and points to `EIDOS.md` — the officially maintained ruleset, carried as a committed copy in the skill — instead of restating the rules. Its `core-overview.md` and `spec-schema.md` references were removed as duplicative; `example-spec.md` stays.
- **`Domains.md` became the registry's navigation map** — each domain's description plus a generated per-spec index — rather than descriptions alone. The body-section catalog was also pulled out of `EIDOS.md` into the Spec shape, leaving `EIDOS.md` with the rules for using a body, not the section list.

### Removed

- **The per-doc `eidos_version` frontmatter field** — the version is a registry fact now, in `.eidos/Registry.md`.
- **The top-level `templates/` folder** and **`scripts/sync-skills.sh`** — replaced by the seed in `eidos-init` and the registry's own `.eidos/`.

**Migration from 2.x:** use the `eidos-migrate` skill, or diff `versions/v2.1.0.md` against `EIDOS.md`. The net per registry is small: install `.eidos/` from the v3 seed (shapes, canonical `Schema.md`, `Registry.md`), drop `eidos_version` from every spec and product doc, and write `**Eidos Version:** 3.0.0` into `.eidos/Registry.md`. The body section set is unchanged, so specs need no restructuring.

## [2.1.0] - 2026-06-18

### Added

- Apache License 2.0 (`LICENSE`); `license: Apache-2.0` declared in the plugin manifest.
- `eidos-format` skill — reshapes a rough draft or brain-dump into the Eidos spec shape, preserving the author's words and adding nothing. It reads the spec template for the target shape and is mostly a format-and-organize pass within a single file.
- An `## AI` section at the foot of `EIDOS.md` — condensed operating guidance (facilitate-don't-author, authoring, validating, the link format) for an AI working without the skills installed; humans can stop above it. The former top-level `## Validation` section folded into it.

### Changed

- Clarified that the spec body sections are a scaffold, not a form: shape them for readability (sub-headings, tables, lists), never flatten rich content onto one line, and keep acceptance criteria short with supporting detail pushed into tables or sub-sections. Captured as Rule 3, _Write it like a human would read it_, and echoed in the schema, the `eidos` skill, and the Spec Template.
- Cross-references between specs are now markdown links (relative path, `%20` for spaces, `#heading` for a section), never bare `code-style` names — readable and navigable. Captured as Rule 4, _Reference other specs as links, never bare names_, with a new _Referencing other specs_ section; the example specs' Dependencies were converted, and `eidos-format` treats name→link as a formatting fix. The convention extends to linking properties: `depends_on` now holds markdown-link strings rather than bare ids (the linked spec's `id` stays its permanent identity).
- Clarified the shared spec shape: _which_ sections appear is flexible (omit what doesn't apply, no empty headings), but their order and names are strongly encouraged — close to required — so every spec reads predictably and is not a free-for-all. Reworded Rule 5 (was _One shape for specs, always_) to _One shared shape, in a predictable order_.

### Fixed

- The `eidos` skill resolved templates from a bare `templates/` path, so when used in an adopting repo it looked in that project's working directory instead of the standard. It now resolves them the same way `eidos-init`/`eidos-migrate` do — `${CLAUDE_PLUGIN_ROOT}/templates/` in Claude Code, a vendored copy inside the skill on Claude Desktop — and `scripts/sync-skills.sh` vendors `templates/` into `eidos` too. An adopting repo holds only `Blueprint/`; it never needs a `templates/` folder of its own.

## [2.0.0] - 2026-06-17

A breaking redesign of the spec contract and body. Eidos now captures the _intent_ of the build (never work or status), carries requirements as labeled acceptance criteria, and ships a default `Domains.md` and a `Blueprint/` root.

### Added

- `created` and `modified` frontmatter fields (`YYYY-MM-DD`).
- `## Dependencies` and `## Testing` body sections.
- Optional `### Implementation Notes` under `## Intent` — the intent of the implementation, never its state.
- `**AC{n}:**` labels for acceptance criteria, unique within a spec for reference, under requirement sub-headings (Functional, Performance, Design, External interface, Quality attributes) inside `## Behaviors & Acceptance Criteria`.
- `Domains.md` as part of the default layout, with a new `templates/Domains Template.md`.
- Full-semver version snapshots in `versions/`, plus an `eidos-migrate` skill for non-sequential migration between any two versions.
- An optional, recommended `eidos_version` frontmatter field, so each doc declares the standard it targets (aids migration and tooling).
- An `eidos-init` skill that scaffolds a new registry from the templates, following the current `EIDOS.md` (no example-copying).
- Packaged as an installable Claude Code plugin (`.claude-plugin/`), with the skills in the top-level `skills/` and `scripts/sync-skills.sh` to vendor assets for standalone use.

### Changed

- Renamed the registry root from `product/` to `Blueprint/` — it sorts to the top of the file tree and reads as the product's defining document; still low-stakes and renameable, since nothing points at it by path.
- `## Behavior` → `## Behaviors & Acceptance Criteria`.
- Merged `## Constraints` and `## Decisions` into a single `## Constraints & Decisions`; decision dates are now optional.
- `status` is a soft baseline — `Draft | Intake | In Progress | Done | Archived | Deprecated` (an off-list value warns, never fails) — shown bracketed in the template; `type` is shown bracketed too.
- `Domains.md` uses `##` sub-headings per domain instead of a bullet list, and is listed among the product docs.
- `Open Questions` → `Open Questions & Assumptions`, moved up to just after Intent.
- Criteria: `Objective and scope` → `Scope Objectives`, plus a new `Parameters & Variables` section. Market: a new `Competitors` section, with `Position and difference` → `Positioning & Differentiators` and `How it earns` → `Earning Capabilities`. Product docs no longer carry a `Decisions` log.
- Plain-language pass across `EIDOS.md` and the README for non-technical readers.

### Removed

- Frontmatter fields `last_validated`, `implements`, `serves_job`, `activity`, and `supersedes`.
- The `manifest.json` version pointer — the `EIDOS.md` header and `.claude-plugin/plugin.json` already carry the version, and nothing consumed it.

**Migration from 1.x:** use the `eidos-migrate` skill, or diff `versions/v1.0.0.md` against `EIDOS.md`. Map `status` (`proposed`/`accepted` → `Intake`, `in-progress` → `In Progress`, `shipped` → `Done`, `deprecated` → `Deprecated`); carry `last_validated` into `modified`; relabel behaviors as `AC{n}`; merge Constraints and Decisions; add `Dependencies` and `Testing`.

## [1.0.0] - 2026-06-16

Initial published version of the Eidos standard. The normative definition lives in a single top-level `EIDOS.md`; the repository is the versioned home of the standard, modeled on the backlog.md layout.

### Added

- `EIDOS.md` — the authoritative standard: what a spec is, the two-tier document model, directory layout, product docs, the spec frontmatter contract (required + optional fields), recommended body sections, load-bearing rules, the optional `Domains.md` descriptions, validation, and versioning.
- `CHANGELOG.md`, `manifest.json` (machine-readable version pointer), and `AGENTS.md`.
- `versions/` — reserved for preserved prior versions of `EIDOS.md`.
- `example/` — a filled-in worked example of an Eidos product definition.
- `.claude/skills/eidos/` — the authoring/validation skill, vendored in-repo.

### Removed

- The blank `product/` scaffold. Authors copy `example/` (or run the skill) instead of filling empty templates checked into the standard's repo.

[Unreleased]: https://github.com/BuildableWorks/Eidos/compare/v4.0.0...HEAD
[4.0.0]: https://github.com/BuildableWorks/Eidos/compare/v3.1.0...v4.0.0
[3.1.0]: https://github.com/BuildableWorks/Eidos/compare/v3.0.0...v3.1.0
[3.0.0]: https://github.com/BuildableWorks/Eidos/compare/v2.1.0...v3.0.0
[2.1.0]: https://github.com/BuildableWorks/Eidos/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/BuildableWorks/Eidos/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/BuildableWorks/Eidos/releases/tag/v1.0.0
