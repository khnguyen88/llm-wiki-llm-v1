---
title: "PagedAttention"
summary: An attention algorithm that applies OS-style virtual memory paging to KV cache management, eliminating fragmentation and enabling copy-on-write sharing across requests
type: concept
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - kv-cache
  - memory-management
  - inference
  - vllm
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.85
provenance: inferred
---

# PagedAttention

An attention algorithm introduced by Kwon et al. (SOSP 2023) as the core of vLLM that applies operating system-style virtual memory paging to [[004-wiki/concepts/kv_cache|KV cache]] management. Instead of allocating contiguous memory for each request's KV cache (causing 13-57% internal fragmentation and 8-38% external fragmentation), PagedAttention divides the cache into fixed-size blocks (pages) that can be placed non-contiguously in physical memory, using block tables for indirection.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Key Benefits

- Near-zero internal fragmentation (waste limited to at most one block per request)
- Zero external fragmentation (all blocks are the same fixed size)
- On-demand allocation (new blocks allocated only when needed, not pre-reserved)
- Memory sharing via copy-on-write across parallel samples, beam search candidates, and shared prefixes

## Performance

PagedAttention achieves 96.3% useful KV storage compared to 20-38% in prior systems with contiguous allocation. Despite ~20-26% higher per-kernel attention latency, end-to-end throughput is 2-4x higher because far more requests can be batched simultaneously.

## Analogy with OS Concepts

| OS Concept | PagedAttention Analog |
|-----------|----------------------|
| Pages | Blocks (fixed-size KV cache units) |
| Bytes | Tokens |
| Processes | Requests |
| Page tables | Block tables (logical-to-physical mapping) |
| Copy-on-write | Shared prefix blocks across requests |

## Related

- [[004-wiki/concepts/kv_cache]]
- [[004-wiki/concepts/memory_wall]]
- [[004-wiki/summaries/adam-rosler-kv-cache-2026-05-12]]