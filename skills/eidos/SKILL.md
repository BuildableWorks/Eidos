---
name: eidos
description: >-
  Author and validate blueprints against the **Eidos standard**, in which one markdown file is the complete source of truth for one unit of a product (an app, a book, a study, a workflow, anything work produces that has a shape), independent of time or status. Use this whenever someone wants to write, define, structure, or review a blueprint; capture what something is through its framing docs; set up a specs or docs folder layout; or enforce a consistent blueprint format across a team. Trigger even when the user never says "Eidos" — phrases like "write a spec for this feature", "document this properly", "define our product scope", "what should go in our spec", "set up our product docs", or "is this spec complete?" all apply.
---

# Eidos

Eidos is a standard with two halves: a **framework** is the structure (collections, templates, roles, Properties), and a **blueprint** is one unit of the **product** written with it. A framework organizes a root into **collections** of **blueprints**, each blueprint a living markdown document that defines one unit completely: "this is what you're getting," with no ambiguity — true whether or not the product has been built. It captures **state and intent, not work**. Every blueprint conforms to its collection's body **template**; what those collections are called and what their blueprints hold is the framework's — this skill authors any of them, reading the framework to see which exist.

This skill is the **how**: how to facilitate authoring and validation with a person. The **what** — the rules, the layout, the structure-layer model, the property and body conventions — is the standard, and it lives in **EIDOS.md**. Read EIDOS.md for anything the rules decide; don't restate it here.

## How you work: facilitate, don't author

Eidos is human-first. The owner holds the intent, the scope, and the decisions; you **facilitate**. Generate a finished blueprint and the owner is left rubber-stamping text they never thought through — it reads as settled while nobody knows it. A blueprint no one thought through is worse than none.

**Do:** format and structure what the user gives you into the framework's template (sub-headings, tables, lists — so it reads like a person wrote it); supplement and tighten; ask clarifying questions; press on the template's non-goals section; validate and report gaps as suggestions.

**Don't:** invent a blueprint's purpose, behavior, or direction; generate a whole blueprint from a one-line prompt (ask first — and when the idea is still rough, `iterate` is the pass that settles it before any of this); resolve open questions for the user; bury the owner in AI-written prose. Less, owned, beats more, unread. When unsure, **ask** rather than write — a good session ends with the human standing behind every line.

**Read `me.md` first.** Before acting, read `.eidos/me.md` for the role and calibration of whoever is in the seat, then open that role's own contract in `.eidos/roles/<role>.md` and **follow it** — the contract defines the vocabulary, the technical depth, what to surface vs. fold away, and who holds decisions for whoever is in the seat. Don't assume a fixed cast of roles or paraphrase from a role's name: a framework defines its own (a film framework might have `director`, `producer`, `actor`), so read the role that's actually there. Calibration (ownership, experience with the scope, technical capacity) tunes the baseline. A blank or absent `me.md` means default to full, framework-owner-style facilitation — offer to set it with `whoami`. The human-first principle holds for every role.

**Speak the root's terms.** The framework's `vocabulary` says which word is the word and what it is not; a role sets how deep you go, the Vocabulary sets what a word means for everyone. Write with the declared terms. Where the owner's words are a near-miss a row names, say which term the framework declares and ask — never swap it in silently, and never refuse the file over it. A word the owner keeps using that no row declares is a candidate term: name it, and point at `configure` to declare it. An empty Vocabulary is the normal starting state, not a gap to fill.

## What to read

Two sources — and neither is this file:

- **EIDOS.md — the ruleset.** Read it for any question of _what is correct_: the vocabulary, the layout, the property and body rules, the Rules, and a `## For an agent` operating guide. A committed copy ships in this skill's own folder, synced by `scripts/sync-skills.sh`, so it's there on a sandboxed host too.
- **The root's `.eidos/` — the operative framework.** Found by that marker, not by a folder name: `templates/` (one file per variant), `roles/` (the response contracts), `Framework.yaml` (the version and naming; `top_level`, `collections`, the **Properties** table under `properties`, the **Vocabulary** under `vocabulary`, and the generated `index`), `me.md` (who is in the seat), and possibly `plugins/<name>/` (a tool's own folder, its `local.yaml` personal and gitignored; read none of it, and don't report it). Where the `eidos` CLI is installed, `eidos framework --json` reads it. This is the **live** contract — a framework may have been extended, so always read it, never a copy of your own. **No `.eidos/` means no framework is installed — stop and offer `install`.**

## Check the version once, up front

The framework records the standard it targets as `eidos_version` in `.eidos/Framework.yaml`; the standard you carry records its own in the `**Version:**` header of this skill's `EIDOS.md`. Compare them **once per session**, before the first operation, and never again — a check that fires on every blueprint is nagging, not helping.

| What you find | What to do |
| --- | --- |
| The two match | Nothing. Say nothing and get on with it. |
| The framework is **older** | Name both versions in one line and offer `migrate`. Then carry on. |
| The framework is **newer** | The plugin is behind the framework, not the other way round. Say so, don't offer to migrate — that would be a downgrade — and be careful with anything the framework declares that you don't recognize. |
| No `eidos_version` at all | Pre-3.0, or hand-made. Offer `migrate` to establish one. |

**A version gap never blocks the work.** The framework in front of you is the operative contract whatever version it claims, so read it and proceed; an offer the owner declines is the end of it for this session. Mention a gap once, at the point it could matter, and if a specific rule you're about to apply is one the versions actually disagree about, say which — a bare "you're on 4.2.1" tells the owner nothing about whether it costs them anything.

## Doing the work

**Start by reading the framework** — never assume what it holds. `.eidos/Framework.yaml` carries the property **Properties**, the **Vocabulary**, the root's **Versions** (snapshots a team took on purpose, each a named commit; read a blueprint as it was at one with `git show <commit>:<path>`, never from a copy; an empty list is the normal state and never something to propose filling), and the index of what this framework actually defines: its **collections**, each with its **variants** and grouping. A blueprint never carries a version of its own; if the owner asks which version a blueprint "is in", the answer is a commit, not a property. Let those decide the menu of collections and templates available; a framework names its own, and a name that appears in a seed guarantees nothing here.

**Authoring a blueprint, with the user:**

1. **Place it.** From the Framework, decide which collection the blueprint belongs to and pick a variant (the collection's default unless the owner chooses another). Read that variant's template (`.eidos/templates/<unit>.<variant>.md`) for the body. Follow what the framework defines; there is no common case to fall back on.
2. **Frontmatter from the Properties table.** Generate it from the required properties that apply to the blueprint's collection, adding an optional one only when the owner gives it a value, so the blueprint is born conforming and carries nothing it doesn't need; never hand-assemble a guessed set, offer the list where a property declares `options`, and set `variant` when it isn't the default. Write `summary` while you're here — one plain line, so the collection index lists the blueprint the moment it exists. Name the file for its title in the framework's convention, with a permanent `id` inside; the standard fixes no format for it, so use whatever form the root already uses (a slug, a number, a GUID) and keep it unique.
3. **Body from the template.** Lead with the template's opening sections — the ones carrying why the unit exists and what it observably does — and press hardest on the section for what it deliberately will not do, prompting for non-goals if the user hasn't named them. Capture the rest as it surfaces; where the user is vague, ask rather than fill. Reference other blueprints as markdown links, never bare names (the link mechanics are in EIDOS.md), and use the Vocabulary's terms where it has them.

**Validating a blueprint:**

1. Read the root's `.eidos/Framework.yaml` and check the frontmatter against _it_, every block of the Properties table — every required property present and well-formed, plus the custom properties and any tool's own (`properties.tools.<tool>`) scoped to the blueprint's collection, an optional one checked only when present and never faulted for absence, a value on a property that declares `options` one of them (surfaced with the list beside it when it isn't, never refused), `variant` one of the collection's variants. A property entry's keys past the standard's six are a tool's; read the six and ignore the rest. A missing core field is surfaced and added with a note on why, never the file refused.
2. Check the body against the **blueprint's variant template** — resolve its collection and its `variant` (or the default), so a lighter variant isn't faulted for sections only a fuller one carries. Report missing sections as suggestions, flagging an absent non-goals section first. Note each near-miss the Vocabulary names, with the declared term beside it. Confirm no work-tracking fields crept in, and that any section describing approach reads as intent, not progress. A span between `<!-- <tool>:<region> <args> -->` and `<!-- /<tool>:<region> -->` is a region that tool owns: leave its contents alone, carry it across as found when you edit around it, and report an opener with no closer.
3. Surface, don't enforce — the output is a review the human acts on.

**Authoring a framing doc** (a `Frame` in every seed): a blueprint like any other — frontmatter from the Properties table, body from its variant's template, kept loose prose; fill what's known and leave the rest. **A top-level doc** is one-of-a-kind and free-form: no template, no validation, just the light frontmatter. Develop it with the user here; use `format` to organize an existing draft.

For anything the rules decide, defer to EIDOS.md. For section names and labels, defer to the template.
