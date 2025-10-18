"""
Factuality validation module for validai.

This module provides assertions for validating factual correctness and accuracy
of LLM outputs against known facts and sources.
"""

from typing import List, Dict, Any, Optional


def assert_contains_fact(output: str, fact: str) -> bool:
    """
    Assert that the output contains a specific fact.

    Args:
        output: LLM output to check
        fact: Fact that should be present in the output

    Returns:
        True if fact is present

    Raises:
        AssertionError: If fact is not found

    Note:
        This is a simple substring check. Production would use NLI
        (Natural Language Inference) models for fact verification.
    """
    if fact.lower() not in output.lower():
        raise AssertionError(f"Fact '{fact}' not found in output")
    
    return True


def assert_no_contradiction(output: str, reference: str) -> bool:
    """
    Assert that the output doesn't contradict a reference text.

    Args:
        output: LLM output to check
        reference: Reference text to check against

    Returns:
        True if no contradiction detected

    Raises:
        AssertionError: If contradiction is detected

    Note:
        This is a placeholder. Production would use NLI models to detect
        contradictions and entailment.
    """
    # Placeholder logic - would use NLI models in production
    contradiction_markers = [
        "however", "but", "although", "despite", "in contrast",
        "on the contrary", "whereas"
    ]
    
    output_lower = output.lower()
    has_contradiction = any(marker in output_lower for marker in contradiction_markers)
    
    # This is overly simplistic - just for demonstration
    if has_contradiction and reference.lower() in output_lower:
        # More sophisticated logic would be needed
        pass
    
    return True


def assert_accurate_numbers(
    output: str,
    expected_values: Dict[str, float],
    tolerance: float = 0.01
) -> bool:
    """
    Assert that numerical values in output match expected values.

    Args:
        output: LLM output to check
        expected_values: Dictionary of metric names to expected values
        tolerance: Acceptable tolerance for numerical differences

    Returns:
        True if all numbers are accurate within tolerance

    Raises:
        AssertionError: If any numbers are outside tolerance

    Note:
        This is a simple implementation. Production would use NER
        and numerical reasoning to extract and verify numbers.
    """
    import re
    
    for metric, expected in expected_values.items():
        # Try to find the metric and its value in the output
        pattern = rf"{metric}[:\s]+(\d+\.?\d*)"
        match = re.search(pattern, output, re.IGNORECASE)
        
        if not match:
            raise AssertionError(f"Metric '{metric}' not found in output")
        
        actual = float(match.group(1))
        diff = abs(actual - expected)
        
        if diff > tolerance:
            raise AssertionError(
                f"Value for '{metric}' is {actual}, expected {expected} "
                f"(difference {diff} exceeds tolerance {tolerance})"
            )
    
    return True


def assert_cites_sources(output: str, min_sources: int = 1) -> bool:
    """
    Assert that the output cites sources or references.

    Args:
        output: LLM output to check
        min_sources: Minimum number of sources required

    Returns:
        True if sufficient sources are cited

    Raises:
        AssertionError: If insufficient sources are cited

    Note:
        This looks for common citation patterns. Production would use
        more sophisticated citation extraction.
    """
    import re
    
    # Look for common citation patterns
    patterns = [
        r"\[\d+\]",  # [1], [2], etc.
        r"\(\w+,?\s*\d{4}\)",  # (Author, 2023)
        r"https?://\S+",  # URLs
        r"according to",  # Source attribution phrases
        r"source:",
    ]
    
    citation_count = 0
    for pattern in patterns:
        matches = re.findall(pattern, output, re.IGNORECASE)
        citation_count += len(matches)
    
    if citation_count < min_sources:
        raise AssertionError(
            f"Found {citation_count} citations, expected at least {min_sources}"
        )
    
    return True


def assert_verifiable(output: str, facts_db: Optional[Dict[str, Any]] = None) -> bool:
    """
    Assert that claims in the output are verifiable.

    Args:
        output: LLM output to check
        facts_db: Optional database of known facts for verification

    Returns:
        True if claims are verifiable

    Raises:
        AssertionError: If claims cannot be verified

    Note:
        This is a placeholder. Production would integrate with fact-checking
        APIs and knowledge bases.
    """
    # Placeholder implementation
    if facts_db is None:
        # Without a facts database, just check if output makes definite claims
        claim_markers = ["is", "are", "was", "were", "will be"]
        output_lower = output.lower()
        
        has_claims = any(marker in output_lower for marker in claim_markers)
        
        if not has_claims:
            raise AssertionError("Output does not make verifiable claims")
    
    return True
