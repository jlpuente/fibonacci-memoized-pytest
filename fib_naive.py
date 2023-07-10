def fib(n):
    """
    Recursively computes the n-th term of the Fibonacci sequence.
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(38))
