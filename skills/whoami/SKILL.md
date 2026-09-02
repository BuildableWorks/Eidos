---
name: whoami
description: >-
  Set or update who you are in a root — your role and calibration — written to your personal `_eidos/me.md`. Use when someone wants to "set my user", "tell Eidos who I am", "I'm the designer / a developer / the framework owner", "change my role", "set up who I am", "the AI is talking over my head" or "it's explaining things I already know", or when `_eidos/me.md` is blank or absent. It offers whatever roles the framework installed (`_eidos/roles/`), then calibrates the chosen one on three axes — your role for this product, your experience with the scope, and your technical capacity — and writes `_eidos/me.md`. That file is personal and gitignored; the agent reads it before acting to decide how to respond (vocabulary, depth, what to surface, who decides). Companion to `install`, which scaffolds the folder; this sets the actor.
---

# Eidos Whoami

Set the **actor** — who is in the seat — so the agent knows how to respond to _you_. Writes your personal `_eidos/me.md`: a **role** (the baseline response contract) plus a **calibration** (how it adjusts for you). Companion to `install`: that one scaffolds the folder, this one is about the person.

`_eidos/me.md` is **personal and gitignored** — each person who works on the folder runs this for themselves, and no one's role lands in anyone else's checkout.

## Why this matters

A role is a response contract: vocabulary and technical depth, what to surface vs. fold away, who holds which decisions. One role is told to keep mechanism out of the reply; another gets full technical depth; the Framework Owner is brought the decisions. Without an actor the agent defaults to full facilitation — workable, but generic.

## How you work

A short guided interview, then a small file write. You do **not** invent role content — it lives in `_eidos/roles/`. You help the actor pick one and calibrate it.

## Procedure

1. **Find the roles.** Read `_eidos/roles/` from the root, found by its `_eidos/` marker. No `_eidos/` means no framework installed — offer `install`. An `_eidos/` with no `roles/` is an older framework — offer to install a seed's, or point to `migrate`.
2. **Read the current `_eidos/me.md`** if it exists, so you update rather than overwrite blind.
3. **Pick the role.** With `AskUserQuestion`, offer the roles actually installed in `_eidos/roles/` — **list the folder, don't assume a cast.** Every framework carries a Framework Owner; the rest differ by seed (a software framework has a Developer and a Designer, a book framework an Editor and a Reader). Describe each from its own file. Let the actor pick one, or describe a custom role.
4. **Calibrate it** on three axes (ask, don't assume):
   - **Ownership** — what they own on this folder, in their own words.
   - **Experience with the scope** — new, familiar, or deep. Sets how much orientation to give.
   - **Technical capacity** — non-technical, some, or fluent. Sets how much mechanism and jargon, on top of the role's default.
5. **Write `_eidos/me.md`.** The chosen role under `## You are: <Role>` (a link to its role file in `_eidos/roles/`), then a `## Calibration` block with the three axes in the actor's words. Don't fill an axis they declined — leave it for later.
6. **Confirm.** Summarize who you now understand them to be and how you'll adjust, and note they can re-run this any time their role changes.

## Boundaries

- **Personal file only.** You write `_eidos/me.md` — not blueprints (`eidos`), not the framework index (`configure`), not the role files themselves (a team decision).
- **Never commit it.** `me.md` is gitignored by the root's `.gitignore`. If it somehow isn't ignored, say so — it shouldn't be shared.
- **A blank actor is valid.** If the actor would rather not say, leave `me.md` blank; the agent defaults to full facilitation and can ask again later.

## Example `_eidos/me.md`

```markdown
# Me

Personal and per-actor — gitignored, never shared. The agent reads it before acting.

## You are: <Role>

Role: [_eidos/roles/<role>.md](roles/<role>.md). One line on how you want to be helped.

## Calibration

- **Ownership:** <what you own on this folder, in your own words>.
- **Experience with the scope:** Deep — a year on this product. (Skip the basics.)
- **Technical capacity:** Low — explain in product/UX terms, not db/infra.
```
