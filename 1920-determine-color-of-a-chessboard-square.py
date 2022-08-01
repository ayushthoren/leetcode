class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
      if ord(coordinates[0])%2==int(coordinates[1])%2: return False
      return True
