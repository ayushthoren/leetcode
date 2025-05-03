class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for f in range(len(fruits)):
            for b in range(len(baskets)):
                if baskets[b]>=fruits[f]: baskets.pop(b); break
        return len(baskets)
