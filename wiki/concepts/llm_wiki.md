---
title: "LLM Wiki"
summary: "A personalization pattern where an LLM incrementally builds a persistent, navigable wiki of knowledge, putting the user in full control of their data"
type: concept
sources:
  - raw/articles/farzapedia.md
tags:
  - llm-wiki
  - personalization
  - knowledge-management
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# LLM Wiki

A pattern for AI personalization where the LLM incrementally builds and maintains a persistent wiki of structured knowledge, rather than relying on implicit learning. The wiki is explicit, inspectable, and controlled by the user. ^[raw/articles/farzapedia.md:4-6]

## Key Points

- The LLM Wiki pattern contrasts with the "status quo" approach where an AI "allegedly gets better the more you use it" through implicit learning ^[raw/articles/farzapedia.md:4]
- Memory artifacts are explicit and navigable — the user can see exactly what the AI does and does not know, and can inspect and manage the artifact even if the LLM does the direct text writing ^[raw/articles/farzapedia.md:6]
- Data remains under the user's control on their local computer, not locked inside an AI provider's system ^[raw/articles/farzapedia.md:7]
- The approach puts the user in full control: data is theirs, in universal formats, explicit and inspectable ^[raw/articles/farzapedia.md:11]
- Managing the wiki requires handling file directories, but agents make this simpler and can help significantly ^[raw/articles/farzapedia.md:13]

## Details

The LLM Wiki pattern addresses personalization through four interconnected properties. **Explicit** means the knowledge artifact is viewable and manageable — not hidden in a black-box model. **Yours** means the data stays on the user's machine, extractable and portable. **File over app** means the data lives in universal formats like markdown and images, making it interoperable with any tool. **BYOAI** means any AI model can be plugged into the information, including finetuning an open source model on the wiki so it "knows" the user in its weights. ^[raw/articles/farzapedia.md:4-9]

Karpathy acknowledges this is not the simplest approach — it requires managing file directories — but argues that agents make it significantly easier. He further suggests that "agent proficiency" is a core skill of the 21st century, given that agents speak English and handle all the computer tasks. ^[raw/articles/farzapedia.md:13]

## Related

- [[concepts/file_over_app]]
- [[concepts/byoai]]