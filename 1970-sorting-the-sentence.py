class Solution:
    def sortSentence(self, s: str) -> str:
      s=s.split(" ")
      idxs={}
      for i in s:
        idxs[int(i[-1])]=i[0:-1]
      return " ".join([idxs[j] for j in range(1,len(s)+1)])
