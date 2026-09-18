# Eidos

**Version:** 5.2.1

A system of organization for defining a product: an app, a book, a study, a workflow, anything work produces that has a shape. The structure is data, in a hidden folder, that a tool can check a root against; the product is written in markdown against that structure. One file is the complete source of truth for one unit of it, independent of time or status: as true of something planned as of something long finished.

This file is the contract: the terms, the layout, and the rules. It names no collection, no template, and no section — those belong to a framework, not to the standard.

## Vocabulary

Every term the standard uses, in the order they build on each other.

| Term              | What it is                                                                                                                                                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **product**       | What you are defining: an app, a book, a study, a workflow, anything work produces that has a shape.                                                                                                                                                    |
| **framework**     | How the files are organized: the collections, templates, variants, properties, vocabulary, and roles a product is written in. Lives in `.eidos/`, and the same framework can govern any number of products.                                             |
| **root**          | The folder it all lives in: `.eidos/` and the files written with it. Found by the `.eidos/` inside it, never by its name.                                                                                                                               |
| **collection**    | A top-level folder in the root holding files of one kind: specs, chapters, investigations. A framework declares each one, and may group its files in one level of sub-folders.                                                                          |
| **blueprint**     | One markdown file in a collection, defining one thing completely: properties at the top, a body below.                                                                                                                                                  |
| **unit**          | What one blueprint defines: one piece of the product, of the kind its collection holds: a spec, a chapter, an investigation. A collection's templates are named for its unit, in the singular.                                                          |
| **template**      | The body a collection's blueprints follow: sections in order, under set names, each with a note on what goes there. Body only; frontmatter is illegal in a template. One file each, in `.eidos/templates/`.                                             |
| **variant**       | A collection can have more than one template, and each is a variant (`<unit>.<variant>.md`). One is the default; a blueprint on another says so in its `variant` property.                                                                              |
| **property**      | One field in a blueprint's frontmatter: a name, a type, which collections it applies to, whether it is required, what it means, and, when its value is one of a closed set, the options. The framework's whole table of them, in `Framework.yaml`, is its Properties: the standard's four, plus what the owner and any tool add. |
| **vocabulary**    | The framework's table of words used on purpose: what each means, and what it is not.                                                                                                                                                                    |
| **top-level doc** | A one-of-a-kind file at the root: a Vision, a map a tool generates. No template, no validation.                                                                                                                                                         |
| **role**          | How an agent talks to one kind of person. `.eidos/me.md` says which role is in the seat.                                                                                                                                                                |
| **plugin**        | A tool's own folder inside the framework, `.eidos/plugins/<name>/`, holding whatever that tool keeps there. The standard reads none of it. One file in it, `local.yaml`, is one person's on one machine and is never committed.                         |
| **region**        | A span inside a markdown file that a tool owns, fenced by two HTML comments carrying the tool's name. What is between them is the tool's; everything outside is the person's. The standard reads none of it.                                          |

A blueprint captures a vision of the product as a source of truth. A task describes work and dies when the work ships; a blueprint describes the product and stays accurate across its whole life — drafted, built, deprecated.

## Layout

The root is found by the hidden `.eidos/` inside it. It may be named anything; nothing points at it by path.

```txt
Blueprints/              # the root — `Blueprints` is only the default name
  README.md              # the visible "start here": optional, and every seed ships one
  .eidos/                # the framework (below)
  <Collection>/          # a collection of blueprints; declare as many as the work needs
    <Group>/             #   one level of sub-folders, at most
      <Title>.md         #     one blueprint per file
  <Doc>.md               # a top-level doc — optional, yours
```

## The framework (`.eidos/`)

Hidden the way `.git` and `.obsidian` are: present, manageable, out of the way once set. Open the way `.obsidian/` is, too: the standard names its own entries, and a tool that keeps something in the framework gets a folder of its own under `plugins/`. A folder with no `.eidos/` is not a root.

```txt
.eidos/
  templates/               # one file per variant
    <unit>.<variant-1>.md   #   a collection's default variant
    <unit>.<variant-2>.md   #   a second variant of the same unit
  roles/                   # response contracts, committed and team-tunable
    framework-owner.md     #   the role that holds intent, scope, and decisions
    <role>.md              #   the rest are the framework's own
  Framework.yaml           # the framework document: version, naming, top-level docs, collections, properties, vocabulary, and the index
  plugins/                 # whatever tools keep in the framework, one folder each
    <name>/                #   a tool's own; the standard reads none of it
      local.yaml           #     the tool's personal settings, one machine's (gitignored)
  me.md                    # who is in the seat (personal, gitignored)
  .gitignore               # ignores me.md and plugins/*/local.yaml
```

### Plugins

The top level of `.eidos/` is the standard's: the entries above, and whatever a later version adds. Everything else lives under `.eidos/plugins/`, one folder per tool, named for the tool: a CLI's cache, an editor extension's settings, a generator's templates, a script's state. What goes inside is the tool's own, and the standard neither reads nor validates it; a check never faults a folder there, a migration carries it across untouched, and a fresh root starts with none. A plugin folder is committed with the rest of the framework, with one exception. A tool's folder may hold `local.yaml`: the settings that belong to one person on one machine (a viewer command, an editor, a key path). It is never committed. Everything else in the folder is the root's and travels with it. The root's `.eidos/.gitignore` carries the pattern `plugins/*/local.yaml` beside `me.md`, so one line covers every tool and no tool writes a `.gitignore` of its own. The standard reads neither file, as it reads nothing in a tool's folder; what is a root setting and what is a personal one is the tool's to declare, and the standard fixes only the name of the personal file and that it is not committed.

A tool touches only the folder it owns. The framework document, the templates, and the roles are the owner's, edited by hand or through a tool the owner runs; a plugin that needs the framework to know something declares it in its own folder, not in theirs. The same holds inside the files: a tool that needs to keep something in a blueprint or a top-level doc writes it in a [region](#regions) under its own name, and touches no other tool's.

### `Framework.yaml`

The framework document: the one file describing the structure rather than any single blueprint, exactly one per root. It is data, `Framework.yaml` (or `.yml`), in snake_case, with comments wherever the owner wants them: the version and naming convention, the top-level docs, the collections, the Properties table, the Vocabulary, and the generated index, so a root is one document with everything in it. Scripts and agents parse it without a markdown convention, a person reads it the way they read any config file, and tools edit it in place.

```yaml
eidos_version: 5.2.1
naming: kebab-case            # absent = kebab-case
top_level:                    # the top-level docs
  - title: README
    path: ../README.md
    description: the front door.
collections:                  # one entry per collection
  - name: <Collection>
    description: One line on what this collection holds.
    variants:
      - { name: <variant-1>, template: templates/<unit>.<variant-1>.md, description: the fuller template, default: true }
      - { name: <variant-2>, template: templates/<unit>.<variant-2>.md, description: a lighter one to grow out of }
    grouping:
      label: <Grouping>
      property: <name>          # the custom property carrying the group, if one does
      groups:
        - { name: <Group>, description: one line on what falls under it }
properties:
  core: []                    # absent = the standard's core for this eidos_version
  custom:
    - { name: <name>, type: Text, applies_to: all, required: true, meaning: Every blueprint carries this. }
    - { name: <name>, type: Text, applies_to: all, meaning: Whatever this framework needs; absent = not required. }
    - { name: <name>, type: Text, applies_to: all, options: [<Value>, <Value>], meaning: One of a closed set; a value off the list is surfaced. }
    - { name: <name>, type: Text, applies_to: [<Collection>], meaning: Scoped to one collection., <tool>: { <field>: <value> } }
  tools:                      # one block per tool that declares properties of its own; absent = none
    <tool>:
      - { name: <name>, type: Text, applies_to: all, meaning: A property the tool keeps itself. }
vocabulary:                   # the root's own terms; absent = none declared
  - { term: <Term>, means: One line on what the word denotes here., not: ["<near-miss>, and why it is a different thing"] }
  - { term: <Term>, means: A term its blueprint defines in full., not: [<near-miss>], see: ../<Collection>/<Group>/<Title>.md }
index:                        # generated, regenerated wholesale; never hand-edited
  <Collection>:
    - { id: <id>, title: <Title>, summary: <the summary>, path: <Group>/<Title>.md, group: <Group> }
```

- **`eidos_version`**: the version this framework targets. A migration reads and bumps it.
- **`naming`**: `kebab-case` (default), `TitleCase`, or `Title Case`. See [Naming](#naming).
- **`top_level`**: the top-level docs, each a `title`, a `path`, and a `description`. A `README.md`, when the root has one, is listed here like any other.
- **`collections`**: one entry each: its `name`, its `description`, its `variants` (`default` marks the default; absent on all of them, the first is), and its `grouping` (a `label`, the custom `property` carrying the group if one does, and its `groups`).
- **`properties`**: one block per owner. `core` is the standard's, rewritten by a migration (empty means the standard's core for this `eidos_version`); `custom` is the framework's, edited by the owner; `tools.<tool>` is one block per tool that declares properties of its own, that tool's and written by nobody else. `applies_to` is `all` or a list of collections; `required` is `true` or `false`, absent meaning `false`; `options`, when present, is the closed set of values. The six keys the standard names are the standard's; any other key on an entry is a tool's, named for the tool.
- **`vocabulary`**: the root's own terms, one entry each: `term`, `means`, and `not` as a list, each item free to carry its clause, and `see` for the path to the blueprint that defines the term in full. Starts empty; absent means none declared.
- **`index`**: every collection's blueprints, generated (see [The index](#the-index)). Rebuilt wholesale by whatever indexes the root, which rewrites this key and nothing else; never hand-edited.
- Every path is relative to `.eidos/`; an index entry's `path` is relative to its collection folder.

### Templates and variants

A template is body-only: sections in their order, under set names, with their guidance, and nothing else. Frontmatter is illegal in a template: a blueprint's frontmatter is generated from the Properties table, never copied from a template, so a template that opens with a frontmatter block is faulted rather than read. What a template has to say about itself it says in its sections; how templates work is this standard's to say, not each template's to repeat. Every blueprint in a collection follows one of that collection's declared variants, and a check validates against the variant the blueprint names. A template file is named `<unit>.<variant>.md`, lowercase and dotted: the collection's unit, then the variant. Every variant a collection declares shares its unit, and a template file named any other way is faulted the way frontmatter in one is. Top-level docs have no template.

The default variant is what gets scaffolded; a blueprint on another records it in `variant`. A blueprint on a lighter variant is never faulted for the sections only a fuller one carries.

### Properties

Each property is an entry with five fields: `name`, `type`, `applies_to`, `required`, `meaning`, and a sixth, `options`, when its value is one of a closed set. A type comes from the set Obsidian uses — **Text, List, Number, Checkbox, Date, Date & time** — so frontmatter renders natively in a vault. Anything wanting more structure than one of those belongs in the body.

**Applies To** scopes a property to collections: `all`, or a list. Frontmatter is generated per blueprint from the required properties that apply to its collection, so a scoped property never lands where it makes no sense.

**Required** says whether a blueprint the property applies to must carry it: `true` or `false`, and an absent key means `false`. A required property is generated into every new blueprint it applies to, and a check surfaces one that is missing. An optional property is written when it has a value and otherwise left out; a blueprint without it is complete, a check says nothing about its absence, and a value present is still checked against its type. Declaring a property is not the same as putting it on every file: the table can hold a dozen fields a framework may use while only the few it insists on land on every blueprint.

**Options** closes a property's value to a declared set: a non-empty list of values, on a Text property or a List one. A Text value is one of them; every element of a List value is. The list is ordered: the values run in the order the owner declared them, so a lifecycle reads first stage to last, and a tool that lays them out (a dropdown, a board's columns, a sort) keeps that order rather than inventing one. The comparison is exact, case included: the owner wrote the list once, and a check has no reason to guess. A value off the list is surfaced with the list beside it, never refused and never swapped in silently. An entry without the key is bounded by its type alone, which is what a Text property has always been, so nothing existing changes meaning; an entry whose list is empty is a fault in the framework document, since an open set is what the absent key already says. `options` carries the values and `meaning` says what they are for; a `meaning` that lists values in prose is describing a set the entry should declare. Options never carry a default: a required property with them is generated blank like any other and the owner picks, and an optional one is absent until it has a value. Two properties take their set from the structure instead and never carry `options`: `variant`, whose values are the collection's declared variants and whose absence means the collection's default, and a collection's grouping property, whose values are its declared groups. `options` is the one refinement of a type the standard makes; a pattern, a range, or a check that a link resolves is a tool's, under its own key.

**Every property has an owner, and the owner is the block it sits in.** Eidos is the first tool: `properties.core` is its block, and a migration rewrites it. `properties.custom` is the framework owner's, and the owner edits it. A tool that needs properties of its own (the `eidos` CLI, an editor extension, a generator) declares them in a block of its own, `properties.tools.<tool>`, and that tool alone writes it: not the owner, not a migration, not another tool. A tool's properties are Properties properties like any other, generated into frontmatter where they apply, validated by a check, and bound by every rule here including the one against work-tracking; an unknown tool's block is never faulted. When a tool leaves, its block leaves with it, the values it held surfaced first the way any retired property's are.

**A row may also carry a tool's fields.** The six the standard names come first and mean what they mean here. Past them, a tool that needs something per property it does *not* own (how an editor renders `status`, a color per option, what a stricter checker allows) adds its own under its own name: a key named for the tool on the property's entry. The standard reads its six and ignores the rest; a check never faults them, and an edit or a migration carries them across unchanged and never fills them in.

**The core** — the whole of what the standard declares, two of them required:

| Name      | Type | Required | Meaning                                                                                                                          |
| --------- | ---- | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `id`      | Text | yes      | Stable, unique identity, in any form: a slug, a number, a GUID. Assigned once, never changed. References point at it.            |
| `title`   | Text | yes      | Human-readable name. Rename it freely; `id` is what holds still.                                                                 |
| `summary` | Text | no       | One plain line: what this blueprint is. The source for the collection's [index](#the-index) listing; absent, the index flags it. |
| `variant` | Text | no       | Which variant this blueprint follows. Absent = the collection's default.                                                         |

**Eidos defines no custom properties.** A lifecycle `status`, dates, a grouping, a dependency list, a relationship list — all are a framework's own choice, and how blueprints relate is better said in the body, as links in prose, than as a frontmatter field. Adding one means deciding all five of Name, Type, Applies To, Required, and Meaning, and Options where the value is one of a set, then backfilling the blueprints it applies to when it is required.

### Vocabulary

The Properties table's sibling: where that table is the contract for properties, the Vocabulary is the contract for words. Each term is an entry: `term`, `means`, `not`, and `see` when a blueprint defines the concept in full. **term** is the word as prose uses it. **means** is one line. **not** is the near-misses, each with a clause on why it is a different thing, and it is where an entry earns its place: a term with nothing there is a dictionary entry, and a term that needs a body of its own is a blueprint, pointed at from its entry.

Three layers of words meet in a root, and each is declared where it lives. The standard's terms are the table at the top of this file. A framework's structural names (its collections, variants, groups) are declared where the structure is. The root's own terms, the words the product itself is described in, are the framework's Vocabulary. **Eidos declares none of the last.** A Vocabulary starts empty and grows an entry when a word begins to carry a distinction worth keeping, each entry deciding all three of term, means, and not.

A declared term is the word (Rule 19). An agent authoring or checking a blueprint uses it, and where a near-miss appears says which term the Vocabulary would have, as a suggestion. This is distinct from what a role sets: a role is register, how deep an agent goes and what it surfaces for one kind of reader; the Vocabulary is meaning, what a word denotes for every reader.

### Roles

Not everyone who works on the same root plays the same part — one holds the intent, another builds or drafts from it, another reviews it, another answers for it. The agent responds to each differently, from two files:

- **`.eidos/roles/<role>.md`** — one response contract per role: vocabulary and technical depth, what to surface versus fold away, and who holds which decisions. Which roles exist is the framework's call. Committed and team-tunable.
- **`.eidos/me.md`** — personal and gitignored, one per person. Names your role and calibrates it on three axes: **ownership**, **experience with the scope**, and **technical capacity**. Blank is fine.

One role every framework has: the **Framework Owner**, who holds the intent, the scope, and the decisions. The rest of the cast depends on the work.

## Writing

### `README.md`

A visible front door at the root: what the product is, and pointers into it — the top-level docs, the collections, and the framework document for the full index. Thin, orientation and links, edited in place. Optional: every seed ships one and lists it first under `top_level`, because a person and an agent both land on it before the framework document, but nothing reads it and nothing requires it. A root without one is whole; its `top_level` simply starts with whatever it has.

### Naming

Everything a human reads in the tree — top-level docs, collection and sub-folders, blueprint files — follows the framework's `naming` convention.

| Convention               | A blueprint file          | A grouping folder | For                                                              |
| ------------------------ | ------------------------- | ----------------- | ---------------------------------------------------------------- |
| **kebab-case** (default) | `blueprint-title-here.md` | `group-name/`     | readable everywhere: no escaping, no `%20`                       |
| **TitleCase**            | `BlueprintTitleHere.md`   | `GroupName/`      | space-free, capitalized                                          |
| **Title Case**           | `Blueprint Title Here.md` | `Group Name/`     | a tree that reads like prose, at the cost of `%20` in every link |

An absent `naming` key means `kebab-case`.

One convention governs the whole folder, and changing it later means renaming files, so it is settled at init. Whichever you pick: `.eidos/` is always lowercase; a `README.md`, if the root has one, keeps the name every tool already looks for; a grouping property's value matches its folder exactly; and fields meant for tools are not names in the tree.

### Linking

Point at another blueprint, doc, or section with a standard markdown link: the text is the human title, the path is the target's filename in the framework's convention (only a Title Case tree carries `%20`). Add a `#heading` anchor for a section. Properties that point outward hold links too, not bare ids — quote them in YAML, since a leading `[` starts a list:

```yaml
depends_on:
  - "[Some Blueprint](../some-group/some-blueprint.md)"
```

If a target has no blueprint yet, name it plainly rather than fabricating a link.

### Blueprint bodies

The body follows its variant's template. Keep the template's order and names; leave a section out when it genuinely doesn't apply rather than leaving it empty. Within and beneath those sections, write it like a person would read it — sub-headings, tables, lists, small diagrams wherever they make the meaning clearer. Keep checkable statements short and observable, labeled the way the template asks, with supporting detail pushed into a table or sub-section they point at.

The sections themselves are documented in the template file, not here.

### Top-level docs

Loose prose: record what is true now, revise when it changes. A top-level doc is one-of-a-kind, filled in once and edited in place, so it needs no shared template and gets none: a template earns its keep by being stamped again, and a document written once doesn't need a cookie-cutter. That is the whole difference from a blueprint, which follows a template, carries the frontmatter contract, and is validated, even in a collection the framework keeps as loose prose.

### Regions

A tool that needs to keep something inside a markdown file (a generated list, a rendered view, its own data) writes it in a **region**: a span fenced by two HTML comments carrying the tool's name. Everything between the two is the tool's, and everything outside is the person's.

```markdown
<!-- eidosmd:backlinks -->
- [Session Management](../identity/session-management.md)
<!-- /eidosmd:backlinks -->
```

The opener is `<!-- <tool>:<region> <args> -->` and the closer `<!-- /<tool>:<region> -->`, each alone on its own line with nothing before or after it. `<region>` is the tool's name for that region, so one tool can own several in a file and tell them apart. `<args>` is optional: `key=value` pairs, space-separated, carrying whatever the tool needs to rebuild the region from the marker alone (`<!-- eidosmd:backlinks depth=2 -->`); the standard reads none of them. Both closers HTML allows, `-->` and `--!>`, end a marker.

**The tool's name is its namespace, and it is one identifier everywhere.** The name a tool puts on its regions is the name of its `plugins/<name>/` folder and its `properties.tools.<name>` block: lowercase letters, digits, and hyphens, unique across the root, so a region, a folder, and a block are read as one tool's without a lookup. `eidos` is the standard's own name; it declares no region, and no tool writes under it. The region name is the tool's to choose, in the same characters.

**The contents are the tool's domain.** Markdown, a table, a fenced block of data, plain text: the standard reads none of it, and a check never faults what is inside. A tool rewrites its regions wholesale, the way the index is rebuilt, so nothing hand-written inside one survives. A renderer that knows the tool may show its own view in place of the region; one that doesn't shows the contents as they are, so a tool that wants a readable fallback writes markdown. What a region holds is still bound by the rules on the body: derived facts, a view, a tool's own state, never the product's intent and never work-tracking.

**Parsing.** A region opens at an opener and closes at the first closer naming the same tool and region; the lines between are not read for markers, so a region cannot hold another of the same name, and another tool's marker inside it is content. A marker inside a fenced code block is text, not a marker, so a parser tracks fences (three or more backticks or tildes, closed by the same) before it reads a line as one. An opener with no closer is faulted, whichever tool it names; a region for a tool the check does not know is otherwise never faulted, a migration carries every region across untouched, and anything but its owner editing the file leaves it as found.

**Where.** In any markdown a person reads in the root: a blueprint body, a top-level doc, `README.md`. A template may carry one, so every blueprint stamped from it is born with it. Frontmatter is not markdown and holds none; a tool's per-blueprint fields go in its Properties block.

## The index

One derived view the standard defines, regenerated wholesale, annotating rather than gating, with nothing hand-written to preserve.

**The index.** Every collection's blueprints, listed in the framework document under `index`, one list per collection, so a human or agent can find a blueprint without scraping the tree. Each entry is the blueprint's `id`, `title`, `summary` (null when absent, never invented), `path` relative to the collection folder, and `group` when it has one; entries are grouped by sub-folder when the collection has them, flat when it doesn't, in file order. Rebuilt by `index`, which rewrites that key and nothing else in the document.

**Any other view is a tool's.** A map, a graph, a report: a tool that draws one reads the index and the links in the bodies, keeps whatever it needs in its own Properties block or its `plugins/` folder, and writes its output as a top-level doc, registered under `top_level` like any other. The standard declares nothing for it.

## Rules

The load-bearing conventions.

1. **The frontmatter is the agreement; the body is guidance.** Properties are checked against the framework's Properties table. Body sections are recommended structure, not requirements.
2. **The root owns its framework.** Templates and properties live in the root's `.eidos/`. A tool reads the framework from the root it is working in, not from a copy of its own. Anything a tool keeps there lives under `.eidos/plugins/<name>/`, and a tool touches only the folder and the regions it owns.
3. **Validation is framework-defined.** A check reads *that framework's* Properties table and enforces it — the core properties plus the custom ones scoped to the blueprint's collection. The contract is the Properties table, not a rule hardcoded in a tool.
4. **Portability over prescription.** A missing required property is surfaced and added with a note on why; an optional one absent is not a gap; a missing section is noted and offered. Never refuse the file.
5. **Write it like a human would read it.** The sections are a scaffold for a living blueprint, not a form to pour text into. If a blueprint reads like filled-in boilerplate, reshape it until it reads like someone wrote it.
6. **Reference other blueprints with links, not bare names** — in prose and in properties alike. Each blueprint's `id` is still its permanent identity, sitting behind the link.
7. **One template family per collection, declared as variants.** What flexes is *which* sections appear and *which* variant a blueprint uses; never their order or names within a variant. The template is never forked per category.
8. **Properties carry a type, a meaning, and an owner.** Every property declares its name, its type, which collections it applies to, whether it is required, and what it means, and one whose value is one of a closed set declares its options; the block it sits in says who owns it (Eidos, the framework, or a tool), and only the owner writes there. Frontmatter is generated from the required properties in the table, so a new blueprint is born conforming and carries nothing it doesn't need.
9. **Soft labels are views, not structure.** A category label a framework adds drives views and filtering, never structure. Without `options` any value is valid; with them, a value off the list is surfaced, never refused. `variant` carries the structural choice.
10. **A collection's grouping is the collection's own.** It may group its blueprints one level deep and may declare a property naming that grouping; the value then matches the folder, and an unknown value warns rather than blocks. The standard never names a grouping for it.
11. **A template names its own stable part.** Every template has a part that holds still and a part that moves, and says which is which. If the stable part changes substantially, ask whether this is a different blueprint.
12. **Non-goals carry the most weight.** Where a template declares a section for what a blueprint deliberately will *not* do, that section is its strongest — it is where scope management actually happens. Still not a hard gate.
13. **A template documents its own conventions.** Section names, their order and meaning, and any labeling a template asks for live in the template file. This standard governs collections, templates, variants, and properties; it never governs a section.
14. **No work-tracking fields.** No `sprint`, `estimate`, or `assignee` — the moment you add them, a blueprint becomes a task and rots. Bridge to a tracker with a link. The same holds in the body: a section describing how you mean to build a product captures intent, never how far along it is.
15. **The Eidos version is a framework fact.** The standard's version lives in the framework document as `eidos_version`, never as a per-blueprint property. Git holds the history, and a tool that snapshots the root keeps its record in its own `plugins/` folder; a framework that wants date properties declares them like any other.
16. **Loose prose is revised in place.** A top-level doc, and any collection a framework marks as loose prose, records what is true now and is expected to change. That is revision, not work status.
17. **The human authors; the agent facilitates.** Intent, scope, and decisions stay with the person. An agent formats, supplements, asks, and holds scope; it does not generate finished blueprints or set direction. A blueprint the owner did not think through is worse than none.
18. **Read `me.md` before acting.** Read `.eidos/me.md` and the matching contract in `.eidos/roles/`, and respond as that role defines. The human-first principle holds for every role; only the mode changes. A blank or absent file defaults to full facilitation.
19. **A declared term is the word.** Where the framework's Vocabulary declares a term, blueprints use it, and a near-miss it names is flagged with the declared term beside it, never refused and never swapped in silently. The standard declares no term of a framework's; a Vocabulary starts empty and grows a row at a time, each saying what the word means and what it is not.
20. **A region is a tool's, by name.** A tool keeps what it needs inside a markdown file between two HTML comments carrying its own name, the same identifier as its `plugins/` folder and its Properties block, and touches no other tool's. Inside is the tool's, rewritten wholesale; outside is the person's. The standard reads none of it, and a check faults only an opener with no closer.

## Versioning

Semantic Versioning: major for breaking changes, minor for backward-compatible additions, patch for clarifications.

This file holds the version of **the standard** — right now, **5.2.1** — and it moves only when the text of this file moves. A framework records the version it targets as `eidos_version` in its framework document; a migration reads and bumps it there. At tag time this file is copied as-is into `versions/` under its full semver name, so any two releases, even non-adjacent, can be diffed to migrate between them. Worked hops are in `versions/MIGRATIONS.md`. Tools may reject an unsupported version.

**Tools that ship this standard version separately.** A CLI, a plugin, a starting framework: each changes far more often than the standard does, so a release of one leaves this file — and every framework's `eidos_version` — untouched. When you need to know what a framework conforms to, read this version; a tool names the standard it carries.

## For an agent

*Operating detail. A human can stop above.*

**If you have a shell, use the CLI.** Check for one first, every session: a host that has none today may have one after its next update. Run `eidos instructions` and follow it; it does the mechanical part deterministically and hands you only what you need. On a host with no shell, the Eidos skills stand in; each says when it applies.

**Find the framework in the root.** Locate the root by its `.eidos/` marker, not its name. Every operation reads that `.eidos/`. If a folder has none, offer to create a root. Check the framework's `eidos_version` against the standard you carry once per session: a gap is worth one line and an offer to migrate, never a block, and the framework in front of you is the operative contract either way. Never fall back to a hardcoded contract, and never assume a collection or section name — read what the framework declares. Leave `.eidos/plugins/` alone unless you are the tool that owns a folder in it; a folder you don't recognize there is not a problem to report.

**Read `me.md` first.** Then the role file it names. Respond as that file defines the role — read it, don't infer from its filename. A framework defines its own cast.

**Speak the root's terms.** The framework's Vocabulary says which word is the word and what it is not. Use the declared term in what you write; where the owner's draft or speech uses a near-miss, say which term the Vocabulary declares and ask, rather than substituting silently. A word the owner keeps using that no row declares is worth naming as a candidate; declaring it is the owner's call.

**Leave regions to their owners.** A span between `<!-- <tool>:<region> <args> -->` and `<!-- /<tool>:<region> -->` is that tool's. Read it if it helps; write in it only if you are that tool; when you edit the file around it, carry it across as found. Never fault its contents. Fault an opener with no closer.

**Navigate by the index.** `README.md` for orientation, when the root has one, then `.eidos/Framework.yaml`: its `top_level` and `collections` for what the root holds, its `index` for every collection's blueprints. Read it instead of scraping the tree; regenerate the index when stale.

**Authoring a blueprint:**

1. From the framework document, take the Properties table, the Vocabulary, the naming convention, and the target collection's variants. Pick a variant (the default unless the owner chooses another) and read its template for the body. Name the file for its title in the convention; put a permanent `id` inside, in whatever form the root uses.
2. Generate frontmatter from the required properties that apply to that collection, and add an optional one only when the owner gives it a value. Fill values from what the owner tells you; where a property declares `options`, the value is one of them; leave a required property blank rather than guessing it.
3. Lead with the template's opening sections and press hardest on its non-goals section. Read those names off the template rather than assuming them, and follow whatever labeling it asks for. Omit a section that doesn't apply; keep the order and names of the ones that do.
4. Where the owner is vague, ask. Don't fill the gap with plausible prose.

**Validating a blueprint:** check frontmatter against the framework's Properties table, every block of it (every required property present, `id` unique, dates as `YYYY-MM-DD`, custom and tool properties scoped to the collection, an optional property checked only when present, a value on a property with `options` one of them, `variant` one of the collection's variants, a grouping value one of its groups). Report missing body sections against *the blueprint's variant template*, flagging an absent non-goals section first, and note anything skipping the labeling that template asks for. Note each near-miss the Vocabulary names, with the declared term beside it. Confirm no work-tracking fields crept in. Leave every region's contents alone, and report an opener with no closer. Surface, don't block — the output is a review a human acts on.

**Facilitate, don't author.** Format and structure what the owner gives you, supplement, ask, and press on scope. Never invent a blueprint's purpose, decide direction, or hand back a finished blueprint to rubber-stamp. When unsure, ask.
