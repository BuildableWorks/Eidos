# Project Manager

## Who they are

Tracks **scope and progress**, not product direction or implementation. Wants to know what is in and out of scope, how far along the work is, where the dependencies and risks are, and what is left, and to keep that picture current as the blueprints change.

## How to respond

- **Vocabulary & depth:** scope, status, dependencies, risk, and effort, in plain terms. Skip deep implementation and product rationale unless it bears on scope or schedule.
- **Decisions:** none are theirs. They don't set direction (the owners) or make technical calls (the Developer); they surface scope creep, blocked or at-risk work, and gaps, and bring them to whoever owns the call.
- **Surface / hide:** surface **Out of Scope** (the in/out line), each blueprint's `status`, `depends_on` and other dependencies, the decisions waiting on a sign-off, and the Backlog: the tasks that serve each blueprint, their status, milestone, and what blocks them. Fold away mechanism and prose rationale.
- **Focus:** what is in vs. out, which blueprints are approved, what the Backlog says is moving or stuck, and where scope is drifting from Criteria.

A blueprint captures **state and intent, not work**: it has no sprint, estimate, or assignee, on purpose. Progress lives on the Backlog, where each task names the blueprints it serves; read movement from there and from git history, never by adding work fields to a blueprint. Infer **level of effort** from a blueprint's shape (its requirements, dependencies, and open questions) and from the tasks that serve it, not a stored estimate.

## Calibration

Usually moderate **technical capacity**, and broad-but-shallow **experience with the scope**: they span the whole product rather than living in one unit. Lean on `status`, the Backlog, dependencies, and the in/out line.
