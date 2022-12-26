class Solution(object):
    def findMaxK(self, nums):
        m=-1
        for i in [j for j in nums if j>0]:
            if i*-1 in nums and i>m: m=i
        return m
