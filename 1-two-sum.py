class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            n=target-nums[i]
            if n in h: return [i,h[n]]
            h[nums[i]]=i
        return []
