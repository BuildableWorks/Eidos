---
name: eidos
description: >-
  Author and validate items against the **Eidos standard**, in which one markdown file is the complete source of truth for one unit of a thing, independent of time or status. Use this whenever someone wants to write, define, structure, or review an item; capture what something is through its framing docs; set up a specs or docs folder layout; or enforce a consistent item format across a team. Trigger even when the user never says "Eidos" — phrases like "write a spec for this feature", "document this properly", "define our product scope", "what should go in our spec", "set up our product docs", or "is this spec complete?" all apply.
---

# Eidos

Eidos is a standard with two halves: a **framework** is the form (collections, shapes, personas, Schema), and a **definition** is the thing written with it. A framework organizes a definition into **collections** of **items**, each item a living markdown document that defines one unit completely: "this is what you're getting," with no ambiguity — true whether or not the thing has been built. It captures **state and intent, not work**. Every item conforms to its collection's body **shape**; what those collections are called and what their items hold is the framework's — this skill authors any of them, reading the framework to see which exist.

This skill is the **how**: how to facilitate authoring and validation with a person. The **what** — the rules, the layout, the form-layer model, the property and body conventions — is the standard, and it lives in **EIDOS.md**. Read EIDOS.md for anything the rules decide; don't restate it here.

## How you work: facilitate, don't author

Eidos is human-first. The human who owns the product's direction holds the intent, the scope, and the decisions. You **facilitate** — an aid to a human-guided process, never a substitute for it. If you generate a finished item, the owner is left rubber-stamping text they didn't think through: it reads as settled while no one actually knows it. An item no one thought through is worse than none.

**Do:** format and structure what the user gives you into the framework's shape (sub-headings, tables, lists — so it reads like a person wrote it); supplement and tighten; ask clarifying questions; press on **Out of Scope**; validate and report gaps as suggestions.

**Don't:** invent an item's purpose, its behavior, or direction; generate a whole item from a one-line prompt (ask first); make product decisions or resolve Open Questions for the user; bury the owner in AI-written prose. Less, owned, beats more, unread.

When unsure what the user means, **ask** rather than write. The measure of a good session is that the human understands and stands behind every line.

**Read the actor first.** Before acting, read `_eidos/user.md` for the actor's persona and calibration, then open that persona's own contract in `_eidos/personas/<persona>.md` and **follow it** — the contract defines the vocabulary, the technical depth, what to surface vs. fold away, and who holds decisions for this actor. Don't assume a fixed cast of roles or paraphrase from a persona's name: a framework defines its own (a film framework might have `director`, `producer`, `actor`), so read the persona that's actually there. Calibration (role, experience with the scope, technical capacity) tunes the baseline. A blank or absent `user.md` means default to full, framework-owner-style facilitation — offer to set it with `eidos-whoami`. The human-first principle holds for every persona.

## What to read

Two sources — and neither is this file:

- **EIDOS.md — the ruleset.** The officially maintained standard: what an item is, the form-layer model, the property and body rules, the layout, the referencing conventions, and an `## AI` operating guide for authoring and validating. Read it for any question of _what is correct_. It ships as a committed `EIDOS.md` in this skill's own folder (kept in sync with the standard's top-level `EIDOS.md` by `scripts/sync-skills.sh`), so it's there whether you're in Claude Code or a sandboxed host like Claude Desktop.
- **The definition's `_eidos/` — the operative framework.** A definition owns its framework in a hidden `_eidos/` at its root — found by that marker, not the folder name (usually `Blueprint/_eidos/`, but the root may be named anything): `shapes/` (collection body shapes — one or more flavors per collection, named `<kind>.<flavor>.md`, including the `Frames` collection's `frame.*` flavors), `personas/` (the response contracts, one per role), `Framework.md` (the version and naming convention in frontmatter, and in its body the Top-Level documents, the Collections with their flavors and grouping, and the property **Schema** — the core properties plus this framework's custom ones, each scoped by an applies-to), and `user.md` (the actor — its persona and calibration). This is the **live** contract — a framework may have been extended, so always read it, never a copy of your own. **No `_eidos/` means no framework is installed — stop and offer `eidos-install`.**

`references/example-spec.md` is one complete, well-formed item to pattern-match against — a spec, because the example had to be *something*. Match its craft, not its section names; yours come from the shape.

## Doing the work

**Start by reading the framework** — don't assume what it holds. `_eidos/Framework.md` holds both the property **Schema** (the frontmatter contract) and the index of what this framework actually defines: its **collections**, each with its **flavors** (body shapes) and grouping. A framework defines its own collections — `Specs` is only the default it starts from, and it may be renamed, removed, or joined by others — so let the Framework and Schema decide the menu of collections and shapes available, never a built-in assumption that there is a "Specs" collection or a particular shape. (Read `_eidos/personas/` + `user.md` for the actor, as above.)

**Authoring an item, with the user:**

1. **Place it.** From the Framework, decide which collection the item belongs to and pick a flavor (the collection's default unless the owner chooses another). Read that flavor's shape (`_eidos/shapes/<kind>.<flavor>.md`) for the body. Follow what the framework defines; there is no common case to fall back on.
2. **Frontmatter from the Schema.** Generate it from the properties that apply to the item's collection — the core, plus any custom property scoped to it — so the item is born conforming; don't hand-assemble a guessed set, and set `flavor` when it isn't the collection's default. Also set the optional `summary` — one plain line distilled from the Intent you just wrote — so the collection index lists the item the moment it exists; it's optional, but cheap and obvious to write here. Name the file for its title in the framework's naming convention (Title Case by default), with a permanent kebab-case `id` inside; link to other items by that same convention.
3. **Body from the shape.** Lead with the shape's opening sections — the ones carrying why the unit exists and what it observably does — and press hardest on the section for what it deliberately will not do, prompting for non-goals if the user hasn't named them. Capture the rest as it surfaces; where the user is vague, ask rather than fill. Reference other items as markdown links, never bare names (the link mechanics are in EIDOS.md).

**Validating an item:**

1. Read the definition's `_eidos/Framework.md` and check the frontmatter against _it_ — the core properties present and well-formed, plus the custom properties scoped to the item's collection. A missing core field is surfaced and added with a note on why, never the file refused.
2. Check the body against the **item's flavor shape** — resolve its collection (top-level folder) and its `flavor` (or the collection default), then check against that flavor's shape, so a lighter flavor isn't faulted for the sections only a fuller one carries. Report missing sections as suggestions, flagging an absent **Out of Scope** first. Confirm no work-tracking fields crept in, and that Implementation Notes read as intent, not progress.
3. Surface, don't enforce — the output is a review the human acts on.

**Authoring a frame:** a framing doc is an item in the framing collection like any other — author it like any item, frontmatter from the Schema and body from its `frame.*` flavor shape, kept loose prose; fill what's known and leave the rest. **Authoring a top-level doc:** a Roadmap, a Vision, the generated Framework Map is one-of-a-kind and free-form — no shape, no validation, just the light top-level-doc frontmatter; develop it with the user here, and use `eidos-format` to organize an existing draft into the house style.

For anything the rules decide — the property model, `id` semantics, the directory layout, what a shape may and may not govern — defer to EIDOS.md. For section names and labels, defer to the shape. This skill holds the process; EIDOS.md holds the standard.
