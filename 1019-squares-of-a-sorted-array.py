class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      new=[0 for j in nums]
      p1, p2, p3 = 0, len(nums)-1, len(nums)-1
      while p3>=0:
        if abs(nums[p1])<abs(nums[p2]):
          new[p3]=nums[p2]**2
          p3-=1
          p2-=1
        elif abs(nums[p2])<abs(nums[p1]):
          new[p3]=nums[p1]**2
          p3-=1
          p1+=1
        else:
          new[p3]=nums[p1]**2
          p3-=1
          p1+=1
      return new
