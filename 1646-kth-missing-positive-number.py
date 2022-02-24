class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
      missing=[]
      for i in range(1, arr[-1]):
        if i not in arr: missing.append(i)
      if len(missing)<k: return arr[-1]+(k-len(missing))
      return missing[k-1]
