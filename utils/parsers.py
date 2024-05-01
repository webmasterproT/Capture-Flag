```python
import json
from jsonschema import validate, ValidationError
from dataclasses import dataclass
from typing import Any, Dict, Optional

# Importing schemas from shared dependencies
from utils.constants import (
    UserSchema,
    ConfigSchema,
    UpdateSchema,
    ThreatIndicatorSchema,
    SigmaRuleSchema,
    MitreAttackSchema,
    KillChainSchema,
    LoggingSchema,
    DetectionRuleSchema,
    ForensicArtifactSchema,
    CtfScenarioSchema,
    ToolSchema,
    ExploitPayloadSchema,
    SampleSchema,
    SourceSchema,
    ChallengeSchema,
    ScenarioSchema,
    TemplateSchema,
    FilterSchema,
    LogSchema,
    IntegrityCheckSchema,
    ParameterSchema,
    GoalSchema,
    ResultSchema,
    ReportSchema,
    PlanSchema,
    CaseSchema,
    TechniqueSchema,
    PuzzleSchema,
    ProblemSchema,
    ChallengeTemplateSchema
)

@dataclass
class ParsedData:
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

def load_json_file(file_path: str) -> ParsedData:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return ParsedData(data=data)
    except FileNotFoundError:
        return ParsedData(error=f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        return ParsedData(error=f"Invalid JSON format: {e}")

def validate_json_data(data: Dict[str, Any], schema: Dict[str, Any]) -> ParsedData:
    try:
        validate(instance=data, schema=schema)
        return ParsedData(data=data)
    except ValidationError as e:
        return ParsedData(error=f"JSON validation error: {e}")

def parse_user_data(file_path: str) -> ParsedData:
    parsed_data = load_json_file(file_path)
    if parsed_data.error:
        return parsed_data
    return validate_json_data(parsed_data.data, UserSchema)

def parse_config_data(file_path: str) -> ParsedData:
    parsed_data = load_json_file(file_path)
    if parsed_data.error:
        return parsed_data
    return validate_json_data(parsed_data.data, ConfigSchema)

# Additional parse functions for other schemas can be added here following the same pattern

# Example usage:
# user_data = parse_user_data('data/user_preferences.json')
# if user_data.error:
#     print(f"Error parsing user data: {user_data.error}")
# else:
#     print(f"User data loaded successfully: {user_data.data}")
```

This `utils/parsers.py` module provides functionality to load and validate JSON data against predefined schemas. It uses the `jsonschema` library to validate the data and returns a `ParsedData` object containing either the data or an error message. Additional parsing functions can be added for other schemas following the same pattern.