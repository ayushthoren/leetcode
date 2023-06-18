class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices=sorted(prices)
        after=money-(prices[0]+prices[1])
        if after<0: return money
        return after
