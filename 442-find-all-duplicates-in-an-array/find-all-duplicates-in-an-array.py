class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
      cts={}
      for i in nums:
        if i not in cts: cts[i]=0
        cts[i]+=1
      return [j for j in cts if cts[j]>1]