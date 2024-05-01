```python
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64decode, b64encode
from utils.constants import CRYPTO_CHALLENGES
from utils.helpers import load_data_from_json

class CryptoSolver:
    def __init__(self):
        self.challenges = load_data_from_json(CRYPTO_CHALLENGES)

    def solve_challenge(self, challenge_id):
        challenge = self.challenges.get(challenge_id)
        if not challenge:
            return f"No challenge found with ID: {challenge_id}"

        challenge_type = challenge.get('type')
        if challenge_type == 'classic':
            return self.solve_classic(challenge)
        elif challenge_type == 'modern':
            return self.solve_modern(challenge)
        else:
            return "Unsupported challenge type"

    def solve_classic(self, challenge):
        # Implement classic cipher solving algorithms like Caesar, transposition, etc.
        # This is a placeholder for the actual implementation
        return "Classic cipher solved"

    def solve_modern(self, challenge):
        # Implement modern cipher solving algorithms like AES, 3DES, RC4, Twofish, etc.
        # This is a placeholder for the actual implementation
        cipher_data = challenge.get('cipher_data')
        key = challenge.get('key')
        iv = challenge.get('iv')
        algorithm = challenge.get('algorithm')

        if algorithm == 'AES':
            return self.decrypt_aes(cipher_data, key, iv)
        elif algorithm == '3DES':
            return self.decrypt_3des(cipher_data, key, iv)
        # Add other algorithms as needed
        else:
            return "Unsupported modern algorithm"

    def decrypt_aes(self, cipher_data, key, iv):
        cipher_data = b64decode(cipher_data)
        key = b64decode(key)
        iv = b64decode(iv)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(cipher_data) + decryptor.finalize()

    def decrypt_3des(self, cipher_data, key, iv):
        cipher_data = b64decode(cipher_data)
        key = b64decode(key)
        iv = b64decode(iv)
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(cipher_data) + decryptor.finalize()

    # Add other decryption methods as needed

# Example usage:
# crypto_solver = CryptoSolver()
# result = crypto_solver.solve_challenge('challenge_id_123')
# print(result)
```

This code provides a basic structure for the `crypto_solver.py` file, which includes a class `CryptoSolver` that can load cryptographic challenges from a JSON file and solve them based on their type (classic or modern). The `solve_classic` and `solve_modern` methods are placeholders and should be implemented with actual algorithms for solving the respective types of ciphers. The `decrypt_aes` and `decrypt_3des` methods provide examples of how to decrypt modern ciphers using the `cryptography` library in Python.