class Solution(object):
    def checkXMatrix(self, grid):
      for y in range(len(grid)):
        for x in range(len(grid[0])):
          if x == y or y == (len(grid[y])-x)-1:
            if grid[y][x] == 0:
              print(x, y)
              print("cross")
              return False
          else:
            if grid[y][x] != 0:
              print(grid[y][x])
              print("other")
              return False
      return True
