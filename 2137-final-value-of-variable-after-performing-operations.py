class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        for i in operations:
            if "+" in i: x+=1
            else: x-=1
        return x
