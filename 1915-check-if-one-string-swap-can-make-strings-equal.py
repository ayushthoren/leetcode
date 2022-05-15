class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
      if s1==s2: return True
      swap,swapTo=[],[]
      for i in range(len(s1)):
        if s1[i]!=s2[i]: swap.append(s1[i]); swapTo.append(s2[i])
      if len(swap)==2 and swap[0]==swapTo[1] and swap[1]==swapTo[0]: return True
      return False
