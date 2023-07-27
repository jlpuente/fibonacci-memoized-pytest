import unittest

import fib_iterative
import fib_naive
import fib_memo

"""
Note: A testcase is created by subclassing unittest.TestCase.
The nine individual tests are defined with methods whose names start with the letters test
and they are in three classes of three methods. 
This naming convention informs the test runner about which methods represent tests.
No matter how many classes there are. The naming convention is able to find the tests
thanks to the name convention.
- Usage mode: enter 'fib_unitest.py' in a terminal in the same directory as this test script.
"""


class TestFibonacciIterative(unittest.TestCase):

    def test_fibonacci_1_is_1(self):
        self.assertEqual(fib_iterative.fib(1), 1)

    def test_fibonacci_9_is_34(self):
        self.assertEqual(fib_iterative.fib(9), 34)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fib_iterative.fib(-1)


class TestFibonacciNaive(unittest.TestCase):

    def test_fibonacci_1_is_1(self):
        self.assertEqual(fib_naive.fib(1), 1)

    def test_fibonacci_9_is_34(self):
        self.assertEqual(fib_naive.fib(9), 34)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fib_naive.fib(-1)


class TestFibonacciMemoized(unittest.TestCase):

    def test_fibonacci_1_is_1(self):
        self.assertEqual(fib_memo.fib(1), 1)

    def test_fibonacci_9_is_34(self):
        self.assertEqual(fib_memo.fib(9), 34)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fib_memo.fib(-1)


if __name__ == '__main__':
    unittest.main()
