---
name: whoami
description: >-
  Set or update who you are in a root: your role and calibration, written to your personal `.eidos/me.md`. Use for "set my user", "I'm the designer", "change my role", "the AI is talking over my head", "it's explaining things I already know", or when `me.md` is blank or absent. Offers the roles the framework installed, calibrates the chosen one on three axes, and writes the file. Personal and gitignored; the agent reads it before acting.
---

# Eidos Whoami

A role is a response contract: vocabulary, depth, what to surface, who decides. `me.md` names yours and tunes it. Each person runs this for themselves; the file is gitignored and never lands in another checkout. You do not write role content (that lives in `.eidos/roles/`); you help the person pick one and calibrate it.

## Procedure

1. **Find the roles** in `.eidos/roles/`. No `.eidos/` means offer `install`; an `.eidos/` with no `roles/` is an older framework, offer `migrate`.
2. **Read the current `me.md`**, if any, so you update rather than overwrite blind.
3. **Pick the role.** Offer the roles actually installed, described from their own files; never assume a cast. Every framework has a Framework Owner; the rest differ by seed. A custom role in their own words is fine.
4. **Calibrate** on three axes, asking rather than assuming: **ownership** (what they own here), **experience with the scope** (new, familiar, deep), **technical capacity** (non-technical, some, fluent). Leave an axis they decline blank.
5. **Write `.eidos/me.md`** and confirm how you will adjust. They can re-run this any time.

```markdown
# Me

## You are: <Role>

Role: [.eidos/roles/<role>.md](roles/<role>.md). One line on how you want to be helped.

## Calibration

- **Ownership:** <in your own words>
- **Experience with the scope:** Deep; a year on this product.
- **Technical capacity:** Low; explain in product terms, not infrastructure.
```

A blank `me.md` is valid: the agent defaults to full facilitation. If `me.md` is not gitignored, say so.
