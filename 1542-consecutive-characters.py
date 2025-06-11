class Solution:
    def maxPower(self, s: str) -> int:
        c,m,l=0,1,""
        for i in s:
            m=max(m,c)
            if i!=l: c,l=0,i
            c+=1
        return max(m,c)
