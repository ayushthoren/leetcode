class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        inBoth=[]
        for i in nums1:
            if i in nums2: inBoth.append(i)
        if inBoth: return sorted(inBoth)[0]
        return int("".join(sorted([str(sorted(nums1)[0]),str(sorted(nums2)[0])])))
