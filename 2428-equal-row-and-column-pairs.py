class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ct=0
        for row in grid:
            for n in range(len(row)):
                col=[grid[i][n] for i in range(len(grid))]
                if row==col: ct+=1
        return ct
