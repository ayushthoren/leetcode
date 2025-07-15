class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((123-ord(s[i]))*(i+1) for i in range(len(s)))
