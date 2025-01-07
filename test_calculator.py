import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_add_negative_with_positive(self):
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_add_negative_with_negative(self):
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_add_zeros(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_negative_with_positive(self):
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_subtract_negative_with_negative(self):
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_subtract_zeros(self):
    def test_subtract_zeros(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)

    def test_factorial_of_zero(self):
        self.assertEqual(self.calc.factorial(0), 1)

    def test_factorial_of_negative(self):
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4)

    def test_square_root_of_zero(self):
        self.assertEqual(self.calc.square_root(0), 0)

    def test_square_root_of_negative(self):
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
        self.assertEqual(self.calc.subtract(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
