class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "".join(["1" for o in range(s.count("1")-1)]+["0" for z in range(s.count("0"))])+"1"
