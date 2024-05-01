```python
import json
import os
import datetime

# Define the path for the log file and other dependencies
LOG_FILE_PATH = "data/user_activity_logs.json"
LOGGING_POLICY = "data/logging_policy.json"

# Load the logging policy
def load_logging_policy():
    if os.path.exists(LOGGING_POLICY):
        with open(LOGGING_POLICY, 'r') as file:
            return json.load(file)
    else:
        # Default policy if the file does not exist
        return {
            "log_level": "INFO",
            "log_format": "{timestamp} - {level} - {message}",
            "timestamp_format": "%Y-%m-%d %H:%M:%S"
        }

# Function to log messages
def log_message(level, message):
    policy = load_logging_policy()
    if level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        raise ValueError("Invalid log level")

    # Check if the log level is allowed by the policy
    if level in policy.get("log_level", "INFO"):
        timestamp = datetime.datetime.now().strftime(policy.get("timestamp_format", "%Y-%m-%d %H:%M:%S"))
        log_entry = policy.get("log_format", "{timestamp} - {level} - {message}").format(timestamp=timestamp, level=level, message=message)
        
        # Append the log entry to the log file
        if os.path.exists(LOG_FILE_PATH):
            with open(LOG_FILE_PATH, 'r+') as file:
                logs = json.load(file)
                logs.append(log_entry)
                file.seek(0)
                json.dump(logs, file, indent=4)
        else:
            # Create the log file if it does not exist
            with open(LOG_FILE_PATH, 'w') as file:
                json.dump([log_entry], file, indent=4)

# Example usage of the logging function
if __name__ == "__main__":
    log_message("INFO", "Logging script template initialized")
    log_message("ERROR", "Test error message")
```