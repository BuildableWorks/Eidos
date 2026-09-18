# Seeds

The starting frameworks Eidos ships. A seed is a root: a complete `.eidos/` (templates, roles, `Framework.yaml`, `me.md`, `.gitignore`), every folder it declares, and a `README.md`. It is exactly what `eidos init` produces from it, so it can be checked in place and published to the Eidos Registry as a package by path (`seeds/software` and so on). `eidos init` installs the one you pick. Reshape it from there.

| Seed | For | Folders |
| --- | --- | --- |
| [`software/`](software) | a product, service, or system being built | `Frames` (architecture, audience, criteria, market) · `Specs` by domain · `assets` |
| [`book/`](book) | a book, long-form argument, or course | `Frames` (premise, reader, voice, market) · `Chapters` by part · `assets` |
| [`research/`](research) | a question, a study, or a programme of inquiry | `Frames` (question, prior work, method, ethics) · `Investigations` by strand · `assets` |

```txt
<seed>/
  .eidos/            # the framework
    roles/           #   response contracts, one per role
    templates/       #   body templates, <unit>.<variant>.md
    .gitignore       #   keeps me.md and plugins/*/local.yaml out of version control
    Framework.yaml   #   the framework document
    me.md            #   blank; who is in the seat (personal)
  <Collection>/      # every folder Framework.yaml declares, empty but for a .gitkeep
  assets/
  README.md          # the {{Product}} front door
```

The declared folders ship empty: an installer scaffolds the blueprints. Each seed's `.eidos/.gitignore` ignores the `me.md` beside it, so in this repository the blank `me.md` is force-added (`git add -f`, which `scripts/sync-skills.sh` does) rather than left out.

Nothing in Eidos knows a folder by name: `software` is the default, and the other two run the same machinery under different words. None fit? Start from the nearest and reshape it with the `eidos` CLI.
