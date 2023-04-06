class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        n=bin(n)[2:][::-1]
        eo=[0,0]
        for i in range(len(n)):
            if n[i]=="1":
                if i%2==0: eo[0]+=1
                else: eo[1]+=1
        return eo
