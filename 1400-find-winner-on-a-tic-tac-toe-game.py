class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
      grid=[[0,0,0],[0,0,0],[0,0,0]]
      p="X"
      for i in moves:
        grid[i[0]][i[1]]=p
        if p=="X": p="O"
        else: p="X"

      def checkArr(arr):
        if arr.count("X")==3: return "A"
        if arr.count("O")==3: return "B"

      for j in range(3):
        if checkArr(grid[j]): return checkArr(grid[j])

        tmp=[grid[k][j] for k in range(3)]
        if checkArr(tmp): return checkArr(tmp)

      tmp=[grid[l][l] for l in range(3)]
      if checkArr(tmp): return checkArr(tmp)

      tmp=[grid[h][-(h+1)] for h in range(3)]
      if checkArr(tmp): return checkArr(tmp)

      for t in grid:
        for y in t:
          if y==0: return "Pending"

      return "Draw"
