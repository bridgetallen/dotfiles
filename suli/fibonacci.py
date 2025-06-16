from functools import lru_cache
import sys

# Increase string digit limit for large integers
sys.set_int_max_str_digits(1_000_000)

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

def fib_fast_doubling(n):
    def helper(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = helper(n // 2)
            c = a * (2 * b - a)
            d = a * a + b * b
            return (c, d) if n % 2 == 0 else (d, c + d)
    return helper(n)[0]

# Example use
fib_num = fib_fast_doubling(1_000_000)
print(f"The 1,000,000th Fibonacci number has {len(str(fib_num))} digits.")
print(f"First 20 digits: {str(fib_num)[:20]}")

