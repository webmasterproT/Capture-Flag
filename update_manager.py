```python
import json
import requests
from utils.constants import UPDATE_MANIFEST, API_KEY
from utils.helpers import check_internet_connection, verify_update_signature

class UpdateManager:
    def __init__(self):
        self.update_manifest_url = "https://update.server.com/manifest.json"
        self.headers = {"Authorization": f"Bearer {API_KEY}"}

    def check_for_updates(self):
        if not check_internet_connection():
            return False, "No internet connection available."

        try:
            response = requests.get(self.update_manifest_url, headers=self.headers)
            response.raise_for_status()
            update_manifest = response.json()

            with open(UPDATE_MANIFEST, 'r') as local_manifest_file:
                local_manifest = json.load(local_manifest_file)

            if update_manifest["version"] > local_manifest["version"]:
                if verify_update_signature(update_manifest):
                    return True, update_manifest
                else:
                    return False, "Update signature verification failed."
            else:
                return False, "No new updates available."

        except requests.RequestException as e:
            return False, str(e)

    def download_update(self, update_info):
        try:
            update_url = update_info["url"]
            response = requests.get(update_url, headers=self.headers)
            response.raise_for_status()

            with open(update_info["filename"], 'wb') as update_file:
                update_file.write(response.content)

            return True, "Update downloaded successfully."

        except requests.RequestException as e:
            return False, str(e)

    def apply_update(self, filename):
        # Placeholder for update application logic
        # This should include file integrity checks, installation of new files,
        # backup of old files, and updating the local update manifest.
        pass

    def run_update_sequence(self):
        update_available, update_info_or_error = self.check_for_updates()
        if update_available:
            download_success, download_message = self.download_update(update_info_or_error)
            if download_success:
                self.apply_update(update_info_or_error["filename"])
                return True, "Update applied successfully."
            else:
                return False, download_message
        else:
            return False, update_info_or_error

# Example usage:
if __name__ == "__main__":
    update_manager = UpdateManager()
    success, message = update_manager.run_update_sequence()
    print(message)
```

This code provides a basic structure for an update manager that checks for updates, downloads them, and applies them. The actual implementation of the `apply_update` method would depend on the specifics of the application and the update process. The `verify_update_signature` function is a placeholder for the actual signature verification logic, which should be implemented to ensure the integrity and authenticity of the updates.