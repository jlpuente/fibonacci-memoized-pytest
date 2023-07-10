def fib(n):
    """
    Iteratively computes the n-th term of the Fibonacci sequence.
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n < 2:
        return n
    nth_2 = nth_1 = 1
    for i in range(n-2):
        fib = nth_2 + nth_1
        nth_2 = nth_1
        nth_1 = fib
    return fib


print(fib(38))
