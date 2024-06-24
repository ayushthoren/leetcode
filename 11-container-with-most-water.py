class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1,p2=0,len(height)-1
        ma=0
        while p1<p2:
            a=min(height[p1],height[p2])*(p2-p1)
            if a>ma: ma=a
            if height[p1]<height[p2]: p1+=1
            else: p2-=1
        return ma
