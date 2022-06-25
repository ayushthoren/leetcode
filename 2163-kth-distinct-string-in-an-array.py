class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
      distinct=[]
      for i in arr:
        if arr.count(i)==1 and i not in distinct: distinct.append(i)
      if len(distinct)>=k: return distinct[k-1]
      return ""
