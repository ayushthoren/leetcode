class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      ptr=0
      new=""
      w1l, w2l = len(word1), len(word2)
      while len(new)<w1l+w2l:
        if ptr<w1l: new+=word1[ptr]
        if ptr<w2l: new+=word2[ptr]
        ptr+=1
      return new
