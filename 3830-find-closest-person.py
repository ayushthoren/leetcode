class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        o,t=abs(x-z),abs(y-z)
        return 1 if o<t else 2 if t<o else 0
