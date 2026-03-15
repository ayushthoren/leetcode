class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        l, m = -1, float("inf")
        for i in range(len(capacity)):
            if itemSize <= capacity[i] < m: l, m = i, capacity[i]
        return l
