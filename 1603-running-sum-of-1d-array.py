class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=0
        new=[]
        for i in nums:
            s+=i
            new.append(s)
        return new
