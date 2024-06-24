class Solution:
    def reverse(self, x: int) -> int:
        n=-1 if x<0 else 1
        x=int(str(abs(x))[::-1])*n
        return x if -2147483648<x<2147483647 else 0