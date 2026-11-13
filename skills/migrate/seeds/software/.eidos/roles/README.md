# Roles

Default **roles** for this framework: who is in the seat, and how the agent should respond to them. A role is a **response contract**: it sets the vocabulary, the level of technical depth, what to surface and what to fold away, and who holds which decisions. The agent reads it **before acting** (see the Eidos standard's `EIDOS.md`, "Roles").

These are the opinionated baseline, installed into a project's `.eidos/roles/` with the framework and committed, so a team can tune how a role is treated for their product. Each person who works in the project picks one in their local, gitignored `.eidos/me.md` and **calibrates** it (what they own here, their experience with the scope, and their technical capacity) with `eidos whoami`. Role sets the baseline; calibration tunes it per person.

- [Developer](developer.md): builds from the blueprints.
- [Designer](designer.md): shapes the experience.
- [QA Engineer](qa-engineer.md): holds the build to what the specs promise.
- [Project Manager](project-manager.md): tracks scope and progress.
- [Stakeholder](stakeholder.md): reviews direction.

A role is a baseline, not a cage: anyone can write a custom role in their `me.md`, and a framework can add or reshape role files here. The human-first principle holds for every role: the human authors and decides; the role only changes _how_ the agent helps.
