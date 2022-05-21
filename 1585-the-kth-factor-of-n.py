class Solution:
    def kthFactor(self, n: int, k: int) -> int:
      factors=[i for i in range(1,n+1) if n%i==0]
      if k<=len(factors): return factors[k-1]
      return -1
