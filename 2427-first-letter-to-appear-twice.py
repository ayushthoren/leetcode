class Solution:
    def repeatedCharacter(self, s: str) -> str:
      seen=[]
      for i in s:
        if i in seen: return i
        seen.append(i)
