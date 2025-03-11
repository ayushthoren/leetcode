class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last,ct={"a":-1,"b":-1,"c":-1},0
        for i in range(len(s)):
            last[s[i]]=i
            ct+=1+min(last.values())
        return ct
