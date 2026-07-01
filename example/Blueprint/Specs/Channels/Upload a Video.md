---
id: upload-a-video
title: Upload a Video
summary: publish a source file to a channel; accepted fast, processed reliably.
type: feature
domain: Channels
status: Intake
date_created: 2026-06-20
date_modified: 2026-06-23
owner: Brenton
depends_on: [transcode-pipeline]
connects_to: ["[Watch a Video](../Playback/Watch%20a%20Video.md)"]
tags: [channels, publishing]
beta: true
---

# Upload a Video

## Intent

Publishing is the creator's core action. If an upload is fragile, or a video won't play on some device, creators leave for a platform that "just works." This defines what uploading means and what a creator can count on — accepted fast, processed reliably, published when ready.

### Assumptions

Assuming a single client→ingest upload is good enough for this cut — no resumable or multipart upload for very large files yet.

### Implementation Notes

The client sends a source file to the ingest endpoint; a background pipeline transcodes it into the streaming renditions and publishes to the catalog when ready. Acceptance is decoupled from processing so a large file or a slow transcode never blocks the creator.

## Open Questions

- What is the largest source file and longest duration accepted in this cut?
- If transcoding fails partway, does the creator get a retry, or a clear failure with the source preserved?

## Behaviors & Acceptance Criteria

### Functional

- **AC1:** A creator uploads a source file to their channel, with a title and description.
- **AC2:** The upload is accepted and acknowledged before transcoding finishes.
- **AC3:** The pipeline transcodes the source into the renditions the player needs.
- **AC4:** When processing completes, the video is published to the creator's channel and is watchable.
- **AC5:** The creator can see processing status — processing, ready, or failed.

### Quality attributes

- **AC6:** Source uploads are treated as untrusted input — validated and sandboxed before processing.
- **AC7:** A failed transcode preserves the creator's source and surfaces the failure rather than losing the upload.

## Out of Scope

- Does not trim, edit, or enhance video.
- Does not schedule publishing or set visibility tiers beyond published / not.
- No monetization, automatic captions, or generated thumbnails.
- No Shorts or live ingest.

## Dependencies

- A **transcode pipeline** that produces the streaming renditions — no spec of its own here, so it rides in `depends_on` as `transcode-pipeline`.
- Object storage for the source file and the renditions.
- The channel catalog the published video attaches to.

## Testing

- AC1–AC4: upload a fixture source, assert immediate acknowledgment and later a published, watchable video.
- AC5: assert status transitions through processing → ready.
- AC6/AC7: with a hostile or corrupt source, assert it is sandboxed, and that a failure preserves the source and reports clearly.

## Constraints & Decisions

- Acceptance is decoupled from transcoding, so publishing never blocks on processing.
- A failed transcode must never lose the creator's original upload.

<!-- append-only; date optional but recommended -->

- 2026-06-20: Accept-then-process, rather than blocking the creator on the transcode. (Brenton)
