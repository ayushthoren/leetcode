class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
      import copy
      if len(nums)<3: return True
      increasing=False
      if nums[0]<=nums[-1]: 
        increasing=True
      tmp=copy.deepcopy(nums)
      if increasing:
        tmp=sorted(tmp)
        if tmp==nums: return True
      else:
        tmp=sorted(tmp, reverse=True)
        if tmp==nums: return True
      return False
