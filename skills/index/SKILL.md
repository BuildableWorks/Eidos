---
name: index
description: >-
  Rebuild the generated `index` key in a project's (a root's) `.eidos/Framework.yaml`, one list per collection, so a human or agent finds a blueprint without scraping the tree. Use for "regenerate the index", "reindex the blueprints", "the index is stale", or after blueprints are added, renamed, moved, or removed. Runs `eidos index` where there is a shell; does the walk by hand otherwise. Regenerable, never gates.
---

# Eidos Index

The index is derived, not written: each entry is a blueprint's own `id`, `title`, `summary`, `path` (relative to the collection folder), and `folder` (the path of its folder from the collection, null at the top). Rewrite the `index` key wholesale and touch nothing else in the document.

## Run the CLI when you can

```
eidos index      # rebuild every collection's index
eidos check      # reports a stale index, among the rest
```

Where `eidos` is missing, `curl -fsSL https://eidosmd.com/install | sh` (macOS, Linux) or `irm https://eidosmd.com/install.ps1 | iex` (Windows) installs it. It names every blueprint missing a `summary`; writing those (one plain line, distilled from Intent, on the blueprint itself) is your only authoring task. Then run it again. On a sandboxed host, do the walk by hand; the procedure is exactly what the CLI does.

## Procedure

1. Read `.eidos/me.md`, then the `folders` of type `collection` in `Framework.yaml`. No `.eidos/` means offer `install`.
2. For each collection, walk its folder to any depth: the blueprints at the top and in every folder beneath it. Ignore any file that is not markdown. Read each blueprint's `id`, `title`, and `summary`.
3. Take `summary` verbatim. A blueprint without one is listed with `summary: null` and flagged; write the summary on the blueprint, never into the index alone.
4. Rewrite the `index` key: one list per collection in declared order, entries in file order, folder by folder, depth first.

   ```yaml
   index:
     Specs:
       - { id: magic-link-sign-in, title: Magic Link Sign-In, summary: "passwordless sign-in by an emailed single-use link.", path: identity/magic-link-sign-in.md, folder: identity }
       - { id: session-management, title: Session Management, summary: null, path: identity/session-management.md, folder: identity }
   ```

5. Reconcile: a declared folder with no folder on disk is flagged; where the collection sets `undeclared_folders: false`, a folder it does not declare is asked about, not invented (`configure`); where it sets `loose_files: false`, a blueprint outside a deepest folder is flagged.
6. Report the blueprints indexed, those still missing a `summary`, and any folder to reconcile.

Idempotent: running it again yields the same key plus any new blueprints. It annotates and navigates; it never validates.
