class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
      for i in range(len(nums)-1):
        si=nums[i]+nums[i+1]
        for j in range(len(nums)-1):
          sj=nums[j]+nums[j+1]
          if i!=j and si==sj: return True
      return False
