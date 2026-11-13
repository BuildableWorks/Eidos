# {{title}}

_The overarching shape of the product as a built system. When the detail outgrows a single file, give it an `architecture` folder beside this doc in Frames, its docs following no template (the folder's default variant set to none), and keep this doc as the map that points into it. Link the system diagram from assets rather than describing it twice._

## Shape

_The system in one breath: the major pieces and how they fit. A paragraph or a simple sketch. Enough that a newcomer can hold the whole in their head before reading any spec._

## Components

_The named parts and what each is responsible for. One line to a short paragraph each. Boundaries matter more than internals here; this is the map, not the territory._

## Data and flow

_What moves through the system and where it lives. The path a request, a record, or an event takes from edge to store and back._

## Boundaries and dependencies

_Where this system ends and others begin. Outside services, platforms, and integrations it leans on. The seams where it could break or be swapped._
