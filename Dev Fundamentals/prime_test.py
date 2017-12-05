import unittest
from Class01 import is_prime

class PrimeTest(unittest.TestCase):
    def test_5_is_prime(self):
        self.assertTrue(is_prime(5))

    def test_4_is_prime(self):
        self.assertFalse(is_prime(4))
if __name__ == "__main__":
    unittest.main()
