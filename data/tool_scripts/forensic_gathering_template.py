import json
import os
from datetime import datetime
from utils.helpers import generate_unique_filename, execute_shell_command
from utils.constants import FORENSIC_ARTIFACTS, LOGGING_POLICY, USER_ACTIVITY_LOGS

class ForensicGathering:
    def __init__(self, api_key):
        self.api_key = api_key
        self.forensic_data_path = FORENSIC_ARTIFACTS
        self.logging_policy = LOGGING_POLICY
        self.user_activity_logs = USER_ACTIVITY_LOGS

    def log_activity(self, activity):
        with open(self.user_activity_logs, 'a') as log_file:
            timestamp = datetime.now().isoformat()
            log_entry = {'timestamp': timestamp, 'activity': activity}
            json.dump(log_entry, log_file)
            log_file.write('\n')

    def gather_artifacts(self, target_directory):
        artifacts = []
        for root, dirs, files in os.walk(target_directory):
            for file in files:
                artifact_path = os.path.join(root, file)
                artifacts.append(artifact_path)
                self.log_activity(f"Artifact gathered: {artifact_path}")
        return artifacts

    def analyze_artifacts(self, artifacts):
        analysis_results = {}
        for artifact in artifacts:
            result = execute_shell_command(f"file {artifact}")
            analysis_results[artifact] = result
            self.log_activity(f"Artifact analyzed: {artifact}")
        return analysis_results

    def save_forensic_data(self, analysis_results):
        unique_filename = generate_unique_filename(self.forensic_data_path, 'forensic_data', 'json')
        with open(unique_filename, 'w') as forensic_file:
            json.dump(analysis_results, forensic_file)
        self.log_activity(f"Forensic data saved: {unique_filename}")

    def execute(self, target_directory):
        self.log_activity("Forensic gathering started.")
        artifacts = self.gather_artifacts(target_directory)
        analysis_results = self.analyze_artifacts(artifacts)
        self.save_forensic_data(analysis_results)
        self.log_activity("Forensic gathering completed.")

if __name__ == "__main__":
    api_key = json.load(open('data/api_keys.json')).get('forensic_api_key')
    target_directory = '/path/to/target/directory'  # This should be replaced with the actual target directory
    forensic_gathering = ForensicGathering(api_key)
    forensic_gathering.execute(target_directory)