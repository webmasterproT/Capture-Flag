import json
import os
from datetime import datetime
from utils.helpers import generate_unique_identifier, log_activity
from utils.constants import FORENSIC_ARTIFACTS, USER_ACTIVITY_LOGS
from forensics import analyze_log_files, network_packet_capture_analysis

class ForensicChallenge:
    def __init__(self, challenge_id=None):
        self.challenge_id = challenge_id or generate_unique_identifier()
        self.artifacts = []
        self.results = {}
        self.start_time = datetime.now()
        self.end_time = None

    def load_challenge(self, challenge_path):
        with open(challenge_path, 'r') as file:
            self.artifacts = json.load(file)

    def start_challenge(self):
        log_activity(USER_ACTIVITY_LOGS, f"Forensic challenge {self.challenge_id} started at {self.start_time}")
        for artifact in self.artifacts:
            if artifact['type'] == 'log_file':
                self.results[artifact['name']] = analyze_log_files(artifact['data'])
            elif artifact['type'] == 'network_capture':
                self.results[artifact['name']] = network_packet_capture_analysis(artifact['data'])
            else:
                log_activity(USER_ACTIVITY_LOGS, f"Unknown artifact type: {artifact['type']}")

    def complete_challenge(self):
        self.end_time = datetime.now()
        duration = self.end_time - self.start_time
        log_activity(USER_ACTIVITY_LOGS, f"Forensic challenge {self.challenge_id} completed in {duration}")
        return self.results

    def save_results(self):
        results_path = os.path.join('data', 'forensic_investigation_reports', f"{self.challenge_id}_results.json")
        with open(results_path, 'w') as file:
            json.dump(self.results, file, default=str)
        log_activity(USER_ACTIVITY_LOGS, f"Results for forensic challenge {self.challenge_id} saved to {results_path}")

if __name__ == "__main__":
    challenge = ForensicChallenge()
    challenge.load_challenge('data/forensic_challenges.json')
    challenge.start_challenge()
    results = challenge.complete_challenge()
    challenge.save_results()