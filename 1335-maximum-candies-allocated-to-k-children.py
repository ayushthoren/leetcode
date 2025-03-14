class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l,r=0,max(candies)
        while l<r:
            m=(l+r+1)//2
            if sum(p//m for p in candies)>=k: l=m
            else: r=m-1
        return l
