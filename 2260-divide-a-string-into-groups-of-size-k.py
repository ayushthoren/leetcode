class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        pt,c,out=0,"",[]
        for i in s:
            c+=i
            pt+=1
            if pt==k: out.append(c); pt,c=0,""
        if c:
            for j in range(k-len(c)): c+=fill
            out.append(c)
        return out
