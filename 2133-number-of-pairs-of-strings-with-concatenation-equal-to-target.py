class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ct=0
        numsl=len(nums)
        for i in range(numsl):
            for j in range(numsl):
                if nums[i]+nums[j]==target and i!=j: ct+=1
        return ct
