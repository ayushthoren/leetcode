class Solution:
    def average(self, salary: List[int]) -> float:
      sLen=len(salary)
      if sLen<3: return 0
      return sum(sorted(salary)[1:sLen-1])/(sLen-2)
