# {{Product}}

> **Start here.** This is the project for **{{Product}}**: the source of truth for what this
> program asks and what would count as an answer, true whether or not a single study has run.

{{One line: the question this program exists to answer.}}

## Top-level documents

_Your own one-of-a-kind docs: a Preregistration, a Data Management Plan, an Ethics Approval, a Bibliography. Add them here as you write them._

## Folders

- **[Frames](frames/)**: what every investigation is judged against: the Question, Prior Work, Method, and Ethics.
- **[Investigations](investigations/)**: the lines of inquiry, in folders that nest: a strand, its studies, and the experiments in each.
- **[Decisions](decisions/)**: the method, analysis, scope, and ethics calls, and every deviation from a plan, each proposed and then signed off.
- **[Backlog](backlog/)**: the work that serves the investigations (runs, analyses, literature reviews, drafts, reviews), one task each, on a board.
- **[Data](data/)**: small datasets, codebooks, and data dictionaries; raw data that is large or sensitive stays in its governed store, linked by URL.
- **[Figures](figures/)**: figures, diagrams, and slides, a figure with its data and script kept together as a bundle.
- **[Literature](literature/)**: the papers and preprints Prior Work cites.

## How to use it

An investigation here describes what is being asked and what would settle it. It is not a lab
notebook, a protocol, or a task list: the calls a notebook would log go in Decisions, and the runs
go on the Backlog. Write the question, the prediction, and the falsifier before the work, and keep
them true after. An investigation that comes back `Inconclusive` or `Abandoned` stays here, because
the question and the attempt are both part of what the program knows.

---

_An Eidos project. Its framework lives in [`.eidos/`](.eidos/); `eidos check` validates it and `eidos index` keeps the index current._
