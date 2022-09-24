class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
      if len(nums)==1: return sorted(nums[0])
      ints=set(nums[0]).intersection(set(nums[1]))
      for i in nums: ints=ints.intersection(set(i))
      return sorted(list(ints))
