class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                possible=[]
                #possible paths
                if row>0: possible.append(grid[row-1][col])
                if col>0: possible.append(grid[row][col-1])
                #Find best path
                if possible: grid[row][col]=grid[row][col]+min(possible)
        return grid[-1][-1]
