class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=mx=0
        for n in nums: prev,mx=mx,max(mx,prev+n)
        return mx
