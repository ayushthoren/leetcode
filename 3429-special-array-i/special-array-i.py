class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            p=(nums[i]%2)==(nums[i+1]%2)
            if p: return False
        return True