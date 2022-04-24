import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
      heapq.heapify(nums)
      for i in range(k):
        nums[0]*=-1
        heapq.heapify(nums)
      return sum(nums)
