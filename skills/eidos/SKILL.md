---
name: eidos
description: >-
  Author and validate blueprints against the Eidos standard, in which one markdown file is the complete source of truth for one unit of a product (an app, a book, a study, anything work produces that has a shape). Use whenever someone wants to write, define, structure, or review a blueprint, capture what something is through its framing docs, or enforce a consistent blueprint format. Trigger even when the user never says "Eidos": "write a spec for this feature", "document this properly", "define our product scope", "is this spec complete?" all apply.
---

# Eidos

A **framework** is the structure (folders, templates, roles, Properties, Vocabulary) in a root's `.eidos/`; a **blueprint** is one unit of the **product** written with it. This skill is the how: facilitating authoring and validation with a person. The what is **EIDOS.md**, a copy of which ships in this folder. Read it for anything the rules decide; don't restate it.

## Facilitate, don't author

The owner holds intent, scope, and decisions. Format and structure what they give you, supplement, ask, and press on the template's non-goals. Never invent a blueprint's purpose, generate a whole blueprint from a one-line prompt (when the idea is rough, `iterate` settles it first), resolve open questions for the owner, or bury them in prose. When unsure, ask.

**Read `me.md` first**, then the role contract it names in `.eidos/roles/<role>.md`, and follow it. A framework defines its own roles; read the one that is there rather than assuming a cast. Blank means full, framework-owner-style facilitation; offer `whoami`.

**Speak the root's terms.** Write with the declared `vocabulary`. Where the owner's word is a near-miss an entry names, say which term the framework declares and ask; never swap silently. A word they keep using that no entry declares is a candidate for `configure`.

## Read the framework, never a copy

Find the root by its `.eidos/` marker. `Framework.yaml` carries the version, `naming`, `top_level`, `folders` (each with its type; a collection with its variants and grouping), `properties`, `vocabulary`, and the generated `index`. Read `templates/` for bodies. Read nothing in `plugins/`. No `.eidos/` means offer `install`. Where the CLI is present, `eidos framework --json` reads it for you.

**Check the version once per session.** Compare `eidos_version` with the `**Version:**` in this folder's EIDOS.md. Match: say nothing. Older: name both in one line, offer `migrate`, carry on. Newer: say the plugin is behind and be careful with anything you don't recognize; never offer to migrate down. Absent: offer `migrate`. A gap never blocks the work.

## Authoring

1. **Place it.** Pick the collection and variant (the default unless the owner chooses). Read that variant's template for the body.
2. **Frontmatter from the Properties table.** Generate the required properties that apply to the collection; add an optional one only when the owner gives it a value; offer the list where a property has `options`; set `variant` when not the default. Write `summary` now. Name the file for its title in `naming`, with a permanent `id` inside in whatever form the root uses.
3. **Body from the template.** Lead with its opening sections, press hardest on non-goals, capture the rest as it surfaces. Where the owner is vague, ask. Link other blueprints and files with relative markdown links, never bare names.

A framing doc is a blueprint like any other, kept loose. A top-level doc has no template, just light frontmatter and an entry under `top_level`; `format` organizes an existing draft.

## Validating

1. **Frontmatter** against every block of the Properties table: required properties present, optional ones checked only when present, values on `options` properties on the list (surfaced with the list beside them when not), `variant` one of the collection's, a grouping value one of its groups. Keys past the standard's six on a property entry are a tool's; ignore them.
2. **Body** against the blueprint's own variant template, so a lighter variant is not faulted for a fuller one's sections. Report missing sections as suggestions, non-goals first. Flag Vocabulary near-misses with the declared term beside them. Confirm no work-tracking fields, and that approach reads as intent, not progress. Check every link and image path resolves.
3. **Regions** (`<!-- <tool>:<region> -->` to `<!-- /<tool>:<region> -->`) belong to their tool: leave the contents alone, report an opener with no closer.
4. **The root** against the framework document: every folder declared under `folders`, every file under `top_level`, and every entry present. Surface anything without its counterpart and offer `configure`. Inside a collection, a non-markdown file is not a blueprint; say nothing. Inside an `assets` or `other` folder, read nothing.
5. **Surface, don't enforce.** The output is a review the human acts on. Never refuse a file.
