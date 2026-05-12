---
title: "Memoization"
summary: An optimization technique coined by Donald Michie in 1968 where function results are cached rather than recomputed, serving as the theoretical foundation for KV cache in transformer inference
type: concept
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - memoization
  - caching
  - computer-science
  - inference
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Memoization

An optimization technique coined by Donald Michie in 1968 in his paper "'Memo' Functions and Machine Learning" (Nature, Vol. 218). The term derives from "memorandum" ("to be remembered"). Michie proposed that functions should have both a "rule part" (computational procedure) and a "rote part" (lookup table), with the machine deciding which to use based on expediency.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Core Principles

1. Each evaluation by rule adds a fresh entry to the rote (cache)
2. The rule vs. rote decisions are handled by the machine behind the scenes
3. Various interactions between rule and rote are permitted, including external updates to the rote and self-modifying rules

## Connection to Machine Learning

Michie connected memoization to machine learning, building on A.L. Samuel's 1959 checkers program which used "rote-learning" and "learning by generalization." Michie demonstrated memo functions with a factorial example: after computing `fact(3)=6`, all intermediate results are stored; a subsequent call to `fact(5)` only needs to compute two new values because `fact(3)=6` is already cached. In preliminary tests, memoized programs "learned" to evaluate standard numerical functions 10-20x faster after 200 successive calls.

## Connection to KV Cache

The [[concepts/kv_cache|KV cache]] in transformer inference is a direct application of memoization: the expensive matrix multiplications that transform embeddings into key and value vectors are computed once and cached, rather than recomputed on every generation step. Without memoization applied to attention, generation would cost roughly 1,000 times more compute.

## Related

- [[concepts/kv_cache]]
- [[entities/donald_michie]]
- [[summaries/adam-rosler-kv-cache-2026-05-12]]