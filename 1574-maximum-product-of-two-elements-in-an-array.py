class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f = s = 0
        for i in nums:
            if i > f: s, f = f, i
            elif i > s: s = i
        return (f - 1) * (s - 1)
