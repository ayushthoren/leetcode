class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
      mat = [[0 for i in range(n)] for j in range(m)]
      for k in indices:
        mat[k[0]]=[l+1 for l in mat[k[0]]]
        for h in mat: h[k[1]]+=1
      oddCt=0
      for y in mat:
        for u in y:
          if u%2==1: oddCt+=1
      return oddCt
