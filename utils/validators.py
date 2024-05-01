import re
from jsonschema import validate, ValidationError
from dataclasses import dataclass

@dataclass
class ValidationSchemas:
    UserSchema: dict = {
        "type": "object",
        "properties": {
            "username": {"type": "string"},
            "password": {"type": "string"},
            "privileges": {"type": "array", "items": {"type": "string"}},
            "api_key": {"type": "string"}
        },
        "required": ["username", "password", "privileges", "api_key"]
    }
    ConfigSchema: dict = {
        "type": "object",
        "properties": {
            "logging_level": {"type": "string", "enum": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]},
            "update_interval": {"type": "number"},
            "threat_detection": {"type": "object"}
        },
        "required": ["logging_level", "update_interval", "threat_detection"]
    }
    UpdateSchema: dict = {
        "type": "object",
        "properties": {
            "version": {"type": "string"},
            "files": {"type": "array", "items": {"type": "string"}},
            "checksum": {"type": "string"}
        },
        "required": ["version", "files", "checksum"]
    }

def validate_user_data(data):
    try:
        validate(instance=data, schema=ValidationSchemas.UserSchema)
        return True
    except ValidationError as e:
        print(f"User data validation error: {e}")
        return False

def validate_config_data(data):
    try:
        validate(instance=data, schema=ValidationSchemas.ConfigSchema)
        return True
    except ValidationError as e:
        print(f"Config data validation error: {e}")
        return False

def validate_update_data(data):
    try:
        validate(instance=data, schema=ValidationSchemas.UpdateSchema)
        return True
    except ValidationError as e:
        print(f"Update data validation error: {e}")
        return False

def is_valid_api_key(api_key):
    # Assuming API key is a 32 character hex string
    return bool(re.match(r'^[a-f0-9]{32}$', api_key))

def is_valid_privilege(privilege):
    # Assuming a predefined set of privileges
    valid_privileges = ['admin', 'user', 'guest', 'red_team']
    return privilege in valid_privileges

# Additional validators can be added here as needed for other functionalities and data types.