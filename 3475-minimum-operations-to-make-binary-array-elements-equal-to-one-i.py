class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ct=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                nums[i]^=1; nums[i+1]^=1; nums[i+2]^=1
                ct+=1
        return ct if nums[-1]==1 and nums[-2]==1 else -1
