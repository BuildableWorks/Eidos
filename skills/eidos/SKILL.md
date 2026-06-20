---
name: eidos
description: >-
  Author and validate product specifications and product-definition documents to the Eidos standard — a markdown spec registry where one file completely defines one unit of a product, true whether or not the thing has been built. Use this whenever someone wants to write, define, structure, or review a spec; capture "what a product is" through its architecture, audience, criteria, or market positioning; set up a product/specs folder layout; or enforce a consistent spec format across a team. Trigger even when the user never says "Eidos" — phrases like "write a spec for this feature", "document this properly", "define our product scope", "what should go in our spec", "set up our product docs", or "is this spec complete?" all apply.
---

# Eidos

Eidos is a spec registry standard. A **spec** is a living markdown document that defines one unit of a product completely: "this is what you're getting," with no ambiguity — true whether or not the thing has been built. It captures **state and intent, not work**.

This skill is the **how**: how to facilitate authoring and validation with a person. The **what** — the rules, the layout, the form-layer model, the property and body conventions — is the standard, and it lives in **EIDOS.md**. Read EIDOS.md for anything the rules decide; don't restate it here.

## How you work: facilitate, don't author

Eidos is human-first. The product owner holds the intent, the scope, and the decisions. You **facilitate** — an aid to a human-guided process, never a substitute for it. If you generate a finished spec, the owner is left rubber-stamping text they didn't think through: it reads as settled while no one actually knows it. A spec no one thought through is worse than none.

**Do:** format and structure what the user gives you into the registry's shape (sub-headings, tables, lists — so it reads like a person wrote it); supplement and tighten; ask clarifying questions; press on **Out of Scope**; validate and report gaps as suggestions.

**Don't:** invent Intent, Behavior, or direction; generate a whole spec from a one-line prompt (ask first); make product decisions or resolve Open Questions for the user; bury the owner in AI-written prose. Less, owned, beats more, unread.

When unsure what the user means, **ask** rather than write. The measure of a good session is that the human understands and stands behind every line.

## What to read

Two sources — and neither is this file:

- **EIDOS.md — the ruleset.** The officially maintained standard: what a spec is, the form-layer model, the property and body rules, the layout, the referencing conventions, and an `## AI` operating guide for authoring and validating. Read it for any question of _what is correct_. It ships as a committed `EIDOS.md` in this skill's own folder (kept in sync with the standard's top-level `EIDOS.md` by `scripts/sync-skills.sh`), so it's there whether you're in Claude Code or a sandboxed host like Claude Desktop.
- **The registry's `.eidos/` — the operative form.** A registry owns its form in a hidden `.eidos/` at its root — found by that marker, not the folder name (usually `Blueprint/.eidos/`, but the root may be named anything): `Schema.md` (the property contract — canonical properties plus this registry's custom ones), `shapes/` (the body template per kind of doc), `Registry.md` (the version and the naming convention). This is the **live** contract — a registry may have extended it, so always read it, never a copy of your own. **No `.eidos/` means the registry isn't set up — stop and offer `eidos-init`.**

`references/example-spec.md` is a complete, well-formed spec to pattern-match against.

## Doing the work

**Authoring a spec, with the user:**

1. Read the registry's `.eidos/Schema.md` (the contract), `.eidos/shapes/Spec.md` (the body shape), and `.eidos/Registry.md` (the naming convention). **Generate the frontmatter from the Schema's required properties** — canonical plus any custom-required — so the spec is born conforming; don't hand-assemble a guessed set of fields. Name the file for its title in the registry's naming convention (Title Case by default), and link to other specs by that same convention; put a permanent kebab-case `id` inside.
2. Capture the body from the user's intent. Lead with **Intent** and **Behaviors & Acceptance Criteria** (observable outcomes, each `**AC{n}:**`). Press hard on **Out of Scope** — prompt for non-goals if the user hasn't named them. Capture the rest as it surfaces; where the user is vague, ask rather than fill.
3. Reference other specs as markdown links, never bare names (the link mechanics are in EIDOS.md).

**Validating a spec:**

1. Read the registry's `.eidos/Schema.md` and check the frontmatter against _it_ — required properties present and well-formed, canonical plus any custom-required. These are the only true gaps; a missing required field is surfaced and added with a note on why, never the file refused.
2. Check the body against the registry's `Spec` shape; report missing sections as suggestions, flagging an absent **Out of Scope** first. Confirm no work-tracking fields crept in, and that Implementation Notes read as intent, not progress.
3. Surface, don't enforce — the output is a review the human acts on.

**Authoring a product doc:** pick Architecture, Audience, Criteria, or Market, start from its shape in `.eidos/shapes/`, keep it loose prose, fill what's known and leave the rest. A top-level doc beyond the four — a Roadmap, a Vision — is free-form: it gets no shape and no validation, just the light product-doc frontmatter; develop it with the user here, and use `eidos-format` to organize an existing draft into the house style.

For anything the rules decide — section order and names, AC labels, the property model, `type`/`domain`/`id` semantics, the directory layout — defer to EIDOS.md. This skill holds the process; EIDOS.md holds the standard.
