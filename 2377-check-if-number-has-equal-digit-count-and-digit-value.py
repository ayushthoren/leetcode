class Solution:
    def digitCount(self, num: str) -> bool:
      for i in range(len(num)):
        if not num.count(str(i))==int(num[i]): return False
      return True
