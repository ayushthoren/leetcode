class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=set(nums1).intersection(set(nums2))
        if i: return min(i)
        return -1
