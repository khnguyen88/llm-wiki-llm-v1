---
title: "Model Naming Conventions"
summary: "The structured grammar encoded in LLM model names — family, version, size, alignment, context, format, quantization — that enables fast triage but not replacement for benchmarking"
type: concept
sources:
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
  - raw/articles/Naming Conventions of LLM Models.md
  - raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md
  - raw/articles/How to navigate LLM model names.md
  - raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md
tags:
  - llm
  - naming-conventions
  - model-selection
  - deployment
  - cloud-provider
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Model Naming Conventions

LLM model names encode a soft grammar of practical metadata — family, version, size, alignment stage, and runtime compatibility tags. Names serve as structured shorthand for model selection, enabling fast triage across stakeholders: researchers tracking experiment lineage, platform teams managing artifacts, product teams selecting deployment candidates, and governance teams auditing usage. However, names are useful heuristics, not guarantees. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

## Key Points

- Name pattern: `<family>-<version>-<size>-<alignment>-<context>-<format>-<quant>` — order varies across vendors but the information pattern is similar ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]
- Branded names identify vendor and architectural lineage — some encode acronyms (Llama = **L** arge **La** nguage **M** odel **M** eta **A** I), others are marketing-driven (Granite evoking reliability) ^[raw/articles/How to navigate LLM model names.md]
- Major version changes may break compatibility with serving tools like vLLM, requiring new releases to support the model; minor versions correspond to incremental improvements or data refreshes ^[raw/articles/How to navigate LLM model names.md]
- Size tags (7B, 8B, 70B) determine memory, latency, and quality trade-offs; quantization tags (Q4, int8, 4bit) signal compressed variants with lower VRAM requirements ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]
- Concrete vRAM requirements: granite-3.2-8b-instruct fits on a single A10 (24 GB) with limited context; Llama-3.1-405b-instruct requires 900+ GB across sixteen H100s ^[raw/articles/How to navigate LLM model names.md]
- Alignment stage (base/instruct/chat) is the strongest first filter for model selection — deploying a base model in a user-facing assistant role is one of the most common and costly mistakes ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]
- Model purpose tags in names indicate specialization: base (fine-tuning starting point), instruct (prompt-following, the default for chat), vision (multi-modal input), code (coding, now largely subsumed by instruct), embedding (vector conversion for RAG), guard (safety filtering), reasoning (chain-of-thought before responding) ^[raw/articles/How to navigate LLM model names.md]
- "Vision-instruct" models combine both vision and instruction-following capabilities in a single model ^[raw/articles/How to navigate LLM model names.md]
- Memory estimation from names: raw weight storage ≈ P × b/8 bytes, where P is parameter count and b is bits per weight; e.g., 8B at FP16 ≈ 16 GB, 8B at 4-bit ≈ 4 GB (before KV cache and framework overhead) ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]
- Naming ambiguity risks: Instruct quality varies across vendors, missing context tags cause truncation surprises, quant tags without method details (NF4, GPTQ, AWQ) risk quality drops, similar names across forks create provenance risks ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]
- Simpler naming pattern: model name — parameter count — fine-tuning type — quantization type; e.g., `llama3.3-70b-instruct-q4_K_M` = Llama 3.3, 70B params, instruct-tuned, Q4 K-quant medium ^[raw/articles/LLM Naming Explained (What do the options mean_).md]
- Quantization tradeoffs in model names are analogous to video resolution: 1080p (FP16, high quality, large) vs. 720p vs. 480p (Q2, small, significant quality loss) ^[raw/articles/LLM Naming Explained (What do the options mean_).md]
- Common suffix meanings: Turbo (speed + cost optimized), Mini (smaller + cheaper), Pro (high capability), Flash (ultra-fast), Instruct (fine-tuned for instructions), Chat (conversation-optimized), rlhf (trained with human feedback) ^[raw/articles/Naming Conventions of LLM Models.md]
- Size hierarchy in names: xxl > xl > large > base > small; parameter counts (7B, 13B, 70B) serve as size indicators ^[raw/articles/Naming Conventions of LLM Models.md]
- Versioning tags (v0.1, v1, v2) indicate iterations of fine-tuning ^[raw/articles/Naming Conventions of LLM Models.md]
- File format extensions in model names indicate framework compatibility: .bin (binary), .pt (PyTorch), .onnx (cross-framework interoperable), .gguf (quantized inference), .tflite (TensorFlow Lite) ^[raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md]
- Domain-specific fine-tuning labels include Medical (healthcare), Code (code generation), and Embedding (vector generation), extending beyond the standard Instruct/Chat variants ^[raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md]
- Naming conventions serve four practical purposes: deployment environment selection (smaller quantized models for edge devices), task-specific model identification (Instruct/Chat labels), platform compatibility assessment (format extensions), and performance optimization (quantization levels) ^[raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md]
- For high-stakes applications, prioritize accuracy with higher-bit quantization (Q8); for lower-stakes or resource-constrained deployments, opt for efficient quantization (Q4, INT8) ^[raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md]
- When deploying through cloud providers (Bedrock, Vertex AI, Foundry), pin specific model versions using `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, and `ANTHROPIC_DEFAULT_HAIKU_MODEL`; without pinning, model aliases resolve to the latest version which may not yet be enabled in the account ^[raw/document/claude code/claude-code-108-third-party-integrations-2026-04-29.md]

## Details

### The Naming Grammar

Most naming systems encode five fields: (1) family — architectural lineage or vendor stream, (2) generation/version — release evolution, (3) capacity tier — parameter count or size class, (4) alignment stage — base vs instruct/chat, and (5) runtime compatibility tags — format, quantization, context window. Even when undocumented, teams treat names as structured metadata for artifact identity and compatibility. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

Example decodings: `Llama-3.1-8B-Instruct` = Llama family, v3.1, 8B params, instruction-tuned. `Qwen2.5-14B-Instruct-GGUF-Q4_K_M` = Qwen 2.5, 14B, instruct, GGUF format, 4-bit quantized. `Phi-3-mini-4k-instruct` = Phi family, mini tier, 4k context, instruction-tuned. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md] Additional example: `deepseek-r1:70b-llama-distill-q4_K_M` = DeepSeek R1, 70B params, distilled into Llama architecture, 4-bit K-quant medium compression. ^[raw/articles/LLM Naming Explained (What do the options mean_).md] Further examples: `Llama-3.2-7B-Chat-Q4_K.gguf` = Llama v3.2, 7B params, chat-tuned, 4-bit K-quant, GGUF format. `GPT-3.5-175B-Instruct-Q8.onnx` = GPT v3.5, 175B params, instruct-tuned, 8-bit quantized, ONNX format. `BitNet-b1.58-3B-Medical-IQ3.gguf` = BitNet v1.58, 3B params, medical-tuned, integer quantization level 3, GGUF format. `Llama-2-13B-Embedding-Q4_F.pt` = Llama v2, 13B params, embedding-optimized, 4-bit quantization, PyTorch format. `Falcon-40B-Chat-FP16.bin` = Falcon family, 40B params, chat-tuned, 16-bit floating point, binary format. ^[raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md]

### Ambiguity and Validation

Model names are not perfect standards. The `Instruct` label means different tuning quality across vendors. Missing context tags can cause prompt truncation surprises. Quant tags without method details (e.g., just `Q4` without specifying NF4 vs GPTQ vs AWQ) risk unexpected quality drops. Similar names across forks create security and provenance risks. Mitigation: always verify claims in the model card, benchmark on your task set, and pin exact source with checksum. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

### Decision Guide

Model selection priority by requirement: lowest latency → smaller size tags (3B, 7B) plus quant tags; strongest assistant behavior → Instruct/Chat variants; long-form reasoning → large context window tags (16k, 32k, 128k); reproducibility → clear family and versioned release naming. After filtering by name, validate candidates on workload prompts, cost and latency budgets, and safety requirements. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

### Paid vs Open-Source Naming

Paid and open-source models follow fundamentally different naming conventions reflecting their audiences. Paid models use the pattern `[Model Family] + [Version] + [Variant/Capability Tier]` — designed for simplicity, branding, and product differentiation for non-technical users (e.g., GPT-4o = GPT family, 4th gen, omni/multimodal; Gemini 1.5 Pro = Gemini family, v1.5, high capability). Open-source models use `[organization]/[model-family]-[version]-[size]-[variant]-[format]` — designed as engineering artifacts exposing technical metadata (e.g., `meta-llama/Llama-2-7b-chat-hf` = Meta's Llama v2, 7B params, chat-tuned, Hugging Face format). Paid models are designed like products; open-source models are designed like engineering artifacts. ^[raw/articles/Naming Conventions of LLM Models.md]

### Team Naming Policy

Consistent internal naming practices reduce debugging time: use a consistent naming schema for fine-tuned variants, include date/version and evaluation profile in artifact metadata, separate model lineage name from deployment environment tags, maintain a model registry with immutable IDs and aliases, and document mappings from external vendor names to internal IDs. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

### File Format in Model Names

File format extensions in model names signal platform and framework compatibility. Common formats: .bin (binary models for low-level deployment), .pt (PyTorch native format), .onnx (cross-framework interoperable format), .gguf (quantized formats for inference frameworks and on-device deployment), .tflite (TensorFlow Lite for mobile and embedded). The format choice determines which tools and hardware can load the model. ^[raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md]

## Related

- [[concepts/quantization]]
- [[concepts/instruction_tuning]]
- [[concepts/gguf]]
- [[concepts/safetensors]]
- [[concepts/vision_models]]
- [[concepts/guard_models]]
- [[concepts/embedding_models]]
- [[entities/hugging_face]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]