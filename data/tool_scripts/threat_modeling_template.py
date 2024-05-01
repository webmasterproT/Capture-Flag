import json
import requests
from utils.constants import API_KEY, MITRE_ATTACK, THREAT_INDICATORS
from utils.helpers import initialize_system, log_activity, update_configuration
from ai_integration import query_ai_for_threat_modeling

def threat_modeling_template(api_key=API_KEY, threat_indicators=THREAT_INDICATORS, mitre_attack=MITRE_ATTACK):
    # Ensure the system is initialized with the necessary configurations
    system_status = initialize_system(api_key)
    if not system_status:
        raise SystemError("Failed to initialize the threat modeling system.")

    # Load threat indicators and MITRE ATT&CK framework data
    with open(threat_indicators, 'r') as ti_file:
        threat_indicators_data = json.load(ti_file)
    with open(mitre_attack, 'r') as ma_file:
        mitre_attack_data = json.load(ma_file)

    # Query the AI for threat modeling based on current threat indicators and MITRE ATT&CK data
    ai_threat_model = query_ai_for_threat_modeling(api_key, threat_indicators_data, mitre_attack_data)

    # Log the threat model obtained from AI
    log_activity("Threat modeling completed with AI assistance.", ai_threat_model)

    # Update system configuration with the latest threat model
    update_configuration("threat_model", ai_threat_model)

    # Return the threat model for further processing or action
    return ai_threat_model

if __name__ == "__main__":
    # Run the threat modeling template with the provided API key and data files
    threat_model = threat_modeling_template()
    print("Threat Model Generated:", threat_model)