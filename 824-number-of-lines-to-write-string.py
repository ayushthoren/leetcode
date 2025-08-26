class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        l, w = 1, 0
        for i in s:
            t = widths[ord(i) - 97]
            if w + t > 100: l += 1; w = t
            else: w += t
        return l, w
