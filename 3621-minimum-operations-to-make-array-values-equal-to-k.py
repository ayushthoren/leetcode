class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=set()
        for i in nums:
            if i<k: return -1
            elif i!=k: s.add(i)
        return len(s)
