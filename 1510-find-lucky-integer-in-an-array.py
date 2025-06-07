class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max(k for k,v in (Counter(arr)|{-1:-1}).items() if k==v)
