class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for y in range(2):
            for x in range(2):
                square=[grid[y][x], grid[y][x+1], grid[y+1][x], grid[y+1][x+1]]
                if square.count("B")>=3 or square.count("W")>=3: return True
        return False
