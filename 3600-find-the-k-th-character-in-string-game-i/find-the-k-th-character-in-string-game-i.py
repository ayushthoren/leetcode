class Solution:
    def kthCharacter(self, k: int) -> str:
        if k==1: return "a"
        l,s=2,"ab"
        while l<k:
            tmp=list(s)
            for i in range(l):
                c=ord(tmp[i])
                if c==122: c=96
                tmp[i]=chr(c+1)
            s+="".join(tmp)
            l+=l
        return s[k-1]