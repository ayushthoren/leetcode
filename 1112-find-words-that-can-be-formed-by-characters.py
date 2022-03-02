class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
      lens=0
      for i in words:
        canBeSpelled=True
        for j in i:
          if chars.count(j)<i.count(j): canBeSpelled=False
        if canBeSpelled: lens+=len(i)
      return lens
