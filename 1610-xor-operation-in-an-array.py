class Solution(object):
    def xorOperation(self, n, start):
      nums=[start+2*i for i in range(n)]
      x=nums[0]
      for j in range(1,len(nums)): x^=nums[j]
      return x
