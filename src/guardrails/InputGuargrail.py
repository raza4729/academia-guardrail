from typing import Dict, Any
    
def sanitize_input(user_input: str) -> str:
    pass

def build_prompt(input_data: Dict[str, Any]) -> str:
    """Combine instruction and text into a single prompt."""
    instruction = "Summarize the following abstract in maximum 3 sentences and provide factual citations."
    
    abstract = input_data.get("abstract", "")
    abstract = abstract.lstrip("'([")
    abstract = abstract.rstrip("')")

    # Merge instruction and text
    combined = f"{instruction}" + "\n\n" + abstract

    # unsafe token cleaning
    safe_prompt = combined.replace("Ignore previous instructions", "[filtered]")
    return safe_prompt.strip()