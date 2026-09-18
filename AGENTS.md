# Agents

This repository is the home of the **Eidos** standard. `EIDOS.md` is the authoritative definition; everything else supports it. Read it, and the relevant skill in [`skills/`](skills), before creating, scaffolding, migrating, or reviewing anything in a root.

**What lives where.** This repository owns the standard (`EIDOS.md`, frozen per release in `versions/`), the seeds (`seeds/`), and the Claude plugin of eight skills (`skills/`). The `eidos` CLI (npm `eidosmd`) is The Virtual Panda's, at [gitlab.com/the-virtual-panda/eidosmd](https://gitlab.com/the-virtual-panda/eidosmd); it vendors `EIDOS.md` and `seeds/` from a checkout here with its own sync script, so a release of the standard is followed by a sync and a release there. A change to how the tool behaves belongs over there; a change to what conforms belongs here.

**Eidos is human-first.** The Framework Owner holds intent, scope, and decisions. Format, supplement, ask, and press on scope; never generate finished blueprints or set direction.

## Two versions, bumped separately

- **The plugin version** lives in `.claude-plugin/plugin.json` **and** `.claude-plugin/marketplace.json` (both, or updates no-op: Claude Code compares the marketplace field against the installed version). It moves on every shipped release, including skill-only and seed-only ones. Each release gets a `CHANGELOG.md` entry naming the plugin version and, on its first line, the standard it ships.
- **The standard version** lives in `EIDOS.md` (`**Version:**`, the Versioning section, the `eidos_version` in the sample YAML). It moves only when the text of `EIDOS.md` moves. When it does, also update the heading in `README.md` and `eidos_version` in every `seeds/*/.eidos/Framework.yaml`, copy `EIDOS.md` to `versions/vX.Y.Z.md`, add the hop to `versions/MIGRATIONS.md` (newest first) and the line to `versions/README.md`, and fingerprint it in `skills/migrate/SKILL.md`.

A skill fix bumps the plugin and nothing else.

**Tag every shipped release `vX.Y.Z`** on the plugin version, lightweight, on the release's final commit: `git tag v5.3.0 && git push origin v5.3.0`. The standard's artifact is the file in `versions/`; the plugin's is the tag. There is no second tag namespace, and tags are not how an install detects an update.

**After changing `EIDOS.md`, `seeds/`, `versions/`, or `CHANGELOG.md`, run `scripts/sync-skills.sh`** and commit the updated copies in `skills/eidos`, `skills/install`, and `skills/migrate`. They are committed because Claude Desktop sandboxes each skill to its own folder. `scripts/sync-skills.sh --check` verifies them; `scripts/package-plugin.sh` refreshes them before zipping.
