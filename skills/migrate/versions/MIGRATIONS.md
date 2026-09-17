# Migrations

The worked hop for every released version of the standard, newest first. `migrate` reads the one it needs; a reader can skim any of them to see what a release actually cost.

A migration is a **diff between two snapshots**, so these are conveniences, not a required path. To go from 1.0.0 to 4.3.0 you diff `versions/v1.0.0.md` against the target directly and apply the net change — you do not walk the list. Read a hop when you want the shortcuts and the judgment calls someone already worked out.

Each entry says what moves, what stays, and what needs a human decision.

## 4.7.0 → 5.0.0

**The vocabulary release. Five names move on disk and the framework document takes its one form, all mechanically; set `eidos_version: 5.0.0` when they have.** Nothing is dropped and nothing needs a decision unless a template file is misnamed, and the `eidos` CLI's `migrate` makes the whole hop in one run.

- **`_eidos/` → `.eidos/`.** The folder name only; everything inside keeps its place. A root-level `.gitignore` that named `_eidos/me.md` updates to match; the `.gitignore` inside the folder does not change.
- **`Framework.md` → `Framework.yaml`.** The framework document has one form. A root that kept the markdown form writes the same fields as data (`eidos_version`, `naming`, `top_level`, `collections`, `properties`, `vocabulary`, `versions`), builds the index inside it under `index`, and removes `Framework.md` and each collection's `index.md`. The markdown form's prose (section intros, HTML comments) has no field to land in; keep what is worth keeping as comments. A root already on `Framework.yaml` has nothing to do here.
- **`shapes/` → `templates/`**, and every path to one in the framework document. A template file must be `<unit>.<variant>.md` (one unit per collection) and must not open with frontmatter; a check now faults both. **Needs the owner** only if a collection's templates disagree on their unit.
- **`schema:` → `properties:`**, with its blocks `core`, `custom`, and `tools.<tool>`. In a markdown document being converted, the headings first: `## Schema` → `## Properties`, `### Eidos Core` → `### Eidos`, `### Custom Properties` → `### Custom`, `### <tool> Properties` → `### <tool>`.
- **`flavors:` → `variants:`** on every collection, and each entry's `shape:` → `template:`. In a markdown document being converted, `- **Flavors:**` → `- **Variants:**`.
- **`flavor` → `variant`.** The core row in the Properties table, and the property on every blueprint that carries it. A blueprint without one still means the collection's default.
- **Three words leave the standard's table**, `term`, `actor`, and `frame`, and `properties` folds into `property`; nothing on disk carried any of them.
- **`versions:` leaves the framework document.** Most roots have the empty list the seed shipped: delete the key. A root that recorded snapshots moves the entries into the plugin folder of whatever tool tracks them (`.eidos/plugins/<name>/`), and the `blueprints/<version>` tags it made stay in git as they are. **Needs the owner** only to pick where a non-empty list goes.
- **The framing collection leaves the standard.** Rule 19 ("Every framework declares a framing collection") is dropped and Rule 20 renumbers to 19. A root's `Frames` collection is a collection like any other and stays declared exactly as it is; the only change is that a check no longer faults a framework without one.
- **Cosmetic:** seed prose installed into a root (`roles/README.md`) still says shape, flavor, and Schema until refreshed, and a seed template still opens with the old comment. Nothing reads those words.

### Per root

1. **`git mv _eidos .eidos`**, then **`git mv .eidos/shapes .eidos/templates`**.
2. **In the framework document**, rename the keys above and rewrite the `shapes/` paths as `templates/`. Rewrite the core block as `id`, `title`, `summary`, `variant`, and update the version note on it. A root on `Framework.md` does the same in the markdown, then writes `Framework.yaml` from it, builds the `index`, and deletes `Framework.md` and every `index.md`.
3. **On every blueprint**, rename the `flavor` property to `variant`. Values are unchanged.
4. **Look at each template.** One that opens with `---` has frontmatter to remove; one named any other way than `<unit>.<variant>.md` is renamed, and its path in the framework document with it.
5. **Set `eidos_version: 5.0.0`.**

**Nothing else moves.** No body section, no blueprint filename, no collection.

## 4.6.0 → 4.7.0

**Every Schema property has an owner, and the owner is the block it sits in. Set `eidos_version: 4.7.0`; nothing on disk has to move.**

- **`### <tool> Properties` joins `### Eidos Core` and `### Custom Properties`** (`schema.tools.<tool>` in `Framework.yaml`): one block per tool that declares properties of its own, written by that tool alone. Eidos is the first tool and the core block was already its; this generalizes it. `configure` edits the custom block only, `migrate` rewrites the core block only, and a tool's block is never faulted, never filled in, and carried across untouched.
- **A property a tool declared under 4.6.0** sat in `### Custom Properties` with the tool's column filled. It still conforms; whether to move it into the tool's own block is that tool's next release, not this migration. If the owner moves it by hand, the row moves whole, values on blueprints untouched.
- **`connects_to` is no longer a core property.** The core is `id`, `title`, `summary`, `flavor`. Nothing has read `connects_to` since the canvas generator left in 4.5.0, and how blueprints relate belongs in the body as links. **Needs a decision per root that used it.** `migrate` rewrites the core block without it and then surfaces every blueprint carrying a value, and the owner picks one of three: declare `connects_to` in `### Custom Properties` (it is then the framework's own, unchanged on every blueprint); fold each link into the body where the relationship is explained; or drop it, the values shown first. Never dropped silently.
- **`- **Canvas:**` is no longer a declared bullet** on a collection (`canvas` in YAML). Leave it or delete it; nothing reads it, and a tool that draws keeps its own declarations. `configure` stops writing it for new collections.
- **`id` is no longer required to be kebab-case.** Stable and unique, in any form. Every existing id still conforms; a root that wants numbers or GUIDs from here on may use them, and a check no longer reads the format.
- **Rule 8 gains three words** ("and an owner"). Nothing renumbers.

### Per root

1. **Set `eidos_version: 4.7.0`** in the framework document, and update the version note in its `## Schema` block. That is the whole migration.

**Nothing else moves.** No property, no body section, no filename, no collection.

## 4.5.0 → 4.6.0

**What a root defines is a `product`; a framework declares its Vocabulary, the root's own terms, beside its Schema; the root can be snapshotted as a version, on purpose and only when asked; and `_eidos/` is open to tools. Set `eidos_version: 4.6.0` and add the two sections empty; nothing else moves.**

- **`product` is a declared term**, first in the table: what a root defines, of any kind. The standard had said "the thing" everywhere. Prose only; no file, folder, or property carried the word, and a root's own `README.md` template already said `{{Product}}`. Seed prose installed into a root (`_eidos/Framework.md` intros, `_eidos/roles/framework-owner.md`) still says "the thing" in a few places until refreshed; cosmetic, nothing reads those words.

- **`## Vocabulary` joins the framework document** after `## Schema` (a `vocabulary` key in `Framework.yaml`). One row per term: **Term** (the word as prose uses it, or a link to the blueprint that defines the concept in full), **Means** (one line), **Not** (the near-misses, each with why it is a different thing). The Schema is the contract for properties; this is the contract for words. Eidos declares none of a framework's terms, so every seed ships the table empty, and a root without the section loads and simply declares no terms.
- **Two terms join the standard's own table**, `term` and `Vocabulary`, and the `framework` entry lists Vocabulary among what a framework holds. The framework document's one-line description everywhere (`EIDOS.md`, `README.md`, the seeds) now ends "Schema, Vocabulary".
- **Rule 20 is appended, and nothing renumbers.** A declared term is the word: blueprints use it, a near-miss is flagged with the declared term beside it, never refused and never swapped in silently. Rules 1 through 19 are as they were.
- **`## Versions` joins the framework document** after `## Vocabulary` (a `versions` key in `Framework.yaml`): snapshots of the root, taken on purpose, newest first, one row each: **Version** (the root's own number, not the thing's release version), **Commit** (a sha in the repository the root lives in; the snapshot, nothing copied), **Tag** (optional; `blueprints/<version>` when wanted). Rule 15 now says the root's version is a framework fact like the Eidos version, and never a blueprint property. **Unused until selected:** the section arrives empty and stays empty unless a team asks for a fixed point; no skill proposes one and no check faults its absence. A root that already tagged snapshots under another name keeps them; whether to record them as rows is the owner's call, with `configure`, and nothing is migrated automatically.
- **`_eidos/plugins/<name>/` is reserved for tools**, one folder each, named for the tool; the standard reads none of it, and a tool touches only its own. **A Schema row may carry a tool's fields** past the standard's four: a column headed with the tool's name in markdown, a key named for the tool in YAML. Neither needs anything on the way up. A root that already has a tool's folder somewhere else in `_eidos/` may move it under `plugins/` when that tool supports the location; that is the tool's release, not this migration.
- **A Glossary top-level doc stays a top-level doc.** A root that kept one keeps it, unchanged. The entries in it that carry a distinction are candidates for rows, moved one at a time with `configure`, which presses for the Not; nothing is migrated out of prose automatically, and a glossary that is definitions without near-misses may be fine where it is.

### Per root

1. **Set `eidos_version: 4.6.0`** in the framework document, and update the version note in its `## Schema` block.
2. **Add `## Vocabulary` and `## Versions` empty** after `## Schema` in `Framework.md`, in that order: each a heading and its three-column header (`Term | Means | Not`, `Version | Commit | Tag`) and nothing else; the seeds carry an intro paragraph for each worth copying. A YAML root adds nothing, since an absent `vocabulary` or `versions` key means none. `migrate` adds both empty and never fills them.
3. **Optional: declare terms** with `configure`, starting from the collisions the owner already knows about, and, only if a team wants fixed points, **record versions** for the commits already worth naming, the owner supplying the sha and the number for each.

**Nothing else moves.** No property, no body section, no filename, no collection. Anything already under `_eidos/plugins/`, and any extra column a tool has on a Schema row, is carried across as is.

## 4.4.3 → 4.5.0

**The framework document has a second form, `Framework.yaml`, for scripts and agents; a YAML root keeps its index inside it. Set `eidos_version: 4.5.0`; nothing on disk has to move.**

- **`Framework.yaml` (or `.yml`) joins `Framework.md`** as a form of the framework document: the same fields in the snake_case the frontmatter uses, comments allowed, exactly one of the two per root. Markdown is the form for people (it renders in a vault); YAML is the form for a root that scripts and agents read, and the one the `eidos` CLI works in. The field reference is in `EIDOS.md` under "`Framework.yaml`".
- **A YAML root has no `index.md` files.** Its indexes live inside the framework document under `index`, one list per collection (`id`, `title`, `summary`, `path`, `group`), regenerated wholesale by `eidos index`, which rewrites that key and nothing else. A markdown root keeps a per-collection `index.md` exactly as before, rebuilt by the `index` skill's `build-index.py`.
- **The canvas is declared, not shipped.** The standard no longer ships a canvas generator; a collection's `- **Canvas:**` bullet and a blueprint's `connects_to` still say how one would draw. The `canvas` skill left the plugin.
- **"Prefer the skills" is "prefer the tooling".** The `eidos` command carries the mechanical part (`init`, `new`, `check`, `index`, `instructions`); the skills carry the judgment. The Rules are unchanged in number and meaning; Rule 15 says "the framework document" where it said `Framework.md`.

### Per root

1. **Set `eidos_version: 4.5.0`** in the framework document, and update the version note in its `## Schema` block. That is the whole migration.
2. **Optional: move to YAML** to work in the CLI. `eidos convert` writes `Framework.yaml` with the index inside it and removes `Framework.md` and each collection's `index.md`. The markdown form's prose (section intros, HTML comments) has no field to land in and is left behind; keep anything that matters in the root's `README.md`.

**Nothing else moves.** No property, no body section, no filename, no collection.

## 4.4.2 → 4.4.3

**One word: a framework is the *structure*, not the *form*. Set `eidos_version: 4.4.3`; nothing on disk has to move.**

- **`framework` is now "the structure a root is written in".** The concept has not moved an inch: the same collections, shapes, flavors, roles, naming convention, and Schema, in the same hidden `_eidos/`. Only the word for it changed, because "form" and "shape" are near-synonyms in ordinary English and `shape` is a term four rows down the same table. A reader who met "the form everything is written in" had no way to know it did not mean the body templates.
- **"The form layer" is "the structure layer"** wherever the prose names it, including the fingerprints `migrate` reads to identify a source version. The directory it names is still `_eidos/` (v4.1+) or `.eidos/` (v3.0-v4.0).
- **`EIDOS.md`'s opening line drops "structures".** It described the file as "the terms, the structures, and the rules"; with `framework` now claiming the singular, that plural echoed a term it did not mean. It reads "the terms, the layout, and the rules", naming the section it always meant.
- **The Greek keeps its word.** `README.md` still glosses εἶδος as "the form or essence of a thing", and Plato's Form stays capitalized. That line is etymology, not vocabulary.

### Per root

1. **Set `eidos_version: 4.4.3`** in `_eidos/Framework.md`, and update the version note in its `## Schema` block. That is the whole migration.

**Nothing else moves.** No property, no body section, no filename, no collection. There is no seed prose to refresh either, because nothing `install` writes into a root ever carried the word.

## 4.4.1 → 4.4.2

**A clarity pass over the glossary and the Rules. Set `eidos_version: 4.4.2`; nothing on disk has to move.**

- **`root` is now a declared term** — the one folder Eidos lives in, found by its `_eidos/` and never by its name. 4.4.1 retired "definition" and left the concept unnamed, so the standard fell back on "an Eidos folder" in about a hundred places. The word was already doing the work; it is now in the vocabulary, and the prose uses it consistently.
- **`shape` and `flavor` stop defining each other.** A shape is one body template, one file in `_eidos/shapes/`. A collection's shapes are variants of one family, and each variant is a flavor. Neither concept moved; the table just stopped looping.
- **`frame` no longer reads as "expires".** It said "loose, point-in-time", which sits badly beside a standard whose whole claim is that a blueprint is independent of time or status. A frame is what the whole thing is, taken whole rather than unit by unit, revised when that judgment changes. Nothing about how frames work has moved.
- **The Rules go 24 → 19 and renumber.** Five restated a section above them and were dropped, not relaxed: `id` permanence lives in the Schema table, naming in `## Naming`, `Framework.md` and `README.md` in their own sections, the generated index under `## Generated leaves`, and "top-level docs have no shape" in both the vocabulary and `## Frames and top-level docs`. **If you cite Eidos rules by number anywhere, re-check them** — that is the one thing in this release that can go stale.
- **The old Rule 16 named two properties the standard does not define.** It mandated how `date_created` and `date_modified` behave, while the Schema section says Eidos defines no custom properties and that dates are a framework's own choice. It keeps the half that binds (the Eidos version is a framework fact, in `Framework.md`) and leaves dates to whichever framework declares them. **A framework already using those properties changes nothing** — it now simply owns them outright.
- **The canvas is the Blueprint Map.** It draws blueprints and their `connects_to` edges; the framework is the one thing it never draws. `canvas` writes `blueprint-map.canvas` (or `BlueprintMap.canvas` / `Blueprint Map.canvas`) from here on, and only when you don't pass `--out` — so **an existing `framework-map.canvas` keeps its name until you regenerate without one.** If you do let it rename, update its bullet in `## Top-Level`.

### Per root

1. **Set `eidos_version: 4.4.2`** in `_eidos/Framework.md`, and update the version note in its `## Schema` block. That is the whole required migration.
2. **Optionally regenerate the canvas** to take the new name, and fix its `## Top-Level` bullet if you do.
3. **Optionally refresh the seed prose in `_eidos/`,** which still says "Framework Map" where the standard now says "Blueprint Map". Cosmetic: nothing reads those words.

**Nothing else moves.** No property, no body section, no filename, no collection.

## 4.4.0 → 4.4.1

**A vocabulary release. Set `eidos_version: 4.4.1`; nothing on disk has to move.**

Three changes, all in the text of the standard:

- **`item` is now `blueprint`.** The same thing it always was: one markdown file in a collection, defining one unit completely. No property, folder, or filename ever carried the word, so nothing an agent or a script reads changes.
- **`definition` is retired, with no replacement.** It named the whole folder, but it collided with what a blueprint does (a blueprint *defines* a unit), and the everyday sense of the word is a dictionary entry rather than a folder tree. Eidos now turns on two words, framework and blueprint. Where the standard needs to name the folder it says "an Eidos folder" or "the root".
- **The default root name is `Blueprints/`,** plural, since it holds many. Only the default `install` offers. The root may still be named anything and nothing points at it by path.

### Per folder

1. **Set `eidos_version: 4.4.1`** in `_eidos/Framework.md`, and update the version note in its `## Schema` block. That is the whole required migration.
2. **Optionally refresh the seed prose in `_eidos/`.** `Framework.md`'s intro lines, the shape files, and `roles/*.md` say "item" and "definition" where the standard now says "blueprint". Purely cosmetic — nothing reads those words — so it is worth doing only where no one has edited the text since `install` wrote it.
3. **Leave a hand-edited role or shape alone** unless the owner asks for it. Their words are theirs.
4. **Renaming the root is optional.** An existing `Blueprint/` works exactly as it did; rename it only if the owner wants the plural, and then it is a plain folder rename with nothing pointing at it to fix.

**Nothing else moves.** No property, no body section, no filename, no collection.

Earlier hops on this page still say "item" and "definition" — they describe what those releases did, in the words those releases used.

## 4.3.2 → 4.4.0

**Rename two things inside `_eidos/`, write the definition's naming convention down, then set `eidos_version: 4.4.0`.**

### The two renames — every definition

Mechanical, and nothing outside `_eidos/` moves.

- **`_eidos/personas/` → `_eidos/roles/`.** Same files, same contents, same filenames inside (`framework-owner.md` and the rest keep their names). "Persona" was borrowed from UX, where a persona is an archetype of a *customer*, which is what a framing doc about the audience holds, not what these files hold. These are response contracts for the person at the keyboard, and the standard was already reaching for "role" to explain them.
- **`_eidos/user.md` → `_eidos/me.md`.** Same file, same contents. "User" in a product definition means the product's users; this file is you. The concept is still the **actor**; only the filename changed.
- **Update the two pointers.** `_eidos/.gitignore` ignores `me.md` instead of `user.md` (still the one `_eidos/` file not committed), and `me.md`'s own link to its role file now points at `_eidos/roles/`.
- **In `me.md`, the first calibration axis is renamed** from "Role for this definition" to **Ownership**. It always asked what you own here, and with the contracts now called roles the old label read as "your role's role". Rewrite the label; keep the answer.
- **A definition that never had `personas/` or a `user.md` skips this.** Both are optional in practice: a framework with no roles installed, and an actor who never recorded themselves, both still work.

Custom roles a team wrote are theirs and travel as they are. If a framework had renamed or added role files, the folder move touches none of it.

### The naming default — only if `naming` is absent

4.4.0 changes one default: `kebab-case` is now what the standard recommends and what an absent `naming` key means. Through 4.3.2 an absent key meant `Title Case`. **A definition that already carries the key needs nothing here** — the key is authoritative in both versions and only the fallback moved.

For a definition with **no** `naming` key, settle it rather than letting the default decide:

- **Read the convention off the files.** The tree already answers the question. A collection folder or item filename containing a space means `Title Case`; space-free and capitalized (`WatchAVideo.md`) means `TitleCase`; lowercase and hyphenated (`watch-a-video.md`) means `kebab-case`. Check a couple of collections rather than one file, and if they disagree, that is a real inconsistency to surface, not something to average.
- **Confirm it with the owner, then write it into `_eidos/Framework.md`.** State what the files say and what you are about to record. Recording what the definition already does is not a change to it.
- **Adopting kebab-case is a separate, deliberate pass,** never bundled into the version bump — it renames every collection folder, sub-folder, and item file, rewrites every link, and lowercases each grouping property's value to match its folder (`domain: Channels` → `domain: channels`). Do it when the owner wants it.

### Two smaller notes

- **The canvas's default filename follows the convention** — `framework-map.canvas` under kebab-case, `FrameworkMap.canvas` under TitleCase, `Framework Map.canvas` under Title Case. `canvas` only picks the name when you don't pass `--out`, so an existing canvas keeps its name until you regenerate without one; if it does get renamed, update its bullet in `## Top-Level`.
- **`README.md` is now named as an exception** beside `_eidos/`: it keeps the name every tool already looks for, whatever the convention. Nothing to change — this writes down what every definition was already doing.

**Nothing else moves.** No shape, no role file's contents, no property in the Schema, no body section.

## 4.3.1 → 4.3.2

**Set `eidos_version: 4.3.2`, or don't.**

The only change to the standard is its Versioning section, which now says that the plugin versions separately from the standard. Nothing a definition contains depends on it, so a definition left on 4.3.1 is not stale in any way that matters.

From here the two version lines diverge: a release that fixes a skill bumps the plugin and leaves `EIDOS.md` — and your `eidos_version` — alone.

## 4.3.0 → 4.3.1

**Set `eidos_version: 4.3.1`.** That is the whole migration.

The standard text is unchanged — `versions/v4.3.1.md` differs from `v4.3.0.md` only in its version lines. 4.3.1 shrank the skills and moved these worked hops out of `migrate` into this file. Nothing inside a definition is affected.

## 4.2.1 → 4.3.0

Additive, and the per-definition work is one bullet per collection. 4.3.0 takes the seed's own vocabulary out of the standard and the generators: `EIDOS.md` no longer names Intent, Out of Scope, Acceptance Criteria, or Implementation Notes in its Rules (the shape files already documented all four), and `build-canvas.py` no longer treats a collection called `Frames` as full-file nodes or looks for a section called `## Intent`.

- **Declare a `- **Canvas:**` bullet on every collection** in `_eidos/Framework.md`, under its `### ` heading beside **Leaf** and **Flavors**. It takes `file` (full-file nodes, for prose read whole), `card` (a text node embedding the whole item), or `card from ## Section` (a card embedding just that section). For a seed-derived definition the answers are `Frames` → `file` and `Specs` → `card from `## Intent``, which reproduce 4.2.x behavior exactly. For any collection the owner added, **ask** — the right answer depends on that shape, and there is no longer a name-based guess to fall back on.
- **Regenerate the canvas** with `canvas` if the definition has one. An undeclared collection now draws as a plain whole-item card, so a definition that skips the declarations gets a duller map, never a broken one.
- **Nothing else moves.** No item frontmatter, no body, no shape, no persona, no folder or file names. The removed Rules were duplicates of guidance already living in `_eidos/shapes/`, so a definition that customized its shapes keeps exactly what it wrote.
- **`owner` leaves the core Schema.** Delete its row from `### Eidos Core`. It was never read by any tool, and the actor file (`_eidos/user.md`) already says who is at the keyboard. **Don't strip `owner:` from items** — if a definition uses it, add it back as a row in `### Custom Properties` (Text, applies-to `all`) and every item keeps validating. If nobody uses it, leave the stray keys or clear them; either is fine.
- **Version.** Set `eidos_version: 4.3.0` in `_eidos/Framework.md`.

The net per definition: one `Canvas` bullet per collection, then set `eidos_version: 4.3.0`. Nothing else — the seeds and examples this release adds are repo-side, and where a framework was originally copied from has never been recorded in a definition.

## 4.2.0 → 4.2.1

The cheapest migration in the standard's history: **set `eidos_version: 4.2.1` in `_eidos/Framework.md`, and stop.** Nothing else in a definition changes.

4.2.1 fixes only what the two central words mean. Through 4.2.0 the standard called a whole `Blueprint/` a "framework"; from 4.2.1 the **framework** is the `_eidos/` form layer alone — collections, shapes, flavors, personas, naming, Schema — and the product written with it is the **definition**. One framework, many definitions.

- **No file or folder renames.** `_eidos/`, `Framework.md`, the shapes, the personas, and every collection folder keep their names. `Framework.md` names the framework more accurately now than it did before.
- **No property changes.** `### Eidos Core` is byte-identical to 4.2.0; only the version note above it moves to 4.2.1. Custom properties are untouched.
- **No persona rename.** `framework-owner` keeps its filename and its `# Framework Owner` heading — the role still holds intent, scope, and decisions. Any `user.md` naming it stays valid.
- **Optional prose pass.** If a definition's own `README.md` or top-level docs describe themselves as "this framework," reword them to "this definition." Cosmetic, and never required.

The net per definition: one line. Set `eidos_version: 4.2.1`.

## 4.1.0 → 4.2.0

A pure vocabulary-and-file rename — the per-product artifact becomes a **Framework**, not a "registry." No item frontmatter or body changes; the form layer's contents are untouched but for names. Diffing `versions/v4.1.0.md` against `EIDOS.md` (4.2.0) yields:

- **`_eidos/Registry.md` → `_eidos/Framework.md`.** Rename the index-and-contract file. Its body — `## Top-Level`, `## Collections`, `## Schema` (`### Eidos Core` + `### Custom Properties`) — is unchanged. Update the Top-Level regeneration marker from `<!-- eidos-registry: top-level index (regenerated) -->` to `<!-- configure: top-level index (regenerated) -->`.
- **`_eidos/personas/registry-owner.md` → `_eidos/personas/framework-owner.md`.** Same response contract; rename the file and its `# Registry Owner` heading → `# Framework Owner`, and fix the `[Registry Owner](registry-owner.md)` link in `_eidos/personas/README.md`. Any `user.md` naming the old persona is personal and gitignored — leave it, or point the actor at `whoami`.
- **Canvas.** If the definition has a generated "Registry Map" top-level doc, rename it "Framework Map" (the `.canvas` file and its `## Top-Level` bullet). `canvas` writes `Framework Map.canvas` from here on.
- **Version.** Set `eidos_version: 4.2.0` in `_eidos/Framework.md`.

Nothing else moves: the shapes, the Schema rows, every item's frontmatter and body, and the `_eidos/` directory name are identical to 4.1.0. Custom personas and custom properties carry across untouched. (The `eidos-registry`/`eidos-schema` → `configure` skill merge is a tooling change — nothing in a definition references a skill by name, so there's nothing per-definition to migrate for it.)

The net per definition: rename `Registry.md` → `Framework.md` (and its Top-Level marker), rename the `registry-owner` persona → `framework-owner`, optionally rename the Registry Map canvas → Framework Map. Set `eidos_version: 4.2.0`.

## 4.0.0 → 4.1.0

A property-model rework, the framing docs promoted to a collection, and a directory rename. Diffing `versions/v4.0.0.md` against `EIDOS.md` (4.1.0) yields:

- **Form-dir rename** — rename the form layer `.eidos/` → `_eidos/` (the dot dropped so Obsidian shows it and the owner can edit the Registry, shapes, and personas from the vault). Rename the directory; nothing inside it changes name. Every 4.0 registry takes this one structural step.
- **Schema moves into `Registry.md` as a `## Schema` section** — there is no separate `Schema.md`. The old flat `## Eidos Canonical` block becomes `### Eidos Core` (`id`, `title`, `summary`, `flavor`, `owner`, `connects_to`) plus `### Custom Properties` (the registry's) — which carries the seed's shipped defaults (`status`, `date_created`, `date_modified`, `tags`, and, scoped to `Specs`, `domain`, `depends_on`, `type`) with an **Applies To** column, followed by any pre-existing custom rows (give each an Applies To of `all`). Delete the old `_eidos/Schema.md`.
- **Property changes on every item:**
  - **Rename** `created` → `date_created` and `modified` → `date_modified`.
  - **Keep `type`, but move it** — it's no longer a core/required property, just a `Specs`-scoped custom default (a soft category label). Drop `type: frame` from the framing docs — their collection and flavor identify them.
  - **Optionally add** `summary` (one line from Intent, for the index) and `connects_to` (canvas edges) — both optional, nothing to backfill.
  - `owner` keeps its value but now means who owns the document (non-owners are warned before editing).
- **Persona rename** — `_eidos/personas/product-owner.md` → `_eidos/personas/registry-owner.md` (the same response contract, generalized to true registry ownership).
- **Templates → the Frames collection.** The `templates/` concept is retired: move `.eidos/templates/{Architecture,Audience,Criteria,Market}.md` → `_eidos/shapes/frame.{architecture,audience,criteria,market}.md` (they become the `Frames` collection's flavor shapes — strip the inline frontmatter, keep the body and its guidance). Delete the old `templates/`.
- **Framing docs → collection items.** Move the registry's root `Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md` into a new `Frames/` folder, and give each the collection frontmatter generated from the Schema (`id`, `flavor:` its kind, `owner`, `status`, `summary`, the two dates), preserving its prose. They are no longer top-level docs.
- **Registry** — in `_eidos/Registry.md`, declare `Frames` **first** in `## Collections` (framing docs are the most primary), then `Specs`; give Frames its four `frame.*` flavors (flat, no domains). Remove the four framing docs from `## Top-Level`, leaving only the owner's own top-level docs (a Roadmap, a Vision, the Registry Map). Bump `eidos_version` to `4.1.0`. Regenerate each collection's `index.md` with `index`.

The net per registry: rename `.eidos/` → `_eidos/`; merge `Schema.md` into `Registry.md`'s `## Schema` (Core + Custom, Applies To column); on every item rename the two date keys (and drop `type: frame` from frames); optionally add `summary`/`connects_to`; move `templates/*` → `shapes/frame.*`; move the four framing docs into a Frames-first `Frames/` collection; rename the `product-owner` persona to `registry-owner`; trim `## Top-Level` (README first). Set `eidos_version: 4.1.0` when done.

## 3.1.0 → 4.0.0

A breaking move — the layout changes — but the per-item contract barely does. Diffing `versions/v3.1.0.md` against `versions/v4.0.0.md` yields (note: migrating straight to the current version instead folds the framing docs into the `Frames` collection — see the 4.0 → 4.1 example below — rather than into a `templates/` folder):

- **Properties** — the canonical block gains one **optional** property, `flavor` (Text, no): which body flavor an item follows, absent meaning the collection's default. Rewrite `## Eidos Canonical` to the 4.0.0 seed and leave `## Custom Registry Properties` untouched. Nothing to backfill — absent already means default.
- **Shapes, templates, flavors** — rename `.eidos/shapes/Spec.md` → `spec.full.md` (the Specs collection's default flavor) and offer to add `spec.micro.md` from the seed. Remove the `Domains.md` shape (the Domains doc is gone). **Move the top-level-doc shapes (`Architecture.md`, `Audience.md`, `Criteria.md`, `Market.md`) from `.eidos/shapes/` into a new `.eidos/templates/`** — shapes are now collection-only; top-level docs use templates. Spec sections are unchanged, so items need no body restructuring.
- **`Domains.md` → `Specs/index.md`** (the breaking change). Move the top-level `Domains.md` into a generated `Specs/index.md` leaf inside the collection — the per-item listing, links now relative to `Specs/`. Lift the domain **descriptions** up into the Registry's Collections section (under Specs → Domains), since the leaf is purely generated. Regenerate the leaf with `index`.
- **`Registry.md` gains a body.** Frontmatter unchanged but for the version bump to `4.0.0`. Add the body: a `## Top-Level` (a bullet per top-level doc — link + the owner's one-line description) and a `## Collections` declaring the default `Specs` collection with its flavors (`full` default, `micro` if added), its domain grouping (with the descriptions lifted from `Domains.md`), and a pointer to `Specs/index.md`.
- **`README.md` start-here** — install the chosen seed's `README.md` → `<root>/README.md` and fill the product name; it is the visible front door into the Registry.
- **Personas + the actor file** — install the seed's persona defaults (`personas/` → `.eidos/personas/`), its blank `user.md` → `.eidos/user.md`, and its `.gitignore` → `.eidos/.gitignore` (merge a `user.md` line into an existing `.eidos/.gitignore` rather than overwriting it). Then run `whoami` so each actor sets their persona and calibration.
- **Specs** — untouched; bodies and frontmatter already conform, and `flavor` is optional, defaulting to `full`.

The net per registry: add the optional `flavor`; rename the shape; relocate `Domains.md` → `Specs/index.md` (descriptions up to the Registry); add the Registry body, a root `README.md`, `.eidos/personas/`, and `.eidos/user.md` + `.eidos/.gitignore`. No per-item body edits. Set `eidos_version: 4.0.0` when done.

## 3.0.0 → 3.1.0

A small, additive move — nothing in a 3.0.0 registry breaks. Diffing `versions/v3.0.0.md` against `versions/v3.1.0.md` yields:

- **Form layer** — the shapes and the canonical property set are unchanged; the only edit to the `## Eidos Canonical` block is the `domain` property's wording, now "matching its folder … in the registry's naming convention." Rewrite the canonical block to the 3.1.0 seed and leave `## Custom Registry Properties` untouched.
- **`Registry.md` becomes YAML frontmatter.** The 3.0.0 bold-key lines move into frontmatter: `**Eidos Version:** 3.0.0` becomes an `eidos_version` key (bumped to `3.1.0`), and a `naming` key is added.
- **Naming** — set `naming: Title Case`: it is the prior behavior, so this just records what the registry already does. Switch to `TitleCase` or `kebab-case` only if the owner wants space-free names — which then means renaming the files, a separate and deliberate pass.
- **Top-level docs** — no migration. The registry may now add its own free-form top-level docs (a Roadmap, a Vision) via `format`, but nothing existing changes.

The net is the small `Registry.md` conversion plus the one-line Schema reword; items and top-level docs are otherwise untouched.

## v2.x → 3.0.0

This is the move that introduces the form layer. Diffing `versions/v2.1.0.md` against `EIDOS.md` (3.0.0) yields:

- **Form layer** — install `Blueprint/.eidos/` from the canonical seed: `shapes/` (the body shapes, one per kind of doc), `Schema.md` (the canonical property block), and `Registry.md`. The body section set is unchanged from v2.1, so the Spec shape carries the same sections — they simply now live in `.eidos/shapes/Spec.md` instead of a standalone template.
- **Properties** — the canonical property set is otherwise the same as v2.1, with one removal: **`eidos_version` comes off every item and top-level doc** — the version is now a registry fact in `.eidos/Registry.md`. Frontmatter is otherwise unchanged.
- **Body** — no restructuring; v2.1 and 3.0.0 share the same baseline sections and `AC{n}` labeling.
- **Version** — write `**Eidos Version:** 3.0.0` into `.eidos/Registry.md`.

The net of v2 → v3 is small per file (drop `eidos_version`) but adds the `.eidos/` form layer once for the whole registry. Preserve any custom properties or reshaped sections — but a clean v2 registry won't have any yet.

## v1.0.0 → 2.0.0

Diffing `versions/v1.0.0.md` against `versions/v2.0.0.md` yields:

- **Frontmatter** — remove `last_validated`, `implements`, `serves_job`, `activity`, `supersedes`; add `created` and `modified` (`YYYY-MM-DD`); remap `status` (`proposed`/`accepted` → `Intake`, `in-progress` → `In Progress`, `shipped` → `Done`, `deprecated` → `Deprecated`).
- **Body** — `## Behavior` → `## Behaviors & Acceptance Criteria`, label criteria `AC{n}` under `###` requirement sub-headings; merge `## Constraints` + `## Decisions` → `## Constraints & Decisions`; add `## Dependencies` and `## Testing` stubs; add an optional `### Implementation Notes` under Intent.
- **Structure** — root `product/` → `Blueprint/`; `Domains.md` bullet list → `##` sub-headings per domain.

Carry `last_validated`'s date into `modified` (and `created` if no better date exists), and surface any `supersedes`/`implements` targets for the human to record in prose `Dependencies` before dropping the fields. To go straight from v1 to v3, diff those two snapshots and combine this with the form-layer install above.
