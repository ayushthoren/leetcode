class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(d)*f for d,f in Counter(str(n)).items())
