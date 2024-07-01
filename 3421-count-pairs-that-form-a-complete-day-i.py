class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ct,ln=0,len(hours)
        for i in range(ln):
            for j in range(i+1,ln):
                if i!=j and (hours[i]+hours[j])%24==0: ct+=1
        return ct
