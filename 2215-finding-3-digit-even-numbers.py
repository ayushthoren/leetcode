class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ct,o=Counter(digits),[]
        for i in range(100,1000,2):
            f,s,t=i%10,(i//10)%10,i//100
            ct[f]-=1; ct[s]-=1; ct[t]-=1
            if ct[f]>=0 and ct[s]>=0 and ct[t]>=0: o.append(i)
            ct[f]+=1; ct[s]+=1; ct[t]+=1
        return o
