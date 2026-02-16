class Solution:
    def mirrorDistance(self, n: int) -> int:
        t, r = n, 0
        while t: r *= 10; r += t % 10; t //= 10
        return abs(r - n)
