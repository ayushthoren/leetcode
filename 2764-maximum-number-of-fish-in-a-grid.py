class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        stack,cts=[],[]
        
        def checkAdjacent(x,y):
            water=[]
            if x>0 and grid[y][x-1]>0: water.append([x-1,y])
            if y>0 and grid[y-1][x]>0: water.append([x,y-1])
            if x<n-1 and grid[y][x+1]>0:water.append([x+1,y])
            if y<m-1 and grid[y+1][x]>0:water.append([x,y+1])
            return water

        for y in range(m):
            for x in range(n):
                if grid[y][x]>0:
                    stack.append([x,y])
                    cts.append(0)
                    while stack:
                        adj=checkAdjacent(stack[-1][0],stack[-1][1])
                        cts[-1]+=grid[stack[-1][1]][stack[-1][0]]
                        grid[stack[-1][1]][stack[-1][0]]=0
                        stack.pop(-1)
                        stack.extend(adj)
        
        try: return max(cts)
        except: return 0
