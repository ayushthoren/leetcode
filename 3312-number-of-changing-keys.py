class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.lower()
        last,ct=s[0],0
        for i in s:
            if i!=last: ct+=1
            last=i
        return ct
