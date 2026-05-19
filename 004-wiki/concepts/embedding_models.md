---
title: "Embedding Models"
summary: "LLMs that convert text into numerical vectors for storage, querying, and retrieval in vector databases; often paired with RAG workflows"
type: concept
sources:
  - raw/articles/How to navigate LLM model names.md
  - raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md
tags:
  - llm
  - embedding
  - rag
  - vector-database
  - response-caching
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.85
provenance: extracted
---

# Embedding Models

Embedding models convert text into numerical token vectors for storage, querying, and retrieval from a vector database. They are often used in retrieval-augmented generation (RAG) workflows alongside instruct models. ^[raw/articles/How to navigate LLM model names.md]

## Key Points

- Embedding is the process of converting text to numerical vectors that can be stored, queried, and retrieved from a vector database ^[raw/articles/How to navigate LLM model names.md]
- Embedding models are commonly paired with instruct models in RAG pipelines, where the embedding model handles retrieval and the instruct model generates the final response ^[raw/articles/How to navigate LLM model names.md]
- In model names, "embedding" or "Embed" signals that the model is purpose-built for vector generation rather than text generation ^[raw/articles/How to navigate LLM model names.md]

- On OpenRouter, the `/api/v1/embeddings` endpoint is eligible for response caching; cache hits zero out `usage.prompt_tokens` and `usage.total_tokens` (the `completion_tokens` field is not present in embedding responses) ^[raw/document/openrouter/openrouter-031-guides-features-response-caching-2026-04-29.md]

## Related

- [[concepts/model_naming]]
- [[concepts/rag]]
- [[entities/openrouter]]
- [[concepts/response_caching]]