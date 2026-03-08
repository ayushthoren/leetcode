class Solution:
    def countMonobit(self, n: int) -> int:
        c, x = 1, 1
        while x <= n: c += 1; x = x * 2 + 1
        return c
