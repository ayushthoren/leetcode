class Solution:
    def maxDepth(self, s: str) -> int:
        m, c = 0, 0
        for i in s:
            if i == "(": c += 1; m = max(m, c)
            if i == ")": c -=1
        return m
