class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([1 for i in stones if i in jewels])
