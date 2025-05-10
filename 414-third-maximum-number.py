class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f,s,t=None,None,None
        for i in nums:
            if i==f or i==s or i==t: continue
            if not f or i>f: f,s,t=i,f,s
            elif not s or i>s: s,t=i,s
            elif not t or i>t: t=i
        print(f,s,t)
        return t if t!=None else f
