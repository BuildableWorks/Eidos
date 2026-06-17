---
type: system
title: Architecture
tags: [eidos, product, architecture]
created: 2026-06-16
modified: 2026-06-17
eidos_version: 2.0.0
---

# Architecture

## Shape

Marginalia is a single web application backed by one relational database. A user signs in by email, saves articles from anywhere via a browser extension or a paste box, and the app fetches and stores a readable copy. Teams share a library; members annotate and reply. The whole system is a Rails-style monolith behind a CDN, with a background worker for article fetching.

## Components

- **Web app** — server-rendered pages plus a thin client for inline annotation. Owns sessions, rendering, and all user-facing routes.
- **Article fetcher** — a background worker that retrieves a URL, extracts readable content, and stores a snapshot. Isolated so a slow or hostile site can't block a request.
- **Library store** — the relational database: users, teams, saved articles, annotations, and replies.
- **Browser extension** — a small client that posts a URL to the save endpoint. No logic beyond capture and auth handoff.

## Data and flow

A save request carries a URL and a session. The web app records the article row, enqueues a fetch job, and returns immediately. The fetcher resolves the URL, extracts content, and writes the snapshot back. Reads (library, article, thread) are served directly from the store. Annotations write straight through; there is no eventual-consistency layer.

## Boundaries and dependencies

- **Email delivery** is external (a transactional email provider); sign-in depends on it.
- **Article source sites** are untrusted third parties; the fetcher treats every response as hostile input.
- The browser extension depends on the web app's save and auth endpoints; it ships on each browser's store on that store's review cadence.
