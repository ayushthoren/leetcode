class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n=len(grid)
        stronger=[0 for s in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1: stronger[j]+=1
        for k in range(n):
            if stronger[k]==0: return k
