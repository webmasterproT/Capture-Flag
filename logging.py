import json
import logging
import os
from datetime import datetime

# Define the path for the log files and ensure the directory exists
LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Define the log file name with a timestamp
log_file_name = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_file_path = os.path.join(LOG_DIR, log_file_name)

# Configure the logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

# Exported variables from shared dependencies
from utils.constants import USER_ACTIVITY_LOGS

def log_activity(activity, level='info'):
    """
    Log the activity to the log file and console.

    :param activity: The activity message to log.
    :param level: The logging level ('info', 'warning', 'error', 'critical').
    """
    if level == 'info':
        logging.info(activity)
    elif level == 'warning':
        logging.warning(activity)
    elif level == 'error':
        logging.error(activity)
    elif level == 'critical':
        logging.critical(activity)
    else:
        logging.info(activity)

    # Append the activity to the user activity logs
    with open(USER_ACTIVITY_LOGS, 'a') as log_file:
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'activity': activity,
            'level': level
        }
        log_file.write(json.dumps(log_entry) + '\n')

def get_log_file_path():
    """
    Get the path of the current log file.

    :return: Path of the log file.
    """
    return log_file_path

# Example usage of the logging functions
if __name__ == "__main__":
    log_activity("Application started", level='info')
    # ... other code ...
    log_activity("An example warning message", level='warning')
    # ... other code ...
    log_activity("An example error message", level='error')
    # ... other code ...
    log_activity("Application ended", level='info')