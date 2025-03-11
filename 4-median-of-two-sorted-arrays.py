class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)
        p1=p2=0
        def next():
            nonlocal p1, p2
            if p1<m and p2<n:
                if nums1[p1]<nums2[p2]: o=nums1[p1]; p1+=1
                else: o=nums2[p2]; p2+=1
            elif p1==m: o=nums2[p2]; p2+=1
            else: o=nums1[p1]; p1+=1
            return o
        if (m+n)%2==0:
            for _ in range((m+n)//2-1): next()
            return (next()+next())/2
        for _ in range((m+n)//2): next()
        return next()
