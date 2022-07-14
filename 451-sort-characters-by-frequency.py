class Solution:
    def frequencySort(self, s: str) -> str:
      chrCts={}
      sorted_s = sorted(s)
      for i in s:
        if i in chrCts: chrCts[i]+=1
        else: chrCts[i]=1
      new = sorted(sorted_s,key=lambda x: chrCts[x])
      return "".join(new[::-1])
