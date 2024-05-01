```python
import requests
import json
from utils.constants import API_KEY, AI_QUERY_LOGS

class APIInteraction:
    def __init__(self, api_key=API_KEY):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})

    def send_query(self, endpoint, data):
        try:
            response = self.session.post(endpoint, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'An error occurred: {err}')
        return None

    def log_query(self, query_data, response_data):
        with open(AI_QUERY_LOGS, 'a') as log_file:
            log_entry = {
                'query': query_data,
                'response': response_data
            }
            log_file.write(json.dumps(log_entry) + '\n')

    def query_ai(self, prompt, max_tokens=100):
        endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'
        data = {
            'prompt': prompt,
            'max_tokens': max_tokens
        }
        response = self.send_query(endpoint, data)
        if response:
            self.log_query(data, response)
            return response.get('choices', [{}])[0].get('text', '').strip()
        return ''

# Example usage:
# api_interaction = APIInteraction()
# ai_response = api_interaction.query_ai("Create a secure connection to a database.")
# print(ai_response)
```