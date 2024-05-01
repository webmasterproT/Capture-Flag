import json
import requests
from utils.constants import API_KEY, DETECTION_RULES, THREAT_INDICATORS
from utils.helpers import log_activity, send_alert
from utils.parsers import parse_detection_logs

class DetectionEngine:
    def __init__(self):
        self.api_key = API_KEY
        self.detection_rules = self.load_detection_rules()
        self.threat_indicators = self.load_threat_indicators()

    def load_detection_rules(self):
        with open(DETECTION_RULES, 'r') as file:
            return json.load(file)

    def load_threat_indicators(self):
        with open(THREAT_INDICATORS, 'r') as file:
            return json.load(file)

    def monitor_traffic(self, traffic_data):
        for rule in self.detection_rules:
            if self.match_rule(traffic_data, rule):
                self.handle_detection(rule, traffic_data)

    def match_rule(self, traffic_data, rule):
        # Implement complex logic to match traffic data with detection rules
        return any(indicator in traffic_data for indicator in self.threat_indicators)

    def handle_detection(self, rule, traffic_data):
        log_activity(f"Detection occurred: {rule['name']}")
        send_alert(f"Threat detected based on rule: {rule['name']}")
        self.report_to_dashboard(rule, traffic_data)

    def report_to_dashboard(self, rule, traffic_data):
        # Send the detection details to the dashboard for user review
        detection_log = parse_detection_logs(rule, traffic_data)
        dashboard_endpoint = "http://localhost:8000/api/detections"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(dashboard_endpoint, headers=headers, json=detection_log)
        if response.status_code == 200:
            log_activity("Detection reported to dashboard successfully.")
        else:
            log_activity("Failed to report detection to dashboard.")

if __name__ == "__main__":
    detection_engine = DetectionEngine()
    # Example traffic data, in a real scenario this would come from network monitoring tools
    example_traffic_data = "Suspicious activity detected on port 22"
    detection_engine.monitor_traffic(example_traffic_data)