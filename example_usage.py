"""
Example usage of validai for testing LLM outputs.

This script demonstrates basic usage of the validai package.
"""

from validai import structure, semantic, factuality, safety


def test_json_output():
    """Example: Testing JSON output from an LLM."""
    llm_output = '{"answer": "Paris", "confidence": 0.95, "sources": ["wiki"]}'
    
    # Validate structure
    data = structure.assert_json_valid(llm_output)
    print(f"✓ JSON is valid: {data}")
    
    structure.assert_has_keys(llm_output, ["answer", "confidence"])
    print("✓ Required keys present")


def test_text_output():
    """Example: Testing text output from an LLM."""
    llm_output = "Python is a high-level programming language known for its simplicity."
    
    # Validate semantics
    semantic.assert_contains_concept(llm_output, "Python")
    print("✓ Contains expected concept")
    
    reference = "Python is a programming language that emphasizes readability."
    semantic.assert_similar(llm_output, reference, threshold=0.3)
    print("✓ Semantically similar to reference")


def test_factual_output():
    """Example: Testing factual content from an LLM."""
    llm_output = "According to documentation [1], Python was created in 1991."
    
    # Validate factuality
    factuality.assert_contains_fact(llm_output, "Python")
    print("✓ Contains expected facts")
    
    factuality.assert_cites_sources(llm_output, min_sources=1)
    print("✓ Cites sources properly")


def test_safe_output():
    """Example: Testing safety of LLM output."""
    llm_output = "This is a helpful and safe response about programming."
    
    # Validate safety
    safety.assert_no_pii(llm_output)
    print("✓ No PII detected")
    
    safety.assert_no_toxic_content(llm_output)
    print("✓ No toxic content")
    
    safety.assert_safe(llm_output)
    print("✓ Comprehensive safety check passed")


if __name__ == "__main__":
    print("ValidAI Example Usage\n" + "=" * 50)
    
    print("\n1. Testing JSON Output:")
    test_json_output()
    
    print("\n2. Testing Text Output:")
    test_text_output()
    
    print("\n3. Testing Factual Output:")
    test_factual_output()
    
    print("\n4. Testing Safe Output:")
    test_safe_output()
    
    print("\n" + "=" * 50)
    print("All examples passed! ✓")
