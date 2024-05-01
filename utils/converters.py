```python
import json
import base64
from cryptography.fernet import Fernet
from utils.constants import CONFIG_DEFAULTS, USER_PREFERENCES

def json_to_dict(json_string):
    """
    Convert a JSON string to a dictionary.
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON string")

def dict_to_json(dictionary):
    """
    Convert a dictionary to a JSON string.
    """
    return json.dumps(dictionary, indent=4)

def base64_encode(data):
    """
    Encode data to a base64 string.
    """
    return base64.b64encode(data).decode('utf-8')

def base64_decode(data):
    """
    Decode data from a base64 string.
    """
    return base64.b64decode(data)

def encrypt_data(data, key):
    """
    Encrypt data using the provided key.
    """
    fernet = Fernet(key)
    return fernet.encrypt(data.encode('utf-8')).decode('utf-8')

def decrypt_data(encrypted_data, key):
    """
    Decrypt data using the provided key.
    """
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data.encode('utf-8')).decode('utf-8')

def load_configuration(file_path=CONFIG_DEFAULTS):
    """
    Load configuration from a JSON file.
    """
    with open(file_path, 'r') as config_file:
        return json.load(config_file)

def save_configuration(config_data, file_path=USER_PREFERENCES):
    """
    Save configuration to a JSON file.
    """
    with open(file_path, 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

def convert_sigma_rule_to_query(sigma_rule):
    """
    Convert a SIGMA rule to a query string.
    """
    # Placeholder for actual conversion logic
    return "SELECT * FROM logs WHERE " + sigma_rule

def convert_mitre_attack_to_profile(mitre_attack):
    """
    Convert a MITRE ATT&CK technique to a threat profile.
    """
    # Placeholder for actual conversion logic
    return {"technique": mitre_attack, "profile": "Threat Profile"}

def convert_kill_chain_to_workflow(kill_chain):
    """
    Convert an adversary kill chain to a workflow.
    """
    # Placeholder for actual conversion logic
    return {"kill_chain": kill_chain, "workflow": "Workflow Steps"}

# Additional converters can be added here as needed to support the application's functionality.
```