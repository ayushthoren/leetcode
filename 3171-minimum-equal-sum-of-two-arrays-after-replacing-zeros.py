class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1,s2=sum(i if i!=0 else 1 for i in nums1),sum(j if j!=0 else 1 for j in nums2)
        if (s1>s2 and 0 in nums2) or s1==s2: return s1
        if s2>s1 and 0 in nums1: return s2
        return -1
