class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        m, o = 0, ""
        for i in range(len(s)):
            c = set()
            for j in range(i, len(s)):
                c.add(s[j])
                n = all(k.swapcase() in c for k in c)
                l = j - i + 1
                if n and l > m: m, o = l, s[i:j+1]
        return o
