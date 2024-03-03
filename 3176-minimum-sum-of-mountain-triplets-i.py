class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minsum=-1
        ln=len(nums)
        for i in range(ln):
            for j in range(i,ln):
                for k in range(j,ln):
                    if nums[i]<nums[j] and nums[k]<nums[j]:
                        mtsum=nums[i]+nums[j]+nums[k]
                        if minsum==-1 or mtsum<minsum: minsum=mtsum
        return minsum
