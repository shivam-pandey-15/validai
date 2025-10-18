"""
ValidAI: A pytest plugin for testing non-deterministic LLM outputs.

This package provides a robust, property-based testing framework for AI applications,
enabling reliable CI/CD by offering assertions for:
- Structure validation (JSON, XML, schemas)
- Semantic similarity and meaning
- Factuality and correctness
- Safety and PII detection
"""

__version__ = "0.1.0"
__all__ = ["structure", "semantic", "factuality", "safety"]

# Import assertion modules for convenient access
from validai import structure, semantic, factuality, safety
