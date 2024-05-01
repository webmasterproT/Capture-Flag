from PIL import Image
import stepic
import io
import base64

class SteganographyTools:
    def __init__(self):
        pass

    @staticmethod
    def encode_message(image_path, message):
        """
        Encodes a message into an image using the stepic library.
        """
        # Open the image
        img = Image.open(image_path)

        # Encode the message into the image
        img_encoded = stepic.encode(img, message.encode())

        # Save the image
        output_path = image_path.split('.')[0] + '_encoded.png'
        img_encoded.save(output_path, 'PNG')

        return output_path

    @staticmethod
    def decode_message(image_path):
        """
        Decodes a message from an image using the stepic library.
        """
        # Open the image
        img = Image.open(image_path)

        # Decode the message from the image
        data = stepic.decode(img)

        return data.decode()

    @staticmethod
    def encode_message_to_base64(image_path, message):
        """
        Encodes a message into an image and returns a base64 representation.
        """
        # Open the image
        img = Image.open(image_path)

        # Encode the message into the image
        img_encoded = stepic.encode(img, message.encode())

        # Save the image to a buffer
        buffered = io.BytesIO()
        img_encoded.save(buffered, format="PNG")

        # Convert to base64
        img_base64 = base64.b64encode(buffered.getvalue())

        return img_base64.decode()

    @staticmethod
    def decode_message_from_base64(img_base64):
        """
        Decodes a message from a base64 encoded image.
        """
        # Convert base64 to bytes
        img_bytes = base64.b64decode(img_base64)

        # Read the image from the bytes
        img = Image.open(io.BytesIO(img_bytes))

        # Decode the message from the image
        data = stepic.decode(img)

        return data.decode()

# Example usage:
# steganography_tools = SteganographyTools()
# encoded_image_path = steganography_tools.encode_message('original_image.png', 'Secret Message')
# decoded_message = steganography_tools.decode_message(encoded_image_path)
# print(decoded_message)

# encoded_image_base64 = steganography_tools.encode_message_to_base64('original_image.png', 'Secret Message')
# decoded_message_from_base64 = steganography_tools.decode_message_from_base64(encoded_image_base64)
# print(decoded_message_from_base64)