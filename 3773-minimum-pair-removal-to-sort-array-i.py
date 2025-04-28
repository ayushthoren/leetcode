class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops,good=0,False
        while not good:
            m,j,good=float("inf"),False,True
            for i in range(len(nums)-1):
                s=nums[i]+nums[i+1]
                if s<m: m,j=s,i
                if nums[i]>nums[i+1]: good=False
            if (j or j==0) and not good: nums[j]+=nums.pop(j+1); ops+=1
        return ops
