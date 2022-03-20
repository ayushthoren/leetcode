class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
      arr.sort()
      cts={}
      for i in arr:
        ct=bin(i).count("1")
        if ct not in cts: cts[ct]=[]
        cts[ct].append(i)
      sortCts=sorted(cts)
      return [k for j in sortCts for k in cts[j]]
