class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return n**2 if n**2*w<=maxWeight else maxWeight//w
