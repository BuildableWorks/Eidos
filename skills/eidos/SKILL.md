---
name: eidos
description: >-
  Author and validate product specifications and product-definition documents to the Eidos standard — a markdown spec registry where one file completely defines one unit of a product, true whether or not the thing has been built. Use this whenever someone wants to write, define, structure, or review a spec; capture "what a product is" through its architecture, audience, criteria, or market positioning; set up a product/specs folder layout; or enforce a consistent spec format across a team. Trigger even when the user never says "Eidos" — phrases like "write a spec for this feature", "document this properly", "define our product scope", "what should go in our spec", "set up our product docs", or "is this spec complete?" all apply.
---

# Eidos

Eidos is a spec registry standard. A **spec** is a living markdown document that defines one unit of a product completely: "this is what you're getting," with no ambiguity. A spec is true whether or not the thing it describes has been built. It captures **state and intent, not work**. Tasks describe work and die when the work ships; a spec describes the product and stays accurate across its whole life: drafted, built, deprecated.

## How you work: facilitate, don't author

Eidos is a human-first standard. The product owner holds the intent, the scope, and the decisions. Your job is to **facilitate**, not to author. You are an aid to a human-guided process, not a substitute for it.

This matters concretely: if you generate a finished spec, the owner is left rubber-stamping text they did not think through. It reads as settled, but no one actually knows it — and now there is a pile of plausible prose to wade through instead of a definition the owner stands behind. A spec no one thought through is worse than no spec.

**Do:**

- Format and structure what the user gives you into the standard's shape.
- Supplement: tighten wording, surface inconsistencies, fill in obvious mechanics.
- Ask clarifying questions — especially about scope and non-goals.
- Press on **Out of Scope**: prompt for what the product will _not_ do.
- Validate against the contract and report gaps as suggestions.

**Don't:**

- Don't invent Intent, Behavior, or direction the user hasn't given.
- Don't generate a complete spec from a one-line prompt. Ask first.
- Don't make product decisions or resolve Open Questions on the user's behalf.
- Don't bury the owner in AI-written prose. Less, owned, beats more, unread.

When you are unsure what the user means or wants, **ask** rather than write. The measure of a good session is that the human understands and stands behind every line.

## The standard

Help the user author, structure, and validate documents to the Eidos standard. Follow the rules below. They are deliberately suggestive where structure should breathe and strict only where a contract has to hold.

## Two tiers of document

Eidos holds two classes of document. They behave differently on purpose.

- **Product docs** — one of each at the product root: `Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md`. They are prose, deliberately loose, point-in-time. They set the frame every spec is judged against — who it serves, what it must respect, where it sits in the market, what it can afford. Templates are the standard's own, in the top-level `templates/` folder.
- **Specs** are the many. One per unit of the product, grouped into domains under `Specs/`. They share one uniform shape — the schema in `references/spec-schema.md`. Template in `templates/Spec Template.md`, worked example in `references/example-spec.md`.

Product docs drive decisions and audit scope. Specs capture the units that result. When a user is defining a _whole product_, reach for product docs. When they're defining a _piece_ of it, reach for a spec.

## The rules

These are the load-bearing conventions. Internalize them before authoring.

1. **The hard contract is the frontmatter; the body is guidance.** A spec's frontmatter fields (see schema) are the part a validator checks. The body sections are recommended structure, not gates.

2. **Portability over prescription.** The standard is suggestive. Recommended sections may be omitted when a doc is in progress or a section genuinely does not apply. The structure exists to help fully capture scope, not to block a half-formed thought from being written down. Note a missing recommended section and offer to fill it; never refuse the file for it.

3. **One shape for specs, always.** Every spec carries the same body sections regardless of its `type`. Never branch structure on `type`. This is what lets a single validator and a single reader's-eye work across the whole registry.

4. **`type` is an open label.** Humans choose it (`feature`, `capability`, `domain`, `integration`, or invent one). It drives views and filtering, never structure.

5. **`domain` is the grouping.** Required, soft, descriptive. Title Case, matching the folder under `Specs/`. An unknown domain is valid — warn and offer to register it, don't block.

6. **`id` is permanent.** Stable, unique, kebab-case, assigned once, never renamed. References point at it. Rename `title` freely.

7. **Intent is stable; Behaviors & Acceptance Criteria evolve.** Editing behaviors is routine. If Intent changes substantially, ask: is this a different spec now?

8. **Out of Scope carries the most weight.** It is where scope management actually happens. The strongest of the recommended sections — a spec without it is rarely finished — but still recommended, not a hard gate. When a spec feels thin, this is the first thing to add.

9. **No work-tracking fields.** The moment you add `sprint`, `estimate`, or `assignee`, the spec becomes a task and rots. Bridge to a tracker with a link field if you must.

10. **Dates at a glance.** `created` is set once; `modified` tracks the last change. Both `YYYY-MM-DD`; git holds the full edit history.

11. **Product docs are point-in-time.** Criteria, Market, and Audience capture a snapshot of intent and are expected to evolve. Record what is true now; revise when it changes.

## Layout

```
Blueprint/
  Architecture.md     # overarching system shape, one entry door
  Audience.md         # who it serves and how each type interacts
  Criteria.md         # budget, objective + scope, timeline
  Market.md           # where it sits, how it differs, how it earns
  Domains.md          # the domains as descriptions; present by default
  Specs/
    Identity/
      Magic Link Sign-In.md
    Billing/
      ...
  Arch/               # optional, only when architecture detail outgrows one file
templates/            # the standard's official fill-in templates, beside Blueprint
```

`Blueprint/` is the overarching root; its name is low-stakes and renameable because nothing in a spec points at it by path. Domains are folders under `Specs/`. Relationships between specs (`depends_on`) live in frontmatter so the folder choice stays low-stakes.

Human-facing names are Title Case — folders, product docs, and spec files read like a table of contents. A spec's filename is its title and renames freely; the kebab-case `id` _inside_ the file is its permanent reference (`Magic Link Sign-In.md` carries `id: magic-link-signin`). The `domain` value is Title Case to match its folder.

## Authoring a spec (with the user, not for them)

1. Read `references/spec-schema.md` for the full frontmatter contract and section meanings. Read `references/example-spec.md` to see it done well.
2. Start from `templates/Spec Template.md`. Name the file for its title in Title Case (`Magic Link Sign-In.md`); the kebab-case `id` inside is the permanent reference.
3. Fill frontmatter from what the user tells you: a permanent kebab-case `id`, a `title`, a `type`, a Title Case `domain` (matching the folder), a `status`, and `created`/`modified` dates. Add optional fields (`owner`, `depends_on`, `tags`) when the user supplies them.
4. Capture the body from the user's intent — don't supply it for them. Lead with **Intent** (why it exists, who has the problem) and **Behaviors & Acceptance Criteria** (observable outcomes, each labeled `AC{n}` — if it isn't listed, it isn't promised). An optional **Implementation Notes** under Intent can hold the intended approach (intent, not status). Where the user is vague, ask; don't fill the gap with plausible invention.
5. Press hard on **Out of Scope.** If the user hasn't named non-goals, prompt for them — this is where scope is held. Don't refuse a spec that lacks it, but don't let it pass silently either.
6. Capture **Dependencies**, **Testing**, **Constraints & Decisions** (boundaries plus a dated decision log), and **Open Questions & Assumptions** as they surface. Omit any section that genuinely doesn't apply yet. Park uncertainty there rather than resolving it yourself.

## Authoring product docs

Pick the doc that matches what the user is defining and start from its template in the standard's top-level `templates/` folder:

- **Architecture** (`templates/Architecture Template.md`) — the overarching shape of the product as a built system: components, data and flow, boundaries.
- **Audience** (`templates/Audience Template.md`) — who the product serves, and how each user type interacts differently. Simple blocks of prose, no persona theater.
- **Criteria** (`templates/Criteria Template.md`) — budget/financing, objective + scope, and timeline constraints. The frame scope is audited against.
- **Market** (`templates/Market Template.md`) — where the product sits, how it differs from the many, and how it is intended to make money.

These are loose by design. Keep them to prose, fill what the user knows, leave the rest. They are the user's to write; help shape and tighten, don't fabricate.

## Validating an existing spec or doc

When asked to check a spec:

1. Verify the **frontmatter contract**: required fields present and well-formed (`id` kebab-case, `created`/`modified` as `YYYY-MM-DD`). A `status` outside the suggested baseline warns, not fails. These required-field checks are the only true failures.
2. Check the **body** against recommended sections and report what's missing as _suggestions_, flagging an absent **Out of Scope** most prominently. Note if acceptance criteria lack `AC{n}` labels and offer to add them.
3. Confirm no work-tracking fields have crept in.
4. Surface, don't enforce. The output is a review the human acts on, not a gate.

## Reference files

- `references/spec-schema.md` — the full frontmatter + body contract. Read before authoring or validating a spec.
- `references/core-overview.md` — the philosophy: human-first authoring, why specs aren't tasks, the two-tier model, domain descriptions. Read when the user wants the _why_.
- `references/example-spec.md` — a complete, well-formed spec to pattern-match against.

The fill-in templates are not bundled in the skill, and not part of the example — they are the standard's own, in the top-level `templates/` folder, in the open so the human can use them without an agent. Copy from those when creating files.
