import unittest
from fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):

    def test_nthvalue(self):
        fibonacci = Fibonacci()
        self.assertEqual(
            fibonacci.nthvalue(1), 0, "should give 0 as the value for the 1th term in fibonacci series")
        self.assertEqual(
            fibonacci.nthvalue(2), 1, "should give 1 as the value for the 2th term in fibonacci series")
        self.assertEqual(
            fibonacci.nthvalue(3), 1, "should give 1 as the value for the 3th term in fibonacci series")
        self.assertEqual(
            fibonacci.nthvalue(4), 2, "should give 2 as the value for the 4th term in fibonacci series")
        self.assertEqual(
            fibonacci.nthvalue(5), 3, "should give 4 as the value for the 5th term in fibonacci series")
        self.assertEqual(
            fibonacci.nthvalue(6), 5, "should give 5 as the value for the 6th term in fibonacci series")
        self.assertEqual(
            fibonacci.nthvalue(7), 8, "should give 8 as the value for the 7th term in fibonacci series")

        with self.assertRaises(ValueError):
            fibonacci.nthvalue(0)

    def test_series(self):
        fibonacci = Fibonacci()
        self.assertEqual(fibonacci.series(
            1), [0], "should give a list with first 1 terms of fibonacci series")
        self.assertEqual(fibonacci.series(
            2), [0, 1], "should give a list with first 1 terms of fibonacci series")
        self.assertEqual(fibonacci.series(
            3), [0, 1, 1], "should give a list with first 1 terms of fibonacci series")
        self.assertEqual(fibonacci.series(
            4), [0, 1, 1, 2], "should give a list with first 1 terms of fibonacci series")
        with self.assertRaises(ValueError):
            fibonacci.series(0)


if __name__ == "__main__":
    unittest.main()
