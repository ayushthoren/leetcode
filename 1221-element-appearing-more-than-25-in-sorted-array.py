class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
      cts={}
      for i in arr:
        if i not in cts: cts[i]=0
        cts[i]+=1
      return list(cts.keys())[list(cts.values()).index(max(cts.values()))]
