---
id: saved-articles
title: Saved Articles
type: feature
domain: library
status: proposed
last_validated: 2026-06-16
owner: brenton
depends_on: [session-management]
implements:
supersedes: []
serves_job: "save an article in one click and trust it's there to read later"
activity: core-loop
tags: [capture, reading]
---

# Saved Articles

## Intent

The whole product starts with a save. If capture is slow or a saved article later
turns out to be broken or unreadable, the team stops trusting the library and goes
back to pasting links in chat. This spec defines what saving an article means and
what the team can count on afterward.

## Behavior

- A user saves an article by submitting its URL, from the extension or a paste box.
- The save is recorded immediately and acknowledged before content is fetched.
- The system fetches a readable snapshot of the article and stores it with the save.
- A saved article appears in the whole team's library, attributed to who saved it.
- If the same URL is saved again by the team, it is recognized rather than duplicated.
- If fetching fails, the article still appears, flagged as unreadable, with the
  original link preserved.

## Out of Scope

- Does not save PDFs, videos, or non-article pages in v1; URLs that aren't articles
  are kept as links only.
- Does not provide folders, tags, or full-text search yet.
- Does not capture private or paywalled content the fetcher can't reach.
- Does not sync to external read-it-later services.

## Constraints

- The save acknowledgment must return without waiting on the fetch.
- Fetched content must be sanitized; article sources are untrusted input.
- A failed fetch must never lose the user's original URL.

## Open Questions

- How long should a snapshot be retained if the source goes offline?
- Should re-saving an existing article surface the existing one or create a personal
  reference to it?

## Decisions

<!-- append-only, dated, one line each -->
- 2026-06-16: Acknowledge the save before fetching, so capture always feels instant. (brenton)
- 2026-06-16: Failed fetches degrade to a link rather than rejecting the save. (brenton)
