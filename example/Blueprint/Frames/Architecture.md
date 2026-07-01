---
id: architecture
title: Architecture
summary: the YouTube subset as a built system, the one entry door.
flavor: architecture
status: Done
date_created: 2026-06-16
date_modified: 2026-07-01
owner: Brenton
tags: [eidos, product, architecture]
---

# Architecture

## Shape

This registry defines a **small subset of YouTube**: watching videos, resuming where you left off, running a channel, and subscribing to one. It is a web and mobile client over a handful of services — a catalog of videos and channels, an upload-and-transcode pipeline, a CDN that delivers the bytes, and a per-viewer store for playback state. The recommendation feed, comments, ads, and Shorts are deliberately out of this subset.

## Components

- **Client + player** — the web and mobile app. Owns the watch page, the player (play/pause/seek, quality), the channel page, and sign-in. Plays adaptive streams; it does not store video.
- **Catalog** — the source of truth for videos and channels: titles, descriptions, ownership, subscription edges, view counts.
- **Upload & transcode pipeline** — ingests a creator's source file, transcodes it into the streaming renditions, and publishes the result to the catalog when ready. Asynchronous by design.
- **Delivery (CDN)** — serves the transcoded segments to the player from the edge. The catalog hands the player signed URLs; the bytes never touch the app server.
- **Playback store** — per-viewer state: the furthest-watched position per video, for [Resume Playback](../Specs/Playback/Resume%20Playback.md).

## Data and flow

A watch starts with the client asking the catalog for a video; the catalog returns metadata plus signed CDN URLs, and the player streams segments from the edge, adapting quality to the connection. An upload runs the other way: the client sends a source file to the pipeline, which transcodes asynchronously and writes the finished renditions back to the catalog, flipping the video to published. Subscriptions and playback position are small writes straight to the catalog and the playback store.

## Boundaries and dependencies

- **Video delivery** is the CDN's job; the app never streams bytes itself, and a slow edge degrades quality, not availability.
- **Transcoding** is a background concern — a creator's upload is accepted before it is watchable, and the pipeline can be slow without blocking the client.
- **Source uploads** are untrusted input: the pipeline validates and sandboxes every file.
