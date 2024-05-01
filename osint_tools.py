```python
import requests
from bs4 import BeautifulSoup
import json
import re
from utils.constants import OSINT_SOURCES
from utils.helpers import search_social_media, search_public_records, search_web_pages

class OSINTTools:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_social_media_profiles(self, username):
        results = search_social_media(username)
        return results

    def search_public_databases(self, query):
        results = search_public_records(query)
        return results

    def web_content_search(self, query):
        results = search_web_pages(query)
        return results

    def gather_intelligence(self, target):
        intelligence_data = {
            'social_media': self.search_social_media_profiles(target),
            'public_records': self.search_public_databases(target),
            'web_content': self.web_content_search(target)
        }
        return intelligence_data

    def save_intelligence_data(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_osint_sources(self):
        with open(OSINT_SOURCES, 'r') as file:
            sources = json.load(file)
        return sources

    def perform_osint(self, target):
        sources = self.load_osint_sources()
        intelligence = {}
        for source in sources:
            if source['type'] == 'social_media':
                intelligence[source['name']] = self.search_social_media_profiles(target)
            elif source['type'] == 'public_records':
                intelligence[source['name']] = self.search_public_databases(target)
            elif source['type'] == 'web_content':
                intelligence[source['name']] = self.web_content_search(target)
        return intelligence

# Example usage
if __name__ == "__main__":
    osint = OSINTTools(api_key='YOUR_API_KEY')
    target_info = osint.perform_osint('target_identifier')
    osint.save_intelligence_data(target_info, 'target_intelligence.json')
```