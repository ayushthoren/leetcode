class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        m=-1
        for i in range(-1,len(nums)-1):
            m=max(m,abs(nums[i]-nums[i+1]))
        return m
