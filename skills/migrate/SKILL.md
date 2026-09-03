---
name: migrate
description: >-
  Migrate a root — its blueprints and top-level docs — from one version of the standard to another. Use whenever someone wants to upgrade, migrate, or bring a root up to date with a new Eidos version — e.g. "migrate our specs to Eidos 3.0", "we bumped the standard, update the specs", "bring this folder to the latest format", or "what changed between Eidos v1 and v3 and how do I move my specs over". Migrations are non-sequential: go directly from any source version to any target (v1.0.0 → v3.0.0) by diffing the two version snapshots. Trigger even when the user doesn't say "migrate" — "these specs are on the old format" or "update the frontmatter to the new schema" apply too.
---

# Eidos Migrate

Move a root's blueprints and top-level docs from one version of the Eidos standard to another. A migration is a **diff between two standard snapshots**, applied to the folder. You do not step through intermediate versions — to go from v1.0.0 to v3.0.0, you diff those two snapshots directly and apply the net change.

This skill is the companion to `eidos` (authoring/validation). Read `eidos` for the target contract; read this when the contract itself has moved and files need to catch up.

## How you work: facilitate, don't bulldoze

Migration is mechanical, but it is still the owner's folder. Propose the plan, show what will change, and **never silently drop content**. If the target version removes a field or section that holds real information, surface that information and ask where it should go (fold into another section, keep as a note, or deliberately drop) — do not delete it on the user's behalf. The custom part of a root's framework — its custom properties, any reshaped section — is the owner's and is preserved, never overwritten.

## What you read

Committed copies live in this skill's own folder, synced from the standard by `scripts/sync-skills.sh`, so they are present on a sandboxed host too:

- **`versions/vX.Y.Z.md`** — a frozen snapshot of each released standard. A migration needs both endpoints.
- **`versions/MIGRATIONS.md`** — the worked hop for each release: what moves, what stays, what needs a human decision. Read the one spanning your source and target; it is a shortcut, not a required path.
- **`EIDOS.md`** — the current standard, and the usual target.
- **`seeds/`** — every seed, for when a pre-v3 folder needs a structure layer installed.

If a needed snapshot is missing, say so; never fabricate a version's contract.

## Procedure

1. **Establish the target.** Default to the current `EIDOS.md`. If migrating to a non-current version, use its `versions/` snapshot.

2. **Establish the source.** Check for the structure-layer directory — `_eidos/` (v4.1+) or `.eidos/` (v3.0–v4.0) — and read its index file — `Framework.md` (v4.2+) or `Registry.md` (v3.0–v4.1) — where a v3+ folder declares its version. If there is neither (pre-v3), detect the source from the file shape and confirm with the user. Fingerprints:

   - **v1.x** — frontmatter has `last_validated`, `implements`, `serves_job`, `activity`, or `supersedes`; body uses `## Behavior`, separate `## Constraints` and `## Decisions`; `status` is lowercase (`proposed`, `in-progress`, …); root folder is `product/`.
   - **v2.x** — frontmatter has `created`/`modified` and often a per-doc `eidos_version`; body uses `## Behaviors & Acceptance Criteria` with `AC{n}` labels, merged `## Constraints & Decisions`; `status` is Title Case; **no structure-layer directory**.
   - **v3.0–v4.0** — has a structure-layer directory named **`.eidos/`** (`shapes/`, `Schema.md`, `Registry.md`); the version is in `Registry.md`; blueprints carry no `eidos_version`. **v4.1** is identical but the directory is renamed **`_eidos/`** (the dot dropped so Obsidian shows it). **v4.2+** additionally renames the index file `Registry.md` → **`Framework.md`**; the `registry-owner` role is `framework-owner`. **v4.2.1** settles the vocabulary: the `_eidos/` structure layer is the *framework*, the product written with it is the *folder*. Prose only. **v4.3.0** adds a `- **Canvas:**` bullet to each collection in `Framework.md`; a root without one still loads, and draws every collection as a plain card. **v4.4.0** renames `_eidos/personas/` → `_eidos/roles/` and `_eidos/user.md` → `_eidos/me.md` (a root still on the old names is pre-4.4.0), and flips the naming default: an absent `naming` key means `kebab-case` where it used to mean `Title Case`. A root carrying the key is unaffected; for one without it, read the convention off its own filenames (a space means Title Case, space-free and capitalized means TitleCase, lowercase and hyphenated means kebab-case), confirm it, and write it down before bumping.

3. **Diff the two snapshots.** Check `versions/MIGRATIONS.md` first — if a hop spanning your endpoints is written up, it has the shortcuts already. Then derive the net transformation across four concerns: **the structure layer** (does the target keep one, and under what name), **properties** (fields added, removed, renamed, or re-valued, mapped onto the target Schema), **body shape** (sections renamed, merged, split, added, removed, and any labeling), and **layout** (root folder, collection layout, generated leaves).

   Diffing the endpoints means a field dropped and later reintroduced, or renamed twice, resolves to its correct net state automatically.

4. **Write the migration plan.** A short, per-concern list of every transform, plus anything that needs human judgment (removed fields/sections that hold content, a custom shape that conflicts). Show it before touching files.

5. **Apply, once the plan is agreed.** Order matters when the structure layer is involved:

   - **The structure layer first.** If the target has one and the folder doesn't, **ask which seed** and install it whole into the structure dir. The seed ships inside this skill and the folder may be on another machine: across a device bridge, send the seed files with the file-delivery tool and write them to their final paths in a single call. Never re-type contents, base64, or a tarball through a heredoc, and never stage an archive inside the repo. If the folder already has one, rename the directory and its index file to the target's names, then rewrite **only** the standard-managed core block — leave the framework's custom properties untouched, and offer new canonical shapes additively rather than overwriting a customized one. The per-version names are in `versions/MIGRATIONS.md`.
   - **Migrate each blueprint** (across every collection). Map frontmatter onto the target Schema's properties; drop removed fields _after_ surfacing any content they held; add newly-required fields as stubs the human fills (e.g. `date_created` where none can be derived). Restructure the body to the target flavor's shape, applying labeling; add new recommended sections only as clearly-flagged empty stubs — never invent their contents.
   - **Apply structural/naming changes** across the folder (e.g. `product/` → `Blueprint/`).
   - **Set the version.** Write the target version into the structure dir's index file — `_eidos/Framework.md` for 4.2+, `_eidos/Registry.md` for 3.0–4.1 (creating it if new).

6. **Validate.** Run the `eidos` validation pass against the **target** Schema and report remaining gaps as suggestions, not failures.

7. **Report.** Summarize per file: what changed, what was carried over, and every place a human decision is still needed.
