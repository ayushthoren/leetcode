class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate=[k for k in licensePlate.lower() if k.isalpha()]
        shortest=None
        for i in words:
            good=True
            for l in licensePlate:
                if licensePlate.count(l)>i.count(l): good=False
            if good:
                if not shortest or len(i)<len(shortest): shortest=i
        return shortest
