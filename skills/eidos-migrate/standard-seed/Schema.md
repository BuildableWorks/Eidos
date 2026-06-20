# Schema

The property contract for this registry — what a spec's frontmatter must and may carry. Skills read this file to author and validate specs. Two parts: the properties Eidos defines, and the ones you add.

A property's `type` is drawn from the set Obsidian uses — Text, List, Number, Checkbox, Date, Date & time — so this registry's frontmatter renders natively in an Obsidian vault. Anything that wants more structure than one of those almost belongs in the body (a shape), not in a property.

## Eidos Canonical

_Managed by the standard (Eidos 3.1.0). `eidos-migrate` rewrites this block on a version change — don't hand-edit it._

| name       | type | required | meaning                                                                                       |
| ---------- | ---- | -------- | --------------------------------------------------------------------------------------------- |
| id         | Text | yes      | Stable, unique, kebab-case identity. Assigned once, never renamed. References point at it.     |
| title      | Text | yes      | Human-readable name. Rename freely.                                                            |
| type       | Text | yes      | Open, soft label. Drives views, never structure. e.g. feature, capability, domain, integration. |
| domain     | Text | yes      | The grouping, matching its folder under Specs/ in the registry's naming convention. An unknown domain warns, not fails. |
| status     | Text | yes      | Lifecycle value: Draft / Intake / In Progress / Done / Archived / Deprecated. Off-list warns.   |
| created    | Date | yes      | YYYY-MM-DD. The day the spec was first written. Set once.                                       |
| modified   | Date | yes      | YYYY-MM-DD. The day the spec was last changed.                                                  |
| owner      | Text | no       | Who answers questions about this spec.                                                          |
| depends_on | List | no       | Specs this one needs, each a markdown link to that spec.                                        |
| tags       | List | no       | Free tags.                                                                                      |

## Custom Registry Properties

_Yours to define. Add a property with the `eidos-property` skill — it presses for name, type, required, and meaning, then backfills the existing specs. This block is preserved across migration._

<!-- None yet. A row takes the same shape as the canonical ones, e.g.:

| name | type | required | meaning |
| ---- | ---- | -------- | ------- |
| team | Text | no       | Owning team, for filtering. |

-->
