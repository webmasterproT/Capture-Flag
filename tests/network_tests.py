import unittest
from network_analysis import perform_network_analysis
from utils.constants import THREAT_INDICATORS, DETECTION_RULES
from utils.helpers import load_json_data

class TestNetworkAnalysis(unittest.TestCase):

    def setUp(self):
        # Load threat indicators and detection rules for testing
        self.threat_indicators = load_json_data(THREAT_INDICATORS)
        self.detection_rules = load_json_data(DETECTION_RULES)

    def test_network_analysis_detects_threats(self):
        # Simulate network traffic data that includes threat indicators
        simulated_traffic = {
            'source_ip': '192.168.1.100',
            'destination_ip': '10.0.0.1',
            'payload': 'malicious_payload_signature',
            'protocol': 'TCP'
        }
        
        # Perform network analysis on the simulated traffic
        analysis_result = perform_network_analysis(simulated_traffic, self.threat_indicators, self.detection_rules)
        
        # Assert that a threat was detected
        self.assertTrue(analysis_result['threat_detected'])
        self.assertIn('malicious_payload_signature', analysis_result['threat_details']['signatures'])

    def test_network_analysis_no_threats(self):
        # Simulate benign network traffic data
        benign_traffic = {
            'source_ip': '192.168.1.101',
            'destination_ip': '10.0.0.2',
            'payload': 'benign_data',
            'protocol': 'UDP'
        }
        
        # Perform network analysis on the benign traffic
        analysis_result = perform_network_analysis(benign_traffic, self.threat_indicators, self.detection_rules)
        
        # Assert that no threat was detected
        self.assertFalse(analysis_result['threat_detected'])

    def test_network_analysis_with_invalid_data(self):
        # Simulate invalid network traffic data
        invalid_traffic = {
            'source_ip': None,
            'destination_ip': '10.0.0.3',
            'payload': '',
            'protocol': 'ICMP'
        }
        
        # Perform network analysis on the invalid traffic
        with self.assertRaises(ValueError):
            perform_network_analysis(invalid_traffic, self.threat_indicators, self.detection_rules)

if __name__ == '__main__':
    unittest.main()