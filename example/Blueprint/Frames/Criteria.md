---
id: criteria
title: Criteria
summary: budget, scope objectives, and timeline that decide and audit scope.
type: frame
flavor: criteria
status: Done
created: 2026-06-16
modified: 2026-07-01
tags: [eidos, product, criteria]
---

# Criteria

## Budget

A staffed product bet, not a side project: a small cross-functional team (a few engineers, a designer, a PM) with real infrastructure spend on transcoding and CDN egress. Egress is the dominant cost and scales with watch time, so the build optimizes delivery before features.

## Scope Objectives

The objective for this cycle is a **watchable, publishable core**: a creator can upload to a channel, a viewer can watch reliably and resume, and viewers can subscribe. That ceiling rules out anything outside watch / publish / subscribe — no recommendation feed, no comments, no ads, no Shorts, no live. Each is a major surface of its own and would pull scope past a coherent first cut.

## Timeline

Private beta with a small set of invited creators and their audiences first; open signups gated on the pipeline holding up under real upload volume, not on a date. Transcoding and delivery lead the rest, because nothing else is watchable until they are solid.

## Parameters & Variables

- **Transcode pipeline throughput** — upload-to-watchable latency under load sits on the critical path; if it can't keep up, open signups slip.
- **CDN egress cost** — the dominant variable cost; a pricing change or a watch-time spike reshapes the budget directly.
- **Content policy & moderation capacity** — opening uploads broadly depends on moderation being in place; it gates how wide the beta can go.
- **A mobile client** — if mobile lands this cycle, signed-out link playback and resume matter much more; if it slips, the web player carries the beta.
