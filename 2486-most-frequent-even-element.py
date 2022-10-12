class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
      nums=[e for e in sorted(nums) if e%2==0]
      maxCt=0
      mins=[]
      for i in nums:
        iCt=nums.count(i)
        if iCt>maxCt:
          maxCt=iCt
          mins=[i]
        if iCt==maxCt:
          mins.append(i)
      if len(mins)==0: return -1
      return min(mins)
