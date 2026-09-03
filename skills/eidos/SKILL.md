---
name: eidos
description: >-
  Author and validate blueprints against the **Eidos standard**, in which one markdown file is the complete source of truth for one unit of a thing, independent of time or status. Use this whenever someone wants to write, define, structure, or review a blueprint; capture what something is through its framing docs; set up a specs or docs folder layout; or enforce a consistent blueprint format across a team. Trigger even when the user never says "Eidos" — phrases like "write a spec for this feature", "document this properly", "define our product scope", "what should go in our spec", "set up our product docs", or "is this spec complete?" all apply.
---

# Eidos

Eidos is a standard with two halves: a **framework** is the structure (collections, shapes, roles, Schema), and a **blueprint** is the thing written with it. A framework organizes a root into **collections** of **blueprints**, each blueprint a living markdown document that defines one unit completely: "this is what you're getting," with no ambiguity — true whether or not the thing has been built. It captures **state and intent, not work**. Every blueprint conforms to its collection's body **shape**; what those collections are called and what their blueprints hold is the framework's — this skill authors any of them, reading the framework to see which exist.

This skill is the **how**: how to facilitate authoring and validation with a person. The **what** — the rules, the layout, the structure-layer model, the property and body conventions — is the standard, and it lives in **EIDOS.md**. Read EIDOS.md for anything the rules decide; don't restate it here.

## How you work: facilitate, don't author

Eidos is human-first. The owner holds the intent, the scope, and the decisions; you **facilitate**. Generate a finished blueprint and the owner is left rubber-stamping text they never thought through — it reads as settled while nobody knows it. A blueprint no one thought through is worse than none.

**Do:** format and structure what the user gives you into the framework's shape (sub-headings, tables, lists — so it reads like a person wrote it); supplement and tighten; ask clarifying questions; press on the shape's non-goals section; validate and report gaps as suggestions.

**Don't:** invent a blueprint's purpose, behavior, or direction; generate a whole blueprint from a one-line prompt (ask first — and when the idea is still rough, `iterate` is the pass that settles it before any of this); resolve open questions for the user; bury the owner in AI-written prose. Less, owned, beats more, unread. When unsure, **ask** rather than write — a good session ends with the human standing behind every line.

**Read the actor first.** Before acting, read `_eidos/me.md` for the actor's role and calibration, then open that role's own contract in `_eidos/roles/<role>.md` and **follow it** — the contract defines the vocabulary, the technical depth, what to surface vs. fold away, and who holds decisions for this actor. Don't assume a fixed cast of roles or paraphrase from a role's name: a framework defines its own (a film framework might have `director`, `producer`, `actor`), so read the role that's actually there. Calibration (ownership, experience with the scope, technical capacity) tunes the baseline. A blank or absent `me.md` means default to full, framework-owner-style facilitation — offer to set it with `whoami`. The human-first principle holds for every role.

## What to read

Two sources — and neither is this file:

- **EIDOS.md — the ruleset.** Read it for any question of _what is correct_: the vocabulary, the layout, the property and body rules, the Rules, and a `## For an agent` operating guide. A committed copy ships in this skill's own folder, synced by `scripts/sync-skills.sh`, so it's there on a sandboxed host too.
- **The root's `_eidos/` — the operative framework.** Found by that marker, not by a folder name: `shapes/` (one file per flavor), `roles/` (the response contracts), `Framework.md` (version and naming in frontmatter; Top-Level, Collections, and the property **Schema** in its body), `me.md` (the actor). This is the **live** contract — a framework may have been extended, so always read it, never a copy of your own. **No `_eidos/` means no framework is installed — stop and offer `install`.**

## Check the version once, up front

The framework records the standard it targets as `eidos_version` in `_eidos/Framework.md`; the standard you carry records its own in the `**Version:**` header of this skill's `EIDOS.md`. Compare them **once per session**, before the first operation, and never again — a check that fires on every blueprint is nagging, not helping.

| What you find | What to do |
| --- | --- |
| The two match | Nothing. Say nothing and get on with it. |
| The framework is **older** | Name both versions in one line and offer `migrate`. Then carry on. |
| The framework is **newer** | The plugin is behind the framework, not the other way round. Say so, don't offer to migrate — that would be a downgrade — and be careful with anything the framework declares that you don't recognize. |
| No `eidos_version` at all | Pre-3.0, or hand-made. Offer `migrate` to establish one. |

**A version gap never blocks the work.** The framework in front of you is the operative contract whatever version it claims, so read it and proceed; an offer the owner declines is the end of it for this session. Mention a gap once, at the point it could matter, and if a specific rule you're about to apply is one the versions actually disagree about, say which — a bare "you're on 4.2.1" tells the owner nothing about whether it costs them anything.

## Doing the work

**Start by reading the framework** — never assume what it holds. `_eidos/Framework.md` carries the property **Schema** and the index of what this framework actually defines: its **collections**, each with its **flavors** and grouping. Let those decide the menu of collections and shapes available; a framework names its own, and a name that appears in a seed guarantees nothing here.

**Authoring a blueprint, with the user:**

1. **Place it.** From the Framework, decide which collection the blueprint belongs to and pick a flavor (the collection's default unless the owner chooses another). Read that flavor's shape (`_eidos/shapes/<kind>.<flavor>.md`) for the body. Follow what the framework defines; there is no common case to fall back on.
2. **Frontmatter from the Schema.** Generate it from the properties that apply to the blueprint's collection, so the blueprint is born conforming; never hand-assemble a guessed set, and set `flavor` when it isn't the default. Write `summary` while you're here — one plain line, so the collection index lists the blueprint the moment it exists. Name the file for its title in the framework's convention, with a permanent kebab-case `id` inside.
3. **Body from the shape.** Lead with the shape's opening sections — the ones carrying why the unit exists and what it observably does — and press hardest on the section for what it deliberately will not do, prompting for non-goals if the user hasn't named them. Capture the rest as it surfaces; where the user is vague, ask rather than fill. Reference other blueprints as markdown links, never bare names (the link mechanics are in EIDOS.md).

**Validating a blueprint:**

1. Read the root's `_eidos/Framework.md` and check the frontmatter against _it_ — the core properties present and well-formed, plus the custom properties scoped to the blueprint's collection. A missing core field is surfaced and added with a note on why, never the file refused.
2. Check the body against the **blueprint's flavor shape** — resolve its collection and its `flavor` (or the default), so a lighter flavor isn't faulted for sections only a fuller one carries. Report missing sections as suggestions, flagging an absent non-goals section first. Confirm no work-tracking fields crept in, and that any section describing approach reads as intent, not progress.
3. Surface, don't enforce — the output is a review the human acts on.

**Authoring a frame:** a blueprint in the framing collection like any other — frontmatter from the Schema, body from its flavor's shape, kept loose prose; fill what's known and leave the rest. **A top-level doc** is one-of-a-kind and free-form: no shape, no validation, just the light frontmatter. Develop it with the user here; use `format` to organize an existing draft.

For anything the rules decide, defer to EIDOS.md. For section names and labels, defer to the shape.
