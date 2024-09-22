class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        o=0
        for i in commands:
            if i=="UP": o-=n
            if i=="DOWN": o+=n
            if i=="LEFT": o-=1
            if i=="RIGHT": o+=1
        return o