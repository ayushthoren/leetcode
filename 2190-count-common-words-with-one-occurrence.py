class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
      ct=0
      for i in words1:
        if words1.count(i)==1 and words2.count(i)==1: ct+=1
      return ct
