---
name: install
description: >-
  Stand up a new Eidos root in a repo that has none: "set up eidos", "init the blueprints", "scaffold our product docs", "start documenting our product". Offers the seed frameworks (software, book, research), installs the chosen one into `.eidos/`, and scaffolds its folders. For a root that already exists, use `eidos` or `migrate`.
---

# Eidos Install

Create a fresh root from a seed. Scaffold structure and blank templates; write no content. Intent, scope, and decisions are the owner's; ask for the few things you need and hand off to `eidos`.

## The seeds

A committed copy of `seeds/` ships in this folder. Each is a complete framework: `templates/`, `roles/`, `Framework.yaml`, `me.md`, `.gitignore` (all installed into `.eidos/`) and a `README.md` (installed at the root). Read them at runtime rather than trusting a table: `eidos seeds` prints every seed's version and folders in one call; by hand, read each seed's `Framework.yaml` `folders` key.

## Run the CLI when you can

With a shell (`npx eidosmd` runs it uninstalled):

```
eidos seeds
eidos init <root> --seed <seed> --naming "<convention>" --group "<Group>" --product "<Name>"
```

It installs the seed, sets `naming`, renames folders into the convention, creates every declared folder and group, scaffolds one blank blueprint per framing variant, adds the starting groups to `grouping.groups`, and builds the index. It writes no prose. `--dry-run` shows every write. On a sandboxed host, do steps 5 and 6 by hand; they are exactly what it does.

## Procedure

1. **Confirm it's a fresh start.** An `.eidos/` anywhere in the tree is a root; if one exists, stop and point to `eidos` or `migrate`.
2. **Choose the seed.** Ask what the owner is defining, not which seed they want. A seed is a starting point, not a commitment; one that is close is fine, and `software` is the default only when the repo is code.
3. **Name the root.** Default `Blueprints/`. Nothing points at it by path, so any name works.
4. **Choose `naming`.** kebab-case (default), TitleCase, or Title Case. It governs the whole root and changing it later means renaming files.
5. **Install the framework.** Copy the seed into `<root>/.eidos/`, all but `README.md`, which goes to `<root>/README.md`. Set `naming`. Take every file from one seed; roles are written against their own folders. Across a device bridge, send the files with the file-delivery tool and write them to their final paths in one call; never re-type, base64, or archive them.
6. **Scaffold the folders.** Read `folders` from the installed `Framework.yaml` and create each in the convention: the framing collection with one blank blueprint per variant (frontmatter from the Properties table, body from the template, prompts kept), the grouped collection with a sub-folder per starting group the owner names (each added to `grouping.groups` with a description they supply), the `assets` folder, and any other. Fill the README's name and one line. Leave `top_level` at the README and `vocabulary` empty. Build the index.
7. **Set who you are.** Run `whoami` into `.eidos/me.md`. Blank is fine.
8. **Hand off.** Report the seed, what landed in `.eidos/`, and the folders scaffolded; point to `eidos` to author.

## After

Commit the root, `.eidos/` and all; the seeded `.gitignore` keeps out `me.md` and any tool's `plugins/*/local.yaml`. From here: `eidos` authors and validates, `configure` reshapes the framework, `index` rebuilds the index, `migrate` moves versions.
