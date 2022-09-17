class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set([i for i in set(nums1) if i in set(nums2)]+[j for j in set(nums2) if j in set(nums1)]))
