<!--
The Investigation shape — the body of one line of inquiry, and the documentation of each section. An
investigation's frontmatter is generated from the framework's Schema (in Framework.md), so it is not
written here. Keep the sections that apply and delete the rest, but leave the order and headings as
they are — a reader should know what to expect from any investigation in this definition. The italic
prompts are guidance; delete them as you fill each section in.
-->

# {{title}}

## Intent

_The question this investigation answers, and why it is worth answering. One or two paragraphs, ending in an actual question mark. This is the stable part: if the question changes substantially, you have a different investigation, not an edit to this one._

### Assumptions

_What you are taking as given and have not tested — about the population, the instrument, the prior literature, the world. Nested under Intent because they frame it. Surface them so an untested assumption doesn't get read later as a finding._

## Open Questions

_What you don't yet know about how to run this — an undecided measure, an unresolved confound, a missing approval. Kept high so uncertainty is seen rather than buried. When one is settled it graduates into an Assumption, a Claim, or a Decision._

## Claims & Evidence

_What this investigation asserts, and what supports each assertion. Label each claim **C1:**, **C2:**, … (bold, unique within this investigation). Give each its evidence and its strength; a claim with no evidence yet is still a claim — mark it so. Push data, tables, and instrument detail into a sub-section a claim points to, not onto the line. Evolves freely._

- **C1:** <!-- the assertion --> <!-- evidence: … -->

## What Would Change Our Mind

_The falsifier: the specific result that would make you abandon or revise the claims above. Concrete enough that someone could go and look. An investigation with no falsifier is an opinion with citations, and this is the section this framework leans on hardest._

## Out of Scope

_What this investigation **cannot** tell you, and who will be tempted to think it can. Populations not sampled, mechanisms not tested, the causal claim the design does not support. The second-hardest-working section here: it is what keeps a finding from being over-read downstream._

## Dependencies

_What this needs before it can run: data, access, approvals, instruments, or another investigation's result. The `depends_on` property at the top is the investigation-only subset of this, as links. Reference other investigations as markdown links — never bare names._

## Method

_How the question is actually approached: design, sample, measures, analysis. Enough that a reader can judge whether the Claims follow. Detail belongs here rather than on a claim line; a full protocol can live in its own top-level doc this section points at._

## Notes & Decisions

_Two things under one header. **Notes**: threats to validity, things to chase, what surprised you. **Decisions**: an append-only log, one line each, with an optional but recommended date._

<!-- 2026-08-26: Dropped the second cohort, consent window closed. (Brenton) -->
