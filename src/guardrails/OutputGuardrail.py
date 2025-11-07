
from nltk.tokenize import sent_tokenize

class OutputGuardrail:
    
    def validate_schema(self, output: str, expected_format: str) -> bool:
        # Placeholder for format validation logic
        return True
    
    def _url_saftey_check(self, url: str) -> bool:
        # Placeholder for URL safety check logic
        return True  
    
    def _validate_citation_format(self, citation: str) -> bool:
        # Placeholder for citation format validation logic
        return True
    
    def _validate_relevance(self, text: str, context: str) -> bool:
        # Placeholder for relevance check logic
        return True
    
    def _language_check(self, text: str, language: str) -> bool:
        # Placeholder for language check logic
        return True

    def _validate_sent_length(self, text: str, min_sentences: int) -> bool:
        sentences = sent_tokenize(text)
        return len(sentences) >= min_sentences

    def check_completeness(self, output: str, required_elements: list) -> bool:
        violations = []
        # 1. Check length constraint 
        if not self._validate_sent_length(output, required_elements["min_sentences"]):
            violations.append(f"Too few sentences: found {len(sent_tokenize(output))}, "
                            f"expected at least {required_elements['min_sentences']}")

        # 2. Check language constraint

        if not violations:
            return True, output
        else:
            return False, violations
    
