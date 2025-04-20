class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cts,t={},0
        for i in answers:
            if i==0: t+=1
            elif i in cts and cts[i]>0: cts[i]-=1
            else: t+=i+1; cts[i]=i
        return t
