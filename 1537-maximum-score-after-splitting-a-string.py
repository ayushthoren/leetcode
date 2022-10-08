class Solution:
    def maxScore(self, s: str) -> int:
      maxScore=0
      for i in range(1,len(s)):
        tmp=s[:i].count("0")+s[i:].count("1")
        if tmp>maxScore: maxScore=tmp
      return maxScore
