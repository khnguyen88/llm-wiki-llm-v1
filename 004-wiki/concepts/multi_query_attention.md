---
title: "Multi-Query Attention (MQA)"
summary: An attention variant using a single key-value head shared across all query heads, maximizing inference speed at the cost of some quality degradation
type: concept
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - attention
  - kv-cache
  - inference
  - transformers
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.85
provenance: inferred
---

# Multi-Query Attention (MQA)

An attention variant introduced by Shazeer (2019) that uses a single key-value head shared across all query heads. This is the most aggressive reduction of [[concepts/kv_cache|KV cache]] size, eliminating all KV head redundancy. It maximizes inference speed and minimizes memory bandwidth requirements but can degrade quality and training stability, especially in larger models.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Key Properties

- MQA is equivalent to GQA-1 (one group)
- Reduces KV cache to 2 x L x D (one KV head instead of H)
- Can cause quality degradation and training instability compared to MHA and GQA
- Used in PaLM 540B (48Q/1KV) and Falcon 40B (64Q/1KV)

## Relationship to Other Attention Variants

| Variant | KV Heads | Quality | Speed |
|---------|----------|---------|-------|
| MHA | H | Best | Slowest |
| GQA | G (1<G<H) | Near-MHA | Near-MQA |
| MQA | 1 | Degraded | Fastest |

For models at or above 7B parameters, [[concepts/grouped_query_attention|GQA-8]] is generally preferred over MQA as it provides near-MHA quality with most of MQA's speed benefits.

## Related

- [[concepts/kv_cache]]
- [[concepts/attention_mechanism]]
- [[concepts/grouped_query_attention]]
- [[summaries/adam-rosler-kv-cache-2026-05-12]]