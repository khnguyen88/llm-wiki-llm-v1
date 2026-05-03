---
title: "Model Naming Conventions"
summary: "The structured grammar encoded in LLM model names -- family, version, size, alignment, context, format, quantization -- that enables fast triage but not replacement for benchmarking"
type: concept
sources:
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
  - raw/articles/Naming Conventions of LLM Models.md
  - raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md
  - raw/articles/How to navigate LLM model names.md
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - naming-conventions
  - model-selection
  - deployment
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Model Naming Conventions

LLM model names encode a soft grammar of practical metadata -- family, version, size, alignment stage, and runtime compatibility tags. Names serve as structured shorthand for model selection, enabling fast triage across stakeholders: researchers tracking experiment lineage, platform teams managing artifacts, product teams selecting deployment candidates, and governance teams auditing usage. However, names are useful heuristics, not guarantees. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

## The Naming Grammar

Most naming systems encode five fields: (1) family -- architectural lineage or vendor stream, (2) generation/version -- release evolution, (3) capacity tier -- parameter count or size class, (4) alignment stage -- base vs instruct/chat, (5) runtime compatibility tags -- format, quantization, context window. The general pattern is `[Org/] Family-Version-Size [-Active] -Training [-Format] [-Quantization]`, though order varies across vendors. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md] ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

| Component | Example | Meaning |
|---|---|---|
| Organization | `bartowski` | Community quantizer who published the variant |
| Family | `Qwen3.5` | Model family and generation |
| Size | `32B` | 32 billion parameters (or `35B-A3B` for MoE models) |
| Training | `Instruct` / `IT` / `it` | Instruction-tuned (follows prompts) |
| Format | `GGUF` | File format for local inference |
| Quantization | `Q4_K_M` | 4-bit precision, K-quant method, medium block size |
| Context | `4k`, `32k`, `128k` | Context window length |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

### Example Decodings

| Model Name | Decoded Meaning |
|---|---|
| `Llama-3.1-8B-Instruct` | Llama family, v3.1, 8B params, instruction-tuned |
| `Qwen2.5-14B-Instruct-GGUF-Q4_K_M` | Qwen 2.5, 14B, instruct, GGUF format, 4-bit quantized |
| `Phi-3-mini-4k-instruct` | Phi family, mini tier, 4k context, instruction-tuned |
| `google/gemma-4-26B-A4B-it` | Google org, Gemma 4, 26B total / 4B active MoE, instruction-tuned |
| `deepseek-r1:70b-llama-distill-q4_K_M` | DeepSeek R1, 70B, distilled into Llama, 4-bit K-quant medium |
| `Llama-3.2-7B-Chat-Q4_K.gguf` | Llama v3.2, 7B, chat-tuned, 4-bit K-quant, GGUF format |
| `GPT-3.5-175B-Instruct-Q8.onnx` | GPT v3.5, 175B, instruct, 8-bit quantized, ONNX format |

^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md] ^[raw/articles/LLM Naming Explained (What do the options mean_).md] ^[raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md] ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Branded Names and Versioning

Branded names identify vendor and architectural lineage -- some encode acronyms (Llama = "Large Language Model Meta AI"), others are marketing-driven (Granite evoking reliability). ^[raw/articles/How to navigate LLM model names.md]

Version numbers follow simplified semantic versioning (major.minor, typically omitting patch). Major version changes indicate significant architectural or training-data shifts that may break compatibility with serving tools like vLLM. Minor versions correspond to incremental improvements or data refreshes. ^[raw/articles/How to navigate LLM model names.md]

## Alignment and Purpose Tags

Alignment tags in model names are the strongest first filter for model selection -- deploying a base model in a user-facing assistant role is one of the most common and costly mistakes. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

| Tag | Description |
|---|---|
| `base` | Generic pretrained model, starting point for fine-tuning; text completion only |
| `instruct` / `IT` / `it` | Fine-tuned on instruction-response pairs; standard for conversational use |
| `chat` | Further optimized for multi-turn conversation (older term, largely replaced by "instruct") |
| `vision` / `VL` | Multi-modal: accepts text + image inputs |
| `coder` | Fine-tuned specifically for code generation |
| `reasoning` / `thinking` | Optimized for chain-of-thought reasoning |
| `embedding` | Converts text to numerical vectors for RAG |
| `guard` / `guardian` | Safety filtering for detecting unsafe content |

^[raw/articles/How to navigate LLM model names.md] ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

Training suffixes also indicate specific fine-tuning techniques: `-DPO` (Direct Preference Optimization), `-RLHF` (Reinforcement Learning from Human Feedback), `-LoRA` (Low-Rank Adaptation adapter weights only). ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Memory Estimation from Names

Raw weight storage: Memory(weights) approximately equals P x b/8 bytes, where P is parameter count and b is bits per weight. For Q4_K_M GGUF, file size in GB roughly equals parameter count in billions x 0.6. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md] ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

| Model | Precision | Raw Weight Size |
|---|---|---|
| 8B | FP16 (16-bit) | ~16 GB |
| 8B | 4-bit | ~4 GB |
| 7B | Q4_K_M | ~4 GB |
| 32B | Q4_K_M | ~19 GB |
| 70B | Q4_K_M | ~40 GB |

## Common Suffixes in Commercial Models

| Suffix | Meaning |
|---|---|
| Turbo | Optimized for speed + cost |
| Mini | Smaller + cheaper |
| Pro | High capability |
| Flash | Ultra-fast |

^[raw/articles/Naming Conventions of LLM Models.md]

## Paid vs Open-Source Naming

Paid and open-source models follow fundamentally different conventions reflecting their audiences. Paid models use `[Model Family] + [Version] + [Variant/Capability Tier]` -- designed for simplicity, branding, and product differentiation (e.g., GPT-4o, Gemini 1.5 Pro). Open-source models use `[organization]/[model-family]-[version]-[size]-[variant]-[format]` -- designed as engineering artifacts exposing technical metadata (e.g., `meta-llama/Llama-2-7b-chat-hf`). Paid models are designed like products; open-source models are designed like engineering artifacts. ^[raw/articles/Naming Conventions of LLM Models.md]

## Ambiguity and Naming Risks

Model names are not perfect standards. Risks include: Instruct quality varying across vendors, missing context tags causing truncation surprises, quant tags without method details (NF4 vs GPTQ vs AWQ) risking quality drops, and similar names across forks creating provenance risks. Mitigation: always verify claims in the model card, benchmark on your task set, and pin exact sources with checksums. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

## Team Naming Policy

Consistent internal naming practices reduce debugging time: use a consistent naming schema for fine-tuned variants, include date/version and evaluation profile in artifact metadata, separate model lineage name from deployment environment tags, maintain a model registry with immutable IDs, and document mappings from external vendor names to internal IDs. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

## Related

- [[concepts/quantization]]
- [[concepts/instruction_tuning]]
- [[concepts/gguf]]
- [[concepts/safetensors]]
- [[concepts/mixture_of_experts]]
- [[concepts/distillation]]
- [[entities/hugging_face]]
- [[entities/ollama]]
