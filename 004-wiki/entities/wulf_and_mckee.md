---
title: "Wulf and McKee"
summary: William A. Wulf and Sally A. McKee, who coined the term "memory wall" in their 1995 paper identifying the growing gap between processor and memory performance as the binding constraint on computing
type: entity
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - computer-architecture
  - memory-wall
  - history
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Wulf and McKee

William A. Wulf and Sally A. McKee, the computer architects who coined the term "memory wall" in their 1995 paper "Hitting the Memory Wall: Implications of the Obvious" (ACM SIGARCH Computer Architecture News, Vol. 23, Issue 1, pp. 20-24). They identified the growing gap between processor speed (improving at 75-80% per year) and DRAM speed (improving at only ~7% per year) as the fundamental bottleneck on computing performance.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Key Facts

- Paper published March 1995, cited ~1,329 times (original) and ~226 times (2004 follow-up)
- McKee published a 2004 follow-up "Reflections on the Memory Wall" at the 1st Conference on Computing Frontiers
- Their analysis showed average cycles per memory access would grow from 1.52 (2000) to 98.8 (2010) under conservative assumptions
- They noted all known mitigation techniques "provide one-time boosts to either bandwidth or latency" that delay but do not change the fundamentals
- Their prediction directly explains why GPU memory bandwidth (not compute) is the binding constraint on LLM inference cost

## Related

- [[concepts/memory_wall]]
- [[concepts/kv_cache]]
- [[summaries/adam-rosler-kv-cache-2026-05-12]]