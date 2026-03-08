class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if y == 0 and x == 0: continue
                elif y == 0: grid[y][x] += grid[y][x-1]
                elif x == 0: grid[y][x] += grid[y-1][x]
                else: grid[y][x] += min(grid[y][x-1], grid[y-1][x])
        return grid[-1][-1]
