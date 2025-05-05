class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        c,d=0,n**2
        while maxWeight-w>=0 and c<d: maxWeight-=w; c+=1
        return c
