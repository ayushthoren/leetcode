class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, r = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < b: b = prices[i]
            elif prices[i] - b > r: r = prices[i] - b
        return r
