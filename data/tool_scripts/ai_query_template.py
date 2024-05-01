import json
import requests
from utils.constants import API_KEY, AI_QUERY_LOGS

class AIQueryEngine:
    def __init__(self):
        self.api_key = API_KEY
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})

    def query_ai(self, prompt, max_tokens=100):
        """
        Send a query to the AI with a given prompt and return the response.
        """
        endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
        data = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": 0.5,
            "top_p": 1.0,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
            "stop": ["\n"]
        }
        response = self.session.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()

    def log_query(self, prompt, response):
        """
        Log the AI query and response to a file for later review.
        """
        log_entry = {
            "prompt": prompt,
            "response": response,
            "timestamp": datetime.now().isoformat()
        }
        with open(AI_QUERY_LOGS, 'a') as log_file:
            json.dump(log_entry, log_file)
            log_file.write('\n')

    def execute_query(self, prompt):
        """
        Execute a query to the AI and log the results.
        """
        response = self.query_ai(prompt)
        self.log_query(prompt, response)
        return response

# Example usage:
if __name__ == "__main__":
    ai_query_engine = AIQueryEngine()
    prompt = "Create a secure connection to a remote server using SSH."
    response = ai_query_engine.execute_query(prompt)
    print(response['choices'][0]['text'])