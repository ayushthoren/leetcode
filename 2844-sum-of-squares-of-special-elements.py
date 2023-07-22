class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ln,s=len(nums),0
        for i in range(1,ln+1):
            if ln%i==0: s+=nums[i-1]**2
        return s
