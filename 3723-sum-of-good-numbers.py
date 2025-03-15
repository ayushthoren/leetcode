class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ln,s=len(nums),0
        for i in range(ln):
            good=True
            if i-k>=0 and not nums[i]>nums[i-k]: good=False
            if i+k<ln and not nums[i]>nums[i+k]: good=False
            if good: s+=nums[i]
        return s
