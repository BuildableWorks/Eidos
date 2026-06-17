---
id: session-management
title: Session Management
type: feature
domain: identity
status: proposed
last_validated: 2026-06-16
owner: brenton
depends_on: [magic-link-signin]
implements: passwordless-auth
supersedes: []
serves_job: "stay signed in across visits without re-proving who I am every time"
activity: getting-started
tags: [auth, session]
---

# Session Management

## Intent

Once a user has proven control of their email, asking them to do it again on every
visit would defeat the point of low-friction sign-in. A session lets a signed-in
user keep working across visits and devices, and lets them end that access when a
device is lost or shared.

## Behavior

- A successful sign-in starts a session bound to the browser that completed it.
- A session persists across visits until it expires or is ended.
- A user can see their active sessions and end any one of them.
- Ending a session immediately revokes access for that device.
- Sessions expire after a period of inactivity.

## Out of Scope

- Does not provide "remember this device" or trusted-device skipping of sign-in.
- Does not manage team membership or permissions; that is a separate concern.
- Does not offer single sign-on or third-party identity providers.

## Constraints

- Revocation must take effect on the next request, not on the next expiry.
- Session identifiers must not be guessable or reusable after end.

## Open Questions

- Should ending all sessions also invalidate any unused magic links?
- What inactivity window balances safety against re-sign-in friction?

## Decisions

<!-- append-only, dated, one line each -->
- 2026-06-16: Inactivity expiry over fixed-lifetime sessions, to match infrequent readers. (brenton)
