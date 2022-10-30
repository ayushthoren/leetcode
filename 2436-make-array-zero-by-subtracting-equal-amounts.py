class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
      nLen=len(nums)
      ops=0
      while sum(nums)>0:
        print(nums)
        nMin=min([j for j in nums if j>0])
        for i in range(nLen):
          if nums[i]>0: nums[i]=nums[i]-nMin
        ops+=1
      return ops
