class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ct,l,t=0,0,0
        for r in range(len(nums)):
            t+=nums[r]
            while l<=r and t*(r-l+1)>=k: t-=nums[l]; l+=1
            ct+=r-l+1
        return ct
