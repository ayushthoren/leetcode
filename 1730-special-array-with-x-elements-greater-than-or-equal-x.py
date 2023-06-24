class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(max(nums)+1):
            ct=0
            for j in nums:
                if j>=i: ct+=1
            if ct==i: return i
        return -1
