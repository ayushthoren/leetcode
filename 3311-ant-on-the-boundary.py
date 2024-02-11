class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos,ct=0,0
        for i in nums:
            pos+=i
            if pos==0: ct+=1
        return ct
