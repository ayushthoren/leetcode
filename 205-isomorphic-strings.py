class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      assignments={}
      alreadySet=[]
      for i in range(len(s)):
        if s[i] not in assignments:
          if t[i] not in alreadySet:
            alreadySet.append(t[i])
            assignments[s[i]]=t[i]
          else: return False
        if assignments[s[i]]!=t[i]: return False
      return True
