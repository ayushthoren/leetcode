class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s=set()
        for i in arr:
            if 2*i in s or (i%2==0 and i//2 in s): return True
            s.add(i)
        return False
