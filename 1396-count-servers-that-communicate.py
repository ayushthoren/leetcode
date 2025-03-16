class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        rc,cc,ans=[0]*m,[0]*n,0
        for y in range(m):
            for x in range(n):
                if grid[y][x]: rc[y]+=1; cc[x]+=1
        for y in range(m):
            for x in range(n):
                if grid[y][x] and (rc[y]>1 or cc[x]>1): ans+=1
        return ans
