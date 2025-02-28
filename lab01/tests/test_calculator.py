import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sum_two_ints(self):
        self.assertEqual(self.calculator.add(-4, 10), 6)

    def test_sum_two_ints_negative(self):
        self.assertNotEqual(self.calculator.add(4, 8), 2)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
