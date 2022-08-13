class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
      all=set(nums1+nums2+nums3)
      arrCt=0
      toot=[]
      for i in all:
        arrCt=0
        if i in nums1: arrCt+=1
        if i in nums2: arrCt+=1
        if i in nums3: arrCt+=1
        if arrCt>=2: toot.append(i)
      return toot
