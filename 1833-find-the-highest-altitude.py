class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts=[0]
        for i in gain: alts.append(alts[-1]+i)
        return max(alts)
