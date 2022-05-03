class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
      halfLen=len(nums)//2
      for i in nums:
        if nums.count(i)==halfLen: return i
