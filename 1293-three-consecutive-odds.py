class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ct=0
        for i in arr:
            if i%2==1: ct+=1
            else: ct=0
            if ct==3: return True
        return False
