---
name: format
description: >-
  Reshape an existing rough draft (a brain-dump, notes, half-formed prose) into Eidos form, preserving the author's words and adding nothing. Works on a collection blueprint or a free-form top-level doc. Use when someone says "format this", "organize these notes into the template", "clean up this spec", "make this match the template". Formatting within one file, not authoring: `eidos` develops content, `iterate` settles an unsettled idea, `install` scaffolds, `migrate` upgrades.
---

# Eidos Format

Take a file someone has written and give it the framework's structure. You organize and format; you do not author.

## Preserve, don't pad

- **Keep their wording.** Move sentences into the section they belong in, tidy grammar and markdown, and stop. Never inflate three words into a paragraph.
- **Add nothing of substance.** No invented behaviors, decisions, scope, or acceptance criteria.
- **Surface gaps; don't fill them.** Omit a section with nothing under it. For one that clearly should have content (usually non-goals), keep the heading with a short `<!-- TODO -->` and say so.
- **Mark what you inferred**: a guessed `title`, a heading you chose for a loose sentence.

## Read like a human would read it

Tables for structured data, numbered lists for sequences, bullets for enumerations, `####` sub-headings where a section has internal structure. Keep checkable statements short and point them at detail. Turn references into relative markdown links in the framework's `naming`; converting a name into a link is formatting, in scope.

## Two kinds of file

- **A collection blueprint** is reshaped toward its variant's template in `.eidos/templates/` (the collection's default unless the draft's `variant` says otherwise), with frontmatter from `Framework.yaml`.
- **A top-level doc** has no template. Organize by its own logic, keep the light frontmatter (`title`, `tags`, `date_created`, `date_modified`), and if it has no `top_level` entry yet, hand that back as a gap for `configure`.

No `.eidos/` means offer `install` first; you template toward the framework's real structure, never a guess.

## Procedure

1. Read the whole file first.
2. Open the variant's template and `Framework.yaml` (Properties and Vocabulary). Read section names off the template, never from memory.
3. Route content by meaning: what it won't do into non-goals, what is taken as given into assumptions, what is unanswered into open questions, observable outcomes among the checkable statements. Where the template has no home for a passage, say so.
4. Format for readability, labeled the way the template asks.
5. Fill only derivable frontmatter: `title` from the heading, dates to today. Leave `id`, a lifecycle, a grouping, and anything you can't derive honestly.
6. List the gaps and your changes: empty sections (non-goals first), inferred structure, and each Vocabulary near-miss with the declared term beside it. Swapping a word is changing the author's words, so it goes on the list, not in the file.
7. Hand back the file plus the list. If one dump covers several units, say so and ask how to split it rather than splitting silently.
