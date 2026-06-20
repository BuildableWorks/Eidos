---
name: eidos-domains
description: >-
  Build or refresh the Domains.md navigation index for an Eidos registry — the table of contents that maps each domain to its specs. Use when someone wants to "update the domains index", "regenerate Domains.md", "build a table of contents for the specs", "map the registry", says the domains file is out of date, or after specs have been added, renamed, moved, or removed. It crawls Specs/, groups by domain, preserves the hand-written domain descriptions, and rebuilds each domain's list of specs as links with a one-line summary drawn from each spec's Intent. Regenerable and never gates.
---

# Eidos Domains

Keep `Domains.md` working as the registry's **map** — the file a human or an agent reads first to find the right spec without scraping the tree. Each domain has two layers: the owner's short **description** (theirs, written once) and a generated **index** of that domain's specs (links + one-line summaries). This skill rebuilds the index and leaves the descriptions alone.

## How you work: derive, don't author

The index is navigation derived from the specs, so regenerating it is safe and mechanical. But two things stay the human's:

- **Domain descriptions.** If a domain has no description, add the `##` heading and ask the owner to describe it — don't invent the description.
- **The specs themselves.** A summary distills a spec's _own_ Intent into one line; it never adds meaning the spec doesn't have. The spec is the source of truth; the index just points at it.

## Where things are

- `Domains.md` at the registry root (usually `Blueprint/Domains.md`).
- The specs under `Specs/<Domain>/`, each carrying a `domain` in its frontmatter and an `## Intent` section.
- This needs a set-up registry. If there's no `.eidos/`, it isn't an Eidos registry yet — offer `eidos-init`.

## Procedure

1. **Crawl the specs.** Walk `Specs/`. For each spec, read its `domain` (frontmatter), its `title`, its path, and its `## Intent`.
2. **Summarize each spec.** Distill its Intent to one plain line — the first sentence tightened, or a faithful one-line paraphrase of the problem it solves. One line, no more; never beyond what the Intent says.
3. **Group by `domain`.** Use the frontmatter `domain`, not the folder, if the two ever differ (and flag the mismatch).
4. **Rebuild `Domains.md`.** One `##` per domain. Under each:
   - keep the owner's existing description prose untouched;
   - below it, regenerate the spec index — a marker comment, then a bullet per spec: `- [Title](Specs/<Domain>/<File>.md) — one-line summary`. Build each path from the target's filename in the registry's naming convention (read `naming` from `.eidos/Registry.md`): encode spaces as `%20` in a Title Case registry; a TitleCase or kebab-case one has no spaces to encode.

   ```markdown
   ## Identity

   Who the user is and how they prove it.

   <!-- eidos-domains: spec index (regenerated) -->
   - [Magic Link Sign-In](Specs/Identity/Magic%20Link%20Sign-In.md) — passwordless sign-in by an emailed single-use link.
   - [Session Management](Specs/Identity/Session%20Management.md) — keep a signed-in user across visits, and let them end access on a device.
   ```

   The marker comment is how you find and replace the generated list on a re-run without disturbing the description above it.
5. **Reconcile domains.**
   - A domain with specs but **no description** — add the heading and a `<!-- TODO: describe this domain -->`, and tell the owner.
   - A domain **described but with no specs** — dangling; flag it and ask whether to drop the description or whether a spec is missing.
6. **Report** — the domains and specs indexed, any summaries you'd like the owner to sharpen, and any domain still needing a description.

## Notes

- Regenerable and idempotent: running it again yields the same file (plus any new specs). It never gates — `Domains.md` annotates and navigates, it doesn't validate.
- This is the index half of Eidos navigation; the property/shape form lives in `.eidos/` and is handled by the other skills.
