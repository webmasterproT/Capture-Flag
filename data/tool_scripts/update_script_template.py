import json
import requests
from pathlib import Path
from utils.constants import UPDATE_MANIFEST, API_KEY

def check_for_updates(api_endpoint, headers):
    try:
        response = requests.get(api_endpoint, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error checking for updates: {e}")
        return None

def download_update(file_url, headers, destination):
    try:
        with requests.get(file_url, headers=headers, stream=True) as r:
            r.raise_for_status()
            with open(destination, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading update: {e}")
        return False

def apply_update(update_script_path):
    exec(open(update_script_path).read(), globals())

def update_system():
    update_manifest_path = Path(UPDATE_MANIFEST)
    if not update_manifest_path.is_file():
        print("Update manifest not found.")
        return

    with open(update_manifest_path, 'r') as f:
        update_manifest = json.load(f)

    api_endpoint = update_manifest.get('api_endpoint')
    headers = {'Authorization': f'Bearer {API_KEY}'}

    update_info = check_for_updates(api_endpoint, headers)
    if not update_info:
        print("No update information received.")
        return

    latest_version = update_info.get('latest_version')
    current_version = update_manifest.get('current_version')

    if latest_version != current_version:
        print(f"New update available: {latest_version}")
        file_url = update_info.get('file_url')
        update_script_path = Path(update_info.get('update_script'))

        if download_update(file_url, headers, update_script_path):
            print("Update downloaded successfully. Applying update...")
            apply_update(update_script_path)
            update_manifest['current_version'] = latest_version
            with open(update_manifest_path, 'w') as f:
                json.dump(update_manifest, f)
            print("Update applied successfully.")
        else:
            print("Failed to download the update.")
    else:
        print("System is up to date.")

if __name__ == "__main__":
    update_system()