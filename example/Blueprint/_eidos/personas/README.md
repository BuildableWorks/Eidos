# Personas

Default **personas** for Eidos — who is in the seat, and how the agent should respond to them. A persona is a **response contract**: it sets the vocabulary, the level of technical depth, what to surface vs. fold away, and who holds which decisions. The agent reads it **before acting** (see [`EIDOS.md`](../EIDOS.md), "The actor").

These are the opinionated baseline, browsable here and installed into a registry's `.eidos/personas/` by `eidos-init` (committed, so a team can tune how a role is treated for their product). Each person who works in the registry picks one in their personal, gitignored `.eidos/user.md` and **calibrates** it — their role on this product, their experience with the scope, and their technical capacity — with the `eidos-whoami` skill. Persona sets the baseline; calibration tunes it per person.

- [Product Owner](product-owner.md) — holds intent, scope, and decisions.
- [Developer](developer.md) — builds from the specs.
- [Stakeholder](stakeholder.md) — reviews direction.
- [Designer](designer.md) — shapes the experience.

A persona is a baseline, not a cage: an actor can write a custom role in their `user.md`, and a registry can add or reshape persona files here. The human-first principle holds for every persona — the human authors and decides; the persona only changes _how_ the agent helps.
