from functools import lru_cache


class Fibonacci:
    @staticmethod
    @lru_cache(maxsize=5)
    def nthvalue(n):
        if n <= 0:
            raise ValueError('Value of n cannot be zero!')
        return n-1 if n <= 2 else Fibonacci.nthvalue(n - 1) + Fibonacci.nthvalue(n - 2)

    @staticmethod
    def series(n):
        if n <= 0:
            raise ValueError('Value of n cannot be zero!')
        return [Fibonacci.nthvalue(i+1) for i in range(n)]
