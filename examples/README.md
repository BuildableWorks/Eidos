# Examples

Two filled-in Eidos definitions to read and pattern-match against. They are deliberately different
kinds of thing, because that is the claim Eidos makes: `specs` and `domains` are the default seed, not
the essence, and every skill works the same way across both.

| Example | What it defines | Seed | Collections |
| --- | --- | --- | --- |
| [`Blueprint/`](Blueprint) | a small subset of **YouTube** — watching and resuming videos, running and following a channel | `software` | `frames` · `specs` by domain |
| [`Screenplay/`](Screenplay) | **The Salt Road**, a short film about a cartographer who can no longer read her own maps | `book`, reshaped | `frames` · `scenes` by act |

For what the pieces _are_ — framework and definition, top-level docs, collections, shapes, flavors,
Schema, roles — see the [root README](../README.md) and [`EIDOS.md`](../EIDOS.md). This file just
walks the two.

To start your own definition, run the `install` skill and pick a [seed](../seeds) — don't copy
either of these.

---

## `Blueprint/` — a subset of YouTube

The software case, and the one `EIDOS.md` teaches from. `Blueprint` is the default root name; nothing
points at it by path, so a definition may call its root anything.

```
Blueprint/                 # the definition
  README.md                # the definition's own "start here" front door
  _eidos/                  # the framework (hidden): shapes, roles, Framework (index + config + Schema), me, .gitignore
  roadmap.md               # a custom top-level doc — free-form, no shape
  frames/                  # the framing collection
    index.md               #   generated index of the collection
    architecture.md  audience.md  criteria.md  market.md
  specs/                   # the default collection
    index.md               #   generated index of the collection
    playback/              #   ┐ domains — the specs collection's grouping
      watch-a-video.md     #   │
      resume-playback.md   #   │ (flavor: micro)
    channels/              #   ┘
      subscribe-to-a-channel.md
      upload-a-video.md
```

What to notice:

- The **framing collection** ([Architecture](Blueprint/frames/architecture.md), [Audience](Blueprint/frames/audience.md), [Criteria](Blueprint/frames/criteria.md), [Market](Blueprint/frames/market.md)) frames the product — one framing doc per flavor, listed in the generated [`frames/index.md`](Blueprint/frames/index.md); [Roadmap](Blueprint/roadmap.md) is a custom top-level doc this definition added.
- The **specs collection** holds the units, grouped into the **`playback`** and **`channels`** domains, listed in the generated [`specs/index.md`](Blueprint/specs/index.md).
- It offers two **flavors** — `spec.full` (default) and `spec.micro`. [Resume Playback](Blueprint/specs/playback/resume-playback.md) carries `flavor: micro`, so it's checked against the lighter shape.
- [`_eidos/Framework.md`](Blueprint/_eidos/Framework.md), in its `## Schema` section (`### Custom Properties`), adds one **custom property**, `beta` — a framework extending the baseline without forking the standard.
- [`_eidos/roles/`](Blueprint/_eidos/roles) holds the **response contracts**, and [`_eidos/me.md`](Blueprint/_eidos/me.md) names the **actor** (here a technically-fluent Framework Owner). `me.md` is normally gitignored; it's committed here only to show its shape.

---

## `Screenplay/` — The Salt Road

The other end of the range. Nothing here is called a spec, and the definition still validates,
indexes, and maps identically.

```
Screenplay/                # the definition — a custom root name
  README.md
  _eidos/                  # the framework: scene + frame shapes, two roles, Framework, me, .gitignore
  framework-map.canvas     # a generated top-level doc — the canvas
  frames/
    index.md
    premise.md  voice.md  audience.md  market.md
  scenes/                  # the units — not "specs"
    index.md
    act-i/                 #   ┐ acts — the scenes collection's grouping
      cold-open.md         #   │
      the-commission.md    #   │
    act-ii/                #   ┘
      the-crossing.md
      what-she-says.md     #     (flavor: beat)
```

What to notice:

- It started from the [`book`](../seeds/book) seed and was **reshaped**: `chapters` → `scenes`, `part` → `act`, chapter shapes → scene shapes, and a new `pov` property. The standard was not forked, and `configure` is how you'd do it. That reshaping is the normal case, not a special one.
- The scenes collection declares **`Canvas: card from ## Logline`** in [`_eidos/Framework.md`](Screenplay/_eidos/Framework.md). The canvas embeds that section because the framework says so — no generator knows a collection or a section by name.
- **Grouping is the collection's own.** `act` here does exactly what `domain` does under `specs`, and `frames` groups by nothing at all.
- [What She Says](Screenplay/scenes/act-ii/what-she-says.md) carries `flavor: beat` — the film's ending, deliberately thin, because the decision hasn't been made. A definition is allowed to be honest about that; a task list isn't.
- **Out of Scope is doing real work.** [The Crossing](Screenplay/scenes/act-ii/the-crossing.md) rules out a rescue and a flashback, and points at the scenes that carry what it won't. That is the section the standard leans on hardest, in a medium that has never had a place to write it down.
