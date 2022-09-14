class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
      new=[]
      for i in range(len(nums)):
        new.insert(index[i],nums[i])
      return new
