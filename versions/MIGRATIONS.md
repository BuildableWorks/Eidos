# Migrations

The worked hop for every released version of the standard, newest first. `migrate` reads the one it needs; a reader can skim any of them to see what a release actually cost.

A migration is a **diff between two snapshots**, so these are conveniences, not a required path. To go from 1.0.0 to 4.3.0 you diff `versions/v1.0.0.md` against the target directly and apply the net change — you do not walk the list. Read a hop when you want the shortcuts and the judgment calls someone already worked out.

Each entry says what moves, what stays, and what needs a human decision.

## 4.3.2 → 4.4.0

**Write the definition's naming convention down, rename two things inside `_eidos/`, then set `eidos_version: 4.4.0`.**

4.4.0 changes one default: `kebab-case` is now what the standard recommends and what an absent `naming` key means. Through 4.3.2 an absent key meant `Title Case`. A definition that already carries the key is unaffected — the key is authoritative in both versions and only the fallback moved — so this is the whole migration for almost everyone: bump the version and stop.

For a definition with **no** `naming` key, settle it rather than letting the default decide:

- **Read the convention off the files.** The tree already answers the question. A collection folder or item filename containing a space means `Title Case`; space-free and capitalized (`WatchAVideo.md`) means `TitleCase`; lowercase and hyphenated (`watch-a-video.md`) means `kebab-case`. Check a couple of collections rather than one file, and if they disagree, that is a real inconsistency to surface, not something to average.
- **Confirm it with the owner, then write it into `_eidos/Framework.md`.** State what the files say and what you are about to record. Recording what the definition already does is not a change to it.
- **Adopting kebab-case is a separate, deliberate pass,** never bundled into the version bump — it renames every collection folder, sub-folder, and item file, rewrites every link, and lowercases each grouping property's value to match its folder (`domain: Channels` → `domain: channels`). Do it when the owner wants it.

Two smaller notes:

- **The canvas's default filename follows the convention** — `framework-map.canvas` under kebab-case, `FrameworkMap.canvas` under TitleCase, `Framework Map.canvas` under Title Case. `canvas` only picks the name when you don't pass `--out`, so an existing canvas keeps its name until you regenerate without one; if it does get renamed, update its bullet in `## Top-Level`.
- **`README.md` is now named as an exception** beside `_eidos/`: it keeps the name every tool already looks for, whatever the convention. Nothing to change — this writes down what every definition was already doing.

Two renames in the form layer come with this version, both mechanical. Nothing outside `_eidos/` moves.

- **`_eidos/personas/` → `_eidos/roles/`.** Same files, same contents, same filenames inside (`framework-owner.md` and the rest keep their names). "Persona" was borrowed from UX, where a persona is an archetype of a *customer*, which is what a framing doc about the audience holds, not what these files hold. These are response contracts for the person at the keyboard, and the standard was already reaching for "role" to explain them.
- **`_eidos/user.md` → `_eidos/me.md`.** Same file, same contents. "User" in a product definition means the product's users; this file is you. The concept is still the **actor**; only the filename changed.
- **Update the two pointers.** `_eidos/.gitignore` ignores `me.md` instead of `user.md` (still the one `_eidos/` file not committed), and `me.md`'s own link to its role file now points at `_eidos/roles/`.
- **In `me.md`, the first calibration axis is renamed** from "Role for this definition" to **Ownership**. It always asked what you own here, and with the contracts now called roles the old label read as "your role's role". Rewrite the label; keep the answer.
- **A definition that never had `personas/` or a `user.md` needs nothing.** Both are optional in practice: a framework with no roles installed, and an actor who never recorded themselves, both still work.

Custom roles a team wrote are theirs and travel as they are. If a framework had renamed or added role files, the folder move touches none of it.

**Nothing else moves.** No shape, no role, no property in the Schema, no body section.

## 4.3.1 → 4.3.2

**Set `eidos_version: 4.3.2`, or don't.**

The only change to the standard is its Versioning section, which now says that the plugin versions separately from the standard. Nothing a definition contains depends on it, so a definition left on 4.3.1 is not stale in any way that matters.

From here the two version lines diverge: a release that fixes a skill bumps the plugin and leaves `EIDOS.md` — and your `eidos_version` — alone.

## 4.3.0 → 4.3.1

**Set `eidos_version: 4.3.1`.** That is the whole migration.

The standard text is unchanged — `versions/v4.3.1.md` differs from `v4.3.0.md` only in its version lines. 4.3.1 shrank the skills and moved these worked hops out of `migrate` into this file. Nothing inside a definition is affected.

## 4.2.1 → 4.3.0

Additive, and the per-definition work is one bullet per collection. 4.3.0 takes the seed's own vocabulary out of the standard and the generators: `EIDOS.md` no longer names Intent, Out of Scope, Acceptance Criteria, or Implementation Notes in its Rules (the shape files already documented all four), and `build-canvas.py` no longer treats a collection called `Frames` as full-file nodes or looks for a section called `## Intent`.

- **Declare a `- **Canvas:**` bullet on every collection** in `_eidos/Framework.md`, under its `### ` heading beside **Leaf** and **Flavors**. It takes `file` (full-file nodes, for prose read whole), `card` (a text node embedding the whole item), or `card from ## Section` (a card embedding just that section). For a seed-derived definition the answers are `Frames` → `file` and `Specs` → `card from `## Intent``, which reproduce 4.2.x behavior exactly. For any collection the owner added, **ask** — the right answer depends on that shape, and there is no longer a name-based guess to fall back on.
- **Regenerate the canvas** with `canvas` if the definition has one. An undeclared collection now draws as a plain whole-item card, so a definition that skips the declarations gets a duller map, never a broken one.
- **Nothing else moves.** No item frontmatter, no body, no shape, no persona, no folder or file names. The removed Rules were duplicates of guidance already living in `_eidos/shapes/`, so a definition that customized its shapes keeps exactly what it wrote.
- **`owner` leaves the core Schema.** Delete its row from `### Eidos Core`. It was never read by any tool, and the actor file (`_eidos/user.md`) already says who is at the keyboard. **Don't strip `owner:` from items** — if a definition uses it, add it back as a row in `### Custom Properties` (Text, applies-to `all`) and every item keeps validating. If nobody uses it, leave the stray keys or clear them; either is fine.
- **Version.** Set `eidos_version: 4.3.0` in `_eidos/Framework.md`.

The net per definition: one `Canvas` bullet per collection, then set `eidos_version: 4.3.0`. Nothing else — the seeds and examples this release adds are repo-side, and where a framework was originally copied from has never been recorded in a definition.

## 4.2.0 → 4.2.1

The cheapest migration in the standard's history: **set `eidos_version: 4.2.1` in `_eidos/Framework.md`, and stop.** Nothing else in a definition changes.

4.2.1 fixes only what the two central words mean. Through 4.2.0 the standard called a whole `Blueprint/` a "framework"; from 4.2.1 the **framework** is the `_eidos/` form layer alone — collections, shapes, flavors, personas, naming, Schema — and the product written with it is the **definition**. One framework, many definitions.

- **No file or folder renames.** `_eidos/`, `Framework.md`, the shapes, the personas, and every collection folder keep their names. `Framework.md` names the framework more accurately now than it did before.
- **No property changes.** `### Eidos Core` is byte-identical to 4.2.0; only the version note above it moves to 4.2.1. Custom properties are untouched.
- **No persona rename.** `framework-owner` keeps its filename and its `# Framework Owner` heading — the role still holds intent, scope, and decisions. Any `user.md` naming it stays valid.
- **Optional prose pass.** If a definition's own `README.md` or top-level docs describe themselves as "this framework," reword them to "this definition." Cosmetic, and never required.

The net per definition: one line. Set `eidos_version: 4.2.1`.

## 4.1.0 → 4.2.0

A pure vocabulary-and-file rename — the per-product artifact becomes a **Framework**, not a "registry." No item frontmatter or body changes; the form layer's contents are untouched but for names. Diffing `versions/v4.1.0.md` against `EIDOS.md` (4.2.0) yields:

- **`_eidos/Registry.md` → `_eidos/Framework.md`.** Rename the index-and-contract file. Its body — `## Top-Level`, `## Collections`, `## Schema` (`### Eidos Core` + `### Custom Properties`) — is unchanged. Update the Top-Level regeneration marker from `<!-- eidos-registry: top-level index (regenerated) -->` to `<!-- configure: top-level index (regenerated) -->`.
- **`_eidos/personas/registry-owner.md` → `_eidos/personas/framework-owner.md`.** Same response contract; rename the file and its `# Registry Owner` heading → `# Framework Owner`, and fix the `[Registry Owner](registry-owner.md)` link in `_eidos/personas/README.md`. Any `user.md` naming the old persona is personal and gitignored — leave it, or point the actor at `whoami`.
- **Canvas.** If the definition has a generated "Registry Map" top-level doc, rename it "Framework Map" (the `.canvas` file and its `## Top-Level` bullet). `canvas` writes `Framework Map.canvas` from here on.
- **Version.** Set `eidos_version: 4.2.0` in `_eidos/Framework.md`.

Nothing else moves: the shapes, the Schema rows, every item's frontmatter and body, and the `_eidos/` directory name are identical to 4.1.0. Custom personas and custom properties carry across untouched. (The `eidos-registry`/`eidos-schema` → `configure` skill merge is a tooling change — nothing in a definition references a skill by name, so there's nothing per-definition to migrate for it.)

The net per definition: rename `Registry.md` → `Framework.md` (and its Top-Level marker), rename the `registry-owner` persona → `framework-owner`, optionally rename the Registry Map canvas → Framework Map. Set `eidos_version: 4.2.0`.

## 4.0.0 → 4.1.0

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
- **Registry** — in `_eidos/Registry.md`, declare `Frames` **first** in `## Collections` (framing docs are the most primary), then `Specs`; give Frames its four `frame.*` flavors (flat, no domains). Remove the four framing docs from `## Top-Level`, leaving only the owner's own top-level docs (a Roadmap, a Vision, the Registry Map). Bump `eidos_version` to `4.1.0`. Regenerate each collection's `index.md` with `index`.

The net per registry: rename `.eidos/` → `_eidos/`; merge `Schema.md` into `Registry.md`'s `## Schema` (Core + Custom, Applies To column); on every item rename the two date keys (and drop `type: frame` from frames); optionally add `summary`/`connects_to`; move `templates/*` → `shapes/frame.*`; move the four framing docs into a Frames-first `Frames/` collection; rename the `product-owner` persona to `registry-owner`; trim `## Top-Level` (README first). Set `eidos_version: 4.1.0` when done.

## 3.1.0 → 4.0.0

A breaking move — the layout changes — but the per-item contract barely does. Diffing `versions/v3.1.0.md` against `versions/v4.0.0.md` yields (note: migrating straight to the current version instead folds the framing docs into the `Frames` collection — see the 4.0 → 4.1 example below — rather than into a `templates/` folder):

- **Properties** — the canonical block gains one **optional** property, `flavor` (Text, no): which body flavor an item follows, absent meaning the collection's default. Rewrite `## Eidos Canonical` to the 4.0.0 seed and leave `## Custom Registry Properties` untouched. Nothing to backfill — absent already means default.
- **Shapes, templates, flavors** — rename `.eidos/shapes/Spec.md` → `spec.full.md` (the Specs collection's default flavor) and offer to add `spec.micro.md` from the seed. Remove the `Domains.md` shape (the Domains doc is gone). **Move the top-level-doc shapes (`Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md`) from `.eidos/shapes/` into a new `.eidos/templates/`** — shapes are now collection-only; top-level docs use templates. Spec sections are unchanged, so items need no body restructuring.
- **`Domains.md` → `Specs/index.md`** (the breaking change). Move the top-level `Domains.md` into a generated `Specs/index.md` leaf inside the collection — the per-item listing, links now relative to `Specs/`. Lift the domain **descriptions** up into the Registry's Collections section (under Specs → Domains), since the leaf is purely generated. Regenerate the leaf with `index`.
- **`Registry.md` gains a body.** Frontmatter unchanged but for the version bump to `4.0.0`. Add the body: a `## Top-Level` (a bullet per top-level doc — link + the owner's one-line description) and a `## Collections` declaring the default `Specs` collection with its flavors (`full` default, `micro` if added), its domain grouping (with the descriptions lifted from `Domains.md`), and a pointer to `Specs/index.md`.
- **`README.md` start-here** — install the chosen seed's `README.md` → `<root>/README.md` and fill the product name; it is the visible front door into the Registry.
- **Personas + the actor file** — install the seed's persona defaults (`personas/` → `.eidos/personas/`), its blank `user.md` → `.eidos/user.md`, and its `.gitignore` → `.eidos/.gitignore` (merge a `user.md` line into an existing `.eidos/.gitignore` rather than overwriting it). Then run `whoami` so each actor sets their persona and calibration.
- **Specs** — untouched; bodies and frontmatter already conform, and `flavor` is optional, defaulting to `full`.

The net per registry: add the optional `flavor`; rename the shape; relocate `Domains.md` → `Specs/index.md` (descriptions up to the Registry); add the Registry body, a root `README.md`, `.eidos/personas/`, and `.eidos/user.md` + `.eidos/.gitignore`. No per-item body edits. Set `eidos_version: 4.0.0` when done.

## 3.0.0 → 3.1.0

A small, additive move — nothing in a 3.0.0 registry breaks. Diffing `versions/v3.0.0.md` against `versions/v3.1.0.md` yields:

- **Form layer** — the shapes and the canonical property set are unchanged; the only edit to the `## Eidos Canonical` block is the `domain` property's wording, now "matching its folder … in the registry's naming convention." Rewrite the canonical block to the 3.1.0 seed and leave `## Custom Registry Properties` untouched.
- **`Registry.md` becomes YAML frontmatter.** The 3.0.0 bold-key lines move into frontmatter: `**Eidos Version:** 3.0.0` becomes an `eidos_version` key (bumped to `3.1.0`), and a `naming` key is added.
- **Naming** — set `naming: Title Case`: it is the prior behavior, so this just records what the registry already does. Switch to `TitleCase` or `kebab-case` only if the owner wants space-free names — which then means renaming the files, a separate and deliberate pass.
- **Top-level docs** — no migration. The registry may now add its own free-form top-level docs (a Roadmap, a Vision) via `format`, but nothing existing changes.

The net is the small `Registry.md` conversion plus the one-line Schema reword; items and top-level docs are otherwise untouched.

## v2.x → 3.0.0

This is the move that introduces the form layer. Diffing `versions/v2.1.0.md` against `EIDOS.md` (3.0.0) yields:

- **Form layer** — install `Blueprint/.eidos/` from the canonical seed: `shapes/` (the body shapes, one per kind of doc), `Schema.md` (the canonical property block), and `Registry.md`. The body section set is unchanged from v2.1, so the Spec shape carries the same sections — they simply now live in `.eidos/shapes/Spec.md` instead of a standalone template.
- **Properties** — the canonical property set is otherwise the same as v2.1, with one removal: **`eidos_version` comes off every item and top-level doc** — the version is now a registry fact in `.eidos/Registry.md`. Frontmatter is otherwise unchanged.
- **Body** — no restructuring; v2.1 and 3.0.0 share the same baseline sections and `AC{n}` labeling.
- **Version** — write `**Eidos Version:** 3.0.0` into `.eidos/Registry.md`.

The net of v2 → v3 is small per file (drop `eidos_version`) but adds the `.eidos/` form layer once for the whole registry. Preserve any custom properties or reshaped sections — but a clean v2 registry won't have any yet.

## v1.0.0 → 2.0.0

Diffing `versions/v1.0.0.md` against `versions/v2.0.0.md` yields:

- **Frontmatter** — remove `last_validated`, `implements`, `serves_job`, `activity`, `supersedes`; add `created` and `modified` (`YYYY-MM-DD`); remap `status` (`proposed`/`accepted` → `Intake`, `in-progress` → `In Progress`, `shipped` → `Done`, `deprecated` → `Deprecated`).
- **Body** — `## Behavior` → `## Behaviors & Acceptance Criteria`, label criteria `AC{n}` under `###` requirement sub-headings; merge `## Constraints` + `## Decisions` → `## Constraints & Decisions`; add `## Dependencies` and `## Testing` stubs; add an optional `### Implementation Notes` under Intent.
- **Structure** — root `product/` → `Blueprint/`; `Domains.md` bullet list → `##` sub-headings per domain.

Carry `last_validated`'s date into `modified` (and `created` if no better date exists), and surface any `supersedes`/`implements` targets for the human to record in prose `Dependencies` before dropping the fields. To go straight from v1 to v3, diff those two snapshots and combine this with the form-layer install above.
