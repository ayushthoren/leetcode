class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g,s=sorted(g),sorted(s)
        p1,p2,ct=0,0,0
        while p1<len(g) and p2<len(s):
            if g[p1]<=s[p2]: ct+=1; p1+=1
            p2+=1
        return ct
