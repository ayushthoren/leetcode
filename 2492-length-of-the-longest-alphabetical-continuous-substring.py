class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        p1=0
        p2=1
        l=1
        while p2<len(s):
            if ord(s[p2-1])==ord(s[p2])-1: l=max(l,(p2-p1)+1)
            else: p1=p2
            p2+=1
        return l
