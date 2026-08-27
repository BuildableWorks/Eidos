# Examples

Two filled-in Eidos definitions to read and pattern-match against. They are deliberately different
kinds of thing, because that is the claim Eidos makes: `Specs` and `domains` are the default seed, not
the essence, and every skill works the same way across both.

| Example | What it defines | Seed | Collections |
| --- | --- | --- | --- |
| [`Blueprint/`](Blueprint) | a small subset of **YouTube** — watching and resuming videos, running and following a channel | `software` | `Frames` · `Specs` by domain |
| [`Screenplay/`](Screenplay) | **The Salt Road**, a short film about a cartographer who can no longer read her own maps | `book`, reshaped | `Frames` · `Scenes` by act |

For what the pieces _are_ — framework and definition, top-level docs, collections, shapes, flavors,
Schema, personas — see the [root README](../README.md) and [`EIDOS.md`](../EIDOS.md). This file just
walks the two.

To start your own definition, run the `eidos-install` skill and pick a [seed](../seeds) — don't copy
either of these.

---

## `Blueprint/` — a subset of YouTube

The software case, and the one `EIDOS.md` teaches from. `Blueprint` is the default root name; nothing
points at it by path, so a definition may call its root anything.

```
Blueprint/                 # the definition
  README.md                # the definition's own "start here" front door
  _eidos/                  # the framework (hidden): shapes, personas, Framework (index + config + Schema), user, .gitignore
  Roadmap.md               # a custom top-level doc — free-form, no shape
  Frames/                  # the Frames collection — framing docs
    index.md               #   generated index of the collection
    Architecture.md  Audience.md  Criteria.md  Market.md
  Specs/                   # the default collection
    index.md               #   generated index of the collection
    Playback/              #   ┐ domains — the Specs collection's grouping
      Watch a Video.md     #   │
      Resume Playback.md   #   │ (flavor: micro)
    Channels/              #   ┘
      Subscribe to a Channel.md
      Upload a Video.md
```

What to notice:

- The **Frames collection** ([Architecture](Blueprint/Frames/Architecture.md), [Audience](Blueprint/Frames/Audience.md), [Criteria](Blueprint/Frames/Criteria.md), [Market](Blueprint/Frames/Market.md)) frames the product — one framing doc per flavor, listed in the generated [`Frames/index.md`](Blueprint/Frames/index.md); [Roadmap](Blueprint/Roadmap.md) is a custom top-level doc this definition added.
- The **Specs collection** holds the units, grouped into the **Playback** and **Channels** domains, listed in the generated [`Specs/index.md`](Blueprint/Specs/index.md).
- It offers two **flavors** — `spec.full` (default) and `spec.micro`. [Resume Playback](Blueprint/Specs/Playback/Resume%20Playback.md) carries `flavor: micro`, so it's checked against the lighter shape.
- [`_eidos/Framework.md`](Blueprint/_eidos/Framework.md), in its `## Schema` section (`### Custom Properties`), adds one **custom property**, `beta` — a framework extending the baseline without forking the standard.
- [`_eidos/personas/`](Blueprint/_eidos/personas) holds the **response contracts**, and [`_eidos/user.md`](Blueprint/_eidos/user.md) names the **actor** (here a technically-fluent Framework Owner). `user.md` is normally gitignored; it's committed here only to show its shape.

---

## `Screenplay/` — The Salt Road

The other end of the range. Nothing here is called a spec, and the definition still validates,
indexes, and maps identically.

```
Screenplay/                # the definition — a custom root name
  README.md
  _eidos/                  # the framework: scene + frame shapes, two personas, Framework, user, .gitignore
  Framework Map.canvas     # a generated top-level doc — the canvas
  Frames/
    index.md
    Premise.md  Voice.md  Audience.md  Market.md
  Scenes/                  # the units — not "Specs"
    index.md
    Act I/                 #   ┐ acts — the Scenes collection's grouping
      Cold Open.md         #   │
      The Commission.md    #   │
    Act II/                #   ┘
      The Crossing.md
      What She Says.md     #     (flavor: beat)
```

What to notice:

- It started from the [`book`](../seeds/book) seed and was **reshaped**: `Chapters` → `Scenes`, `part` → `act`, chapter shapes → scene shapes, and a new `pov` property. The standard was not forked, and `eidos-configure` is how you'd do it. That reshaping is the normal case, not a special one.
- The Scenes collection declares **`Canvas: card from ## Logline`** in [`_eidos/Framework.md`](Screenplay/_eidos/Framework.md). The canvas embeds that section because the framework says so — no generator knows a collection or a section by name.
- **Grouping is the collection's own.** `act` here does exactly what `domain` does under `Specs`, and `Frames` groups by nothing at all.
- [What She Says](Screenplay/Scenes/Act%20II/What%20She%20Says.md) carries `flavor: beat` — the film's ending, deliberately thin, because the decision hasn't been made. A definition is allowed to be honest about that; a task list isn't.
- **Out of Scope is doing real work.** [The Crossing](Screenplay/Scenes/Act%20II/The%20Crossing.md) rules out a rescue and a flashback, and points at the scenes that carry what it won't. That is the section the standard leans on hardest, in a medium that has never had a place to write it down.
