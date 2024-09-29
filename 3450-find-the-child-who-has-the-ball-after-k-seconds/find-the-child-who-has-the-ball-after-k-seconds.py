class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        i,d=0,1
        for j in range(k):
            if i==n-1: d=-1
            if i==0: d=1
            i+=d
        return i