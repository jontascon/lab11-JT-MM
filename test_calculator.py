# https://github.com/jontascon/lab11-JT-MM
# Partner 1: Jon Tascon
# Partner 2: Jon Tascon
# Partner two is the same as one due to lack of response from Matthew Merrell.

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

    def test_multiply(self):
        self.assertEqual(calculator.mul(4, 3), 12)

    def test_divide(self):
        self.assertEqual(calculator.div(3, 3), 1)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -4)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)


if __name__ == "__main__":
    unittest.main()