class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            s=target-nums[i]
            if s in nums:
                j=nums.index(s)
                if j!=i: return [i,j]
