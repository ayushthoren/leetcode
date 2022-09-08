class Solution(object):
    def maximumProduct(self, nums):
      nums=sorted(nums)
      p1=nums[0]*nums[1]*nums[-1]
      p2=nums[-1]*nums[-2]*nums[-3]
      return max(p1,p2)
