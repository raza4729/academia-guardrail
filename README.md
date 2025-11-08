# Guardrails

A simple, from-scratch project for building and testing **custom LLM guardrails**, built to keep abstracts concise, citations accurate, and short.


## Features

* **Input Guardrails**: language detection, injection filtering, and prompt sanitation.
* **Output Guardrails**: sentence length, citation detection, and text relevence.
* **Config-Driven**: thresholds (e.g., min sentences, language).
* **Extensible Design**: add your own checks or plug in domain-specific validators.

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
 │
 ├── pipeline.py
 └── config/
      └── guardrails_config.json
```

---

## Example Usage

```python
from guardrails.OutputGuardrail import OutputGuardrail
cfg = {"language": "en", "min_sentences": 3}
guardrail = OutputGuardrail(cfg)
result = guardrail.check_completeness(output="Your model output text")
print(result)
```

---

## Future Work

* Add citation accuracy scoring
* Integrate embedding-based relevance check
* Introduce adaptive confidence thresholds

---
