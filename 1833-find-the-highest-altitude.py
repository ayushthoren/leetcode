class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts,ma=[0],0
        for i in gain:
            alts.append(alts[-1]+i)
            if alts[-1]>ma: ma=alts[-1]
        return ma
