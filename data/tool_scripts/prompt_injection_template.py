import json
import requests
from utils.constants import AI_QUERY_LOGS, AI_RESPONSES, AI_PROMPTS

def prompt_injection(api_key, target_system, injection_payload):
    """
    Perform prompt injection on the target system using AI-generated payloads.

    :param api_key: The API key for AI service authentication.
    :param target_system: Information about the target system for injection.
    :param injection_payload: The payload to be injected into the target system.
    :return: The result of the injection attempt.
    """
    # Define the headers for the API request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Define the API endpoint for prompt injection
    ai_endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

    # Prepare the data for the AI query
    ai_query = {
        'prompt': f"Perform prompt injection on the following system: {json.dumps(target_system)}\n\n{injection_payload}",
        'max_tokens': 150,
        'temperature': 0.0
    }

    # Send the request to the AI service
    response = requests.post(ai_endpoint, headers=headers, json=ai_query)

    # Log the AI query
    with open(AI_QUERY_LOGS, 'a') as log_file:
        log_file.write(json.dumps({'query': ai_query, 'timestamp': response.headers.get('Date')}))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the AI response
        ai_response = response.json()
        injection_result = ai_response.get('choices', [{}])[0].get('text', '')

        # Log the AI response
        with open(AI_RESPONSES, 'a') as response_file:
            response_file.write(json.dumps({'response': ai_response, 'timestamp': response.headers.get('Date')}))

        # Return the result of the injection attempt
        return injection_result
    else:
        # Log the failed attempt
        with open(AI_PROMPTS, 'a') as error_log:
            error_log.write(json.dumps({'error': response.text, 'timestamp': response.headers.get('Date')}))

        # Return an error message
        return f"Failed to perform prompt injection: {response.text}"

# Example usage:
# api_key = 'your-api-key'
# target_system = {'system': 'target-system-details'}
# injection_payload = 'injection-payload-details'
# result = prompt_injection(api_key, target_system, injection_payload)
# print(result)