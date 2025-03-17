class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cts={}
        for i in nums: cts[i]=cts.get(i,0)+1
        for j in cts:
            if cts[j]%2==1: return False
        return True
