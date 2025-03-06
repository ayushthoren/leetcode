class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ct={}
        for y in grid:
            for x in y:
                ct[x]=ct.get(x,0)+1
        a,b=0,0
        for i in range(1,(len(grid)**2)+1):
            if ct.get(i,0)==2: a=i
            elif ct.get(i,0)==0: b=i
        return [a,b]
