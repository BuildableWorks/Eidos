<!--
The Spec shape — micro flavor. The smallest spec worth writing: why it exists, what you're getting,
and what it will not do. A starting point that grows into the full flavor (spec.full.md) as the unit
firms up — add the full flavor's sections (Implementation Notes, Dependencies, Testing, Constraints &
Decisions, …) when they earn their place, and set `flavor: full` (or drop `flavor`) once it has.
A spec's frontmatter is generated from .eidos/Schema.md, so it is not written here. Keep the order and
headings; the italic prompts are guidance — delete them as you fill each section in.
-->

# {{title}}

## Intent

_Why this exists — the problem and who has it. One or two paragraphs. This is the stable part: if Intent changes substantially, you probably have a different spec, not an edit to this one._

## Open Questions & Assumptions

_Unresolved questions, and the assumptions you're proceeding on — kept high, right after Intent, so uncertainty is seen rather than buried, and guesses don't leak into Behaviors as if they were settled. A micro spec almost always has these; surfacing them is half the point of writing one early._

## Behaviors & Acceptance Criteria

_What it does, as observable outcomes — the "this is what you're getting" section. If a behavior isn't listed here, it isn't promised. Label each criterion **AC1:**, **AC2:**, … (bold, unique within this spec). Keep each short and checkable; push rich detail into a table or sub-section it points to._

- **AC1:** <!-- the first observable outcome -->

## Out of Scope

_Explicit non-goals — the section the standard leans on hardest, because this is where scope is held. A micro spec carries it too; it's the first thing to write, not the last._
