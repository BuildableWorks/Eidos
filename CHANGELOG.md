# Changelog

**About:** The current version of the standard is always the one in `EIDOS.md`. It
follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`). Major
bumps for breaking changes, minor for backward-compatible additions, patch for
clarifications. When releasing a new major version, preserve the outgoing `EIDOS.md`
in `versions/` (e.g. `versions/v1.md`).

---

## 1.0.0

- **Summary:** Initial published version of the Eidos standard. The normative
  definition now lives in a single top-level `EIDOS.md`; the repository becomes the
  versioned home of the standard, modeled on the backlog.md layout.
- **Added:**
  - **`EIDOS.md`** — the authoritative standard, consolidated from the skill: what a
    spec is, the two-tier document model, directory layout, product docs, the spec
    frontmatter contract (required + optional fields), recommended body sections,
    load-bearing rules, the optional `domains.md` descriptions, validation, and
    versioning.
  - **`CHANGELOG.md`** — this file.
  - **`manifest.json`** — machine-readable pointer to the current `version`.
  - **`AGENTS.md`** — directs agents to the `eidos` skill and the README sync rule.
  - **`versions/`** — reserved for preserved prior major versions of `EIDOS.md`.
  - **`example/`** — a filled-in worked example of an Eidos product definition.
  - **`.claude/skills/eidos/`** — the authoring/validation skill, vendored in-repo.
- **Removed:**
  - The blank `product/` scaffold. Authors copy `example/` (or run the skill)
    instead of filling empty templates checked into the standard's repo.
