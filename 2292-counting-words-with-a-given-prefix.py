class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
      ct=0
      for i in words:
        if len(i)>=len(pref):
          if i[:len(pref)]==pref: ct+=1
      return ct
