def memoize(f):
    """
    Recursively computes the n-th term of the Fibonacci sequence using a cache.
    Caching/memoization is an optimization technique that you can use in your
    applications to keep recent or often-used data in memory locations that
    are faster or computationally cheaper to access than their source.
    """
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def fib(n):
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(38))
