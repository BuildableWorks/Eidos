---
name: eidos-migrate
description: >-
  Migrate an Eidos registry — its items and top-level docs — from one version of the standard to another. Use whenever someone wants to upgrade, migrate, or bring a registry up to date with a new Eidos version — e.g. "migrate our specs to Eidos 3.0", "we bumped the standard, update the specs", "bring this registry to the latest format", or "what changed between Eidos v1 and v3 and how do I move my specs over". Migrations are non-sequential: go directly from any source version to any target (v1.0.0 → v3.0.0) by diffing the two version snapshots. Trigger even when the user doesn't say "migrate" — "these specs are on the old format" or "update the frontmatter to the new schema" apply too.
---

# Eidos Migrate

Move a registry's items and top-level docs from one version of the Eidos standard to another. A migration is a **diff between two standard snapshots**, applied to the registry. You do not step through intermediate versions — to go from v1.0.0 to v3.0.0, you diff those two snapshots directly and apply the net change.

This skill is the companion to `eidos` (authoring/validation). Read `eidos` for the target contract; read this when the contract itself has moved and files need to catch up.

## How you work: facilitate, don't bulldoze

Migration is mechanical, but it is still the owner's registry. Propose the plan, show what will change, and **never silently drop content**. If the target version removes a field or section that holds real information, surface that information and ask where it should go (fold into another section, keep as a note, or deliberately drop) — do not delete it on the user's behalf. The custom part of a registry's form — its custom properties, any reshaped section — is the owner's and is preserved, never overwritten.

## Where the version history lives

Migration needs the version snapshots, the changelog's migration notes, the current standard, and — when bringing a registry up to a version that has a form layer — the canonical form-layer seed. Find them where the standard lives:

These ship as committed copies inside this skill's own folder — `versions/`, `CHANGELOG.md`, `EIDOS.md`, `seed/`, and `personas/` — kept in sync with the standard's top-level sources by `scripts/sync-skills.sh`. So they're present whether you're in Claude Code or a sandboxed host (Claude Desktop). The top-level files stay the source of truth; these are synced copies. When working inside the standard's own repo, the top-level files are right there.

`versions/vX.Y.Z.md` is a frozen snapshot of each released standard; `CHANGELOG.md` holds the per-version migration notes; `EIDOS.md` is the current standard and the usual target. A migration needs both endpoints. If a needed snapshot is missing, say so; never fabricate a version's contract.

## Procedure

1. **Establish the target.** Default to the current `EIDOS.md`. If migrating to a non-current version, use its `versions/` snapshot.

2. **Establish the source.** Check for the form-layer directory — `_eidos/` (v4.1+) or `.eidos/` (v3.0–v4.0) — and read its `Registry.md`, where a v3+ registry declares its version. If there is neither (pre-v3), detect the source from the file shape and confirm with the user. Fingerprints:

   - **v1.x** — frontmatter has `last_validated`, `implements`, `serves_job`, `activity`, or `supersedes`; body uses `## Behavior`, separate `## Constraints` and `## Decisions`; `status` is lowercase (`proposed`, `in-progress`, …); root folder is `product/`.
   - **v2.x** — frontmatter has `created`/`modified` and often a per-doc `eidos_version`; body uses `## Behaviors & Acceptance Criteria` with `AC{n}` labels, merged `## Constraints & Decisions`; `status` is Title Case; **no form-layer directory**.
   - **v3.0–v4.0** — has a form-layer directory named **`.eidos/`** (`shapes/`, `Schema.md`, `Registry.md`); the version is in `Registry.md`; items carry no `eidos_version`. **v4.1+** is identical but the directory is renamed **`_eidos/`** (the dot dropped so Obsidian shows it).

3. **Diff the two snapshots.** Compare source and target and derive the net transformation across four concerns:

   - **The form layer** — whether the target keeps the form in a hidden directory (v3+) the source lacked, and what it's named: `.eidos/` in v3.0–v4.0, `_eidos/` from v4.1 (dot dropped so Obsidian shows it). Going to v3, the registry gains that directory with `shapes/`, `Schema.md`, and `Registry.md`; migrating a v3.0–v4.0 registry to v4.1+ also **renames `.eidos/` → `_eidos/`**.
   - **Properties (frontmatter)** — fields added, removed, renamed, or with changed value sets. In v3 the contract is the Schema, so map the source's per-item fields onto the properties the target Schema declares (through 4.0 a flat `## Eidos Canonical` block in `.eidos/Schema.md`; from 4.1 a `## Schema` section inside `Registry.md`, with `### Eidos Core` plus `### Custom Properties`).
   - **Body/shape** — sections renamed, merged, split, added, or removed; labeling conventions (`AC{n}`).
   - **Structure/naming** — root folder name, collection layout and per-collection indexes (the top-level `Domains.md` was retired for a generated `Specs/index.md` in 4.0.0), file layout.

   Because you diff the two endpoints, a field dropped and later reintroduced, or renamed twice, resolves to its correct net state automatically.

4. **Write the migration plan.** A short, per-concern list of every transform, plus anything that needs human judgment (removed fields/sections that hold content, a custom shape that conflicts). Show it before touching files.

5. **Apply, once the plan is agreed.** Order matters when the form layer is involved:

   - **Install or update the form layer first.** If the target has a form dir and the registry has none, install the canonical seed (`shapes/` — including the `frame.*` flavors of the Frames collection — `personas/`, `Registry.md` (which from 4.1 carries the Schema in its `## Schema` section), `user.md`, and `.gitignore`, plus a root `README.md`) into the form dir — `Blueprint/_eidos/` for the current standard (`.eidos/` for a pre-4.1 target). If the registry already has a form dir, first **rename `.eidos/` → `_eidos/` when the target is 4.1+**, then rewrite only the standard-managed core block to the target version (`## Eidos Canonical` in `.eidos/Schema.md` through 4.0; the `### Eidos Core` block inside `Registry.md`'s `## Schema` from 4.1) and **leave the registry's custom properties untouched**; offer any new or changed canonical shapes additively, never overwriting a shape the owner has customized.
   - **Migrate each item** (across every collection). Map frontmatter onto the target Schema's properties; drop removed fields _after_ surfacing any content they held; add newly-required fields as stubs the human fills (e.g. `date_created` where none can be derived). Restructure the body to the target flavor's shape, applying labeling; add new recommended sections only as clearly-flagged empty stubs — never invent their contents.
   - **Apply structural/naming changes** across the registry (e.g. `product/` → `Blueprint/`).
   - **Set the version.** Write the target version into the form dir's `Registry.md` — `_eidos/Registry.md` for 4.1+ (creating it if new).

6. **Validate.** Run the `eidos` validation pass against the **target** Schema and report remaining gaps as suggestions, not failures.

7. **Report.** Summarize per file: what changed, what was carried over, and every place a human decision is still needed.

## Worked example: 3.1.0 → 4.0.0

A breaking move — the layout changes — but the per-item contract barely does. Diffing `versions/v3.1.0.md` against `versions/v4.0.0.md` yields (note: migrating straight to the current version instead folds the framing docs into the `Frames` collection — see the 4.0 → 4.1 example below — rather than into a `templates/` folder):

- **Properties** — the canonical block gains one **optional** property, `flavor` (Text, no): which body flavor an item follows, absent meaning the collection's default. Rewrite `## Eidos Canonical` to the 4.0.0 seed and leave `## Custom Registry Properties` untouched. Nothing to backfill — absent already means default.
- **Shapes, templates, flavors** — rename `.eidos/shapes/Spec.md` → `spec.full.md` (the Specs collection's default flavor) and offer to add `spec.micro.md` from the seed. Remove the `Domains.md` shape (the Domains doc is gone). **Move the top-level-doc shapes (`Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md`) from `.eidos/shapes/` into a new `.eidos/templates/`** — shapes are now collection-only; top-level docs use templates. Spec sections are unchanged, so items need no body restructuring.
- **`Domains.md` → `Specs/index.md`** (the breaking change). Move the top-level `Domains.md` into a generated `Specs/index.md` leaf inside the collection — the per-item listing, links now relative to `Specs/`. Lift the domain **descriptions** up into the Registry's Collections section (under Specs → Domains), since the leaf is purely generated. Regenerate the leaf with `eidos-index`.
- **`Registry.md` gains a body.** Frontmatter unchanged but for the version bump to `4.0.0`. Add the body: a `## Top-Level` (a bullet per top-level doc — link + the owner's one-line description) and a `## Collections` declaring the default `Specs` collection with its flavors (`full` default, `micro` if added), its domain grouping (with the descriptions lifted from `Domains.md`), and a pointer to `Specs/index.md`.
- **`README.md` start-here** — install `seed/README.md` → `<root>/README.md` and fill the product name; it is the visible front door into the Registry.
- **Personas + the actor file** — install the persona defaults (`personas/` → `.eidos/personas/`), the blank `seed/user.md` → `.eidos/user.md`, and `seed/gitignore` → `.eidos/.gitignore` (merge a `user.md` line into an existing `.eidos/.gitignore` rather than overwriting it). Then run `eidos-whoami` so each actor sets their persona and calibration.
- **Specs** — untouched; bodies and frontmatter already conform, and `flavor` is optional, defaulting to `full`.

The net per registry: add the optional `flavor`; rename the shape; relocate `Domains.md` → `Specs/index.md` (descriptions up to the Registry); add the Registry body, a root `README.md`, `.eidos/personas/`, and `.eidos/user.md` + `.eidos/.gitignore`. No per-item body edits. Set `eidos_version: 4.0.0` when done.

## Worked example: 4.0.0 → 4.1.0

A property-model rework, the framing docs promoted to a collection, and a directory rename. Diffing `versions/v4.0.0.md` against `EIDOS.md` (4.1.0) yields:

- **Form-dir rename** — rename the form layer `.eidos/` → `_eidos/` (the dot dropped so Obsidian shows it and the owner can edit the Registry, shapes, and personas from the vault). Rename the directory; nothing inside it changes name. Every 4.0 registry takes this one structural step.
- **Schema moves into `Registry.md` as a `## Schema` section** — there is no separate `Schema.md`. The old flat `## Eidos Canonical` block becomes `### Eidos Core` (`id`, `title`, `summary`, `flavor`, `owner`, `connects_to`) plus `### Custom Properties` (the registry's) — which carries the seed's shipped defaults (`status`, `date_created`, `date_modified`, `tags`, and, scoped to `Specs`, `domain`, `depends_on`, `type`) with an **Applies To** column, followed by any pre-existing custom rows (give each an Applies To of `all`). Delete the old `_eidos/Schema.md`.
- **Property changes on every item:**
  - **Rename** `created` → `date_created` and `modified` → `date_modified`.
  - **Keep `type`, but move it** — it's no longer a core/required property, just a `Specs`-scoped custom default (a soft category label). Drop `type: frame` from the framing docs — their collection and flavor identify them.
  - **Optionally add** `summary` (one line from Intent, for the index) and `connects_to` (canvas edges) — both optional, nothing to backfill.
  - `owner` keeps its value but now means who owns the document (non-owners are warned before editing).
- **Persona rename** — `_eidos/personas/product-owner.md` → `_eidos/personas/registry-owner.md` (the same response contract, generalized to true registry ownership).
- **Templates → the Frames collection.** The `templates/` concept is retired: move `.eidos/templates/{Architecture,Audience,Criteria,Market}.md` → `_eidos/shapes/frame.{architecture,audience,criteria,market}.md` (they become the `Frames` collection's flavor shapes — strip the inline frontmatter, keep the body and its guidance). Delete the old `templates/`.
- **Framing docs → collection items.** Move the registry's root `Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md` into a new `Frames/` folder, and give each the collection frontmatter generated from the Schema (`id`, `flavor:` its kind, `owner`, `status`, `summary`, the two dates), preserving its prose. They are no longer top-level docs.
- **Registry** — in `_eidos/Registry.md`, declare `Frames` **first** in `## Collections` (framing docs are the most primary), then `Specs`; give Frames its four `frame.*` flavors (flat, no domains). Remove the four framing docs from `## Top-Level`, leaving only the owner's own top-level docs (a Roadmap, a Vision, the Registry Map). Bump `eidos_version` to `4.1.0`. Regenerate each collection's `index.md` with `eidos-index`.

The net per registry: rename `.eidos/` → `_eidos/`; merge `Schema.md` into `Registry.md`'s `## Schema` (Core + Custom, Applies To column); on every item rename the two date keys (and drop `type: frame` from frames); optionally add `summary`/`connects_to`; move `templates/*` → `shapes/frame.*`; move the four framing docs into a Frames-first `Frames/` collection; rename the `product-owner` persona to `registry-owner`; trim `## Top-Level` (README first). Set `eidos_version: 4.1.0` when done.

## Worked example: 3.0.0 → 3.1.0

A small, additive move — nothing in a 3.0.0 registry breaks. Diffing `versions/v3.0.0.md` against `versions/v3.1.0.md` yields:

- **Form layer** — the shapes and the canonical property set are unchanged; the only edit to the `## Eidos Canonical` block is the `domain` property's wording, now "matching its folder … in the registry's naming convention." Rewrite the canonical block to the 3.1.0 seed and leave `## Custom Registry Properties` untouched.
- **`Registry.md` becomes YAML frontmatter.** The 3.0.0 bold-key lines move into frontmatter: `**Eidos Version:** 3.0.0` becomes an `eidos_version` key (bumped to `3.1.0`), and a `naming` key is added.
- **Naming** — set `naming: Title Case`: it is the prior behavior, so this just records what the registry already does. Switch to `TitleCase` or `kebab-case` only if the owner wants space-free names — which then means renaming the files, a separate and deliberate pass.
- **Top-level docs** — no migration. The registry may now add its own free-form top-level docs (a Roadmap, a Vision) via `eidos-format`, but nothing existing changes.

The net is the small `Registry.md` conversion plus the one-line Schema reword; items and top-level docs are otherwise untouched.

## Worked example: v2.x → 3.0.0

This is the move that introduces the form layer. Diffing `versions/v2.1.0.md` against `EIDOS.md` (3.0.0) yields:

- **Form layer** — install `Blueprint/.eidos/` from the canonical seed: `shapes/` (the body shapes, one per kind of doc), `Schema.md` (the canonical property block), and `Registry.md`. The body section set is unchanged from v2.1, so the Spec shape carries the same sections — they simply now live in `.eidos/shapes/Spec.md` instead of a standalone template.
- **Properties** — the canonical property set is otherwise the same as v2.1, with one removal: **`eidos_version` comes off every item and top-level doc** — the version is now a registry fact in `.eidos/Registry.md`. Frontmatter is otherwise unchanged.
- **Body** — no restructuring; v2.1 and 3.0.0 share the same baseline sections and `AC{n}` labeling.
- **Version** — write `**Eidos Version:** 3.0.0` into `.eidos/Registry.md`.

The net of v2 → v3 is small per file (drop `eidos_version`) but adds the `.eidos/` form layer once for the whole registry. Preserve any custom properties or reshaped sections — but a clean v2 registry won't have any yet.

## Worked example: v1.0.0 → 2.0.0

Diffing `versions/v1.0.0.md` against `versions/v2.0.0.md` yields:

- **Frontmatter** — remove `last_validated`, `implements`, `serves_job`, `activity`, `supersedes`; add `created` and `modified` (`YYYY-MM-DD`); remap `status` (`proposed`/`accepted` → `Intake`, `in-progress` → `In Progress`, `shipped` → `Done`, `deprecated` → `Deprecated`).
- **Body** — `## Behavior` → `## Behaviors & Acceptance Criteria`, label criteria `AC{n}` under `###` requirement sub-headings; merge `## Constraints` + `## Decisions` → `## Constraints & Decisions`; add `## Dependencies` and `## Testing` stubs; add an optional `### Implementation Notes` under Intent.
- **Structure** — root `product/` → `Blueprint/`; `Domains.md` bullet list → `##` sub-headings per domain.

Carry `last_validated`'s date into `modified` (and `created` if no better date exists), and surface any `supersedes`/`implements` targets for the human to record in prose `Dependencies` before dropping the fields. To go straight from v1 to v3, diff those two snapshots and combine this with the form-layer install above.
