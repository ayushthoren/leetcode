class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ls=len(s)
        t=l=o=z=0
        for r,b in enumerate(s):
            if b=="1": o+=1
            else: z+=1
            while o>k and z>k:
                if s[l]=="1": o-=1
                else: z-=1
                l+=1
            t+=r-l+1
        return t
