import copy
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
      correct=copy.deepcopy(heights)
      correct.sort()
      ct=0
      for i in range(len(heights)):
        if heights[i]!=correct[i]: ct+=1
      return ct
