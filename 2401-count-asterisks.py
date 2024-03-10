class Solution:
    def countAsterisks(self, s: str) -> int:
        vb,ct=False,0
        for i in s:
            if i=="|": vb=not vb
            if not vb and i=="*": ct+=1
        return ct
