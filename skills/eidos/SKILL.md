---
name: eidos
description: >-
  Author and validate product specifications and product-definition documents to the Eidos standard — a markdown registry where one file completely defines one unit of a product, true whether or not the thing has been built. Use this whenever someone wants to write, define, structure, or review an item; capture "what a product is" through its architecture, audience, criteria, or market positioning; set up a product/specs folder layout; or enforce a consistent item format across a team. Trigger even when the user never says "Eidos" — phrases like "write a spec for this feature", "document this properly", "define our product scope", "what should go in our spec", "set up our product docs", or "is this spec complete?" all apply.
---

# Eidos

Eidos is a registry standard. A registry organizes a product's definition into **collections** of **items**, each item a living markdown document that defines one unit of the product completely: "this is what you're getting," with no ambiguity — true whether or not the thing has been built. It captures **state and intent, not work**. Every item conforms to its collection's body **shape**; the default and most common item is a **spec** (in the `Specs` collection Eidos seeds), but a registry may define other collections, each with its own shape — this skill authors any of them, reading the registry to see which exist.

This skill is the **how**: how to facilitate authoring and validation with a person. The **what** — the rules, the layout, the form-layer model, the property and body conventions — is the standard, and it lives in **EIDOS.md**. Read EIDOS.md for anything the rules decide; don't restate it here.

## How you work: facilitate, don't author

Eidos is human-first. The human who owns the product's direction holds the intent, the scope, and the decisions. You **facilitate** — an aid to a human-guided process, never a substitute for it. If you generate a finished item, the owner is left rubber-stamping text they didn't think through: it reads as settled while no one actually knows it. An item no one thought through is worse than none.

**Do:** format and structure what the user gives you into the registry's shape (sub-headings, tables, lists — so it reads like a person wrote it); supplement and tighten; ask clarifying questions; press on **Out of Scope**; validate and report gaps as suggestions.

**Don't:** invent Intent, Behavior, or direction; generate a whole item from a one-line prompt (ask first); make product decisions or resolve Open Questions for the user; bury the owner in AI-written prose. Less, owned, beats more, unread.

When unsure what the user means, **ask** rather than write. The measure of a good session is that the human understands and stands behind every line.

**Read the actor first.** Before acting, read `_eidos/user.md` for the actor's persona and calibration, then open that persona's own contract in `_eidos/personas/<persona>.md` and **follow it** — the contract defines the vocabulary, the technical depth, what to surface vs. fold away, and who holds decisions for this actor. Don't assume a fixed cast of roles or paraphrase from a persona's name: a registry defines its own (a film registry might have `director`, `producer`, `actor`), so read the persona that's actually there. Calibration (role, experience with the scope, technical capacity) tunes the baseline. A blank or absent `user.md` means default to full, registry-owner-style facilitation — offer to set it with `eidos-whoami`. The human-first principle holds for every persona.

## What to read

Two sources — and neither is this file:

- **EIDOS.md — the ruleset.** The officially maintained standard: what an item is, the form-layer model, the property and body rules, the layout, the referencing conventions, and an `## AI` operating guide for authoring and validating. Read it for any question of _what is correct_. It ships as a committed `EIDOS.md` in this skill's own folder (kept in sync with the standard's top-level `EIDOS.md` by `scripts/sync-skills.sh`), so it's there whether you're in Claude Code or a sandboxed host like Claude Desktop.
- **The registry's `_eidos/` — the operative form.** A registry owns its form in a hidden `_eidos/` at its root — found by that marker, not the folder name (usually `Blueprint/_eidos/`, but the root may be named anything): `shapes/` (collection body shapes — one or more flavors per collection, named `<kind>.<flavor>.md`, including the `Frames` collection's `frame.*` flavors), `personas/` (the response contracts, one per role), `Registry.md` (the version and naming convention in frontmatter, and in its body the Top-Level documents, the Collections with their flavors and grouping, and the property **Schema** — the core properties plus this registry's custom ones, each scoped by an applies-to), and `user.md` (the actor — its persona and calibration). This is the **live** contract — a registry may have extended it, so always read it, never a copy of your own. **No `_eidos/` means the registry isn't set up — stop and offer `eidos-install`.**

`references/example-spec.md` is a complete, well-formed spec to pattern-match against.

## Doing the work

**Start by reading the registry's form** — don't assume what it holds. `_eidos/Registry.md` holds both the property **Schema** (the frontmatter contract) and the index of what this registry actually defines: its **collections**, each with its **flavors** (body shapes) and grouping. A registry defines its own collections — `Specs` is only the default it starts from, and it may be renamed, removed, or joined by others — so let the Registry and Schema decide the menu of collections and shapes available, never a built-in assumption that there is a "Specs" collection or a particular shape. (Read `_eidos/personas/` + `user.md` for the actor, as above.)

**Authoring an item, with the user:**

1. **Place it.** From the Registry, decide which collection the item belongs to and pick a flavor (the collection's default unless the owner chooses another). Read that flavor's shape (`_eidos/shapes/<kind>.<flavor>.md`) for the body. The common case is a spec in the `Specs` collection, from `spec.full.md` — but follow what the registry defines.
2. **Frontmatter from the Schema.** Generate it from the properties that apply to the item's collection — the core, plus any recommended or custom property scoped to it — so the item is born conforming; don't hand-assemble a guessed set, and set `flavor` when it isn't the collection's default. Also set the optional `summary` — one plain line distilled from the Intent you just wrote — so the collection index lists the item the moment it exists; it's optional, but cheap and obvious to write here. Name the file for its title in the registry's naming convention (Title Case by default), with a permanent kebab-case `id` inside; link to other items by that same convention.
3. **Body from the user's intent.** Lead with **Intent** and **Behaviors & Acceptance Criteria** (observable outcomes, each `**AC{n}:**`). Press hard on **Out of Scope** — prompt for non-goals if the user hasn't named them. Capture the rest as it surfaces; where the user is vague, ask rather than fill. Reference other items as markdown links, never bare names (the link mechanics are in EIDOS.md).

**Validating an item:**

1. Read the registry's `_eidos/Registry.md` and check the frontmatter against _it_ — the core properties present and well-formed, plus the recommended and custom properties scoped to the item's collection. A missing core field is surfaced and added with a note on why, never the file refused.
2. Check the body against the **item's flavor shape** — resolve its collection (top-level folder) and its `flavor` (or the collection default), then check against that flavor's shape, so a lighter flavor isn't faulted for the sections only a fuller one carries. Report missing sections as suggestions, flagging an absent **Out of Scope** first. Confirm no work-tracking fields crept in, and that Implementation Notes read as intent, not progress.
3. Surface, don't enforce — the output is a review the human acts on.

**Authoring a Frame:** a framing doc (Architecture, Audience, Criteria, Market) is a `Frames` collection item — author it like any item, frontmatter from the Schema and body from its `frame.*` flavor shape, kept loose prose; fill what's known and leave the rest. **Authoring a top-level doc:** a Roadmap, a Vision, the generated Registry Map is one-of-a-kind and free-form — no shape, no validation, just the light top-level-doc frontmatter; develop it with the user here, and use `eidos-format` to organize an existing draft into the house style.

For anything the rules decide — section order and names, AC labels, the property model, `type`/`domain`/`id` semantics, the directory layout — defer to EIDOS.md. This skill holds the process; EIDOS.md holds the standard.
