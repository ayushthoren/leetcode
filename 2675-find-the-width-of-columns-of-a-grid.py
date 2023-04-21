class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        lens=[0 for s in range(len(grid[0]))]
        for i in grid:
            for j in range(len(i)):
                lenj=len(str(i[j]))
                if lenj>lens[j]: lens[j]=lenj
        return lens
