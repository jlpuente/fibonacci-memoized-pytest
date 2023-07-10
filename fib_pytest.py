import pytest
import fib_iterative
import fib_naive
import fib_memo


def test_fibonacci_iterative_1_is_1():
    assert fib_iterative.fib(1) == 1


def test_fibonacci_iterative_9_is_34():
    assert fib_iterative.fib(9) == 34


def test_fibonacci_iterative_negative():
    with pytest.raises(ValueError):
        fib_naive.fib(-1)


def test_fibonacci_naive_1_is_1():
    assert fib_naive.fib(1) == 1


def test_fibonacci_naive_9_is_34():
    assert fib_naive.fib(9) == 34


def test_fibonacci_naive_negative():
    with pytest.raises(ValueError):
        fib_naive.fib(-1)


def test_fibonacci_memo_1_is_1():
    assert fib_memo.fib(1) == 1


def test_fibonacci_memo_9_is_34():
    assert fib_memo.fib(9) == 34


def test_fibonacci_memo_negative():
    with pytest.raises(ValueError):
        fib_memo.fib(-1)
