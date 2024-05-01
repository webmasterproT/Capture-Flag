import json
import os

# Define the path for the JSON data files
DATA_DIR = "data"
API_KEYS_FILE = os.path.join(DATA_DIR, "api_keys.json")
USER_PREFERENCES_FILE = os.path.join(DATA_DIR, "user_preferences.json")
CONFIG_DEFAULTS_FILE = os.path.join(DATA_DIR, "config_defaults.json")

# Define default configuration values
DEFAULT_CONFIG = {
    "api_key": "",
    "user_preferences": {},
    "update_manifest": {},
    "threat_indicators": {},
    "sigma_rules": {},
    "mitre_attack": {},
    "adversary_kill_chains": {},
    "logging_policy": {},
    "detection_rules": {},
    "forensic_artifacts": {},
    "ctf_scenarios": {},
    "red_team_tools": {},
    "exploit_payloads": {},
    "reverse_engineering_samples": {},
    "steganography_samples": {},
    "osint_sources": {},
    "crypto_challenges": {},
    "programming_challenges": {},
    "debugging_scenarios": {},
    "incident_response_templates": {},
    "risk_assessment_models": {},
    "cyber_capabilities": {},
    "privilege_escalation_vectors": {},
    "injection_vectors": {},
    "rce_samples": {},
    "packet_monitoring_filters": {},
    "post_mortem_templates": {},
    "ai_prompts": {},
    "ai_responses": {},
    "ai_query_logs": {},
    "user_activity_logs": {},
    "system_integrity_checks": {},
    "operational_parameters": {},
    "user_defined_goals": {},
    "attack_simulation_results": {},
    "forensic_investigation_reports": {},
    "threat_hunting_logs": {},
    "risk_analysis_reports": {},
    "incident_response_logs": {},
    "data_collection_records": {},
    "detection_logs": {},
    "forensic_evidence": {},
    "critical_infrastructure_protection_plans": {},
    "prompt_injection_cases": {},
    "sql_injection_cases": {},
    "xss_injection_cases": {},
    "xpath_injection_cases": {},
    "command_control_scenarios": {},
    "discovery_methods": {},
    "credential_access_techniques": {},
    "lateral_movement_strategies": {},
    "privilege_escalation_methods": {},
    "rce_techniques": {},
    "crypto_puzzles": {},
    "programming_problems": {},
    "osint_challenges": {},
    "reverse_engineering_challenges": {},
    "forensic_challenges": {},
    "steganography_challenges": {}
}

class ConfigManager:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        # Load the configuration from the JSON files
        config = DEFAULT_CONFIG.copy()
        config.update(self.load_json_data(API_KEYS_FILE))
        config.update(self.load_json_data(USER_PREFERENCES_FILE))
        config.update(self.load_json_data(CONFIG_DEFAULTS_FILE))
        return config

    @staticmethod
    def load_json_data(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def get_api_key(self):
        return self.config.get('api_key', '')

    def get_user_preferences(self):
        return self.config.get('user_preferences', {})

    def save_config(self):
        # Save the current configuration to the JSON files
        self.save_json_data(API_KEYS_FILE, {'api_key': self.get_api_key()})
        self.save_json_data(USER_PREFERENCES_FILE, self.get_user_preferences())

    @staticmethod
    def save_json_data(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

# Instantiate the ConfigManager
config_manager = ConfigManager()

# Example usage
api_key = config_manager.get_api_key()
user_preferences = config_manager.get_user_preferences()
# ... perform operations using the configuration data
# Save any changes to the configuration
config_manager.save_config()