import unittest
from steganography_tools import SteganographyDecoder, SteganographyEncoder
from utils.helpers import generate_random_image, generate_random_message
from utils.constants import STEGANOGRAPHY_SAMPLES

class TestSteganography(unittest.TestCase):

    def setUp(self):
        self.encoder = SteganographyEncoder()
        self.decoder = SteganographyDecoder()
        self.sample_image = generate_random_image()
        self.secret_message = generate_random_message()
        self.encoded_image = None

    def test_encode_decode(self):
        # Test encoding of a message into an image
        self.encoded_image = self.encoder.encode(self.sample_image, self.secret_message)
        self.assertIsNotNone(self.encoded_image, "Encoding returned None, expected an image with encoded data.")

        # Test decoding of a message from an image
        decoded_message = self.decoder.decode(self.encoded_image)
        self.assertEqual(decoded_message, self.secret_message, "Decoded message does not match the original message.")

    def test_encode_decode_with_samples(self):
        # Test encoding and decoding with predefined samples
        for sample in STEGANOGRAPHY_SAMPLES:
            with self.subTest(sample=sample):
                image_path = sample['image_path']
                message = sample['message']
                encoded_image = self.encoder.encode(image_path, message)
                self.assertIsNotNone(encoded_image, "Encoding returned None, expected an image with encoded data.")

                decoded_message = self.decoder.decode(encoded_image)
                self.assertEqual(decoded_message, message, "Decoded message does not match the original message in sample.")

    def test_decode_without_message(self):
        # Test decoding an image without a message
        decoded_message = self.decoder.decode(self.sample_image)
        self.assertIsNone(decoded_message, "Decoded message should be None for an image without encoded data.")

    def test_decode_corrupted_image(self):
        # Test decoding a corrupted image
        corrupted_image = self.encoder.corrupt_image(self.encoded_image)
        with self.assertRaises(Exception):
            _ = self.decoder.decode(corrupted_image)

if __name__ == '__main__':
    unittest.main()