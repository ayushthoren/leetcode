class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
      lucky=[]
      for row in matrix:
        rowMin=min(row)
        for i in range(len(row)):
          if row[i]==rowMin:
            if row[i]==max([r[i] for r in matrix]):
              lucky.append(row[i])
      return lucky
