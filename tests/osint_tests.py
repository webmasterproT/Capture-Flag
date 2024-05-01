import unittest
from osint_tools import gather_osint
from utils.constants import OSINT_SOURCES
from utils.helpers import validate_osint_source
from data.osint_challenges import osint_challenges

class TestOSINT(unittest.TestCase):
    def setUp(self):
        self.sources = OSINT_SOURCES
        self.challenges = osint_challenges

    def test_gather_osint_valid_sources(self):
        for source in self.sources:
            with self.subTest(source=source):
                self.assertTrue(validate_osint_source(source), f"Invalid OSINT source: {source}")

    def test_gather_osint_results(self):
        for challenge in self.challenges:
            with self.subTest(challenge=challenge):
                result = gather_osint(challenge['source'], challenge['query'])
                self.assertIsNotNone(result, "No OSINT data returned.")
                self.assertIn('data', result, "OSINT data should have a 'data' key.")
                self.assertTrue(len(result['data']) > 0, "OSINT data should not be empty.")

    def test_gather_osint_invalid_source(self):
        invalid_source = "http://invalidsource.com"
        result = gather_osint(invalid_source, "test query")
        self.assertIsNone(result, "OSINT gathering should return None for an invalid source.")

if __name__ == '__main__':
    unittest.main()