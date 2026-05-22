---
title: "Angular Clean Code Tip: Stop Direct Parent-Child Communication"
summary: "Kirill Ushakov recommends minimizing direct parent-child component communication in Angular apps, favoring state management libraries like NGXS to share and update data."
type: summary
sources:
  - 001a-raw/transcripts/kirill-ushakov-2026-05-21.md
tags:
  - angular
  - state-management
  - clean-code
  - component-architecture
created: "2026-05-21T12:00:00Z"
updated: "2026-05-21T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Angular Clean Code Tip: Stop Direct Parent-Child Communication

## Summary

Kirill Ushakov advises Angular developers to minimize direct communication between parent and child components. Instead of passing data directly between components, he recommends relying on a state management library like NGXS to serve as the single source of truth for sharing and updating application state.^[001a-raw/transcripts/kirill-ushakov-2026-05-21.md]

## Key Takeaways

- **Avoid direct parent-child communication** — component-to-component data passing creates tight coupling and makes the app harder to maintain^[001a-raw/transcripts/kirill-ushakov-2026-05-21.md]
- **Use state management as the intermediary** — NGXS (or similar libraries) centralizes state, decoupling components from each other^[001a-raw/transcripts/kirill-ushakov-2026-05-21.md]
- **Components read and write through state** — rather than emitting events to parents or passing inputs down through multiple layers

## Related

- [[concepts/deployment-patterns|Deployment Patterns]]
- [[concepts/observability|Observability]]
