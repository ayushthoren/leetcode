class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      a=list(set(nums1).intersection(nums2))
      new = []
      for i in a:
        for j in range(min([nums1.count(i), nums2.count(i)])): new.append(i)
      return new