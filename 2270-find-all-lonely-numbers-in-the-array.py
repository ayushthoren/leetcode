class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
      cts={}
      numSet=set()
      for i in nums:
        if i not in cts: cts[i]=0
        cts[i]+=1
        numSet.add(i)
      return [j for j in cts if cts[j]<2 and j-1 not in numSet and j+1 not in numSet]
