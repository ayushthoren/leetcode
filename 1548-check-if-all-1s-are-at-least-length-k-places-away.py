class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
      dist=0
      dists=[]
      for i in nums:
        if i==0: dist+=1
        if i==1:
          dists.append(dist)
          dist=0
      for j in dists[1:]:
        if j<k: return False
      return True
