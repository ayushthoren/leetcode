class Solution:
    def minimumSum(self, num: int) -> int:
        num, a, b, t = map(int, sorted(str(num))), 0, 0, True
        for i in num:
            if t: a = (a * 10) + i; t = False
            else: b = (b * 10) + i; t = True
        return a + b
