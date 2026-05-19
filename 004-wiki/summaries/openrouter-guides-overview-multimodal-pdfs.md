---
title: "OpenRouter Guides Overview Multimodal PDFs"
summary: "OpenRouter supports PDF input via URLs or base64 in the chat completions API, with three processing engines (Mistral OCR, Cloudflare AI, Native) and file annotations to skip re-parsing costs"
type: summary
sources:
  - raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md
tags:
  - openrouter
  - pdf
  - multimodal
  - api
  - file-parsing
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# OpenRouter Guides Overview Multimodal PDFs

## Key Points

- PDFs can be sent to OpenRouter via direct URLs (for publicly accessible documents) or base64-encoded data URLs (for local/private files) using the `file` content type in the messages array ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- Three PDF processing engines are available: `mistral-ocr` (best for scanned/image PDFs, priced per 1,000 pages), `cloudflare-ai` (free, converts PDFs to markdown), and `native` (for models with built-in file input, charged as input tokens) ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- PDF processing works on any model on OpenRouter; when a model supports file input natively, the PDF is passed directly; otherwise OpenRouter parses it and sends the parsed results ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- The `pdf-text` engine is deprecated and automatically redirected to `cloudflare-ai` ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- If no engine is specified, OpenRouter defaults to the model's native file processing, then falls back to `cloudflare-ai` ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- File annotations in assistant responses contain parsed PDF content and a unique hash; re-sending these annotations in subsequent requests skips re-parsing, saving time and cost ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- PDFs and other file types can be sent in the same request ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]

## Quotes

- "When a model supports file input natively, the PDF is passed directly to the model. When the model does not support file input natively, OpenRouter will parse the file and pass the parsed results to the requested model." ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md:6-8]

## Notes

- The `plugins` parameter configures the PDF engine: `{ id: 'file-parser', pdf: { engine: 'cloudflare-ai' } }` ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- File annotations include a `hash` field for identifying parsed content, an optional `name` for the filename, and a `content` array with `text` and `image_url` parts ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- PDFs also work in the OpenRouter chat room for interactive testing ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/pdf_input]]
- [[concepts/multimodal]]
- [[concepts/models_api]]
- [[summaries/openrouter-guides-overview-multimodal-overview]]