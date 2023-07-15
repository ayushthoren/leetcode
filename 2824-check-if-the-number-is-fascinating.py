class Solution:
    def isFascinating(self, n: int) -> bool:
        new=str(n)+str(n*2)+str(n*3)
        return len(set((new)))==len(new) and "0" not in new
