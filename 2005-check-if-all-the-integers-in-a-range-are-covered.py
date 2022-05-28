class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      allNums=[n for n in range(left, right+1)]
      for i in ranges:
        for r in range(i[0], i[1]+1):
          if r in allNums: allNums.remove(r)
      if allNums==[]: return True
      return False
