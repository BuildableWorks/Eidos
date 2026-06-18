# Changelog

All notable changes to the Eidos standard are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). The current version of the standard always lives in `EIDOS.md`; each prior released version is frozen in `versions/` under its full semver name.

## [Unreleased]

### Added

- Apache License 2.0 (`LICENSE`); `license: Apache-2.0` declared in the plugin manifest.

### Fixed

- The `eidos` skill resolved templates from a bare `templates/` path, so when used in an adopting repo it looked in that project's working directory instead of the standard. It now resolves them the same way `eidos-init`/`eidos-migrate` do — `${CLAUDE_PLUGIN_ROOT}/templates/` in Claude Code, a vendored copy inside the skill on Claude Desktop — and `scripts/sync-skills.sh` vendors `templates/` into `eidos` too. An adopting repo holds only `Blueprint/`; it never needs a `templates/` folder of its own.

## [2.0.0] - 2026-06-17

A breaking redesign of the spec contract and body. Eidos now captures the _intent_ of the build (never work or status), carries requirements as labeled acceptance criteria, and ships a default `Domains.md` and a `Blueprint/` root.

### Added

- `created` and `modified` frontmatter fields (`YYYY-MM-DD`).
- `## Dependencies` and `## Testing` body sections.
- Optional `### Implementation Notes` under `## Intent` — the intent of the implementation, never its state.
- `**AC{n}:**` labels for acceptance criteria, unique within a spec for reference, under requirement sub-headings (Functional, Performance, Design, External interface, Quality attributes) inside `## Behaviors & Acceptance Criteria`.
- `Domains.md` as part of the default layout, with a new `templates/Domains Template.md`.
- Full-semver version snapshots in `versions/`, plus an `eidos-migrate` skill for non-sequential migration between any two versions.
- An optional, recommended `eidos_version` frontmatter field, so each doc declares the standard it targets (aids migration and tooling).
- An `eidos-init` skill that scaffolds a new registry from the templates, following the current `EIDOS.md` (no example-copying).
- Packaged as an installable Claude Code plugin (`.claude-plugin/`), with the skills in the top-level `skills/` and `scripts/sync-skills.sh` to vendor assets for standalone use.

### Changed

- Renamed the registry root from `product/` to `Blueprint/` — it sorts to the top of the file tree and reads as the product's defining document; still low-stakes and renameable, since nothing points at it by path.
- `## Behavior` → `## Behaviors & Acceptance Criteria`.
- Merged `## Constraints` and `## Decisions` into a single `## Constraints & Decisions`; decision dates are now optional.
- `status` is a soft baseline — `Draft | Intake | In Progress | Done | Archived | Deprecated` (an off-list value warns, never fails) — shown bracketed in the template; `type` is shown bracketed too.
- `Domains.md` uses `##` sub-headings per domain instead of a bullet list, and is listed among the product docs.
- `Open Questions` → `Open Questions & Assumptions`, moved up to just after Intent.
- Criteria: `Objective and scope` → `Scope Objectives`, plus a new `Parameters & Variables` section. Market: a new `Competitors` section, with `Position and difference` → `Positioning & Differentiators` and `How it earns` → `Earning Capabilities`. Product docs no longer carry a `Decisions` log.
- Plain-language pass across `EIDOS.md` and the README for non-technical readers.

### Removed

- Frontmatter fields `last_validated`, `implements`, `serves_job`, `activity`, and `supersedes`.
- The `manifest.json` version pointer — the `EIDOS.md` header and `.claude-plugin/plugin.json` already carry the version, and nothing consumed it.

**Migration from 1.x:** use the `eidos-migrate` skill, or diff `versions/v1.0.0.md` against `EIDOS.md`. Map `status` (`proposed`/`accepted` → `Intake`, `in-progress` → `In Progress`, `shipped` → `Done`, `deprecated` → `Deprecated`); carry `last_validated` into `modified`; relabel behaviors as `AC{n}`; merge Constraints and Decisions; add `Dependencies` and `Testing`.

## [1.0.0] - 2026-06-16

Initial published version of the Eidos standard. The normative definition lives in a single top-level `EIDOS.md`; the repository is the versioned home of the standard, modeled on the backlog.md layout.

### Added

- `EIDOS.md` — the authoritative standard: what a spec is, the two-tier document model, directory layout, product docs, the spec frontmatter contract (required + optional fields), recommended body sections, load-bearing rules, the optional `Domains.md` descriptions, validation, and versioning.
- `CHANGELOG.md`, `manifest.json` (machine-readable version pointer), and `AGENTS.md`.
- `versions/` — reserved for preserved prior versions of `EIDOS.md`.
- `example/` — a filled-in worked example of an Eidos product definition.
- `.claude/skills/eidos/` — the authoring/validation skill, vendored in-repo.

### Removed

- The blank `product/` scaffold. Authors copy `example/` (or run the skill) instead of filling empty templates checked into the standard's repo.

[Unreleased]: https://gitlab.com/the-virtual-panda/Eidos/-/compare/v2.0.0...HEAD
[2.0.0]: https://gitlab.com/the-virtual-panda/Eidos/-/compare/v1.0.0...v2.0.0
[1.0.0]: https://gitlab.com/the-virtual-panda/Eidos/-/tags/v1.0.0
