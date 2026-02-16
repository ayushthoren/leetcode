class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [[0 for x in range(n)] for y in range(m)]; a[0][0] = 1
        for y in range(m):
            for x in range(n):
                if y > 0: a[y][x] += a[y-1][x]
                if x > 0: a[y][x] += a[y][x-1]
        return a[-1][-1]
