class Solution:
    def isPowerOfThree(self, n: int) -> bool:
      while n>=3:
        d=n/3
        if not d.is_integer(): return False
        n=int(d)
      if n==1: return True
      return False