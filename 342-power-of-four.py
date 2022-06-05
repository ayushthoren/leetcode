class Solution:
    def isPowerOfFour(self, n: int) -> bool:
      if n<=0: return False
      while n>1:
        n/=4
        if not n.is_integer(): return False
      return True
