class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
      firstX = coordinates[0][0]
      firstY = coordinates[0][1]
      run = coordinates[1][0]-coordinates[0][0]
      rise = coordinates[1][1]-coordinates[0][1]
      for i in range(1,len(coordinates)):
        print(coordinates[i][1], coordinates[i][0])
        if run*(coordinates[i][1]-firstY) != rise * (coordinates[i][0]-firstX): return False
      return True
