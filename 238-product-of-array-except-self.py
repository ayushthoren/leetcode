class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln=len(nums)
        l,r,out=1,1,[1]*ln
        for i in range(ln):
            out[i]*=l; l*=nums[i]
        for j in reversed(range(ln)):
            out[j]*=r; r*=nums[j]
        return out
