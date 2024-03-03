class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        pts,new=[list(range(i[0],i[1]+1)) for i in nums],[]
        for i in pts: new+=i
        return len(set(new))
