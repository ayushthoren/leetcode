class Solution:
    def longestPalindrome(self, s: str) -> int:
        cts,t,odd={},0,False
        for i in s: cts[i]=cts.get(i,0)+1
        for j in cts.values():
            if j%2==0: t+=j
            else: t+=j-1; odd=True
        return t+1 if odd else t
