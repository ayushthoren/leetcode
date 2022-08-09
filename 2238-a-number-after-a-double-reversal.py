class Solution(object):
    def isSameAfterReversals(self, num):
        return int(str(int(str(num)[::-1]))[::-1])==num
