class Solution(object):
    def summaryRanges(self, nums):
      ranges=[]
      lastSplit=0
      for i in range(len(nums)):
        if i>0 and nums[i]!=nums[i-1]+1:
          ranges.append(nums[lastSplit:i])
          lastSplit=i
      if lastSplit<len(nums): ranges.append(nums[lastSplit:])
      for j in range(len(ranges)):
        if len(ranges[j])!=1:
          ranges[j]=str(ranges[j][0])+"->"+str(ranges[j][-1])
        else: ranges[j]=str(ranges[j][0])
      return ranges