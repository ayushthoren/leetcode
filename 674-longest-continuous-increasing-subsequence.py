class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c, m = 1, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: c += 1
            else: m = max(c, m); c = 1
        return max(c, m)
