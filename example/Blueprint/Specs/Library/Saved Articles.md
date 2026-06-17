---
id: saved-articles
title: Saved Articles
type: feature
domain: Library
status: Intake
created: 2026-06-16
modified: 2026-06-17
eidos_version: 2.0.0
owner: brenton
depends_on: [session-management]
tags: [capture, reading]
---

# Saved Articles

## Intent

The whole product starts with a save. If capture is slow or a saved article later turns out to be broken or unreadable, the team stops trusting the library and goes back to pasting links in chat. This spec defines what saving an article means and what the team can count on afterward.

### Implementation Notes

Intend to acknowledge a save by persisting the URL synchronously, then hand fetching off to a background worker. The article record exists before its content does, so capture never blocks on the network.

## Open Questions & Assumptions

- How long should a snapshot be retained if the source goes offline?
- Should re-saving an existing article surface the existing one or create a personal reference to it?

## Behaviors & Acceptance Criteria

### Functional

- **AC1:** A user saves an article by submitting its URL, from the extension or a paste box.
- **AC2:** The save is recorded immediately and acknowledged before content is fetched.
- **AC3:** The system fetches a readable snapshot of the article and stores it with the save.
- **AC4:** A saved article appears in the whole team's library, attributed to who saved it.
- **AC5:** If the same URL is saved again by the team, it is recognized rather than duplicated.
- **AC6:** If fetching fails, the article still appears, flagged as unreadable, with the original link preserved.

### Performance

- **AC7:** The save acknowledgment (AC2) returns without waiting on the fetch.

### Quality attributes

- **AC8:** Fetched content is sanitized before storage; article sources are treated as untrusted input.

## Out of Scope

- Does not save PDFs, videos, or non-article pages in v1; URLs that aren't articles are kept as links only.
- Does not provide folders, tags, or full-text search yet.
- Does not capture private or paywalled content the fetcher can't reach.
- Does not sync to external read-it-later services.

## Dependencies

- **Session Management** (`depends_on: session-management`) — a save is attributed to the signed-in user who made it.
- An article fetcher/extractor that produces the readable snapshot in AC3.
- Object storage for the stored snapshots.

## Testing

- AC1–AC4: a save-and-list integration test asserts immediate acknowledgment and later snapshot availability.
- AC5: save a duplicate URL and assert a single record.
- AC6/AC8: with a failing or hostile fetch fixture, the save survives flagged unreadable, and malicious markup is stripped from any stored content.

## Constraints & Decisions

- A failed fetch must never lose the user's original URL.

<!-- append-only; date optional but recommended -->

- 2026-06-16: Acknowledge the save before fetching, so capture always feels instant. (brenton)
- 2026-06-16: Failed fetches degrade to a link rather than rejecting the save. (brenton)
