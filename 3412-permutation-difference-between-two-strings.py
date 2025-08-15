class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs({s[i]: i for i in range(len(s))}[t[j]]-j) for j in range(len(t)))
