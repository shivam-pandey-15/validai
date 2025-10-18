"""
Semantic validation module for validai.

This module provides assertions for validating semantic properties of LLM outputs,
including similarity, relevance, and meaning preservation.
"""

from typing import Optional


def assert_similar(output: str, reference: str, threshold: float = 0.8) -> bool:
    """
    Assert that two texts are semantically similar.

    Args:
        output: LLM output to compare
        reference: Reference text to compare against
        threshold: Similarity threshold (0.0 to 1.0)

    Returns:
        True if texts are similar above threshold

    Raises:
        AssertionError: If similarity is below threshold

    Note:
        This is a placeholder implementation. In production, this would use
        embeddings models (e.g., sentence-transformers) for true semantic similarity.
    """
    # Simple word overlap similarity for demonstration
    output_words = set(output.lower().split())
    reference_words = set(reference.lower().split())
    
    if not output_words or not reference_words:
        raise AssertionError("Cannot compute similarity for empty strings")
    
    intersection = output_words.intersection(reference_words)
    union = output_words.union(reference_words)
    
    similarity = len(intersection) / len(union) if union else 0.0
    
    if similarity < threshold:
        raise AssertionError(
            f"Semantic similarity {similarity:.2f} below threshold {threshold:.2f}"
        )
    
    return True


def assert_contains_concept(output: str, concept: str) -> bool:
    """
    Assert that the output contains a specific concept or topic.

    Args:
        output: LLM output to check
        concept: Concept or topic to search for

    Returns:
        True if concept is present

    Raises:
        AssertionError: If concept is not found

    Note:
        This is a simple keyword-based check. Production would use NLP
        techniques for concept detection.
    """
    concept_lower = concept.lower()
    output_lower = output.lower()
    
    if concept_lower not in output_lower:
        raise AssertionError(f"Concept '{concept}' not found in output")
    
    return True


def assert_relevant_to(output: str, query: str, threshold: float = 0.5) -> bool:
    """
    Assert that the output is relevant to a given query.

    Args:
        output: LLM output to check
        query: Query or prompt to check relevance against
        threshold: Relevance threshold (0.0 to 1.0)

    Returns:
        True if output is relevant

    Raises:
        AssertionError: If relevance is below threshold

    Note:
        This uses simple word overlap. Production would use semantic search models.
    """
    query_words = set(query.lower().split())
    output_words = set(output.lower().split())
    
    if not query_words:
        raise ValueError("Query cannot be empty")
    
    overlap = query_words.intersection(output_words)
    relevance = len(overlap) / len(query_words) if query_words else 0.0
    
    if relevance < threshold:
        raise AssertionError(
            f"Relevance score {relevance:.2f} below threshold {threshold:.2f}"
        )
    
    return True


def assert_tone(output: str, expected_tone: str) -> bool:
    """
    Assert that the output has a specific tone.

    Args:
        output: LLM output to check
        expected_tone: Expected tone (e.g., 'formal', 'casual', 'professional')

    Returns:
        True if tone matches

    Raises:
        AssertionError: If tone doesn't match

    Note:
        This is a placeholder. Production would use sentiment analysis
        and style classification models.
    """
    # Simple heuristics for demonstration
    tone_indicators = {
        "formal": ["therefore", "furthermore", "consequently", "however"],
        "casual": ["hey", "yeah", "cool", "awesome", "gonna"],
        "professional": ["please", "kindly", "regarding", "sincerely"],
    }
    
    expected_tone_lower = expected_tone.lower()
    if expected_tone_lower not in tone_indicators:
        raise ValueError(f"Unsupported tone: {expected_tone}")
    
    output_lower = output.lower()
    indicators = tone_indicators[expected_tone_lower]
    
    found = any(indicator in output_lower for indicator in indicators)
    
    if not found:
        raise AssertionError(
            f"Output does not appear to have {expected_tone} tone"
        )
    
    return True
