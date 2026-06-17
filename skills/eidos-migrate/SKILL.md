---
name: eidos-migrate
description: >-
  Migrate Eidos specs and product docs from one version of the standard to another. Use whenever someone wants to upgrade, migrate, or bring specs up to date with a new Eidos version — e.g. "migrate our specs to Eidos 2.0", "we bumped the standard, update the specs", "bring this registry to the latest format", or "what changed between Eidos v1 and v3 and how do I move my specs over". Migrations are non-sequential: go directly from any source version to any target (v1.0.0 → v3.1.0) by diffing the two version snapshots. Trigger even when the user doesn't say "migrate" — "these specs are on the old format" or "update the frontmatter to the new schema" apply too.
---

# Eidos Migrate

Move a registry's specs and product docs from one version of the Eidos standard to another. A migration is a **diff between two standard snapshots**, applied to each file. You do not step through intermediate versions — to go from v1.0.0 to v3.1.0, you diff those two snapshots directly and apply the net change.

This skill is the companion to `eidos` (authoring/validation). Read `eidos` for the target contract; read this when the contract itself has moved and files need to catch up.

## How you work: facilitate, don't bulldoze

Migration is mechanical, but it is still the owner's registry. Propose the plan, show what will change, and **never silently drop content**. If the target version removes a field or section that holds real information, surface that information and ask where it should go (fold into another section, keep as a note, or deliberately drop) — do not delete it on the user's behalf.

## Where the version history lives

Migration needs the version snapshots, the changelog's migration notes, and the current standard. Find them in whichever location exists:

- **`${CLAUDE_PLUGIN_ROOT}/`** (installed as the plugin) — `${CLAUDE_PLUGIN_ROOT}/versions/`, `${CLAUDE_PLUGIN_ROOT}/CHANGELOG.md`, and the current `${CLAUDE_PLUGIN_ROOT}/EIDOS.md`.
- **This skill's own `versions/`, `CHANGELOG.md`, and `EIDOS.md`** — present when the skill was made standalone by `scripts/sync-skills.sh`. These are gitignored, so run that script first if they're missing.
- **The repo's top-level files** — when working inside the standard's own repo.

`versions/vX.Y.Z.md` is a frozen snapshot of every prior released standard; `CHANGELOG.md` holds the per-version migration notes; `EIDOS.md` is the current standard and the usual target. A migration needs both endpoints — the source's snapshot (or its changelog notes) and the target. If a needed snapshot is missing, say so; never fabricate a version's contract.

## Procedure

1. **Establish the target.** Default to the current `EIDOS.md`. If migrating to a non-current version, use its `versions/` snapshot.

2. **Establish the source.** Check the `eidos_version` frontmatter first — if a doc declares it, that is the source. Otherwise (older docs predate the field) detect it from the file shape and confirm with the user. Fingerprints:

   - **v1.x** — frontmatter has `last_validated`, `implements`, `serves_job`, `activity`, or `supersedes`; body uses `## Behavior`, separate `## Constraints` and `## Decisions`; `status` is lowercase (`proposed`, `in-progress`, …); root folder is `product/`.
   - **v2.0.0** — frontmatter has `created`/`modified`; body uses `## Behaviors & Acceptance Criteria` with `AC{n}` labels, `## Dependencies`, `## Testing`, merged `## Constraints & Decisions`; `status` is Title Case. When unsure, ask the user which version the specs are on.

3. **Diff the two snapshots.** Compare the source and target standards and derive the net transformation:

   - **Frontmatter** — fields added, removed, renamed, or with changed value sets (e.g. an enum remap).
   - **Body** — sections renamed, merged, split, added, or removed; labeling conventions (e.g. `AC{n}`).
   - **Structure/naming** — root folder name, `Domains.md` format, file layout. Because you diff the two endpoints, a field that was dropped and later reintroduced, or renamed twice, resolves to its correct net state automatically.

4. **Write the migration plan.** A short, per-concern list of every transform, plus anything that needs human judgment (removed fields/sections that hold content). Show it before touching files.

5. **Apply per file**, once the plan is agreed:

   - Rename and remap frontmatter; drop removed fields _after_ surfacing any content they held; add newly-required fields (leave values for the human where they can't be derived, e.g. `created`).
   - Restructure the body: rename/merge/split sections, apply labeling, and add new recommended sections as empty stubs flagged for the human to fill — never invent their contents.
   - Apply structural/naming changes (e.g. `product/` → `Blueprint/`, `Domains.md` list → sub-headings) across the registry.

6. **Validate.** Run the `eidos` validation pass against the **target** contract and report remaining gaps as suggestions, not failures.

7. **Report.** Summarize per file: what changed, what was carried over, and every place a human decision is still needed.

## Worked example: v1.0.0 → 2.0.0

Diffing `versions/v1.0.0.md` against `EIDOS.md` (2.0.0) yields:

- **Frontmatter** — remove `last_validated`, `implements`, `serves_job`, `activity`, `supersedes`; add `created` and `modified` (`YYYY-MM-DD`); remap `status` (`proposed`/`accepted` → `Intake`, `in-progress` → `In Progress`, `shipped` → `Done`, `deprecated` → `Deprecated`).
- **Body** — `## Behavior` → `## Behaviors & Acceptance Criteria`, label criteria `AC{n}` under `###` requirement sub-headings; merge `## Constraints` + `## Decisions` → `## Constraints & Decisions`; add `## Dependencies` and `## Testing` stubs; add an optional `### Implementation Notes` under Intent.
- **Structure** — root `product/` → `Blueprint/`; `Domains.md` bullet list → `##` sub-headings per domain.

Carry `last_validated`'s date into `modified` (and `created` if no better date exists), and surface any `supersedes`/`implements` targets for the human to record in prose `Dependencies` before dropping the fields.
