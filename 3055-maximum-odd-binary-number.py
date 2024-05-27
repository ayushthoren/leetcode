class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "".join(["1"]*(s.count("1")-1)+["0"]*(s.count("0")))+"1"
