class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[0 for i in range(n)] for j in range(m)]
        grid[0][0]=1
        for y in range(m):
            for x in range(n):
                if [x,y]!=[0,0]:
                    up,left=0,0
                    if y!=0: up=grid[y-1][x]
                    if x!=0: left=grid[y][x-1]
                    grid[y][x]=up+left
        return grid[m-1][n-1]