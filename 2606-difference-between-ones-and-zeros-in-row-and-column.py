class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        d=grid.copy()
        c=[[grid[y][x] for y in range(m)] for x in range(n)]
        co,cz=[k.count(1) for k in c],[l.count(0) for l in c]
        ro,rz=[p.count(1) for p in grid],[q.count(0) for q in grid]
        for i in range(m):
            for j in range(n): d[i][j]=ro[i]+co[j]-rz[i]-cz[j]
        return d
