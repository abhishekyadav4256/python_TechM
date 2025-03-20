import unittest
from unittest import mock
import math

def square_root(num):
    """Function that returns the square root of a number."""
    return math.sqrt(num)

class TestMathMocking(unittest.TestCase):
    @mock.patch('math.sqrt', return_value=100)  # Mocking math.sqrt
    def test_mocked_sqrt(self, mock_sqrt):
        result = square_root(25)  # This should return 100 instead of 5
        self.assertEqual(result, 100)  # Check if mocked value is returned

if __name__ == '__main__':
    unittest.main()
