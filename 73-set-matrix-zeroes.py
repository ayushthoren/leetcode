class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        r,c=[False]*m,[False]*n
        for y in range(m):
            for x in range(n):
                if matrix[y][x]==0: r[y],c[x]=True,True
        for y in range(m):
            for x in range(n):
                if r[y] or c[x]: matrix[y][x]=0
