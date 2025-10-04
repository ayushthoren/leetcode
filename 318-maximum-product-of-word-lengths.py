class Solution:
    def maxProduct(self, words: List[str]) -> int:
        m = 0
        for i, j in combinations(words, 2):
            if not set(i) & set(j): m = max(m, len(i) * len(j))
        return m
