class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
      n=len(nums)
      maxDiff=-1
      for i in range(len(nums)):
        for j in range(len(nums)):
          if 0<=i<j<n and nums[i]<nums[j]:
            if nums[j]-nums[i]>maxDiff: maxDiff=nums[j]-nums[i]
      return maxDiff
