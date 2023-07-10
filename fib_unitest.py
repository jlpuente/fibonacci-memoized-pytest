import unittest

import fib_iterative
import fib_naive
import fib_memo


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
