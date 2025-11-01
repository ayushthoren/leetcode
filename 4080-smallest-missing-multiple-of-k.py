class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s, i = set(nums), 0
        while True:
            i += k
            if i not in s: return i
