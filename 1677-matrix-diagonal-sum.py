class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
      summ=0
      l=len(mat)
      for i in range(l):
        summ+=mat[i][i]
        summ+=mat[i][-(i+1)]
      return summ-mat[l//2][l//2] if l%2==1 else summ
