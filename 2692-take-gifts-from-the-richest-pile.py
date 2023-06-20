class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            maxx=0
            for j in range(len(gifts)):
                if gifts[j]>gifts[maxx]: maxx=j
            gifts[maxx]=math.floor(math.sqrt(gifts[maxx]))
        return sum(gifts)
