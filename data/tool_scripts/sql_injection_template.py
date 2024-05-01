import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

# Shared dependencies
from utils.constants import INJECTION_VECTORS, USER_ACTIVITY_LOGS
from utils.helpers import log_activity, generate_random_string
from utils.validators import is_valid_url

class SQLInjectionTemplate:
    def __init__(self, target_url, api_key):
        self.target_url = target_url
        self.api_key = api_key
        self.session = requests.Session()
        self.payloads = INJECTION_VECTORS['sql_injection_cases']

    def test_sql_injection(self):
        if not is_valid_url(self.target_url):
            raise ValueError("Invalid URL provided for SQL Injection testing.")

        for payload in self.payloads:
            encoded_payload = quote(payload)
            vulnerable, response = self.attempt_injection(encoded_payload)
            if vulnerable:
                log_activity(USER_ACTIVITY_LOGS, f"SQL Injection successful with payload: {payload}")
                return True, response
        return False, None

    def attempt_injection(self, payload):
        test_url = f"{self.target_url}?input={payload}"
        response = self.session.get(test_url)
        if self.is_vulnerable_response(response.text):
            return True, response
        return False, None

    @staticmethod
    def is_vulnerable_response(content):
        indicators = ['syntax error', 'mysql_fetch_array', 'You have an error in your SQL syntax']
        for indicator in indicators:
            if indicator.lower() in content.lower():
                return True
        return False

    def log_injection_attempt(self, payload, success):
        activity = {
            'action': 'SQL Injection Attempt',
            'payload': payload,
            'success': success,
            'timestamp': generate_random_string(10)  # Placeholder for actual timestamp function
        }
        log_activity(USER_ACTIVITY_LOGS, activity)

if __name__ == "__main__":
    # Example usage
    target = "http://example.com/login"
    api_key = "YOUR_API_KEY_HERE"
    sql_injection_tester = SQLInjectionTemplate(target, api_key)
    success, response = sql_injection_tester.test_sql_injection()
    if success:
        print("SQL Injection vulnerability found!")
    else:
        print("Target is not vulnerable to SQL Injection.")