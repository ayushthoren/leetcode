class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
      new=[[0 for xg in range(len(matrix))] for yg in range(len(matrix[0]))]
      for y in range(len(matrix)):
        for x in range(len(matrix[0])):
          new[x][y]=matrix[y][x]
      return new
