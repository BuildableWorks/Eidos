# Eidos

***εἶδος** (eidos), Greek: the form or essence of a thing, the look that makes it what it is.*

> [!IMPORTANT]
> **Docs live at [eidosmd.com](https://eidosmd.com).** This repository holds the standard ([`EIDOS.md`](EIDOS.md)), the seeds, and a Claude plugin of skills. To *use* Eidos, install the CLI: `npm install -g eidosmd`, then `eidos instructions`. The skills are for hosts with no shell (Claude Desktop chat, the web, Cowork).

## **[Eidos v5.3.0](EIDOS.md)**, the standard

Eidos defines a product in markdown: an app, a book, a study, anything work produces that has a shape. One file is the complete source of truth for one unit of the product, as true of something planned as of something long shipped. The files live in your repo beside the code; the structure they follow is data in a hidden `.eidos/` folder a tool can check against. No SaaS, no lock-in, nothing outside the repo.

A tracker is a database of work, and work dies when it ships. Eidos is a database of intent. Humans and coding agents read the same source of truth, and every role answers to the same blueprint in the same words.

Eidos is **human-first**: a Framework Owner holds intent, scope, and decisions. An agent formats, asks, and presses on scope. It does not author blueprints for you.

## How it works

Three words. A **product** is what you define. A **framework** is the structure you write it in: folders, templates, properties, vocabulary, roles. A **blueprint** is one unit of the product, one file, frontmatter plus body. One framework governs any number of blueprints.

It all lives in one folder, the **root**:

```txt
Blueprints/              # the root; any name works
  .eidos/                # the framework
    plugins/<name>/      #   a tool's own folder
    roles/               #   how the agent talks to each role
    templates/           #   body templates, one per variant
    Framework.yaml       #   version, naming, folders, properties, vocabulary, index
    me.md                #   who you are (personal, gitignored)
  <Assets>/              # files that are not markdown
  <Collection>/          # blueprints of one kind
    <Group>/<Title>.md   #   one blueprint per file
  <Doc>.md               # a one-of-a-kind doc, listed in the framework
```

Every folder and file at the root is declared in `Framework.yaml`, so a reader never asks what something is. A collection's blueprints follow one of its **templates** (a collection may offer several **variants**), carry the framework's **properties** in frontmatter (four from Eidos: `id`, `title`, `summary`, `variant`; the rest are yours), and use the framework's **vocabulary**.

The standard names none of it. The [seeds](seeds) show the same machinery answering to three vocabularies:

|                    | [`software`](seeds/software)                        | [`book`](seeds/book)                      | [`research`](seeds/research)                    |
| ------------------ | --------------------------------------------------- | ----------------------------------------- | ----------------------------------------------- |
| **framing docs**   | `Frames`: architecture, audience, criteria, market  | `Frames`: premise, reader, voice, market  | `Frames`: question, prior work, method, ethics  |
| **the blueprints** | `Specs`                                             | `Chapters`                                | `Investigations`                                |
| **grouped by**     | domain                                              | part                                      | strand                                          |
| **variants**       | `full` · `micro`                                    | `full` · `sketch`                         | `full` · `note`                                 |

Pick the nearest and reshape it. A framework that ends up looking like none of them is working as intended.

## Quick start

1. `npm install -g eidosmd`, or install the [skills](#the-skills) where there is no shell.
2. `eidos init` (or the `install` skill). Pick a seed; everything in it is reshapeable later.
3. Fill the framing docs first. Loose prose: write what is known, leave the rest.
4. Author blueprints, one file each. Frontmatter is generated; the body follows the template. Press hardest on the non-goals section.
5. Commit the folder, `.eidos/` and all. Review it in PRs beside the code.

```bash
eidos init --group Identity --product "Care Connect"
eidos new specs "Session Management" --group identity
eidos check
eidos index
```

The CLI is published as [`eidosmd`](https://www.npmjs.com/package/eidosmd) and maintained by [The Virtual Panda](https://gitlab.com/the-virtual-panda/eidosmd); [eidosmd.com/docs/cli](https://eidosmd.com/docs/cli) documents every command. It carries its own copy of the standard and the seeds and versions separately; `eidos --version` names the standard it ships.

## The skills

For hosts with no shell. Eidos ships as a Claude plugin of eight skills:

| Skill       | Does                                                                   |
| ----------- | ---------------------------------------------------------------------- |
| `eidos`     | author and validate blueprints                                         |
| `iterate`   | question one rough idea until it holds still; writes nothing           |
| `format`    | reshape a rough draft into Eidos form                                  |
| `install`   | scaffold a new root from a seed                                        |
| `configure` | add a folder, variant, property, or term; keep the framework document current |
| `index`     | regenerate the index                                                   |
| `whoami`    | set your role in `me.md`                                               |
| `migrate`   | move a root to a new version of the standard                           |

**Claude Code:** `/plugin marketplace add BuildableWorks/Eidos`, then `/plugin install eidos@eidos`. For a local clone: `claude --plugin-dir /path/to/eidos`.

**Claude Desktop / Web:** Customize → Plugins → + → *add marketplace from repository* → `https://github.com/BuildableWorks/Eidos` → install **eidos**. Without repo access, `./scripts/package-plugin.sh` builds `dist/eidos-plugin.zip` to upload instead (a snapshot; it won't auto-update).

Three skills (`eidos`, `install`, `migrate`) carry committed copies of `EIDOS.md`, `seeds/`, and `versions/`, because Desktop sandboxes each skill to its own folder. The top-level files are the source of truth; [`scripts/sync-skills.sh`](scripts/sync-skills.sh) refreshes the copies, and `--check` fails if one drifts.

## Seeds

[`seeds/`](seeds) holds the starting frameworks: [`software`](seeds/software) (the default), [`book`](seeds/book), and [`research`](seeds/research). Each is a complete `.eidos/` (templates, roles, `Framework.yaml`, `me.md`, `.gitignore`) plus a root `README.md`. A seed is a starting point, not a cage: add a property, adjust a template, retune a role, none of it forks the standard.

## Versioning

Three things version separately, all [SemVer](https://semver.org/):

- **The standard**: the version in `EIDOS.md`, recorded by a root as `eidos_version`. Moves only when the text moves. Each release is frozen in [`versions/`](versions/), with upgrade paths in [`MIGRATIONS.md`](versions/MIGRATIONS.md).
- **The plugin**: `.claude-plugin/plugin.json`. Moves on every shipped release; tagged `vX.Y.Z`.
- **The CLI**: its own repo and npm. Each release names the standard it ships.

[`CHANGELOG.md`](CHANGELOG.md) tracks plugin releases and the standard each one ships; *Standard: unchanged* means your roots need nothing.

## License

[Apache License 2.0](LICENSE). Copyright © 2026 Buildable.
