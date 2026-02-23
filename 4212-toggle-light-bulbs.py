class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        m = 0
        for b in bulbs: m ^= 1 << b
        return [i for i in range(101) if (m >> i) & 1]
