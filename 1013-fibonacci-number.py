class Solution:
    def fib(self, n: int, i: int = 0, j: int = 1) -> int:
        return i if n==0 else self.fib(n-1, j, i+j)
