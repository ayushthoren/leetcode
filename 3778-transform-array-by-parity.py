class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        e=sum(i%2==0 for i in nums)
        nums[:e],nums[e:]=[0]*e,[1]*(len(nums)-e)
        return nums
