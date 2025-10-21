class Solution(object):
    def countOperations(self, num1, num2):
        ct = 0
        while num1 != 0 and num2 != 0:
            if num1 < num2: num2 -= num1
            else: num1 -= num2
            ct += 1
        return ct
