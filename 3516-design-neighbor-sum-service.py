class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid=grid
        self.n=len(grid)

    def adjacentSum(self, value: int) -> int:
        tmp=0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x]==value:
                    if y-1>=0: tmp+=self.grid[y-1][x]
                    if y+1<=self.n-1: tmp+=self.grid[y+1][x]
                    if x-1>=0: tmp+=self.grid[y][x-1]
                    if x+1<=self.n-1: tmp+=self.grid[y][x+1]
        return tmp

    def diagonalSum(self, value: int) -> int:
        tmp=0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x]==value:
                    if y-1>=0 and x-1>=0: tmp+=self.grid[y-1][x-1]
                    if y+1<=self.n-1 and x+1<=self.n-1: tmp+=self.grid[y+1][x+1]
                    if y-1>=0 and x+1<=self.n-1: tmp+=self.grid[y-1][x+1]
                    if y+1<=self.n-1 and x-1>=0: tmp+=self.grid[y+1][x-1]
        print(tmp)
        return tmp
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
