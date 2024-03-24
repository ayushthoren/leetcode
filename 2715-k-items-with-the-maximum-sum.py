class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        s=0
        if numOnes>=k: return k
        s+=numOnes
        k-=numOnes
        if numZeros>=k: return s
        k-=numZeros
        return s-k
