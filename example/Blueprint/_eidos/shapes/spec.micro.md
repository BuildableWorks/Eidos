<!--
The Spec shape — micro flavor. The smallest spec worth writing: why it exists, what you're getting,
and what it will not do. A starting point that grows into the full flavor (spec.full.md) as the unit
firms up — add the full flavor's sections (Implementation Notes, Dependencies, Testing, Constraints &
Decisions, …) when they earn their place, and set `flavor: full` (or drop `flavor`) once it has.
A spec's frontmatter is generated from the registry's Schema (in Registry.md), so it is not written here. Keep the order and
headings; the italic prompts are guidance — delete them as you fill each section in.
-->

# {{title}}

## Intent

_Why this exists — the problem and who has it. One or two paragraphs. This is the stable part: if Intent changes substantially, you probably have a different spec, not an edit to this one._

### Assumptions

_The assumptions you're proceeding on — what you're taking as given, not yet confirmed. Nested under Intent because they frame it. A micro spec almost always has some; surfacing them is half the point of writing one early._

## Open Questions

_Unresolved questions — what you don't yet know and still need answered. Kept high, right after Intent, so uncertainty is seen rather than buried; when one is settled it graduates into an Assumption, a Behavior, or a Decision._

## Behaviors & Acceptance Criteria

_What it does, as observable outcomes — the "this is what you're getting" section. If a behavior isn't listed here, it isn't promised. Label each criterion **AC1:**, **AC2:**, … (bold, unique within this spec). Keep each short and checkable; push rich detail into a table or sub-section it points to._

- **AC1:** <!-- the first observable outcome -->

## Out of Scope

_Explicit non-goals — the section the standard leans on hardest, because this is where scope is held. A micro spec carries it too; it's the first thing to write, not the last._
