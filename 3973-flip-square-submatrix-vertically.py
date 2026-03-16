class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        t, b = x, x + k - 1
        while t < b:
            for i in range(k):
                tmp = grid[b][y+i]
                grid[b][y+i] = grid[t][y+i]; grid[t][y+i] = tmp
            t += 1; b -= 1
        return grid
