class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        k = k % (len(grid) * len(grid[0]))
        for _ in range(k):
            for i in range(len(grid)): grid[i] = [grid[i-1].pop()] + grid[i]
        return grid
