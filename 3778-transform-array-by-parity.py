class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        p=0
        for i in nums:
            if i%2==0: nums[p]=0; p+=1
        for j in range(p,len(nums)): nums[j]=1
        return nums
