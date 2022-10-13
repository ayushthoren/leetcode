def threeByThree(mat,r1,r2,c1,c2):
  h = mat[r1][c1]
  for i in range(r1,r2+1):
    for j in range(c1,c2+1):
      if mat[i][j]>h: h=mat[i][j]
  return h

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
      gLen=len(grid[0])
      new=[[0 for gx in range(gLen-2)] for gy in range(gLen-2)]
      for y in range(gLen):
        for x in range(gLen):
          if y+2<gLen and x+2<gLen:
            new[y][x]=threeByThree(grid,y,y+2,x,x+2)
      return new
