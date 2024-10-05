class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for i in nums:
            if i not in counts: counts[i] = 1
            else: counts[i] += 1

        uniques = list(set(nums))
        new_sorted = sorted(uniques,key=lambda x: counts[x])[::-1]

        return new_sorted[:k]