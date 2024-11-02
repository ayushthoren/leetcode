class Solution:
    def possibleStringCount(self, word: str) -> int:
        ct,p=1,""
        for i in word:
            if i==p: ct+=1
            p=i
        return ct
