---
name: eidos-whoami
description: >-
  Set or update who you are in an Eidos definition — your persona and calibration — written to your personal `_eidos/user.md`. Use when someone wants to "set my user", "tell Eidos who I am", "I'm the designer / a developer / the framework owner", "change my role", "set up my persona", "the AI is talking over my head" or "it's explaining things I already know", or when `_eidos/user.md` is blank or absent. It offers whatever personas the framework installed (`_eidos/personas/`), then calibrates the chosen one on three axes — your role for this product, your experience with the scope, and your technical capacity — and writes `_eidos/user.md`. That file is personal and gitignored; the agent reads it before acting to decide how to respond (vocabulary, depth, what to surface, who decides). Companion to `eidos-install`, which scaffolds the definition; this sets the actor.
---

# Eidos Whoami

Set the **actor** — who is in the seat — so the agent knows how to respond to _you_. This writes your personal `_eidos/user.md`: a **persona** (the baseline response contract) plus a **calibration** (how that baseline adjusts for you). It is the companion to `eidos-install`, which scaffolds the product; this is about the person, not the product.

`_eidos/user.md` is **personal and gitignored** — each person who works on the definition runs this for themselves, and no one's persona lands in anyone else's checkout.

## Why this matters

Eidos relies on the actor as a core input to how it communicates. A persona is a response contract: it sets vocabulary and technical depth, what to surface vs. fold away, and who holds which decisions. One role is told to keep mechanism out of the reply and talk in the terms of the thing itself; another gets full technical depth; the Framework Owner is brought the decisions to make. Without an actor, the agent defaults to full, framework-owner-style facilitation — workable, but generic. Setting it makes every later session fit you.

## How you work

A short, guided interview, then a small file write. You do **not** invent the persona content — the personas are defined in `_eidos/personas/` (the framework's, seeded from the standard's defaults). You help the actor pick one and calibrate it.

## Procedure

1. **Find the personas.** Read `_eidos/personas/` from the definition root (found by its `_eidos/` marker). If there is no `_eidos/`, no framework is installed — offer `eidos-install`. If `_eidos/` exists but has no `personas/` (an older framework), offer to install them (from the standard's `personas/`), or point to `eidos-install`/`eidos-migrate`.
2. **Read the current `_eidos/user.md`** if it exists, so you update rather than overwrite blind.
3. **Pick the persona.** With `AskUserQuestion`, offer the personas actually installed in `_eidos/personas/` — **list the folder, don't assume a cast.** Every framework carries a Framework Owner; the rest differ by seed (a software framework has a Developer and a Designer, a book framework an Editor and a Reader). Describe each from its own file. Let the actor pick one, or describe a custom role.
4. **Calibrate it** on three axes (ask, don't assume):
   - **Role for this product** — what they own here, in their words (e.g. "I own the shape of it, not the execution").
   - **Experience with the scope** — new to it, familiar, or deep. Sets how much orientation the agent gives.
   - **Technical capacity** — non-technical, some, or fluent. Sets how much mechanism and jargon the agent uses, on top of the persona's default.
5. **Write `_eidos/user.md`.** The chosen persona under `## You are: <Persona>` (a link to its persona file in `_eidos/personas/`), then a `## Calibration` block with the three axes in the actor's words. Don't fill an axis they declined — leave it for later.
6. **Confirm.** Summarize who you now understand them to be and how you'll adjust, and note they can re-run this any time their role changes.

## Boundaries

- **Personal file only.** You write `_eidos/user.md`. You don't author items (`eidos`), change the framework index (`eidos-configure`), or edit the persona definitions (those live in `_eidos/personas/`; reshape them by hand or as a team decision).
- **Never commit it.** `user.md` is gitignored by the definition's `.gitignore`. If it somehow isn't ignored, say so — it shouldn't be shared.
- **A blank actor is valid.** If the actor would rather not say, leave `user.md` blank; the agent defaults to full facilitation and can ask again later.

## Example `_eidos/user.md`

```markdown
# User

Personal and per-actor — gitignored, never shared. The agent reads it before acting.

## You are: <Role>

Persona: [_eidos/personas/<role>.md](personas/<role>.md). One line on how you want to be helped.

## Calibration

- **Role for this definition:** <what you own here, in your own words>.
- **Experience with the scope:** Deep — a year on this product. (Skip the basics.)
- **Technical capacity:** Low — explain in product/UX terms, not db/infra.
```
