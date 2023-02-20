class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        val=0
        while nums:
            if len(nums)>1: val+=int(str(nums[0])+str(nums[-1])); del nums[0]; del nums[-1]
            else: val+=nums[0]; del nums[0]
        return val
