class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s=list(s)
        for i in range(len(s)):
            j=(i+1)*-1
            if s[i]!=s[j]:
                if ord(s[i])<ord(s[j]):s[j]=s[i]
                else: s[i]=s[j]
        return "".join(s)
