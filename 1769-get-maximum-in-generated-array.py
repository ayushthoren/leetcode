class Solution:
    def getMaximumGenerated(self, n: int) -> int:
      if n==0: return 0
      nums=[0,1]
      for i in range(n):
        if 2<=2*i<=n: nums.append(nums[i])
        if 2<=2*i+1<=n: nums.append(nums[i]+nums[i+1])
      return max(nums)
