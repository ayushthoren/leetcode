class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        ok=k
        ps={p:False for p in range(1,n+1)}
        c=1
        while not ps[c]:
            ps[c]=True
            c+=k
            k+=ok
            while c>n: c-=n
        return [i for i in ps if ps[i]==False]
