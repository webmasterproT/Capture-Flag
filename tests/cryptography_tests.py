import unittest
from cryptography.py import CryptoSolver
from utils.constants import CRYPTO_CHALLENGES

class TestCryptography(unittest.TestCase):

    def setUp(self):
        self.crypto_solver = CryptoSolver()

    def test_classic_ciphers(self):
        for challenge in CRYPTO_CHALLENGES['classic']:
            with self.subTest(challenge=challenge):
                cipher_text = challenge['cipher_text']
                cipher_type = challenge['cipher_type']
                expected = challenge['expected']
                result = self.crypto_solver.solve_classic(cipher_text, cipher_type)
                self.assertEqual(result, expected, f"Failed to solve {cipher_type} cipher")

    def test_modern_cryptography(self):
        for challenge in CRYPTO_CHALLENGES['modern']:
            with self.subTest(challenge=challenge):
                encrypted_data = challenge['encrypted_data']
                encryption_type = challenge['encryption_type']
                key = challenge['key']
                expected = challenge['expected']
                result = self.crypto_solver.solve_modern(encrypted_data, encryption_type, key)
                self.assertEqual(result, expected, f"Failed to solve {encryption_type} encryption")

    def test_crypto_puzzles(self):
        for puzzle in CRYPTO_CHALLENGES['puzzles']:
            with self.subTest(puzzle=puzzle):
                puzzle_data = puzzle['puzzle_data']
                puzzle_type = puzzle['puzzle_type']
                expected = puzzle['expected']
                result = self.crypto_solver.solve_puzzle(puzzle_data, puzzle_type)
                self.assertEqual(result, expected, f"Failed to solve {puzzle_type} puzzle")

if __name__ == '__main__':
    unittest.main()