class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=sorted(nums1+nums2)
        ln=len(nums3)
        d=ln//2
        if ln%2==0: return (nums3[d]+nums3[d-1])/2
        return nums3[d]
