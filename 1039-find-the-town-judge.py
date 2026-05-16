class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ppl = [0]*(n+1)
        for a, b in trust: ppl[a]-=1; ppl[b]+=1
        for i in range(1,n+1):
            if ppl[i]==n-1: return i
        return -1
