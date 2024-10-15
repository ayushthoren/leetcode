class Solution(object):
    def islandPerimeter(self, grid):
      perimiter=0
      sides=0
      for y in range(len(grid)):
        for x in range(len(grid[y])):
          if grid[y][x]==1:
            sides=4
            if y!=0 and grid[y-1][x]==1: sides-=1
            if y!=len(grid)-1 and grid[y+1][x]==1: sides-=1
            if x!=0 and grid[y][x-1]==1: sides-=1
            if x!=len(grid[y])-1 and grid[y][x+1]==1: sides-=1
            perimiter+=sides
        sides=0
      return perimiter