---
name: eidos-migrate
description: >-
  Migrate Eidos specs and product docs from one version of the standard to another. Use whenever someone wants to upgrade, migrate, or bring specs up to date with a new Eidos version — e.g. "migrate our specs to Eidos 3.0", "we bumped the standard, update the specs", "bring this registry to the latest format", or "what changed between Eidos v1 and v3 and how do I move my specs over". Migrations are non-sequential: go directly from any source version to any target (v1.0.0 → v3.0.0) by diffing the two version snapshots. Trigger even when the user doesn't say "migrate" — "these specs are on the old format" or "update the frontmatter to the new schema" apply too.
---

# Eidos Migrate

Move a registry's specs and product docs from one version of the Eidos standard to another. A migration is a **diff between two standard snapshots**, applied to the registry. You do not step through intermediate versions — to go from v1.0.0 to v3.0.0, you diff those two snapshots directly and apply the net change.

This skill is the companion to `eidos` (authoring/validation). Read `eidos` for the target contract; read this when the contract itself has moved and files need to catch up.

## How you work: facilitate, don't bulldoze

Migration is mechanical, but it is still the owner's registry. Propose the plan, show what will change, and **never silently drop content**. If the target version removes a field or section that holds real information, surface that information and ask where it should go (fold into another section, keep as a note, or deliberately drop) — do not delete it on the user's behalf. The custom part of a registry's form — its custom properties, any reshaped section — is the owner's and is preserved, never overwritten.

## Where the version history lives

Migration needs the version snapshots, the changelog's migration notes, the current standard, and — when bringing a registry up to a version that has a form layer — the canonical `.eidos/` seed. Find them where the standard lives:

These ship as committed copies inside this skill's own folder — `versions/`, `CHANGELOG.md`, `EIDOS.md`, and `standard-seed/` — kept in sync with the standard's top-level sources by `scripts/sync-skills.sh`. So they're present whether you're in Claude Code or a sandboxed host (Claude Desktop). The top-level files stay the source of truth; these are synced copies. When working inside the standard's own repo, the top-level files are right there.

`versions/vX.Y.Z.md` is a frozen snapshot of each released standard; `CHANGELOG.md` holds the per-version migration notes; `EIDOS.md` is the current standard and the usual target. A migration needs both endpoints. If a needed snapshot is missing, say so; never fabricate a version's contract.

## Procedure

1. **Establish the target.** Default to the current `EIDOS.md`. If migrating to a non-current version, use its `versions/` snapshot.

2. **Establish the source.** Check `.eidos/Registry.md` first — a v3+ registry declares its version there. If there is no `.eidos/` (pre-v3), detect the source from the file shape and confirm with the user. Fingerprints:

   - **v1.x** — frontmatter has `last_validated`, `implements`, `serves_job`, `activity`, or `supersedes`; body uses `## Behavior`, separate `## Constraints` and `## Decisions`; `status` is lowercase (`proposed`, `in-progress`, …); root folder is `product/`.
   - **v2.x** — frontmatter has `created`/`modified` and often a per-doc `eidos_version`; body uses `## Behaviors & Acceptance Criteria` with `AC{n}` labels, merged `## Constraints & Decisions`; `status` is Title Case; **no `.eidos/` form layer**.
   - **v3.x** — has a `.eidos/` form layer (`shapes/`, `Schema.md`, `Registry.md`); the version is in `Registry.md`; specs carry no `eidos_version`.

3. **Diff the two snapshots.** Compare source and target and derive the net transformation across four concerns:

   - **The form layer** — whether the target keeps the form in a `.eidos/` (v3+) the source lacked. Going to v3, this is the headline change: the registry gains `.eidos/shapes/`, `.eidos/Schema.md`, and `.eidos/Registry.md`.
   - **Properties (frontmatter)** — fields added, removed, renamed, or with changed value sets. In v3 the contract is the Schema, so map the source's per-spec fields onto the target Schema's canonical (+ custom) properties.
   - **Body/shape** — sections renamed, merged, split, added, or removed; labeling conventions (`AC{n}`).
   - **Structure/naming** — root folder name, `Domains.md` format, file layout.

   Because you diff the two endpoints, a field dropped and later reintroduced, or renamed twice, resolves to its correct net state automatically.

4. **Write the migration plan.** A short, per-concern list of every transform, plus anything that needs human judgment (removed fields/sections that hold content, a custom shape that conflicts). Show it before touching files.

5. **Apply, once the plan is agreed.** Order matters when the form layer is involved:

   - **Install or update the form layer first.** If the target has a `.eidos/` and the registry has none, install the canonical seed (`shapes/`, `Schema.md`, `Registry.md`) into `Blueprint/.eidos/`. If the registry already has a `.eidos/`, rewrite only the Schema's `## Eidos Canonical` block to the target version and **leave `## Custom Registry Properties` untouched**; offer any new or changed canonical shapes additively, never overwriting a shape the owner has customized.
   - **Migrate each spec.** Map frontmatter onto the target Schema's properties; drop removed fields _after_ surfacing any content they held; add newly-required fields as stubs the human fills (e.g. `created` where none can be derived). Restructure the body to the target shape, applying labeling; add new recommended sections only as clearly-flagged empty stubs — never invent their contents.
   - **Apply structural/naming changes** across the registry (e.g. `product/` → `Blueprint/`).
   - **Set the version.** Write the target version into `.eidos/Registry.md` (creating it if new).

6. **Validate.** Run the `eidos` validation pass against the **target** Schema and report remaining gaps as suggestions, not failures.

7. **Report.** Summarize per file: what changed, what was carried over, and every place a human decision is still needed.

## Worked example: 3.0.0 → 3.1.0

A small, additive move — nothing in a 3.0.0 registry breaks. Diffing `versions/v3.0.0.md` against `EIDOS.md` (3.1.0) yields:

- **Form layer** — the shapes and the canonical property set are unchanged; the only edit to the `## Eidos Canonical` block is the `domain` property's wording, now "matching its folder … in the registry's naming convention." Rewrite the canonical block to the 3.1.0 seed and leave `## Custom Registry Properties` untouched.
- **`Registry.md` becomes YAML frontmatter.** The 3.0.0 bold-key lines move into frontmatter: `**Eidos Version:** 3.0.0` becomes an `eidos_version` key (bumped to `3.1.0`), and a `naming` key is added.
- **Naming** — set `naming: Title Case`: it is the prior behavior, so this just records what the registry already does. Switch to `TitleCase` or `kebab-case` only if the owner wants space-free names — which then means renaming the files, a separate and deliberate pass.
- **Top-level docs** — no migration. The registry may now add its own free-form top-level docs (a Roadmap, a Vision) via `eidos-format`, but nothing existing changes.

The net is the small `Registry.md` conversion plus the one-line Schema reword; specs and product docs are otherwise untouched.

## Worked example: v2.x → 3.0.0

This is the move that introduces the form layer. Diffing `versions/v2.1.0.md` against `EIDOS.md` (3.0.0) yields:

- **Form layer** — install `Blueprint/.eidos/` from the canonical seed: `shapes/` (the body shapes, one per kind of doc), `Schema.md` (the canonical property block), and `Registry.md`. The body section set is unchanged from v2.1, so the Spec shape carries the same sections — they simply now live in `.eidos/shapes/Spec.md` instead of a standalone template.
- **Properties** — the canonical property set is otherwise the same as v2.1, with one removal: **`eidos_version` comes off every spec and product doc** — the version is now a registry fact in `.eidos/Registry.md`. Frontmatter is otherwise unchanged.
- **Body** — no restructuring; v2.1 and 3.0.0 share the same baseline sections and `AC{n}` labeling.
- **Version** — write `**Eidos Version:** 3.0.0` into `.eidos/Registry.md`.

The net of v2 → v3 is small per file (drop `eidos_version`) but adds the `.eidos/` form layer once for the whole registry. Preserve any custom properties or reshaped sections — but a clean v2 registry won't have any yet.

## Worked example: v1.0.0 → 2.0.0

Diffing `versions/v1.0.0.md` against `versions/v2.0.0.md` yields:

- **Frontmatter** — remove `last_validated`, `implements`, `serves_job`, `activity`, `supersedes`; add `created` and `modified` (`YYYY-MM-DD`); remap `status` (`proposed`/`accepted` → `Intake`, `in-progress` → `In Progress`, `shipped` → `Done`, `deprecated` → `Deprecated`).
- **Body** — `## Behavior` → `## Behaviors & Acceptance Criteria`, label criteria `AC{n}` under `###` requirement sub-headings; merge `## Constraints` + `## Decisions` → `## Constraints & Decisions`; add `## Dependencies` and `## Testing` stubs; add an optional `### Implementation Notes` under Intent.
- **Structure** — root `product/` → `Blueprint/`; `Domains.md` bullet list → `##` sub-headings per domain.

Carry `last_validated`'s date into `modified` (and `created` if no better date exists), and surface any `supersedes`/`implements` targets for the human to record in prose `Dependencies` before dropping the fields. To go straight from v1 to v3, diff those two snapshots and combine this with the form-layer install above.
