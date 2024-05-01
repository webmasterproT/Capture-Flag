```python
import json
import requests
from utils.constants import API_KEY, DATA_COLLECTION_RECORDS
from utils.helpers import log_activity, send_alert

def collect_data(target_url, search_terms):
    """
    Collect data from the specified target URL and search for the given terms.
    """
    try:
        response = requests.get(target_url)
        response.raise_for_status()
        collected_data = response.text

        # Search for the specified terms in the collected data
        findings = {term: collected_data.count(term) for term in search_terms}
        log_activity(f"Data collection complete for {target_url}. Terms found: {findings}")

        # Save the findings
        with open(DATA_COLLECTION_RECORDS, 'a') as file:
            json.dump(findings, file)
            file.write('\n')

        return findings

    except requests.RequestException as e:
        error_message = f"Error collecting data from {target_url}: {str(e)}"
        log_activity(error_message)
        send_alert(error_message)
        return {}

def main():
    # Load user-defined operational parameters
    with open('data/operational_parameters.json') as file:
        operational_params = json.load(file)

    # Extract target information and search terms from operational parameters
    target_url = operational_params.get('target_url')
    search_terms = operational_params.get('search_terms', [])

    # Perform data collection
    if target_url and search_terms:
        findings = collect_data(target_url, search_terms)

        # If AI integration is enabled, send findings to AI for further analysis
        if operational_params.get('ai_integration_enabled'):
            ai_endpoint = operational_params.get('ai_endpoint')
            headers = {'Authorization': f'Bearer {API_KEY}'}
            ai_response = requests.post(ai_endpoint, json=findings, headers=headers)
            ai_analysis = ai_response.json()

            # Log AI analysis results
            log_activity(f"AI analysis results: {ai_analysis}")

if __name__ == "__main__":
    main()
```