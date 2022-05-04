class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
      cts=[0 for lol in range(101)]
      smaller=[]
      for i in nums: cts[i]+=1
      for j in range(len(nums)):
        smaller.append(sum(cts[:nums[j]]))
      return smaller
