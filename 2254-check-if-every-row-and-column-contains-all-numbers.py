class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
      nums=[i for i in range(1, len(matrix)+1)]
      for j in range(len(matrix)):
        if sorted(matrix[j])!=nums: return False
        if sorted([k[j] for k in matrix])!=nums: return False
      return True
