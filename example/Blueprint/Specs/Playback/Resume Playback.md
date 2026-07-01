---
id: resume-playback
title: Resume Playback
summary: remember where each viewer left off, and offer to resume.
type: feature
domain: Playback
flavor: micro
status: Draft
date_created: 2026-06-22
date_modified: 2026-06-23
owner: Brenton
depends_on:
  - "[Watch a Video](Watch%20a%20Video.md)"
connects_to:
  - "[Watch a Video](Watch%20a%20Video.md)"
tags: [playback]
beta: false
---

# Resume Playback

## Intent

People watch long videos in more than one sitting, and across devices. If reopening a video always starts at zero, the viewer loses their place and drops off. This remembers where each viewer stopped and offers to pick up there. It's a **micro** spec on purpose — the smallest useful definition, written to grow into the full flavor once it earns its place.

### Assumptions

Position is per-viewer and follows them across devices via their account, not stored only on one device. Unconfirmed.

## Open Questions

- How precise should a remembered position be — to the second, or near enough to feel right after a re-watch?

## Behaviors & Acceptance Criteria

- **AC1:** As a signed-in viewer watches, their furthest-watched position for that video is remembered.
- **AC2:** Reopening a video they've partly watched offers to resume from that position, or to start over.
- **AC3:** Playback position is per-viewer, never shared, and absent for a signed-out viewer.

## Out of Scope

- Does not store position for signed-out viewers (no account to attach it to).
- No watch-history surface or per-second analytics — just the resume point.
