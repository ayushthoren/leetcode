class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
      for i in paths:
        hasNext=False
        for j in paths:
          if i[1]==j[0]: hasNext=True
        if not hasNext: return i[1]
