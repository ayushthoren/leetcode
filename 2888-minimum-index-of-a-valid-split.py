class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n=len(nums)
        c1,c2={},{}
        for e in nums: c2[e]=c2.get(e,0)+1; c1[e]=0
        for i in range(n):
            num=nums[i]
            c1[num]+=1
            c2[num]-=1
            if c1[num]*2>i+1 and c2[num]*2>n-i-1: return i
        return -1
