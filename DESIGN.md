## 1. Overview

This document describes the internal design of the **Guardrails** project — a lightweight framework for enforcing input/output constraints on large language models (LLMs).
The system aims to make generation more **safe**, **concise**, and **factual**, particularly for abstract summarization tasks.

---

## 2. Core Architecture

```
Input Text (pipeline.py)  ─▶  InputGuardrail  ─▶  models (e.g., Mistral)  ─▶  OutputGuardrail  ─▶  Final Output
```

| Component           | Role                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------- |
| **InputGuardrail**  | Pre-validates text: language detection, preprocessing and malicious content filtering.      |
| **Model Layer**     | Handles inference with a quantized LLM (e.g., Mistral GGUF).                                |
| **OutputGuardrail** | Post-validates model output: sentence count, relevance, and citation detection.             |
| **Pipeline**        | Coordinates guardrails and model, aggregates results, logs violations.                      |

---

## 3. Key Design Decisions

1. **Config-driven behavior** — guardrail thresholds and rules are defined in `guardrails_config.json`.
2. **Stateless architecture** — each run operates on a single text item; no shared mutable state.
3. **Pluggable models** — any model with `.inference(prompt: str)` can be integrated.
4. **Separation of concerns** — input and output validations are modular, testable, and independent.
5. **Graceful failure** — violations raise `GuardrailViolation`, caught at the pipeline level to skip or log items.

---

<!-- ## 4. Class Responsibilities

### `InputGuardrail`

* Normalizes and cleans text.
* Detects non-target languages using `langdetect`.
* Calls the model for **SAFE/MALICIOUS** classification.
* Raises `GuardrailViolation` on:

  * Empty abstracts
  * Language mismatch
  * Malicious content

### `OutputGuardrail`

* Checks sentence count (`min_sentences`, `max_sentences`).
* Verifies presence of citations (e.g., `[1]`, `(Source: …)`).
* Tests semantic relevance between prompt and output.
* Returns structured validation results.

### `Pipeline`

* Initializes guardrails and the model.
* Iterates through dataset entries.
* Logs or stores skipped/flagged cases.

---
-->

## 5. Data Flow Example

```
┌─────────────────────┐
│  input_data (dict)  │
└─────────┬───────────┘
          │
          ▼
   InputGuardrail.build_prompt()
      ├─ Normalize + check language
      ├─ Detect malicious content
      └─ Return validated prompt
          │
          ▼
        Model.inference()
          │
          ▼
   OutputGuardrail.validate()
      ├─ Sentence length check
      ├─ Citation detection
      └─ Relevance score
```

---

## 6. Testing Strategy

| Test                              | Purpose                                     |
| --------------------------------- | ------------------------------------------- |
| `test_foreign_language_rejected`  | Ensures non-English inputs are blocked.     |
| `test_malicious_content_blocked`  | Confirms malicious text triggers violation. |
| `test_output_citation_pattern`    | Detects citations in generated text.        |
| `test_sentence_length_validation` | Validates sentence count constraints.       |

---

## 8. References

* [Mistral-7B-Instruct-v0.2-GGUF on Hugging Face](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)
* [Langdetect Python Library](https://pypi.org/project/langdetect/)

---
