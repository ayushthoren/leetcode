class Solution:
    def sortColors(self, nums: List[int]) -> None:
      clrCts={0:0,1:0,2:0}
      alrDone=0
      for i in nums:
        clrCts[i]=nums.count(i)
      for j in clrCts:
        for k in range(clrCts[j]):
          nums[alrDone]=j; alrDone+=1
      return nums