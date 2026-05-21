---
title: "Token Embedding"
summary: A vector of approximately 4,000 learned numbers representing each token in a transformer model, where semantic similarity between words corresponds to vector alignment measured by dot products
type: concept
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - embeddings
  - tokens
  - transformers
  - vector-similarity
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Token Embedding

A vector of approximately 4,000 learned numbers that represents each token inside a transformer model. When a prompt is sent, the model slices it into tokens and looks up each token's embedding from a giant table stored in the model file. Inside the model, the word "cat" is not text -- it is a list of 4,000 numbers.^[001a-raw/transcripts/adam-rosler-2026-05-12.md]

## Semantic Similarity

During pre-training, the model nudges embeddings until related concepts point in similar directions in the vector space. The dot product of two embedding vectors yields a single number: positive and large for aligned (related) concepts, zero for perpendicular (unrelated) concepts, and negative for opposite concepts. This means asking how related two words are reduces to checking how aligned their vectors are. Search engines have used vector similarity since the 1970s.^[001a-raw/transcripts/adam-rosler-2026-05-12.md]

## Role in Attention

Embeddings serve as the input to [[004-wiki/concepts/attention-mechanism|attention]], but they are cheap to compute (a simple lookup from a stored table). The expensive operation is the matrix multiplication that transforms each embedding into a key vector and a value vector for [[004-wiki/concepts/kv-cache|KV cache]]. This is why the KV cache stores the transformed K and V rather than the raw embeddings.^[001a-raw/transcripts/adam-rosler-2026-05-12.md]

## Related

- [[004-wiki/concepts/attention-mechanism]]
- [[004-wiki/concepts/kv-cache]]
- [[004-wiki/summaries/adam-rosler-kv-cache-2026-05-12]]