# Seeds

The starting frameworks Eidos ships. A seed is a complete `.eidos/` (templates, roles, `Framework.yaml`, `me.md`, `.gitignore`) plus a root `README.md`; `eidos init` installs the one you pick. Reshape it from there.

| Seed | For | Folders |
| --- | --- | --- |
| [`software/`](software) | a product, service, or system being built | `Frames` (architecture, audience, criteria, market) · `Specs` by domain · `assets` |
| [`book/`](book) | a book, long-form argument, or course | `Frames` (premise, reader, voice, market) · `Chapters` by part · `assets` |
| [`research/`](research) | a question, a study, or a programme of inquiry | `Frames` (question, prior work, method, ethics) · `Investigations` by strand · `assets` |

```txt
<seed>/
  roles/           # response contracts, one per role
  templates/       # body templates, <unit>.<variant>.md
  .gitignore       # keeps me.md and plugins/*/local.yaml out of version control
  Framework.yaml   # the framework document
  me.md            # blank; who is in the seat (personal)
  README.md        # the {{Product}} front door, installed at the root
```

Nothing in Eidos knows a folder by name: `software` is the default, and the other two run the same machinery under different words. None fit? Start from the nearest and reshape it with the `eidos` CLI.
