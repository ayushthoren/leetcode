class Solution:
    def binaryGap(self, n: int) -> int:
      n=bin(n)[2:]
      if n.count("1")<2: return 0
      dist=0
      maxDist=0
      for i in n:
        dist+=1
        if i=="1":
          if dist>maxDist: maxDist=dist
          dist=0
      return maxDist
