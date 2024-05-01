from Crypto.Cipher import AES, DES3, ARC4
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import json

class CryptographyManager:
    def __init__(self):
        self.supported_ciphers = {
            'AES': AES,
            '3DES': DES3,
            'RC4': ARC4
        }
        self.keys = {
            'AES': get_random_bytes(32),
            '3DES': DES3.adjust_key_parity(get_random_bytes(24)),
            'RC4': get_random_bytes(16)
        }
        self.block_size = AES.block_size

    def encrypt(self, plaintext, cipher_type):
        if cipher_type not in self.supported_ciphers:
            raise ValueError(f"Unsupported cipher type: {cipher_type}")

        cipher = self.supported_ciphers[cipher_type].new(self.keys[cipher_type], AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plaintext.encode(), self.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        result = json.dumps({'iv': iv, 'ciphertext': ct})
        return result

    def decrypt(self, enc_dict, cipher_type):
        if cipher_type not in self.supported_ciphers:
            raise ValueError(f"Unsupported cipher type: {cipher_type}")

        try:
            enc_dict = json.loads(enc_dict)
            iv = b64decode(enc_dict['iv'])
            ct = b64decode(enc_dict['ciphertext'])
            cipher = self.supported_ciphers[cipher_type].new(self.keys[cipher_type], AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ct), self.block_size).decode('utf-8')
            return plaintext
        except (ValueError, KeyError):
            raise ValueError("Incorrect decryption")

    def solve_classic_cipher(self, ciphertext, cipher_type):
        # Placeholder for classic cipher solving logic
        # This should be replaced with actual implementation
        if cipher_type == 'Caesar':
            # Implement Caesar cipher decryption logic
            pass
        elif cipher_type == 'Transposition':
            # Implement Transposition cipher decryption logic
            pass
        else:
            raise ValueError(f"Unsupported classic cipher type: {cipher_type}")
        return "Decrypted message"

# Example usage:
crypto_manager = CryptographyManager()
plaintext = "Secret Message"
cipher_type = 'AES'

encrypted = crypto_manager.encrypt(plaintext, cipher_type)
print(f"Encrypted: {encrypted}")

decrypted = crypto_manager.decrypt(encrypted, cipher_type)
print(f"Decrypted: {decrypted}")

# Solve classic cipher
ciphertext = "Vjku ku pqv vtcpurgt"
solved_message = crypto_manager.solve_classic_cipher(ciphertext, 'Caesar')
print(f"Solved Classic Cipher: {solved_message}")