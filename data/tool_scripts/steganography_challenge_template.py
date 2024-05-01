import os
import base64
from PIL import Image
from io import BytesIO
from steganography_tools import extract_message_from_image

def steganography_challenge():
    # Load the challenge parameters
    challenge_image_path = 'data/steganography_samples/challenge_image.png'
    expected_message = 'data/steganography_samples/expected_message.txt'

    # Check if the challenge image exists
    if not os.path.exists(challenge_image_path):
        raise FileNotFoundError(f"Challenge image not found at {challenge_image_path}")

    # Check if the expected message file exists
    if not os.path.exists(expected_message):
        raise FileNotFoundError(f"Expected message file not found at {expected_message}")

    # Read the expected message
    with open(expected_message, 'r') as file:
        expected_message_content = file.read().strip()

    # Extract the hidden message from the image
    hidden_message = extract_message_from_image(challenge_image_path)

    # Check if the extracted message matches the expected message
    if hidden_message == expected_message_content:
        print("Steganography challenge solved successfully.")
        return True
    else:
        print("Failed to solve the steganography challenge.")
        return False

def extract_message_from_image(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to bytes
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()

        # Decode the hidden message
        hidden_data = base64.b64decode(img_bytes)
        hidden_message = hidden_data.decode('utf-8')

        # Return the hidden message
        return hidden_message

if __name__ == "__main__":
    # Run the steganography challenge
    steganography_challenge()