# validai

**The pytest for AI 🤖**

A Python pytest plugin for robustly testing non-deterministic LLM outputs. Enable reliable CI/CD for AI applications by providing a robust, property-based testing framework for LLMs.

## 🎯 Goal

Enable reliable CI/CD for AI applications by providing a robust, property-based testing framework for LLMs. ValidAI helps you assert structure, semantics, safety, and factuality of AI-generated content with confidence.

## ✨ Features

ValidAI provides comprehensive assertion modules for validating different aspects of LLM outputs:

### 🏗️ Structure Validation
- **JSON validation**: Ensure outputs are valid JSON with required keys
- **Schema validation**: Validate against JSON schemas
- **Format checking**: Verify output format (JSON, XML, Markdown, etc.)

### 🧠 Semantic Validation
- **Similarity checking**: Assert semantic similarity between texts
- **Concept detection**: Verify presence of specific concepts or topics
- **Relevance testing**: Ensure output relevance to queries
- **Tone validation**: Check for appropriate tone (formal, casual, professional)

### ✅ Factuality Validation
- **Fact checking**: Assert presence of specific facts
- **Contradiction detection**: Identify contradictions with reference texts
- **Numerical accuracy**: Verify numerical values within tolerance
- **Source citation**: Ensure proper source attribution
- **Verifiability**: Check if claims are verifiable

### 🛡️ Safety Validation
- **PII detection**: Identify and flag personally identifiable information
- **Toxicity checking**: Detect toxic or harmful content
- **Bias detection**: Identify biased language
- **Content appropriateness**: Validate content for target audience
- **Prompt injection detection**: Detect potential security vulnerabilities

## 📦 Installation

```bash
pip install validai
```

Or install from source:

```bash
git clone https://github.com/shivam-pandey-15/validai.git
cd validai
pip install -e .
```

## 🚀 Quick Start

### Basic Usage

```python
from validai import structure, semantic, factuality, safety

# Test LLM JSON output
llm_output = '{"answer": "Python", "confidence": 0.95}'
structure.assert_json_valid(llm_output)
structure.assert_has_keys(llm_output, ["answer", "confidence"])

# Test semantic properties
text_output = "Python is a high-level programming language."
semantic.assert_contains_concept(text_output, "Python")
semantic.assert_similar(text_output, "Python is a programming language", threshold=0.7)

# Test factual correctness
factual_output = "According to research [1], Python was created in 1991."
factuality.assert_contains_fact(factual_output, "Python")
factuality.assert_cites_sources(factual_output, min_sources=1)

# Test safety
safety.assert_no_pii(llm_output)
safety.assert_no_toxic_content(llm_output)
safety.assert_safe(llm_output)  # Comprehensive safety check
```

### Using with Pytest

ValidAI automatically registers as a pytest plugin, providing fixtures:

```python
import pytest

@pytest.mark.llm
def test_llm_response(validai_structure, validai_safety):
    """Test LLM output validation."""
    llm_output = '{"response": "Hello, how can I help?"}'
    
    # Use fixtures
    validai_structure.assert_json_valid(llm_output)
    validai_safety.assert_safe(llm_output)

def test_with_all_modules(validai_all):
    """Access all validation modules."""
    output = "Safe and structured response"
    validai_all["structure"].assert_format(output, "json")
    validai_all["safety"].assert_no_pii(output)
```

## 📚 Documentation

### Structure Module

```python
from validai.structure import (
    assert_json_valid,
    assert_json_schema,
    assert_has_keys,
    assert_format,
)

# Validate JSON
data = assert_json_valid('{"key": "value"}')

# Check required keys
assert_has_keys('{"name": "Alice", "age": 30}', ["name", "age"])

# Validate format
assert_format(output, "json")  # or "xml", "markdown"
```

### Semantic Module

```python
from validai.semantic import (
    assert_similar,
    assert_contains_concept,
    assert_relevant_to,
    assert_tone,
)

# Check similarity
assert_similar(output, reference, threshold=0.8)

# Verify concept presence
assert_contains_concept(output, "machine learning")

# Check relevance
assert_relevant_to(output, query="What is Python?", threshold=0.5)

# Validate tone
assert_tone(output, "professional")
```

### Factuality Module

```python
from validai.factuality import (
    assert_contains_fact,
    assert_no_contradiction,
    assert_accurate_numbers,
    assert_cites_sources,
    assert_verifiable,
)

# Check for facts
assert_contains_fact(output, "Paris is the capital of France")

# Verify numerical accuracy
assert_accurate_numbers(output, {"temperature": 98.6}, tolerance=0.1)

# Ensure source citation
assert_cites_sources(output, min_sources=2)
```

### Safety Module

```python
from validai.safety import (
    assert_no_pii,
    assert_no_toxic_content,
    assert_no_bias,
    assert_appropriate_content,
    assert_no_prompt_injection,
    assert_safe,
)

# Check for PII
assert_no_pii(output, pii_types=["email", "phone", "ssn"])

# Verify no toxicity
assert_no_toxic_content(output, threshold=0.5)

# Check for bias
assert_no_bias(output, protected_attributes=["gender", "race"])

# Comprehensive safety check
assert_safe(output)
```

## 🧪 Testing

Run the test suite:

```bash
pytest tests/
```

Run tests with coverage:

```bash
pytest tests/ --cov=validai --cov-report=html
```

## 🛠️ Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run code formatting:

```bash
black validai/ tests/
```

Run linting:

```bash
flake8 validai/ tests/
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

ValidAI is designed to make testing AI applications more reliable and straightforward. It draws inspiration from property-based testing frameworks and adapts them for the unique challenges of LLM validation.

## 📮 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: This is an early-stage project. The validation functions provide basic implementations suitable for demonstration and testing. Production deployments should integrate specialized models and services (e.g., sentence transformers for semantic similarity, Perspective API for toxicity, Microsoft Presidio for PII detection) for more robust validation.
