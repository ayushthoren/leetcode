class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cts,ctt={},{}
        steps=0
        for i in s:
            if i not in cts: cts[i]=0
            cts[i]+=1
        for j in t:
            if j not in ctt: ctt[j]=0
            ctt[j]+=1
        for k in cts:
            if k not in ctt: steps+=cts[k]
            else:
                tmp=cts[k]-ctt[k]
                if tmp>0: steps+=tmp
        return steps
