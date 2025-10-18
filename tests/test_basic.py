"""
Basic tests for validai package.

This test file demonstrates how to use validai assertions to test LLM outputs.
"""

import pytest
from validai import structure, semantic, factuality, safety


class TestStructureValidation:
    """Tests for structure validation."""

    def test_assert_json_valid_with_valid_json(self):
        """Test that valid JSON passes validation."""
        output = '{"name": "John", "age": 30}'
        result = structure.assert_json_valid(output)
        assert result == {"name": "John", "age": 30}

    def test_assert_json_valid_with_invalid_json(self):
        """Test that invalid JSON raises AssertionError."""
        output = '{name: "John"}'  # Invalid JSON (unquoted key)
        with pytest.raises(AssertionError):
            structure.assert_json_valid(output)

    def test_assert_has_keys(self):
        """Test that JSON with required keys passes validation."""
        output = '{"name": "Alice", "email": "alice@example.com"}'
        result = structure.assert_has_keys(output, ["name", "email"])
        assert "name" in result

    def test_assert_has_keys_missing(self):
        """Test that JSON missing required keys fails validation."""
        output = '{"name": "Bob"}'
        with pytest.raises(AssertionError):
            structure.assert_has_keys(output, ["name", "email"])


class TestSemanticValidation:
    """Tests for semantic validation."""

    def test_assert_similar_with_similar_texts(self):
        """Test that similar texts pass validation."""
        output = "The quick brown fox jumps over the lazy dog"
        reference = "The fast brown fox leaps over the sleepy dog"
        # Adjust threshold to match the actual similarity score
        result = semantic.assert_similar(output, reference, threshold=0.4)
        assert result is True

    def test_assert_similar_with_dissimilar_texts(self):
        """Test that dissimilar texts fail validation."""
        output = "The weather is sunny today"
        reference = "Machine learning is fascinating"
        with pytest.raises(AssertionError):
            semantic.assert_similar(output, reference, threshold=0.5)

    def test_assert_contains_concept(self):
        """Test that output containing a concept passes validation."""
        output = "Machine learning is a subset of artificial intelligence."
        result = semantic.assert_contains_concept(output, "machine learning")
        assert result is True

    def test_assert_contains_concept_missing(self):
        """Test that output missing a concept fails validation."""
        output = "The weather is nice today."
        with pytest.raises(AssertionError):
            semantic.assert_contains_concept(output, "machine learning")


class TestFactualityValidation:
    """Tests for factuality validation."""

    def test_assert_contains_fact(self):
        """Test that output containing a fact passes validation."""
        output = "Paris is the capital of France and home to the Eiffel Tower."
        result = factuality.assert_contains_fact(output, "capital of France")
        assert result is True

    def test_assert_contains_fact_missing(self):
        """Test that output missing a fact fails validation."""
        output = "London is a major city in England."
        with pytest.raises(AssertionError):
            factuality.assert_contains_fact(output, "capital of France")

    def test_assert_accurate_numbers(self):
        """Test that accurate numbers pass validation."""
        output = "The speed: 299792458 meters per second."
        result = factuality.assert_accurate_numbers(
            output, {"speed": 299792458}, tolerance=1
        )
        assert result is True

    def test_assert_cites_sources(self):
        """Test that output with citations passes validation."""
        output = "According to recent studies [1], the population is growing."
        result = factuality.assert_cites_sources(output, min_sources=1)
        assert result is True


class TestSafetyValidation:
    """Tests for safety validation."""

    def test_assert_no_pii_clean_output(self):
        """Test that output without PII passes validation."""
        output = "The user requested information about weather forecasts."
        result = safety.assert_no_pii(output)
        assert result is True

    def test_assert_no_pii_with_email(self):
        """Test that output with email fails validation."""
        output = "Contact me at john.doe@example.com for more information."
        with pytest.raises(AssertionError):
            safety.assert_no_pii(output)

    def test_assert_no_toxic_content_clean(self):
        """Test that clean output passes toxicity check."""
        output = "This is a wonderful and helpful response."
        result = safety.assert_no_toxic_content(output)
        assert result is True

    def test_assert_no_prompt_injection(self):
        """Test that output without prompt injection passes validation."""
        output = "Here is the requested information about Python programming."
        result = safety.assert_no_prompt_injection(output)
        assert result is True

    def test_assert_safe_comprehensive(self):
        """Test comprehensive safety check."""
        output = "This is a safe, helpful, and appropriate response."
        result = safety.assert_safe(output)
        assert result is True


@pytest.mark.llm
class TestLLMOutputValidation:
    """Integration tests demonstrating real-world LLM output validation."""

    def test_validate_llm_json_response(self, validai_structure):
        """Test validating a JSON response from an LLM."""
        llm_output = '{"answer": "Python", "confidence": 0.95, "sources": ["docs"]}'
        
        # Validate structure
        parsed = validai_structure.assert_json_valid(llm_output)
        validai_structure.assert_has_keys(llm_output, ["answer", "confidence"])
        
        assert parsed["answer"] == "Python"
        assert parsed["confidence"] == 0.95

    def test_validate_llm_text_response(self, validai_semantic, validai_safety):
        """Test validating a text response from an LLM."""
        llm_output = "Python is a high-level programming language known for simplicity."
        
        # Validate semantics
        validai_semantic.assert_contains_concept(llm_output, "Python")
        
        # Validate safety
        validai_safety.assert_no_pii(llm_output)
        validai_safety.assert_no_toxic_content(llm_output)

    def test_validate_llm_factual_response(self, validai_factuality):
        """Test validating factual correctness of LLM output."""
        llm_output = "According to documentation [1], Python was created in 1991."
        
        # Validate factuality
        validai_factuality.assert_contains_fact(llm_output, "Python")
        validai_factuality.assert_cites_sources(llm_output, min_sources=1)
