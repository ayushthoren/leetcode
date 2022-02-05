class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      ct=0
      mxct=0
      for i in nums:
        if i==1: ct+=1
        else: ct=0
        if ct>mxct: mxct=ct
      return mxct
