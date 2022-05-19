class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
      nums.sort()
      p1, p2 = 0, k - 1
      res = float("inf")
      while p2 < len(nums):
        res = min(res, nums[p2] - nums[p1])
        p1+=1
        p2+=1
      return res
