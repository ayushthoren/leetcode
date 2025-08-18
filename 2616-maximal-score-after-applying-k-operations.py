class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        s, h = 0, [-n for n in sorted(nums, reverse = True)[:k]]
        for _ in range(k): m = heapq.heappop(h); s -= m; heapq.heappush(h, m // 3)
        return s
