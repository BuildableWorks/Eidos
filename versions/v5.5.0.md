# Eidos

**Version:** 5.5.0

Eidos is a way to define a product in markdown: an app, a book, a study, anything work produces that has a shape. The structure is data in a hidden folder that a tool can check against; the product is written in markdown against that structure. One file is the complete source of truth for one unit of the product, as true of something planned as of something long shipped.

This file is the contract: the terms, the layout, and the rules. It names no collection, template, or section; those belong to a framework.

## Terms

| Term              | What it is                                                                                                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **product**       | What you are defining.                                                                                                                                                 |
| **framework**     | How the files are organized: folders, templates, properties, vocabulary, roles. Lives in `.eidos/`; one framework can govern many products.                            |
| **root**          | The folder it all lives in. Found by the `.eidos/` inside it, never by its name.                                                                                       |
| **folder**        | A top-level folder in the root, declared with who owns it: `@eidos/collections` for the standard, `@<tool>/<kind>` for a tool, nobody for the person's own.            |
| **collection**    | A folder owned by `@eidos/collections`, holding blueprints of one kind: specs, chapters, investigations. Its sub-folders, if any, are its declared groups.             |
| **blueprint**     | One markdown file in a collection, defining one unit of the product completely: properties on top, a body below.                                                       |
| **unit**          | What one blueprint defines: a spec, a chapter, an investigation. Templates are named for it, singular.                                                                 |
| **template**      | The body a collection's blueprints follow: sections in order, under set names. Body only. One file per variant in `.eidos/templates/`.                                 |
| **variant**       | One of a collection's templates (`<unit>.<variant>.md`). The collection, or a group in it, may name a default; a blueprint on another says so in `variant`.            |
| **property**      | One frontmatter field: name, type, which collections it applies to, whether required, meaning, and options when closed. The whole table is the framework's Properties. |
| **vocabulary**    | The framework's table of words used on purpose: what each means and what it is not.                                                                                    |
| **top-level doc** | A one-of-a-kind file at the root, listed in the framework document. No template; the body is never validated.                                                          |
| **role**          | How an agent talks to one kind of person. `.eidos/me.md` says which role is in the seat.                                                                               |
| **plugin**        | A tool's own folder, `.eidos/plugins/<name>/`, and any root folder it owns. The standard reads none of it.                                                             |
| **region**        | A span in a markdown file that a tool owns, fenced by two HTML comments carrying its name. The standard reads none of it.                                              |

A task describes work and dies when it ships. A blueprint describes the product and stays accurate for its whole life.

## Layout

```txt
Blueprints/              # the root; any name works, this is the default
  .eidos/                # the framework
    plugins/<name>/      #   a tool's own folder; local.yaml and local/ inside it stay on this machine (gitignored)
    roles/<role>.md      #   response contracts
    templates/           #   <unit>.<variant>.md, one per variant
    .gitignore           #   ignores me.md, plugins/*/local.yaml, and plugins/*/local/
    Framework.yaml       #   the framework document
    me.md                #   who is in the seat (local, gitignored)
  <Collection>/          # owned by @eidos/collections: blueprints
    <Group>/             #   a declared group; nothing deeper
      <Title>.md         #     one blueprint per file
  <Folder>/              # owned by a tool (@<tool>/<kind>) or by nobody: declared, never read
  <Doc>.md               # a top-level doc, listed under top_level
```

**Everything at the root is declared.** A folder is `.eidos/` or declared under `folders`; a file is listed under `top_level`. Anything else is surfaced, and the owner declares it or moves it. Hidden entries (`.git`, `.obsidian/`) are the host's and exempt.

### Folders

| Owner                | Holds                                     | The standard                                                                    |
| -------------------- | ----------------------------------------- | ------------------------------------------------------------------------------- |
| `@eidos/collections` | blueprints, optionally in declared groups | generates, validates, and indexes the markdown files; ignores any other file    |
| `@<tool>/<kind>`     | whatever that tool says                   | reads nothing inside; the folder is declared and left to its tool, known or not |
| none                 | whatever the description says             | reads nothing inside; the folder is declared and otherwise left alone           |

An owner is `@<tool>/<kind>`, quoted in YAML: the tool's one identifier, then the tool's own name for what the folder holds, in the same characters. The standard owns `@eidos/collections` and defines nothing else under `@eidos/`. A tool registers as many kinds as it needs, and what a folder under one holds, how it is named, and what is checked inside are that tool's to say. A check faults an owner that is malformed or an `@eidos/` kind the standard does not name, and never a tool's.

A collection is flat or grouped. Grouped, every sub-folder is a declared group, and a group holds blueprints and nothing deeper. A grouping property's value is the group's name; an unknown value warns.

### Plugins

The top level of `.eidos/` is the standard's. A tool keeps what it needs in `.eidos/plugins/<name>/` and touches nothing else. The name is one identifier everywhere the tool appears (its folder, its Properties block, its regions, the root folders it owns): lowercase letters, digits, hyphens, unique in the root; `eidos` is reserved. A check never faults a plugin folder and a migration carries it across untouched. A tool's `local.yaml` is one person's settings and its `local/` folder one person's files, neither ever committed; nothing else in the folder is local.

### `Framework.yaml`

One per root, `Framework.yaml` or `.yml`, snake_case, comments welcome. Every path is relative to `.eidos/`.

```yaml
eidos_version: 5.5.0
naming: kebab-case            # kebab-case (default) | TitleCase | Title Case
top_level:
  - { title: <Title>, path: ../<Doc>.md, description: one line }
folders:
  - name: <Collection>
    owned_by: "@eidos/collections"
    description: one line
    variants:
      - { name: <variant>, template: templates/<unit>.<variant>.md, description: one line, default: true }
    grouping:
      label: <Grouping>
      property: <name>          # the custom property carrying the group, if one does
      groups:
        - { name: <Group>, description: one line, default_variant: <variant> }   # optional: this group's default
  - { name: <Folder>, owned_by: "@<tool>/<kind>", description: one line }
  - { name: <Folder>, description: one line }
properties:
  core: []                    # the standard's; empty = the core for this eidos_version
  custom:
    - { name: <name>, type: Text, applies_to: all, required: true, meaning: one line }
    - { name: <name>, type: Text, applies_to: [<Collection>], options: [<Value>, <Value>], meaning: one line }
  tools:
    <tool>:
      - { name: <name>, type: Text, applies_to: all, meaning: one line }
vocabulary:
  - { term: <Term>, means: one line, not: ["<near-miss>, and why"], see: ../<Collection>/<Title>.md }
index:                        # generated; never hand-edited
  <Collection>:
    - { id: <id>, title: <Title>, summary: <summary>, path: <Group>/<Title>.md, group: <Group> }
```

- **`top_level`**: every file at the root, each a `title`, `path`, and `description`.
- **`folders`**: every folder at the root, each a `name` and `description`, and `owned_by` when something owns it. A `@eidos/collections` folder also carries `variants` (`default: true` marks the collection's default; with none marked, it has none) and `grouping`. A group may name its own default with `default_variant`, one of the collection's variants. A malformed owner, or an `@eidos/` kind the standard does not name, is a fault; a tool's owner never is.
- **`properties`**: one block per owner. `core` is the standard's, rewritten by a migration. `custom` is the owner's. `tools.<tool>` is that tool's alone. The six keys the standard names are the standard's; any other key on an entry is a tool's.
- **`vocabulary`**: the root's own terms. Starts empty.
- **`index`**: every collection's blueprints, rebuilt wholesale by whatever indexes the root, which touches no other key.

### Templates

A template is body only: sections in order, under set names, with guidance. Frontmatter in a template is a fault. The file is `<unit>.<variant>.md`, lowercase. A blueprint is validated against the variant it names; a lighter variant is never faulted for sections only a fuller one has.

### Properties

Each entry: `name`, `type`, `applies_to`, `required`, `meaning`, and `options` when the value is one of a closed set.

- **type** is one of Text, List, Number, Checkbox, Date, Date & time.
- **applies_to** is `all` or a list of collections.
- **required** (absent = `false`): a required property is generated into every new blueprint and surfaced when missing. An optional one is written when it has a value; its absence is never a gap.
- **options**: an ordered, non-empty list of allowed values, compared exactly. An off-list value is surfaced, never refused. An empty list is a fault. No default rides with it. `variant` and a grouping property take their sets from the structure and never carry `options`.

The block a property sits in owns it, and only the owner writes there. The core:

| Name      | Type | Required | Meaning                                                                                    |
| --------- | ---- | -------- | ------------------------------------------------------------------------------------------ |
| `id`      | Text | yes      | Stable, unique identity, in any form. Assigned once, never changed.                        |
| `title`   | Text | yes      | Human-readable name. Rename freely; `id` holds still.                                      |
| `summary` | Text | no       | One line: what this blueprint is. Feeds the index; absent, the index flags it.             |
| `variant` | Text | no       | Which variant this blueprint follows. Absent = its group's default, else the collection's. |

A tool that scaffolds a blueprint writes the variant it resolved; with no default at either level, the person picks. Moving a blueprint to another group never changes its `variant`.

Eidos defines no custom properties. Status, dates, grouping, dependencies: all the framework's choice.

### Vocabulary

Each entry: `term`, `means`, `not` (the near-misses and why each differs), and `see` when a blueprint defines it in full. Eidos declares none of a root's terms. Where a term is declared, blueprints use it; a near-miss is flagged with the term beside it, never swapped in silently.

### Roles

`.eidos/roles/<role>.md` says how an agent responds to one kind of person: depth, what to surface, who decides. The people who own the product hold intent, scope, and decisions. `.eidos/me.md` names your role and calibrates it on ownership, experience with the scope, and technical capacity. Blank is fine.

## Writing

### Naming

Everything a human reads in the tree follows `naming`. Absent means `kebab-case`.

| Convention               | A blueprint file          | A group folder | Trade                                 |
| ------------------------ | ------------------------- | -------------- | ------------------------------------- |
| **kebab-case** (default) | `blueprint-title-here.md` | `group-name/`  | readable everywhere, no `%20`         |
| **TitleCase**            | `BlueprintTitleHere.md`   | `GroupName/`   | space-free, capitalized               |
| **Title Case**           | `Blueprint Title Here.md` | `Group Name/`  | reads like prose, `%20` in every link |

Exceptions: `.eidos/` is lowercase, `README.md` keeps its name, a grouping value matches its folder exactly, a folder a tool owns is named as the tool says, and nothing inside a folder the standard does not own is held to the convention.

### Linking

A standard markdown link, path relative to the file it sits in, text the human title, `#heading` for a section. Properties that point outward hold links too, quoted in YAML. Files that are not blueprints are linked or embedded the same way (`![Login flow](../assets/login-flow.png)`): no wikilinks, no absolute paths, no resolution by filename. A check verifies the path resolves. If a target has no blueprint yet, name it plainly.

### Bodies

A blueprint's body follows its variant's template: keep the order and names, leave out a section that doesn't apply rather than leaving it empty, and write it like a person would read it. A top-level doc is loose prose, revised in place, with no template.

### Regions

A tool keeps what it needs inside a markdown file between `<!-- <tool>:<region> <args> -->` and `<!-- /<tool>:<region> -->`, each alone on its line. `<args>` is optional `key=value` pairs. Inside is the tool's, rewritten wholesale; outside is the person's. A region closes at the first matching closer (`-->` or `--!>`); a marker inside a fenced code block is text. An opener with no closer is faulted; a region for an unknown tool never is. Frontmatter holds no regions.

## The index

The one derived view the standard defines. Every collection's blueprints, under `index`: `id`, `title`, `summary` (null when absent, never invented), `path` relative to the collection, and `group`. Grouped by group when the collection has them, in file order. Any other view is a tool's, written as a top-level doc.

## Rules

1. **The frontmatter is the agreement; the body is guidance.** Properties are checked. Sections are recommended.
2. **The root owns its framework.** A tool reads the framework from the root it is in, never from a copy of its own.
3. **Validation is framework-defined.** A check enforces that framework's Properties table, nothing hardcoded.
4. **Surface, never refuse.** A missing required property is added with a note; a missing section is offered. Never refuse the file.
5. **Write it like a human would read it.** If it reads like filled-in boilerplate, reshape it.
6. **Reference blueprints with links, not bare names,** in prose and properties alike. `id` sits behind the link.
7. **One template family per collection, as variants.** What flexes is which sections appear; never their order or names.
8. **Every property has a type, a meaning, and an owner.** Frontmatter is generated from the required ones, so a new blueprint is born conforming.
9. **Soft labels are views, not structure.** A category property drives filtering, never structure. `variant` carries the structural choice.
10. **A collection's grouping is its own.** Every sub-folder is a declared group; a group holds blueprints and nothing deeper.
11. **A template names its own stable part.** If the stable part changes substantially, ask whether this is a different blueprint.
12. **Non-goals carry the most weight.** Where a template has a section for what a blueprint will not do, that section is its strongest.
13. **A template documents its own conventions.** The standard governs folders, templates, variants, and properties; never a section.
14. **No work-tracking fields.** No sprint, estimate, or assignee; bridge to a tracker with a link. Intent, never progress.
15. **The Eidos version is a framework fact,** in `eidos_version`, never on a blueprint.
16. **Loose prose is revised in place.** That is revision, not work status.
17. **The human authors; the agent facilitates.** Intent, scope, and decisions stay with the person.
18. **Read `me.md` before acting,** then the role it names. Blank means full facilitation.
19. **A declared term is the word.** A near-miss is flagged, never swapped silently.
20. **A region is a tool's, by name.** Inside is the tool's; outside is the person's.
21. **Everything at the root is declared.** Every folder and every file has an entry, and nothing is declared that isn't there.
22. **A folder is its owner's.** The standard's rules reach `@eidos/collections` and no further; a tool's folder is that tool's, and an unowned one is the person's.

## Versioning

Semantic Versioning. This file's version moves only when its text moves; a framework records the version it targets as `eidos_version`. Each release is frozen in `versions/` and the worked hops are in `versions/MIGRATIONS.md`. Tools ship their own version and may reject an unsupported standard.

## For an agent

- **Use the CLI when you have a shell.** Run `eidos instructions`. Without one, the Eidos skills stand in.
- **Find the root by `.eidos/`,** never by name. Read that framework; never assume a folder, section, or property name. Check `eidos_version` once per session; a gap is one line and an offer, never a block.
- **Read `me.md` first,** then the role file. Speak the root's declared terms.
- **Leave plugins, regions, and owned folders to their owners.** Carry them across as found; fault only an opener with no closer.
- **Navigate by the framework document,** not the tree: `top_level`, `folders`, `index`. Check the root against it and surface what is missing on either side; never invent a description, never delete a file.
- **Authoring:** take the Properties table, Vocabulary, naming, and the collection's variants; generate frontmatter from the required properties; follow the template's sections, pressing hardest on non-goals; where the owner is vague, ask.
- **Validating:** frontmatter against every block of the Properties table; body against the blueprint's variant; a group's `default_variant` the collection does not declare surfaced like an unknown variant; a blueprint without `variant` and no default in its group or collection surfaced as a gap; links resolve; no work-tracking fields; near-misses flagged. Surface, don't block.
- **Facilitate, don't author.** Never invent a blueprint's purpose or hand back a finished one to rubber-stamp.
