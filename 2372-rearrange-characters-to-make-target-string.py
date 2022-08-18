class Solution(object):
    def rearrangeCharacters(self, s, target):
      sCts={}
      tCts={}
      for sl in s:
        if sl not in sCts: sCts[sl]=0
        sCts[sl]+=1
      for tl in target:
        if tl not in tCts: tCts[tl]=0
        tCts[tl]+=1
      ct=float("inf")
      for i in tCts:
        if i not in sCts or tCts[i]>sCts[i]: return 0
        d=sCts[i]//tCts[i]
        if d<ct: ct=d
      return ct
