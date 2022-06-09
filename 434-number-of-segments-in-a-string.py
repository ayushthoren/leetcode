class Solution:
    def countSegments(self, s: str) -> int:
      ct=0
      isWord=False
      for i in s:
        if i == " ":
            if isWord: ct+=1; isWord=False
        else: isWord=True
      if isWord: return ct+1
      return ct
