import unittest
from tst_function import is_prime

class PrimeTestCase(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))

    def test_negative_numbers(self):
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(-11))
        self.assertFalse(is_prime(-13))

if __name__ == '__main__':
    unittest.main()