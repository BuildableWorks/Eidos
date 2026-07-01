---
id: subscribe-to-a-channel
title: Subscribe to a Channel
summary: follow a creator so their channel is yours to return to.
type: feature
domain: Channels
status: Intake
date_created: 2026-06-20
date_modified: 2026-06-23
owner: Brenton
tags: [channels]
beta: true
---

# Subscribe to a Channel

## Intent

Subscriptions turn a one-off watch into following a creator. Without them, every visit starts from scratch and creators have no durable audience. This defines what subscribing means and what each side can count on.

### Assumptions

Assuming a subscription is a flat viewer→channel follow — no tiers, memberships, or paid levels in this cut.

### Implementation Notes

A subscription is an edge from viewer to channel in the catalog. Counts are derived from the edges, not hand-maintained, and the write is idempotent so a double-tap can't double-subscribe.

## Open Questions

- Can a channel owner see who subscribed, or only the count?
- Are a viewer's subscriptions public by default, or private?

## Behaviors & Acceptance Criteria

### Functional

- **AC1:** A signed-in viewer subscribes to a channel from the channel page or a video.
- **AC2:** The viewer can unsubscribe, returning to the prior state.
- **AC3:** Subscribing is idempotent — subscribing twice leaves a single subscription.
- **AC4:** The channel's subscriber count reflects the change.

### Quality attributes

- **AC5:** A signed-out viewer is prompted to sign in, rather than silently failing to subscribe.

## Out of Scope

- Does not build the subscriptions feed or home surface (a separate unit).
- Does not send notifications on new uploads.
- No subscription tiers, memberships, or payments.

## Dependencies

- The channel catalog that owns channels and subscription edges.
- [Watch a Video](../Playback/Watch%20a%20Video.md) — subscribing is offered from the watch surface.

## Testing

- AC1–AC4: subscribe and assert the edge and count; unsubscribe and assert both revert; subscribe twice and assert a single edge.
- AC5: attempt to subscribe while signed out and assert the sign-in prompt.

## Constraints & Decisions

- Subscriber count is always derived from edges, never stored as a hand-updated number.

<!-- append-only; date optional but recommended -->

- 2026-06-20: Notifications split out of subscribing into their own future unit. (Brenton)
