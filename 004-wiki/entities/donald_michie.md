---
title: "Donald Michie"
summary: British computer scientist who coined "memoization" in 1968, proposing that functions cache their results rather than recompute them -- the theoretical foundation underlying KV cache in transformer inference
type: entity
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - computer-science
  - memoization
  - history
  - ai-pioneers
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Donald Michie

British computer scientist who coined the term "memoization" in his 1968 paper "'Memo' Functions and Machine Learning" published in Nature (Vol. 218, pp. 19-22). The term derives from "memorandum" ("to be remembered"), proposing that functions should maintain both a "rule part" (computational procedure) and a "rote part" (lookup table).^[raw/transcripts/adam-rosler-2026-05-12.md]

## Key Facts

- Proposed memoization in 1968 as a technique where each evaluation adds a fresh entry to the cache
- Connected memoization to machine learning, building on A.L. Samuel's 1959 checkers program
- Robin Popplestone implemented Michie's memo function facility in POP-2
- Preliminary tests showed memoized programs running 10-20x faster after 200 successive calls
- Cited 322+ times according to Google Scholar
- The concept directly underpins [[004-wiki/concepts/kv_cache|KV cache]] in transformer inference

## Related

- [[004-wiki/concepts/memoization]]
- [[004-wiki/concepts/kv_cache]]
- [[004-wiki/summaries/adam-rosler-kv-cache-2026-05-12]]