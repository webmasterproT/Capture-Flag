import json
import os
import sys
from cryptography.fernet import Fernet

# Helper function to load JSON data from a file
def load_json_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file - {file_path}")
        sys.exit(1)

# Helper function to save JSON data to a file
def save_json_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error: Unable to write to file - {file_path}\n{str(e)}")
        sys.exit(1)

# Helper function to encrypt data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()

# Helper function to decrypt data
def decrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data.encode()).decode()

# Helper function to generate a new encryption key
def generate_encryption_key():
    return Fernet.generate_key().decode()

# Helper function to dynamically execute code
def execute_dynamic_code(code, local_vars=None):
    if local_vars is None:
        local_vars = {}
    try:
        exec(code, globals(), local_vars)
    except Exception as e:
        print(f"Error executing dynamic code: {str(e)}")
        sys.exit(1)

# Helper function to check if a port is open
def is_port_open(host, port):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# Helper function to get API key from file
def get_api_key(file_path='data/api_keys.json'):
    api_keys = load_json_data(file_path)
    return api_keys.get('API_KEY')

# Helper function to update API key in file
def update_api_key(new_key, file_path='data/api_keys.json'):
    api_keys = load_json_data(file_path)
    api_keys['API_KEY'] = new_key
    save_json_data(file_path, api_keys)

# Helper function to log user activity
def log_user_activity(activity, file_path='data/user_activity_logs.json'):
    logs = load_json_data(file_path)
    logs.append(activity)
    save_json_data(file_path, logs)

# Helper function to validate JSON data against a schema
def validate_json_data(data, schema):
    from jsonschema import validate, ValidationError
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        print(f"JSON validation error: {e.message}")
        return False

# Helper function to get system integrity checks
def get_system_integrity_checks(file_path='data/system_integrity_checks.json'):
    return load_json_data(file_path)

# Helper function to update system integrity checks
def update_system_integrity_checks(checks, file_path='data/system_integrity_checks.json'):
    save_json_data(file_path, checks)

# Helper function to parse command line arguments
def parse_cli_arguments():
    import argparse
    parser = argparse.ArgumentParser(description="Utility script for the security application.")
    parser.add_argument('--key', help='API key for the application', required=False)
    args = parser.parse_args()
    return vars(args)

# Helper function to get operational parameters
def get_operational_parameters(file_path='data/operational_parameters.json'):
    return load_json_data(file_path)

# Helper function to update operational parameters
def update_operational_parameters(params, file_path='data/operational_parameters.json'):
    save_json_data(file_path, params)

# Helper function to get user defined goals
def get_user_defined_goals(file_path='data/user_defined_goals.json'):
    return load_json_data(file_path)

# Helper function to update user defined goals
def update_user_defined_goals(goals, file_path='data/user_defined_goals.json'):
    save_json_data(file_path, goals)