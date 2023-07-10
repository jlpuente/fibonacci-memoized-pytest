# Time performance comparison for 3 Fibonacci sequence implementations

| Fibonacci              | Execution time per loop for F(38) |
|------------------------|-----------------------------------|
| Iterative              | 1.14 us (4 833 333x faster)       |
| Naive                  | 5.51 s (reference)                |
| Memoization (of Naive) | 59.3 ns (92 917 369x faster)      |

**Iterative**:

`python -m timeit -r 10 -s "import fib_iterative" "fib_iterative.fi
b(38)"`

200000 loops, best of 10: 1.14 usec per loop

**Naive**:

`python -m timeit -r 10 -s "import fib_recursive" "fib_recursive.fib(38)"`

1 loop, best of 10: 5.51 sec per loop

**Memoization (of Naive)**:

`python -m timeit -r 10 -s "import fib_memo" "fib_memo.fib(38)"`

5000000 loops, best of 10: 59.3 nsec per loop

The 38-th Fibonacci term is 39088169.