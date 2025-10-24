class Solution:
    def minElement(self, nums: List[int]) -> int:
        m = float("inf")
        for n in nums:
            t = 0
            while n > 0: t += n % 10; n //= 10
            m = min(m, t)
        return m
