class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
      chrIdxs=[]
      dists=[]
      for i in range(len(s)):
        if s[i]==c: chrIdxs.append(i)

      for j in range(len(s)):
        minDist=len(s)
        for k in chrIdxs:
          if abs(k-j)<minDist: minDist=abs(k-j)
        dists.append(minDist)
      return dists
