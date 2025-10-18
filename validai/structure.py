"""
Structure validation module for validai.

This module provides assertions for validating the structure of LLM outputs,
including JSON validation, schema validation, and format checking.
"""

import json
from typing import Any, Dict, Optional


def assert_json_valid(output: str) -> Dict[str, Any]:
    """
    Assert that the output is valid JSON.

    Args:
        output: String output to validate as JSON

    Returns:
        Parsed JSON object

    Raises:
        AssertionError: If output is not valid JSON
    """
    try:
        return json.loads(output)
    except json.JSONDecodeError as e:
        raise AssertionError(f"Output is not valid JSON: {e}")


def assert_json_schema(output: str, schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    Assert that the output matches a JSON schema.

    Args:
        output: String output to validate
        schema: JSON schema to validate against

    Returns:
        Parsed JSON object

    Raises:
        AssertionError: If output doesn't match schema
    """
    parsed = assert_json_valid(output)
    
    # Basic schema validation (would use jsonschema library in production)
    for key in schema.get("required", []):
        if key not in parsed:
            raise AssertionError(f"Required key '{key}' not found in output")
    
    return parsed


def assert_has_keys(output: str, keys: list) -> Dict[str, Any]:
    """
    Assert that the JSON output has specific keys.

    Args:
        output: String output to validate
        keys: List of required keys

    Returns:
        Parsed JSON object

    Raises:
        AssertionError: If any required keys are missing
    """
    parsed = assert_json_valid(output)
    
    missing_keys = [key for key in keys if key not in parsed]
    if missing_keys:
        raise AssertionError(f"Missing required keys: {missing_keys}")
    
    return parsed


def assert_format(output: str, format_type: str) -> bool:
    """
    Assert that the output matches a specific format.

    Args:
        output: String output to validate
        format_type: Expected format (e.g., 'json', 'xml', 'markdown')

    Returns:
        True if format is valid

    Raises:
        AssertionError: If format doesn't match
    """
    if format_type.lower() == "json":
        assert_json_valid(output)
        return True
    elif format_type.lower() == "xml":
        # Basic XML validation (would use lxml in production)
        if not (output.strip().startswith("<") and output.strip().endswith(">")):
            raise AssertionError("Output does not appear to be valid XML")
        return True
    elif format_type.lower() == "markdown":
        # Basic markdown validation
        if not output.strip():
            raise AssertionError("Output is empty")
        return True
    else:
        raise ValueError(f"Unsupported format type: {format_type}")
