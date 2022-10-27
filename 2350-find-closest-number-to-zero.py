class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
      first=nums[0]
      for i in nums:
        if abs(i)<abs(first): first=i
        if abs(i)==abs(first) and i>first: first=i
      return first
