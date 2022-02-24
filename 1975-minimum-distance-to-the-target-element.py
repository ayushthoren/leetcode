class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
      dists=[]
      for i in range(len(nums)):
        if nums[i]==target: dists.append(abs(i-start))
      return min(dists)
