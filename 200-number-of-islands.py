class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        stack,ct=[],0
        
        def checkAdjacent(x,y):
            land=[]
            if x>0 and grid[y][x-1]=="1": land.append([x-1,y])
            if y>0 and grid[y-1][x]=="1": land.append([x,y-1])
            if x<n-1 and grid[y][x+1]=="1":land.append([x+1,y])
            if y<m-1 and grid[y+1][x]=="1":land.append([x,y+1])
            return land

        for y in range(m):
            for x in range(n):
                if grid[y][x]=="1":
                    stack.append([x,y])
                    while stack:
                        adj=checkAdjacent(stack[-1][0],stack[-1][1])
                        grid[stack[-1][1]][stack[-1][0]]="0"
                        stack.pop(-1)
                        stack.extend(adj)
                    ct+=1
                    
        return ct
