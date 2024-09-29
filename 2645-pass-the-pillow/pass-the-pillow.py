class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds,left=time//(n-1),time%(n-1)
        if rounds%2==0: return left+1
        return n-left