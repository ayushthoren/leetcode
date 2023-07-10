class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l!=r:
            m=(l+r)//2
            if nums[m]==target: return m
            if target<nums[m]: r-=1
            else: l+=1
        if nums[l]==target: return l
        return -1
