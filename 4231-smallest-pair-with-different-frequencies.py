class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        nums.sort(); c = Counter(nums)
        f, n = list(c.values()), c.keys()
        for i, x in enumerate(n):
            for j, y in enumerate(n):
                if i < j and f[i] != f[j]: return [x, y]
        return [-1, -1]
