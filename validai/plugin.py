"""
Pytest plugin for validai.

This module registers validai as a pytest plugin, making assertion functions
available as pytest fixtures and providing custom markers.
"""

import pytest
from validai import structure, semantic, factuality, safety


def pytest_configure(config):
    """Register custom markers for validai."""
    config.addinivalue_line(
        "markers", "llm: mark test as an LLM output validation test"
    )
    config.addinivalue_line(
        "markers", "structure: mark test as validating output structure"
    )
    config.addinivalue_line(
        "markers", "semantic: mark test as validating semantic properties"
    )
    config.addinivalue_line(
        "markers", "factuality: mark test as validating factual correctness"
    )
    config.addinivalue_line(
        "markers", "safety: mark test as validating safety properties"
    )


@pytest.fixture
def validai_structure():
    """Fixture providing access to structure validation functions."""
    return structure


@pytest.fixture
def validai_semantic():
    """Fixture providing access to semantic validation functions."""
    return semantic


@pytest.fixture
def validai_factuality():
    """Fixture providing access to factuality validation functions."""
    return factuality


@pytest.fixture
def validai_safety():
    """Fixture providing access to safety validation functions."""
    return safety


@pytest.fixture
def validai_all():
    """Fixture providing access to all validai validation modules."""
    return {
        "structure": structure,
        "semantic": semantic,
        "factuality": factuality,
        "safety": safety,
    }
