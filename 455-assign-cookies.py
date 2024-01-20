class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g,s=sorted(g),sorted(s)
        ct=0
        for i in g:
            for j in range(len(s)):
                if s[j]>=i: s[j]=0; ct+=1; break
        return ct
