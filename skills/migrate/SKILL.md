---
name: migrate
description: >-
  Migrate a root from one version of the Eidos standard to another: "migrate our specs to Eidos 5.3", "we bumped the standard, update the folder", "these specs are on the old format". Migrations are non-sequential: diff the source and target snapshots directly and apply the net change.
---

# Eidos Migrate

A migration is a diff between two standard snapshots, applied to the root. Go straight from the source to the target; never step through intermediate versions.

## Facilitate, don't bulldoze

It is still the owner's folder. Propose the plan, show what will change, and never silently drop content: where the target removes a field or section holding real information, surface it and ask where it goes. Custom properties, the Vocabulary, reshaped templates, every `properties.tools.<tool>` block, every region, and everything under `.eidos/plugins/` are the owner's or a tool's and are carried across untouched.

## What you read

Committed copies in this folder, synced by `scripts/sync-skills.sh`:

- `versions/vX.Y.Z.md`: every released standard. A migration needs both endpoints.
- `versions/MIGRATIONS.md`: the worked hop for each release, newest first. Read the ones spanning your endpoints.
- `versions/README.md`: one line per release, for finding the source by its fingerprint.
- `EIDOS.md`: the current standard, the usual target.
- `seeds/`: for a pre-3.0 root that needs a framework installed.

If a snapshot is missing, say so. Never fabricate a version's contract.

## Procedure

1. **Target.** The current `EIDOS.md` unless told otherwise.

2. **Source.** Read the version from the framework document: `.eidos/Framework.yaml` (5.0.0+), `_eidos/Framework.md` (4.2 to 4.7), `_eidos/Registry.md` (4.1), `.eidos/Registry.md` (3.0 to 4.0). Pre-3.0 roots have no structure directory; fingerprint the files (`last_validated` and `## Behavior` are 1.x; `created`/`modified` with `AC{n}` labels are 2.x) and confirm with the owner. `versions/README.md` has the rest.

3. **Diff the snapshots** across four concerns: the structure layer (its name and files), properties (added, removed, renamed, re-valued), templates (sections renamed, merged, split, added, removed), and layout (root, folders, generated files). Diffing the endpoints resolves a field renamed twice to its net state on its own.

4. **Write the plan**: each transform per concern, and every point needing a human decision. Show it before touching files.

5. **Apply, in order.**
   - The structure layer first. A root with none gets a seed installed whole (ask which; across a device bridge, send the files with the file-delivery tool in one call, never re-typed or archived). A root with one has its directory and document renamed to the target's names, then only the standard's core block rewritten.
   - Each blueprint: map frontmatter onto the target's Properties, drop removed fields after surfacing their content, add newly required ones as stubs, restructure the body to the target variant's template with new sections as flagged empty stubs.
   - Structural changes across the folder (renamed keys, moved folders).
   - Set `eidos_version` in the framework document.

6. **Validate** with the `eidos` pass against the target and report gaps as suggestions.

7. **Report** per file: what changed, what carried over, what still needs a decision.

## Recent hops in one line each

Full detail in `versions/MIGRATIONS.md`.

- **5.3.0**: `collections:` becomes `folders:` with `type: collection` on each entry; a folder may also be `assets` or `other`; every folder and file at the root must be declared; every sub-folder of a collection is a declared group. Rename the key, add the type, then walk the root: offer a declaration or a move for anything undeclared, ask before dropping an entry with nothing behind it.
- **5.2.1**: prose only; bump.
- **5.2.0**: `options` on a property entry (offer to move a `meaning` that lists values); `plugins/*/local.yaml` added to `.eidos/.gitignore`.
- **5.1.0**: regions and `required` on property entries; rewrite the core with `id` and `title` required.
- **5.0.0**: `_eidos/` back to `.eidos/`, `shapes/` to `templates/`, `flavor` to `variant`, `Schema` to `Properties`, one `Framework.yaml` with the index inside; `versions` key dropped.
