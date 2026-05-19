---
title: "PDF Input"
summary: "OpenRouter's mechanism for sending PDF documents to any model via URLs or base64 encoding, with configurable processing engines and annotation-based re-parsing avoidance"
type: concept
sources:
  - raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md
tags:
  - pdf
  - multimodal
  - openrouter
  - file-parsing
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# PDF Input

PDF Input is OpenRouter's mechanism for processing PDF documents through the chat completions API. PDFs are sent in the messages array using the `file` content type, either as direct URLs or base64-encoded data URLs, and work on any model regardless of native file support. ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]

## Key Points

- PDFs are sent via the `file` content type in the messages array with a `filename` and either a URL (`file_data` as a URL string) or base64 data URL (`file_data` as a `data:application/pdf;base64,...` string) ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- When a model supports file input natively, the PDF is passed directly; when it does not, OpenRouter parses the PDF and sends parsed results instead ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- Three processing engines are configurable via the `plugins` parameter: `mistral-ocr`, `cloudflare-ai`, and `native` ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- File annotations returned in assistant responses enable cost and time savings by skipping re-parsing in follow-up requests ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]
- If no engine is specified, OpenRouter defaults to native file processing first, then falls back to `cloudflare-ai` ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]

## Details

### Processing Engines

The `mistral-ocr` engine is best for scanned documents or PDFs containing images; it is priced per 1,000 pages. The `cloudflare-ai` engine converts PDFs to markdown using Cloudflare Workers AI and is free. The `native` engine is only available for models that support file input natively and is charged as input tokens. The deprecated `pdf-text` engine is automatically redirected to `cloudflare-ai`. ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]

### Plugin Configuration

PDF processing is configured via the `plugins` parameter in the request body, using plugin ID `file-parser` with an `engine` field:

```json
{
  "plugins": [
    {
      "id": "file-parser",
      "pdf": {
        "engine": "cloudflare-ai"
      }
    }
  ]
}
```

^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]

### File Annotations and Re-parsing

When OpenRouter parses a PDF, the assistant response includes a `file` annotation containing the parsed content (text blocks and images as base64 data URLs) and a unique `hash` identifying the parsed file. By including this annotation object in subsequent request messages, OpenRouter reuses the pre-parsed content instead of re-parsing the PDF, which saves processing time and cost — especially with the `mistral-ocr` engine. ^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]

### File Annotation Schema

```typescript
type FileAnnotation = {
  type: 'file';
  file: {
    hash: string;           // Unique hash identifying the parsed file
    name?: string;          // Original filename (optional)
    content: ContentPart[]; // Parsed content from the file
  };
};

type ContentPart =
  | { type: 'text'; text: string }
  | { type: 'image_url'; image_url: { url: string } };
```

^[raw/document/openrouter/openrouter-007-guides-overview-multimodal-pdfs-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/multimodal]]
- [[concepts/models_api]]
- [[summaries/openrouter-guides-overview-multimodal-pdfs]]