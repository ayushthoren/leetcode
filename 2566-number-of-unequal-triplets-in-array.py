class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ct=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i<j<k and nums[i]!=nums[j] and nums[i]!=nums[k] and nums[j]!=nums[k]: ct+=1
        return ct
