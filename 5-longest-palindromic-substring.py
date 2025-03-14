class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls=len(s)
        for length in range(ls,0,-1):
            for l in range(ls-length+1):
                r=l+length-1
                p1,p2,valid=l,r,True
                while p1<p2:
                    if s[p1]==s[p2]: p1+=1; p2-=1
                    else: valid=False; break
                if valid: return s[l:r+1]
        return ""
