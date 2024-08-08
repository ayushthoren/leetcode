class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s,d=[],[]
        for i in nums:
            if i<10: s.append(i)
            else: d.append(i)
        return sum(s)!=sum(d)
