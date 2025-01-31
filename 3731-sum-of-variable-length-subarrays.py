class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        return sum([sum(nums[max(0,i-nums[i]):i+1]) for i in range(len(nums))])
