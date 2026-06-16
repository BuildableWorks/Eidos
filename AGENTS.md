# Agents

This repository is the home of the **Eidos** standard. `EIDOS.md` is the
authoritative definition of the format; everything else supports it.

**Use the `eidos` skill to author or validate specs.** It is vendored at
[`.claude/skills/eidos/`](.claude/skills/eidos) and contains the workflow, schema,
templates, and a worked example. Read it (and `EIDOS.md`) before creating or
reviewing any spec or product doc.

**Keep the README badge in sync.** When `EIDOS.md` changes version (the
`**Version:**` header and the Versioning section), update the badge line at the top
of `README.md` so it shows the current version, e.g. `[Eidos v1.0.0](EIDOS.md)`.
Also update `version` in `manifest.json` and add an entry to `CHANGELOG.md`.

**On a new major version,** preserve the outgoing `EIDOS.md` in `versions/` (e.g.
`versions/v1.md`) before editing `EIDOS.md` in place.
