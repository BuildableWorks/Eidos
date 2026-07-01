---
id: magic-link-signin
title: Magic Link Sign-In
type: feature
domain: Identity
status: Intake
created: 2026-06-11
modified: 2026-06-17
owner: Brenton
depends_on: [email-delivery]
tags: [auth, onboarding]
---

# Magic Link Sign-In

## Intent

Passwords are the largest source of sign-in friction and the largest support cost in account recovery. Users who sign in rarely forget their password almost every time, then abandon or open a ticket. Magic links let a returning user prove control of their email and get in, with nothing to remember.

### Assumptions

Assuming the existing `email-delivery` capability is reliable and fast enough to carry sign-in — if delivery is slow or flaky, magic links don't work.

### Implementation Notes

Intend to reuse the existing `email-delivery` capability rather than stand up a new sender. Tokens are single-use and held server-side, keyed to the email and looked up when the link is followed — the link carries an opaque token, not the identity — so an intercepted or logged link grants nothing after first use.

## Open Questions

- What happens when a link is opened on a different device than it was requested from? Allow, block, or warn?
- Should an active session be required to remain on the original device?

## Behaviors & Acceptance Criteria

### Functional

- **AC1:** A user enters their email and requests a link.
- **AC2:** The system sends a single-use link to that address.
- **AC3:** Following the link within its validity window signs the user in and starts a session.
- **AC4:** Requesting a new link invalidates any previous unused link for that address.

### Quality attributes

- **AC5:** An unknown email produces the same response as a known one — and the sameness is not defeatable by timing — so the form does not reveal who has an account.

## Out of Scope

- Does not support SMS or authenticator-app delivery. Email only.
- Does not remember devices or offer "stay signed in" beyond the normal session.
- Does not replace password sign-in; it sits alongside it.
- Does not handle account creation. Unknown emails do not silently register.

## Dependencies

- **Email delivery** (`depends_on: email-delivery`) — the transactional sender that puts the link in the user's inbox. Sign-in is only as reliable as it is.
- A session store to hold the session that AC3 starts.

## Testing

- AC1–AC4: an integration test requests a link, follows it, and asserts a live session; a negative test confirms an expired or superseded link fails.
- AC5: compare both the response body and the response timing for a known vs an unknown email; they must be indistinguishable.

## Constraints & Decisions

- The link validity window must be short enough to limit exposure if an inbox is later compromised.
- Sign-in must complete within the user's email client and a browser — no separate app step.

<!-- append-only; date optional but recommended -->

- 2026-06-11: Email-only for v1; SMS rejected on carrier cost and deliverability. (Brenton)
- 2026-06-11: New link invalidates prior unused link, rather than allowing several live at once. (Brenton)
