class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(-i if i%m==0 else i for i in range(1,n+1))
