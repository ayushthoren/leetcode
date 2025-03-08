class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m,w=float("inf"),0
        for r in range(len(blocks)):
            l=r-k+1
            if blocks[r]=="W": w+=1
            if l>=0:
                m=min(m,w)
                if blocks[l]=="W": w-=1
        return m
