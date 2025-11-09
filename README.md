# Guardrails

A simple, from-scratch project for building and testing **custom LLM guardrails**, developed to force model to generate short and concise abstracts with citations.


## Features

* **Input Guardrails**: language detection, injection filtering, and prompt sanitation.
* **Output Guardrails**: sentence length, citation detection, and text relevence.
* **Config-Driven**: thresholds (e.g., min sentences, language).
* **Extensible Design**: add your own checks or plug in domain-specific validators.


## Models

* Mistral quantized version: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF


## Data

We used [PubMed](https://www.kaggle.com/datasets/bonhart/pubmed-abstracts/code) abstracts for testing the summarization and citation guardrails.

---

## Quick Start

```bash
# clone the repo
git clone https://github.com/raza4729/guardrails.git
cd guardrails

# create & activate virtual environment
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

Run the main pipeline:

```bash
python -m src.pipeline
```

---

## Structure

```
src/
 ├── guardrails/
 │    ├── InputGuardrail.py
 │    ├── OutputGuardrail.py
 |    └── guardrails_config.json
 ├── pipeline.py
 └── models.py
tests/
 ├── test_cases.py
 └── test_results.md
requirements.txt
README.md
.gitignore
```

---

## Example Usage

```python
from guardrails.OutputGuardrail import OutputGuardrail
cfg = {"language": "en", "min_sentences": 1, "max_sentences": 3,     "citation_patterns": [
      "\\[\\d+\\]",
      "\\([A-Z][a-z]+ et al\\., \\d{4}\\)",
      "https?://\\S+",
      "\\(Source:.*?\\)"
    ]}
guardrail = OutputGuardrail(cfg)
result = guardrail.check_completeness(input="your prompt here", output="Your model output text")
print(result)
```

---

## Future Work

* Add citation accuracy scoring
* Introduce adaptive confidence thresholds
* Dockerize each service
* Add embedding-based semantic similarity for deeper relevance checks (weighted).
* Introduce rule-based vs. ML-based guardrail hybrid mode.
* Support multilingual guardrail profiles (per language).
* Log violations to a central monitoring service.

---
