class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s
        z=[[] for row in range(numRows)]
        t,rebound=0,False
        for i in s:
            if t<numRows and not rebound:
                z[t].append(i)
                t+=1
                if t==numRows: rebound=True; t-=1
            else:
                t-=1
                z[t].append(i)
                if t==0: rebound=False; t+=1
        return "".join(["".join(j) for j in z])