class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(n+1):
            if sum(range(1,x+1))==sum(range(x,n+1)): return x
        return -1
