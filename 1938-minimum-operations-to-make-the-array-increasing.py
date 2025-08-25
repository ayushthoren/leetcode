class Solution:
    def minOperations(self, nums: List[int]) -> int:
        o = p = 0
        for i in nums:
            if i <= p:
                p +=1
                o += p - i
            else:
                p = i
        return o
