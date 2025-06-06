class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(nums[i+1]==(nums[i]+nums[i+2])*2 for i in range(len(nums)-2))
