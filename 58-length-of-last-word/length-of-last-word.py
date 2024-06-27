class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([i for i in s.split(" ") if i!=""][-1])