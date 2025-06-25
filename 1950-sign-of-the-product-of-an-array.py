class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 1
        for i in nums:
            if i == 0: return 0
            if i < 0: s = -s
        return s
