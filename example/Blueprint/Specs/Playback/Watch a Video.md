---
id: watch-a-video
title: Watch a Video
summary: play a video reliably, signed in or not, adapting to the connection.
type: feature
domain: Playback
status: Intake
date_created: 2026-06-20
date_modified: 2026-06-23
owner: Brenton
depends_on: [video-catalog, cdn-delivery]
tags: [playback]
beta: true
---

# Watch a Video

## Intent

A view is the core action of the whole product. If a video is slow to start or stalls, the viewer leaves — so what "playing a video" means, and what a viewer can count on, is the first thing to pin down. It must hold whether the viewer is signed in or arrived from a shared link.

### Assumptions

Assuming adaptive-bitrate delivery over the CDN is available and affordable at launch scale — if it isn't, the whole playback approach changes.

### Implementation Notes

Intend to use adaptive-bitrate streaming served from the CDN. The catalog hands the player short-lived **signed segment URLs**; the app server never proxies video bytes. Quality is chosen by the player from the connection, not by the viewer.

## Open Questions

- How long should a signed playback URL stay valid before it has to be refreshed?
- Does a view count on play start, or only after a watch-time threshold (to resist inflation)?

## Behaviors & Acceptance Criteria

### Functional

- **AC1:** A viewer opens a video and the player loads with its title, channel, and controls.
- **AC2:** The viewer can play, pause, and seek anywhere within the video.
- **AC3:** A signed-out viewer who opens a shared link can still watch.
- **AC4:** For a signed-in viewer, playback offers to resume from their saved position (see [Resume Playback](Resume%20Playback.md)).

### Performance

- **AC5:** Playback starts within a couple of seconds on a normal connection.
- **AC6:** Quality adapts to the connection automatically, without the viewer choosing a resolution.

### Quality attributes

- **AC7:** A stalled segment recovers by dropping quality rather than stopping playback.
- **AC8:** A view is counted at most once per viewer per video within a window — replays and seeks don't inflate it.

## Out of Scope

- No comments, ratings, or next-up recommendations on the watch page.
- No offline download or background audio.
- No live playback or a Shorts-style vertical feed.

## Dependencies

- A **video catalog** for metadata and signed URLs, and **CDN delivery** for the bytes — neither has a spec here, so they ride in `depends_on` as `video-catalog` and `cdn-delivery`.
- [Resume Playback](Resume%20Playback.md) — supplies the position AC4 resumes from.

## Testing

- AC1–AC4: an integration test loads a video, asserts the player and controls, exercises play/pause/seek, and confirms a signed-out link still plays.
- AC5–AC6: measure start time and assert the player steps quality down on a throttled connection rather than stalling.
- AC8: replay and seek a single video and assert the view count increments once.

## Constraints & Decisions

- The app server never serves video bytes — delivery is the CDN's, via signed URLs.
- Playback must not hard-stop on a slow segment; degrade quality first.

<!-- append-only; date optional but recommended -->

- 2026-06-20: Adaptive bitrate from the CDN, not a fixed resolution chosen by the viewer. (Brenton)
