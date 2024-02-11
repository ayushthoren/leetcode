class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.lower()
        prev,ct=s[0],0
        for i in s:
            if i!=prev:ct+=1
            prev=i
        return ct
