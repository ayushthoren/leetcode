class Solution:
    def checkString(self, s: str) -> bool:
        return len(s.split("b")[0])==s.count("a")
