class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        sb,gb=bin(start)[2:],bin(goal)[2:]
        sl,gl=len(sb),len(gb)
        if sl<gl: sb="0"*(gl-sl)+sb
        if gl<sl: gb="0"*(sl-gl)+gb
        m=0
        print(sb,gb)
        for i in range(len(sb)):
            if sb[i]!=gb[i]: m+=1
        return m
