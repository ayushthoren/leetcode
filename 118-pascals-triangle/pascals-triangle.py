def pascalRow(prevRow):
  new=[prevRow[0]]
  for i in range(len(prevRow)-1):
    new.append(prevRow[i]+prevRow[i+1])
  new.append(prevRow[-1])
  return new

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      r1 = [[1]]
      r2 = [[1], [1, 1]]
      if numRows == 1: return r1
      elif numRows == 2: return r2
      res = r2
      for i in range(3, numRows+1):
        res.append(pascalRow(res[i - 2]))
      return res