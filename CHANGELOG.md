# Changelog

All notable changes to the Eidos standard are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Entries are plugin releases.** The plugin and the standard version separately: the plugin moves on every shipped release, the standard only when the text of `EIDOS.md` moves. Each entry from 4.3.2 on names the standard it ships, so **Standard: unchanged** means your Eidos folders need nothing; entries before that predate the split, when the two were one number. The current standard always lives in `EIDOS.md`; each of its releases is frozen in `versions/` under its full semver name, with the upgrade path in `versions/MIGRATIONS.md`.

## [Unreleased]

## [4.5.2] - 2026-09-02 — Standard: 4.4.2

**An audit of the glossary, and the repairs it turned up.** 4.5.1 renamed the unit and retired a term; reading the result cold showed what that left behind, plus a few things that had been wrong for longer. All prose: no property, folder, or filename moves, and the only behavior change is the name the canvas gives itself.

Retiring "definition" was right, but the concept it named did not disappear — the standard just stopped having a word for it, and fell back on "an Eidos folder" about a hundred times across the docs and skills. An undeclared phrase used that often is a term whether or not it is in the table. **`root`** is now declared, which also fixes the vocabulary's other problem: the table used to open on `framework`, "the form *everything* is written in", with nothing named for it to be the form *of*. Now `root` comes first and `framework` has an antecedent.

The Rules had quietly become a summary of the document. Twenty-four "load-bearing conventions", of which five restated a section that had already said it, so a reader could not tell which rules carried information they did not already have. Those five fold back into the sections that carried them and the list renumbers. Nothing is relaxed, and if you cite Eidos rules by number, that is the one thing here worth re-checking.

### Changed

- **`root` is a declared term** — the one folder Eidos lives in, holding the framework, the collections, and any top-level docs, found by its hidden `_eidos/` and never by its name. It leads the vocabulary table, and the prose across `EIDOS.md`, the seeds, and all nine skills now uses it instead of "an Eidos folder", "the folder", and "the definition root" interchangeably.
- **`shape` and `flavor` stop defining each other.** Shape was "the body template a collection's blueprints follow" and flavor was "one of a collection's shapes", so a reader could not tell whether a collection has one shape or several. A shape is now one body template, one file in `_eidos/shapes/`; a collection's shapes are variants of one family, and each variant is a flavor. The concepts are untouched.
- **`frame` no longer contradicts the thesis.** The vocabulary described frames as "loose, point-in-time" two rows after the standard claims a blueprint is "independent of time or status" — and a frame is a blueprint. What that phrase meant is that a frame is judgment about the whole rather than a description of one unit, revised when the judgment changes, so it now says that. Rule 16 (was 17) drops the phrase to match.
- **The Rules go 24 → 19, and renumber.** Dropped as restatements: `id` permanence (in the Schema table, which now also notes that `title` renames freely), human-facing naming (`## Naming`), `Framework.md` is the index and `README.md` the door (their own sections), each collection has a generated index (`## Generated leaves`), and shapes are for collections (the vocabulary and `## Frames and top-level docs`).
- **The generated canvas is the Blueprint Map.** It draws blueprints and their `connects_to` edges; the framework is the one thing it never draws, which made "Framework Map" exactly backwards after the rename. `build-canvas.py` defaults to `blueprint-map.canvas` (or `BlueprintMap.canvas` / `Blueprint Map.canvas`) and, as before, only picks the name when `--out` is absent — so **an existing `framework-map.canvas` keeps its name until it is regenerated without one.**

### Fixed

- **Rule 15 (was 16) mandated behavior for properties the standard does not define.** It fixed how `date_created` and `date_modified` behave, three sections after the Schema says "Eidos defines no custom properties" and names dates as a framework's own choice. It keeps the half that binds — the Eidos version is a framework fact, in `Framework.md`, never a per-blueprint property — and leaves dates to the framework declaring them. Nothing changes for a framework already carrying them.
- **`README.md` claimed six core properties.** There are five: `id`, `title`, `summary`, `flavor`, `connects_to`. Wrong since the core set last changed, and unrelated to this release.

## [4.5.1] - 2026-09-02 — Standard: 4.4.1

**One word doing the work of two.** The unit of an Eidos folder is a **blueprint**, not an "item", and **definition** leaves the vocabulary with nothing in its place. Prose only: no property, folder, or filename ever carried either word, so every folder already in a repo is conformant as it stands.

"Definition" had two problems and they compounded. The standard leans on the verb everywhere — a blueprint "defines one unit completely" — so *the definition* read just as naturally as the file as it did the folder full of them, and the vocabulary entry had to open with "The whole thing being defined" to pull it back. A term that needs a disambiguating gloss is not carrying its weight. The everyday sense made it worse: people hear "a definition" and picture a dictionary entry two lines long, not a folder tree. And it was the only abstraction in a vocabulary of concrete nouns — framework, collection, shape, frame, seed all have a picture; the biggest container, the one that most needs one, did not.

Blueprint takes the unit slot, where the granularity is right: one drawing of one thing, complete on its own, and indifferent to whether the thing is built yet. Architects keep blueprints of buildings that have stood for a century — as-built drawings — which is exactly what Eidos claims for a unit: as true of something planned as of something long finished. It also pairs. Framework and blueprint are both construction nouns, so the form/thing split lands without explanation, and the folder holding it all turns out to need no name of its own.

Migration is one line, `eidos_version: 4.4.1`, plus an optional cosmetic refresh of the seed prose inside `_eidos/`. The hop is in `versions/MIGRATIONS.md`.

### Changed

- **`item` → `blueprint`,** through `EIDOS.md`, the three seeds, and all nine skills. Same thing it always was: one markdown file in a collection, defining one unit completely, a frontmatter contract plus a body shape. Nothing a script or an agent parses uses the word — `id`, `title`, `summary`, `flavor`, and `connects_to` are untouched — so no folder changes shape.
- **The two-word pitch is now framework and blueprint.** Rule 2 becomes "The folder owns its framework", `## Writing a definition` becomes `## Writing`, and "Item bodies" becomes "Blueprint bodies". Where the standard has to name the whole folder it says "an Eidos folder" or "the root", both of which it was already using.
- **The default root name is `Blueprints/`,** plural, because it holds many. This is only the default `install` offers: the root may still be named anything, nothing points at it by path, and **an existing `Blueprint/` keeps working with no rename.**
- **The book seed calls a chapter's plan its blueprint** rather than its "definition" — in the seed README and in the sketch flavor's header. The word was already doing the new job there.

### Removed

- **The term `definition`.** Retired from the vocabulary table and from every skill, seed, and script that used it as a term. It survives in two places where it is ordinary English and means what it says: `AGENTS.md` calling `EIDOS.md` the authoritative definition of the format, and the research seed's prior-work frame listing a definition among the things a literature can disagree on. Historical changelog entries and the earlier hops in `versions/MIGRATIONS.md` keep the words those releases shipped.

## [4.5.0] - 2026-09-02 — Standard: 4.4.0

**Shorter names, all round.** `some-spec-feature.md` is what a definition names its files unless it says otherwise, the skills drop their `eidos-` prefix, the actor layer stops borrowing words that already meant something else, a ninth skill lands to question an idea before anyone writes it down, and two piles of worked example content leave the repo.

kebab-case first. Naming has been a choice since 3.1.0, with Title Case as the default because the file tree is a table of contents and `Magic Link Sign-In.md` reads like one. It does, right up until something has to point at it: every link then carries `%20`, every path needs quoting in a shell, and every tool that touches the tree has one more escaping rule to get right. kebab-case gives up the spaces and gets all of that back, and the filename becomes the `id` rather than a second rendering of the title. Title Case and TitleCase stay exactly as they are, one line in `Framework.md` and a rename pass away.

Then the actor layer, where two names were borrowed words. A **persona**, in the UX sense everyone brings to the word, is a fictional archetype of a *customer*, which is exactly what a framing doc about the audience holds. So a designer opening `_eidos/personas/` expected user archetypes and found response contracts for the person at the keyboard. And "user", in a product definition, means the product's users; `_eidos/user.md` read as "this definition's users" when it meant "you". The standard was already reaching past both: it defined a persona as "a response contract for one **role**", and named the files `personas/<role>.md`.

### Added

- **A ninth skill, [`iterate`](skills/iterate/SKILL.md)** — the pass before authoring. One rough idea, questioned until it holds still: which collection and flavor it takes, what it is actually for, and how it fits what is already written. It runs three passes over a single idea (shape, intent, fit), asks in small batches against the neighbors it just read rather than in a vacuum, and **writes no file** — it ends with a recap the owner agreed to and hands that to `eidos`. It carries the stop conditions too, because an open-ended question loop that never stops is its own failure: you can state the idea in three sentences, or two rounds add nothing, or the owner is out of answers and what remains gets written down as open. Learning that an idea is really two ideas, or already covered, is a good outcome for a session that produces no item.
- **`eidos` checks the framework's version when it starts.** It reads `eidos_version` from `_eidos/Framework.md`, compares it to the `**Version:**` of the `EIDOS.md` it carries, and says something only when they differ — one line naming both versions and an offer of `migrate`. A definition *newer* than the plugin is called out as the plugin being behind, and never offered a migrate, since that would be a downgrade. **Once per session, and never a block:** the framework in front of you is the operative contract at whatever version it claims, so a declined offer ends it, and a check that fired on every item would be nagging rather than helping. The same rule is now in `EIDOS.md`'s `## For an agent`, so it holds for any agent, not just this skill.

### Changed

- **The skills drop their `eidos-` prefix.** `eidos-install` is `install`, `eidos-migrate` is `migrate`, and so on through `format`, `configure`, `index`, `canvas`, and `whoami`; the core `eidos` skill keeps its name. Every host that surfaces a skill already says where it came from, so the prefix was paying for nothing and cost seven characters in every cross-reference. Historical changelog entries and the per-release notes in `versions/README.md` keep the names those releases actually shipped; the worked hops in `versions/MIGRATIONS.md`, which someone follows today, use the new ones. Nothing inside a definition names a skill, so no definition changes.
- **`_eidos/personas/` → `_eidos/roles/`.** Same files, same filenames inside; `framework-owner` and the rest are untouched. `actor` + `role` is also the pairing that reads: an actor plays a role.
- **The software seed's audience frame takes the word `persona` over.** Its `## User types` section is now `## Personas`, with the prompts under it asking for a persona rather than a type. Freeing the word from the form layer is what makes this possible: the audience frame is where a UX persona actually belongs, and it was the concept the old naming was colliding with. The shape's warning against the marketing-deck artifact stays, reworded to "no headshot-and-demographics cards" so it no longer reads as contradicting its own heading. A seed shape only, so no definition changes and nothing in the standard moves.
- **`_eidos/user.md` → `_eidos/me.md`.** "Me" cannot collide with anything, which `actor.md` would have: the `eidos` skill itself offers `actor` as a role a film framework might declare, so `_eidos/roles/actor.md` beside `_eidos/actor.md` was a trap. The **concept is still the actor** — only the filename moved, the way `README.md` is the door while "Framework" is the concept.
- **`me.md`'s first calibration axis is renamed to Ownership.** It always asked what you own on this definition; with the contracts now called roles, "Role for this definition" read as your role's role.
- **The seeded `.gitignore` ignores `me.md`** and says so in its comment. Still the one `_eidos/` file that is not committed.
- **The default naming convention is `kebab-case`**, and an absent `naming` key means `kebab-case` rather than `Title Case`. A definition that carries the key is untouched: the key is authoritative in both versions and only the fallback moved. A definition that doesn't should have its convention read off its own files and written down — `versions/MIGRATIONS.md` has the hop, including how to detect it. Both seeds and `install-seed.py` default to kebab-case; `install` offers it first.
- **`README.md` is named as an exception**, beside `_eidos/`, in the Naming section and in Rule 19. It keeps the name every tool already looks for, whatever the convention — which every definition was already doing, unwritten.
- **The canvas names itself in the convention.** `build-canvas.py` reads `naming` and defaults its output to `framework-map.canvas`, `FrameworkMap.canvas`, or `Framework Map.canvas`. The canvas is a top-level document, so its own name follows the same rule as everything else a human reads in the tree; `--out` still overrides.

### Removed

- **The `examples/` folder.** `Blueprint` (a subset of YouTube) and `Screenplay` (*The Salt Road*) are gone from the repo; worked, filled-in definitions belong on an instructional site, not in the standard's own tree, where they were a second copy of everything to keep in step with every release. `seeds/` still ships three complete frameworks, which is the part someone actually installs. `EIDOS.md`, `README.md`, and `seeds/README.md` no longer point at them.
- **`skills/eidos/references/example-spec.md`.** A whole worked spec loaded on every authoring session, to be pattern-matched for "craft, not section names" — a distinction that does not survive contact with a concrete file. The shape in the definition's own `_eidos/shapes/` already says what the body is, and one seed-flavored example sitting next to it mostly biased the output toward that seed's sections. Less context read, less pull toward the software vocabulary.

### Fixed

- **`install-seed.py` wrote group names that could not match their folders.** `--group "Prior Work"` created `prior-work/` but recorded `**Prior Work**` in the Framework's grouping bullet, so an item's grouping property could match the declaration or the folder but never both. The bullets are now written in the framework's convention, like everything else. Invisible while Title Case was the default and the two happened to agree; not invisible now.

## [4.4.0] - 2026-08-31 — Standard: unchanged (4.3.2)

Install stops being the skill that copies files by hand.

`eidos-index` and `eidos-canvas` each ship a script with a by-hand fallback; install, the most mechanical of the three, shipped only prose — and prose is what an agent improvises against. A real install run spent most of its cost on the copy: three whole seed frameworks read to quote a dozen lines, then a tarball moved between machines as base64 retyped through a shell heredoc, which arrived with a failed checksum and cost the entire round trip. None of that is judgment. All of it is now one call.

### Added

- **`eidos-install` ships an [`install-seed.py`](skills/eidos-install/install-seed.py)**, the sibling of `eidos-index`'s `build-index.py` and `eidos-canvas`'s `build-canvas.py`. Install is the most mechanical of the three: given the seed, the root, the naming convention, and the starting groups, every file it writes is derivable. The script copies the seed into `_eidos/`, moves the README to the definition root, sets `naming`, renames each collection into the convention (heading, folder, and links), scaffolds each collection folder with an empty `index.md`, drops a blank item per framing flavor, and records the groups in the Framework. It writes no prose. `--list` prints every seed's collections, flavors, and grouping in one call, which is also all step 2 needs to offer them. The prose steps stay as the sandboxed-host fallback.

### Changed

- **`eidos-install` step 5 says the seed and the definition may be on different machines.** The seed travels with the skill; the repo may only be reachable across a device bridge. The step now names the transfer: send the seed files with the file-delivery tool and write them to their final paths in one call, never re-typed as contents, base64, or a tarball through a shell heredoc, and never staged as an archive inside the repo. `eidos-migrate` carries the same line where it installs a seed into a definition that has no form layer.
- **`eidos-install` step 2 reads less.** Offering the seeds needs each `Framework.md`'s `## Collections` section, not the whole file: three complete frameworks read to quote a dozen lines.

### Fixed

- **Every seed called its framing collection "highly encouraged, not required."** 4.3.1 fixed that line in `eidos-install` and left it standing in the three seeds and the `Blueprint` example, which is where an installed definition actually reads it — and where `install-seed.py --list` now quotes it from. Rule 22 has made framing required as a declaration since 4.3.0: each seed's `Frames` now says it is that framework's framing collection, and that a frame left unwritten is a gap to surface, not a failure.

- **`eidos-configure`'s description was 340 characters over the 1024-char ceiling**, so `scripts/package-plugin.sh` refused to build the zip: the Claude Desktop upload path has been broken since 4.3.1, while the git-marketplace install everyone uses never checked. Trimmed to 998 by dropping the procedural clause the skill body already carries in full. Every trigger phrase stays.

**Migration from 4.3.2:** none. The standard is untouched, so every definition stays valid at `eidos_version: 4.3.2`. A definition installed before this release carries the old `Frames` description in its own `_eidos/Framework.md`; it is prose, and yours to reword or leave.

## [4.3.2] - 2026-08-26 — Standard: 4.3.2

Splits the plugin's version from the standard's.

They were one number, so a skill fix forced a standard release: 4.3.1 shipped a `versions/v4.3.1.md` snapshot that differed from 4.3.0 by exactly two version lines, and told every definition to bump an `eidos_version` for a change that touched none of them. Skills, seeds, and examples move far more often than `EIDOS.md` does, and the numbers should reflect that.

### Changed

- **`EIDOS.md`'s version is the standard's**, and moves only when the text of that file moves. It is what a definition records as `eidos_version`, what `versions/` snapshots, and what `eidos-migrate` migrates between.
- **`.claude-plugin/plugin.json`'s version is the plugin's**, and moves on every shipped release. It is what `/plugin install` and update checks see. `marketplace.json` must match it or updates no-op.
- **This changelog tracks plugin releases**, each naming the standard it carries.
- **`AGENTS.md` splits the release ritual in two.** A plugin-only release bumps two manifests and adds an entry here — no snapshot, no seed edit, no `eidos_version` change in anyone's definition.

They start on the same number and will drift. That is the point.

**Migration from 4.3.1:** set `eidos_version: 4.3.2` if you want to be current. The standard's only change is the Versioning prose above — nothing a definition contains depends on it, so staying on 4.3.1 is equally valid. This is the last release where a prose-only change to `EIDOS.md` costs you a bump; from here the plugin moves without it.

## [4.3.1] - 2026-08-26

A tooling release: **`EIDOS.md` is byte-identical to 4.3.0 but for its version line.** The standard did not move; the skills that carry it got 25% smaller, and a handful of places where they still contradicted 4.3.0 got fixed.

### Changed

- **Worked migrations move to [`versions/MIGRATIONS.md`](versions/MIGRATIONS.md).** `eidos-migrate` was 63% historical per-version hops and grew by one every release — 3,065 words and climbing. The eight hops now live beside the snapshots they describe, which the skill already syncs and reads on demand. The skill is 1,010 words and **no longer grows when the standard does**; `AGENTS.md` records the new release step so hops land there, never back in the SKILL.
- **Every skill trimmed.** 12,546 → 9,364 words across the eight, without touching the doctrine each has to carry: because a sandboxed host loads a skill alone, repeating "read the actor first" or the naming convention across skills is a requirement, not duplication, and it stayed.

### Fixed

- **`eidos-format` named eight seed sections as universal.** Its sorting step listed Behaviors & Acceptance Criteria, Out of Scope, Dependencies, Testing, Constraints & Decisions, Assumptions, Open Questions, and `AC{n}` as the places to file content — the exact bias 4.3.0 removed from the standard. It now reads section names off the item's flavor shape and routes by meaning.
- **`eidos` validation still hunted for seed sections**, flagging "an absent **Out of Scope**" and checking that "Implementation Notes read as intent."
- **`eidos-install` contradicted Rule 22**, calling the framing collection "highly encouraged, not required" three commits after the standard made it required-by-declaration. It also duplicated `EIDOS.md`'s naming table, complete with the software examples 4.3.0 had neutralized upstream.
- **A typo in `eidos-canvas`** introduced by 4.3.0's own sweep: "so the *detent* shows on the card."

**Migration from 4.3.0:** set `eidos_version: 4.3.1`. Nothing else — no item, property, shape, or collection changes.

## [4.3.0] - 2026-08-26

The de-biasing release. Eidos has always claimed that a collection's name and a shape's sections are the framework's, not the standard's — that a film team could run `Scenes` grouped by `Act` and never write a spec. `EIDOS.md` then taught from the software seed on 67 of its lines, the canvas generator special-cased a collection named `Frames`, and the skills told an agent to lead with Intent and flag a missing Out of Scope whatever it was looking at. An agent that reads a software vocabulary in the standard reaches for it in a framework that has none. This release makes the claim true, and ships two more seeds and a second worked example to prove it.

### Added

- **`seeds/` — three starting frameworks, not one.** `software` (Frames · Specs by domain) is the default. `book` (Frames of premise/reader/voice/market · Chapters by part) and `research` (Frames of question/prior work/method/ethics · Investigations by strand) are complete frameworks in their own right, each with its own shapes, personas, and Schema. `eidos-install` asks which one, reading `seeds/` at runtime rather than a hardcoded list.
- **A second worked example.** [`examples/Screenplay/`](examples/Screenplay) defines *The Salt Road*, a short film — `Scenes` grouped by `act`, a `pov` property, a canvas drawn from `## Logline`, nothing called a spec. It began as the `book` seed and was reshaped, which is what the standard has always claimed you can do and never demonstrated.
- **`- **Canvas:**` on a collection's Framework declaration.** How a collection draws is now the framework's call, beside its Leaf and Flavors: `file`, `card`, or `card from ## Section`. `eidos-configure` asks for it when adding a collection and treats it as a real decision.
- **Rule 14, "A shape documents its own conventions."** Section names, their order and meaning, and any labeling a shape asks for live in the shape file. The standard governs collections, shapes, flavors, and properties; it never governs a section.
- **`owner` removed from the core Schema.** No tool ever read it, and `_eidos/user.md` already establishes who is at the keyboard, so it was a field that had to be filled and never paid for itself. A definition that wants it re-adds it as a custom property and keeps every item valid.
- **Rule 22, "Every framework declares a framing collection."** The one collection every framework must declare, because a framework needs framing. Its name, flavors, and count are the framework's own — required as a declaration, never as a gate, so a declared-but-unwritten frame is a gap to surface rather than a failure.

### Changed

- **`EIDOS.md` names no collection, no shape, and no section.** Every worked example in it is now a placeholder (`<Collection>`, `<kind>.<flavor>.md`, `<Group>`), and the concrete vocabulary lives in `seeds/` and `examples/` where a reader goes looking for it deliberately. The seed's custom-property table is gone from the standard: Eidos defines no custom properties, and says so.
- **`build-canvas.py` knows no collection by name.** The `FRAMES_COLLECTION = "frames"` constant and the hardcoded `## Intent` embed are gone; the script reads each collection's declaration. An undeclared collection draws as a plain whole-item card, since the generator cannot guess which of a shape's sections is its summary.
- **Six Rules generalized or retired.** `domain` becomes "a collection's grouping is the collection's own"; Intent becomes "a shape names its own stable part"; Out of Scope becomes "non-goals carry the most weight"; the `AC{n}:` and Implementation Notes rules retire into the shape file and Rule 15. The Rules go 24 → 24 with different contents, and renumber from 10.
- **Skill procedures read the shape instead of assuming it.** `eidos` authors from the flavor shape's own opening and non-goals sections; validation flags "an absent non-goals section" against that shape; the actor is read from the persona file in front of you rather than inferred from its filename. `eidos-format` and `eidos-canvas` follow.
- **`seed/` → `seeds/software/`, `example/` → `examples/`.** `scripts/sync-skills.sh` syncs all of `seeds/` into `eidos-install` and `eidos-migrate`, and force-tracks every seed's `user.md` past its `.gitignore`.

### Unchanged

- **No item, folder, or property changes in a definition.** `### Eidos Core` is identical to 4.2.1 but for its version note. The retired Rules were duplicates of guidance already written in each shape file, so no guidance is lost and a customized shape keeps exactly what it says. Where a framework was originally copied from has never been recorded in a definition and still isn't.

**Migration from 4.2.1:** run `eidos-migrate` — add a `- **Canvas:**` bullet to each collection in `_eidos/Framework.md` (`Frames` → `file`, `Specs` → `card from ## Intent` reproduces 4.2.x behavior exactly; for a collection you added, decide from its shape), then set `eidos_version: 4.3.0`. Regenerate the canvas if you keep one. No items change.

## [4.2.1] - 2026-08-26

A vocabulary fix, and nothing else. 4.2.0 renamed the per-product artifact from a "registry" to a **Framework**, and in doing so overloaded the word: it named both the portable form layer *and* the product written in it. 4.2.1 splits them.

A **framework** is the form — the collections, body shapes and flavors, personas, naming convention, and property Schema that live in `_eidos/`. It is portable, carries no product content, and is the piece one team can hand to another. A **definition** is the product — the frames, items, and top-level docs a team writes with a framework. One framework, many definitions.

### Changed

- **A "framework" is now the `_eidos/` form layer only.** Every place the standard used "framework" to mean a whole `Blueprint/` now says **definition**: the definition root, the definition's `_eidos/`, "an Eidos definition." Where "framework" already meant the form — the framework's Schema, its naming convention, its declared collections and flavors — it stays, and reads more precisely than before.
- **`EIDOS.md` opens with a `## Vocabulary` section** stating the two terms, so neither can drift again.
- **Skill prose follows the split.** `eidos-install` scaffolds a definition and installs a framework into it; `eidos-migrate` moves a definition to a new version; `eidos-canvas` and `eidos-index` take a `<definition-root>`; the generators' error text reads "not an Eidos definition."

### Unchanged

- **No file, folder, or property changes.** `_eidos/`, `Framework.md`, the shapes, the personas, and every collection folder keep their names. `### Eidos Core` is identical to 4.2.0 but for the version note above it.
- **The `framework-owner` persona keeps its name.** The role still holds intent, scope, and decisions, and any personal `user.md` naming it stays valid. Whether it becomes `definition-owner` is a separate call, deferred rather than settled here.

**Migration from 4.2.0:** set `eidos_version: 4.2.1` in `_eidos/Framework.md`. That is the whole migration — `eidos-migrate` will do it, and there is nothing else to change. Optionally reword a definition's own `README.md` if it describes itself as "this framework."

## [4.2.0] - 2026-07-02

The vocabulary release: what a product carries is now a **Framework**, not a "registry." It's a framework because that's what it does — it frames how you think about the product, and it reads coherently alongside the parts that were already construction-shaped (the default `Blueprint/` root, the `Frames` collection — the studs — `Architecture`, and `Specs`). The rename is mechanical and fully migratable; nothing about how an item works changes. This release also consolidates the two registry-tending skills into one.

### Changed

- **"Registry" → "Framework" throughout the standard.** The per-product artifact — the `_eidos/`-governed thing that holds the index, the collections, and the property contract — is a **Framework**. The concept, prose, and skill vocabulary all move from "registry" to "framework". No behavior changes; the shape of an item, the form layer, and every rule are identical.
- **`_eidos/Registry.md` → `_eidos/Framework.md`.** The index-and-contract file is renamed. Its body (`## Top-Level`, `## Collections`, `## Schema`) is unchanged. The generators (`build-index.py`, `build-canvas.py`) read `Framework.md`; the Top-Level regeneration marker is `<!-- eidos-configure: top-level index (regenerated) -->`.
- **`registry-owner` persona → `framework-owner`.** Same response contract (holds intent, scope, and decisions) — the owner owns the Framework.
- **Generated "Registry Map" canvas → "Framework Map."** `eidos-canvas` writes `Framework Map.canvas` by default.

### Removed

- **`eidos-registry` and `eidos-schema` skills, merged into `eidos-configure`.** Both only ever edited `Framework.md`'s body — `eidos-registry` its Top-Level and Collections/Flavors, `eidos-schema` its property Schema — so one skill now owns the whole file: add a collection or flavor, add/rename/retire a custom property (and backfill it), and refresh the Top-Level index.

**Migration from 4.1.0:** run `eidos-migrate` — it renames `_eidos/Registry.md` → `_eidos/Framework.md`, renames the `registry-owner` persona → `framework-owner`, updates the Top-Level marker comment, and bumps `eidos_version` to `4.2.0`. No item frontmatter or body changes; the form layer's contents are otherwise untouched. Breaking only in that files are renamed — mechanical and reversible, following the 4.1.0 precedent of shipping a form-layer rename as a minor.

## [4.1.0] - 2026-07-01

The release that makes Eidos's navigation mechanical and generalizes the framing docs. Every item gains two optional properties — `summary` (the one-line index/reference blurb) and `connects_to` (canvas edges); the framing docs (Architecture, Audience, Criteria, Market) become an official **`Frames` collection** (the retired `templates/` become its flavor shapes); "top-level documents" become a purely user-created loose layer; two generators ship — `eidos-index` (`build-index.py`) and the new **`eidos-canvas`** skill; and the hidden form directory is renamed **`.eidos/` → `_eidos/`** so Obsidian shows it. Additive over 4.0.0: existing items are untouched and both new properties are optional.

### Added

- **`summary` canonical property (optional).** One plain line — what the item is, in a sentence, distilled from Intent. The source for the collection `index.md` listing (and reference hovers), authored once on the item and read everywhere. Optional; an item missing it is flagged by the index, never refused.
- **`connects_to` canonical property (optional).** A List of links to the items this one connects to on the registry canvas — drawn as directed edges (this → target). The intentional map of how the product's pieces relate, decoupled from `depends_on` (an implementation dependency). Optional; absent means no canvas edges.
- **`Frames` collection.** The framing docs are promoted from one-off top-level docs to a real collection (`Frames/`), highly encouraged but not required. Its flavors — `frame.architecture`, `frame.audience`, `frame.criteria`, `frame.market` — are the old templates, now ordinary body shapes. Frames follow the same frontmatter contract as any collection item (`type: frame`, a `flavor`, a `status`, dates). A flat collection — frames aren't grouped by domain.
- **`build-index.py` in the `eidos-index` skill.** A stdlib-only Python 3 script that reads `_eidos/Registry.md` for the declared collections, walks each collection's folder, and rebuilds its `index.md` from the items' `title` + `summary` — grouped by sub-folder or flat, links URL-encoded for the registry's naming convention. Deterministic and idempotent, with a `--check` mode for CI and a `--collection` filter. Runs wherever a shell is available; on a sandboxed host the skill falls back to doing the walk by hand.
- **`eidos-canvas` skill.** Generate an Obsidian-compatible [JSON Canvas 1.0](https://jsoncanvas.org) `.canvas` map of the registry via `build-canvas.py`: items are text nodes embedding their `## Intent`; **Frames are full-file nodes** in their own group; directories nest into **nested groups** (a sub-directory under a domain becomes another group); each item's `connects_to` links are drawn as edges, with `--include-dependencies` overlaying `depends_on` in a distinct color (purple by default). **Each collection gets its own color** — the skill proposes a schema from the registry, confirms it, and a regenerated canvas keeps its colors so the choice sticks. Top-level documents are not mapped; the generated `.canvas` is itself a top-level document — register it in the Registry's `## Top-Level`.

### Changed

- **Form-layer directory renamed `.eidos/` → `_eidos/`.** The dot is dropped so Obsidian no longer hides the directory — users can open and edit `Registry.md`, the shapes, and the personas straight from the vault. It also sorts to the top of the tree and has no shell/tooling/wikilink edge cases. Same "machinery, out of the way" intent — only the leading character changes.
- **`eidos-init` skill renamed to `eidos-install`.** "Install" reads more plainly than "initialize" for what it does — stand up the form layer and starting collections in a repo.
- **Property model reworked into Core + Custom, scoped by Applies To.** Eidos's own machinery uses six **core** properties (`id`, `title`, `summary`, `flavor`, `owner`, `connects_to`); everything else — `status`, `date_created`, `date_modified`, `tags`, `domain`, `depends_on`, `type` — is a **custom** property the seed ships as a default, useful but not depended on, each scoped by an **Applies To** column (a list of collections, or `all`) so a property never lands where it makes no sense (`domain`, `depends_on`, and `type` are Specs-only). This replaces the old flat "canonical + required" table: the previously-required `domain`, `status`, dates, and `type` were opinionated, not things Eidos needs. `created`/`modified` become `date_created`/`date_modified`; `type` stays as a `Specs`-scoped soft category label (feature, capability, integration), no longer a core/required property. `owner` now means who owns the document (non-owners are warned before editing). Schema table headers are Title Case (`Name`, `Type`, `Applies To`, `Meaning`) for readability.
- **The Schema moved into `Registry.md` as a `## Schema` section**, and the property skill `eidos-property` → **`eidos-schema`**. There is no separate `_eidos/Schema.md` — one file (`Registry.md`) now holds the whole registry index and its frontmatter contract (`### Eidos Core` + `### Custom Properties`).
- **Seed folder `standard-seed/` → `seed/`, personas moved into it.** Dropping the "standard-" theming leaves room for non-canonical seeds later; the personas now live at `seed/personas/` (installed to `_eidos/personas/`) rather than a top-level folder. The seed self-documentation moved into this README's **Canonical Seed** section, `README.template.md` became the seed's `README.md` (it installs directly, no rename gymnastics), and the seed's `.gitignore` is now a real dotfile.
- **Persona `product-owner` → `registry-owner`.** The owner holds true ownership of the registry — which may define a product, a body of research, a methodology, or any other form of thought, not necessarily a product.
- **README is a top-level document.** It's listed first under the Registry's `## Top-Level` — the front door and a first-class entry, not a special case.
- **Spec shape splits "Open Questions & Assumptions" in two.** Assumptions (what you're taking as given) become an `### Assumptions` subsection under `## Intent`, where they frame it; `## Open Questions` (what you don't yet know) stands on its own. Mixing the two made a reader stop to ask "is this an active question or a settled assumption?" — the split removes that. Both `spec.full` and `spec.micro` flavors updated.
- **Collection indexes and the canvas are derived, not authored.** `eidos-index` emits each item's `summary` rather than distilling one at generation time; the canvas is built from `connects_to`. Both regenerate wholesale.
- **"Top-level documents" are now 100% user creations.** Eidos no longer ships canonical top-level docs; the framing four moved into `Frames`. A top-level doc (a Roadmap, a Vision, the generated Registry Map) is one-of-a-kind, free-form prose — no shape, no flavors, no validation — listed in the Registry's `## Top-Level`.

### Removed

- **The `templates/` concept.** The one-off top-level-doc templates are gone, replaced by the `Frames` collection's flavor shapes in `_eidos/shapes/`. `eidos-install` scaffolds a `Frames/` collection (optionally with the four blank framing docs) instead of scaffolding top-level docs from templates.

**Migration from 4.0.0:** run `eidos-migrate` — it renames `.eidos/` → `_eidos/`, adds the optional `summary` and `connects_to` rows to the canonical Schema, moves `.eidos/templates/*` → `_eidos/shapes/frame.*`, moves the root framing docs into `Frames/` as collection items, declares the `Frames` collection, and trims `## Top-Level`. Existing items are untouched; both new properties are optional. Bumps `eidos_version` to `4.1.0`.

## [4.0.0] - 2026-06-23

A breaking release that makes `.eidos/Registry.md` the registry's **index**, generalizes `Specs/` into declared **collections** with multiple body **flavors**, moves each collection's listing into a generated **`index.md`** inside its folder (retiring the top-level `Domains.md`), and adds a visible **`README.md`** "start here" plus a personal **`user.md`** actor file. A 3.x registry migrates with `eidos-migrate`; the per-spec contract is essentially unchanged, but the layout moves.

### Added

- **Collections.** A registry declares its top-level content folders in the Registry body, each with a description. `Specs` is the default; add more — decisions, personas, integrations — with `eidos-registry`. An item's collection is its top-level folder. A collection may group its items one level deep in sub-folders (Specs by domain); deeper nesting is discouraged.
- **Flavors.** A collection can offer more than one body shape — a default `full` and a lighter `micro` — each a file named `<kind>.<flavor>.md` in `.eidos/shapes/`. A new optional canonical property, `flavor`, records which an item follows (absent = the collection's default); validation checks the body against that flavor's shape, so a `micro` spec isn't faulted for `full`-only sections. The canonical default flavor renames `Spec.md` → `spec.full.md`, with `spec.micro.md` beside it. Shapes are **collection-only** and live in `.eidos/shapes/`; the one-of-each top-level-doc scaffolds are now **templates** in `.eidos/templates/` (no flavors, not validated, kept as the record of each doc's intended full form).
- **The Registry as index.** `.eidos/Registry.md` keeps its frontmatter (`eidos_version`, `naming`) and gains a body: a `## Top-Level` list of the top-level documents and a `## Collections` section with each collection's flavors and grouping. It is the authoritative index of the whole registry.
- **`README.md` start-here.** A thin, visible `README.md` at the registry root is the human front door — what the product is, with pointers into the registry — pointing into the hidden `Registry.md`. `eidos-init` seeds it from `standard-seed/README.template.md`.
- **Per-collection `index.md`.** Each collection carries a generated `index.md` leaf inside its folder — the item listing, grouped by sub-folder when present, flat otherwise. Fully generated (descriptions live in the Registry), so it rebuilds wholesale.
- **Personas.** Default response contracts — `personas/`, installed into `.eidos/personas/` (committed, team-tunable) — one per role (Product Owner, Developer, Stakeholder, Designer, Project Manager). A persona sets the agent's vocabulary, technical depth, what it surfaces, and who decides: a Designer gets experience terms (no db indexes), a Developer full depth, the Product Owner the decisions. The agent reads the actor's persona before responding.
- **The actor (`.eidos/user.md`) + `eidos-whoami` skill.** A personal, gitignored file that names the actor's persona and **calibrates** it — role for this product, experience with the scope, technical capacity. Set it with the new `eidos-whoami` skill (a guided who-are-you that `eidos-init` runs); unset or absent defaults to full, product-owner-style facilitation. It is the one `.eidos/` file not committed.
- **`eidos-registry` skill** — add a collection or flavor and keep the Registry's Top-Level/Collections index current.

### Changed

- **Rule 7 reframed** — from "one shape per registry" to "one shape family per collection, declared as flavors." A flavor is a deliberate, registry-declared structural choice; `type` still drives views, never structure. New rules: the Registry is the index and `README.md` its door (21), read the actor before acting (22), each collection has a generated index (23). New **The actor**, **Collections**, **Flavors**, and **Collection indexes** sections in `EIDOS.md`; `## Overview` in the Registry body is now `## Top-Level`.
- **`eidos-domains` → `eidos-index`.** The domain re-indexer generalizes to regenerate any collection's `index.md`, prompting which collections to re-index. `eidos`, `eidos-init`, `eidos-format`, and `eidos-registry` are updated for collections, flavors, the actor, and the new layout; the example registry gains a `micro`-flavored spec, a `Specs/index.md`, a `README.md`, and a committed `user.md`.

### Removed

- **The top-level `Domains.md`** and its shape. Its per-spec listing moves into `Specs/index.md` (one `index.md` per collection); the domain descriptions move up into the Registry's Collections section. This is the breaking change.

**Migration from 3.x:** run `eidos-migrate`. Net per registry: add the optional `flavor` to the canonical Schema; rename `.eidos/shapes/Spec.md` → `spec.full.md` (optionally add `spec.micro.md`); move `Domains.md` → `Specs/index.md` (its descriptions lifted into the Registry); add the Registry body (Top-Level + Collections), a root `README.md`, `.eidos/personas/`, and `.eidos/user.md` with a `.eidos/.gitignore` (then `eidos-whoami` to set personas); bump `eidos_version` to `4.0.0`. The per-spec body and most frontmatter are unchanged.

## [3.1.0] - 2026-06-19

An additive release. A registry now chooses how its files are named, the root folder is officially any name, and a registry can carry its own free-form top-level docs. Nothing here breaks an existing 3.0.0 registry — an unset naming convention defaults to today's Title Case.

### Added

- **Configurable naming convention.** A registry picks how human-facing names — spec files, domain folders, product docs — read, recorded as a `naming` key in `.eidos/Registry.md`'s YAML frontmatter: `Title Case` (the default; spaces, as before), `TitleCase` (no spaces), or `kebab-case` (lowercase, hyphenated — the filename then equals the `id`). The link format follows from it: only a Title Case registry encodes spaces as `%20`, so the two space-free options give clean, scriptable paths. `eidos-init` asks for the convention at setup; `eidos`, `eidos-format`, and `eidos-domains` read it when naming or linking.
- **Free-form top-level docs.** Beyond the canonical four product docs (Architecture, Audience, Criteria, Market), a registry may add its own top-level docs — a Roadmap, a Vision, a Glossary. These are free-form: no shape, no validation. They carry the light product-doc frontmatter and are supported by `eidos-format`, which organizes a draft into the house style rather than checking it against a template — because a top-level doc is filled in once and edited in place, not stamped out like a spec. The example registry gains a `Roadmap.md` to show the pattern.

### Changed

- **The registry root is officially any name.** It was always renameable, but the skills now locate a registry by its `.eidos/` marker rather than the folder name, so `Abstract/`, `Product/`, or the product's own name work as well as the default `Blueprint/`. The root is simply wherever `.eidos/` lives.
- **`Registry.md` is the registry's small config card, now YAML frontmatter.** It records the Eidos version (`eidos_version`) and the naming convention (`naming`) as frontmatter — the two registry-level facts the skills read, in the same metadata format the specs use and ready for `yq`/tooling.
- **`eidos-format` reshapes any registry doc**, not only specs: a spec toward the Spec shape, a product doc toward its shape, and a free-form top-level doc into the house style with no shape at all.

**Migration from 3.0.0:** nothing required — a 3.0.0 registry keeps working, defaulting to Title Case. To adopt the new format, convert `.eidos/Registry.md` to YAML frontmatter with `eidos_version` and `naming` (or run `eidos-migrate`, which does it and bumps the version). The canonical property set is unchanged.

## [3.0.0] - 2026-06-19

A breaking release that moves a registry's **form** — its body shapes and its property contract — out of the standard and into the registry itself, as a hidden `.eidos/` folder. Eidos becomes an opinionated baseline you can extend without forking: adopt as-is, add your own properties, still migrate.

### Added

- **The `.eidos/` form layer.** Every registry now owns its form in a hidden `.eidos/` at its root: `shapes/` (the body template for each kind of document), `Schema.md` (the property contract), and `Registry.md` (the Eidos version). Seeded by `eidos-init` from an opinionated baseline; the skills read it from there.
- **`Schema.md` — a registry-defined property contract.** Two blocks: `## Eidos Canonical` (the standard's properties, managed by `eidos-migrate`) and `## Custom Registry Properties` (yours, preserved across migration). Each property declares name, type, required, and meaning. Property types are drawn from the Obsidian set — Text, List, Number, Checkbox, Date, Date & time — so frontmatter renders natively in an Obsidian vault.
- **Generated frontmatter.** A spec's frontmatter is emitted from the Schema's required properties, so every new spec is born conforming.
- **Registry-defined validation.** A check reads _that registry's_ Schema — canonical required plus any custom-required — and surfaces a missing field by adding it with a note on why, never refusing the file.
- **`eidos-property` skill** — add, rename, or retire a custom property: it presses the owner to decide type, meaning, and whether it's required, writes the row into `Schema.md`, and backfills every existing spec.
- **`eidos-domains` skill** — regenerate `Domains.md` as a navigation index: each domain's hand-written description plus a generated list of its specs (links + a one-line summary distilled from each spec's Intent). Makes `Domains.md` the map humans and agents read first instead of scraping the tree.
- **`Registry.md`** — records the Eidos version in one spot, read and bumped by `eidos-migrate`.

### Changed

- **Skills consume the registry's form instead of vendoring templates.** The canonical baseline lives, public and front-facing, in the top-level `standard-seed/`; `eidos-init` installs it, and `eidos`, `eidos-format`, and `eidos-property` read the live `.eidos/` from the registry in the working directory. The old template triplication is gone; the three skills that need the standard (`eidos`, `eidos-init`, `eidos-migrate`) carry committed copies of just what they need, kept in sync by `scripts/sync-skills.sh`, so a git-marketplace install works on Claude Code and sandboxed Claude Desktop alike.
- **"Works from `EIDOS.md` alone" is retired.** `EIDOS.md` gives the method; doing Eidos now needs the skills and a seeded registry. The `## AI` section and the "templates ship with the standard" guidance were rewritten accordingly.
- **Body shapes** moved from the top-level `templates/` into `.eidos/shapes/`. The Spec shape is body-only (frontmatter is generated); the product-doc shapes keep their own light frontmatter. The baseline section set is unchanged from 2.1.
- **The canonical baseline is a public, top-level `standard-seed/`.** The seed (shapes + `Schema.md` + `Registry.md`) is browsable at the repo root, not tucked inside a skill; `eidos-init` installs it, and `eidos-migrate` reads it.
- **The `eidos` skill is lean and defers to `EIDOS.md`.** It holds the facilitation flow and reads the registry's `.eidos/`, and points to `EIDOS.md` — the officially maintained ruleset, carried as a committed copy in the skill — instead of restating the rules. Its `core-overview.md` and `spec-schema.md` references were removed as duplicative; `example-spec.md` stays.
- **`Domains.md` became the registry's navigation map** — each domain's description plus a generated per-spec index — rather than descriptions alone. The body-section catalog was also pulled out of `EIDOS.md` into the Spec shape, leaving `EIDOS.md` with the rules for using a body, not the section list.

### Removed

- **The per-doc `eidos_version` frontmatter field** — the version is a registry fact now, in `.eidos/Registry.md`.
- **The top-level `templates/` folder** and **`scripts/sync-skills.sh`** — replaced by the seed in `eidos-init` and the registry's own `.eidos/`.

**Migration from 2.x:** use the `eidos-migrate` skill, or diff `versions/v2.1.0.md` against `EIDOS.md`. The net per registry is small: install `.eidos/` from the v3 seed (shapes, canonical `Schema.md`, `Registry.md`), drop `eidos_version` from every spec and product doc, and write `**Eidos Version:** 3.0.0` into `.eidos/Registry.md`. The body section set is unchanged, so specs need no restructuring.

## [2.1.0] - 2026-06-18

### Added

- Apache License 2.0 (`LICENSE`); `license: Apache-2.0` declared in the plugin manifest.
- `eidos-format` skill — reshapes a rough draft or brain-dump into the Eidos spec shape, preserving the author's words and adding nothing. It reads the spec template for the target shape and is mostly a format-and-organize pass within a single file.
- An `## AI` section at the foot of `EIDOS.md` — condensed operating guidance (facilitate-don't-author, authoring, validating, the link format) for an AI working without the skills installed; humans can stop above it. The former top-level `## Validation` section folded into it.

### Changed

- Clarified that the spec body sections are a scaffold, not a form: shape them for readability (sub-headings, tables, lists), never flatten rich content onto one line, and keep acceptance criteria short with supporting detail pushed into tables or sub-sections. Captured as Rule 3, _Write it like a human would read it_, and echoed in the schema, the `eidos` skill, and the Spec Template.
- Cross-references between specs are now markdown links (relative path, `%20` for spaces, `#heading` for a section), never bare `code-style` names — readable and navigable. Captured as Rule 4, _Reference other specs as links, never bare names_, with a new _Referencing other specs_ section; the example specs' Dependencies were converted, and `eidos-format` treats name→link as a formatting fix. The convention extends to linking properties: `depends_on` now holds markdown-link strings rather than bare ids (the linked spec's `id` stays its permanent identity).
- Clarified the shared spec shape: _which_ sections appear is flexible (omit what doesn't apply, no empty headings), but their order and names are strongly encouraged — close to required — so every spec reads predictably and is not a free-for-all. Reworded Rule 5 (was _One shape for specs, always_) to _One shared shape, in a predictable order_.

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

[Unreleased]: https://github.com/BuildableWorks/Eidos/compare/v4.0.0...HEAD
[4.0.0]: https://github.com/BuildableWorks/Eidos/compare/v3.1.0...v4.0.0
[3.1.0]: https://github.com/BuildableWorks/Eidos/compare/v3.0.0...v3.1.0
[3.0.0]: https://github.com/BuildableWorks/Eidos/compare/v2.1.0...v3.0.0
[2.1.0]: https://github.com/BuildableWorks/Eidos/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/BuildableWorks/Eidos/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/BuildableWorks/Eidos/releases/tag/v1.0.0
