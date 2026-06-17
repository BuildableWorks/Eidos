---
id: session-management
title: Session Management
type: feature
domain: Identity
status: Intake
created: 2026-06-16
modified: 2026-06-17
eidos_version: 2.0.0
owner: brenton
depends_on: [magic-link-signin]
tags: [auth, session]
---

# Session Management

## Intent

Once a user has proven control of their email, asking them to do it again on every visit would defeat the point of low-friction sign-in. A session lets a signed-in user keep working across visits and devices, and lets them end that access when a device is lost or shared.

### Implementation Notes

Intend to keep sessions as server-side records keyed by an opaque cookie token. Revocation deletes the record so the next request fails closed, rather than relying on a client-side expiry the server can't retract.

## Open Questions & Assumptions

- Should ending all sessions also invalidate any unused magic links?
- What inactivity window balances safety against re-sign-in friction?

## Behaviors & Acceptance Criteria

### Functional

- **AC1:** A successful sign-in starts a session bound to the browser that completed it.
- **AC2:** A session persists across visits until it expires or is ended.
- **AC3:** A user can see their active sessions and end any one of them.
- **AC4:** Ending a session immediately revokes access for that device.
- **AC5:** Sessions expire after a period of inactivity.

### Quality attributes

- **AC6:** Session identifiers are not guessable, and a session identifier cannot be reused after the session ends.

## Out of Scope

- Does not provide "remember this device" or trusted-device skipping of sign-in.
- Does not manage team membership or permissions; that is a separate concern.
- Does not offer single sign-on or third-party identity providers.

## Dependencies

- **Magic Link Sign-In** (`depends_on: magic-link-signin`) — currently the only way a session is started.
- A session store that supports immediate deletion, for the revocation in AC4.

## Testing

- AC1–AC5: a session-lifecycle integration test signs in, persists across requests, ends the session, and asserts access is gone.
- AC4: assert a revoked session fails on the very next request, not at next expiry.
- AC6: attempt to reuse an ended session identifier and confirm it is rejected.

## Constraints & Decisions

- Revocation must take effect on the next request, not at the next expiry — sessions fail closed.

<!-- append-only; date optional but recommended -->

- 2026-06-16: Inactivity expiry over fixed-lifetime sessions, to match infrequent readers. (brenton)
