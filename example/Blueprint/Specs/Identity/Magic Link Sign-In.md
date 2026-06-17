---
id: magic-link-signin
title: Magic Link Sign-In
type: feature
domain: identity
status: proposed
last_validated: 2026-06-16
owner: brenton
depends_on: [email-delivery]
implements: passwordless-auth
supersedes: []
serves_job: "access my account without remembering a password"
activity: getting-started
tags: [auth, onboarding]
---

# Magic Link Sign-In

## Intent

Passwords are the largest source of sign-in friction and the largest support cost in
account recovery. Users who sign in rarely forget their password almost every time,
then abandon or open a ticket. Magic links let a returning user prove control of
their email and get in, with nothing to remember.

## Behavior

- A user enters their email and requests a link.
- The system sends a single-use link to that address.
- Following the link within its validity window signs the user in and starts a session.
- Requesting a new link invalidates any previous unused link for that address.
- An unknown email produces the same response as a known one, so the form does not
  reveal who has an account.

## Out of Scope

- Does not support SMS or authenticator-app delivery. Email only.
- Does not remember devices or offer "stay signed in" beyond the normal session.
- Does not replace password sign-in; it sits alongside it.
- Does not handle account creation. Unknown emails do not silently register.

## Constraints

- Link validity window short enough to limit exposure if an inbox is compromised.
- Sign-in must complete without the user leaving their email client and a browser.
- Same-response-for-unknown-email must not be defeatable by timing.

## Open Questions

- What happens when a link is opened on a different device than it was requested
  from? Allow, block, or warn?
- Should an active session be required to remain on the original device?

## Decisions

<!-- append-only, dated, one line each -->
- 2026-06-16: Email-only for v1; SMS rejected on carrier cost and deliverability. (brenton)
- 2026-06-16: New link invalidates prior unused link, rather than allowing several live at once. (brenton)
