---
title: "Naming Conventions of LLM Models"
source: "https://www.tothenew.com/blog/naming-conventions-of-llm-models/"
author:
  - "[[Sudarshan]]"
published: 2026-03-30
created: 2026-04-23
description: "Introduction When we see any LLM model names like GPT-4o, Claude 3 Sonnet, or LLaMA-2-7B-chat we wonder why companies give such weird names to their models. But let me tell you, these names have lots of meanings inside it. They provide lots of information about that model. Common Patterns: Suffix"
tags:
  - "clippings"
---
Category

Sort By

- [Data Science](https://www.tothenew.com/blog/category/data-science/ "View all posts in Data Science")

**Introduction**  
When we see any LLM model names like **GPT-4o**, **Claude 3 Sonnet**, or **LLaMA-2-7B-chat** we wonder why companies give such weird names to their models. But let me tell you, these names have lots of meanings inside it. They provide lots of information about that model.

- **Common Patterns:**  
	**Suffix Meaning**  
	Turbo —> Optimised for speed + cost  
	Mini —> Smaller + cheaper  
	Pro —> High capability  
	Flash —> Ultra-fast  
	Instruct —> Fine-tuned to follow instructions  
	Chat —> Optimised for conversations  
	rlhf → trained with human feedback
- **Size Hierarchy:**  
	xxl > xl > large > base > small
- **Size Indicators:**  
	7B, 13B, 70B → parameters
- **Versioning:**  
	v0.1, v1, v2 → iteration of fine-tuning

There are mainly two types of LLMs, lets understand their naming convention one by one.

1. ## Paid Models
	Paid models are mainly business or customer oriented. So, their naming convention mainly focused on Simplicity, branding and positioning.
	General Pattern in paid models:  
	\[Model Family\] + \[Version\] + \[Variant / Capability Tier\]
	*Lets see some examples:*
	***Example 1:*** GPT-4o  
	Breakdown:  
	GPT → Model family  
	4 → Generation (improvement over GPT-3.5)  
	o (omni) → Multimodal capability
	***Meaning:***  
	A 4th-gen model capable of handling text, image, audio, etc.
	***Example 2:*** Gemini 1.5 Pro  
	Breakdown:  
	Gemini → Model family  
	1.5 → Incremental upgrade  
	Pro → High capability
	Other variants:  
	Flash → Faster, cheaper  
	Ultra → Most powerful
	Paid models naming designed for easy understanding of non-technical users, marketing tiers and product differentiation.
2. ## Open-Source Model
	Open source model naming is more technical and architecture oriented.
	General Pattern in open source models:  
	\[organization\]/\[model-family\]-\[version\]-\[size\]-\[variant\]-\[format\]
	***Example 1***: meta-llama/Llama-2-7b-chat-hf  
	Breakdown:  
	meta-llama → Organization  
	Llama-2 → Model family + version  
	7b → 7 billion parameters  
	chat → Fine-tuned for conversation  
	hf → Hugging Face format
	***Meaning:***  
	A 7B parameter chat-optimized LLaMA v2 model
	***Example 2:*** mistralai/Mistral-7B-Instruct-v0.1  
	Breakdown:  
	Mistral-7B → Base model  
	Instruct → Instruction-following  
	v0.1 → Version of fine-tuning
	***Meaning:***  
	Instruction-tuned version of Mistral 7B (early release)

**Final Thoughts:**  
– Paid models are designed like products  
– Open-source models are designed like engineering artifacts

Understanding this difference can help us to select a better model for our specific requirements.

To read more such technical blogs, **please follow us on social media**. Thanks.

<iframe src="https://www.tothenew.com/blog/wp-content/plugins/ttn-blog-enhancements//docs/how-to-write-a-blog.pdf" frameborder="0"></iframe><iframe src="https://www.tothenew.com/blog/wp-content/plugins/ttn-blog-enhancements//docs/how-to-add-perfect-caption.pdf" frameborder="0"></iframe>