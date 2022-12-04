class Solution:
    def findGCD(self, nums: List[int]) -> int:
      a,b=min(nums),max(nums)
      while a%b>0:
        r=a%b
        a,b=b,r
      return b
