class Solution:
    def alternateDigitSum(self, n: int) -> int:
        r=0
        for i in range(len(str(n))):
            if i%2==0: r+=int(str(n)[i])
            else: r-=int(str(n)[i])
        return r
