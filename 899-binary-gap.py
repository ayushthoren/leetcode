class Solution:
    def binaryGap(self, n: int) -> int:
      n=bin(n)[2:]
      if n.count("1")<2: return 0
      dist=0
      dists=[]
      for i in n:
        dist+=1
        if i=="1":
          dists.append(dist)
          dist=0
      return max(dists)
