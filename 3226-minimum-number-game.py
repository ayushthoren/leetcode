class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums, arr = sorted(nums), []
        for i in range(0, len(nums), 2): arr.append(nums[i+1]); arr.append(nums[i])
        return arr
