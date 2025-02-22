class Solution:
    def maxDifference(self, s: str) -> int:
        o,e=[],[]
        for i in set(s):
            f=s.count(i)
            if f%2==0: e.append(f)
            else: o.append(f)
        return max(o)-min(e)
