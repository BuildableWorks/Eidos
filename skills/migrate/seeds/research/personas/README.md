# Personas

Default **personas** for this framework — who is in the seat, and how the agent should respond to them. A persona is a **response contract**: it sets the vocabulary, the level of technical depth, what to surface vs. fold away, and who holds which decisions. The agent reads it **before acting** (see the Eidos standard's `EIDOS.md`, "The actor").

These are the research seed's baseline, browsable here and installed into a definition's `_eidos/personas/` by `install` (committed, so a team can tune how a role is treated for their programme). Each person who works on the definition picks one in their personal, gitignored `_eidos/user.md` and **calibrates** it — their role on this definition, their experience with the scope, and their technical capacity — with the `whoami` skill. Persona sets the baseline; calibration tunes it per person.

- [Framework Owner](framework-owner.md) — holds intent, scope, and decisions.
- [Researcher](researcher.md) — does the work; needs the design in full.
- [Reviewer](reviewer.md) — reads to find the hole; adversarial by design.
- [Sponsor](sponsor.md) — funds or answers for it; needs what it can and cannot conclude.

A persona is a baseline, not a cage: an actor can write a custom role in their `user.md`, and a framework can add or reshape persona files here. The human-first principle holds for every persona — the human authors and decides; the persona only changes _how_ the agent helps.
