# Eidos

**Version:** 5.13.1

Eidos is a way to define a product in markdown: an app, a book, a study, anything work produces that has a shape. The structure is data in a hidden folder that a tool can check against; the product is written in markdown against that structure. One file is the complete source of truth for one unit of the product, as true of something planned as of something long shipped.

This file is the contract: the terms, the layout, and the rules. It names no collection, template, or section; those belong to a framework.

## Terms

| Term              | What it is                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **product**       | What you are defining.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **framework**     | How the files are organized: folders, templates, properties, vocabulary, roles. Lives in `.eidos/`; one framework can govern many products.                                                                                                                                                                                                                                                                                                           |
| **project**       | The folder it all lives in. Found by the `.eidos/` inside it, never by its name. Called a root before 5.7.0.                                                                                                                                                                                                                                                                                                                                          |
| **folder**        | A folder of the project. At the top, a folder is declared under `folders` with what owns it: `@eidos/collections` for the standard, `@<tool>/<kind>` for a tool, nobody for the person's own. Inside a collection, a folder sorts its blueprints, holds blueprints and folders of its own to any depth, and may be declared under the collection's `folders` to give it a description or a default variant. The collection may call its folders by a label of its own (Areas, Domains, Formats). Called a category from 5.9.0 to 5.11.0, and a group before. |
| **collection**    | A folder owned by `@eidos/collections`, holding blueprints of one kind: specs, chapters, investigations. Its folders, if any, sort its blueprints, nested to any depth.                                                                                                                                                                                                                                                                                        |
| **blueprint**     | One markdown file in a collection, defining one unit of the product completely: properties on top, a body below.                                                                                                                                                                                                                                                                                                                                      |
| **unit**          | What one blueprint defines: a spec, a chapter, an investigation. Templates are named for it, singular.                                                                                                                                                                                                                                                                                                                                                |
| **template**      | The body a collection's blueprints follow: sections in order, under set names. Body only. One file per variant in `.eidos/templates/`.                                                                                                                                                                                                                                                                                                                |
| **variant**       | One of a collection's templates (`<unit>.<variant>.md`). The collection, or a folder in it, may name a default; a blueprint on another says so in `variant`.                                                                                                                                                                                                                                                                                        |
| **property**      | One frontmatter field: name, type, which collections (or the top-level docs) it applies to, whether required, meaning, and options when closed. The whole table is the framework's Properties.                                                                                                                                                                                                                                                        |
| **vocabulary**    | The framework's table of words used on purpose: what each means and what it is not.                                                                                                                                                                                                                                                                                                                                                                   |
| **top-level doc** | A one-of-a-kind file at the top of the project, listed in the framework document. No template; the body is never validated. It may open with properties, checked as a blueprint's are.                                                                                                                                                                                                                                                                |
| **Core**          | The part of the project that defines the product: the top-level docs, the blueprints in the collections, and the records a tool keeps for the product (decisions, for example). A blueprint is one piece of it. The standard checks the top-level docs and the collections; a record is documentation in the Core while its folder stays its tool's. A draft is not in it until published. The framework is the shape the Core takes, not part of it. |
| **role**          | How an agent talks to one kind of person. `.eidos/me.md` says which role is in the seat.                                                                                                                                                                                                                                                                                                                                                              |
| **plugin**        | A tool's own folder, `.eidos/plugins/<name>/`, and any project folder it owns. The standard reads none of it.                                                                                                                                                                                                                                                                                                                                         |
| **region**        | A span in a markdown file that a tool owns, fenced by two HTML comments carrying its name. The standard reads nothing inside it.                                                                                                                                                                                                                                                                                                                             |

A task describes work and dies when it ships. A blueprint describes the product and stays accurate for its whole life.

## Layout

```txt
<Project>/               # the project: any folder, found by its .eidos/
  .eidos/                # the framework
    plugins/<name>/      #   a tool's own folder; local.yaml and local/ inside it stay on this machine (gitignored)
    roles/<role>.md      #   response contracts
    templates/           #   <unit>.<variant>.md, one per variant
    .gitignore           #   ignores me.md, plugins/*/local.yaml, and plugins/*/local/
    Framework.yaml       #   the framework document
    me.md                #   who is in the seat (local, gitignored)
  <Collection>/          # owned by @eidos/collections: blueprints
    <Folder>/            #   a folder of the collection, nested to any depth
      <Title>.md         #     one blueprint per file
    <Title>.md           #   a blueprint may sit beside the folders
  <Folder>/              # owned by a tool (@<tool>/<kind>) or by nobody: declared, never read
  <Doc>.md               # a top-level doc, listed under top_level
```

**Everything at the top of the project is declared.** A folder is `.eidos/` or declared under `folders`; a file is listed under `top_level`. Anything else is surfaced, and the owner declares it or moves it. Hidden entries (`.git`, `.obsidian/`) are the host's and exempt.

### Folders

| Owner                | Holds                                         | The standard                                                                    |
| -------------------- | --------------------------------------------- | ------------------------------------------------------------------------------- |
| `@eidos/collections` | blueprints, optionally in folders to any depth | generates, validates, and indexes the markdown files; ignores any other file    |
| `@<tool>/<kind>`     | whatever that tool says                       | reads nothing inside; the folder is declared and left to its tool, known or not |
| none                 | whatever the description says                 | reads nothing inside; the folder is declared and otherwise left alone           |

An owner is `@<tool>/<kind>`, quoted in YAML: the tool's one identifier, then the tool's own name for what the folder holds, in the same characters. The standard owns `@eidos/collections` and defines nothing else under `@eidos/`. A tool registers as many kinds as it needs, and what a folder under one holds, how it is named, and what is checked inside are that tool's to say. A check faults an owner that is malformed or an `@eidos/` kind the standard does not name, and never a tool's.

A collection's folders nest to any depth, and a folder holds blueprints, folders, or both. A collection may declare its folders under its own `folders`, each entry the shape of a top-level folder's (`name`, `title`, `description`) and `default_variant`, with `folders` of its own beneath it; its `label` is the collection's own word for them (Areas, Domains, Parts). A folder's place is its path from the collection, such as `health/fitness`; a folder property's value is that path, and a value that is not the folder the file sits in warns. A folder's `default_variant` holds for everything beneath it until a deeper folder names its own. Two settings make a collection stricter, both on when absent: `loose_files: false` keeps every blueprint in a folder that holds no folders, and `undeclared_folders: false` makes every folder be declared.

A collection that still carries the older `grouping` block (`label`, `property`, `groups`, from before 5.12.0) is read as the same collection with `label`, `folder_property`, one level of `folders`, and both settings off, so it is checked as before. A collection carries `grouping` or the new keys, never both.

### Plugins

The top level of `.eidos/` is the standard's. A tool keeps what it needs in `.eidos/plugins/<name>/` and touches nothing else. The name is one identifier everywhere the tool appears (its folder, its Properties block, its regions, the project folders it owns): lowercase letters, digits, hyphens, unique in the project; `eidos` is reserved. A check never faults a plugin folder and a migration carries it across untouched. A tool's `local.yaml` is one person's settings and its `local/` folder one person's files, neither ever committed; nothing else in the folder is local.

### `Framework.yaml`

One per project, `Framework.yaml` or `.yml`, snake_case, comments welcome. Every path is relative to `.eidos/`.

```yaml
eidos_version: 5.13.1
naming: kebab-case            # kebab-case (default) | TitleCase | Title Case
top_level:
  - { title: <Title>, path: ../<Doc>.md, description: one line }
folders:
  - name: <Collection>
    title: <The name people read>   # optional, as on a collection's folder and a variant
    owned_by: "@eidos/collections"
    description: one line
    variants:
      - { name: <variant>, template: templates/<unit>.<variant>.md, description: one line, default: true }
    label: <Label>              # optional: the collection's own word for its folders
    folder_property: <name>     # optional: the custom property carrying the folder's path, if one does
    loose_files: true           # optional, default true: blueprints may sit beside folders, at any level
    undeclared_folders: true    # optional, default true: a folder on disk is a folder without being declared
    folders:                    # optional: the folders the collection declares
      - name: <Folder>
        description: one line
        default_variant: <variant>   # optional: the default for everything beneath it
        folders:
          - { name: <Folder>, description: one line }
  - { name: <Folder>, owned_by: "@<tool>/<kind>", description: one line }
  - { name: <Folder>, description: one line }
properties:
  core: []                    # the standard's; empty = the standard properties for this eidos_version
  custom:
    - { name: <name>, type: Text, applies_to: all, required: true, meaning: one line }
    - { name: <name>, type: Text, applies_to: [<Collection>], options: [<Value>, <Value>], meaning: one line }
    - { name: <name>, type: Text, applies_to: [top_level], meaning: one line }   # the top-level docs
  tools:
    <tool>:
      - { name: <name>, type: Text, applies_to: all, meaning: one line }
vocabulary:
  - { term: <Term>, means: one line, not: ["<near-miss>, and why"], see: ../<Collection>/<Title>.md }
index:                        # generated; never hand-edited
  <Collection>:
    - { id: <id>, title: <Title>, summary: <summary>, path: <Folder>/<Folder>/<Title>.md, folder: <Folder>/<Folder> }
```

- **`top_level`**: every file at the top of the project, each a `title`, `path`, and `description`.
- **`folders`**: every folder at the top of the project, each a `name` and `description`, and `owned_by` when something owns it. A folder, a collection's folder, and a variant may carry `title`, the name people read; absent, tools show `name`. `name` remains the path and the key everything refers to, and a tool never matches a path or a folder property's value against `title`. A `@eidos/collections` folder may carry `variants`, its templates, and may declare none (`default: true` marks the collection's default; with none marked, it has none), and may carry `label`, `folder_property`, `loose_files`, `undeclared_folders`, and `folders`, the folders it declares, each with `folders` of its own. A collection's folder may name a default with `default_variant`, one of the collection's variants. A malformed owner, or an `@eidos/` kind the standard does not name, is a fault; a tool's owner never is.
- **`properties`**: one block per owner. `core` holds the standard properties, rewritten by a migration. `custom` is the owner's. `tools.<tool>` is that tool's alone. The six keys the standard names are the standard's; any other key on an entry is a tool's.
- **`vocabulary`**: the project's own terms. Starts empty.
- **`index`**: every collection's blueprints, rebuilt wholesale by whatever indexes the project, which touches no other key.

### Templates

A template is body only: sections in order, under set names, with guidance. Frontmatter in a template is a fault. The file is `<unit>.<variant>.md`, lowercase. A blueprint is validated against the variant it names; a lighter variant is never faulted for sections only a fuller one has.

### Properties

Each entry: `name`, `type`, `applies_to`, `required`, `meaning`, and `options` when the value is one of a closed set.

- **type** is one of Text, List, Number, Checkbox, Date, Date & time, Object, matched in any case; any other is a fault. An Object is a mapping whose values are scalars, lists, or further mappings. The standard declares no keys inside it: what they mean is the owner's, or the tool's that writes them.
- **applies_to** is `all` or a list of collections, where `top_level` names the top-level docs. `all` is every collection; a property reaches the top-level docs only when its list names `top_level`, and `top_level` is never a collection's name.
- **required** (absent = `false`): a required property is generated into every new blueprint and surfaced when missing. An optional one is written when it has a value; its absence is never a gap. An Object holding no key (absent, null, or `{}`) is empty.
- **options**: an ordered, non-empty list of allowed values, compared exactly. An off-list value is surfaced, never refused. An empty list is a fault, as is `options` on an Object. No default rides with it. `variant` and a folder property take their sets from the structure and never carry `options`.

The block a property sits in owns it, and only the owner writes there. The standard properties, in `core`:

| Name      | Type | Required | Meaning                                                                                       |
| --------- | ---- | -------- | --------------------------------------------------------------------------------------------- |
| `id`      | Text | yes      | Stable, unique identity, in any form. Assigned once, never changed.                           |
| `title`   | Text | yes      | Human-readable name. Rename freely; `id` holds still.                                         |
| `summary` | Text | no       | One line: what this blueprint is. Feeds the index; absent, the index flags it.                |
| `variant` | Text | no       | Which variant this blueprint follows. Absent = the nearest default on its folder's path, else the collection's. |

A tool that scaffolds a blueprint writes the variant it resolved; with no default on its folder's path or the collection, it writes none unless the person picks one. A blueprint without `variant` and no default follows no template, and conforms: a template is offered, never owed, and whether a project insists on one is a tool's rule. Moving a blueprint to another folder never changes its `variant`.

**A top-level doc may carry properties too.** Its frontmatter holds the properties whose `applies_to` names `top_level`, and `id`, unique across the project like a blueprint's, so a link, a comment, or a tool can point at the doc by it. A doc's `title` and its one line stay under `top_level`, so it carries no `title`, `summary`, or `variant`. A doc with no frontmatter conforms, and so does one without `id`; a required property that applies to `top_level` is surfaced where a doc lacks it, as on a blueprint.

Eidos defines no custom properties. Status, dates, labels, dependencies: all the framework's choice.

### Vocabulary

Each entry: `term`, `means`, `not` (the near-misses and why each differs), and `see` when a blueprint defines it in full. Eidos declares none of a project's terms. Where a term is declared, blueprints use it; a near-miss is flagged with the term beside it, never swapped in silently.

### Roles

`.eidos/roles/<role>.md` says how an agent responds to one kind of person: depth, what to surface, who decides. The people who own the product hold intent, scope, and decisions. `.eidos/me.md` names your role and calibrates it on ownership, experience with the scope, and technical capacity. Blank is fine.

## Writing

### Naming

Everything a human reads in the tree follows `naming`. Absent means `kebab-case`.

| Convention               | A blueprint file          | A folder          | Trade                                 |
| ------------------------ | ------------------------- | ----------------- | ------------------------------------- |
| **kebab-case** (default) | `blueprint-title-here.md` | `folder-name/`    | readable everywhere, no `%20`         |
| **TitleCase**            | `BlueprintTitleHere.md`   | `FolderName/`     | space-free, capitalized               |
| **Title Case** (deprecated) | `Blueprint Title Here.md` | `Folder Name/`    | reads like prose, `%20` in every link |

Title Case stays valid in a project that has it, and a tool should not create a new one: spaces in a path need quoting in every script.

Exceptions: `.eidos/` is lowercase, `README.md` keeps its name, a folder property's value matches the folder's path exactly, a folder a tool owns is named as the tool says, and nothing inside a folder the standard does not own is held to the convention.

### Linking

A standard markdown link, path relative to the file it sits in, text the human title, `#heading` for a section. Properties that point outward hold links too, quoted in YAML. Files that are not blueprints are linked or embedded the same way (`![Login flow](../assets/login-flow.png)`): no wikilinks, no absolute paths, no resolution by filename. A check verifies the path resolves. If a target has no blueprint yet, name it plainly.

### Bodies

A blueprint's body follows its variant's template, when it has one: keep the order and names, leave out a section that doesn't apply rather than leaving it empty, and write it like a person would read it. A blueprint with no template is its author's own sections. A top-level doc is loose prose, revised in place, with no template.

### Regions

A tool keeps what it needs inside a markdown file between `<!-- <tool>:<region> <args> -->` and `<!-- /<tool>:<region> -->`, each alone on its line. `<args>` is optional `key=value` pairs. Inside is the tool's, rewritten wholesale; outside is the person's. A region closes at the first matching closer (`-->` or `--!>`); a marker inside a fenced code block is text. An opener with no closer is faulted; a region for an unknown tool never is. Frontmatter holds no regions.

## The index

The one derived view the standard defines. Every collection's blueprints, under `index`: `id`, `title`, `summary` (null when absent, never invented), `path` relative to the collection, and `folder`, the folder's path from the collection (`health/fitness`), null at the top. In file order, folder by folder, depth first. An index written before 5.12.0 says `group` where this says `folder`, and is rewritten by the next build. Any other view is a tool's, written as a top-level doc.

## Rules

1. **The frontmatter is the agreement; the body is guidance.** Properties are checked. Sections are recommended.
2. **The project owns its framework.** A tool reads the framework from the project it is in, never from a copy of its own.
3. **Validation is framework-defined.** A check enforces that framework's Properties table, nothing hardcoded.
4. **Surface, never refuse.** A missing required property is added with a note; a missing section is offered. Never refuse the file.
5. **Write it like a human would read it.** If it reads like filled-in boilerplate, reshape it.
6. **Reference blueprints with links, not bare names,** in prose and properties alike. `id` sits behind the link.
7. **One template family per collection, as variants.** What flexes is which sections appear; never their order or names.
8. **Every property has a type, a meaning, and an owner.** Frontmatter is generated from the required ones, so a new blueprint is born conforming.
9. **Soft labels are views, not structure.** A label property drives filtering, never structure. `variant` carries the structural choice.
10. **A collection's folders are its own.** A collection's folders nest to any depth. With `loose_files: false`, a blueprint sits only in a folder that holds no folders of its own, and one elsewhere is surfaced. With `undeclared_folders: false`, every folder is declared under the collection's `folders`, and one that is not is surfaced. A declared folder with no folder on disk is surfaced. A folder property's value is checked against the folder the file sits in.
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
21. **Everything at the top of the project is declared.** Every folder and every file has an entry, and nothing is declared that isn't there.
22. **A folder is its owner's.** The standard's rules reach `@eidos/collections` and no further; a tool's folder is that tool's, and an unowned one is the person's.

## Versioning

Semantic Versioning. This file's version moves only when its text moves; a framework records the version it targets as `eidos_version`. Each release is frozen in `versions/` and the worked hops are in `versions/MIGRATIONS.md`. Tools ship their own version and may reject an unsupported standard.

## For an agent

- **Use the CLI when you have a shell.** Run `eidos instructions`. Without one, the Eidos skills stand in.
- **Find the project by `.eidos/`,** never by name. Read that framework; never assume a folder, section, or property name. Check `eidos_version` once per session; a gap is one line and an offer, never a block.
- **Read `me.md` first,** then the role file. Speak the project's declared terms.
- **Leave plugins, regions, and owned folders to their owners.** Carry them across as found; fault only an opener with no closer.
- **Navigate by the framework document,** not the tree: `top_level`, `folders`, `index`. Check the project against it and surface what is missing on either side; never invent a description, never delete a file.
- **Authoring:** take the Properties table, Vocabulary, naming, and the collection's variants; generate frontmatter from the required properties; follow the template's sections, pressing hardest on non-goals; where the owner is vague, ask.
- **Validating:** frontmatter, a blueprint's and a top-level doc's, against every block of the Properties table, each value against its type and a type outside the list faulted; body against the blueprint's variant, where it has one; a folder's `default_variant` the collection does not declare surfaced like an unknown variant; a blueprint without `variant` and no default on its folder's path or in its collection valid, its body checked against nothing; links resolve; no work-tracking fields; near-misses flagged. Surface, don't block.
- **Facilitate, don't author.** Never invent a blueprint's purpose or hand back a finished one to rubber-stamp.
